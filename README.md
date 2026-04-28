# Inteligencia Computacional — Magíster USACH

Repositorio de estudio, análisis y proyectos del ramo **Inteligencia Computacional** del Magíster en Ingeniería de la **Universidad de Santiago de Chile (USACH)**. Profesor referente: **Max Chacón**; equipo: Gonzalo Acuña (NN), José (modelamiento), Mario (bioinformática).

> Documento base del curso: [`data/raw/Documentacion Oficial/introduccion.md`](data/raw/Documentacion%20Oficial/introduccion.md)
> Roadmap de estudio: [`documentation/aprendizaje/ROADMAP.md`](documentation/aprendizaje/ROADMAP.md)

## Propósito

- Centralizar **clases, libros, papers, ejercicios y datasets** del ramo.
- Procesar PDFs (clases del Prof. Chacón) a **Markdown + tablas + imágenes**.
- Resolver **PEP1, PEP2 y trabajo final**, además de **laboratorios L1–L5** (en parejas, mismo dataset todo el semestre).
- Mantener **memoria compartida** del agente "Profe Inteligencia Computacional" en `.copilot/memoria/`.

## Estructura

```
data-inteligencia/
├── .copilot/memoria/        # Memoria compartida (Git): inventario, conceptos, progreso
├── .github/
│   ├── copilot-instructions.md   # Contexto general del proyecto para Copilot
│   └── agents/profe-inteligencia.agent.md  # Agente tutor del curso
├── data/
│   ├── raw/
│   │   ├── Documentacion Oficial/   # introduccion.md (programa)
│   │   ├── clases/Presentaciones_Prof_Max/  # Capítulos I–VII oficiales
│   │   ├── clases/registro-clases/  # Registros y notas de clase
│   │   ├── apuntes/                 # Inferencia, ACP
│   │   ├── ayudantias/2026/         # Ayudantías 2026
│   │   ├── Ejercicios/              # Guías y PEPs anteriores
│   │   ├── Laboratorios/            # Material L1–L5
│   │   ├── Libros/                  # ⚠️ Bibliografía pesada (Bishop, Hastie, Han, Bonelli)
│   │   ├── papers/                  # Papers
│   │   ├── Presentaciones/          # Complementarias (ACP, DW, Series)
│   │   ├── Resumenes/               # Manuales
│   │   ├── Cursos/  Codigo/  datasets/  docs/  examenes/  Tareas/
│   ├── processed/                   # Salidas de pdf_extractor / book_explorer
│   └── exports/                     # Entregas
├── documentation/
│   ├── aprendizaje/                 # Guías de estudio + ROADMAP.md
│   ├── tareas/                      # Plantillas + tareas en progreso/resueltas
│   ├── resumen-clases/              # Resúmenes
│   ├── investigacion/               # Trabajo final (Unidades 8–10)
│   ├── proyectos/                   # Documentación de proyectos
│   └── reports/                     # Informes formales (laboratorios)
├── notebooks/
│   ├── ejercicios/  exploratory/  reports/
├── proyectos/                       # Código de proyectos integradores
├── scripts/
│   ├── analysis/  etl/
│   └── utils/
│       ├── pdf_extractor.py         # Extracción universal de PDFs
│       ├── book_explorer.py         # 🆕 Lectura eficiente de libros pesados
│       ├── task_manager.py          # Gestión de tareas/laboratorios
│       └── update_structure.py      # Sincroniza árbol en docs
├── tests/                           # Tests
├── README.md
└── requirements.txt
```

## Programa del Curso

10 unidades, 17 semanas (38h teoría + 16h laboratorio).

| Unidad | Tema                                   | Horas | Evaluación |
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

**Notas:**
$NT = (\text{PEP1} + \text{PEP2} + \text{Trabajo})/3$ &nbsp;|&nbsp; $NL = \overline{L1..L5}$ &nbsp;|&nbsp; $\text{Final} = 0.6\,NT + 0.4\,NL$

Aprobación: Final ≥ 4.0 y promedio (NT + NL) ≥ 5.0.

## Quick Start

```powershell
# Crear entorno virtual e instalar dependencias
python -m venv .venv
.\.venv\Scripts\Activate.ps1     # Windows PowerShell
pip install -r requirements.txt

# Lanzar JupyterLab
jupyter lab
```

## Flujo de Trabajo

### 1. Procesar capítulos del Prof. Chacón

```powershell
python scripts/utils/pdf_extractor.py "data/raw/clases/Presentaciones_Prof_Max" --format md --all
```

Genera `data/processed/<slug>/` con `texto.md`, `tables/*.csv`, `images/page*.png`, `info.json`.

### 2. Explorar libros pesados sin cargarlos completos

```powershell
# Resumen rápido (páginas, tamaño, ¿tiene TOC?)
python scripts/utils/book_explorer.py "data/raw/Libros/" --info

# Tabla de contenidos embebida
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --toc --save

# Primeras N páginas (portada, índice impreso)
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --first-pages 25 --save

# Búsqueda de un término (regex, página + snippet)
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --search "principal component" --save

# Outline completo (TOC + primeras líneas de cada sección)
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --outline-md --save
```

> ⚠️ **Nunca leer un libro completo** desde el agente. Usar siempre `book_explorer.py`.

### 3. Crear y resolver laboratorios

```powershell
python scripts/utils/task_manager.py create --type laboratorio --id L-01 --name "PCA sobre dataset biomédico"
python scripts/utils/task_manager.py list
```

Cada laboratorio sigue las **7 fases**: Contexto → Datos → Método → Implementación → Evaluación → Comparación → Conclusiones.

### 4. Sincronizar estructura en documentación

```powershell
python scripts/utils/update_structure.py
```

## Memoria del Agente

Versionada en Git en `.copilot/memoria/`:

- `inventario-material.md` — catálogo de material (clases, libros, ejercicios, papers).
- `conceptos-clave.md` — mapa de conceptos por unidad, fórmulas y relaciones.
- `progreso-estudiante.md` — temas vistos, dudas, laboratorios entregados, sesiones.

El agente **Profe Inteligencia Computacional** (`.github/agents/profe-inteligencia.agent.md`) lee y actualiza estos archivos en cada sesión significativa.

## Bibliografía Principal

Disponible en `data/raw/Libros/`:

- **Bishop** — _Pattern Recognition and Machine Learning_ (Springer, 2006)
- **Hastie, Tibshirani, Friedman** — _The Elements of Statistical Learning_ (Springer, 2ª ed., 2011)
- **Han, Kamber, Pei** — _Data Mining: Concepts and Techniques_ (3rd ed.)
- **Hernández, Ramírez, Ferri** — _Introducción a la Minería de Datos_ (Pearson, 2004)
- **Haykin** — _Neural Networks and Learning Machines_ (Prentice Hall, 3ª ed., 2008)
- **Suykens et al.** — _Artificial Neural Networks for Modelling and Control of Non-linear Systems_ (Kluwer, 2010)
- **Bonelli** — _Inteligencia Computacional_ (libro oficial, traducido)

## Licencia y uso

Repositorio personal/académico de estudio. No redistribuir libros sujetos a copyright.
