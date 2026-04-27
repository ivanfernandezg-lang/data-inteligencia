# Inteligencia Computacional

Repositorio de estudio, análisis y proyectos del ramo \*\*\*\* — Magíster USACH.

## Estructura del proyecto

```
data-inteligencia/
├── .copilot
│   └── memoria/
├── .github/
│   ├── agents/
│   └── copilot-instructions.md
├── .vscode/
│   └── settings.json
├── data/
│   ├── exports/  # Datos para reportes o entregas
│   ├── processed/  # Datos procesados
│   └── raw/
│       ├── clases/  # PDFs de presentaciones de clase
│       ├── datasets/  # Datasets para ejercicios y proyectos
│       ├── docs/  # Fuentes de información y links
│       └── papers/  # Papers y artículos de referencia
├── documentation/
│   ├── investigacion/  # Investigación bibliográfica
│   │   ├── md/
│   │   └── mmd/
│   ├── proyectos/  # Documentación por proyecto
│   │   ├── md/
│   │   └── mmd/
│   ├── reports/  # Informes y entregas
│   │   └── md/
│   ├── resumen-clases/  # Resúmenes por clase
│   │   └── md/
│   └── README.md
├── notebooks/
│   ├── ejercicios/  # Ejercicios resueltos
│   │   └── README.md
│   ├── exploratory/  # EDA y análisis exploratorio
│   │   └── README.md
│   └── reports/  # Notebooks de entrega
│       └── README.md
├── proyectos/  # Código de proyectos y trabajos
│   └── README.md
├── scripts/
│   ├── analysis/  # Scripts de análisis y modelos
│   │   └── README.md
│   ├── etl/  # Procesamiento de datos
│   │   └── README.md
│   └── utils/  # Funciones reutilizables
│       ├── MANUAL_RAPIDO.md
│       ├── pdf_extractor.py
│       ├── README.md
│       └── update_structure.py
├── tests/  # Tests de validación
│   └── README.md
├── .gitignore
├── README.md
└── requirements.txt
```

## Descripción de carpetas

### `data/`

Almacena datos en distintas etapas:

- **raw/clases**: PDFs y presentaciones originales de clase.
- **raw/papers**: Artículos científicos y papers de referencia.
- **raw/datasets**: Datasets descargados para ejercicios o proyectos.
- **raw/docs**: Fuentes de información, links y referencias web.
- **processed**: Datos limpios, normalizados y listos para análisis.
- **exports**: Archivos generados para entregas, reportes o presentaciones.

### `notebooks/`

Jupyter Notebooks organizados por propósito:

- **exploratory**: Análisis exploratorio de datos, visualizaciones.
- **ejercicios**: Resolución de ejercicios y problemas de clase.
- **reports**: Notebooks finales pulidos para presentar o entregar.

### `scripts/`

Scripts de automatización y análisis:

- **analysis**: Scripts de optimización, modelos y análisis numérico.
- **utils**: Funciones reutilizables (helpers, formateo, etc.).
- **etl**: Procesamiento de datos (lectura, limpieza, transformación).

### `documentation/`

Documentación organizada por tema → tipo de archivo:

- **reports/**: Informes finales y entregas formales.
- **resumen-clases/**: Apuntes y resúmenes de cada clase.
- **investigacion/**: Revisión bibliográfica, estado del arte.
- **proyectos/**: Documentación técnica de cada proyecto.

> Convención: cada carpeta temática contiene `md/` (Markdown) y opcionalmente `mmd/` (diagramas Mermaid).

### `proyectos/`

Código fuente de trabajos y proyectos. Cada proyecto tiene su propia subcarpeta.

### `tests/`

Tests para validar funciones y scripts de análisis.

## Materiales de clase

Los PDFs de las presentaciones están en `data/raw/clases/`:

| #   | Archivo                                          | Tema                                       |
| --- | ------------------------------------------------ | ------------------------------------------ |
| 1   | `1- Introducción.pdf`                            | Introducción                               |
| 2   | `2 - Optimización.pdf`                           | Optimización                               |
| 3   | `3- Métodos para  optimización irrestricta.pdf`  | Métodos para optimización irrestricta      |
| 3   | `3- Optimización con restricciones.pdf`          | Optimización con restricciones             |
| 4   | `4. Optimización convexa.pdf`                    | Optimización convexa                       |
| 6   | `6- PNL metodos con restricciones.pdf`           | PNL metodos con restricciones              |
| 7   | `7- Optimización combinatorial.pdf`              | Optimización combinatorial                 |
| —   | `Optimizacion en Ingenieria Magister MI- MV.pdf` | Optimizacion en Ingenieria Magister MI- MV |
| —   | `Presentación curso.pdf`                         | Presentación curso                         |

## Quick Start

```bash
# Crear entorno virtual Python
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt

# Ejecutar notebooks
jupyter lab
```
