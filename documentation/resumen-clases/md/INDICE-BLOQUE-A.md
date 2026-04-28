# Índice Bloque A — PEP 1 (Unidades 1–4)

> **Inteligencia Computacional · USACH · Prof. Max Chacón**  
> Generado: 2026-04-27

## Documentación generada

### Resúmenes teóricos

| Unidad                   | Archivo                                            | Temas principales                                                                                           |
| ------------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1 — Introducción/KDD     | [U1-introduccion-kdd.md](U1-introduccion-kdd.md)   | Datos→Conocimiento, etapas KDD, OLTP/OLAP, tipología de problemas, regresión vs aprendizaje no lineal       |
| 2 — PCA                  | [U2-pca.md](U2-pca.md)                             | Formulación geométrica y algebraica, autovalores, covarianza vs correlación, Kaiser, biplot, reconstrucción |
| 3 — Reglas de asociación | [U3-reglas-asociacion.md](U3-reglas-asociacion.md) | Soporte, confianza, lift, conviction, Apriori, FP-Growth, propiedad anti-monotónica                         |
| 4 — Clustering           | [U4-clustering.md](U4-clustering.md)               | Distancias, jerárquico (4 linkages), k-means, DBSCAN, Silhouette, DB, CH                                    |

### Guía de ejercicios resueltos

| Archivo                                                      | Contenido                                                                                                                                                       |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Ejercicios-resueltos-PEP1.md](Ejercicios-resueltos-PEP1.md) | 12 ejercicios completamente resueltos tipo lápiz-papel: KDD, PCA (autovalores, Kaiser, biplot), Apriori paso a paso, clustering jerárquico, k-means, Silhouette |

### Notebooks

| Notebook                     | Unidad | Ubicación                                                                      |
| ---------------------------- | ------ | ------------------------------------------------------------------------------ |
| `00_intro_kdd.ipynb`         | U1     | [notebooks/exploratory/](../../notebooks/exploratory/00_intro_kdd.ipynb)       |
| `02_pca.ipynb`               | U2     | [notebooks/ejercicios/](../../notebooks/ejercicios/02_pca.ipynb)               |
| `03_reglas_asociacion.ipynb` | U3     | [notebooks/ejercicios/](../../notebooks/ejercicios/03_reglas_asociacion.ipynb) |
| `04_clustering.ipynb`        | U4     | [notebooks/ejercicios/](../../notebooks/ejercicios/04_clustering.ipynb)        |

---

## Tabla de conceptos clave (cheatsheet rápido)

### PCA

$$
\mathbf{S}\mathbf{v}_k = \lambda_k \mathbf{v}_k \qquad
\text{VEA}(q) = \frac{\sum_{k=1}^{q}\lambda_k}{\sum_{k=1}^{p}\lambda_k} \qquad
\text{Kaiser}: \lambda_k > 1
$$

### Reglas de asociación

$$
s(A{\Rightarrow}B) = P(A \cup B) \qquad
c(A{\Rightarrow}B) = \frac{s(A \cup B)}{s(A)} \qquad
\text{lift} = \frac{c(A{\Rightarrow}B)}{s(B)} \qquad
\text{conv} = \frac{1-s(B)}{1-c}
$$

### Clustering

$$
d_p(x,y)=\left(\sum_i|x_i-y_i|^p\right)^{1/p} \qquad
J_{k\text{-means}}=\sum_j\sum_{i:c_i=j}\|x_i-\mu_j\|^2
$$

$$
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))} \qquad
\text{DB}=\frac{1}{k}\sum_i\max_{j\ne i}\frac{\sigma_i+\sigma_j}{d(\mu_i,\mu_j)}
$$

---

## Fuentes primarias

| Material              | Ruta                                                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Cap. I Prof. Chacón   | `data/processed/clases/Presentaciones_Prof_Max/capitulo-i-inteligencia-computacional_introducción/`                  |
| Cap. II Prof. Chacón  | `data/processed/clases/Presentaciones_Prof_Max/capítulo-ii-inteligencia-computacional_acp/`                          |
| Cap. III Prof. Chacón | `data/processed/clases/Presentaciones_Prof_Max/capitulo-iii-inteligencia-computaional_ra/`                           |
| Cap. IV Prof. Chacón  | `data/processed/clases/Presentaciones_Prof_Max/capitulo-iv-inteligencia-computacional_aa/`                           |
| Outline Bishop        | `data/processed/libros/pattern-recognition-and-machine-learning-bishop/outline.md`                                   |
| Outline Hastie        | `data/processed/libros/the-elements-of-statistical-learning-trevor-hastie-1/outline.md`                              |
| Outline Han           | `data/processed/libros/data-mining-concepts-and-techniques-3rd-ed-jiawei-han-micheline-kamber-jian-pei-1/outline.md` |

---

## Estado de avance — Bloque A

| Hito                            | Estado                           |
| ------------------------------- | -------------------------------- |
| Leer Cap. I–IV del Prof. Chacón | ✅ Material procesado disponible |
| Resúmenes U1–U4                 | ✅ Generados                     |
| Notebooks de ejercicios         | ✅ Generados (U1–U4)             |
| Guía ejercicios resueltos PEP1  | ✅ Generada                      |
| Dataset común L1–L5 definido    | 🔜 Pendiente                     |
| L1 PCA sobre dataset propio     | 🔜 Pendiente                     |
| L2 Reglas de asociación         | 🔜 Pendiente                     |
| L3 Clustering ≥2 métodos        | 🔜 Pendiente                     |
| Repaso-PEP1.md (síntesis final) | 🔜 Pendiente                     |
