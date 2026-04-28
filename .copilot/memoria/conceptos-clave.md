# Conceptos Clave — Inteligencia Computacional

> **Archivo compartido**: versionado en Git. El agente "Profe Inteligencia Computacional" actualiza este mapa conforme se discuten y refuerzan conceptos en sesiones.

## Mapa de Conceptos por Unidad

### Unidad 1 — Introducción

- Inteligencia computacional vs IA simbólica vs estadística clásica
- Tipología de problemas: descripción, asociación, agrupamiento, clasificación, regresión, predicción de series
- KDD pipeline: selección → preprocesamiento → transformación → minería → evaluación
- Aprendizaje supervisado vs no supervisado vs semi-supervisado vs por refuerzo

### Unidad 2 — Análisis de Componentes Principales (PCA)

- Matriz de covarianza/correlación
- Descomposición espectral, eigenvalores y eigenvectores
- Varianza explicada acumulada, regla del codo, criterio de Kaiser ($\lambda_i > 1$)
- Biplot, loadings, scores
- Conexión con SVD: $X = U\Sigma V^T$

### Unidad 3 — Reglas de Asociación

- Soporte (support), confianza (confidence), lift
- Algoritmo Apriori, propiedad antimonotónica
- FP-Growth (FP-Tree)
- Itemsets frecuentes, reglas fuertes
- Métricas alternativas: conviction, leverage

### Unidad 4 — Análisis de Agrupamientos (Clustering)

- Jerárquico aglomerativo (single, complete, average, Ward) y divisivo
- k-means, k-medoids (PAM)
- DBSCAN, OPTICS
- Métricas internas: silhouette, Davies–Bouldin, Calinski–Harabasz
- Métricas externas: ARI, NMI

### Unidad 5 — Evaluación Estadística

- Holdout, k-fold CV, leave-one-out, bootstrap
- Test de hipótesis: t-test pareado, Wilcoxon, McNemar (clasificadores), ANOVA, Friedman
- Intervalos de confianza, p-valor, potencia

### Unidad 6 — Clasificación Bayesiana

- Teorema de Bayes: $P(C|x) = \frac{P(x|C)P(C)}{P(x)}$
- Naive Bayes (independencia condicional)
- Redes bayesianas (DAG)
- Estimación MLE vs MAP
- Análisis discriminante (LDA, QDA)

### Unidad 7 — Árboles de Decisión

- Entropía $H(S) = -\sum p_i \log_2 p_i$, ganancia de información
- Gini, gain ratio
- ID3, C4.5, CART
- Pruning (pre/post), random forest, boosting (AdaBoost, GBM, XGBoost)

### Unidad 8 — Paradigma Conexionista

- Neurona biológica vs artificial
- Perceptrón de Rosenblatt, función de activación (step, sigmoid, tanh, ReLU)
- Adaline, regla delta
- Capacidad de representación, separabilidad lineal

### Unidad 9 — Retro-propagación del Error (Backpropagation)

- MLP (Multi-Layer Perceptron), funciones de costo (MSE, cross-entropy)
- Regla de la cadena, $\delta = \frac{\partial E}{\partial \text{net}}$
- Algoritmos: gradiente descendente, momentum, Nesterov, RMSprop, Adam
- Regularización: L1/L2, dropout, early stopping
- Redes RBF (Radial Basis Function)

### Unidad 10 — Redes Neuronales con Retroalimentación

- Hopfield (memoria asociativa, energía)
- Elman, Jordan (recurrentes simples)
- BPTT (Backpropagation Through Time)
- LSTM, GRU (gates: forget, input, output)
- Aplicaciones: series temporales, NLP, identificación de sistemas

## Relaciones entre Conceptos

- PCA ↔ SVD ↔ autoencoders lineales (NN sin activación no lineal)
- Naive Bayes ↔ regresión logística (en frontera de decisión cuando las clases son normales con misma covarianza)
- Árboles ↔ random forest ↔ gradient boosting (familia)
- MLP ↔ aproximador universal (teorema de Cybenko, Hornik)

## Errores Conceptuales Comunes

- (a registrar a medida que aparezcan)
