"""
Regenera tablas problematicas con formato que respeta margenes.
"""
import os

tabs_dir = r'C:\Developer\data-inteligencia\proyectos\RNA\notebook\v1\tabs'

# ── tab_resumen.tex: columna "Resultado clave" con p{...} ──
tab_resumen = r"""\begin{tabular}{@{}lllp{5.5cm}@{}}
\toprule
Exp. & Problema & Algoritmo & Resultado clave \\
\midrule
E1 & Capacidad de Cover & Monte Carlo LP & $C_s\approx 2N_w$, $C_d=N_w$ verificado \\
E2 & Datos separables & Perceptron, $\alpha$-LMS, $\mu$-LMS & Perceptron converge en 2 ep.; $\mu$-LMS a 3.5$^\circ$ de Wiener \\
E3 & Datos no separables & Perceptron, $\alpha$-LMS, $\mu$-LMS & $\mu$-LMS mejor: 79.6\% $\pm$1.5 vs Wiener 81.0\% \\
E4 & Superficies MSE & Adaline 2D & MSE signum tiene mesetas y optimos locales \\
E5 & XOR & MRII, MLP-BP & MRII 0/20; MLP-BP 6/20 (2-2-1), 11/20 (2-3-1) \\
E6 & Iris (real) & MLP 4-8-3 & Mejor acc test=91.1\% ($\mu$=0.05, $\eta$=0) \\
E6b & Two-moons & MLP 2-8-1 & Acc test=93.3\% \\
E6c & Wine (real) & $\alpha$-LMS, $\mu$-LMS, Wiener & Wiener acc=98.1\% \\
E6d & MNIST-04 & MLP 64-16-5 & Acc test=98.5\% \\
E7 & MRIII vs BP & Gradiente + costo & Err min=$5.05{\times}10^{-8}$ en $\Delta s{=}10^{-8}$; MRIII 11$\times$ mas caro \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_resumen.tex'), 'w') as f:
    f.write(tab_resumen)

# ── tab_iris.tex: headers abreviados ──
tab_iris = r"""\begin{tabular}{@{}cccccc@{}}
\toprule
$\mu$ & $\eta$ & Acc. train & Acc. test & Ep. 95\% & T (s) \\
\midrule
0.001 & 0.0 & 98.1\% & 91.1\% & 62 & 0.99 \\
0.001 & 0.9 & 98.1\% & 91.1\% & 62 & 1.04 \\
0.010 & 0.0 & 100\% & 91.1\% & 7 & 0.98 \\
0.010 & 0.9 & 100\% & 91.1\% & 7 & 1.08 \\
0.050 & 0.0 & 100\% & 91.1\% & 4 & 1.03 \\
0.050 & 0.9 & 100\% & 91.1\% & 4 & 1.08 \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_iris.tex'), 'w') as f:
    f.write(tab_iris)

# ── tab_lineales.tex ──
tab_lineales = r"""\begin{tabular}{@{}lccc@{}}
\toprule
Algoritmo & Acc. separable & Ep. converg. & Acc. no separable \\
\midrule
Perceptron & 100.0\% & 2 & 75.7\% $\pm$5.5 \\
$\alpha$-LMS & 100.0\% & -- & 75.0\% $\pm$7.4 \\
$\mu$-LMS & 100.0\% & -- & 79.6\% $\pm$1.5 \\
\midrule
Wiener (optimo) & 100.0\% & -- & 81.0\% \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_lineales.tex'), 'w') as f:
    f.write(tab_lineales)

# ── tab_xor.tex ──
tab_xor = r"""\begin{tabular}{@{}lcc@{}}
\toprule
Configuracion & Tasa exito & Mediana epocas \\
\midrule
MRII 2-2-1 sin ruido & 0/20 & -- \\
MRII 2-2-1 + ruido & 0/20 & -- \\
MRII 2-3-1 + ruido & 0/20 & -- \\
MLP-BP 2-2-1 & 6/20 & 40 \\
MLP-BP 2-3-1 & 11/20 & 22 \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_xor.tex'), 'w') as f:
    f.write(tab_xor)

# ── tab_mriii.tex ──
tab_mriii = r"""\begin{tabular}{@{}lcccc@{}}
\toprule
Ocultas (H) & Adalines & BP (ms) & MRIII (ms) & Razon \\
\midrule
4 & 7 & 0.0201 & 0.0701 & 3.5$\times$ \\
16 & 19 & 0.0194 & 0.2148 & 11.0$\times$ \\
64 & 67 & 0.0312 & 0.5881 & 18.9$\times$ \\
256 & 259 & 0.0341 & 2.5297 & 74.1$\times$ \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_mriii.tex'), 'w') as f:
    f.write(tab_mriii)

# ── tab_relevancia.tex ──
tab_relevancia = r"""\begin{tabular}{@{}lcc@{}}
\toprule
Atributo & $\|W_1\|_2$ & Contribucion (\%) \\
\midrule
sepal length (cm) & 1.50 & 6.4\% \\
sepal width (cm) & 4.54 & 19.2\% \\
petal length (cm) & 6.23 & 26.4\% \\
petal width (cm) & 11.32 & 48.0\% \\
\bottomrule
\end{tabular}
"""
with open(os.path.join(tabs_dir, 'tab_relevancia.tex'), 'w') as f:
    f.write(tab_relevancia)

print("Tablas regeneradas con formato ajustado a margenes.")
for fname in sorted(os.listdir(tabs_dir)):
    print(f"  {fname}")
