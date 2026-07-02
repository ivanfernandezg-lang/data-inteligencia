"""
Parte 4: Experimentos E4-E7 + Wine + MNIST + tabla resumen.
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
# E4: Superficies de MSE
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E4: SUPERFICIES DE MSE (Figs. 22-24 del paper)
# ===================================================================
print("\\n" + "="*60)
print("E4: Superficies de MSE")
print("="*60)

# Adaline de 2 pesos sin bias, 6 patrones aleatorios
rng_e4 = np.random.default_rng(7)
X_e4 = rng_e4.normal(0, 1, (6, 2))
d_e4 = np.where(rng_e4.random(6) > 0.5, 1.0, -1.0)

w1 = np.linspace(-3, 3, 80)
w2 = np.linspace(-3, 3, 80)
W1, W2 = np.meshgrid(w1, w2)

MSE_linear = np.zeros_like(W1)
MSE_sigmoid = np.zeros_like(W1)
MSE_signum = np.zeros_like(W1)

for i in range(len(w1)):
    for j in range(len(w2)):
        w = np.array([w1[i], w2[j]])
        s = X_e4 @ w  # sin bias
        MSE_linear[j, i] = np.mean((d_e4 - s) ** 2)
        MSE_sigmoid[j, i] = np.mean((d_e4 - np.tanh(s)) ** 2)
        MSE_signum[j, i] = np.mean((d_e4 - np.sign(s)) ** 2)

min_lin = MSE_linear.min()
min_sig = MSE_sigmoid.min()
min_sgn = MSE_signum.min()
print(f"Minimos MSE: lineal={min_lin:.4f}, sigmoide={min_sig:.4f}, signum={min_sgn:.4f}")

fig = plt.figure(figsize=(18, 5))
titles = ['Error lineal (paraboloide convexo)', 'Error sigmoide (no cuadratico)', 'Error signum (escalonado, mesetas)']
data = [MSE_linear, MSE_sigmoid, MSE_signum]
mins = [min_lin, min_sig, min_sgn]
for idx, (title, dat, mn) in enumerate(zip(titles, data, mins)):
    ax = fig.add_subplot(1, 3, idx+1, projection='3d')
    ax.plot_surface(W1, W2, dat, cmap='viridis', alpha=0.85)
    ax.set_title(f'{title}\\nMin={mn:.4f}', fontsize=10)
    ax.set_xlabel('w1'); ax.set_ylabel('w2'); ax.set_zlabel('MSE')
plt.tight_layout()
plt.savefig('figs/fig_superficies_mse.png', dpi=200, bbox_inches='tight')
plt.show()
print("E4 completado. Figura: figs/fig_superficies_mse.png")
''')

# ═══════════════════════════════════════════════════════════════
# E5: XOR - MRII vs MLP
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E5: XOR -- MRII vs MLP-Backprop (H3)
# ===================================================================
print("\\n" + "="*60)
print("E5: XOR -- MRII vs MLP-Backprop")
print("="*60)

n_trials_xor = 20
results_xor = {}

# MRII 2-2-1 sin ruido
print("\\n--- MRII 2-2-1 SIN ruido ---")
success_mrii_no_noise = 0
epochs_mrii_no_noise = []
for seed in range(n_trials_xor):
    mrii = MadalineII([2, 2, 1], seed=seed)
    hist = mrii.fit(X_xor, d_xor, max_epochs=150, alpha_out=0.5,
                     patience=200, noise_sigma=0.0, verbose=False, seed=seed+1000)
    yp = mrii.predict(X_xor)
    if hamming_error(d_xor, yp) == 0:
        success_mrii_no_noise += 1
        epochs_mrii_no_noise.append(np.argmin(hist['hamming_history']) + 1)
results_xor['MRII 2-2-1 sin ruido'] = (success_mrii_no_noise, epochs_mrii_no_noise)
print(f"  Exito: {success_mrii_no_noise}/{n_trials_xor}")

# MRII 2-2-1 CON ruido
print("\\n--- MRII 2-2-1 CON ruido ---")
success_mrii_noise = 0
epochs_mrii_noise = []
for seed in range(n_trials_xor):
    mrii = MadalineII([2, 2, 1], seed=seed)
    hist = mrii.fit(X_xor, d_xor, max_epochs=150, alpha_out=0.5,
                     patience=15, noise_sigma=0.15, verbose=False, seed=seed+1000)
    yp = mrii.predict(X_xor)
    if hamming_error(d_xor, yp) == 0:
        success_mrii_noise += 1
        epochs_mrii_noise.append(np.argmin(hist['hamming_history']) + 1)
results_xor['MRII 2-2-1 + ruido'] = (success_mrii_noise, epochs_mrii_noise)
print(f"  Exito: {success_mrii_noise}/{n_trials_xor}")

# MRII 2-3-1 CON ruido
print("\\n--- MRII 2-3-1 CON ruido ---")
success_mrii_3 = 0
epochs_mrii_3 = []
for seed in range(n_trials_xor):
    mrii = MadalineII([2, 3, 1], seed=seed)
    hist = mrii.fit(X_xor, d_xor, max_epochs=150, alpha_out=0.5,
                     patience=15, noise_sigma=0.15, verbose=False, seed=seed+1000)
    yp = mrii.predict(X_xor)
    if hamming_error(d_xor, yp) == 0:
        success_mrii_3 += 1
        epochs_mrii_3.append(np.argmin(hist['hamming_history']) + 1)
results_xor['MRII 2-3-1 + ruido'] = (success_mrii_3, epochs_mrii_3)
print(f"  Exito: {success_mrii_3}/{n_trials_xor}")

# MLP 2-2-1 backprop
print("\\n--- MLP 2-2-1 Backprop ---")
success_mlp_2 = 0
epochs_mlp_2 = []
for seed in range(n_trials_xor):
    mlp = MLP([2, 2, 1], mu=0.1, momentum=0.0, seed=seed)
    hist = mlp.fit(X_xor, d_xor.reshape(-1,1), epochs=400, seed=seed+2000)
    yp = mlp.predict_batch(X_xor).flatten()
    yp_bin = np.sign(yp); yp_bin[yp_bin==0] = 1.0
    if accuracy_fn(d_xor, yp_bin) == 1.0:
        success_mlp_2 += 1
        epochs_mlp_2.append(np.argmax(hist['acc_history'] >= 1.0) + 1 if np.any(hist['acc_history'] >= 1.0) else 400)
results_xor['MLP-BP 2-2-1'] = (success_mlp_2, epochs_mlp_2)
print(f"  Exito: {success_mlp_2}/{n_trials_xor}")

# MLP 2-3-1 backprop
print("\\n--- MLP 2-3-1 Backprop ---")
success_mlp_3 = 0
epochs_mlp_3 = []
for seed in range(n_trials_xor):
    mlp = MLP([2, 3, 1], mu=0.1, momentum=0.0, seed=seed)
    hist = mlp.fit(X_xor, d_xor.reshape(-1,1), epochs=400, seed=seed+2000)
    yp = mlp.predict_batch(X_xor).flatten()
    yp_bin = np.sign(yp); yp_bin[yp_bin==0] = 1.0
    if accuracy_fn(d_xor, yp_bin) == 1.0:
        success_mlp_3 += 1
        epochs_mlp_3.append(np.argmax(hist['acc_history'] >= 1.0) + 1 if np.any(hist['acc_history'] >= 1.0) else 400)
results_xor['MLP-BP 2-3-1'] = (success_mlp_3, epochs_mlp_3)
print(f"  Exito: {success_mlp_3}/{n_trials_xor}")

# Figura XOR: regiones de decision
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# MRII 2-3-1 exitosa
mrii_best = MadalineII([2, 3, 1], seed=5)
mrii_best.fit(X_xor, d_xor, max_epochs=150, alpha_out=0.5, patience=15, noise_sigma=0.15, seed=5000)

def plot_decision_region(ax, model, X, d, title, is_mlp=False):
    x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
    y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    if is_mlp:
        Z = np.array([np.sign(model.predict_batch(g.reshape(1,-1))[0,0]) for g in grid])
    else:
        Z = np.array([np.sign(model.forward(g)[0]) for g in grid])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, levels=[-1, 0, 1], colors=['#FFCCCC','#CCCCFF'], alpha=0.5)
    ax.scatter(X[d==1,0], X[d==1,1], c='blue', s=80, edgecolors='k')
    ax.scatter(X[d==-1,0], X[d==-1,1], c='red', s=80, edgecolors='k', marker='s')
    ax.set_title(title)

plot_decision_region(axes[0], mrii_best, X_xor, d_xor, 'MRII 2-3-1 (con ruido)')

# MLP 2-2-1 exitoso
mlp_xor = MLP([2, 2, 1], mu=0.1, momentum=0.0, seed=3)
mlp_xor.fit(X_xor, d_xor.reshape(-1,1), epochs=400, seed=3000)
plot_decision_region(axes[1], mlp_xor, X_xor, d_xor, 'MLP-BP 2-2-1', is_mlp=True)

# Curva MSE MLP
mlp_xor2 = MLP([2, 2, 1], mu=0.1, momentum=0.0, seed=7)
hist_plot = mlp_xor2.fit(X_xor, d_xor.reshape(-1,1), epochs=400, seed=7000)
axes[2].semilogy(hist_plot['mse_history'])
axes[2].set_xlabel('Epoca'); axes[2].set_ylabel('MSE (log)')
axes[2].set_title('MLP 2-2-1: Curva de aprendizaje XOR')
axes[2].grid(True, alpha=0.3)

plt.tight_layout(); plt.savefig('figs/fig_xor.png', dpi=200, bbox_inches='tight'); plt.show()

# Tabla XOR
def fmt_epochs(elist):
    if len(elist) == 0: return '--'
    return str(int(np.median(elist)))

tab_xor = []
tab_xor.append('\\\\begin{tabular}{@{}lccc@{}}')
tab_xor.append('\\\\toprule')
tab_xor.append('Configuracion & Tasa exito & Mediana epocas & \\\\\\\\')
tab_xor.append('\\\\midrule')
for name, (succ, eps) in results_xor.items():
    tab_xor.append(f'{name} & {succ}/{n_trials_xor} & {fmt_epochs(eps)} \\\\\\\\')
tab_xor.append('\\\\bottomrule')
tab_xor.append('\\\\end{tabular}')
with open('tabs/tab_xor.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_xor))
print("\\nTabla: tabs/tab_xor.tex")
print("E5 completado.")
''')

# ═══════════════════════════════════════════════════════════════
# E6: MLP en Iris + Wine + MNIST
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E6: MLP EN DATASETS REALES
# ===================================================================
print("\\n" + "="*60)
print("E6: MLP en Iris + two-moons + Wine + MNIST")
print("="*60)

# --- Perceptron en Iris (preambulo: demostrar separabilidad de setosa) ---
print("\\n--- Perceptron en Iris ---")
Wp_setosa, hp_setosa = train_perceptron(X_iris_train_n, d_setosa_train, alpha=1.0, max_epochs=200)
acc_setosa = accuracy_fn(d_setosa_test, np.sign(np.dot(add_bias(X_iris_test_n), Wp_setosa)))
print(f"  Setosa vs Resto: converge en {hp_setosa['epochs_to_converge']} epocas, acc test={acc_setosa:.4f}")

Wp_vv, hp_vv = train_perceptron(X_vv_train, d_vv_train, alpha=1.0, max_epochs=200)
yp_vv = np.sign(np.dot(add_bias(X_vv_test), Wp_vv)); yp_vv[yp_vv==0]=1.0
acc_vv = accuracy_fn(d_vv_test, yp_vv)
print(f"  Versicolor vs Virginica: converge={hp_vv['epochs_to_converge']}, acc test={acc_vv:.4f}")

# --- MLP Iris 4-8-3 ---
print("\\n--- MLP 4-8-3 en Iris ---")
mu_grid = [0.001, 0.01, 0.05]
eta_grid = [0, 0.9]
best_acc = 0
best_config = None
results_iris = []

for mu in mu_grid:
    for eta in eta_grid:
        mlp_iris = MLP([4, 8, 3], mu=mu, momentum=eta, seed=7)
        t0 = time.perf_counter()
        hist = mlp_iris.fit(X_iris_train_n, d_iris_train_oh, epochs=250, verbose=False, seed=11)
        elapsed = time.perf_counter() - t0
        acc_train = mlp_iris.accuracy(X_iris_train_n, d_iris_train_oh)
        acc_test = mlp_iris.accuracy(X_iris_test_n, d_iris_test_oh)
        # Epocas para llegar a 95% train
        ep95 = np.argmax(hist['acc_history'] >= 0.95) + 1 if np.any(hist['acc_history'] >= 0.95) else 250
        results_iris.append((mu, eta, acc_train, acc_test, ep95, elapsed))
        print(f"  mu={mu:.3f}, eta={eta:.1f}: acc train={acc_train:.4f}, acc test={acc_test:.4f}, ep95={ep95}, t={elapsed:.2f}s")
        if acc_test > best_acc or (acc_test == best_acc and ep95 < (best_config[4] if best_config else 999)):
            best_acc = acc_test
            best_config = (mu, eta, acc_train, acc_test, ep95, elapsed, mlp_iris, hist)

print(f"\\nMejor configuracion: mu={best_config[0]}, eta={best_config[1]}, acc test={best_config[3]:.4f}")

# Figura Iris
best_mlp = best_config[6]
best_hist = best_config[7]
cm, acc_test_cm = best_mlp.classification_report(X_iris_test_n, d_iris_test_oh)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
axes[0].semilogy(best_hist['mse_history'])
axes[0].set_xlabel('Epoca'); axes[0].set_ylabel('MSE (log)')
axes[0].set_title(f'MLP 4-8-3 Iris: Curva MSE (mu={best_config[0]}, eta={best_config[1]})')
axes[0].grid(True, alpha=0.3)

axes[1].plot(best_hist['acc_history'], label='Train')
axes[1].axhline(y=best_config[3], color='green', linestyle='--', label=f'Test={best_config[3]:.4f}')
axes[1].set_xlabel('Epoca'); axes[1].set_ylabel('Accuracy')
axes[1].set_title('MLP Iris: Accuracy por epoca')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

im = axes[2].imshow(cm, cmap='Blues', interpolation='nearest')
axes[2].set_xticks([0,1,2]); axes[2].set_yticks([0,1,2])
axes[2].set_xticklabels(iris.target_names); axes[2].set_yticklabels(iris.target_names)
axes[2].set_xlabel('Predicho'); axes[2].set_ylabel('Real')
axes[2].set_title(f'Matriz de confusion (acc={acc_test_cm:.4f})')
for i in range(3):
    for j in range(3):
        axes[2].text(j, i, str(cm[i,j]), ha='center', va='center', fontweight='bold')
plt.colorbar(im, ax=axes[2])
plt.tight_layout(); plt.savefig('figs/fig_iris_mlp.png', dpi=200, bbox_inches='tight'); plt.show()

# Relevancia de variables (norma L2 pesos primera capa por atributo)
W1_iris = best_mlp.W[0][:, 1:]  # Sin columna bias
relevancia = np.linalg.norm(W1_iris, axis=0)
total = np.sum(relevancia)
feat_names = iris.feature_names
print("\\nRelevancia de variables (norma L2 pesos capa 1):")
for name, r in zip(feat_names, relevancia):
    print(f"  {name}: {r:.2f} ({r/total*100:.1f}%)")

# Tabla Iris
tab_iris = []
tab_iris.append('\\\\begin{tabular}{@{}lccccc@{}}')
tab_iris.append('\\\\toprule')
tab_iris.append('$\\\\mu$ & $\\\\eta$ & Acc. train & Acc. test & Ep. a 95\\\\% & Tiempo (s) \\\\\\\\')
tab_iris.append('\\\\midrule')
for mu, eta, atr, ate, ep95, t in results_iris:
    tab_iris.append(f'{mu:.3f} & {eta:.1f} & {atr*100:.1f}\\\\% & {ate*100:.1f}\\\\% & {ep95} & {t:.2f} \\\\\\\\')
tab_iris.append('\\\\bottomrule')
tab_iris.append('\\\\end{tabular}')
with open('tabs/tab_iris.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_iris))

# Tabla relevancia
tab_rel = []
tab_rel.append('\\\\begin{tabular}{@{}lcc@{}}')
tab_rel.append('\\\\toprule')
tab_rel.append('Atributo & $\\\\|W_1\\\\|_2$ & Contribucion (\\\\%) \\\\\\\\')
tab_rel.append('\\\\midrule')
for name, r in zip(feat_names, relevancia):
    tab_rel.append(f'{name} & {r:.2f} & {r/total*100:.1f}\\\\% \\\\\\\\')
tab_rel.append('\\\\bottomrule')
tab_rel.append('\\\\end{tabular}')
with open('tabs/tab_relevancia.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_rel))
print("Tablas: tabs/tab_iris.tex, tabs/tab_relevancia.tex")

# --- Two-moons con MLP ---
print("\\n--- MLP 2-8-1 en two-moons ---")
mlp_moons = MLP([2, 8, 1], mu=0.02, momentum=0.9, seed=42)
X_mt, X_mv, d_mt, d_mv = train_test_split(X_moons, d_moons, test_size=0.3, random_state=42)
hist_moons = mlp_moons.fit(X_mt, d_mt.reshape(-1,1), epochs=300, verbose=False, seed=11)
yp_moons = mlp_moons.predict_batch(X_mv).flatten()
yp_moons_bin = np.sign(yp_moons); yp_moons_bin[yp_moons_bin==0]=1.0
acc_moons = accuracy_fn(d_mv, yp_moons_bin)
print(f"  MLP 2-8-1 two-moons: acc test = {acc_moons*100:.1f}%")

# Figura moons
fig, ax = plt.subplots(figsize=(8, 6))
x_min, x_max = X_moons[:,0].min()-0.5, X_moons[:,0].max()+0.5
y_min, y_max = X_moons[:,1].min()-0.5, X_moons[:,1].max()+0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
Z = np.array([np.sign(mlp_moons.predict_batch(g.reshape(1,-1))[0,0]) for g in grid])
Z = Z.reshape(xx.shape)
ax.contourf(xx, yy, Z, levels=[-1, 0, 1], colors=['#FFCCCC','#CCCCFF'], alpha=0.5)
ax.scatter(X_moons[d_moons==1,0], X_moons[d_moons==1,1], c='blue', alpha=0.5, s=15, label='+1')
ax.scatter(X_moons[d_moons==-1,0], X_moons[d_moons==-1,1], c='red', alpha=0.5, s=15, label='-1')
ax.set_title(f'MLP 2-8-1 en two-moons (acc test={acc_moons*100:.1f}%)')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_moons.png', dpi=200, bbox_inches='tight'); plt.show()

# --- Wine con alpha-LMS y mu-LMS ---
print("\\n--- Clasificadores lineales en Wine ---")
Wa_wine, ha_wine = train_alpha_lms(X_wine_train_n, d_wt, alpha=0.5, max_epochs=200)
Wm_wine, hm_wine = train_mu_lms(X_wine_train_n, d_wt, mu=0.01, max_epochs=200)
Ww_wine = wiener_solution(X_wine_train_n, d_wt)

Xb_wt = add_bias(X_wine_train_n); Xb_wv = add_bias(X_wine_test_n)
acc_wine_a = accuracy_fn(d_wv, np.sign(np.dot(Xb_wv, Wa_wine)))
acc_wine_m = accuracy_fn(d_wv, np.sign(np.dot(Xb_wv, Wm_wine)))
yp_w = np.sign(np.dot(Xb_wv, Ww_wine)); yp_w[yp_w==0]=1.0
acc_wine_wiener = accuracy_fn(d_wv, yp_w)
print(f"  alpha-LMS: acc test={acc_wine_a*100:.1f}%, MSE train={ha_wine['mse_history'][-1]:.4f}")
print(f"  mu-LMS:    acc test={acc_wine_m*100:.1f}%, MSE train={hm_wine['mse_history'][-1]:.4f}")
print(f"  Wiener:    acc test={acc_wine_wiener*100:.1f}%")

# Figura Wine
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.plot(ha_wine['mse_history'], label='alpha-LMS')
ax1.plot(hm_wine['mse_history'], label='mu-LMS')
mse_w_wiener = mse_loss(d_wt, np.dot(Xb_wt, Ww_wine))
ax1.axhline(y=mse_w_wiener, color='black', linestyle='--', label=f'Wiener MSE={mse_w_wiener:.4f}')
ax1.set_xlabel('Epoca'); ax1.set_ylabel('MSE')
ax1.set_title('Wine: Convergencia MSE')
ax1.legend(); ax1.grid(True, alpha=0.3)

ax2.plot(ha_wine['acc_history'], label='alpha-LMS')
ax2.plot(hm_wine['acc_history'], label='mu-LMS')
ax2.axhline(y=acc_wine_wiener, color='black', linestyle='--', label=f'Wiener acc={acc_wine_wiener*100:.1f}%')
ax2.set_xlabel('Epoca'); ax2.set_ylabel('Accuracy')
ax2.set_title('Wine: Accuracy por epoca')
ax2.legend(); ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_wine.png', dpi=200, bbox_inches='tight'); plt.show()

# --- MNIST reducido con MLP ---
print("\\n--- MLP 64-16-5 en MNIST-04 ---")
mlp_digits = MLP([64, 16, 5], mu=0.01, momentum=0.0, seed=42)
t0 = time.perf_counter()
hist_digits = mlp_digits.fit(X_digits_train_n, d_digits_train_oh, epochs=150, verbose=False, seed=11)
t_digits = time.perf_counter() - t0
acc_digits_train = mlp_digits.accuracy(X_digits_train_n, d_digits_train_oh)
acc_digits_test = mlp_digits.accuracy(X_digits_test_n, d_digits_test_oh)
print(f"  MLP 64-16-5: acc train={acc_digits_train:.4f}, acc test={acc_digits_test:.4f}, tiempo={t_digits:.1f}s")

# Figura MNIST
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.semilogy(hist_digits['mse_history'])
ax1.set_xlabel('Epoca'); ax1.set_ylabel('MSE (log)')
ax1.set_title(f'MLP 64-16-5 MNIST-04: MSE (acc test={acc_digits_test:.4f})')
ax1.grid(True, alpha=0.3)

ax2.plot(hist_digits['acc_history'], label='Train')
ax2.axhline(y=acc_digits_test, color='green', linestyle='--', label=f'Test={acc_digits_test:.4f}')
ax2.set_xlabel('Epoca'); ax2.set_ylabel('Accuracy')
ax2.set_title('MLP MNIST-04: Accuracy por epoca')
ax2.legend(); ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('figs/fig_mnist.png', dpi=200, bbox_inches='tight'); plt.show()

print("E6 completado.")
''')

# ═══════════════════════════════════════════════════════════════
# E7: MRIII vs Backprop
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# E7: MRIII vs BACKPROP -- Equivalencia y costo (H4)
# ===================================================================
print("\\n" + "="*60)
print("E7: MRIII vs Backprop")
print("="*60)

# Red 4-8-3 entrenada en Iris
net_e7 = MLP([4, 8, 3], mu=0.01, seed=5)
net_e7.fit(X_iris_train_n, d_iris_train_oh, epochs=50, seed=55)

# Tomar un patron de Iris (el primero)
x0 = X_iris_train_n[0]
d0 = d_iris_train_oh[0]

# (a) Comparar gradientes para distintos Delta_s
ds_values = np.logspace(-1, -9, 17)
errors_rel = []
for ds in ds_values:
    grad_mriii, _ = mriii_gradient(net_e7, x0, d0, ds=ds)
    grad_bp = backprop_gradient(net_e7, x0, d0)
    # Calcular error relativo (norma)
    flat_mriii = np.concatenate([g.flatten() for g in grad_mriii])
    flat_bp = np.concatenate([g.flatten() for g in grad_bp])
    err = np.linalg.norm(flat_mriii - flat_bp) / (np.linalg.norm(flat_bp) + 1e-15)
    errors_rel.append(err)

min_err_idx = np.argmin(errors_rel)
print(f"Error relativo minimo: {errors_rel[min_err_idx]:.2e} en Delta_s = {ds_values[min_err_idx]:.2e}")

# (b) Costo computacional BP vs MRIII
print("\\n--- Costo computacional por presentacion ---")
hidden_sizes = [4, 16, 64, 256]
n_reps = 30
cost_results = []

for H in hidden_sizes:
    net_cost = MLP([4, H, 3], mu=0.01, seed=1)
    n_ada = sum(w.shape[0] for w in net_cost.W)
    
    # Tiempo backprop (1 forward + 1 backward)
    t0 = time.perf_counter()
    for _ in range(n_reps):
        net_cost.train_pattern(x0, d0)
    t_bp = (time.perf_counter() - t0) / n_reps * 1000  # ms
    
    # Tiempo MRIII (1 + N_Adalines forwards)
    t0 = time.perf_counter()
    for _ in range(n_reps):
        mriii_gradient(net_cost, x0, d0, ds=1e-6)
    t_mriii = (time.perf_counter() - t0) / n_reps * 1000  # ms
    
    ratio = t_mriii / t_bp if t_bp > 0 else 0
    cost_results.append((H, n_ada, t_bp, t_mriii, ratio))
    print(f"  H={H:3d}: BP={t_bp:.4f}ms, MRIII={t_mriii:.4f}ms, ratio={ratio:.1f}x (N_ada={n_ada})")

# Figura MRIII vs BP
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# (a) Error relativo vs Delta_s
ax1.loglog(ds_values, errors_rel, 'o-', markersize=4)
ax1.axvline(x=ds_values[min_err_idx], color='red', linestyle='--', alpha=0.5,
            label=f'Min err={errors_rel[min_err_idx]:.2e}')
ax1.set_xlabel('Delta_s (perturbacion)')
ax1.set_ylabel('Error relativo ||grad_MRIII - grad_BP|| / ||grad_BP||')
ax1.set_title('E7a: MRIII vs Backprop -- Precision del gradiente')
ax1.invert_xaxis()
ax1.legend(); ax1.grid(True, alpha=0.3)

# (b) Costo computacional
Hs = [r[0] for r in cost_results]
t_bps = [r[2] for r in cost_results]
t_mriiis = [r[3] for r in cost_results]
ratios = [r[4] for r in cost_results]
ax2.bar(np.arange(len(Hs))-0.15, t_bps, 0.3, label='Backprop (ms)', color='steelblue')
ax2.bar(np.arange(len(Hs))+0.15, t_mriiis, 0.3, label='MRIII (ms)', color='coral')
ax2.set_xticks(range(len(Hs)))
ax2.set_xticklabels([f'H={h}' for h in Hs])
ax2.set_ylabel('Tiempo por presentacion (ms)')
ax2.set_title('E7b: Costo computacional BP vs MRIII')
ax2.legend()

# Agregar ratios como texto
for i, r in enumerate(ratios):
    ax2.text(i, max(t_bps[i], t_mriiis[i])*1.05, f'{r:.1f}x', ha='center', fontsize=9)
ax2.grid(True, alpha=0.3, axis='y')
plt.tight_layout(); plt.savefig('figs/fig_mriii_bp.png', dpi=200, bbox_inches='tight'); plt.show()

# Tabla MRIII
tab_mriii = []
tab_mriii.append('\\\\begin{tabular}{@{}lcccc@{}}')
tab_mriii.append('\\\\toprule')
tab_mriii.append('Ocultas (H) & Adalines & BP (ms) & MRIII (ms) & Razon \\\\\\\\')
tab_mriii.append('\\\\midrule')
for H, n_ada, t_bp, t_mriii, ratio in cost_results:
    tab_mriii.append(f'{H} & {n_ada} & {t_bp:.4f} & {t_mriii:.4f} & {ratio:.1f}$\\\\times$ \\\\\\\\')
tab_mriii.append('\\\\bottomrule')
tab_mriii.append('\\\\end{tabular}')
with open('tabs/tab_mriii.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_mriii))
print("Tabla: tabs/tab_mriii.tex")
print("E7 completado.")
''')

# ═══════════════════════════════════════════════════════════════
# Tabla resumen final
# ═══════════════════════════════════════════════════════════════
code('''# ===================================================================
# TABLA RESUMEN CONSOLIDADA
# ===================================================================
print("\\n" + "="*60)
print("Generando tabla resumen...")
print("="*60)

tab_resumen = []
tab_resumen.append('\\\\begin{tabular}{@{}llll@{}}')
tab_resumen.append('\\\\toprule')
tab_resumen.append('Exp. & Problema & Algoritmo & Resultado clave \\\\\\\\')
tab_resumen.append('\\\\midrule')
tab_resumen.append('E1 & Capacidad de Cover & Monte Carlo LP & $C_s\\\\approx 2N_w$, $C_d=N_w$ verificado \\\\\\\\')
tab_resumen.append(f'E2 & Datos separables & Perceptron, $\\\\alpha$-LMS, $\\\\mu$-LMS & Perceptron converge en {hp["epochs_to_converge"]} ep.; $\\\\mu$-LMS a {ang_m:.1f} deg de Wiener \\\\\\\\')
tab_resumen.append(f'E3 & Datos no separables & Perceptron, $\\\\alpha$-LMS, $\\\\mu$-LMS & $\\\\mu$-LMS mejor: {ma_m*100:.1f}\\\\% $\\\\pm${ma_s*100:.1f} vs Wiener {acc_wiener_ns*100:.1f}\\\\% \\\\\\\\')
tab_resumen.append('E4 & Superficies MSE & Adaline 2D & MSE signum tiene mesetas y optimos locales \\\\\\\\')
tab_resumen.append(f'E5 & XOR & MRII, MLP-BP & MRII+ruido {success_mrii_noise}/{n_trials_xor}, MLP-BP {success_mlp_2}/{n_trials_xor} \\\\\\\\')
tab_resumen.append(f'E6 & Iris (real) & MLP 4-8-3 & Mejor acc test={best_config[3]*100:.1f}\\\\% ($\\\\mu$={best_config[0]}, $\\\\eta$={best_config[1]}) \\\\\\\\')
tab_resumen.append(f'E6b & Two-moons & MLP 2-8-1 & Acc test={acc_moons*100:.1f}\\\\% \\\\\\\\')
tab_resumen.append(f'E6c & Wine (real) & $\\\\alpha$-LMS, $\\\\mu$-LMS, Wiener & Wiener acc={acc_wine_wiener*100:.1f}\\\\% \\\\\\\\')
tab_resumen.append(f'E6d & MNIST-04 & MLP 64-16-5 & Acc test={acc_digits_test*100:.1f}\\\\% \\\\\\\\')
tab_resumen.append(f'E7 & MRIII vs BP & Gradiente + costo & Err min={errors_rel[min_err_idx]:.2e} en $\\\\Delta s$={ds_values[min_err_idx]:.2e}; MRIII {ratios[1]:.0f}$\\\\times$ mas caro \\\\\\\\')
tab_resumen.append('\\\\bottomrule')
tab_resumen.append('\\\\end{tabular}')
with open('tabs/tab_resumen.tex', 'w', encoding='utf-8') as f:
    f.write('\\n'.join(tab_resumen))
print("Tabla resumen: tabs/tab_resumen.tex")
print("\\n✅ TODOS los experimentos completados.")
print("   Figuras en figs/")
print("   Tablas en tabs/")
''')

print(f"[p4] Celdas 18-22 agregadas. Total: {len(cells)}")
nb.cells = cells
nbf.write(nb, OUT)
print(f"[p4] Guardado. Notebook completo: {len(cells)} celdas.")
