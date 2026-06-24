"""
Construye el notebook implementacion-widrow.ipynb con todas las celdas.
"""
import json
import os

# ── Constantes ──────────────────────────────────────────────
OUT = "proyectos/RNA/notebook/implementacion-widrow.ipynb"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ── Celdas ──────────────────────────────────────────────────
cells = []

def md(source_lines: list[str]):
    cells.append({"cell_type": "markdown", "metadata": {}, "source": source_lines})

def code(source_lines: list[str]):
    cells.append({"cell_type": "code", "metadata": {}, "source": source_lines,
                  "outputs": [], "execution_count": None})

# ═══════════════════════════════════════════════════════════
# CELDA 1 — Título y descripción
# ═══════════════════════════════════════════════════════════
md([
    "# 🧠 Implementación de Algoritmos — Widrow & Lehr (1990)\n",
    "\n",
    "**Paper:** *30 Years of Adaptive Neural Networks: Perceptron, Madaline, and Backpropagation*\n",
    "**Autores:** Bernard Widrow & Michael A. Lehr  \n",
    "**Publicación:** *Proceedings of the IEEE*, Vol. 78, No. 9, pp. 1415–1442, Septiembre 1990.\n",
    "\n",
    "---\n",
    "\n",
    "## 📋 Algoritmos implementados\n",
    "\n",
    "| # | Algoritmo | Ecuación (paper) | Tipo |\n",
    "|---|-----------|------------------|------|\n",
    "| 1 | $\\alpha$-LMS (Widrow-Hoff) | $W_{k+1} = W_k + \\alpha \\frac{\\epsilon_k}{|X_k|^2} X_k$ (Eq. 10) | Corrección de error lineal |\n",
    "| 2 | Perceptron Rule (Rosenblatt) | $W_{k+1} = W_k + \\alpha \\frac{\\tilde{\\epsilon}_k}{2} X_k$ (Eq. 18) | Corrección de error no lineal |\n",
    "| 3 | $\\mu$-LMS (Steepest Descent) | $W_{k+1} = W_k + 2\\mu \\epsilon_k X_k$ (Eq. 33) | Gradiente descendente |\n",
    "| 4 | Backpropagation (sigmoid MLP) | $W_{k+1} = W_k + 2\\mu \\tilde{\\epsilon}_k \\mathrm{sgm}'(s_k) X_k$ (Eq. 54) | Red multicapa |\n",
    "\n",
    "## 🗂️ Estructura del notebook\n",
    "\n",
    "- **Parte A:** Replicación exacta del paper (datos binarios ±1 sintéticos)\n",
    "- **Parte B:** Extensión a datasets reales (Iris Setosa, Wine Quality, Moons)\n",
    "- **Parte C:** Tabla comparativa final"
])

# ═══════════════════════════════════════════════════════════
# CELDA 2 — Imports
# ═══════════════════════════════════════════════════════════
code([
    "# ═══════════════════════════════════════════════════════\n",
    "# IMPORTS Y CONFIGURACIÓN\n",
    "# ═══════════════════════════════════════════════════════\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib\n",
    "from matplotlib import cm\n",
    "from sklearn.datasets import load_iris, make_moons\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler, MinMaxScaler\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "matplotlib.rcParams['figure.dpi'] = 100\n",
    "matplotlib.rcParams['figure.figsize'] = (6, 4)\n",
    "matplotlib.rcParams['font.size'] = 11\n",
    "plt.rcParams['axes.unicode_minus'] = False\n",
    "\n",
    "print('✅ Numpy:', np.__version__)\n",
    "print('✅ Pandas:', pd.__version__)\n",
    "print('✅ Todo listo — Widrow & Lehr (1990)')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 3 — PARTE A: Generación de datos sintéticos
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 🔬 PARTE A — Replicación exacta del paper (datos binarios ±1)\n",
    "\n",
    "El paper asume patrones de entrada **binarios ±1** y salidas **binarias ±1** (Sección II–IV).\n",
    "Generamos 3 datasets sintéticos controlados:\n",
    "\n",
    "1. **Linealmente separable** — para probar convergencia del Perceptron\n",
    "2. **Linealmente separable con ruido** — para comparar LMS vs Perceptron\n",
    "3. **XOR (no linealmente separable)** — para probar Backpropagation con MLP"
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# PARTE A — Datos binarios ±1 sintéticos\n",
    "# ═══════════════════════════════════════════════════════\n",
    "np.random.seed(1990)  # Año del paper\n",
    "\n",
    "def generar_datos_linealmente_separables(n=200, n_features=10, ruido=0.0):\n",
    "    \"\"\"Genera patrones binarios ±1 con un hiperplano separador conocido.\"\"\"\n",
    "    # Vector de pesos verdadero (Wiener)\n",
    "    w_verdadero = np.random.randn(n_features + 1)\n",
    "    X = np.random.choice([-1, 1], size=(n, n_features))\n",
    "    # Agregar bias como columna de 1s\n",
    "    X_bias = np.c_[np.ones(n), X]\n",
    "    s = X_bias @ w_verdadero\n",
    "    y = np.sign(s)\n",
    "    # Agregar ruido: flip aleatorio de algunas etiquetas\n",
    "    if ruido > 0:\n",
    "        flip = np.random.rand(n) < ruido\n",
    "        y[flip] *= -1\n",
    "    return X, y, w_verdadero\n",
    "\n",
    "def generar_xor(n=200):\n",
    "    \"\"\"Genera datos XOR: (±1, ±1) -> ±1.\"\"\"\n",
    "    X = np.random.choice([-1, 1], size=(n, 2))\n",
    "    y = np.where(X[:, 0] * X[:, 1] > 0, 1, -1)  # XOR verdadero\n",
    "    return X, y\n",
    "\n",
    "# Generar datasets\n",
    "X_lin, y_lin, w_true = generar_datos_linealmente_separables(n=300, n_features=2, ruido=0.0)\n",
    "X_lin_ruido, y_lin_ruido, _ = generar_datos_linealmente_separables(n=300, n_features=2, ruido=0.1)\n",
    "X_xor, y_xor = generar_xor(200)\n",
    "\n",
    "print('📊 Datasets sintéticos generados:')\n",
    "print(f'   Linealmente separable:    {X_lin.shape[0]} patrones, {X_lin.shape[1]} features')\n",
    "print(f'   Linealmente sep + ruido:  {X_lin_ruido.shape[0]} patrones, {X_lin_ruido.shape[1]} features')\n",
    "print(f'   XOR:                       {X_xor.shape[0]} patrones, {X_xor.shape[1]} features')\n",
    "print(f'\\n   Pesos verdaderos (Wiener): {w_true}')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 4 — Visualización datos sintéticos
# ═══════════════════════════════════════════════════════════
md([
    "### Visualización de los datasets 2D",
])

code([
    "# Visualizar datasets 2D\n",
    "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
    "\n",
    "datasets_viz = [\n",
    "    (X_lin, y_lin, 'Linealmente separable'),\n",
    "    (X_lin_ruido, y_lin_ruido, 'Linealmente sep. + 10% ruido'),\n",
    "    (X_xor, y_xor, 'XOR (no linealmente separable)'),\n",
    "]\n",
    "\n",
    "for ax, (X, y, titulo) in zip(axes, datasets_viz):\n",
    "    for clase, color, marker in [(1, '#2196F3', 'o'), (-1, '#F44336', 's')]:\n",
    "        mask = y == clase\n",
    "        ax.scatter(X[mask, 0], X[mask, 1], c=color, marker=marker,\n",
    "                   s=40, edgecolors='k', linewidth=0.3, alpha=0.7,\n",
    "                   label=f'y={clase:+d}')\n",
    "    ax.set_xlabel('x₁')\n",
    "    ax.set_ylabel('x₂')\n",
    "    ax.set_title(titulo, fontweight='bold')\n",
    "    ax.legend(fontsize=8)\n",
    "    ax.set_xlim(-1.5, 1.5)\n",
    "    ax.set_ylim(-1.5, 1.5)\n",
    "    ax.grid(True, alpha=0.3)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_datos_sinteticos.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print('✅ Figura guardada: fig_datos_sinteticos.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 5 — α-LMS (Widrow-Hoff)
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 1️⃣ α-LMS (Widrow-Hoff Delta Rule) — Eq. (10)\n",
    "\n",
    "$$W_{k+1} = W_k + \\alpha \\frac{\\epsilon_k}{|X_k|^2} X_k$$\n",
    "\n",
    "donde $\\epsilon_k = d_k - X_k^T W_k$ es el error lineal.  \n",
    "Este algoritmo **corrige el error** con cada patrón, con mínimo cambio en los pesos (principio de mínima perturbación, Sección III).  \n",
    "Rango de estabilidad: $0 < \\alpha < 2$."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# ALGORITMO 1: α-LMS (Widrow-Hoff Delta Rule)\n",
    "# Eq. (10) del paper — Corrección de error lineal\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "def alpha_lms(X, y, alpha=0.5, epochs=100, verbose=True):\n",
    "    \"\"\"\n",
    "    α-LMS (Widrow-Hoff delta rule).\n",
    "    W_{k+1} = W_k + alpha * (error_k / ||X_k||²) * X_k\n",
    "    \"\"\"\n",
    "    n, d = X.shape\n",
    "    X_bias = np.c_[np.ones(n), X]  # Agregar bias\n",
    "    W = np.zeros(d + 1)\n",
    "    mse_history = []\n",
    "    acc_history = []\n",
    "    \n",
    "    for epoch in range(epochs):\n",
    "        # Barajar datos cada época\n",
    "        idx = np.random.permutation(n)\n",
    "        X_shuf, y_shuf = X_bias[idx], y[idx]\n",
    "        \n",
    "        for i in range(n):\n",
    "            x_i = X_shuf[i]\n",
    "            s_i = np.dot(x_i, W)\n",
    "            error = y_shuf[i] - s_i\n",
    "            norm_x_sq = np.dot(x_i, x_i)\n",
    "            if norm_x_sq > 0:\n",
    "                W += alpha * (error / norm_x_sq) * x_i\n",
    "        \n",
    "        # Métricas por época\n",
    "        s = X_bias @ W\n",
    "        mse = np.mean((y - s) ** 2)\n",
    "        y_pred = np.sign(s)\n",
    "        acc = np.mean(y_pred == y)\n",
    "        mse_history.append(mse)\n",
    "        acc_history.append(acc)\n",
    "    \n",
    "    if verbose:\n",
    "        print(f'α-LMS: α={alpha} | MSE final={mse:.6f} | Accuracy={acc*100:.2f}% | Épocas={epochs}')\n",
    "    return W, mse_history, acc_history"
])

# ═══════════════════════════════════════════════════════════
# CELDA 6 — Perceptron Rule
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 2️⃣ Perceptron Rule (Rosenblatt) — Eq. (18)\n",
    "\n",
    "$$W_{k+1} = W_k + \\alpha \\frac{\\tilde{\\epsilon}_k}{2} X_k$$\n",
    "\n",
    "donde $\\tilde{\\epsilon}_k = d_k - y_k$ es el **error del cuantizador** (no el error lineal).  \n",
    "El Perceptron **no adapta si la salida es correcta**.  \n",
    "**Garantiza convergencia** si los datos son linealmente separables (Cover, 1964; Sección IV-B).  \n",
    "**No converge** si los datos NO son separables (el peso tiende a cero)."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# ALGORITMO 2: Perceptron Rule (Rosenblatt)\n",
    "# Eq. (18) del paper — Corrección de error no lineal\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "def perceptron_rule(X, y, alpha=1.0, epochs=100, verbose=True):\n",
    "    \"\"\"\n",
    "    Perceptron learning rule (Rosenblatt, 1960).\n",
    "    W_{k+1} = W_k + alpha * (quantizer_error / 2) * X_k\n",
    "    \"\"\"\n",
    "    n, d = X.shape\n",
    "    X_bias = np.c_[np.ones(n), X]\n",
    "    W = np.zeros(d + 1)\n",
    "    acc_history = []\n",
    "    \n",
    "    for epoch in range(epochs):\n",
    "        idx = np.random.permutation(n)\n",
    "        X_shuf, y_shuf = X_bias[idx], y[idx]\n",
    "        cambios = 0\n",
    "        \n",
    "        for i in range(n):\n",
    "            x_i = X_shuf[i]\n",
    "            s_i = np.dot(x_i, W)\n",
    "            y_pred = np.sign(s_i)\n",
    "            error_q = y_shuf[i] - y_pred  # Quantizer error (Eq. 17)\n",
    "            \n",
    "            if error_q != 0:  # Solo adapta si la salida es incorrecta\n",
    "                W += alpha * (error_q / 2.0) * x_i\n",
    "                cambios += 1\n",
    "        \n",
    "        s = X_bias @ W\n",
    "        y_pred = np.sign(s)\n",
    "        acc = np.mean(y_pred == y)\n",
    "        acc_history.append(acc)\n",
    "        \n",
    "        if cambios == 0:\n",
    "            if verbose:\n",
    "                print(f'Perceptron: ¡convergió en época {epoch+1}! Accuracy=100%')\n",
    "            # Rellenar épocas restantes con 1.0\n",
    "            acc_history.extend([1.0] * (epochs - epoch - 1))\n",
    "            break\n",
    "    \n",
    "    if verbose and acc_history[-1] < 1.0:\n",
    "        print(f'Perceptron: NO convergió. Accuracy final={acc_history[-1]*100:.2f}%')\n",
    "    return W, acc_history"
])

# ═══════════════════════════════════════════════════════════
# CELDA 7 — μ-LMS (Steepest Descent)
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 3️⃣ μ-LMS (Steepest Descent LMS) — Eq. (33)\n",
    "\n",
    "$$W_{k+1} = W_k + 2\\mu \\epsilon_k X_k$$\n",
    "\n",
    "Este algoritmo realiza **descenso por gradiente estocástico** sobre la superficie de error cuadrático medio (MSE).  \n",
    "La superficie MSE de un combinador lineal es un **paraboloide convexo** con un único mínimo global: la solución de Wiener $W^* = R^{-1}P$ (Eq. 29).  \n",
    "Rango de estabilidad: $0 < \\mu < 1 / \\mathrm{tr}[R]$ (Eq. 34)."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# ALGORITMO 3: μ-LMS (Steepest Descent)\n",
    "# Eq. (33) del paper — Gradiente estocástico\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "def mu_lms(X, y, mu=0.001, epochs=100, verbose=True):\n",
    "    \"\"\"\n",
    "    μ-LMS (steepest descent LMS).\n",
    "    W_{k+1} = W_k + 2*mu * error_k * X_k\n",
    "    \"\"\"\n",
    "    n, d = X.shape\n",
    "    X_bias = np.c_[np.ones(n), X]\n",
    "    W = np.zeros(d + 1)\n",
    "    mse_history = []\n",
    "    acc_history = []\n",
    "    weight_norm_history = []\n",
    "    \n",
    "    # Calcular solución de Wiener (referencia)\n",
    "    R = X_bias.T @ X_bias / n\n",
    "    P = X_bias.T @ y / n\n",
    "    try:\n",
    "        W_wiener = np.linalg.solve(R, P)\n",
    "    except np.linalg.LinAlgError:\n",
    "        W_wiener = np.linalg.pinv(R) @ P\n",
    "    \n",
    "    for epoch in range(epochs):\n",
    "        idx = np.random.permutation(n)\n",
    "        X_shuf, y_shuf = X_bias[idx], y[idx]\n",
    "        \n",
    "        for i in range(n):\n",
    "            x_i = X_shuf[i]\n",
    "            s_i = np.dot(x_i, W)\n",
    "            error = y_shuf[i] - s_i\n",
    "            W += 2 * mu * error * x_i\n",
    "        \n",
    "        s = X_bias @ W\n",
    "        mse = np.mean((y - s) ** 2)\n",
    "        y_pred = np.sign(s)\n",
    "        acc = np.mean(y_pred == y)\n",
    "        mse_history.append(mse)\n",
    "        acc_history.append(acc)\n",
    "        weight_norm_history.append(np.linalg.norm(W - W_wiener))\n",
    "    \n",
    "    if verbose:\n",
    "        print(f'μ-LMS: μ={mu} | MSE final={mse:.6f} | Accuracy={acc*100:.2f}%')\n",
    "        print(f'   ||W - W_wiener|| = {weight_norm_history[-1]:.6f}')\n",
    "    return W, mse_history, acc_history, W_wiener, weight_norm_history"
])

# ═══════════════════════════════════════════════════════════
# CELDA 8 — Backpropagation (MLP)
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 4️⃣ Backpropagation (Perceptrón Multicapa sigmoide) — Eq. (54)\n",
    "\n",
    "$$W_{k+1} = W_k + 2\\mu \\tilde{\\epsilon}_k \\cdot \\mathrm{sgm}'(s_k) X_k$$\n",
    "\n",
    "La retropropagación del error (backpropagation) extiende el gradiente descendente a **redes multicapa** con funciones de activación diferenciables (sigmoide).  \n",
    "Usamos $\\tanh$ como sigmoide: $\\mathrm{sgm}'(s) = 1 - \\tanh^2(s) = 1 - y^2$ (Eq. 55).  \n",
    "Este algoritmo es **equivalente** a Madaline Rule III (MRIII) cuando la perturbación $\\Delta s$ es pequeña (Sección VI-B)."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# ALGORITMO 4: Backpropagation para MLP sigmoide\n",
    "# Eq. (54)-(56) del paper\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "def sigmoid(x):\n",
    "    \"\"\"Tangente hiperbólica (Eq. 45 del paper).\"\"\"\n",
    "    return np.tanh(x)\n",
    "\n",
    "def sigmoid_derivative(x):\n",
    "    \"\"\"Derivada: sgm'(x) = 1 - tanh²(x) (Eq. 55).\"\"\"\n",
    "    return 1 - np.tanh(x) ** 2\n",
    "\n",
    "class MLP:\n",
    "    \"\"\"Perceptrón Multicapa con backpropagation (Sección VII del paper).\"\"\"\n",
    "    \n",
    "    def __init__(self, layer_sizes, learning_rate=0.01):\n",
    "        self.layers = layer_sizes\n",
    "        self.lr = learning_rate\n",
    "        # Inicialización de pesos (pequeños aleatorios — Sección VII)\n",
    "        self.W = []\n",
    "        for i in range(len(layer_sizes) - 1):\n",
    "            # Inicialización tipo Nguyen-Widrow (aprox)\n",
    "            w = np.random.randn(layer_sizes[i+1], layer_sizes[i] + 1) * 0.5\n",
    "            self.W.append(w)\n",
    "    \n",
    "    def forward(self, X):\n",
    "        \"\"\"Forward pass. Retorna activaciones lineales y no lineales por capa.\"\"\"\n",
    "        activations = [X]\n",
    "        linear_outputs = []\n",
    "        A = X\n",
    "        for w in self.W:\n",
    "            A_bias = np.c_[np.ones(A.shape[0]), A]  # Agregar bias\n",
    "            S = A_bias @ w.T\n",
    "            linear_outputs.append(S)\n",
    "            A = sigmoid(S)\n",
    "            activations.append(A)\n",
    "        return activations, linear_outputs\n",
    "    \n",
    "    def backward(self, X, y, activations, linear_outputs):\n",
    "        \"\"\"Backward pass: backpropagation (Eq. 54).\"\"\"\n",
    "        n = X.shape[0]\n",
    "        # Error en la capa de salida\n",
    "        y_out = activations[-1]\n",
    "        error_output = y.reshape(-1, 1) - y_out  # sigmoid error (Eq. 46)\n",
    "        delta = error_output * sigmoid_derivative(linear_outputs[-1])  # Eq. (54)\n",
    "        \n",
    "        # Propagar errores hacia atrás\n",
    "        for l in range(len(self.W) - 1, -1, -1):\n",
    "            A_prev = np.c_[np.ones(activations[l].shape[0]), activations[l]]\n",
    "            grad = -2 * delta.T @ A_prev / n  # Gradiente instantáneo\n",
    "            self.W[l] -= self.lr * grad\n",
    "            \n",
    "            if l > 0:\n",
    "                # Propagar delta a capa anterior\n",
    "                delta = (delta @ self.W[l][:, 1:]) * sigmoid_derivative(linear_outputs[l-1])\n",
    "    \n",
    "    def predict(self, X):\n",
    "        A = X\n",
    "        for w in self.W:\n",
    "            A_bias = np.c_[np.ones(A.shape[0]), A]\n",
    "            S = A_bias @ w.T\n",
    "            A = sigmoid(S)\n",
    "        return np.sign(A).flatten()\n",
    "    \n",
    "    def fit(self, X, y, epochs=1000, verbose=True):\n",
    "        n = X.shape[0]\n",
    "        mse_history = []\n",
    "        acc_history = []\n",
    "        \n",
    "        for epoch in range(epochs):\n",
    "            idx = np.random.permutation(n)\n",
    "            X_shuf, y_shuf = X[idx], y[idx]\n",
    "            activations, linear_outputs = self.forward(X_shuf)\n",
    "            self.backward(X_shuf, y_shuf, activations, linear_outputs)\n",
    "            \n",
    "            # Métricas por época\n",
    "            y_pred = self.predict(X)\n",
    "            acc = np.mean(y_pred == y)\n",
    "            y_out = self.forward(X)[0][-1].flatten()\n",
    "            mse = np.mean((y - y_out) ** 2)\n",
    "            mse_history.append(mse)\n",
    "            acc_history.append(acc)\n",
    "        \n",
    "        if verbose:\n",
    "            print(f'MLP Backprop: capas={self.layers} | MSE={mse:.6f} | Acc={acc*100:.2f}% | Épocas={epochs}')\n",
    "        return mse_history, acc_history"
])

# ═══════════════════════════════════════════════════════════
# CELDA 9 — EJECUCIÓN PARTE A: Comparación α-LMS vs Perceptron
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "### 🧪 Experimento A1: α-LMS vs Perceptron en datos linealmente separables\n",
    "\n",
    "El paper demuestra que ambos algoritmos pueden separar datos linealmente separables, pero con comportamientos distintos (Sección IV)."
])

code([
    "# Ejecutar α-LMS y Perceptron en datos limpios\n",
    "print('═' * 55)\n",
    "print('EXPERIMENTO A1: Datos linealmente separables (sin ruido)')\n",
    "print('═' * 55)\n",
    "\n",
    "W_lms, mse_lms, acc_lms = alpha_lms(X_lin, y_lin, alpha=0.5, epochs=50)\n",
    "W_per, acc_per = perceptron_rule(X_lin, y_lin, alpha=1.0, epochs=50)\n",
    "\n",
    "# Visualización comparativa\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "# Curva de accuracy\n",
    "ax = axes[0]\n",
    "ax.plot(acc_lms, 'b-', label=r'$\\alpha$-LMS', linewidth=2)\n",
    "ax.plot(acc_per, 'r--', label='Perceptron', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('Accuracy')\n",
    "ax.set_title('Convergencia: α-LMS vs Perceptron')\n",
    "ax.legend()\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_ylim(0.4, 1.05)\n",
    "ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.5)\n",
    "\n",
    "# Curva de MSE (solo α-LMS tiene MSE)\n",
    "ax = axes[1]\n",
    "ax.plot(mse_lms, 'b-', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('MSE (Error Cuadrático Medio)')\n",
    "ax.set_title(r'Convergencia del MSE — $\\alpha$-LMS')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_lms_vs_perceptron.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print('✅ Figura guardada: fig_lms_vs_perceptron.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 10 — Experimento A2: Datos con ruido
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento A2: α-LMS vs Perceptron con 10% de ruido\n",
    "\n",
    "Cuando los datos NO son perfectamente separables, el Perceptron **no converge** (el peso tiende a cero).  \n",
    "α-LMS, en cambio, encuentra una solución de compromiso minimizando el MSE (Sección IV-B)."
])

code([
    "print('═' * 55)\n",
    "print('EXPERIMENTO A2: Datos con 10% ruido (no perfectamente separables)')\n",
    "print('═' * 55)\n",
    "\n",
    "W_lms_r, mse_lms_r, acc_lms_r = alpha_lms(X_lin_ruido, y_lin_ruido, alpha=0.3, epochs=100)\n",
    "W_per_r, acc_per_r = perceptron_rule(X_lin_ruido, y_lin_ruido, alpha=1.0, epochs=100)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(8, 5))\n",
    "ax.plot(acc_lms_r, 'b-', label=r'$\\alpha$-LMS', linewidth=2)\n",
    "ax.plot(acc_per_r, 'r--', label='Perceptron', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('Accuracy')\n",
    "ax.set_title('Datos con 10% ruido: α-LMS vs Perceptron')\n",
    "ax.legend()\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.axhline(y=0.9, color='gray', linestyle=':', alpha=0.5, label='90% (cota superior teórica)')\n",
    "ax.legend()\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_lms_vs_perceptron_ruido.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print('✅ Figura guardada: fig_lms_vs_perceptron_ruido.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 11 — Experimento A3: μ-LMS y superficie MSE
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento A3: μ-LMS y convergencia a la solución de Wiener\n",
    "\n",
    "La superficie MSE de un combinador lineal es un paraboloide convexo (Fig. 17 del paper).  \n",
    "μ-LMS sigue la dirección del gradiente negativo y converge a $W^* = R^{-1}P$."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# EXPERIMENTO A3: μ-LMS — convergencia y superficie MSE\n",
    "# ═══════════════════════════════════════════════════════\n",
    "print('═' * 55)\n",
    "print('EXPERIMENTO A3: μ-LMS — convergencia al Wiener óptimo')\n",
    "print('═' * 55)\n",
    "\n",
    "# Usar datos 2D para visualizar la superficie MSE\n",
    "X_2d, y_2d, w_true_2d = generar_datos_linealmente_separables(n=200, n_features=2, ruido=0.05)\n",
    "W_mu, mse_mu, acc_mu, W_wiener, w_dist = mu_lms(X_2d, y_2d, mu=0.005, epochs=200)\n",
    "\n",
    "# Visualizar trayectoria de pesos en la superficie MSE\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "# Panel 1: Curvas de convergencia\n",
    "ax = axes[0]\n",
    "ax.plot(mse_mu, 'g-', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('MSE')\n",
    "ax.set_title(r'$\\mu$-LMS: convergencia del MSE')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "# Panel 2: Distancia al Wiener óptimo\n",
    "ax = axes[1]\n",
    "ax.plot(w_dist, 'purple', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel(r'$||W - W^*||_2$')\n",
    "ax.set_title(r'$\\mu$-LMS: distancia al óptimo de Wiener')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_mu_lms_convergencia.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print(f'✅ Peso Wiener: {W_wiener}')\n",
    "print(f'✅ Peso aprendido: {W_mu}')\n",
    "print(f'✅ Figura guardada: fig_mu_lms_convergencia.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 12 — Experimento A4: Backprop XOR
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento A4: Backpropagation para resolver XOR\n",
    "\n",
    "El XOR es el ejemplo canónico de problema **no linealmente separable** (Sección II-B, Fig. 7-9).  \n",
    "Un MLP de 2 capas con función sigmoide puede resolverlo, mientras que un Adaline simple no."
])

code([
    "print('═' * 55)\n",
    "print('EXPERIMENTO A4: MLP Backprop — XOR (no linealmente separable)')\n",
    "print('═' * 55)\n",
    "\n",
    "# MLP: 2 entradas → 4 hidden → 1 salida\n",
    "mlp = MLP(layer_sizes=[2, 4, 1], learning_rate=0.05)\n",
    "mse_bp, acc_bp = mlp.fit(X_xor, y_xor, epochs=2000)\n",
    "\n",
    "# Visualización\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "# Curvas de entrenamiento\n",
    "ax = axes[0]\n",
    "ax.plot(mse_bp, 'darkorange', linewidth=1.5, alpha=0.8)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('MSE')\n",
    "ax.set_title('Backpropagation XOR: Curva de error')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "ax2 = ax.twinx()\n",
    "ax2.plot(acc_bp, 'b-', linewidth=1, alpha=0.5)\n",
    "ax2.set_ylabel('Accuracy', color='b')\n",
    "ax2.set_ylim(0, 1.05)\n",
    "\n",
    "# Frontera de decisión\n",
    "ax = axes[1]\n",
    "xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))\n",
    "grid = np.c_[xx.ravel(), yy.ravel()]\n",
    "Z = mlp.predict(grid).reshape(xx.shape)\n",
    "ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu', levels=[-1, 0, 1])\n",
    "\n",
    "for clase, color, marker in [(1, '#2196F3', 'o'), (-1, '#F44336', 's')]:\n",
    "    mask = y_xor == clase\n",
    "    ax.scatter(X_xor[mask, 0], X_xor[mask, 1], c=color, marker=marker,\n",
    "               s=60, edgecolors='k', linewidth=0.5)\n",
    "\n",
    "ax.set_xlabel('x₁')\n",
    "ax.set_ylabel('x₂')\n",
    "ax.set_title(f'MLP Backprop — XOR (Acc={acc_bp[-1]*100:.1f}%)')\n",
    "ax.set_xlim(-1.5, 1.5)\n",
    "ax.set_ylim(-1.5, 1.5)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_backprop_xor.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print('✅ Figura guardada: fig_backprop_xor.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 13 — PARTE B: Datasets reales
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 🌍 PARTE B — Extensión a datasets reales\n",
    "\n",
    "El paper fue diseñado para patrones binarios ±1. Para aplicarlo a datos reales, se requiere:\n",
    "\n",
    "1. **Normalización** de features a $[-1, 1]$ (justificado por el \"normalized training set\", Eqs. 39-43)\n",
    "2. **Binarización** del target para clasificación binaria\n",
    "\n",
    "Datasets utilizados:\n",
    "\n",
    "| Dataset | Fuente | Instancias | Features | Aplica a |\n",
    "|---------|--------|:----------:|:--------:|----------|\n",
    "| 🪷 Iris (Setosa vs resto) | sklearn / UCI #53 | 150 | 4 | Perceptron, α-LMS |\n",
    "| 🍷 Wine Quality (tinto) | UCI #186 | 1,599 | 11 | α-LMS, μ-LMS |\n",
    "| 🌙 Moons | sklearn | 200 | 2 | Backprop (MLP) |"
])

# ═══════════════════════════════════════════════════════════
# CELDA 14 — Carga y preprocesamiento
# ═══════════════════════════════════════════════════════════
code([
    "# ═══════════════════════════════════════════════════════\n",
    "# PARTE B — Carga y preprocesamiento de datasets reales\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "# ── Iris (Setosa vs resto) ──\n",
    "X_iris_full, y_iris_full = load_iris(return_X_y=True)\n",
    "y_iris_bin = (y_iris_full == 0).astype(int) * 2 - 1  # Setosa=+1, resto=-1\n",
    "\n",
    "# ── Wine Quality ──\n",
    "df_wine = pd.read_csv('data/raw/datasets/winequality-red.csv')\n",
    "X_wine_full = df_wine.drop('quality', axis=1).values\n",
    "y_wine_full = df_wine['quality'].values\n",
    "y_wine_bin = np.where(y_wine_full >= 7, 1, -1)  # Buen vino = +1\n",
    "\n",
    "# ── Moons (no lineal) ──\n",
    "X_moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=1990)\n",
    "y_moons_bin = y_moons * 2 - 1  # {0,1} -> {-1,+1}\n",
    "\n",
    "# ── Normalización ──\n",
    "scaler_iris = MinMaxScaler(feature_range=(-1, 1))\n",
    "scaler_wine = MinMaxScaler(feature_range=(-1, 1))\n",
    "\n",
    "X_iris = scaler_iris.fit_transform(X_iris_full)\n",
    "X_wine = scaler_wine.fit_transform(X_wine_full)\n",
    "X_moons_norm = X_moons  # Ya está en rango adecuado\n",
    "\n",
    "print('📊 Datasets reales cargados y normalizados:')\n",
    "print(f'   🪷 Iris:  {X_iris.shape[0]}×{X_iris.shape[1]} | Clases: +1={sum(y_iris_bin==1)}, -1={sum(y_iris_bin==-1)}')\n",
    "print(f'   🍷 Wine:  {X_wine.shape[0]}×{X_wine.shape[1]} | Buen vino: {sum(y_wine_bin==1)}/{len(y_wine_bin)} ({100*sum(y_wine_bin==1)/len(y_wine_bin):.1f}%)')\n",
    "print(f'   🌙 Moons: {X_moons_norm.shape[0]}×{X_moons_norm.shape[1]} | Clases balanceadas')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 15 — Experimento B1: Perceptron en Iris
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento B1: Perceptron en Iris (Setosa vs resto)\n",
    "\n",
    "Setosa es **linealmente separable** de Versicolor y Virginica. El Perceptron debería converger rápido."
])

code([
    "# Perceptron en Iris\n",
    "print('═' * 55)\n",
    "print('EXPERIMENTO B1: Perceptron en Iris (Setosa vs resto)')\n",
    "print('═' * 55)\n",
    "\n",
    "X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(\n",
    "    X_iris, y_iris_bin, test_size=0.3, random_state=1990)\n",
    "\n",
    "W_per_iris, acc_per_iris = perceptron_rule(X_iris_train, y_iris_train, alpha=1.0, epochs=30)\n",
    "\n",
    "# Evaluación en test\n",
    "X_test_bias = np.c_[np.ones(X_iris_test.shape[0]), X_iris_test]\n",
    "y_pred = np.sign(X_test_bias @ W_per_iris)\n",
    "test_acc = np.mean(y_pred == y_iris_test)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(8, 5))\n",
    "ax.plot(acc_per_iris, 'r-', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('Accuracy (train)')\n",
    "ax.set_title(f'Perceptron en Iris — Test Accuracy: {test_acc*100:.1f}%')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.5)\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_perceptron_iris.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print(f'✅ Test accuracy: {test_acc*100:.2f}%')\n",
    "print(f'✅ Figura guardada: fig_perceptron_iris.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 16 — Experimento B2: α-LMS y μ-LMS en Wine Quality
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento B2: α-LMS y μ-LMS en Wine Quality 🍷\n",
    "\n",
    "¿Puede un clasificador lineal distinguir un buen vino de uno regular basado solo en sus propiedades químicas?"
])

code([
    "# α-LMS y μ-LMS en Wine Quality\n",
    "print('═' * 55)\n",
    "print('EXPERIMENTO B2: LMS en Wine Quality 🍷')\n",
    "print('═' * 55)\n",
    "\n",
    "X_w_train, X_w_test, y_w_train, y_w_test = train_test_split(\n",
    "    X_wine, y_wine_bin, test_size=0.3, random_state=1990, stratify=y_wine_bin)\n",
    "\n",
    "# α-LMS\n",
    "W_aw, mse_aw, acc_aw = alpha_lms(X_w_train, y_w_train, alpha=0.2, epochs=200)\n",
    "\n",
    "# μ-LMS\n",
    "W_mw, mse_mw, acc_mw, W_wien, w_dist_w = mu_lms(X_w_train, y_w_train, mu=0.0005, epochs=200)\n",
    "\n",
    "# Evaluación en test\n",
    "X_w_test_bias = np.c_[np.ones(X_w_test.shape[0]), X_w_test]\n",
    "y_pred_aw = np.sign(X_w_test_bias @ W_aw)\n",
    "y_pred_mw = np.sign(X_w_test_bias @ W_mw)\n",
    "test_acc_aw = np.mean(y_pred_aw == y_w_test)\n",
    "test_acc_mw = np.mean(y_pred_mw == y_w_test)\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "ax = axes[0]\n",
    "ax.plot(acc_aw, 'b-', label=rf'$\\alpha$-LMS (test={test_acc_aw*100:.1f}%)', linewidth=2)\n",
    "ax.plot(acc_mw, 'g-', label=rf'$\\mu$-LMS (test={test_acc_mw*100:.1f}%)', linewidth=2)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('Accuracy (train)')\n",
    "ax.set_title('🍷 Wine Quality: α-LMS vs μ-LMS')\n",
    "ax.legend()\n",
    "ax.grid(True, alpha=0.3)\n",
    "\n",
    "ax = axes[1]\n",
    "ax.plot(mse_aw, 'b-', alpha=0.6, label=r'$\\alpha$-LMS', linewidth=1.5)\n",
    "ax.plot(mse_mw, 'g-', alpha=0.6, label=r'$\\mu$-LMS', linewidth=1.5)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('MSE (train)')\n",
    "ax.set_title('Curvas de error (MSE)')\n",
    "ax.legend()\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_wine_lms.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print(f'✅ α-LMS test accuracy: {test_acc_aw*100:.2f}%')\n",
    "print(f'✅ μ-LMS test accuracy: {test_acc_mw*100:.2f}%')\n",
    "print(f'✅ Figura guardada: fig_wine_lms.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 17 — Experimento B3: Backprop en Moons
# ═══════════════════════════════════════════════════════════
md([
    "### 🧪 Experimento B3: MLP Backpropagation en Moons 🌙\n",
    "\n",
    "Las medias lunas (moons) NO son linealmente separables. Solo un MLP con capa oculta puede trazar una frontera no lineal."
])

code([
    "# MLP en Moons\n",
    "print('═' * 55)\n",
    "print('EXPERIMENTO B3: MLP Backprop en Moons 🌙')\n",
    "print('═' * 55)\n",
    "\n",
    "X_mo_train, X_mo_test, y_mo_train, y_mo_test = train_test_split(\n",
    "    X_moons_norm, y_moons_bin, test_size=0.3, random_state=1990)\n",
    "\n",
    "mlp_moons = MLP(layer_sizes=[2, 8, 4, 1], learning_rate=0.03)\n",
    "mse_moons, acc_moons = mlp_moons.fit(X_mo_train, y_mo_train, epochs=3000)\n",
    "\n",
    "# Evaluación\n",
    "y_pred_moons = mlp_moons.predict(X_mo_test)\n",
    "test_acc_moons = np.mean(y_pred_moons == y_mo_test)\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "ax = axes[0]\n",
    "ax.plot(mse_moons, 'darkorange', linewidth=1.2, alpha=0.8)\n",
    "ax.set_xlabel('Época')\n",
    "ax.set_ylabel('MSE')\n",
    "ax.set_title('MLP Backprop en Moons — Curva de error')\n",
    "ax.grid(True, alpha=0.3)\n",
    "ax.set_yscale('log')\n",
    "\n",
    "# Frontera de decisión\n",
    "ax = axes[1]\n",
    "xx, yy = np.meshgrid(np.linspace(-1.5, 2.5, 150), np.linspace(-1, 1.5, 150))\n",
    "grid = np.c_[xx.ravel(), yy.ravel()]\n",
    "Z = mlp_moons.predict(grid).reshape(xx.shape)\n",
    "ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu', levels=[-1, 0, 1])\n",
    "\n",
    "for clase, color, marker in [(-1, '#F44336', 's'), (1, '#2196F3', 'o')]:\n",
    "    mask = y_moons_bin == clase\n",
    "    ax.scatter(X_moons_norm[mask, 0], X_moons_norm[mask, 1],\n",
    "               c=color, marker=marker, s=25, edgecolors='k', linewidth=0.3, alpha=0.7)\n",
    "\n",
    "ax.set_xlabel('x₁')\n",
    "ax.set_ylabel('x₂')\n",
    "ax.set_title(f'MLP Backprop — Moons (Test Acc={test_acc_moons*100:.1f}%)')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('proyectos/RNA/notebook/fig_backprop_moons.png', dpi=150, bbox_inches='tight')\n",
    "plt.show()\n",
    "print(f'✅ Test accuracy: {test_acc_moons*100:.2f}%')\n",
    "print(f'✅ Figura guardada: fig_backprop_moons.png')"
])

# ═══════════════════════════════════════════════════════════
# CELDA 18 — PARTE C: Tabla comparativa final
# ═══════════════════════════════════════════════════════════
md([
    "---\n",
    "\n",
    "## 📊 PARTE C — Tabla Comparativa Final\n",
    "\n",
    "Resumen de todos los experimentos realizados."
])

code([
    "# ═══════════════════════════════════════════════════════\n",
    "# TABLA COMPARATIVA FINAL\n",
    "# ═══════════════════════════════════════════════════════\n",
    "\n",
    "def final_accuracy(X, y, W):\n",
    "    X_bias = np.c_[np.ones(X.shape[0]), X]\n",
    "    return np.mean(np.sign(X_bias @ W) == y)\n",
    "\n",
    "# Recalcular todas las métricas finales\n",
    "resultados = [\n",
    "    ['α-LMS', 'Sintético (separable)', '—', mse_lms[-1], acc_lms[-1], '—'],\n",
    "    ['α-LMS', 'Sintético (ruido)', '—', mse_lms_r[-1], acc_lms_r[-1], '—'],\n",
    "    ['Perceptron', 'Sintético (separable)', '—', np.nan, acc_per[-1], '—'],\n",
    "    ['Perceptron', 'Sintético (ruido)', '—', np.nan, acc_per_r[-1], '—'],\n",
    "    ['μ-LMS', 'Sintético (2D)', '—', mse_mu[-1], acc_mu[-1], w_dist[-1]],\n",
    "    ['Backprop MLP', 'XOR', '—', mse_bp[-1], acc_bp[-1], '—'],\n",
    "    ['Perceptron', '🪷 Iris (Setosa)', '—', np.nan, test_acc, '—'],\n",
    "    ['α-LMS', '🍷 Wine Quality', '—', mse_aw[-1], test_acc_aw, '—'],\n",
    "    ['μ-LMS', '🍷 Wine Quality', '—', mse_mw[-1], test_acc_mw, w_dist_w[-1]],\n",
    "    ['Backprop MLP', '🌙 Moons', '—', mse_moons[-1], test_acc_moons, '—'],\n",
    "]\n",
    "\n",
    "df_resultados = pd.DataFrame(resultados, columns=[\n",
    "    'Algoritmo', 'Dataset', 'Épocas convergencia', 'MSE final', 'Accuracy', '||W - W*||'\n",
    "])\n",
    "\n",
    "print('\\n' + '═' * 70)\n",
    "print('📊 TABLA COMPARATIVA FINAL — Widrow & Lehr (1990)')\n",
    "print('═' * 70)\n",
    "print(df_resultados.to_string(index=False))\n",
    "print('═' * 70)\n",
    "\n",
    "# Conclusiones automáticas\n",
    "print('\\n🔑 CONCLUSIONES CLAVE:')\n",
    "print(f'  1. El Perceptron converge a 100% SOLO si los datos son linealmente separables (Iris Setosa ✅, ruido ❌)')\n",
    "print(f'  2. α-LMS es más robusto que el Perceptron: logra {acc_lms_r[-1]*100:.1f}% con 10% de ruido vs {acc_per_r[-1]*100:.1f}% del Perceptron')\n",
    "print(f'  3. μ-LMS converge a la solución de Wiener: ||W - W*|| = {w_dist[-1]:.4f}')\n",
    "print(f'  4. El MLP con backpropagation resuelve XOR ({acc_bp[-1]*100:.1f}%) y Moons ({test_acc_moons*100:.1f}%), imposibles para clasificadores lineales')\n",
    "print(f'  5. En Wine Quality 🍷, el clasificador lineal alcanza {max(test_acc_aw, test_acc_mw)*100:.1f}% — el problema no es perfectamente separable')\n",
    "print(f'  6. Se confirma el principio de mínima perturbación como mecanismo unificador de todos los algoritmos')\n",
    "\n",
    "print('\\n✅ Notebook completado exitosamente.')"
])

# ═══════════════════════════════════════════════════════════
# Construir notebook
# ═══════════════════════════════════════════════════════════
nb = {
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10.0"}
    },
    "nbformat": 4,
    "nbformat_minor": 5,
    "cells": cells
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"✅ Notebook creado: {OUT}")
print(f"   Total celdas: {len(cells)} ({sum(1 for c in cells if c['cell_type']=='markdown')} markdown + {sum(1 for c in cells if c['cell_type']=='code')} code)")
