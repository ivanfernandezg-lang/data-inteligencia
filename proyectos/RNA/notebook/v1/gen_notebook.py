"""
Generador completo del notebook implementacion-widrow-lehr.ipynb
Tarea IC RNA 2026-1 — Widrow & Lehr (1990)
Se ejecuta: python gen_notebook.py
"""
import nbformat as nbf
import os

OUT = "C:/Developer/data-inteligencia/proyectos/RNA/notebook/v1/implementacion-widrow-lehr.ipynb"

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.10.0"}
}
cells = []

def md(s):
    cells.append(nbf.v4.new_markdown_cell(s))

def code(s):
    cells.append(nbf.v4.new_code_cell(s))

# ═══════════════════════════════════════════════════════════════
# CELDA 0: Título
# ═══════════════════════════════════════════════════════════════
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
6. Madaline Rule III — MRIII (Andes, 1988) $\equiv$ Backpropagation

**Experimentos:** E1–E7 + Wine Quality + MNIST reducido""")

# ═══════════════════════════════════════════════════════════════
# CELDA 1: Mapa experimento → sección
# ═══════════════════════════════════════════════════════════════
md(r"""## Mapa Experimento $\to$ Sección del Informe

| Exp | Tema | Hipótesis | Figura | Tabla |
|---|---|---|---|---|
| E1 | Capacidad de Cover (Monte Carlo) | H1: $C_s \approx 2N_w$ | `fig_cover.png` | — |
| E2 | Reglas lineales en datos separables | H2: Convergencia finita del Perceptrón | `fig_datasets.png`, `fig_fronteras.png`, `fig_convergencia.png` | `tab_lineales.tex` |
| E3 | Datos no separables | H2: Inestabilidad del Perceptrón vs LMS | `fig_noseparable.png` | — |
| E4 | Superficies de MSE | Fundamento geométrico | `fig_superficies_mse.png` | — |
| E5 | XOR: MLP Backprop + MRII | H3: Poder no lineal + óptimos locales | `fig_xor.png` | `tab_xor.tex` |
| E6 | MLP en Iris + two-moons + Wine + MNIST | Validación en datasets reales | `fig_iris_mlp.png`, `fig_wine.png`, `fig_moons.png`, `fig_mnist.png` | `tab_iris.tex`, `tab_relevancia.tex` |
| E7 | MRIII $\equiv$ Backprop + costo computacional | H4: Equivalencia cuando $\Delta s \to 0$ | `fig_mriii_bp.png` | `tab_mriii.tex` |
| — | Tabla resumen consolidada | — | — | `tab_resumen.tex` |

**Semilla global:** `SEED = 1990` para reproducibilidad exacta.""")

# ═══════════════════════════════════════════════════════════════
# CELDA 2: Imports y configuración
# ═══════════════════════════════════════════════════════════════
code("""# ── Imports y configuracion global ──
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 11, 'figure.dpi': 100})
from scipy.optimize import linprog
from scipy.special import comb as scipy_comb
from sklearn.datasets import load_iris, make_moons, load_wine, load_digits
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
print("   Carpetas figs/ y tabs/ listas.")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 3: Utilidades matemáticas
# ═══════════════════════════════════════════════════════════════
code("""# ── Funciones de utilidad ──

def add_bias(X):
    \"\"\"Antepone columna de 1s para el bias (x0 = +1).\"\"\"
    return np.column_stack([np.ones(len(X)), X])

def accuracy_fn(y_true, y_pred):
    \"\"\"Fraccion de predicciones correctas.\"\"\"
    return np.mean(y_true == y_pred)

def mse_loss(y_true, y_pred):
    \"\"\"Error cuadratico medio.\"\"\"
    return np.mean((y_true - y_pred) ** 2)

def hamming_error(y_true, y_pred):
    \"\"\"Numero de patrones mal clasificados.\"\"\"
    return int(np.sum(y_true != y_pred))

def one_hot(y, n_classes):
    \"\"\"Convierte etiquetas {0,...,C-1} a one-hot en {-1,+1}.\"\"\"
    Y = -np.ones((len(y), n_classes))
    Y[np.arange(len(y)), y] = 1.0
    return Y

def normalize_features(X_train, X_test):
    \"\"\"Normaliza al rango [-1, 1] usando min-max del train.\"\"\"
    xmin = X_train.min(axis=0)
    xmax = X_train.max(axis=0)
    denom = xmax - xmin
    denom[denom == 0] = 1.0
    Xt = 2 * (X_train - xmin) / denom - 1
    Xv = 2 * (X_test - xmin) / denom - 1
    return Xt, Xv

def shuffle_epoch(X, d, rng):
    \"\"\"Permutacion aleatoria de patrones para una epoca.\"\"\"
    idx = rng.permutation(len(X))
    return X[idx], d[idx]

def wiener_solution(X_raw, d):
    \"\"\"Solucion optima de Wiener: W* = R^{-1} P (muestral).\"\"\"
    Xb = add_bias(X_raw)
    R = Xb.T @ Xb / len(Xb)
    P = Xb.T @ d / len(Xb)
    try:
        return np.linalg.solve(R, P)
    except np.linalg.LinAlgError:
        return np.linalg.lstsq(R, P, rcond=None)[0]

def sigmoid(s):
    \"\"\"Tangente hiperbolica (tanh).\"\"\"
    return np.tanh(s)

def sigmoid_derivative(y):
    \"\"\"Derivada de tanh: 1 - y^2 (Eq. 55 del paper).\"\"\"
    return 1.0 - y ** 2

print(\"✅ Utilidades definidas.\")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 4: Datos sintéticos
# ═══════════════════════════════════════════════════════════════
code("""# ── Generacion de datasets sinteticos ──
rng_data = np.random.default_rng(SEED)

def make_separable(n=100):
    \"\"\"Dos gaussianas bien separadas: N([+/-2,+/-2], 0.35^2 I).\"\"\"
    X = np.vstack([
        rng_data.normal([ 2,  2], 0.35, (n, 2)),
        rng_data.normal([-2, -2], 0.35, (n, 2))
    ])
    d = np.array([1]*n + [-1]*n)
    return X, d

def make_nonseparable(n=100):
    \"\"\"Dos gaussianas solapadas: N([+/-0.9,+/-0.9], 1.3^2 I).\"\"\"
    X = np.vstack([
        rng_data.normal([ 0.9,  0.9], 1.3, (n, 2)),
        rng_data.normal([-0.9, -0.9], 1.3, (n, 2))
    ])
    d = np.array([1]*n + [-1]*n)
    return X, d

def make_xor():
    \"\"\"4 patrones XOR en {-1,+1}^2.\"\"\"
    X = np.array([[-1,-1], [-1,1], [1,-1], [1,1]], dtype=float)
    d = np.array([-1, 1, 1, -1], dtype=float)
    return X, d

# Generar datasets
X_sep, d_sep = make_separable()
X_nosep, d_nosep = make_nonseparable()
X_xor, d_xor = make_xor()

# Two-moons (scikit-learn)
moons_data = make_moons(n_samples=300, noise=0.20, random_state=SEED)
X_moons, d_moons_raw = moons_data
d_moons = np.where(d_moons_raw == 0, -1.0, 1.0)

print(\"✅ Datos sinteticos generados:\")
print(f\"   Separable:     {X_sep.shape[0]} pts, clases +1/-1\")
print(f\"   No separable:  {X_nosep.shape[0]} pts, clases +1/-1\")
print(f\"   XOR:           {X_xor.shape[0]} pts, d={d_xor}\")
print(f\"   Two-moons:     {X_moons.shape[0]} pts\")""")

# ═══════════════════════════════════════════════════════════════
# CELDA 5: Datos reales
# ═══════════════════════════════════════════════════════════════
code("""# ── Carga y preprocesamiento de datasets reales ──

# === IRIS (Fisher, 1936; UCI) ===
iris = load_iris()
X_iris_raw, y_iris_raw = iris.data, iris.target
X_iris_train, X_iris_test, y_iris_train, y_iris_test = train_test_split(
    X_iris_raw, y_iris_raw, test_size=0.3, random_state=42, stratify=y_iris_raw)
X_iris_train_n, X_iris_test_n = normalize_features(X_iris_train, X_iris_test)
d_iris_train_oh = one_hot(y_iris_train, 3)
d_iris_test_oh  = one_hot(y_iris_test, 3)

# Subconjuntos binarios para Perceptron
d_setosa_train = np.where(y_iris_train == 0, 1.0, -1.0)
d_setosa_test  = np.where(y_iris_test  == 0, 1.0, -1.0)
mask_vv = (y_iris_train == 1) | (y_iris_train == 2)
X_vv_train = X_iris_train_n[mask_vv]; d_vv_train = np.where(y_iris_train[mask_vv] == 1, 1.0, -1.0)
mask_vv_t  = (y_iris_test  == 1) | (y_iris_test  == 2)
X_vv_test  = X_iris_test_n[mask_vv_t];  d_vv_test  = np.where(y_iris_test[mask_vv_t]   == 1, 1.0, -1.0)

# === WINE (UCI) ===
wine = load_wine()
X_wine_raw, y_wine_raw = wine.data, wine.target
d_wine_bin = np.where(y_wine_raw == 0, 1.0, -1.0)
X_wt, X_wv, d_wt, d_wv = train_test_split(
    X_wine_raw, d_wine_bin, test_size=0.3, random_state=42, stratify=d_wine_bin)
X_wine_train_n, X_wine_test_n = normalize_features(X_wt, X_wv)

# === MNIST reducido (digitos 0-4, 8x8=64 features, UCI) ===
digits = load_digits()
X_digits_raw, y_digits_raw = digits.data, digits.target
mask_04 = y_digits_raw <= 4
X_digits_raw = X_digits_raw[mask_04]; y_digits_raw = y_digits_raw[mask_04]
X_dt, X_dv, y_dt, y_dv = train_test_split(
    X_digits_raw, y_digits_raw, test_size=0.3, random_state=42, stratify=y_digits_raw)
X_digits_train_n, X_digits_test_n = normalize_features(X_dt, X_dv)
d_digits_train_oh = one_hot(y_dt, 5); d_digits_test_oh = one_hot(y_dv, 5)

print(\"✅ Datos reales cargados y normalizados a [-1,1]:\")
print(f\"   Iris:        train={X_iris_train_n.shape[0]}, test={X_iris_test_n.shape[0]}, 4 feat, 3 clases\")
print(f\"   Wine:        train={X_wine_train_n.shape[0]}, test={X_wine_test_n.shape[0]}, 13 feat, binario\")
print(f\"   MNIST-04:    train={X_digits_train_n.shape[0]}, test={X_digits_test_n.shape[0]}, 64 feat, 5 clases\")""")

print(f"[gen_notebook] Celdas 0-5 generadas. Total: {len(cells)}")
nb.cells = cells
nbf.write(nb, OUT)
print(f"[gen_notebook] Notebook parcial guardado en {OUT}")
