# Unidad 4 — Análisis de Agrupamientos (Clustering)

> **Curso**: Inteligencia Computacional · USACH · Prof. Max Chacón
> **Fuente primaria**: [`data/processed/clases/Presentaciones_Prof_Max/capitulo-iv-inteligencia-computacional_aa/`](../../../data/processed/clases/Presentaciones_Prof_Max/capitulo-iv-inteligencia-computacional_aa/capitulo-iv-inteligencia-computacional_aa.md)
> **Bibliografía**: Han et al. — _Data Mining_, cap. 10 · Hastie §14.3.
> **Carga**: 4 h teoría + Laboratorio L3 · evalúa en **PEP 1**

---

## 1. Objetivos

- Comprender el concepto de **similaridad** y distancia en $\mathbb{R}^n$.
- Implementar y comparar métodos **jerárquicos** (aglomerativos) y **no jerárquicos** (partitivos).
- Aplicar las métricas de calidad de un agrupamiento.
- Elegir el método adecuado según la forma esperada de los clusters.

---

## 2. Medidas de similaridad / distancia

Una distancia $d : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ debe satisfacer:

1. **No-negatividad**: $d(x,y) \ge 0$, $d(x,x) = 0$.
2. **Simetría**: $d(x,y) = d(y,x)$.
3. **Desigualdad triangular**: $d(x,y) \le d(x,z) + d(z,y)$.

### 2.1 Familia Minkowski

$$
d_p(x,y) = \left(\sum_{i=1}^{n} |x_i - y_i|^p\right)^{1/p}
$$

| $p$      | Nombre                          | Propiedad                       |
| -------- | ------------------------------- | ------------------------------- |
| 1        | Manhattan (_city-block_, $L_1$) | Robusta a outliers              |
| 2        | Euclidiana ($L_2$)              | La más usada; sensible a escala |
| $\infty$ | Chebyshev                       | Máxima diferencia absoluta      |

### 2.2 Otras distancias relevantes

| Distancia       | Fórmula / Descripción                        | Uso                               |
| --------------- | -------------------------------------------- | --------------------------------- |
| **Mahalanobis** | $d = \sqrt{(x-y)^\top \mathbf{S}^{-1}(x-y)}$ | Corrige escala y correlaciones    |
| **Coseno**      | $1 - \frac{x \cdot y}{\|x\|\|y\|}$           | Texto, vectores de alta dimensión |
| **Hamming**     | $\sum_i \mathbf{1}[x_i \ne y_i]$             | Variables categóricas             |
| **Gower**       | Mezcla de continuas + categóricas            | Datos mixtos                      |

> **Buena práctica**: estandarizar las variables antes de aplicar $L_2$ para evitar que dimensiones de mayor escala dominen.

---

## 3. Métodos jerárquicos (aglomerativos)

### 3.1 Algoritmo general

```
1. Inicializar: cada punto es un cluster.
2. Calcular matriz de distancias D.
3. Repetir hasta tener un solo cluster:
   a. Unir los dos clusters más cercanos (según linkage).
   b. Actualizar D.
4. Resultado: dendrograma.
```

### 3.2 Criterios de enlace (_linkage_)

Sea $d(C_i, C_j)$ la distancia entre clusters $C_i$ y $C_j$:

| Enlace                | Fórmula                                                           | Comportamiento                                                |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- | --- | --- | ----------------------------------------- | -------------------------- |
| **Single** (mínimo)   | $\min_{x \in C_i,\, y \in C_j} d(x,y)$                            | Clusters alargados, sensible a ruido (efecto cadena)          |
| **Complete** (máximo) | $\max_{x \in C_i,\, y \in C_j} d(x,y)$                            | Clusters compactos, sensible a outliers                       |
| **Average (UPGMA)**   | $\frac{1}{                                                        | C_i                                                           |     | C_j | }\sum*{x \in C_i}\sum*{y \in C_j} d(x,y)$ | Equilibrio single/complete |
| **Ward**              | Minimiza la varianza intra-cluster al fusionar ($\Delta$ inercia) | Clusters esféricos y equitativos; el más usado en la práctica |

### 3.3 Corte del dendrograma

El número de clusters se define **cortando** el dendrograma a una altura $h$: el número de ramas que cruzan el corte horizontal = número de clusters. Se elige $h$ donde el salto de altura sea **máximo**.

---

## 4. Métodos partitivos: k-means

### 4.1 Algoritmo Lloyd (k-means estándar)

**Entrada**: $\mathbf{X}$, $k$. **Salida**: $k$ centroides $\mu_j$ y asignaciones $c_i$.

```
1. Inicializar k centroides μ_1,...,μ_k (aleatorio o k-means++).
2. Repetir hasta convergencia:
   a. Asignación: c_i = argmin_j d(x_i, μ_j)
   b. Actualización: μ_j = media de {x_i : c_i = j}
```

Minimiza la **inercia** (within-cluster sum of squares, WCSS):

$$
J = \sum_{j=1}^{k} \sum_{i:\, c_i = j} \|x_i - \mu_j\|^2
$$

### 4.2 Propiedades

- **Complejidad**: $O(n \cdot k \cdot d \cdot t)$, con $t$ = iteraciones.
- **Convergencia garantizada** a un mínimo local; resultado depende de inicialización.
- **k-means++**: inicialización inteligente que escoge centroides con probabilidad proporcional a $d^2$ → reduce iteraciones y mejora calidad.
- **Limitaciones**: clusters esféricos, igual varianza asumida, sensible a outliers, requiere $k$ a priori.

### 4.3 k-medoids (PAM)

- El centroide se reemplaza por el **medoide** (el punto real más central del cluster).
- **Ventaja**: robusto a outliers.
- **Desventaja**: más costoso ($O(n^2)$).

---

## 5. DBSCAN (clustering por densidad)

Define clusters como regiones de **alta densidad** separadas por regiones de baja densidad.

**Parámetros**: $\varepsilon$ (radio), $MinPts$ (mínimo de puntos en el $\varepsilon$-vecindario).

**Tipos de puntos**:

| Tipo       | Condición                                              |
| ---------- | ------------------------------------------------------ | ----------------- | ----------- |
| **Core**   | $                                                      | N\_\varepsilon(x) | \ge MinPts$ |
| **Border** | $< MinPts$ vecinos pero alcanzable desde un core point |
| **Noise**  | No core ni border                                      |

**Algoritmo**: expande clusters a partir de core points por **density-reachability**.

- No requiere $k$ a priori.
- Detecta **formas arbitrarias** y **ruido** (outliers clasificados como noise).
- Sensible a $\varepsilon$ y $MinPts$; costoso en alta dimensión (curse of dimensionality).

---

## 6. Métricas de calidad interna

Permiten evaluar agrupamientos **sin etiquetas externas**.

### 6.1 Índice de Silhouette

Para cada punto $i$:

$$
s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}
$$

- $a(i)$: distancia media a los puntos de **su propio** cluster.
- $b(i)$: distancia media al **cluster vecino más cercano**.
- $s(i) \in [-1, 1]$; mayor = mejor.

**Silhouette global**: $\bar{s} = \frac{1}{n}\sum_i s(i)$.

### 6.2 Davies-Bouldin (DB)

$$
\text{DB} = \frac{1}{k} \sum_{i=1}^{k} \max_{j \ne i} \frac{\sigma_i + \sigma_j}{d(\mu_i, \mu_j)}
$$

- $\sigma_j$: dispersión intra-cluster.
- Menor DB → mejor separación.

### 6.3 Calinski-Harabasz (CH) — Variance Ratio Criterion

$$
\text{CH} = \frac{\text{BSS}/(k-1)}{\text{WSS}/(n-k)}
$$

- BSS: varianza **entre** clusters. WSS: varianza **dentro** de clusters.
- Mayor CH → clusters más definidos.

### 6.4 Método del codo (para k-means)

Graficar WCSS vs $k$ y buscar el punto de "codo" donde la reducción adicional es mínima.

---

## 7. Comparación de métodos

| Criterio       | k-means    | k-medoids  | Jerárquico-Ward   | DBSCAN      |
| -------------- | ---------- | ---------- | ----------------- | ----------- |
| Requiere $k$   | Sí         | Sí         | No (post-corte)   | No          |
| Forma clusters | Esférica   | Esférica   | Esférica          | Arbitraria  |
| Outliers       | Sensible   | Robusto    | Sensible (single) | Los detecta |
| Escalabilidad  | Alta       | Media      | Baja ($O(n^2)$)   | Media-alta  |
| Determinista   | No (init.) | No (init.) | Sí                | Sí          |

---

## 8. Ejemplo numérico (clustering jerárquico)

Puntos en $\mathbb{R}^2$: $A(1,1)$, $B(1,2)$, $C(2,1)$, $D(5,4)$, $E(5,5)$.

Matriz de distancias euclidianas:

|     | A    | B    | C    | D    | E    |
| --- | ---- | ---- | ---- | ---- | ---- |
| A   | 0    | 1.00 | 1.00 | 5.00 | 5.66 |
| B   | 1.00 | 0    | 1.41 | 4.47 | 5.00 |
| C   | 1.00 | 1.41 | 0    | 4.24 | 5.00 |
| D   | 5.00 | 4.47 | 4.24 | 0    | 1.41 |
| E   | 5.66 | 5.00 | 5.00 | 1.41 | 0    |

**Linkage single**, paso a paso:

1. Une $A$-$B$ (dist=1.00) → cluster $\{A,B\}$.
2. Une $\{A,B\}$-$C$ (min dist: $d(B,C)=1.41$, $d(A,C)=1.00$ → 1.00) → $\{A,B,C\}$.
3. Une $D$-$E$ (dist=1.41) → $\{D,E\}$.
4. Une $\{A,B,C\}$-$\{D,E\}$ (dist mínima = $d(C,D)=4.24$) → un solo cluster.

Corte a $h=2$ → 2 clusters: $\{A,B,C\}$ y $\{D,E\}$.

---

## 9. Clustering en el pipeline KDD

| Etapa KDD         | Rol                                                      |
| ----------------- | -------------------------------------------------------- |
| Pre-procesamiento | Estandarizar variables (obligatorio para k-means).       |
| Transformación    | Reducción con PCA para visualización 2D/3D.              |
| Minería           | Aplicar método + seleccionar $k$ / parámetros.           |
| Evaluación        | Silhouette, DB, CH, validación externa si hay etiquetas. |
| Conocimiento      | Caracterizar cada cluster (estadísticos, reglas).        |

---

## 10. Conceptos clave para PEP 1

- Calcular la **matriz de distancias** y ejecutar agrupamiento jerárquico **a mano** para pocos puntos.
- Diferencia entre **single**, **complete**, **average** y **Ward** (fórmulas y comportamiento).
- Saber cuándo usar k-means vs DBSCAN.
- Calcular el **índice Silhouette** para un punto específico.
- Interpretar el **dendrograma** y elegir el número de clusters por mayor salto.

---

## 11. Recursos

- Notebook: [04_clustering.ipynb](../../../notebooks/ejercicios/04_clustering.ipynb).
- Ejercicios: `data/raw/Ejercicios/Guía - Análisis de Agrupamiento.pdf`.
- Han, Kamber, Pei, _Data Mining: Concepts and Techniques_, 3rd ed., Cap. 10.
- Hastie, Tibshirani, Friedman, _Elements of Statistical Learning_, §14.3.
- `sklearn.cluster`: `KMeans`, `AgglomerativeClustering`, `DBSCAN`.
- `sklearn.metrics`: `silhouette_score`, `davies_bouldin_score`, `calinski_harabasz_score`.
