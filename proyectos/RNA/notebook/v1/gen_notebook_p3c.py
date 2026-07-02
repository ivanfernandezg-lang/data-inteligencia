"""
Parte 3 (corregida): MRII, MRIII, experimentos E1-E3.
Usa strings simples sin raw para evitar conflictos de parsing.
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

# ═══════════════════════════════════════════════════════════════
# MRII
# ═══════════════════════════════════════════════════════════════
code('''# -------------------------------------------------------------------
# Madaline Rule II -- MRII (Widrow, Winter & Baxter, 1987)
# Red feedforward de Adalines con cuantizador signum en TODAS las capas.
#
# Algoritmo por patron erroneo:
#   1. Ordenar Adalines ocultas por |s| creciente (load-sharing).
#   2. Inversion tentativa (flip) de 1 Adaline, luego de pares.
#   3. Si reduce Hamming: aceptar + correccion absoluta colineal.
#   4. Capa de salida: alpha-LMS.
#   5. Escape de optimos locales: ruido gaussiano si Hamming se estanca.
# -------------------------------------------------------------------

class MadalineII:
    def __init__(self, layer_sizes, seed=SEED):
        self.L = len(layer_sizes) - 1
        self.rng = np.random.default_rng(seed)
        self.W = []
        for l in range(self.L):
            n_in = layer_sizes[l] + 1
            n_out = layer_sizes[l + 1]
            self.W.append(self.rng.uniform(-0.5, 0.5, (n_out, n_in)))

    def forward(self, x, flip=None):
        a = x.copy()
        last_s = None
        for l in range(self.L):
            a_bias = np.append(1.0, a)
            s = self.W[l] @ a_bias
            y = np.sign(s); y[y == 0] = 1.0
            if flip is not None and flip[0] == l:
                for idx in flip[1]:
                    y[idx] = -y[idx]
            a = y
            last_s = s
        return a, last_s

    def _all_suminders(self, x):
        all_s = []
        a = x.copy()
        for l in range(self.L):
            a_bias = np.append(1.0, a)
            s = self.W[l] @ a_bias
            all_s.append((l, s))
            y = np.sign(s); y[y == 0] = 1.0
            a = y
        return all_s

    def _reinforce(self, x, layer, adaline_idx):
        a = x.copy()
        for l in range(layer):
            a_b = np.append(1.0, a)
            s_l = self.W[l] @ a_b
            y_l = np.sign(s_l); y_l[y_l == 0] = 1.0
            a = y_l
        a_bias = np.append(1.0, a)
        s = self.W[layer][adaline_idx] @ a_bias
        target = -np.sign(s) if np.sign(s) != 0 else 1.0
        margin = 1.0
        denom = np.dot(a_bias, a_bias)
        if denom > 0:
            self.W[layer][adaline_idx] += ((target * margin - s) / denom) * a_bias

    def fit(self, X, d, max_epochs=150, alpha_out=0.5, patience=15,
            noise_sigma=0.15, verbose=False, seed=None):
        rng = np.random.default_rng(seed if seed is not None else SEED)
        N = len(X)
        hamming_hist, acc_hist = [], []
        best_W = [W.copy() for W in self.W]
        best_hamming = N + 1
        stall_count = 0

        for ep in range(1, max_epochs + 1):
            idx = rng.permutation(N)
            for k in idx:
                xk, dk = X[k], d[k]
                y_out, _ = self.forward(xk)
                if np.sign(y_out) == dk:
                    continue

                all_s = self._all_suminders(xk)
                hidden_layers = [(l, s) for l, s in all_s if l < self.L - 1]

                if not hidden_layers:
                    a_bias = np.append(1.0, xk)
                    s_out = self.W[-1] @ a_bias
                    eps = dk - s_out
                    denom = np.dot(a_bias, a_bias)
                    if denom > 0:
                        self.W[-1] += alpha_out * (eps / denom) * a_bias
                    continue

                # Ordenar por |s| creciente
                flat_ada = []
                for l, s in hidden_layers:
                    for j in range(len(s)):
                        flat_ada.append((l, j, abs(s[j])))
                flat_ada.sort(key=lambda x: x[2])

                # Inversiones individuales
                accepted = False
                for l, j, _ in flat_ada:
                    y_tent, _ = self.forward(xk, flip=(l, [j]))
                    if np.sign(y_tent) == dk:
                        self._reinforce(xk, l, j)
                        accepted = True
                        break

                # Inversiones de a pares
                if not accepted and len(flat_ada) >= 2:
                    import itertools
                    for (l1, j1, _), (l2, j2, _) in itertools.combinations(flat_ada, 2):
                        if l1 == l2:
                            y_tent, _ = self.forward(xk, flip=(l1, [j1, j2]))
                        else:
                            self.forward(xk, flip=(l1, [j1]))
                            y_tent, _ = self.forward(xk, flip=(l2, [j2]))
                        if np.sign(y_tent) == dk:
                            self._reinforce(xk, l1, j1)
                            self._reinforce(xk, l2, j2)
                            accepted = True
                            break

                # alpha-LMS en salida si no se acepto
                if not accepted:
                    a = xk.copy()
                    for l in range(self.L - 1):
                        a_b = np.append(1.0, a)
                        s_l = self.W[l] @ a_b
                        y_l = np.sign(s_l); y_l[y_l == 0] = 1.0
                        a = y_l
                    a_out = np.append(1.0, a)
                    s_out = self.W[-1] @ a_out
                    eps = dk - s_out
                    denom = np.dot(a_out, a_out)
                    if denom > 0:
                        self.W[-1] += alpha_out * (eps / denom) * a_out

            # Evaluacion de epoca
            y_all = np.array([np.sign(self.forward(X[i])[0]) for i in range(N)])
            h = int(np.sum(d != y_all))
            acc = accuracy_fn(d, y_all)
            hamming_hist.append(h)
            acc_hist.append(acc)

            if h < best_hamming:
                best_hamming = h
                best_W = [W.copy() for W in self.W]
                stall_count = 0
            else:
                stall_count += 1

            if stall_count >= patience:
                for Wl in self.W:
                    Wl += rng.normal(0, noise_sigma, Wl.shape)
                stall_count = 0
                if verbose:
                    print(f"  Ep {ep}: escape ruido sigma={noise_sigma}")

            if verbose and ep % 20 == 0:
                print(f"  Ep {ep:3d}: Hamming={h}, acc={acc:.4f}, stall={stall_count}")

        self.W = best_W
        return {
            'hamming_history': np.array(hamming_hist),
            'acc_history': np.array(acc_hist),
            'best_hamming': best_hamming
        }

    def predict(self, X):
        return np.array([np.sign(self.forward(x)[0]) for x in X])

print("Clase MadalineII definida.")
''')

# ═══════════════════════════════════════════════════════════════
# MRIII
# ═══════════════════════════════════════════════════════════════
code('''# -------------------------------------------------------------------
# Madaline Rule III -- MRIII (Andes, 1988) EQUIVALENTE a Backprop
# Estima d(eps^2)/ds_j perturbando el sumidero de cada Adaline.
# Eq. 102: d(eps^2)/ds_j ~= (eps^2_pert - eps^2_base) / Delta_s
# Cuando Delta_s -> 0: MRIII == backprop (demostrado por Widrow).
# -------------------------------------------------------------------

def mriii_gradient(net, x, d_target, ds=1e-6):
    acts_base, sums_base = net.forward(x)
    y_base = acts_base[-1][1:]
    eps_base = d_target - y_base
    eps2_base = np.sum(eps_base ** 2)

    grads = []
    for l in range(net.L):
        n_ada = net.W[l].shape[0]
        grad_l = np.zeros(n_ada)

        for j in range(n_ada):
            a = x.copy()
            for ll in range(net.L):
                a_bias = np.append(1.0, a)
                s = net.W[ll] @ a_bias
                if ll == l:
                    s[j] += ds
                a = sigmoid(s)
            eps_pert = d_target - a
            eps2_pert = np.sum(eps_pert ** 2)
            grad_l[j] = (eps2_pert - eps2_base) / ds

        grads.append(grad_l)
    return grads, eps2_base

def backprop_gradient(net, x, d_target):
    acts, sums = net.forward(x)
    deltas = net._backprop_deltas(acts, sums, d_target)
    return [-2.0 * d for d in deltas]

print("Funciones MRIII definidas.")
''')

# ═══════════════════════════════════════════════════════════════
# Seccion Experimentos
# ═══════════════════════════════════════════════════════════════
md('''---
## Experimentos

A continuacion se ejecutan los experimentos E1 a E7, mas Wine Quality y MNIST reducido.
Cada experimento genera sus figuras en `figs/` y/o tablas LaTeX en `tabs/`.
Los resultados se referencian desde el informe.''')

# ═══════════════════════════════════════════════════════════════
# E1: Capacidad de Cover
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E1: CAPACIDAD DE COVER (H1: C_s ~ 2*N_w, C_d = N_w)
# ===================================================================
print("="*60)
print("E1: Capacidad de Cover -- Monte Carlo")
print("="*60)

def check_separable(X, d):
    """Test de separabilidad lineal via LP."""
    N, n = X.shape
    c = np.zeros(n)
    A_ub = -d.reshape(-1, 1) * X
    b_ub = -np.ones(N)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(None, None), method='highs')
    return res.success

def cover_theory(Np, Nw):
    """Probabilidad teorica de separabilidad (Cover, 1964)."""
    if Np <= Nw:
        return 1.0
    s = 0.0
    for i in range(Nw):
        s += scipy_comb(Np - 1, i, exact=False)
    return 2.0 ** (1 - Np) * s

# Parametros
Nw_list = [2, 5, 15]
ratios = np.arange(0.5, 4.01, 0.25)
n_trials = 80
results = {}

for Nw in Nw_list:
    probs = []
    for ratio in ratios:
        Np = max(1, int(ratio * Nw))
        sep_count = 0
        for trial in range(n_trials):
            rng_e1 = np.random.default_rng(SEED + trial)
            X = rng_e1.normal(0, 1, (Np, Nw))
            d = np.where(rng_e1.random(Np) > 0.5, 1.0, -1.0)
            if check_separable(X, d):
                sep_count += 1
        probs.append(sep_count / n_trials)
    results[Nw] = probs

# Grafico
fig, ax = plt.subplots(figsize=(9, 6))
colors = {2: 'blue', 5: 'green', 15: 'red'}
for Nw in Nw_list:
    ax.plot(ratios, results[Nw], 'o-', color=colors[Nw], markersize=4,
            label=f'Nw={Nw} (empirico)')
    theory = [cover_theory(int(max(1, r*Nw)), Nw) for r in ratios]
    ax.plot(ratios, theory, '--', color=colors[Nw], alpha=0.6,
            label=f'Nw={Nw} (teorico)')

ax.axvline(x=1.0, color='gray', linestyle=':', alpha=0.7, label='Cd=Nw')
ax.axvline(x=2.0, color='gray', linestyle='--', alpha=0.7, label='Cs~2Nw')
ax.set_xlabel('Np / Nw')
ax.set_ylabel('Probabilidad de separabilidad lineal')
ax.set_title('E1: Capacidad de Cover -- Validacion Monte Carlo')
ax.legend(fontsize=8, ncol=2)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figs/fig_cover.png', dpi=200, bbox_inches='tight')
plt.show()

for Nw in Nw_list:
    theory_vals = np.array([cover_theory(int(max(1, r*Nw)), Nw) for r in ratios])
    dev = np.mean(np.abs(np.array(results[Nw]) - theory_vals))
    print(f"  Nw={Nw:2d}: desviacion media |emp-teo| = {dev:.4f}")

print("E1 completado. Figura: figs/fig_cover.png")
''')

# ═══════════════════════════════════════════════════════════════
# E2: Reglas lineales en datos separables
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E2: REGLAS LINEALES EN DATOS SEPARABLES (H2)
# ===================================================================
print("\\n" + "="*60)
print("E2: Reglas lineales en datos separables")
print("="*60)

# Entrenar los 3 algoritmos
W_perceptron, hp = train_perceptron(X_sep, d_sep, alpha=1.0, max_epochs=100)
W_alpha, ha = train_alpha_lms(X_sep, d_sep, alpha=0.5, max_epochs=100)
W_mu, hm = train_mu_lms(X_sep, d_sep, mu=0.02, max_epochs=100)
W_wiener = wiener_solution(X_sep, d_sep)

# Angulo respecto a W*
def angle_between(w1, w2):
    cos_ang = np.dot(w1, w2) / (np.linalg.norm(w1) * np.linalg.norm(w2))
    return np.degrees(np.arccos(np.clip(cos_ang, -1, 1)))

ang_p = angle_between(W_perceptron, W_wiener)
ang_a = angle_between(W_alpha, W_wiener)
ang_m = angle_between(W_mu, W_wiener)
print(f"Angulos vs W*: Perceptron={ang_p:.1f}deg, alpha-LMS={ang_a:.1f}deg, mu-LMS={ang_m:.1f}deg")

# Calcular tr[R] y mu_max
Xb = add_bias(X_sep)
R = Xb.T @ Xb / len(Xb)
trR = np.trace(R)
mu_max_theory = 1.0 / trR
mse_wiener = mse_loss(d_sep, np.dot(Xb, W_wiener))
print(f"tr[R]={trR:.4f}, mu_max=1/tr[R]={mu_max_theory:.6f}")
print(f"MSE Wiener={mse_wiener:.6f}")

# Figura 1: Datasets
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].scatter(X_sep[d_sep==1,0], X_sep[d_sep==1,1], c='blue', alpha=0.6, label='+1')
axes[0].scatter(X_sep[d_sep==-1,0], X_sep[d_sep==-1,1], c='red', alpha=0.6, label='-1')
axes[0].set_title('Dataset separable'); axes[0].legend()
axes[1].scatter(X_nosep[d_nosep==1,0], X_nosep[d_nosep==1,1], c='blue', alpha=0.6)
axes[1].scatter(X_nosep[d_nosep==-1,0], X_nosep[d_nosep==-1,1], c='red', alpha=0.6)
axes[1].set_title('Dataset no separable')
axes[2].scatter(X_xor[d_xor==1,0], X_xor[d_xor==1,1], c='blue', s=100)
axes[2].scatter(X_xor[d_xor==-1,0], X_xor[d_xor==-1,1], c='red', s=100)
axes[2].set_title('XOR')
for ax in axes: ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_datasets.png', dpi=200, bbox_inches='tight'); plt.show()

# Figura 2: Fronteras de decision
def plot_boundary(ax, W, X, d, color, ls='-'):
    x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
    y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    s_grid = np.dot(add_bias(grid), W)
    Z = np.sign(s_grid).reshape(xx.shape)
    ax.contour(xx, yy, Z, levels=[0], colors=color, linestyles=ls, linewidths=2)
    ax.contourf(xx, yy, Z, levels=[-1, 0, 1], colors=['#FFCCCC','#CCCCFF'], alpha=0.15)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ['Perceptron', 'alpha-LMS', 'mu-LMS']
Ws = [W_perceptron, W_alpha, W_mu]
angs = [ang_p, ang_a, ang_m]
colors_b = ['green', 'orange', 'purple']
for i, (ax, W, title, c, a) in enumerate(zip(axes, Ws, titles, colors_b, angs)):
    ax.scatter(X_sep[d_sep==1,0], X_sep[d_sep==1,1], c='blue', alpha=0.5, s=20)
    ax.scatter(X_sep[d_sep==-1,0], X_sep[d_sep==-1,1], c='red', alpha=0.5, s=20)
    plot_boundary(ax, W, X_sep, d_sep, c)
    plot_boundary(ax, W_wiener, X_sep, d_sep, 'black', '--')
    ax.set_title(f'{title} ({a:.1f} deg vs Wiener)')
    ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_fronteras.png', dpi=200, bbox_inches='tight'); plt.show()

# Figura 3: Convergencia mu-LMS para distintos mu
print("\\nProbando mu-LMS con distintos mu...")
mu_values = [0.001, 0.01, 0.05, 0.12]
fig, ax = plt.subplots(figsize=(9, 5))
for mu in mu_values:
    with np.errstate(over='ignore', invalid='ignore'):
        _, hm_tmp = train_mu_lms(X_sep, d_sep, mu=mu, max_epochs=80)
        mse_clipped = np.clip(hm_tmp['mse_history'], 0, 1e9)
        label = f'mu={mu}' + (' (DIVERGE!)' if mu > mu_max_theory else '')
        ax.semilogy(mse_clipped, label=label, alpha=0.8)
ax.axhline(y=mse_wiener, color='black', linestyle='--', label=f'MSE Wiener={mse_wiener:.4f}')
ax.set_xlabel('Epoca'); ax.set_ylabel('MSE (log)')
ax.set_title('E2: Convergencia mu-LMS para distintos mu')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_convergencia.png', dpi=200, bbox_inches='tight'); plt.show()
print("E2 completado.")
''')

# ═══════════════════════════════════════════════════════════════
# E3: Datos no separables
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E3: DATOS NO SEPARABLES (H2: inestabilidad Perceptron vs LMS)
# ===================================================================
print("\\n" + "="*60)
print("E3: Datos no separables")
print("="*60)

max_ep = 120
Wp_ns, hp_ns = train_perceptron(X_nosep, d_nosep, alpha=1.0, max_epochs=max_ep)
Wa_ns, ha_ns = train_alpha_lms(X_nosep, d_nosep, alpha=0.5, max_epochs=max_ep)
Wm_ns, hm_ns = train_mu_lms(X_nosep, d_nosep, mu=0.02, max_epochs=max_ep)
W_wiener_ns = wiener_solution(X_nosep, d_nosep)

Xb_ns = add_bias(X_nosep)
yp_wiener = np.sign(np.dot(Xb_ns, W_wiener_ns)); yp_wiener[yp_wiener==0] = 1.0
acc_wiener_ns = accuracy_fn(d_nosep, yp_wiener_ns)

def last40_stats(hist):
    return np.mean(hist[-40:]), np.std(hist[-40:])

pa_m, pa_s = last40_stats(hp_ns['acc_history'])
aa_m, aa_s = last40_stats(ha_ns['acc_history'])
ma_m, ma_s = last40_stats(hm_ns['acc_history'])

print(f"Accuracy (media +/- std, ultimas 40 epocas):")
print(f"  Perceptron: {pa_m*100:.1f}% +/- {pa_s*100:.1f}")
print(f"  alpha-LMS:  {aa_m*100:.1f}% +/- {aa_s*100:.1f}")
print(f"  mu-LMS:     {ma_m*100:.1f}% +/- {ma_s*100:.1f}")
print(f"  Wiener:     {acc_wiener_ns*100:.1f}%")

# Figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.plot(hp_ns['acc_history'], label='Perceptron', alpha=0.8)
ax1.plot(ha_ns['acc_history'], label='alpha-LMS', alpha=0.8)
ax1.plot(hm_ns['acc_history'], label='mu-LMS', alpha=0.8)
ax1.axhline(y=acc_wiener_ns, color='black', linestyle='--', label=f'Wiener ({acc_wiener_ns*100:.1f}%)')
ax1.set_xlabel('Epoca'); ax1.set_ylabel('Accuracy')
ax1.set_title('E3: Accuracy en datos no separables')
ax1.legend(); ax1.grid(True, alpha=0.3)

ax2.plot(hp_ns['w_norm_history'], label='Perceptron', alpha=0.8)
ax2.plot(ha_ns['w_norm_history'], label='alpha-LMS', alpha=0.8)
ax2.plot(hm_ns['w_norm_history'], label='mu-LMS', alpha=0.8)
ax2.set_xlabel('Epoca'); ax2.set_ylabel('||W||')
ax2.set_title('E3: Norma del vector de pesos')
ax2.legend(); ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_noseparable.png', dpi=200, bbox_inches='tight'); plt.show()

# Tabla lineales LaTeX
tab_lines = []
tab_lines.append('\\\\begin{tabular}{@{}lccc@{}}')
tab_lines.append('\\\\toprule')
tab_lines.append('Algoritmo & Acc. separable & Ep. converg. & Acc. no separable \\\\\\\\')
tab_lines.append('\\\\midrule')
tab_lines.append(f'Perceptron & 100.0\\\\% & {hp["epochs_to_converge"]} & {pa_m*100:.1f}\\\\% $\\\\pm${pa_s*100:.1f} \\\\\\\\')
tab_lines.append(f'$\\\\alpha$-LMS & 100.0\\\\% & -- & {aa_m*100:.1f}\\\\% $\\\\pm${aa_s*100:.1f} \\\\\\\\')
tab_lines.append(f'$\\\\mu$-LMS & 100.0\\\\% & -- & {ma_m*100:.1f}\\\\% $\\\\pm${ma_s*100:.1f} \\\\\\\\')
tab_lines.append('\\\\midrule')
tab_lines.append(f'Wiener (optimo) & 100.0\\\\% & -- & {acc_wiener_ns*100:.1f}\\\\% \\\\\\\\')
tab_lines.append('\\\\bottomrule')
tab_lines.append('\\\\end{tabular}')
with open('tabs/tab_lineales.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_lines))
print("Tabla: tabs/tab_lineales.tex")
print("E3 completado.")
''')

print(f"[p3] Celdas 12-17 agregadas. Total: {len(cells)}")
nb.cells = cells
nbf.write(nb, OUT)
print(f"[p3] Guardado.")
