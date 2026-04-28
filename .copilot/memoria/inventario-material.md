# Inventario de Material — data/raw/

> Catálogo del material disponible para el ramo Inteligencia Computacional (Magíster USACH).
> Actualizado: 2026-04-27.

---

## 1. Documentación Oficial

- `data/raw/Documentacion Oficial/introduccion.md` — **documento base del curso**: programa, evaluaciones, bibliografía oficial, fórmulas de notas.

## 2. Capítulos Oficiales del Prof. Max Chacón

Ubicación: `data/raw/clases/Presentaciones_Prof_Max/`

| Cap | Archivo                                                | Unidad |
| --- | ------------------------------------------------------ | ------ |
| I   | Capitulo I Inteligencia Computacional_Introducción.pdf | 1      |
| II  | Capítulo II Inteligencia Computacional_ACP.pdf         | 2      |
| III | Capitulo III Inteligencia Computaional_RA.pdf          | 3      |
| IV  | Capitulo IV Inteligencia Computacional_AA.pdf          | 4      |
| V   | Capitulo V Inteligencia Computacional_AEstadiatico.pdf | 5      |
| VI  | Capítulo VI Inteligencia Computacional_CB.pdf          | 6      |
| VII | Capitulo VII Inteligencia Computacional_AD.pdf         | 7      |

> ⚠️ Faltan capítulos VIII, IX y X (paradigma conexionista, retro-propagación, RNN). Para esos temas usar Haykin, Bishop y Suykens.

## 3. Libros (⚠️ pesados — usar `book_explorer.py`)

Ubicación: `data/raw/Libros/`

| Sigla     | Archivo                                                                                     | Cobertura                        |
| --------- | ------------------------------------------------------------------------------------------- | -------------------------------- |
| Bishop    | Pattern-Recognition-and-Machine-Learning-Bishop.pdf                                         | PCA, Bayesian, NN, kernels       |
| Hastie 1  | The Elements of Statistical Learning - Trevor Hastie 1.pdf                                  | Aprendizaje supervisado          |
| Hastie 2  | The Elements of Statistical Learning - Trevor Hastie 2.pdf.pdf                              | Ensembles, no supervisado        |
| Han 1     | Data Mining - Concepts and Techniques [3rd ed.] ... 1.pdf                                   | Preprocesamiento, asociación     |
| Han 2     | Data Mining - Concepts and Techniques [3rd ed.] ... 2.pdf                                   | Clustering, clasificación        |
| Hernández | Introduccion-a-La-Mineria-de-Datos-Jose-Hernandez-Orallo... .pdf                            | Texto en español, intro          |
| Hernández | José Hernández Orallo... - Introducción a la minería de datos.-Pearson Educación (2004).pdf | Texto en español, intro (alt)    |
| IME       | Apuntes_completos_IME.pdf                                                                   | Apuntes generales                |
| Bonelli   | Inteligencia computacional/InteligenciaComputacional-Livro\*.pdf                            | Versión oficial (PT + traducida) |
| Bonelli   | Inteligencia Computaciona ltraducido/InteligenciaComputacional-Livro Official.pdf           | Traducción oficial al español    |

## 4. Apuntes y Guías

- `data/raw/apuntes/Apunte_Introducción_AD_01-2026.pdf` — Análisis de Datos, intro
- `data/raw/apuntes/INFERENCIA Y MODELOS ESTADÍSTICOS Jacqueline Köhler C.pdf` — Inferencia
- `data/raw/apuntes/analisis de componentes/` — apuntes de PCA
- `data/raw/Resumenes/manual completo de estadística.pdf` — Manual de estadística

## 5. Ejercicios y Pruebas Anteriores

Ubicación: `data/raw/Ejercicios/`

- `581580439-Guia-Ejercicios-Inteligencia-Computacional.pdf`
- `863697173-Analisis-de-Datos-Guia-4-v2025.pdf`
- `Guía - Análisis de Componentes Principales.pdf`
- `Guía - Análisis de Agrupamiento.pdf`
- `IC_Ejercicios_PEP1_20-04-2026.pdf` ← **prep PEP1 2026**

## 6. Presentaciones Complementarias

- `data/raw/Presentaciones/Análisis en Componentes Principales/`
- `data/raw/Presentaciones/Data WareHouse/`
- `data/raw/Presentaciones/Análisis de Datos Capítulo VIII "Análisis de Series Temporales".pdf`
- `data/raw/Presentaciones/Chapter3 - Data Preprocessing.pdf`
- `data/raw/Presentaciones/Data Mining_ Concepts and Techniques Chapter 4_ Data Warehousing and OLAP.pdf`

## 7. Laboratorios

Ubicación: `data/raw/Laboratorios/`

- `general/Formato_informe/` — formato oficial del informe
- `general/Laboratorios-old/` — laboratorios de años anteriores
- `laboratorio 1/ejemplos/` — material para L1

## 8. Ayudantías

Ubicación: `data/raw/ayudantias/2026/` — `250426.docx`

## 9. Pendientes (carpetas vacías)

- `data/raw/Cursos/` — vacía
- `data/raw/Codigo/` — vacía
- `data/raw/datasets/` — vacía (definir dataset L1–L5 idealmente biomédico)
- `data/raw/docs/` — vacía
- `data/raw/examenes/` — vacía
- `data/raw/papers/` — vacía
- `data/raw/Tareas/` — vacía
- `data/raw/clases/registro-clases/` — vacía

## Próximos pasos sugeridos

1. Procesar capítulos del Prof. Chacón con `pdf_extractor.py` → `data/processed/`.
2. Generar `outline.md` de cada libro con `book_explorer.py --outline-md --save`.
3. Definir dataset biomédico para los laboratorios L1–L5.
4. Resolver `IC_Ejercicios_PEP1_20-04-2026.pdf` como preparación para PEP1.
