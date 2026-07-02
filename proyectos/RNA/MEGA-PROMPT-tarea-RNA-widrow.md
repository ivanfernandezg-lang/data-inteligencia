# MEGA PROMPT — Informe LaTeX + Notebook: Tarea RNA sobre Widrow & Lehr (1990)

Copia todo el contenido de este archivo y pégalo como prompt en la otra IA.

---

## ROL Y OBJETIVO

Actúa como un ingeniero informático senior con experiencia en machine learning, redes neuronales clásicas y LaTeX académico. Debes producir **DOS entregables completos y funcionales**:

1. **`informe-widrow.tex`** — Informe académico en español, LaTeX compilable con `pdflatex`, de ~10 páginas, que analiza el paper de Widrow & Lehr (1990).
2. **`implementacion-widrow-lehr.ipynb`** — Notebook Jupyter (Python, NumPy puro para los algoritmos) que implementa desde cero los algoritmos del paper, ejecuta 7 experimentos reproducibles y **genera automáticamente** las figuras (`figs/*.png`) y tablas LaTeX (`tabs/*.tex`) que el informe carga.

El flujo de trabajo del usuario es: ejecutar el notebook → copiar `figs/` y `tabs/` junto al `.tex` → compilar. **El informe debe compilar incluso si faltan las figuras/tablas** (usar recuadros de marcador de posición vía `\IfFileExists`).

---

## 1. CONTEXTO DE LA TAREA (enunciado oficial)

- **Curso:** Inteligencia Computacional — módulo Redes Neuronales Artificiales, Magíster en Ingeniería Informática, Universidad de Santiago de Chile (USACH), Primer Semestre 2026.
- **Profesor:** Gonzalo Acuña Leiva. **Entrega:** 06/07/2026. Grupos de hasta 2 personas.
- **Entregables del curso:** informe de 10 páginas + video de 10–15 min (el video NO lo generas tú; solo informe y notebook).
- **Objetivo general:** identificar y comprender los conceptos fundamentales de RNA aplicados al fenómeno/problema del artículo seleccionado.
- **Objetivos específicos:** describir el problema; analizar el marco teórico identificando tipo, arquitectura, modo (aprendizaje/reconocimiento), funciones de agrupamiento y activación; describir la experimentación (conjunto de datos y origen); evaluar resultados con métricas de eficiencia según el tipo de problema (regresión/clasificación/clustering); elaborar conclusión propia.

### Rúbrica del informe (respétala como estructura de secciones):

| Sección | Peso | Contenido exigido |
|---|---|---|
| Presentación, ortografía y redacción | 10% | Formato profesional, español impecable |
| Introducción | 15% | Descripción del ámbito/problema, ¿por qué usar RNA para este tipo de problemas?, hipótesis si las hay |
| Marco Teórico | 15% | Métodos, técnicas y características principales de las RNA del artículo, algoritmos implementados y sus ventajas |
| Experimentación | 15% | Características del conjunto de datos, algoritmos, librerías, desempeño en costo de complejidad computacional |
| Análisis de resultados | 30% | Interpretación, eficiencia, criterios de selección del modelo final (variables que aportan mayor información al modelo, métricas de desempeño) |
| Conclusiones | 20% | Aporte al conocimiento del problema mediante la RNA utilizada; **evaluación de la hipótesis** |
| Referencias | 10% | Citas en el texto + bibliografía tras las conclusiones |

---

## 2. EL PAPER (contenido que debes dominar y reflejar)

**Widrow, B. & Lehr, M. A. (1990). "30 Years of Adaptive Neural Networks: Perceptron, Madaline, and Backpropagation". Proceedings of the IEEE, 78(9), 1415–1442.**

Es un **artículo de revisión/tutorial** (no experimental sobre un dataset único). Tema central: la historia, teoría y características operativas de los algoritmos de entrenamiento supervisado para redes **feedforward**, unificados por el **principio de mínima perturbación** (*minimal disturbance principle*): "adaptar para reducir el error de salida ante el patrón actual, con mínima perturbación a las respuestas ya aprendidas".

### Contenido por secciones del paper:

- **Secc. I (Introducción):** 30° aniversario de la regla del Perceptrón (Rosenblatt, 1960) y del LMS (Widrow & Hoff, 1960). Historia: Madaline I (1962), backpropagation descubierto por Werbos (1974), redescubierto por Parker (1982) y popularizado por Rumelhart, Hinton & Williams (1985-86). MRII (Widrow & Winter, 1987) para cuantizadores duros multicapa; MRIII (David Andes, 1988) reemplaza signum por sigmoides — Widrow y estudiantes demostraron que MRIII ≡ backpropagation.
- **Secc. II (Conceptos fundamentales):** motivación (problemas mal definidos e intensivos en cómputo que el cerebro resuelve con paralelismo masivo); el **combinador lineal adaptativo** (s_k = X_k^T W_k, entrada con bias x0=+1); el **Adaline** = combinador lineal + cuantizador signum; **separabilidad lineal** (un Adaline de 2 entradas realiza 14 de 16 funciones lógicas; XOR/XNOR no son separables, Eq. 5); **capacidad de Cover (1964)**: probabilidad de separabilidad P(Np,Nw) = 1 si Np≤Nw, si no 2^(1−Np)·Σ_{i=0}^{Nw−1} C(Np−1, i) → capacidad determinística C_d = N_w, estadística C_s ≈ 2N_w (Fig. 5 del paper); clasificadores no lineales: discriminantes polinomiales (Specht) y redes multicapa; cotas de Baum para redes de 2 capas: N_w/N_y − K1 ≤ C_d ≤ (N_w/N_y)·log2(N_w/N_y) + K2; **trade-off capacidad–generalización** (N_p ≫ N_w/N_y; la limitación del Adaline es "una fortaleza, no el defecto fatal imaginado por algunos críticos" — alusión a Minsky & Papert); aplicación NETtalk (Sejnowski & Rosenberg, red 80-26 que aprende a pronunciar texto).
- **Secc. III:** el principio de mínima perturbación como idea motivadora que llevó al descubrimiento del LMS.
- **Secc. IV (Reglas de corrección de error, un elemento):**
  - **α-LMS / regla delta Widrow-Hoff (Eq. 10):** W_{k+1} = W_k + α·(ε_k/||X_k||²)·X_k, con error LINEAL ε_k = d_k − s_k. Cambio de pesos colineal con X_k (mínima perturbación geométrica). El error se reduce en factor α por presentación. Estable para 0<α<2, rango práctico 0.1<α<1. Autonormalizante.
  - **Regla del Perceptrón (Rosenblatt, Eq. 18):** W_{k+1} = W_k + α·(ε̃_k/2)·X_k con error del CUANTIZADOR ε̃_k = d_k − y_k ∈ {−2,0,+2}. Solo adapta si la decisión es incorrecta. Teorema de convergencia: separa en pasos finitos si el problema es separable; si NO es separable "continúa para siempre", el vector de pesos gravita hacia cero y cada adaptación puede cambiar drásticamente la función.
  - **Reglas de Mays:** incremento con zona muerta ±γ y relajación modificada; mitigan el colapso en problemas no separables.
- **Secc. V (Corrección de error, multielemento):**
  - **Madaline I (MRI):** primera capa de Adalines signum adaptativas + lógica fija (AND/OR/mayoría). Load-sharing: adapta la(s) Adaline(s) con |s| más cercano a cero ("asignar responsabilidad a quien puede asumirla más fácilmente"). Presentación aleatoria de patrones (Ridgway: la cíclica genera ciclos de adaptación).
  - **Madaline II (MRII):** todas las capas adaptativas. Ante patrón erróneo: inversión tentativa (vía perturbación Δs) de la salida de las Adalines ocultas en orden de |s| creciente; aceptar la adaptación (α-LMS colineal con la entrada) SOLO si reduce el error de Hamming; extensible a pares, tríos, etc. Puede estancarse en óptimos locales.
- **Secc. VI (Descenso más pronunciado, un elemento):**
  - Superficie de MSE del combinador lineal: ξ(W) = E[d²] − 2P^T W + W^T R W, hiperparaboloide CONVEXO, mínimo único = solución de Wiener W* = R^{-1}P, con R = E[X X^T], P = E[d·X] (Eq. 29).
  - **μ-LMS (Eq. 33):** W_{k+1} = W_k + 2μ·ε_k·X_k (gradiente instantáneo insesgado −2ε_k X_k). Estabilidad: 0 < μ < 1/tr[R] (Eq. 34). α-LMS ≡ μ-LMS sobre un conjunto de entrenamiento normalizado → con patrones no binarios α-LMS converge a solución levemente sesgada.
  - **Adaline sigmoide + backprop (Eqs. 54–56):** W_{k+1} = W_k + 2μ·ε̃_k·sgm'(s_k)·X_k; con tanh: sgm'(s)=1−y².
  - **MRIII un elemento (Eqs. 60–61):** gradiente por perturbación Δs del sumador, sin usar la derivada analítica; robusto para hardware analógico; equivalente a backprop cuando Δs→0.
  - **Superficies de MSE (Figs. 22–24):** error lineal = paraboloide convexo; error sigmoide = no cuadrático pero navegable; error signum = escalonado con mesetas y óptimos locales (inadecuado para gradiente).
- **Secc. VII (Descenso más pronunciado, redes):**
  - **Backpropagation (Eqs. 71–99):** el problema central es obtener "señales de error" para Adalines ocultas. Deltas: δ^(L)_j = ε_j·sgm'(s_j) en salida (Eq. 78; con tanh Eq. 79: δ = ε(1−y²)); ocultas por regla de la cadena δ^(l) = (W^(l+1)T δ^(l+1)) ⊙ sgm'(s^(l)) (Eq. 87). Actualización ΔW = 2μ·δ·X^T (Eq. 94). δ NO es un error: el objetivo es reducir ε² de salida. **Momentum (Eqs. 96–97):** ΔW_k = η·ΔW_{k−1} + (1−η)·2μ·δ_k X_k, filtro pasabajos de actualizaciones, η≈0.8–0.9. Pasada hacia atrás de complejidad comparable a la de adelante. Inicialización: pesos pequeños aleatorios (cero o mal elegidos → falla). Menciona quickprop, delta-bar-delta, backprop through time (truck backer-upper de Nguyen & Widrow: red de 26 Adalines aprende a retroceder un camión con acoplado).
  - **MRIII para redes (Eqs. 100–103):** perturbar cada Adaline, medir Δ(ε²)/Δs sobre la salida de TODA la red; ∇̂ = (Δε²/Δs)·X. Equivalente a backprop si Δs pequeño; requiere 1+N_Adalines pasadas hacia adelante por presentación vs. 1 adelante + 1 atrás de backprop → backprop domina en digital, MRIII se justifica en hardware analógico (hubo un chip comercial).
  - **Superficies MSE de redes (Figs. 29–32):** backprop, MRIII y MRII sujetos a óptimos locales. **Remedios que da el paper: adición esporádica de ruido a los pesos, o reentrenar con distintas inicializaciones aleatorias.**
- **Secc. VIII (Resumen):** taxonomía (Fig. 33): corrección de error {lineal: α-LMS; no lineal: Perceptron, Mays, MRI, MRII} vs. descenso más pronunciado {lineal: μ-LMS; no lineal: backprop, MRIII}, en un elemento vs. red.

---

## 3. ESPECIFICACIÓN DEL NOTEBOOK

**Requisitos técnicos:** Python 3, algoritmos **desde cero con NumPy** (scikit-learn SOLO para cargar Iris, `make_moons`, `train_test_split`, `StandardScaler`, `confusion_matrix`; scipy para `linprog` y `comb`). **Semilla global SEED=1990** y semillas fijas en cada experimento (reproducibilidad exacta). Crear carpetas `figs/` y `tabs/` y guardar salidas con NOMBRES FIJOS (el informe los referencia). Cada figura con `plt.savefig` a 200 dpi. Celda inicial markdown con tabla de mapeo experimento→sección del informe.

### Implementaciones (una celda de reglas de un elemento, otra de redes):
- `add_bias(X)`: antepone columna de 1s. Convención d ∈ {−1,+1}.
- `train_alpha_lms(X, d, alpha, epochs, seed)`: Eq. 10, presentación aleatoria por época, historial de MSE/accuracy/||W||.
- `train_mu_lms(...)`: Eq. 33, mismo historial + trayectoria de pesos.
- `train_perceptron(...)`: Eq. 18, registra época de convergencia (0 errores) y se detiene.
- `wiener_solution(X, d)`: W* = R^{-1}P muestral.
- **Clase `MLP`**: capas totalmente conectadas de Adalines tanh, pesos W[l] de forma (n_out, n_in+1) con columna 0 = bias, init uniforme ±0.5. Métodos: `forward(x, perturb=None)` (perturb=(capa,j,Δs) suma Δs al sumador — para MRIII), `backprop_deltas` (Eqs. 78/79 y 87), `train_pattern` (Eq. 94 con momentum Eqs. 96–97: V = η·V + (1−η)·2μ·δ·x^T), `fit` estocástico patrón a patrón con permutación aleatoria, `predict_batch`, `accuracy` (argmax si one-hot ±1; signo si escalar).
- **Clase `MadalineII`** (¡CRÍTICO, ver sección 5 de este prompt!): red de Adalines signum, todas las capas adaptativas. `forward(x, flip=(capa, índices))` permite invertir la salida binaria de Adalines seleccionadas (equivale a la perturbación Δs del paper). Entrenamiento por patrón erróneo: probar inversiones tentativas de las ocultas en orden |s| creciente, **primero de a una y luego DE A PARES** (`itertools.combinations`); aceptar solo si reduce el error de Hamming del patrón; al aceptar, reforzar con corrección absoluta colineal: w += ((target·margin − s)/||xb||²)·xb con margin=1.0, target = −sign(s). Capa de salida: α-LMS con α=0.5 hacia d. **Escape de óptimos locales (remedio del propio paper, Secc. VII-E): si el error de Hamming global se estanca `patience=15` épocas, añadir ruido gaussiano σ=0.15 a todos los pesos al final de cada época estancada.** `fit(max_epochs=150)`.
- `mriii_deltas(net, x, d, ds)`: estima ∂ε²/∂s_j para TODA Adaline perturbando su sumador (Eq. 102): (ε²_perturbado − ε²_base)/Δs.

### Los 7 experimentos (con los resultados reales que DEBES citar en el informe):

**E1 — Capacidad de Cover (H1)** → `figs/fig_cover.png`
Para Nw ∈ {2, 5, 15} y razones Np/Nw ∈ [0.5, 4] (paso 0.25), generar 80 ensayos de Np patrones X~N(0, I_Nw) con respuestas ±1 aleatorias; testear separabilidad lineal por factibilidad LP (linprog: d_i·(x_i·w) ≥ 1, hiperplano homogéneo, method='highs'). Graficar probabilidad empírica (puntos) vs. fórmula teórica de Cover (curvas), con líneas verticales en Np/Nw=1 (C_d) y =2 (C_s). **Resultado real: desviación media |empírica − teórica| = 0.025.**

**E2 — Reglas lineales en datos separables (H2)** → `figs/fig_datasets.png`, `figs/fig_fronteras.png`, `figs/fig_convergencia.png`
Datasets sintéticos (rng con SEED): separable = 2 gaussianas N([±2,±2], 0.35I), 100 pts c/u; no separable = N([±0.9,±0.9], 1.3I); XOR = 4 patrones ±1 con d=(−1,1,1,−1); two-moons (n=300, noise=0.20, random_state=SEED). Entrenar Perceptron (α=1), α-LMS (α=0.5), μ-LMS (μ=0.02) en el separable; graficar las 3 fronteras + la de Wiener (línea negra discontinua). **Resultados reales: Perceptron converge en 2 épocas (100%); ángulos respecto de W*: Perceptron 17.1°, α-LMS 14.9°, μ-LMS 5.3°; tr[R]=9.30 → μ_max teórico = 1/tr[R] = 0.1075.** Segunda subfigura: MSE (log) por época para μ ∈ {0.001, 0.01, 0.05, 0.12} — μ=0.12 > μ_max DIVERGE (envolver en np.errstate(over/invalid='ignore') y clipear MSE a 1e9 para graficar); línea horizontal en ξ_min de Wiener (**= 0.042**). Figura aparte: α-LMS con α ∈ {0.1, 0.5, 1.0, 1.9} converge en todo el rango estable.

**E3 — Datos no separables (H2)** → `figs/fig_noseparable.png`, `tabs/tab_lineales.tex`
120 épocas de los 3 algoritmos en el dataset no separable. Panel 1: accuracy por época (Perceptron oscila; LMS estable; línea de Wiener). Panel 2: ||W|| por época (oscilación del Perceptron). **Resultados reales (media±std últimas 40 épocas): Perceptron 79.7%±7.3 (oscila), α-LMS 77.4%±6.5, μ-LMS 83.9%±1.0 (estable, el mejor).** Tabla `tab_lineales.tex` (tabular con booktabs): algoritmo, acc separable, épocas de convergencia, acc no separable, fila del óptimo de Wiener.

**E4 — Superficies de MSE (Figs. 22–24 del paper)** → `figs/fig_superficies_mse.png`
Adaline de 2 pesos sin bias, 6 patrones aleatorios 2D (rng seed 7) con d ∈ {±1}. Grilla w1,w2 ∈ [−3,3]. Tres superficies 3D (plot_surface, cmap viridis): E[(d−s)²] (paraboloide convexo), E[(d−tanh(s))²] (no cuadrática), E[(d−sign(s))²] (escalonada con mesetas). **Mínimos reales: lineal 0.785, sigmoide 0.764, signum 0.667.**

**E5 — XOR: MRII vs MLP-backprop (H3)** → `figs/fig_xor.png`, `tabs/tab_xor.tex`
Sobre 20 inicializaciones (seeds 0–19), medir tasa de éxito y mediana de épocas. **Resultados reales: MRII 2-2-1 sin ruido 1/20 (¡se estanca en óptimos locales, tal como advierte el paper!); MRII 2-2-1 + ruido esporádico 12/20 (mediana 84 ép.); MRII 2-3-1 + ruido 19/20 (87 ép.); MLP-BP 2-2-1 (μ=0.1, 400 ép.) 8/20 (mediana 40); MLP-BP 2-3-1 12/20 (22).** Figura de 3 paneles: regiones de decisión de una MRII 2-3-1 exitosa (contourf), regiones del MLP 2-2-1 (banda diagonal), curva MSE del MLP. Tabla con las 5 configuraciones.

**E6 — MLP en Iris (dataset real)** → `figs/fig_iris_mlp.png`, `tabs/tab_iris.tex`, `tabs/tab_relevancia.tex`
Iris (Fisher 1936, UCI; 150×4, 3 clases). Primero, Perceptron: **setosa-vs-resto converge en 2 épocas (separable, verifica el teorema); versicolor-vs-virginica NO converge en 200 épocas, acc final 95.0% (no separable).** Luego MLP 4-8-3 tanh, targets one-hot en {−1,+1}, split 70/30 estratificado (random_state=42), StandardScaler ajustado en train, 250 épocas, grilla μ ∈ {0.001, 0.01, 0.05} × η ∈ {0, 0.9} (semillas: red seed=7, fit seed=11). **Resultados reales: TODAS las configuraciones alcanzan 91.1% en test y 100% en train; épocas para llegar a 95% train: 52/5/3 (η=0) y 52/6/3 (η=0.9); ~1.8 s cada una. Mejor configuración por criterio (acc test, luego rapidez): μ=0.05, η=0.** Figura de 3 paneles: curvas MSE (log), accuracy test por época, matriz de confusión del mejor (los errores se concentran en versicolor↔virginica). **Relevancia de variables** (norma L2 de los pesos de primera capa por atributo, entradas estandarizadas): petal width 7.46 (43.1%), petal length 4.49 (25.9%), sepal width 3.21 (18.6%), sepal length 2.15 (12.4%) → tabla `tab_relevancia.tex`. Extra: MLP 2-8-1 (μ=0.02, η=0.9, 300 ép.) en two-moons → **93.3% test**.

**E7 — MRIII ≡ backprop y costo computacional (H4)** → `figs/fig_mriii_bp.png`, `tabs/tab_mriii.tex`
(a) Red 4-8-3 (seed 5), un patrón de Iris: comparar el gradiente analítico ∂ε²/∂s_j = −2δ_j (backprop) contra el estimado por perturbación (MRIII) para Δs ∈ logspace(−1, −9, 17). Gráfico log-log del error relativo (norma) vs Δs, eje x invertido: decrece linealmente con Δs y rebota por precisión de punto flotante. **Resultado real: error relativo mínimo 1.38×10⁻⁸ en Δs = 3×10⁻⁸.** (b) Costo por presentación (ms) de BP (1 forward + 1 backward) vs MRIII (1 + N_Adalines forwards) para redes 4-H-3 con H ∈ {4, 16, 64, 256} (time.perf_counter, 30 repeticiones). **Resultado real: MRIII ≈ 17× más caro con 16 ocultas, y la brecha crece con el tamaño.** Tabla `tab_mriii.tex`: ocultas, #Adalines, ms BP, ms MRIII, razón.

**Tabla resumen final** → `tabs/tab_resumen.tex`: consolidar todos los resultados anteriores (Exp., problema, algoritmo, resultado) para la sección de Análisis.

---

## 4. ESPECIFICACIÓN DEL INFORME LaTeX

- `\documentclass[11pt,a4paper]{article}`; paquetes: inputenc utf8, fontenc T1, `[spanish,es-noshorthands]{babel}`, amsmath, amssymb, graphicx, geometry margin=2.3cm, float, booktabs, enumitem, caption, hyperref con colorlinks.
- **Macros obligatorias** (compilación robusta):
```latex
\newcommand{\figura}[4][0.92]{\begin{figure}[H]\centering
\IfFileExists{figs/#2.png}{\includegraphics[width=#1\textwidth]{figs/#2.png}}%
{\fbox{\parbox[c][2.6cm][c]{0.8\textwidth}{\centering\texttt{figs/#2.png}\\(pendiente: ejecutar el notebook)}}}
\caption{#3}\label{fig:#4}\end{figure}}

\newcommand{\tabla}[3]{\begin{table}[H]\centering\small
\IfFileExists{tabs/#1.tex}{\input{tabs/#1.tex}}%
{\fbox{\parbox[c][1.6cm][c]{0.7\textwidth}{\centering\texttt{tabs/#1.tex}\\(pendiente)}}}
\caption{#2}\label{tab:#3}\end{table}}
```
- **Estructura y contenido (seguir la rúbrica):**
  1. **Título + abstract** (resumen con los números clave: 91.1% Iris, error de gradiente 1.4×10⁻⁸, C_s≈2N_w verificada).
  2. **Introducción (15%):** ámbito y problema (aprendizaje supervisado en redes feedforward, 30 años de algoritmos unificados por mínima perturbación); ¿por qué RNA? (3 argumentos del paper: problemas mal definidos + paralelismo, aprendizaje/generalización con el trade-off capacidad-generalización, aplicabilidad demostrada: NETtalk, truck backer-upper, ecualización adaptativa como primera aplicación comercial masiva); **hipótesis H1–H4** en formato `description`: H1 capacidad de Cover (C_s≈2N_w, C_d=N_w), H2 convergencia finita del Perceptron en separables e inestabilidad en no separables vs estabilidad de LMS cerca de Wiener, H3 XOR irresoluble por un elemento pero resoluble por MRII y MLP (ambos con óptimos locales), H4 MRIII ≡ backprop cuando Δs→0 pero con mayor costo digital.
  3. **Marco teórico (15%):** tipo/arquitectura/modo (feedforward, supervisado, en línea; modos aprendizaje/reconocimiento); Adaline con función de agrupamiento (suma ponderada con bias) y funciones de activación (identidad, signum, sigmoide tanh); separabilidad lineal y capacidad (Eq. de Cover, cotas de Baum, regla de generalización N_p≫N_w/N_y); taxonomía de la Fig. 33; párrafos con las ecuaciones de α-LMS, Perceptron+Mays, μ-LMS (superficie de MSE, Wiener, estabilidad 1/tr[R]), Adaline sigmoide, backprop multicapa (deltas Eqs. 78/87, actualización Eq. 94, momentum 96–97, aclarar que δ no es un error), MRI/MRII (load sharing, inversión tentativa, mínima perturbación), MRIII (Eq. 102, motivación hardware analógico); cierre con las ventajas de la familia (O(N_w) por presentación, garantías en el caso lineal, representaciones internas + aproximación universal en el multicapa).
  4. **Experimentación (15%):** aclarar que el paper es una revisión → la experimentación propia consiste en implementar desde cero y verificar H1–H4 + un dataset real; describir los datasets y su origen (sintéticos generados con semillas, XOR de 4 patrones, Iris de Fisher/UCI vía scikit-learn, two-moons); librerías (NumPy para los algoritmos; scipy/sklearn solo utilitario); tabla o lista del diseño E1–E7; **complejidad computacional**: por presentación, backprop cuesta O(N_w) (forward+backward comparables, sin multiplicaciones de peso en la retro de primera capa), MRIII cuesta (1+N_Adalines) forwards ≈ O(N_w·N_ada), Perceptron/LMS O(N_w); mencionar reproducibilidad (semillas fijas → los números del informe se reproducen exactamente).
  5. **Análisis de resultados (30%)** — la sección más larga (~3 páginas), una subsección por experimento, cada una con su `\figura`/`\tabla` y la interpretación usando los NÚMEROS REALES de la sección 3 de este prompt. Puntos de análisis obligatorios: (E1) el ajuste empírico-teórico valida H1 y la transición se agudiza con N_w; (E2) el Perceptron converge finito pero su frontera queda "donde primero separa" (17.1° de Wiener) mientras μ-LMS optimiza MSE (5.3°); la divergencia con μ=0.12>1/tr[R] confirma la cota de estabilidad; (E3) H2 confirmada: el Perceptron oscila ±7.3 pts y LMS es estable (μ-LMS 83.9%±1.0, a ~0.5 pts del óptimo de Wiener); (E4) la geometría explica POR QUÉ el descenso de gradiente exige sigmoides: el error signum tiene gradiente nulo casi en todas partes; (E5) H3 confirmada, con el hallazgo de que MRII sin ruido se estanca 19/20 veces y el remedio del propio paper (ruido esporádico) lo rescata a 12/20 y 19/20 con 3 ocultas — también backprop 2-2-1 cae en mínimos locales 12/20 veces, coherente con la Secc. VII-E; **criterios de selección del modelo final** (E6): exactitud en test como criterio primario y velocidad de convergencia como secundario → μ=0.05, η=0 (μ grande domina; el momentum no aporta en un problema pequeño y bien condicionado, coherente con el paper: "el momentum por sí solo suele ser de poco valor"); la matriz de confusión concentra los errores en versicolor↔virginica (las clases no separables); **variables que aportan mayor información**: pétalos ≈ 69% del peso total de primera capa (43.1% + 25.9%), consistente con la estructura conocida de Iris; (E7) H4 confirmada numéricamente (error 1.4×10⁻⁸, comportamiento O(Δs) + rebote por precisión finita) y la brecha de costo ~17× justifica que backprop domine en digital y MRIII en analógico. Cerrar con la tabla resumen (`tab_resumen`).
  6. **Conclusiones (20%):** aporte al conocimiento (el paper unifica 30 años bajo mínima perturbación; valor pedagógico e histórico; el linaje Perceptron→Adaline→Madaline→backprop anticipa el deep learning moderno: SGD = μ-LMS generalizado, momentum sigue en uso, la perturbación de MRIII anticipa métodos de orden cero); **evaluación explícita de H1–H4** (las cuatro se confirman, con el matiz de que H3 requirió el remedio del ruido); limitaciones (datasets pequeños, sin comparación con métodos modernos, MRII sensible a hiperparámetros del escape); conclusión personal.
  7. **Referencias:** con `thebibliography` (o BibTeX si prefieres): Widrow & Lehr 1990; Rosenblatt 1958 (Psychological Review) y 1962 (Principles of Neurodynamics); Widrow & Hoff 1960 (IRE WESCON); Cover 1964 (tesis Stanford); Werbos 1974 (tesis Harvard); Rumelhart, Hinton & Williams 1986 (PDP/Nature); Minsky & Papert 1969 (Perceptrons); Cybenko 1989 (aproximación universal); Widrow, Winter & Baxter 1987/88 (MRII); Sejnowski & Rosenberg 1987 (NETtalk); Nguyen & Widrow 1989 (truck backer-upper); Fisher 1936 (Iris).

---

## 5. LECCIONES TÉCNICAS CRÍTICAS (errores ya descubiertos y resueltos — NO los repitas)

1. **MRII ingenua FALLA en XOR (0/20).** Con solo inversiones individuales y corrección absoluta agresiva, una única Adaline oculta monopoliza las correcciones (se rompe el load-sharing) y la red intenta meter todo XOR en un elemento → ciclo eterno con Hamming=2. La solución que funciona: (a) inversiones tentativas de a 1 Y de a pares, (b) refuerzo con corrección absoluta solo tras aceptar la inversión, (c) α-LMS moderado (α=0.5) en la capa de salida, y sobre todo (d) **ruido gaussiano esporádico (σ=0.15) en los pesos cuando el Hamming global se estanca 15 épocas** — que es literalmente el remedio propuesto en la Secc. VII-E del paper. Presenta el estancamiento sin ruido como RESULTADO (confirma la advertencia del paper), no como bug.
2. **μ-LMS con μ > 1/tr[R] genera overflow** → envolver en `np.errstate(over='ignore', invalid='ignore')` y clipear el MSE antes de graficar; es la demostración intencional de la cota de estabilidad.
3. **El informe debe compilar sin las figuras** → macros con `\IfFileExists` (arriba).
4. Presentación de patrones **aleatoria por época** en todos los algoritmos (la cíclica genera ciclos, Ridgway).
5. Inicialización del MLP: uniforme ±0.5; con pesos cero backprop no funciona en multicapa (lo dice el paper).
6. Targets siempre en {−1,+1} (no {0,1}): coherente con el paper y con tanh; con entradas ±1 el α-LMS adapta todos los pesos en cada ciclo.
7. En `nbformat`/JSON del notebook, cuidar el escapado de backslashes de LaTeX dentro de strings de Python (usar raw strings `r'''...'''`).

---

## 6. FORMATO DE ENTREGA

Entrega en tu respuesta: (1) el archivo `.tex` completo en un bloque de código; (2) el notebook, ya sea como JSON `.ipynb` completo o como script generador con nbformat; (3) instrucciones de uso en 3 líneas (ejecutar notebook → copiar figs/ y tabs/ → compilar 2 veces con pdflatex). Todo el texto del informe en español formal académico chileno, sin anglicismos innecesarios (usar cursiva para términos como *backpropagation*, *feedforward*), citas con `\cite{}` en todas las afirmaciones tomadas del paper.
