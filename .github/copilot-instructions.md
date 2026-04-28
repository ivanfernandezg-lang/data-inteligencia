# Copilot Instructions — Inteligencia Computacional (USACH)

## Contexto del Proyecto

Repositorio de estudio del ramo **Inteligencia Computacional** del Magíster en Ingeniería de la **Universidad de Santiago de Chile (USACH)**. Profesor referente: **Max Chacón** (USACH); equipo docente complementario: Gonzalo Acuña (redes neuronales), José (modelamiento), Mario (bioinformática).

El proyecto sigue un flujo completo: extracción de PDFs y libros → procesamiento a Markdown/CSV/imágenes → documentación estructurada → laboratorios y trabajos resueltos → notebooks interactivos.

> Documento base del curso: [`data/raw/Documentacion Oficial/introduccion.md`](../data/raw/Documentacion%20Oficial/introduccion.md).

## Idioma

- **Siempre responder en español** (español chileno académico).
- Usar terminología técnica en español, con el equivalente en inglés entre paréntesis cuando sea relevante. Ejemplo: "análisis de componentes principales (PCA)", "retro-propagación del error (backpropagation)".
- Los nombres de variables en código pueden estar en inglés o español según el contexto.

## Temas del Curso (10 unidades, 17 semanas)

| Unidad | Título                                 | Horas | Evaluación |
| ------ | -------------------------------------- | ----- | ---------- |
| 1      | Introducción                           | 3     | PEP 1      |
| 2      | Análisis de Componentes Principales    | 3     | PEP 1      |
| 3      | Reglas de asociación                   | 4     | PEP 1      |
| 4      | Análisis de agrupamientos              | 4     | PEP 1      |
| 5      | Evaluación Estadística                 | 2     | PEP 2      |
| 6      | Clasificación Bayesiana                | 5     | PEP 2      |
| 7      | Árboles de decisión                    | 5     | PEP 2      |
| 8      | El paradigma Conexionista              | 2     | Trabajo    |
| 9      | Retro-propagación del Error            | 4     | Trabajo    |
| 10     | Redes neuronales con retroalimentación | 6     | Trabajo    |

**Distribución de evaluación:**

- **PEP 1** (escrita, lápiz y papel): Unidades 1–4
- **PEP 2** (escrita, lápiz y papel): Unidades 5–7
- **Trabajo final** (revisión bibliográfica + presentación oral + informe): Unidades 8–10
- **Laboratorios L1–L5** (en parejas, R o Python, mismo problema todo el semestre)

**Fórmulas:**

- $NT = (\text{PEP1} + \text{PEP2} + \text{Trabajo}) / 3$
- $NL = \text{promedio}(L1, \ldots, L5)$
- $\text{Final} = 0.6 \cdot NT + 0.4 \cdot NL$
- Aprobación: Final ≥ 4.0 y promedio acumulado (NT + NL) ≥ 5.0

## Estructura del Proyecto

```
data/
├── raw/
│   ├── Documentacion Oficial/  # Documento base del curso (introduccion.md)
│   ├── clases/
│   │   ├── Presentaciones_Prof_Max/  # Capítulos I–VII oficiales del Prof. Chacón
│   │   └── registro-clases/          # Registros y notas de clase
│   ├── apuntes/                # Apuntes de inferencia, ACP, etc.
│   ├── ayudantias/2026/        # Material de ayudantías
│   ├── Cursos/                 # Material externo de cursos relacionados
│   ├── Ejercicios/             # Guías de ejercicios y PEPs anteriores
│   ├── examenes/               # Pruebas/exámenes anteriores
│   ├── Laboratorios/           # Material de laboratorios L1–L5
│   ├── Libros/                 # ⚠️ Bibliografía pesada (Bishop, Hastie, Han, Bonelli, etc.)
│   ├── papers/                 # Papers y artículos
│   ├── Presentaciones/         # Presentaciones complementarias (ACP, DW, Series)
│   ├── Resumenes/              # Resúmenes y manuales
│   ├── Tareas/                 # Tareas asignadas
│   ├── Codigo/                 # Código de referencia
│   └── datasets/               # Datasets para laboratorios
├── processed/                  # Contenido extraído (MD, CSV, PNG, info.json)
└── exports/                    # Archivos para entregas

.copilot/memoria/               # Memoria compartida del agente (versionada en Git)
├── progreso-estudiante.md
├── conceptos-clave.md
└── inventario-material.md

documentation/
├── aprendizaje/                # Guías de estudio y ejercicios resueltos
├── tareas/                     # Sistema de tareas (plantillas, en-progreso, resueltas)
├── resumen-clases/             # Resúmenes por clase
├── investigacion/              # Investigación bibliográfica para trabajo final
├── proyectos/                  # Documentación de proyectos
└── reports/                    # Informes formales (laboratorios)

notebooks/
├── ejercicios/                 # Notebooks de ejercicios y PCA, clustering, NN
├── exploratory/                # Análisis exploratorio (EDA) de datasets
└── reports/                    # Notebooks de entrega de laboratorios

scripts/utils/
├── pdf_extractor.py            # Extracción universal de PDFs (texto/tablas/imágenes/OCR)
├── book_explorer.py            # 🆕 Lectura eficiente de libros pesados (índice, primeras pgs)
├── task_manager.py             # Gestión de tareas/laboratorios
└── update_structure.py         # Sincronización de estructura

proyectos/                      # Código de proyectos integradores
tests/                          # Tests de validación
```

## Stack Tecnológico

- **Python 3.10+** (también se acepta R en laboratorios)
- **Machine Learning**: scikit-learn, xgboost
- **Redes neuronales**: tensorflow / keras, pytorch
- **Reglas de asociación**: mlxtend (apriori, fp-growth)
- **Clustering**: scikit-learn, scipy.cluster
- **Estadística**: scipy.stats, statsmodels, pingouin
- **Científico**: numpy, scipy, pandas, sympy
- **Visualización**: matplotlib, seaborn, plotly
- **Notebooks**: JupyterLab
- **PDF**: PyMuPDF (pymupdf)

## Convenciones de Código

- Scripts en `scripts/` con docstrings en español
- Type hints en funciones
- Notebooks con celdas Markdown explicativas entre código
- Ecuaciones LaTeX (KaTeX): inline con `$...$`, bloques con `$$...$$`
- Tablas en CSV dentro de `tables/`
- Imágenes nombradas como `pageXXX_imgXX.png`
- Datasets compartidos para laboratorios deben quedar en `data/raw/datasets/<nombre>/`

## Sistema de Tareas y Laboratorios (7 Fases)

Cada tarea o laboratorio sigue este flujo:

| Fase              | Contenido                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------- |
| 1. Contexto       | Problema, dominio (idealmente biomédico), variables, objetivo de aprendizaje             |
| 2. Datos          | Origen, EDA, preprocesamiento, normalización, partición train/test/val                   |
| 3. Método         | Selección y justificación del método (PCA, k-means, Bayes, árboles, MLP, RBF, RNN, etc.) |
| 4. Implementación | Código Python (o R) con visualizaciones reproducibles                                    |
| 5. Evaluación     | Métricas, validación cruzada, significancia estadística                                  |
| 6. Comparación    | Contraste con otros métodos vistos en clase aplicados al mismo problema                  |
| 7. Conclusiones   | Lecciones aprendidas, limitaciones, trabajo futuro                                       |

## Tipos de Trabajo

- **laboratorio** (8–12 h): L1–L5 obligatorios, en parejas, mismo dataset durante el semestre
- **ejercicio-clase** (1–3 h): Ejercicios cortos para PEP1/PEP2
- **investigacion** (10–20 h): Revisión bibliográfica para trabajo final (Unidades 8–10)
- **proyecto** (20–40 h): Proyectos integradores

## Herramientas Disponibles

```powershell
# Extraer PDFs (texto + tablas + imágenes)
python scripts/utils/pdf_extractor.py "data/raw/clases/Presentaciones_Prof_Max" --format md --all

# Explorar libros pesados sin cargarlos completos (índice, primeras páginas, búsqueda)
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --toc
python scripts/utils/book_explorer.py "data/raw/Libros/" --first-pages 15

# Gestionar tareas y laboratorios
python scripts/utils/task_manager.py create --type laboratorio --id L-01 --name "PCA sobre dataset X"
python scripts/utils/task_manager.py list

# Sincronizar estructura en docs
python scripts/utils/update_structure.py
```

## Cómo Ayudar

1. **Explicar conceptos**: Usar primero el material procesado en `data/processed/` y los capítulos del Prof. Chacón (`data/raw/clases/Presentaciones_Prof_Max/`) como fuente primaria
2. **Bibliografía**: Para profundizar usar Bishop (Pattern Recognition), Hastie (Elements of Statistical Learning), Han (Data Mining), Haykin (Neural Networks). **Siempre con `book_explorer.py` para evitar cargar libros completos**.
3. **Resolver laboratorios**: Seguir las 7 fases, comparar métodos sobre el mismo dataset
4. **Generar notebooks**: Con celdas explicativas, visualizaciones, métricas y código reproducible
5. **Validación estadística**: Usar tests apropiados (t-test, ANOVA, McNemar, validación cruzada k-fold)
6. **Formato matemático**: LaTeX para ecuaciones, matrices y derivaciones (especialmente en backpropagation y PCA)

## Restricciones Importantes

- ⚠️ **NUNCA cargar libros enteros de `data/raw/Libros/`** — usar `book_explorer.py` (índice, primeras páginas, búsqueda por término).
- NO inventar contenido que no esté en las clases sin marcarlo explícitamente.
- NO simplificar excesivamente — el nivel es de magíster.
- SIEMPRE referenciar la clase, capítulo o libro fuente cuando uses material del curso.
