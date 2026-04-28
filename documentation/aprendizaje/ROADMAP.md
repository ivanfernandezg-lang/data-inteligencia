# Roadmap de Estudio — Inteligencia Computacional (USACH)

> Hoja de ruta progresiva basada en el programa oficial del curso (Prof. Max Chacón) y el material disponible en este repositorio.
> Documento base: [`data/raw/Documentacion Oficial/introduccion.md`](../../data/raw/Documentacion%20Oficial/introduccion.md)
> Inventario: [`.copilot/memoria/inventario-material.md`](../../.copilot/memoria/inventario-material.md)

## Visión general

El curso tiene **17 semanas** divididas en **3 bloques de evaluación** y **5 laboratorios** que comparten el mismo dataset (idealmente biomédico).

| Bloque | Unidades | Evaluación        | Semanas aprox. |
| ------ | -------- | ----------------- | -------------- |
| A      | 1–4      | **PEP 1**         | 1–6            |
| B      | 5–7      | **PEP 2**         | 7–11           |
| C      | 8–10     | **Trabajo final** | 12–17          |

En paralelo:

- **L1** durante bloque A (PCA / EDA)
- **L2** durante bloque A (reglas de asociación)
- **L3** durante bloque A→B (clustering)
- **L4** durante bloque B (Bayes y/o árboles)
- **L5** durante bloque C (redes neuronales)

---

## Fase 0 — Setup (semana 0, 2–3 h)

**Objetivo**: dejar el entorno listo y procesar todo el material.

1. Crear venv e instalar dependencias:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. Procesar capítulos del Prof. Chacón:
   ```powershell
   python scripts/utils/pdf_extractor.py "data/raw/clases/Presentaciones_Prof_Max" --format md --all
   ```
3. Generar outline de los libros pesados (sin cargarlos enteros):
   ```powershell
   python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --outline-md --save
   python scripts/utils/book_explorer.py "data/raw/Libros/The Elements of Statistical Learning - Trevor Hastie 1.pdf" --outline-md --save
   python scripts/utils/book_explorer.py "data/raw/Libros/Data Mining - Concepts and Techniques [3rd ed.] - Jiawei Han, Micheline Kamber, Jian Pei 1 .pdf" --outline-md --save
   ```
4. Definir el **dataset común L1–L5** (sugerencia: dataset biomédico como `Wisconsin Breast Cancer`, `Pima Indians Diabetes`, `MIMIC-III`, o algún dataset clínico abierto). Guardar en `data/raw/datasets/<nombre>/`.
5. Conformar pareja para los laboratorios.

---

## Bloque A — Hacia la PEP 1 (Unidades 1–4)

### Semana 1 — Unidad 1: Introducción (3 h teoría)

- **Lectura**: Capítulo I del Prof. Chacón (`data/processed/capitulo-i-...`).
- **Conceptos clave**: KDD pipeline, tipología de problemas, supervisado vs no supervisado.
- **Complementario**: Han cap. 1 (búsqueda con `book_explorer.py --search "knowledge discovery"`).
- **Entregable interno**: notebook `notebooks/exploratory/00_intro_kdd.ipynb` con un ejemplo simple del pipeline.

### Semana 2–3 — Unidad 2: PCA (3 h teoría) + 🧪 **L1**

- **Lectura**: Capítulo II del Prof. Chacón + `data/raw/Presentaciones/Análisis en Componentes Principales/`.
- **Apuntes**: `data/raw/apuntes/analisis de componentes/`.
- **Bibliografía**: Bishop §12.1 (`book_explorer.py --search "principal component"`), Hastie §14.5.
- **Ejercicios**: `data/raw/Ejercicios/Guía - Análisis de Componentes Principales.pdf`.
- **Notebook**: `notebooks/ejercicios/02_pca.ipynb` (matriz de covarianza, eigenvalores, biplot, varianza explicada).
- **🧪 L1 — PCA / EDA del dataset L1–L5**:
  - Fase 1–7 según `documentation/tareas/plantillas/`
  - Visualizar primeras 2–3 componentes, loadings, scree plot.
  - Entregable: `documentation/reports/L1-PCA.md` + notebook en `notebooks/reports/`.

### Semana 4 — Unidad 3: Reglas de asociación (4 h teoría) + 🧪 **L2**

- **Lectura**: Capítulo III del Prof. Chacón. Han caps. 6–7 (Apriori, FP-Growth).
- **Conceptos**: support, confidence, lift, conviction; `mlxtend.frequent_patterns`.
- **Notebook**: `notebooks/ejercicios/03_reglas_asociacion.ipynb` con dataset transaccional.
- **🧪 L2**: discretizar el dataset común y aplicar Apriori/FP-Growth.

### Semana 5 — Unidad 4: Análisis de agrupamientos (4 h teoría) + 🧪 **L3**

- **Lectura**: Capítulo IV del Prof. Chacón. Han cap. 10. Hastie §14.3.
- **Métodos**: jerárquico (single/complete/average/Ward), k-means, k-medoids, DBSCAN.
- **Métricas**: silhouette, Davies–Bouldin, Calinski–Harabasz.
- **Ejercicios**: `Guía - Análisis de Agrupamiento.pdf`.
- **Notebook**: `notebooks/ejercicios/04_clustering.ipynb`.
- **🧪 L3**: aplicar ≥2 métodos al dataset común y comparar con métricas.

### Semana 6 — Repaso y **PEP 1**

- **Resolver**: `data/raw/Ejercicios/IC_Ejercicios_PEP1_20-04-2026.pdf`.
- **Documentar**: `documentation/aprendizaje/Repaso-PEP1.md` con resúmenes y ejercicios resueltos.
- **Checklist PEP1**: KDD, PCA (autovalores/varianza explicada), Apriori (cómputo manual), clustering (jerárquico paso a paso).

---

## Bloque B — Hacia la PEP 2 (Unidades 5–7)

### Semana 7 — Unidad 5: Evaluación Estadística (2 h teoría)

- **Lectura**: Capítulo V del Prof. Chacón + `data/raw/apuntes/INFERENCIA Y MODELOS ESTADÍSTICOS Jacqueline Köhler C.pdf`.
- **Conceptos**: holdout, k-fold, leave-one-out, bootstrap; t-test pareado, McNemar, Wilcoxon, Friedman.
- **Notebook**: `notebooks/ejercicios/05_evaluacion_estadistica.ipynb` con `scipy.stats` y `pingouin`.

### Semana 8–9 — Unidad 6: Clasificación Bayesiana (5 h teoría) + 🧪 **L4 (parte 1)**

- **Lectura**: Capítulo VI del Prof. Chacón. Bishop cap. 8 (`--search "Bayesian network"`), Hastie §6.6.
- **Métodos**: Naive Bayes (Gaussiano/Multinomial/Bernoulli), LDA/QDA, redes bayesianas (intro).
- **Notebook**: `notebooks/ejercicios/06_bayes.ipynb` con `sklearn.naive_bayes`.
- **🧪 L4 parte 1**: aplicar Naive Bayes al dataset común con validación k-fold y test estadístico.

### Semana 10–11 — Unidad 7: Árboles de decisión (5 h teoría) + 🧪 **L4 (parte 2)** + **PEP 2**

- **Lectura**: Capítulo VII del Prof. Chacón. Hastie cap. 9–10–15 (árboles, boosting, RF).
- **Métodos**: ID3, C4.5, CART, pruning, Random Forest, XGBoost.
- **Notebook**: `notebooks/ejercicios/07_arboles.ipynb`.
- **🧪 L4 parte 2**: comparar árboles vs Bayes en el mismo dataset (test de McNemar).
- **PEP 2**: repaso de Unidades 5–7 en `documentation/aprendizaje/Repaso-PEP2.md`.

---

## Bloque C — Trabajo Final + L5 (Unidades 8–10)

### Semana 12 — Unidad 8: Paradigma Conexionista (2 h teoría)

- **Lectura**: ⚠️ no hay capítulo del Prof. Chacón aún. Usar:
  - Haykin caps. 1–4 (`book_explorer.py "data/raw/Libros/<Haykin>.pdf" --toc`)
  - Bishop cap. 5
  - Bonelli (libro oficial traducido)
- **Conceptos**: neurona biológica/artificial, perceptrón, Adaline, separabilidad lineal.

### Semana 13–14 — Unidad 9: Retro-propagación del Error (4 h teoría) + 🧪 **L5 (parte 1)**

- **Lectura**: Haykin caps. 4–5; Bishop cap. 5; apuntes complementarios.
- **Conceptos**: MLP, regla de la cadena, MSE/cross-entropy, momentum/Adam, regularización (L1/L2/dropout/early stopping), RBF.
- **Notebook**: `notebooks/ejercicios/09_mlp_backprop.ipynb` (implementación manual + Keras).
- **🧪 L5 parte 1**: MLP sobre dataset común, comparar con métodos previos (Bayes, árboles).

### Semana 15–16 — Unidad 10: Redes con retroalimentación (6 h teoría) + 🧪 **L5 (parte 2)**

- **Lectura**: Haykin caps. 13–15; Suykens (control no lineal).
- **Modelos**: Hopfield, Elman/Jordan, BPTT, LSTM, GRU.
- **Notebook**: `notebooks/ejercicios/10_rnn_lstm.ipynb`.
- **🧪 L5 parte 2**: aplicar RNN/LSTM si el dataset tiene componente temporal, o cerrar comparación final.

### Semana 17 — Trabajo Final

- **Formato**: revisión bibliográfica + presentación oral + informe escrito.
- **Carpeta**: `documentation/investigacion/md/`.
- **Sugerencia de tema**: comparación de arquitecturas recurrentes (LSTM/GRU/Echo State) en una aplicación biomédica.
- **Bibliografía**: papers en `data/raw/papers/` + Haykin + Bishop + Suykens (extraer secciones con `book_explorer.py --search`).
- **Entrega**: informe en `documentation/reports/Trabajo-Final.md` + slides + presentación.

---

## Checklist Transversal

Para cada unidad y laboratorio, asegurar:

- [ ] Capítulo del Prof. Chacón leído (o equivalente en libro si no existe).
- [ ] Conceptos registrados en `.copilot/memoria/conceptos-clave.md`.
- [ ] Notebook con ejemplo numérico ejecutable.
- [ ] Comparación con al menos otro método visto en clase.
- [ ] Validación estadística donde corresponda.
- [ ] Memoria del estudiante actualizada (`.copilot/memoria/progreso-estudiante.md`).

## Estimación de carga

| Bloque       | Horas teoría | Horas laboratorio | Horas estudio personal | Total aprox. |
| ------------ | ------------ | ----------------- | ---------------------- | ------------ |
| A (Ud. 1–4)  | 14           | ~24 (L1–L3)       | 30                     | ~70 h        |
| B (Ud. 5–7)  | 12           | ~12 (L4)          | 25                     | ~50 h        |
| C (Ud. 8–10) | 12           | ~12 (L5)          | 30 (+ trabajo final)   | ~55 h        |

## Próximos hitos inmediatos

1. ✅ Procesar capítulos del Prof. Chacón → `data/processed/`.
2. ✅ Generar outlines de Bishop, Hastie y Han con `book_explorer.py`.
3. 🔜 Definir dataset L1–L5 (idealmente biomédico) y dejarlo en `data/raw/datasets/`.
4. 🔜 Resolver `IC_Ejercicios_PEP1_20-04-2026.pdf` como ensayo.
5. 🔜 Iniciar L1 (PCA/EDA) en `notebooks/reports/L1-PCA.ipynb`.
