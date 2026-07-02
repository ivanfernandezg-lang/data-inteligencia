"""
Parte 2: Agrega algoritmos al notebook existente.
"""
import nbformat as nbf

IN  = "C:/Developer/data-inteligencia/proyectos/RNA/notebook/v1/implementacion-widrow-lehr.ipynb"
OUT = IN

with open(IN, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

cells = list(nb.cells)

def md(s):
    cells.append(nbf.v4.new_markdown_cell(s))

def code(s):
    cells.append(nbf.v4.new_code_cell(s))

# ── CELDA 6 ──
md("""## Algoritmos de Aprendizaje -- Un Solo Elemento

Implementaciones desde cero en NumPy puro de los algoritmos para un unico
elemento adaptativo (Adaline). Todas usan presentacion aleatoria por epoca.
Convencion: $d \\in \\{-1, +1\\}$, entradas con bias $x_0 = +1$.

Referencias: Widrow & Lehr (1990), Secciones IV y VI.""")

# ── CELDA 7: Perceptron ──
code("""# -------------------------------------------------------------------
# Regla del Perceptron (Rosenblatt, 1958) -- Eq. (18)
# W_{k+1} = W_k + alpha * (epsilon_tilde_k / 2) * X_k
# epsilon_tilde_k = d_k - y_k in {-2, 0, +2}
# Solo adapta si la decision es incorrecta.
# Teorema: converge en pasos finitos si los datos son linealmente
# separables; si no, el vector de pesos tiende a cero.
# -------------------------------------------------------------------

def train_perceptron(X_raw, d, alpha=1.0, max_epochs=200, seed=SEED):
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

        yp = np.sign(np.dot(Xb, W))
        yp[yp == 0] = 1.0
        acc_hist.append(accuracy_fn(d, yp))
        wnorm_hist.append(np.linalg.norm(W))
        if errors == 0 and conv_epoch < 0:
            conv_epoch = epoch

    return W, {
        'epochs_to_converge': conv_epoch,
        'acc_history': np.array(acc_hist),
        'w_norm_history': np.array(wnorm_hist)
    }

# Test rapido
Wp_test, hp_test = train_perceptron(X_sep, d_sep)
print(f"Perceptron separable: converge en {hp_test['epochs_to_converge']} epocas, acc={hp_test['acc_history'][-1]:.4f}")
""")

# ── CELDA 8: alpha-LMS ──
code("""# -------------------------------------------------------------------
# alpha-LMS / Regla Delta de Widrow-Hoff (1960) -- Eq. (10)
# W_{k+1} = W_k + alpha * (epsilon_k / ||X_k||^2) * X_k
# epsilon_k = d_k - s_k  (error LINEAL)
# Rango estable: 0 < alpha < 2. Practico: 0.1 < alpha < 1.0.
# Cambio de peso colineal con X_k = minima perturbacion geometrica.
# -------------------------------------------------------------------

def train_alpha_lms(X_raw, d, alpha=0.5, max_epochs=200, seed=SEED):
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

    return W, {
        'mse_history': np.array(mse_hist),
        'acc_history': np.array(acc_hist),
        'w_norm_history': np.array(wnorm_hist)
    }

Wa_test, ha_test = train_alpha_lms(X_sep, d_sep, alpha=0.5)
print(f"alpha-LMS separable: MSE={ha_test['mse_history'][-1]:.6f}, acc={ha_test['acc_history'][-1]:.4f}")
""")

# ── CELDA 9: mu-LMS ──
code("""# -------------------------------------------------------------------
# mu-LMS / Descenso por gradiente estocastico -- Eq. (33)
# W_{k+1} = W_k + 2*mu * epsilon_k * X_k
# Estabilidad: 0 < mu < 1/tr[R].
# Superficie MSE: hiperparaboloide CONVEXO, unico minimo global W*.
# Gradiente instantaneo: INSESGADO.
# -------------------------------------------------------------------

def train_mu_lms(X_raw, d, mu=0.01, max_epochs=200, seed=SEED):
    rng = np.random.default_rng(seed)
    Xb = add_bias(X_raw)
    N, nw = Xb.shape
    W = np.zeros(nw)
    mse_hist, acc_hist, wnorm_hist = [], [], []
    w_traj = [W.copy()]

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
        if epoch <= 50:
            w_traj.append(W.copy())

    return W, {
        'mse_history': np.array(mse_hist),
        'acc_history': np.array(acc_hist),
        'w_norm_history': np.array(wnorm_hist),
        'weight_trajectory': np.array(w_traj)
    }

Wmu_test, hmu_test = train_mu_lms(X_sep, d_sep, mu=0.02)
print(f"mu-LMS separable: MSE={hmu_test['mse_history'][-1]:.6f}, acc={hmu_test['acc_history'][-1]:.4f}")
""")

# ── CELDA 10: Seccion Redes ──
md("""## Algoritmos de Aprendizaje -- Redes Multicapa

Implementaciones desde cero en NumPy puro:
1. **MLP con Backpropagation** (Rumelhart, Hinton & Williams, 1986)
2. **Madaline Rule II -- MRII** (Widrow, Winter & Baxter, 1987)
3. **Madaline Rule III -- MRIII** (Andes, 1988) $\\equiv$ Backpropagation

Referencias: Widrow & Lehr (1990), Secciones V, VI y VII.""")

# ── CELDA 11: Clase MLP ──
code("""# -------------------------------------------------------------------
# MLP con Backpropagation
# Deltas: salida delta^(L) = eps * sgm'(s), Eq. 78/79
#         ocultas delta^(l) = (W^(l+1)^T * delta^(l+1)) .* sgm'(s^(l)), Eq. 87
# Actualizacion: DeltaW = 2*mu * delta * x^T, Eq. 94
# Momentum: V = eta*V + (1-eta)*2*mu*delta*x^T, Eqs. 96-97
# -------------------------------------------------------------------

class MLP:
    def __init__(self, layer_sizes, mu=0.01, momentum=0.0, seed=SEED):
        self.L = len(layer_sizes) - 1
        self.mu = mu
        self.momentum = momentum
        self.rng = np.random.default_rng(seed)
        self.W = []
        self.V = []
        for l in range(self.L):
            n_in_l = layer_sizes[l] + 1
            n_out_l = layer_sizes[l + 1]
            Wl = self.rng.uniform(-0.5, 0.5, (n_out_l, n_in_l))
            self.W.append(Wl)
            self.V.append(np.zeros_like(Wl))

    def forward(self, x):
        acts = [np.append(1.0, x)]
        sums = []
        a = x.copy()
        for l in range(self.L):
            a_bias = np.append(1.0, a)
            s = self.W[l] @ a_bias
            sums.append(s)
            a = sigmoid(s)
            acts.append(np.append(1.0, a))
        return acts, sums

    def _backprop_deltas(self, acts, sums, d_target):
        deltas = [None] * self.L
        y_out = acts[-1][1:]
        eps = d_target - y_out
        deltas[-1] = eps * sigmoid_derivative(y_out)

        for l in range(self.L - 2, -1, -1):
            y_hidden = acts[l + 1][1:]
            W_next = self.W[l + 1][:, 1:]
            delta_next = deltas[l + 1]
            deltas[l] = (W_next.T @ delta_next) * sigmoid_derivative(y_hidden)

        return deltas

    def train_pattern(self, x, d_target):
        acts, sums = self.forward(x)
        deltas = self._backprop_deltas(acts, sums, d_target)
        for l in range(self.L):
            a_in = acts[l]
            delta = deltas[l]
            dw = 2 * self.mu * np.outer(delta, a_in)
            if self.momentum > 0:
                self.V[l] = self.momentum * self.V[l] + (1 - self.momentum) * dw
                self.W[l] += self.V[l]
            else:
                self.W[l] += dw

    def fit(self, X, d, epochs=100, verbose=False, seed=None):
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
            if verbose and ep % max(1, epochs//10) == 0:
                print(f"  Ep {ep:4d}/{epochs}: MSE={mse_hist[-1]:.6f}, acc={acc_hist[-1]:.4f}")
        return {'mse_history': np.array(mse_hist), 'acc_history': np.array(acc_hist)}

    def predict_batch(self, X):
        preds = np.zeros((len(X), self.W[-1].shape[0]))
        for i in range(len(X)):
            acts, _ = self.forward(X[i])
            preds[i] = acts[-1][1:]
        return preds

    def accuracy(self, X, d_onehot):
        preds = self.predict_batch(X)
        y_pred = np.argmax(preds, axis=1)
        y_true = np.argmax(d_onehot, axis=1) if d_onehot.ndim == 2 else np.where(d_onehot > 0, 1, 0)
        return accuracy_fn(y_true, y_pred)

# Test rapido XOR
mlp_test = MLP([2, 2, 1], mu=0.1, momentum=0.0)
hist_test = mlp_test.fit(X_xor, d_xor.reshape(-1,1), epochs=400)
print(f"MLP(2,2,1) XOR: MSE={hist_test['mse_history'][-1]:.6f}, acc={hist_test['acc_history'][-1]:.4f}")
""")

print(f"[p2] Celdas 6-11 agregadas. Total: {len(cells)}")
nb.cells = cells
nbf.write(nb, OUT)
print(f"[p2] Guardado.")
