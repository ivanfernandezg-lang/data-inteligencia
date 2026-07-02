"""
Parte 2: Agrega algoritmos y experimentos al notebook existente.
Ejecutar: python gen_notebook_p2.py
"""
import nbformat as nbf
import os

IN  = "C:/Developer/data-inteligencia/proyectos/RNA/notebook/v1/implementacion-widrow-lehr.ipynb"
OUT = IN

with open(IN, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

cells = list(nb.cells)

def md(s):
    cells.append(nbf.v4.new_markdown_cell(s))

def code(s):
    cells.append(nbf.v4.new_code_cell(s))

# ═══════════════════════════════════════════════════════════════
# CELDA 6: Sección — Algoritmos de un elemento
# ═══════════════════════════════════════════════════════════════
md(r"""---
## 🔬 Algoritmos de Aprendizaje — Un Solo Elemento

Implementaciones desde cero en NumPy puro de los algoritmos para un único elemento adaptativo
(Adaline). Todas usan presentación aleatoria por época (*random shuffling*, Ridgway).
Convención: $d \in \{-1, +1\}$, entradas con bias $x_0 = +1$.

Referencias: Widrow & Lehr (1990), Secciones IV y VI.""")

# ═══════════════════════════════════════════════════════════════
# CELDA 7: train_perceptron
# ═══════════════════════════════════════════════════════════════
code(r"""# ── Regla del Perceptron (Rosenblatt, 1958) — Eq. (18) ──
# W_{k+1} = W_k + alpha * (epsilon_tilde_k / 2) * X_k
# epsilon_tilde_k = d_k - y_k in {-2, 0, +2}
# Solo adapta si la decision es incorrecta. Teorema de convergencia: separa en pasos finitos.

def train_perceptron(X_raw, d, alpha=1.0, max_epochs=200, seed=SEED):
    """
    Entrena un Perceptron con presentacion aleatoria por epoca.
    Retorna: W (pesos finales), history (dict con epochs_to_converge, acc_history, w_norm_history)
    """
    rng = np.random.default_rng(seed)
    Xb = add_bias(X_raw)
    N, nw = Xb.shape
    W = np.zeros(nw)
    acc_hist, wnorm_hist = [], []
    conv_epoch = -1

    for epoch in range(1, max_epochs + 1):
        Xs, ds = shuffle_epoch(Xb, d, rng)
        errors = 0
        for k in range(N):
            xk, dk = Xs[k], ds[k]
            s = np.dot(xk, W)
            y = np.sign(s) if s != 0 else 1.0
            if y != dk:
                W = W + alpha * ((dk - y) / 2.0) * xk
                errors += 1

        yp = np.sign(np.dot(Xb, W)); yp[yp == 0] = 1.0
        acc_hist.append(accuracy_fn(d, yp))
        wnorm_hist.append(np.linalg.norm(W))
        if errors == 0 and conv_epoch < 0:
            conv_epoch = epoch

    return W, {'epochs_to_converge': conv_epoch,
               'acc_history': np.array(acc_hist),
               'w_norm_history': np.array(wnorm_hist)}

# Test rapido
Wp_test, hp_test = train_perceptron(X_sep, d_sep)
print(f"Perceptron en datos separables: {hp_test['epochs_to_converge']} epocas, acc={hp_test['acc_history'][-1]:.4f}")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 8: train_alpha_lms
# ═══════════════════════════════════════════════════════════════
code(r"""# ── alpha-LMS / Regla Delta de Widrow-Hoff (1960) — Eq. (10) ──
# W_{k+1} = W_k + alpha * (epsilon_k / ||X_k||^2) * X_k
# epsilon_k = d_k - s_k  (error LINEAL)
# Rango estable: 0 < alpha < 2. Practico: 0.1 < alpha < 1.0.
# Autonormalizante: el cambio de peso es colineal con X_k.

def train_alpha_lms(X_raw, d, alpha=0.5, max_epochs=200, seed=SEED):
    """
    Entrena con alpha-LMS (Widrow-Hoff).
    Retorna: W, history (mse_history, acc_history, w_norm_history)
    """
    rng = np.random.default_rng(seed)
    Xb = add_bias(X_raw)
    N, nw = Xb.shape
    W = np.zeros(nw)
    mse_hist, acc_hist, wnorm_hist = [], [], []

    for epoch in range(1, max_epochs + 1):
        Xs, ds = shuffle_epoch(Xb, d, rng)
        for k in range(N):
            xk, dk = Xs[k], ds[k]
            s = np.dot(xk, W)
            eps = dk - s
            W = W + alpha * (eps / np.dot(xk, xk)) * xk

        s_all = np.dot(Xb, W)
        mse_hist.append(mse_loss(d, s_all))
        yp = np.sign(s_all); yp[yp == 0] = 1.0
        acc_hist.append(accuracy_fn(d, yp))
        wnorm_hist.append(np.linalg.norm(W))

    return W, {'mse_history': np.array(mse_hist),
               'acc_history': np.array(acc_hist),
               'w_norm_history': np.array(wnorm_hist)}

# Test rapido
Wa_test, ha_test = train_alpha_lms(X_sep, d_sep, alpha=0.5)
print(f"alpha-LMS en datos separables: MSE final={ha_test['mse_history'][-1]:.6f}, acc={ha_test['acc_history'][-1]:.4f}")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 9: train_mu_lms
# ═══════════════════════════════════════════════════════════════
code(r"""# ── mu-LMS / Descenso por gradiente estocastico — Eq. (33) ──
# W_{k+1} = W_k + 2*mu * epsilon_k * X_k
# Estabilidad: 0 < mu < 1/tr[R]. MSE = hiperparaboloide CONVEXO, unico minimo global W*.
# El gradiente instantaneo -2*epsilon_k*X_k es INSESGADO: E[-2*epsilon_k*X_k] = gradiente real.

def train_mu_lms(X_raw, d, mu=0.01, max_epochs=200, seed=SEED):
    """
    Entrena con mu-LMS (descenso por gradiente estocastico).
    Retorna: W, history (mse_history, acc_history, w_norm_history, weight_trajectory)
    """
    rng = np.random.default_rng(seed)
    Xb = add_bias(X_raw)
    N, nw = Xb.shape
    W = np.zeros(nw)
    mse_hist, acc_hist, wnorm_hist = [], [], []
    w_traj = [W.copy()]  # Trayectoria de pesos (solo 2D+1 para visualizacion)

    for epoch in range(1, max_epochs + 1):
        Xs, ds = shuffle_epoch(Xb, d, rng)
        for k in range(N):
            xk, dk = Xs[k], ds[k]
            s = np.dot(xk, W)
            eps = dk - s
            W = W + 2 * mu * eps * xk

        s_all = np.dot(Xb, W)
        mse_hist.append(mse_loss(d, s_all))
        yp = np.sign(s_all); yp[yp == 0] = 1.0
        acc_hist.append(accuracy_fn(d, yp))
        wnorm_hist.append(np.linalg.norm(W))
        if epoch <= 50:  # Guardar trayectoria inicial
            w_traj.append(W.copy())

    return W, {'mse_history': np.array(mse_hist),
               'acc_history': np.array(acc_hist),
               'w_norm_history': np.array(wnorm_hist),
               'weight_trajectory': np.array(w_traj)}

# Test rapido
Wmu_test, hmu_test = train_mu_lms(X_sep, d_sep, mu=0.02)
print(f"mu-LMS en datos separables: MSE final={hmu_test['mse_history'][-1]:.6f}, acc={hmu_test['acc_history'][-1]:.4f}")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 10: Sección — Redes Multicapa
# ═══════════════════════════════════════════════════════════════
md(r"""---
## 🧠 Algoritmos de Aprendizaje — Redes Multicapa

Implementaciones desde cero en NumPy puro de MLP con Backpropagation, Madaline Rule II (MRII)
y Madaline Rule III (MRIII). Referencias: Widrow & Lehr (1990), Secciones V, VI y VII.""")

# ═══════════════════════════════════════════════════════════════
# CELDA 11: Clase MLP
# ═══════════════════════════════════════════════════════════════
code(r"""# ── MLP con Backpropagation (Rumelhart, Hinton & Williams, 1986) ──
# Arquitectura: capas totalmente conectadas de Adalines con tanh.
# Entrenamiento: estocastico patron-a-patron con momentum (Eqs. 94, 96-97).
# Deltas: delta^(L) = epsilon * sgm'(s) en salida (Eq. 78/79)
#         delta^(l) = (W^(l+1)^T * delta^(l+1)) .* sgm'(s^(l)) en ocultas (Eq. 87)
# Actualizacion: Delta W = 2*mu * delta * x^T (Eq. 94)

class MLP:
    """
    Perceptron Multicapa con backpropagation y momentum.
    Targets one-hot en {-1, +1}. Activacion: tanh.
    """
    def __init__(self, layer_sizes, mu=0.01, momentum=0.0, seed=SEED):
        """
        layer_sizes: [n_in, n_h1, n_h2, ..., n_out]
        mu: tasa de aprendizaje
        momentum: factor de momentum (0 = sin momentum)
        """
        self.L = len(layer_sizes) - 1  # Numero de capas de pesos
        self.mu = mu
        self.momentum = momentum
        self.rng = np.random.default_rng(seed)

        # Inicializacion uniforme +-0.5 (el paper recomienda pesos pequenos no cero)
        self.W = []
        self.V = []  # Terminos de momentum
        for l in range(self.L):
            n_in_l = layer_sizes[l] + 1  # +1 para bias
            n_out_l = layer_sizes[l + 1]
            Wl = self.rng.uniform(-0.5, 0.5, (n_out_l, n_in_l))
            self.W.append(Wl)
            self.V.append(np.zeros_like(Wl))

    def forward(self, x):
        """
        Forward pass para UN patron x (sin bias, shape=(n_in,)).
        Retorna: (activations, suminders)
          activations[l]: salida de capa l (con bias antepuesto para capa 0)
          suminders[l]:   suma ponderada ANTES de activacion
        """
        acts = [np.append(1.0, x)]  # Capa 0 = entrada con bias
        sums = []
        a = x.copy()
        for l in range(self.L):
            a_bias = np.append(1.0, a)
            s = self.W[l] @ a_bias
            sums.append(s)
            if l < self.L - 1:
                a = sigmoid(s)  # Capa oculta: tanh
            else:
                a = sigmoid(s)  # Capa de salida: tanh
            acts.append(np.append(1.0, a))
        return acts, sums

    def _backprop_deltas(self, acts, sums, d_target):
        """
        Calcula deltas para todas las capas (Eqs. 78/79 y 87).
        d_target: vector de salida deseada en {-1,+1}
        Retorna lista de deltas por capa (solo las Adalines, sin bias).
        """
        deltas = [None] * self.L
        # Capa de salida (Eq. 78/79)
        y_out = acts[-1][1:]  # Quitar bias
        eps = d_target - y_out
        delta_out = eps * sigmoid_derivative(y_out)  # Eq. 79 con tanh
        deltas[-1] = delta_out

        # Retropropagar (Eq. 87)
        for l in range(self.L - 2, -1, -1):
            y_hidden = acts[l + 1][1:]  # Salida de capa l (sin bias)
            W_next = self.W[l + 1][:, 1:]  # Pesos sin columna bias
            delta_next = deltas[l + 1]
            delta_h = (W_next.T @ delta_next) * sigmoid_derivative(y_hidden)
            deltas[l] = delta_h

        return deltas

    def train_pattern(self, x, d_target):
        """
        Una presentacion de patron: forward + backprop + update con momentum.
        x: vector de entrada sin bias. d_target: vector deseado {-1,+1}.
        """
        acts, sums = self.forward(x)
        deltas = self._backprop_deltas(acts, sums, d_target)

        for l in range(self.L):
            a_in = acts[l]  # Entrada a capa l (con bias)
            delta = deltas[l]
            dw = 2 * self.mu * np.outer(delta, a_in)  # Eq. 94
            if self.momentum > 0:
                self.V[l] = self.momentum * self.V[l] + (1 - self.momentum) * dw  # Eq. 96-97
                self.W[l] += self.V[l]
            else:
                self.W[l] += dw

    def fit(self, X, d, epochs=100, verbose=False, seed=None):
        """
        Entrena el MLP con presentacion aleatoria por epoca.
        X: (N, n_in) sin bias. d: (N, n_out) one-hot en {-1,+1}.
        """
        rng_fit = np.random.default_rng(seed if seed is not None else SEED)
        N = len(X)
        mse_hist, acc_hist = [], []

        for ep in range(1, epochs + 1):
            idx = rng_fit.permutation(N)
            for k in idx:
                self.train_pattern(X[k], d[k])

            preds = self.predict_batch(X)
            mse_hist.append(mse_loss(d, preds))
            if d.ndim == 2 and d.shape[1] > 1:
                acc_hist.append(self.accuracy(X, d))
            else:
                yp = np.sign(preds.flatten()); yp[yp == 0] = 1.0
                acc_hist.append(accuracy_fn(d.flatten(), yp))

            if verbose and ep % max(1, epochs // 10) == 0:
                print(f"  Epoca {ep:4d}/{epochs}: MSE={mse_hist[-1]:.6f}, acc={acc_hist[-1]:.4f}")

        return {'mse_history': np.array(mse_hist), 'acc_history': np.array(acc_hist)}

    def predict_batch(self, X):
        """Predice salidas continuas (tanh) para un lote."""
        preds = np.zeros((len(X), self.W[-1].shape[0]))
        for i in range(len(X)):
            acts, _ = self.forward(X[i])
            preds[i] = acts[-1][1:]  # Sin bias
        return preds

    def accuracy(self, X, d_onehot):
        """Accuracy para clasificacion multiclase (one-hot)."""
        preds = self.predict_batch(X)
        y_pred = np.argmax(preds, axis=1)
        y_true = np.argmax(d_onehot, axis=1) if d_onehot.ndim == 2 else np.where(d_onehot > 0, 1, 0)
        return accuracy_fn(y_true, y_pred)

    def classification_report(self, X, d_onehot, target_names=None):
        """Reporte de clasificacion via sklearn."""
        preds = self.predict_batch(X)
        y_pred = np.argmax(preds, axis=1)
        y_true = np.argmax(d_onehot, axis=1)
        return confusion_matrix(y_true, y_pred), accuracy_score(y_true, y_pred)

print("Clase MLP definida. Test rapido en XOR...")

# Test rapido XOR
mlp_test = MLP([2, 2, 1], mu=0.1, momentum=0.0)
hist_test = mlp_test.fit(X_xor, d_xor.reshape(-1,1), epochs=400)
print(f"MLP(2,2,1) en XOR: MSE final={hist_test['mse_history'][-1]:.6f}, acc={hist_test['acc_history'][-1]:.4f}")""")

print(f"[gen_notebook_p2] Celdas 6-11 agregadas. Total: {len(cells)}")
nb.cells = cells
nbf.write(nb, OUT)
print(f"[gen_notebook_p2] Guardado en {OUT}")
