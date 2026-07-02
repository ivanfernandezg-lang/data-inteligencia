"""
Generador del notebook implementacion-widrow-lehr.ipynb
Tarea IC RNA 2026-1 — Widrow & Lehr (1990)
"""
import nbformat as nbf
import os

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.10.0"}
}

cells = []

def md(source):
    cells.append(nbf.v4.new_markdown_cell(source))

def code(source):
    cells.append(nbf.v4.new_code_cell(source))

# ══════════════════════════════════════════════════════════
# CELDA 0: Título
# ══════════════════════════════════════════════════════════
md(r"""# Implementación de Algoritmos de Aprendizaje en RNA Feedforward

**Tarea IC RNA 2026-1 — Módulo Redes Neuronales Artificiales**
Magíster en Ingeniería Informática — Universidad de Santiago de Chile

**Paper:** Widrow, B. & Lehr, M. A. (1990). *30 Years of Adaptive Neural Networks: Perceptron, Madaline, and Backpropagation.* Proceedings of the IEEE, 78(9), 1415–1442.

**Algoritmos implementados desde cero en NumPy puro:**
1. Regla del Perceptrón (Rosenblatt, 1958)
2. $\alpha$-LMS / Regla Delta de Widrow-Hoff (1960)
3. $\mu$-LMS / Descenso por gradiente estocástico
4. MLP con Backpropagation (Rumelhart, Hinton & Williams, 1986)
5. Madaline Rule II — MRII (Widrow, Winter & Baxter, 1987)
6. Madaline Rule III — MRIII (Andes, 1988) ≡ Backpropagation

**Experimentos:** E1–E7 + Wine Quality + MNIST reducido""")

# ══════════════════════════════════════════════════════════
# CELDA 1: Mapa experimento → sección
# ══════════════════════════════════════════════════════════
md(r"""## Mapa Experimento → Sección del Informe

| Experimento | Tema | Hipótesis | Figura | Tabla |
|---|---|---|---|---|
| E1 | Capacidad de Cover (Monte Carlo) | H1: $C_s \approx 2N_w$ | `fig_cover.png` | — |
| E2 | Reglas lineales en datos separables | H2: Convergencia finita del Perceptrón | `fig_datasets.png`, `fig_fronteras.png`, `fig_convergencia.png` | `tab_lineales.tex` |
| E3 | Datos no separables | H2: Inestabilidad del Perceptrón vs LMS | `fig_noseparable.png` | — |
| E4 | Superficies de MSE | Fundamento geométrico | `fig_superficies_mse.png` | — |
| E5 | XOR: MLP Backprop + MRII | H3: Poder no lineal + óptimos locales | `fig_xor.png` | `tab_xor.tex` |
| E6 | MLP en Iris + two-moons + Wine | Validación en datasets reales | `fig_iris_mlp.png`, `fig_wine.png`, `fig_moons.png` | `tab_iris.tex`, `tab_relevancia.tex` |
| E7 | MRIII ≡ Backprop + costo computacional | H4: Equivalencia cuando $\Delta s \to 0$ | `fig_mriii_bp.png` | `tab_mriii.tex` |
| — | Tabla resumen consolidada | — | — | `tab_resumen.tex` |

**Semilla global:** `SEED = 1990` para reproducibilidad exacta.""")

# ══════════════════════════════════════════════════════════
# CELDA 2: Imports y configuración
# ══════════════════════════════════════════════════════════
code(r"""# ── Imports y configuración global ──
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 11, 'figure.dpi': 100})
from scipy.optimize import linprog
from scipy.special import comb
from sklearn.datasets import load_iris, make_moons, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import itertools, time, warnings, os, sys
warnings.filterwarnings('ignore')

# Semilla global
SEED = 1990
np.random.seed(SEED)

# Carpetas de salida
os.makedirs('figs', exist_ok=True)
os.makedirs('tabs', exist_ok=True)

print("✅ Entorno configurado. NumPy", np.__version__)
print("   figs/ y tabs/ listos para recibir salidas.")""")

# ══════════════════════════════════════════════════════════
# CELDA 3: Utilidades
# ══════════════════════════════════════════════════════════
code(r"""# ── Funciones de utilidad ──

def add_bias(X: np.ndarray) -> np.ndarray:
    """Antepone columna de 1s para el bias."""
    return np.column_stack([np.ones(len(X)), X])

def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Fracción de predicciones correctas."""
    return np.mean(y_true == y_pred)

def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Error cuadrático medio."""
    return np.mean((y_true - y_pred) ** 2)

def hamming_error(y_true: np.ndarray, y_pred: np.ndarray) -> int:
    """Número de patrones mal clasificados (error de Hamming)."""
    return int(np.sum(y_true != y_pred))

def one_hot(y: np.ndarray, n_classes: int) -> np.ndarray:
    """Convierte etiquetas {0,1,...,C-1} a one-hot en {-1,+1}."""
    Y = -np.ones((len(y), n_classes))
    Y[np.arange(len(y)), y] = 1.0
    return Y

def normalize_features(X_train: np.ndarray, X_test: np.ndarray) -> tuple:
    """Normaliza al rango [-1, 1] usando MinMax del train."""
    xmin, xmax = X_train.min(axis=0), X_train.max(axis=0)
    denom = xmax - xmin
    denom[denom == 0] = 1.0
    Xt = 2 * (X_train - xmin) / denom - 1
    Xv = 2 * (X_test - xmin) / denom - 1
    return Xt, Xv

def shuffle_epoch(X: np.ndarray, d: np.ndarray, rng: np.random.Generator):
    """Permutación aleatoria de patrones para una época."""
    idx = rng.permutation(len(X))
    return X[idx], d[idx]

print("✅ Utilidades definidas: add_bias, accuracy, mse_loss, one_hot, normalize_features, shuffle_epoch")""")

# ══════════════════════════════════════════════════════════
# CELDA 4: Datos sintéticos
# ══════════════════════════════════════════════════════════
code(r"""# ── Generación de datasets sintéticos ──
rng_data = np.random.default_rng(SEED)

def make_separable(n=100):
    """Dos gaussianas separables: N([±2,±2], 0.35²·I)."""
    X = np.vstack([
        rng_data.normal([2, 2], 0.35, (n, 2)),
        rng_data.normal([-2, -2], 0.35, (n, 2))
    ])
    d = np.array([1]*n + [-1]*n)
    return X, d

def make_nonseparable(n=100):
    """Dos gaussianas solapadas: N([±0.9,±0.9], 1.3²·I)."""
    X = np.vstack([
        rng_data.normal([0.9, 0.9], 1.3, (n, 2)),
        rng_data.normal([-0.9, -0.9], 1.3, (n, 2))
    ])
    d = np.array([1]*n + [-1]*n)
    return X, d

def make_xor():
    """4 patrones XOR en {-1,+1}²."""
    X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]], dtype=float)
    d = np.array([-1, 1, 1, -1], dtype=float)
    return X, d

# Datasets generados
X_sep, d_sep = make_separable()
X_nosep, d_nosep = make_nonseparable()
X_xor, d_xor = make_xor()
moons_data = make_moons(n_samples=300, noise=0.20, random_state=SEED)
X_moons, d_moons_raw = moons_data[0], moons_data[1]
d_moons = np.where(d_moons_raw == 0, -1.0, 1.0)

print(f"✅ Datos sintéticos generados:")
print(f"   Separable:    {X_sep.shape[0]} pts, clases +1/-1")
print(f"   No separable: {X_nosep.shape[0]} pts, clases +1/-1")
print(f"   XOR:          {X_xor.shape[0]} pts, d = {d_xor}")
print(f"   Two-moons:    {X_moons.shape[0]} pts")""")

# ══════════════════════════════════════════════════════════
# CELDA 5: Datos reales (Iris, Wine, MNIST)
# ══════════════════════════════════════════════════════════
code(r"""# ── Carga de datasets reales ──

# Iris (Fisher, 1936)
iris = load_iris()
X_iris_raw, y_iris_raw = iris.data, iris.target
print(f"✅ Iris: {X_iris_raw.shape[0]}×{X_iris_raw.shape[1]}, clases={iris.target_names}")

# Split estratificado
X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(
    X_iris_raw, y_iris_raw, test_size=0.3, random_state=42, stratify=y_iris_raw
)
# Normalizar a [-1,1]
X_iris_train_norm, X_iris_test_norm = normalize_features(X_iris_train, X_iris_test)
d_iris_train_oh = one_hot(y_iris_train, 3)
d_iris_test_oh = one_hot(y_iris_test, 3)

# Subconjuntos binarios para Perceptron (clases originales)
# Setosa (clase 0) vs Resto
mask_setosa_train = y_iris_train == 0
mask_setosa_test = y_iris_test == 0
X_setosa_train = X_iris_train_norm.copy()
d_setosa_train = np.where(y_iris_train == 0, 1.0, -1.0)
X_setosa_test = X_iris_test_norm.copy()
d_setosa_test = np.where(y_iris_test == 0, 1.0, -1.0)

# Versicolor (clase 1) vs Virginica (clase 2)
mask_vv = (y_iris_train == 1) | (y_iris_train == 2)
X_vv_train = X_iris_train_norm[mask_vv]
d_vv_train = np.where(y_iris_train[mask_vv] == 1, 1.0, -1.0)
mask_vv_test = (y_iris_test == 1) | (y_iris_test == 2)
X_vv_test = X_iris_test_norm[mask_vv_test]
d_vv_test = np.where(y_iris_test[mask_vv_test] == 1, 1.0, -1.0)

# Wine Quality (UCI, Cortez et al. 2009) — binarizado
wine = load_wine()
X_wine_raw, y_wine_raw = wine.data, wine.target
# Binarizar: clase 0 vs resto
d_wine_bin = np.where(y_wine_raw == 0, 1.0, -1.0)
X_wine_train, X_wine_test, d_wine_train, d_wine_test = train_test_split(
    X_wine_raw, d_wine_bin, test_size=0.3, random_state=42, stratify=d_wine_bin
)
X_wine_train_norm, X_wine_test_norm = normalize_features(X_wine_train, X_wine_test)

# MNIST reducido (dígitos 0-4)
from sklearn.datasets import load_digits
digits = load_digits()
X_digits_raw, y_digits_raw = digits.data, digits.target
mask_04 = y_digits_raw <= 4
X_digits_raw = X_digits_raw[mask_04]
y_digits_raw = y_digits_raw[mask_04]
X_digits_train, X_digits_test, y_digits_train, y_digits_test = train_test_split(
    X_digits_raw, y_digits_raw, test_size=0.3, random_state=42, stratify=y_digits_raw
)
X_digits_train_norm, X_digits_test_norm = normalize_features(X_digits_train, X_digits_test)
d_digits_train_oh = one_hot(y_digits_train, 5)
d_digits_test_oh = one_hot(y_digits_test, 5)

print(f"✅ Datos reales cargados y preprocesados:")
print(f"   Iris train/test: {X_iris_train_norm.shape[0]}/{X_iris_test_norm.shape[0]}")
print(f"   Wine train/test: {X_wine_train_norm.shape[0]}/{X_wine_test_norm.shape[0]}")
print(f"   MNIST-04 train/test: {X_digits_train_norm.shape[0]}/{X_digits_test_norm.shape[0]}")""")

# ══════════════════════════════════════════════════════════
# CELDA 6: Sección — Algoritmos de un elemento
# ══════════════════════════════════════════════════════════
md(r"""## 🔬 Algoritmos de Aprendizaje — Un Elemento

Implementaciones desde cero en NumPy puro de los 3 algoritmos de un solo elemento adaptativo. Convención: $d \in \{-1, +1\}$, entradas con bias $x_0 = +1$.""")

# ══════════════════════════════════════════════════════════
# CELDA 7: Perceptron
# ══════════════════════════════════════════════════════════
code(r"""# ── Regla del Perceptrón (Rosenblatt, 1958) — Eq. (18) ──
# W_{k+1} = W_k + α·(ε̃_k/2)·X_k,  ε̃_k = d_k − y_k ∈ {−2, 0, +2}
# Solo adapta si la decisión es incorrecta.

def train_perceptron(X_raw, d, alpha=1.0, max_epochs=200, seed=SEED, verbose=False):
    """
    Entrena un Perceptrón con presentación aleatoria por época.
    
    Parámetros:
        X_raw: patrones (N×n) sin bias
        d: respuestas deseadas ∈ {−1,+1}
        alpha: tasa de aprendizaje
        max_epochs: máximo de épocas
        seed: semilla para reproducibilidad
        verbose: mostrar progreso
    
    Retorna:
        W: vector de pesos final (n+1,)
        history: dict con 'epochs_to_converge', 'acc_history', 'w_norm_history'
    """
    rng = np.random.default_rng(seed)
    Xb = add_bias(X_raw)
    N, n_plus_1 = Xb.shape
    W = np.zeros(n_plus_1)
    
    acc_history = []
    w_norm_history = []
    converged_epoch = -1
    
    for epoch in range(1, max_epochs + 1):
        Xs, ds = shuffle_epoch(Xb, d, rng)
        errors_this_epoch = 0
        
        for k in range(N):
            xk, dk = Xs[k], ds[k]
            s = np.dot(xk, W)
            y = np.sign(s) if s != 0 else 1.0
            if y != dk:
                W = W + alpha * ((dk - y) / 2.0) * xk
                errors_this_epoch += 1
        
        y_pred = np.sign(np.dot(Xb, W))
        y_pred[y_pred == 0] = 1.0
        acc = accuracy(d, y_pred)
        acc_history.append(acc)
        w_norm_history.append(np.linalg.norm(W))
        
        if verbose and epoch % 10 == 0:
            print(f"  Época {epoch:3d}: errores={errors_this_epoch}, acc={acc:.4f}")
        
        if errors_this_epoch == 0 and converged_epoch < 0:
            converged_epoch = epoch
    
    return W, {'epochs_to_converge': converged_epoch,
               'acc_history': np.array(acc_history),
               'w_norm_history': np.array(w_norm_history)}

# Test rápido
W_p, hist_p = train_perceptron(X_sep, d_sep, verbose=True)
print(f"✅ Perceptrón: converge en {hist_p['epochs_to_converge']} épocas, acc final={hist_p['acc_history'][-1]:.4f}")""")

print(f"  Celdas 0-7 creadas...")
nb.cells = cells
print(f"  Total celdas hasta ahora: {len(cells)}")
