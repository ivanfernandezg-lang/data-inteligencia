# Unidad 1 — Introducción y Proceso KDD

> **Curso**: Inteligencia Computacional · USACH · Prof. Max Chacón
> **Fuente primaria**: [`data/processed/clases/Presentaciones_Prof_Max/capitulo-i-inteligencia-computacional_introducción/`](../../../data/processed/clases/Presentaciones_Prof_Max/capitulo-i-inteligencia-computacional_introducci%C3%B3n/capitulo-i-inteligencia-computacional_introducci%C3%B3n.md)
> **Complementario**: Han, J. — _Data Mining: Concepts and Techniques_, 3rd ed., Cap. 1.
> **Carga**: 3 h teoría · evalúa en **PEP 1**

---

## 1. Objetivos de aprendizaje

- Distinguir **dato → información → conocimiento → meta-conocimiento**.
- Identificar las etapas del proceso de descubrimiento de conocimiento en bases de datos (KDD).
- Diferenciar bases de datos **operacionales (OLTP)** vs **analíticas (OLAP / DW)**.
- Tipificar problemas de aprendizaje: **supervisado, no supervisado, semi-supervisado, por refuerzo**.
- Comparar modelos lineales (regresión) con aprendizaje no lineal.

---

## 2. Definiciones fundamentales

| Concepto              | Definición operacional (Chacón, Cap. I)                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dato**              | Hecho o medida que describe una característica de un objeto/evento.                                                                                                             |
| **Información**       | Datos procesados y presentados en forma útil para un observador.                                                                                                                |
| **Conocimiento**      | Información procesada que permite emitir juicios y conclusiones.                                                                                                                |
| **Meta-conocimiento** | Reglas que permiten obtener conocimiento.                                                                                                                                       |
| **Minería de Datos**  | Conjunto de técnicas para extraer información/conocimiento desde BBDD.                                                                                                          |
| **KDD**               | Proceso _no trivial_ de identificación de patrones válidos, novedosos, potencialmente útiles y comprensibles a partir de los datos (Frawley et al., 1989; Fayyad et al., 1996). |

> **Pirámide informacional**: Datos → Información → Conocimiento → Meta-conocimiento. Reducción en cantidad, aumento en valor.

---

## 3. El proceso KDD (Fayyad, 1996)

```
Datos brutos → Selección → Pre-procesamiento → Transformación → Minería de Datos → Evaluación/Interpretación → Conocimiento
                  ↑__________________________ retroalimentación __________________________|
```

### Etapas detalladas

1. **Selección**: identificar el subconjunto de datos relevantes (filas y columnas).
2. **Pre-procesamiento**: limpieza, manejo de faltantes, ruido, outliers, integración de fuentes.
3. **Transformación**: normalización, discretización, reducción de dimensionalidad (p.ej. PCA), generación de nuevas variables.
4. **Minería de Datos**: aplicación del algoritmo (clasificación, regresión, clustering, reglas de asociación, etc.).
5. **Evaluación / Interpretación**: métricas de calidad, validación estadística, visualización, traducción a conocimiento accionable.

> **Nota**: KDD es **iterativo**. La retroalimentación entre etapas es la regla, no la excepción.

---

## 4. Tipología de problemas

### 4.1 Por tipo de supervisión

| Tipo                 | Etiqueta `y` | Ejemplo                                 | Métodos clásicos                 |
| -------------------- | ------------ | --------------------------------------- | -------------------------------- |
| **Supervisado**      | Sí           | Diagnóstico (benigno/maligno)           | Bayes, árboles, MLP, SVM         |
| **No supervisado**   | No           | Segmentación de pacientes               | k-means, jerárquico, DBSCAN, PCA |
| **Semi-supervisado** | Parcial      | Pocas etiquetas + muchos no-etiquetados | Self-training, label propagation |
| **Refuerzo**         | Recompensa   | Control de glucosa, robótica            | Q-learning, policy gradient      |

### 4.2 Por tarea

- **Predictivas**: clasificación (categórica), regresión (numérica), pronóstico de series temporales.
- **Descriptivas**: agrupamiento, reglas de asociación, detección de anomalías, resumen.

---

## 5. OLTP vs OLAP

| Característica      | OLTP (operacional)    | OLAP / Data Warehouse    |
| ------------------- | --------------------- | ------------------------ |
| Propósito           | Transacciones diarias | Análisis y decisión      |
| Diseño              | Normalizado (3FN)     | Estrella / copo de nieve |
| Operación dominante | INSERT / UPDATE       | SELECT agregadas         |
| Latencia            | ms                    | s a min                  |
| Volumen             | GB                    | TB–PB                    |
| Historial           | Reciente              | Histórico amplio         |

---

## 6. Comparación con regresión lineal clásica

La regresión lineal asume:

$$
y = \beta_0 + \sum_{j=1}^{p} \beta_j x_j + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2)
$$

con linealidad, homocedasticidad, independencia y normalidad del error. Los métodos de **aprendizaje no lineal** (árboles, MLP, RBF, SVM-kernel) **relajan** estos supuestos a costa de mayor complejidad, riesgo de sobreajuste y menor interpretabilidad.

| Criterio              | Regresión lineal | Aprendizaje no lineal |
| --------------------- | ---------------- | --------------------- |
| Interpretabilidad     | Alta             | Variable a baja       |
| Hipótesis sobre datos | Fuertes          | Débiles               |
| Capacidad de modelar  | Limitada         | Alta                  |
| Riesgo overfitting    | Bajo             | Alto                  |
| Datos requeridos      | Pocos            | Muchos                |

---

## 7. Hipótesis comunes en aprendizaje

- **i.i.d.**: muestras independientes e idénticamente distribuidas.
- **Estacionariedad**: la distribución generadora no cambia entre entrenamiento y prueba.
- **Representatividad**: la muestra refleja la población objetivo.
- **No-redundancia / mínima colinealidad** entre atributos (importante para regresión lineal y PCA).

Violaciones típicas en bioinformática: _covariate shift_, _class imbalance_, datos longitudinales no independientes.

---

## 8. Ejemplo guiado: pipeline KDD mínimo

> Notebook: [00_intro_kdd.ipynb](../../../notebooks/exploratory/00_intro_kdd.ipynb)

Dataset: **Wisconsin Breast Cancer** (`sklearn.datasets.load_breast_cancer`).

Etapas:

1. **Selección**: 30 atributos numéricos, 569 instancias, 2 clases (M/B).
2. **Pre-procesamiento**: `StandardScaler` (media 0, varianza 1).
3. **Transformación**: PCA a 2 componentes (anticipo de Unidad 2).
4. **Minería**: regresión logística como baseline.
5. **Evaluación**: accuracy, matriz de confusión, ROC.

---

## 9. Conceptos clave para PEP 1

- KDD ≠ Data Mining: KDD es el **proceso completo**; DM es **una etapa**.
- Las etapas del KDD se preguntan en orden y con sus objetivos.
- Diferencia precisa OLTP/OLAP.
- Pirámide informacional (de menor a mayor abstracción y de mayor a menor cantidad).
- La definición formal de Fayyad (1996) suele preguntarse textual.

---

## 10. Lecturas y referencias

- Capítulo I, Prof. Chacón — base obligatoria.
- Han, Kamber, Pei — _Data Mining_, Cap. 1 (búsqueda con `book_explorer.py "data/raw/Libros/Data Mining*.pdf" --search "knowledge discovery"`).
- Fayyad, U.; Piatetsky-Shapiro, G.; Smyth, P. (1996). _From Data Mining to Knowledge Discovery in Databases_. AI Magazine, 17(3).
