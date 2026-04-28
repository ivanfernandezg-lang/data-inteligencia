# Scripts — Utilidades

Funciones y herramientas reutilizables del proyecto **Inteligencia Computacional** (USACH).

## Scripts

### `pdf_extractor.py`

Extracción universal de PDFs (texto, tablas, imágenes, OCR). Salida en `data/processed/<slug>/`.

```powershell
python scripts/utils/pdf_extractor.py "data/raw/clases/Presentaciones_Prof_Max" --format md --all
```

### `book_explorer.py` 🆕

Explorador eficiente de **libros pesados** (`data/raw/Libros/`) sin cargarlos completos.
Modos: `--info`, `--toc`, `--first-pages N`, `--pages a-b`, `--search "term"`, `--outline-md`.

```powershell
python scripts/utils/book_explorer.py "data/raw/Libros/" --info
python scripts/utils/book_explorer.py "data/raw/Libros/Pattern-Recognition-and-Machine-Learning-Bishop.pdf" --toc --save
python scripts/utils/book_explorer.py "data/raw/Libros/<libro>.pdf" --search "backpropagation" --save
python scripts/utils/book_explorer.py "data/raw/Libros/<libro>.pdf" --outline-md --save
```

> ⚠️ Usar SIEMPRE este script en vez de `read_file` o `pdf_extractor.py` para libros pesados (Bishop, Hastie, Han, Haykin, etc.).

### `task_manager.py`

Gestión de tareas y laboratorios L1–L5 con las 7 fases.

```powershell
python scripts/utils/task_manager.py create --type laboratorio --id L-01 --name "PCA biomédico"
python scripts/utils/task_manager.py list
```

### `update_structure.py`

Sincroniza el árbol de carpetas en `README.md`, `documentation/README.md` y `.github/copilot-instructions.md`.

```powershell
python scripts/utils/update_structure.py
```

## Salidas estandarizadas

- Procesado de PDFs: `data/processed/<slug>/{texto.md, tables/*.csv, images/*.png, info.json}`
- Outlines de libros: `data/processed/libros/<slug>/{info.json, toc.md, first-N.md, search-<term>.md, outline.md}`
