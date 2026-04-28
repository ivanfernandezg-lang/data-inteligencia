# Unidad 2 — Análisis de Componentes Principales (ACP / PCA)

> **Curso**: Inteligencia Computacional · USACH · Prof. Max Chacón
> **Fuente primaria**: [`data/processed/clases/Presentaciones_Prof_Max/capítulo-ii-inteligencia-computacional_acp/`](../../../data/processed/clases/Presentaciones_Prof_Max/cap%C3%ADtulo-ii-inteligencia-computacional_acp/cap%C3%ADtulo-ii-inteligencia-computacional_acp.md)
> **Apuntes**: [`data/raw/apuntes/analisis de componentes/`](../../../data/raw/apuntes/analisis%20de%20componentes/)
> **Bibliografía**: Bishop §12.1 · Hastie §14.5 · Han §3.4
> **Carga**: 3 h teoría + Laboratorio L1 · evalúa en **PEP 1**

---

## 1. Objetivos

- Reducir dimensionalidad preservando la **máxima varianza**.
- Construir un sistema ortonormal de ejes nuevos (componentes) ordenado por varianza.
- Comprender la equivalencia entre PCA y la **descomposición espectral** de la matriz de covarianza.
- Interpretar **loadings**, **scores**, **scree plot** y **biplot**.
- Decidir cuántas componentes retener.

---

## 2. Formulación geométrica (Chacón, Cap. II)

Buscamos una **transformación ortonormal** $\mathbf{y} = \mathbf{A}^\top (\mathbf{x} - \bar{\mathbf{x}})$ tal que:

- el **primer eje** $y_1$ apunta en la dirección de **máxima dispersión** de los datos,
- el **segundo eje** $y_2$ es ortogonal a $y_1$ y captura la siguiente máxima dispersión,
- y así sucesivamente.

Para una rotación, los elementos $a_{ij}$ son **cosenos directores**:

$$
y_1 = a_{11}(x_1 - \bar{x}_1) + a_{12}(x_2 - \bar{x}_2) + a_{13}(x_3 - \bar{x}_3)
$$

con la restricción $a_{11}^2 + a_{12}^2 + a_{13}^2 = 1$ (vector de norma unitaria).

---

## 3. Formulación algebraica

Sea $\mathbf{X} \in \mathbb{R}^{n \times p}$ centrada (cada columna con media 0). La matriz de covarianza muestral es:

$$
\mathbf{S} = \frac{1}{n-1}\mathbf{X}^\top \mathbf{X}
$$

PCA resuelve el problema de optimización:

$$
\max_{\mathbf{a}} \; \mathbf{a}^\top \mathbf{S} \mathbf{a} \quad \text{s.a.} \quad \mathbf{a}^\top \mathbf{a} = 1
$$

cuya solución (multiplicadores de Lagrange) es la **ecuación de autovalores**:

$$
\mathbf{S}\mathbf{a} = \lambda \mathbf{a}
$$

- Los **autovectores** $\mathbf{a}_k$ son las **direcciones principales** (loadings).
- Los **autovalores** $\lambda_k$ son las **varianzas** explicadas por cada componente.
- Las **componentes principales** (scores) son $\mathbf{Y} = \mathbf{X}\mathbf{A}$.

### Propiedades

1. $\sum_{k=1}^{p} \lambda_k = \operatorname{traza}(\mathbf{S}) = \sum_{j=1}^{p} \operatorname{Var}(x_j)$.
2. Las componentes son **mutuamente ortogonales** y **decorrelacionadas**.
3. La **varianza explicada acumulada** por las primeras $q$ componentes es:

$$
\text{VEA}(q) = \frac{\sum_{k=1}^{q} \lambda_k}{\sum_{k=1}^{p} \lambda_k}
$$

---

## 4. PCA vía SVD (vía operativa)

$$
\mathbf{X} = \mathbf{U}\,\mathbf{\Sigma}\,\mathbf{V}^\top
$$

- $\mathbf{V}$ contiene los autovectores de $\mathbf{X}^\top\mathbf{X}$ (loadings).
- Los autovalores son $\lambda_k = \sigma_k^2 / (n-1)$.
- Scores: $\mathbf{Y} = \mathbf{U}\mathbf{\Sigma} = \mathbf{X}\mathbf{V}$.

Más estable numéricamente que computar $\mathbf{S}$ explícitamente. Es el método interno de `sklearn.decomposition.PCA`.

---

## 5. Estandarización: ¿cuándo es obligatoria?

PCA es sensible a la **escala** de los atributos. Si las variables tienen **unidades distintas** (mg/dL, mmHg, kg…), es obligatorio:

$$
z_{ij} = \frac{x_{ij} - \bar{x}_j}{s_j}
$$

En este caso PCA se aplica a la **matriz de correlación** $\mathbf{R}$ (que es la covarianza de las variables estandarizadas).

| Situación                            | Usar covarianza $\mathbf{S}$ | Usar correlación $\mathbf{R}$ |
| ------------------------------------ | :--------------------------: | :---------------------------: |
| Mismas unidades, escalas comparables |              ✔               |                               |
| Unidades distintas                   |                              |               ✔               |
| Una variable domina por escala       |                              |               ✔               |

---

## 6. Selección del número de componentes

Tres criterios complementarios:

1. **Varianza explicada acumulada** ≥ umbral (típico 70–90 %).
2. **Criterio de Kaiser**: retener componentes con $\lambda_k > 1$ (válido sobre matriz de correlación).
3. **Scree plot / codo**: punto donde la curva $\lambda_k$ vs $k$ "se aplana".

---

## 7. Interpretación

- **Loadings** $\mathbf{V}$: peso de cada variable original en cada componente. Variables con $|v_{jk}|$ alto **definen** la componente $k$.
- **Scores** $\mathbf{Y}$: coordenadas de los individuos en el espacio reducido. Útiles para visualizar grupos.
- **Biplot**: superpone scores (puntos) y loadings (flechas) en el plano de las dos primeras componentes.
- **Comunalidad** de la variable $j$ con $q$ componentes: $h_j^2 = \sum_{k=1}^{q} v_{jk}^2 \lambda_k$ (sobre $\mathbf{R}$). Indica cuánta varianza de $x_j$ es retenida.

---

## 8. Ejemplo numérico mínimo

Dataset:

$$
\mathbf{X} = \begin{pmatrix} 2.5 & 2.4 \\ 0.5 & 0.7 \\ 2.2 & 2.9 \\ 1.9 & 2.2 \\ 3.1 & 3.0 \\ 2.3 & 2.7 \\ 2.0 & 1.6 \\ 1.0 & 1.1 \\ 1.5 & 1.6 \\ 1.1 & 0.9 \end{pmatrix}
$$

Pasos:

1. Medias: $\bar{x}_1 = 1.81, \bar{x}_2 = 1.91$.
2. Matriz de covarianza:
   $$
   \mathbf{S} = \begin{pmatrix} 0.6166 & 0.6154 \\ 0.6154 & 0.7166 \end{pmatrix}
   $$
3. Autovalores: $\lambda_1 = 1.2840$, $\lambda_2 = 0.0491$.
4. Autovectores: $\mathbf{v}_1 = (0.6779, 0.7352)^\top$, $\mathbf{v}_2 = (-0.7352, 0.6779)^\top$.
5. Varianza explicada por PC1: $1.2840 / (1.2840+0.0491) \approx 96.3\%$.

Interpretación: una sola componente captura prácticamente toda la información — los datos son **casi unidimensionales** en el plano original.

---

## 9. PCA en el pipeline KDD

| Etapa KDD         | Rol de PCA                                      |
| ----------------- | ----------------------------------------------- |
| Pre-procesamiento | Identificar outliers en el plano $(y_1, y_2)$.  |
| Transformación    | Reducir dimensionalidad (compresión).           |
| Minería de Datos  | Descorrelacionar entradas para regresión / MLP. |
| Visualización     | Proyección 2D / 3D para inspección humana.      |

---

## 10. Limitaciones

- Asume **relaciones lineales** entre variables. Para no-linealidad: **Kernel PCA**, **Isomap**, **t-SNE**, **UMAP**, **Autoencoders**.
- Componentes son combinaciones lineales **densas** ⇒ pierde interpretabilidad si $p$ es alto. Alternativa: **Sparse PCA**.
- Sensible a outliers (la varianza es no-robusta). Alternativa: **Robust PCA**.

---

## 11. Conceptos clave para PEP 1

- Saber **derivar** la ecuación de autovalores desde el problema de optimización.
- Calcular a mano los autovalores de una matriz $2\times 2$ y su varianza explicada.
- Distinguir **covarianza vs correlación** y cuándo usar cada una.
- Interpretar un **scree plot** y aplicar el **criterio de Kaiser**.
- Saber leer un **biplot**: distancia entre puntos = similitud entre individuos; ángulo entre flechas = correlación entre variables.

---

## 12. Recursos

- Notebook: [02_pca.ipynb](../../../notebooks/ejercicios/02_pca.ipynb).
- Ejercicios: `data/raw/Ejercicios/Guía - Análisis de Componentes Principales.pdf`.
- Bishop, _Pattern Recognition and Machine Learning_, §12.1–§12.2.
- Hastie, Tibshirani, Friedman, _Elements of Statistical Learning_, §14.5.
- Jolliffe, I. T. (2002). _Principal Component Analysis_, 2nd ed., Springer.
