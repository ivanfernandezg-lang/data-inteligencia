# 🛠️ Scripts de Utilidad — Guía Rápida

> Referencia rápida para los scripts de `scripts/utils/`
> Ejecutar siempre desde la **raíz del proyecto** (`Optimizacion Ingenieria/`)

---

## ⚡ Setup inicial (solo la primera vez)

```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno
source .venv/bin/activate        # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt
```

> **Cada vez que abras una terminal nueva**, activa el entorno con `source .venv/bin/activate`

---

## 📄 pdf_extractor.py — Extractor de PDFs

Extrae **texto, tablas e imágenes** de cualquier PDF. Soporta PDFs nativos (PowerPoint/Word exportados) y escaneados (OCR).

### Comandos

| Qué quiero hacer                             | Comando                                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Ver info** de todos los PDFs               | `python scripts/utils/pdf_extractor.py data/raw/clases/ --info`                       |
| **Extraer texto** de un PDF                  | `python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf`                   |
| **Extraer todo** (texto + tablas + imágenes) | `python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --all`             |
| **Exportar a Markdown**                      | `python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --format md`       |
| **Extraer todo en Markdown**                 | `python scripts/utils/pdf_extractor.py data/raw/clases/archivo.pdf --format md --all` |
| **Procesar TODOS los PDFs** de una carpeta   | `python scripts/utils/pdf_extractor.py data/raw/clases/ --format md --all`            |
| **PDF escaneado** (con OCR)                  | `python scripts/utils/pdf_extractor.py data/raw/papers/scan.pdf --ocr`                |
| **Elegir carpeta de salida**                 | `python scripts/utils/pdf_extractor.py archivo.pdf -o mi-carpeta/`                    |

### Flags disponibles

| Flag           | Corto    | Qué hace                                   |
| -------------- | -------- | ------------------------------------------ |
| `--info`       |          | Solo muestra info del PDF (no extrae nada) |
| `--format md`  | `-f md`  | Exporta a Markdown (default: txt)          |
| `--tables`     | `-t`     | Extrae tablas a CSV                        |
| `--images`     | `-i`     | Extrae imágenes a PNG                      |
| `--all`        | `-a`     | Activa `--tables` + `--images`             |
| `--ocr`        |          | Usa OCR para PDFs escaneados               |
| `--output DIR` | `-o DIR` | Cambia carpeta de salida                   |

### ¿Dónde queda la salida?

Por defecto en `data/processed/{nombre-pdf}/`:

```
data/processed/1-introduccion/
├── 1-introduccion.md        ← Texto completo
├── info.json                ← Metadata del PDF
├── tables/                  ← Tablas en CSV
│   ├── page002_table01.csv
│   └── page003_table01.csv
└── images/                  ← Imágenes extraídas
    ├── page001_img01.png
    └── page002_img01.png
```

### Ejemplos prácticos

```bash
# 🔍 "¿Qué tipo de contenido tienen mis PDFs de clase?"
python scripts/utils/pdf_extractor.py data/raw/clases/ --info

# 📝 Extraer la clase de optimización convexa a Markdown
python scripts/utils/pdf_extractor.py "data/raw/clases/4. Optimización convexa.pdf" --format md --all

# 📚 Extraer TODAS las clases de una vez
python scripts/utils/pdf_extractor.py data/raw/clases/ --format md --all

# 📄 Extraer un paper descargado (con OCR por si es escaneado)
python scripts/utils/pdf_extractor.py data/raw/papers/paper.pdf --format md --ocr --all

# 💾 Guardar en una carpeta específica
python scripts/utils/pdf_extractor.py data/raw/clases/ --format md --all -o data/exports/clases-md/
```

---

## 🔄 update_structure.py — Actualizador de documentación

Regenera automáticamente las secciones de **estructura de carpetas** en 3 archivos:

| Archivo                           | Qué actualiza                                                      |
| --------------------------------- | ------------------------------------------------------------------ |
| `.github/copilot-instructions.md` | Sección "ESTRUCTURA DEL PROYECTO" (con conteo de archivos)         |
| `README.md`                       | Sección "Estructura del proyecto" (árbol visual) + tabla de clases |
| `documentation/README.md`         | Sección "Estructura de Documentación"                              |

### Comandos

| Qué quiero hacer                       | Comando                                              |
| -------------------------------------- | ---------------------------------------------------- |
| **Ver qué cambiaría** (sin tocar nada) | `python scripts/utils/update_structure.py --dry-run` |
| **Aplicar cambios**                    | `python scripts/utils/update_structure.py`           |

### ¿Cuándo ejecutarlo?

Cada vez que:

- ✅ Agregues una **carpeta nueva** (ej: nuevo proyecto, nueva sección de documentación)
- ✅ Subas **nuevos PDFs** de clase
- ✅ Crees un nuevo **proyecto** en `proyectos/`
- ✅ Añadas **notebooks** o **scripts**

### ¿Qué pasa si agrego una carpeta que no conoce?

El script la **detecta y te avisa**:

```
⚠️  Carpetas nuevas detectadas sin descripción:
   → notebooks/simulaciones/
   💡 Agrégalas en FOLDER_DESCRIPTIONS en update_structure.py
```

Para registrarla, edita el diccionario `FOLDER_DESCRIPTIONS` al inicio de `update_structure.py`:

```python
FOLDER_DESCRIPTIONS: dict[str, str] = {
    ...
    "notebooks/simulaciones": "Notebooks de simulación Monte Carlo",  # ← agregar aquí
}
```

Y vuelve a ejecutar `python scripts/utils/update_structure.py`.

---

## 🔁 Flujo típico de trabajo

```
1. Descargar PDF nuevo       → guardarlo en data/raw/clases/ (o papers/)
2. Extraer contenido         → python scripts/utils/pdf_extractor.py data/raw/clases/ --format md --all
3. Actualizar documentación  → python scripts/utils/update_structure.py
4. Trabajar con el contenido → abrir el .md generado en data/processed/
```
