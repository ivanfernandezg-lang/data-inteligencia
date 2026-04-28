# Guía de Ejercicios Resueltos — PEP 1

> **Inteligencia Computacional · USACH · Prof. Max Chacón**  
> Unidades 1–4 · Bloque A  
> Formato: lápiz y papel (sin computador)

---

## Unidad 1 — Introducción y KDD

### Ejercicio 1.1 — Etapas del KDD

**Enunciado**: Describa las 5 etapas del proceso KDD según Fayyad (1996) y proporcione un ejemplo de cada una para un dataset clínico de pacientes diabéticos.

**Resolución**:

| Etapa                    | Descripción                                        | Ejemplo (Diabetes)                                                                      |
| ------------------------ | -------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **1. Selección**         | Identificar datos relevantes del repositorio       | Extraer registros de pacientes con HbA1c, glucosa, IMC de los últimos 5 años            |
| **2. Pre-procesamiento** | Limpieza, tratamiento de faltantes                 | Imputar glucosa faltante con la mediana; eliminar registros duplicados                  |
| **3. Transformación**    | Normalización, reducción, construcción de features | Estandarizar variables (µ=0, σ=1); calcular PCA para visualización                      |
| **4. Minería de datos**  | Aplicar el algoritmo                               | Árbol de decisión C4.5 para clasificar Diabético/No Diabético                           |
| **5. Evaluación**        | Validar y traducir a conocimiento                  | Validación cruzada 10-fold; accuracy=87%; regla "si glucosa>140 y IMC>30 → riesgo alto" |

> **Nota de examen**: el KDD es **iterativo**. La retroalimentación entre etapas es parte de la respuesta esperada.

---

### Ejercicio 1.2 — OLTP vs OLAP

**Enunciado**: Un hospital opera con un sistema de fichas clínicas electrónicas (cada consulta genera transacciones) y adicionalmente quiere analizar tendencias de enfermedades en los últimos 10 años. Clasifique ambas necesidades como OLTP u OLAP y justifique.

**Resolución**:

- **Fichas clínicas electrónicas** → **OLTP**: operaciones frecuentes de lectura/escritura individual (una consulta = una transacción), requieren baja latencia y diseño normalizado.
- **Análisis de tendencias históricas** → **OLAP / Data Warehouse**: consultas de agregación sobre grandes volúmenes históricos (por ejemplo, `GROUP BY año, diagnóstico`), latencia de segundos aceptable, diseño en estrella.

---

### Ejercicio 1.3 — Tipos de aprendizaje

**Enunciado**: Clasifique los siguientes problemas según el tipo de supervisión:

a) Dado un conjunto de imágenes de células sin etiquetar, encontrar grupos de formas similares.  
b) Con muestras etiquetadas de tumores (benigno/maligno), construir un predictor.  
c) Dado un historial de medicamentos y resultado, aprender qué dosis prescribir.

**Resolución**:

| Problema                           | Tipo               | Justificación                                   |
| ---------------------------------- | ------------------ | ----------------------------------------------- |
| (a) Agrupar imágenes sin etiquetas | **No supervisado** | No hay variable de respuesta $y$                |
| (b) Predecir benigno/maligno       | **Supervisado**    | Etiquetas disponibles en entrenamiento          |
| (c) Aprender dosis óptima          | **Refuerzo**       | La señal es una recompensa (resultado) diferida |

---

## Unidad 2 — PCA

### Ejercicio 2.1 — Autovalores y varianza explicada

**Enunciado**: Dada la siguiente matriz de covarianza de 2 variables:

$$
\mathbf{S} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}
$$

a) Calcule los autovalores.  
b) Calcule los autovectores correspondientes (norma unitaria).  
c) ¿Qué porcentaje de la varianza total explica la primera componente principal?

**Resolución**:

**a) Autovalores**. Resolver $\det(\mathbf{S} - \lambda \mathbf{I}) = 0$:

$$
(4-\lambda)(3-\lambda) - 4 = 0
$$

$$
\lambda^2 - 7\lambda + 8 = 0
$$

$$
\lambda = \frac{7 \pm \sqrt{49-32}}{2} = \frac{7 \pm \sqrt{17}}{2}
$$

$$
\boxed{\lambda_1 = \frac{7+\sqrt{17}}{2} \approx 5.561, \quad \lambda_2 = \frac{7-\sqrt{17}}{2} \approx 1.439}
$$

**b) Autovectores**.

Para $\lambda_1 \approx 5.561$: resolver $(\mathbf{S} - \lambda_1 \mathbf{I})\mathbf{v} = 0$:

$$
\begin{pmatrix} -1.561 & 2 \\ 2 & -2.561 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \mathbf{0}
$$

De la primera fila: $v_1 = \frac{2}{1.561} v_2 \approx 1.281\, v_2$.  
Normalizar: $\|\mathbf{v}\|=1 \Rightarrow v_2 = 1/\sqrt{1+1.281^2} \approx 0.615$, $v_1 \approx 0.788$.

$$
\boxed{\mathbf{v}_1 \approx (0.788,\; 0.615)^\top}
$$

Para $\lambda_2$: $\mathbf{v}_2 = (-0.615,\; 0.788)^\top$ (ortogonal a $\mathbf{v}_1$).

**c) Varianza explicada**:

$$
\text{VE}_1 = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{5.561}{7} \approx \boxed{79.4\%}
$$

---

### Ejercicio 2.2 — Criterio de Kaiser y scree plot

**Enunciado**: Un dataset con 6 variables tiene autovalores (sobre la matriz de correlación): $\lambda = (2.8,\; 1.5,\; 0.9,\; 0.4,\; 0.2,\; 0.1)$.

a) ¿Cuántas componentes retiene el criterio de Kaiser?  
b) ¿Cuántas componentes se necesitan para explicar al menos el 85% de la varianza?  
c) Trace el scree plot y señale el "codo".

**Resolución**:

**a) Kaiser**: retener $\lambda_k > 1$. Los autovalores 2.8 y 1.5 superan 1 → **retener 2 componentes**.

**b) Varianza total** = $2.8+1.5+0.9+0.4+0.2+0.1 = 6.0$ (siempre 6 sobre $\mathbf{R}$).

| CP  | $\lambda_k$ | VEA       |
| --- | ----------- | --------- |
| 1   | 2.8         | 46.7%     |
| 2   | 1.5         | 71.7%     |
| 3   | 0.9         | 86.7% ← ✔ |
| 4   | 0.4         | 93.3%     |

Para ≥85%: **3 componentes**.

**c) Scree plot**:

```
λ
2.8 │•
1.5 │  •
0.9 │    •
0.4 │      •
0.2 │        •
0.1 │          •
    └──────────────  CP
    1  2  3  4  5  6
```

El "codo" está entre CP2 y CP3 (la pendiente se aplana notoriamente). Consistente con Kaiser (k=2) o con el criterio de varianza (k=3 para 85%).

---

### Ejercicio 2.3 — Interpretación de biplot

**Enunciado**: En un biplot de las dos primeras componentes, la flecha de la variable "radio medio" apunta casi en la dirección de PC1 con magnitud alta, mientras que "simetría" forma un ángulo cercano a 90° con "radio medio". ¿Qué concluye?

**Resolución**:

- "Radio medio" **define** la PC1 (alto loading en PC1, bajo en PC2).
- Un ángulo de ~90° entre "radio medio" y "simetría" indica **baja correlación** entre estas variables en los datos originales.
- Las flechas largas indican variables bien representadas (alta comunalidad) en el plano PC1-PC2.

---

## Unidad 3 — Reglas de Asociación

### Ejercicio 3.1 — Cálculo de métricas

**Enunciado**: Dada la base con 6 transacciones:

| TID | Ítems                   |
| --- | ----------------------- |
| 1   | leche, pan, huevo       |
| 2   | leche, mantequilla      |
| 3   | pan, mantequilla        |
| 4   | leche, pan, mantequilla |
| 5   | leche, pan              |
| 6   | pan, huevo              |

Calcule soporte, confianza, lift y conviction para la regla $\{pan\} \Rightarrow \{leche\}$.

**Resolución**:

- $s(\{pan\}) = 5/6$ (TIDs 1,3,4,5,6)
- $s(\{leche\}) = 4/6$ (TIDs 1,2,4,5)
- $s(\{pan, leche\}) = 3/6$ (TIDs 1,4,5)

$$
\text{soporte} = 3/6 = \boxed{0.50}
$$

$$
\text{confianza} = \frac{s(\{pan,leche\})}{s(\{pan\})} = \frac{3/6}{5/6} = \frac{3}{5} = \boxed{0.60}
$$

$$
\text{lift} = \frac{c(\{pan\}\Rightarrow\{leche\})}{s(\{leche\})} = \frac{0.60}{4/6} = \frac{0.60}{0.667} = \boxed{0.90}
$$

$$
\text{conviction} = \frac{1 - s(\{leche\})}{1 - c} = \frac{1 - 0.667}{1 - 0.60} = \frac{0.333}{0.40} = \boxed{0.833}
$$

**Interpretación**: lift < 1 → la presencia de pan _reduce_ ligeramente la probabilidad de leche. La regla no es informativamente útil a pesar de su confianza del 60%.

---

### Ejercicio 3.2 — Apriori paso a paso

**Enunciado**: Con el dataset del Ejercicio 3.1 y $s_{\min}=0.50$, ejecute el algoritmo Apriori para encontrar todos los itemsets frecuentes.

**Resolución**:

**$L_1$** (soporte ≥ 0.50 = 3/6):

| Itemset       | Soporte       |
| ------------- | ------------- |
| {leche}       | 4/6 = 0.667 ✔ |
| {pan}         | 5/6 = 0.833 ✔ |
| {huevo}       | 2/6 = 0.333 ✗ |
| {mantequilla} | 3/6 = 0.500 ✔ |

$L_1 = \{\{leche\},\{pan\},\{mantequilla\}\}$

**$C_2$** (por unión de pares de $L_1$):

| Itemset              | Soporte       |
| -------------------- | ------------- |
| {leche, pan}         | 3/6 = 0.500 ✔ |
| {leche, mantequilla} | 2/6 = 0.333 ✗ |
| {pan, mantequilla}   | 2/6 = 0.333 ✗ |

$L_2 = \{\{leche, pan\}\}$

**$C_3$**: ningún candidato válido ($L_2$ tiene solo un elemento de tamaño 2).

**Itemsets frecuentes totales**: $\{\{leche\},\{pan\},\{mantequilla\},\{leche,pan\}\}$

---

### Ejercicio 3.3 — Propiedad anti-monotónica

**Enunciado**: Explique por qué si $\{A, B, C\}$ es infrecuente con $s_{\min}=0.20$, ningún superconjunto de $\{A,B,C\}$ puede ser frecuente.

**Resolución**:

Por la propiedad de anti-monotonicidad del soporte: para cualquier $S' \supseteq S$:

$$
s(S') \le s(S)
$$

_Demostración_: toda transacción que contiene $S' \supseteq S$ también contiene $S$, pero no viceversa. Por tanto $|\{T : S' \subseteq T\}| \le |\{T : S \subseteq T\}|$ y al dividir por $|\mathcal{D}|$, $s(S') \le s(S)$.

Si $s(\{A,B,C\}) < s_{\min}$, entonces para cualquier $S' \supset \{A,B,C\}$ se tiene $s(S') \le s(\{A,B,C\}) < s_{\min}$. Todos los superconjuntos son **infrecuentes** → Apriori los **poda** sin siquiera contarlos.

---

## Unidad 4 — Clustering

### Ejercicio 4.1 — Clustering jerárquico manual

**Enunciado**: Dado el conjunto de puntos en $\mathbb{R}^2$:
$P_1(1,1)$, $P_2(2,1)$, $P_3(4,3)$, $P_4(5,4)$, $P_5(5,5)$.

Use **linkage completo** con distancia euclidiana para construir el dendrograma paso a paso. Indique el corte que da 2 clusters.

**Resolución**:

**Matriz de distancias iniciales** (Euclideana, valores redondeados):

|       | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ |
| ----- | ----- | ----- | ----- | ----- | ----- |
| $P_1$ | —     | 1.00  | 3.61  | 5.00  | 5.66  |
| $P_2$ | —     | —     | 2.83  | 4.24  | 5.00  |
| $P_3$ | —     | —     | —     | 1.41  | 2.24  |
| $P_4$ | —     | —     | —     | —     | 1.00  |
| $P_5$ | —     | —     | —     | —     | —     |

**Paso 1**: mínima distancia → $d(P_1,P_2)=1.00$ ó $d(P_4,P_5)=1.00$ (empate). Unir $\{P_4,P_5\}$ a altura 1.00.

Actualizar con **complete linkage**:
$d(\{P_4,P_5\}, P_3) = \max(1.41, 2.24) = 2.24$, $d(\{P_4,P_5\}, P_2) = \max(4.24, 5.00) = 5.00$, $d(\{P_4,P_5\}, P_1) = \max(5.00, 5.66) = 5.66$.

**Paso 2**: mínima → $d(P_1,P_2)=1.00$. Unir $\{P_1,P_2\}$ a altura 1.00.

Actualizar: $d(\{P_1,P_2\}, P_3) = \max(3.61,2.83)=3.61$, $d(\{P_1,P_2\},\{P_4,P_5\}) = \max(5.00,5.66)=5.66$.

**Paso 3**: mínima → $d(\{P_4,P_5\},P_3)=2.24$. Unir $\{P_3,P_4,P_5\}$ a altura 2.24.

**Paso 4**: unir $\{P_1,P_2\}$ con $\{P_3,P_4,P_5\}$ a altura 5.66.

**Dendrograma**:

```
altura
5.66 ──────────────────────────────
2.24       ┌──────────────
1.00  ┌──  │        ┌──
      P1 P2 P3      P4 P5
```

**Corte a altura 3**: 2 clusters → $\{P_1,P_2\}$ y $\{P_3,P_4,P_5\}$.

---

### Ejercicio 4.2 — k-means paso a paso

**Enunciado**: Con los puntos $A(1,1)$, $B(2,3)$, $C(4,2)$, $D(5,4)$, $E(1,4)$, $k=2$, centroides iniciales $\mu_1=(1,1)$, $\mu_2=(5,4)$:

Ejecute **2 iteraciones** de k-means (distancia euclidiana).

**Resolución**:

**Iteración 1 — Asignación**:

| Punto  | $d(\cdot,\mu_1)$ | $d(\cdot,\mu_2)$ | Cluster |
| ------ | ---------------- | ---------------- | ------- |
| A(1,1) | 0.00             | 5.66             | 1       |
| B(2,3) | 2.24             | 3.61             | 1       |
| C(4,2) | 3.16             | 2.24             | 2       |
| D(5,4) | 5.66             | 0.00             | 2       |
| E(1,4) | 3.00             | 4.12             | 1       |

$C_1=\{A,B,E\}$, $C_2=\{C,D\}$

**Iteración 1 — Actualización**:

$$
\mu_1 = \left(\frac{1+2+1}{3}, \frac{1+3+4}{3}\right) = (1.33,\; 2.67)
$$

$$
\mu_2 = \left(\frac{4+5}{2}, \frac{2+4}{2}\right) = (4.50,\; 3.00)
$$

**Iteración 2 — Asignación**:

| Punto  | $d(\cdot,\mu_1)$ | $d(\cdot,\mu_2)$ | Cluster |
| ------ | ---------------- | ---------------- | ------- |
| A(1,1) | 1.75             | 4.03             | 1       |
| B(2,3) | 0.75             | 2.55             | 1       |
| C(4,2) | 2.75             | 1.12             | 2       |
| D(5,4) | 4.32             | 1.12             | 2       |
| E(1,4) | 1.53             | 3.54             | 1       |

Sin cambios → **converge**. Clusters finales: $\{A,B,E\}$ y $\{C,D\}$.

---

### Ejercicio 4.3 — Índice Silhouette

**Enunciado**: Con los clusters del Ejercicio 4.2, calcule el coeficiente Silhouette para el punto B(2,3).

**Resolución**:

$C_1=\{A(1,1), B(2,3), E(1,4)\}$, $C_2=\{C(4,2), D(5,4)\}$.

**$a(B)$** = distancia media de B a los otros puntos de $C_1$:

$$
a(B) = \frac{d(B,A) + d(B,E)}{2} = \frac{\sqrt{1+4} + \sqrt{1+1}}{2} = \frac{2.236 + 1.414}{2} = 1.825
$$

**$b(B)$** = distancia media de B al cluster vecino más cercano ($C_2$):

$$
b(B) = \frac{d(B,C) + d(B,D)}{2} = \frac{\sqrt{4+1} + \sqrt{9+1}}{2} = \frac{2.236 + 3.162}{2} = 2.699
$$

$$
s(B) = \frac{b(B) - a(B)}{\max\{a(B), b(B)\}} = \frac{2.699 - 1.825}{2.699} = \boxed{0.324}
$$

Interpretación: $s(B) \approx 0.32$ → el punto está razonablemente bien asignado a su cluster, pero sin una separación muy clara.

---

## Checklist final PEP 1

Asegúrate de poder responder de memoria:

- [ ] Las 5 etapas KDD con ejemplos.
- [ ] Diferencia dato / información / conocimiento / meta-conocimiento.
- [ ] OLTP vs OLAP (características técnicas).
- [ ] Derivar la ecuación de autovalores de PCA desde el problema variacional.
- [ ] Calcular autovalores de una $2\times2$ a mano.
- [ ] Criterio de Kaiser y varianza explicada.
- [ ] Definición formal de soporte, confianza, lift y conviction.
- [ ] Propiedad anti-monotónica y su impacto en Apriori.
- [ ] Ejecutar Apriori a mano (5–6 transacciones).
- [ ] Criterios de enlace (single/complete/average/Ward) y sus características.
- [ ] k-means: una iteración completa de asignación y actualización.
- [ ] Calcular Silhouette para un punto específico.
