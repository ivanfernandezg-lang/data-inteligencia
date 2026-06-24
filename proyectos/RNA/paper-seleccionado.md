# 🔬 Selección de Paper — Tarea IC RNA 2026-1

> **Fecha análisis:** 23 de junio de 2026
> **Objetivo:** Seleccionar el mejor paper para la tarea del módulo RNA (Prof. Gonzalo Acuña), considerando que hay **poco tiempo** y se está **recién aprendiendo RNA**.

---

## 📋 Contexto de la Tarea

| Elemento          | Detalle                                              |
| ----------------- | ---------------------------------------------------- |
| **Asignatura**    | Inteligencia Computacional — Módulo Redes Neuronales |
| **Profesor**      | Gonzalo Acuña Leiva                                  |
| **Fecha entrega** | 06/07/2026 (~2 semanas)                              |
| **Entregables**   | Informe 10 páginas + Video 10–15 min                 |
| **Modalidad**     | Grupos de hasta 2 personas                           |

### Estructura del informe:

| Sección                | Peso | Contenido esperado                                            |
| ---------------------- | ---- | ------------------------------------------------------------- |
| Presentación           | 10%  | Ortografía, redacción, formato                                |
| Introducción           | 15%  | Problema, ¿por qué RNA?, hipótesis                            |
| Marco Teórico          | 15%  | Tipo, arquitectura, modo aprendizaje, funciones de activación |
| Experimentación        | 15%  | Dataset, algoritmos, librerías, costo computacional           |
| Análisis de resultados | 30%  | Métricas, eficiencia, criterios de selección de modelo        |
| Conclusiones           | 20%  | Aporte al conocimiento, evaluación de hipótesis               |
| Referencias            | 10%  | Citas y bibliografía                                          |

---

## 🎯 Criterios de Selección

Dado que el estudiante tiene **poco tiempo** y está **recién aprendiendo RNA**, se priorizó:

| #   | Criterio                        | Peso       | Descripción                                                                                                     |
| --- | ------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| 1   | **Alineación con el curso**     | ⭐⭐⭐⭐⭐ | El paper debe tratar temas vistos en clases: perceptron, adaline, MLP, backpropagation                          |
| 2   | **Facilidad de comprensión**    | ⭐⭐⭐⭐   | Debe ser legible para alguien que recién ve RNA, sin notación excesivamente densa                               |
| 3   | **Facilidad de implementación** | ⭐⭐⭐⭐   | Los experimentos deben ser reproducibles con Python + scikit-learn/keras en hardware modesto                    |
| 4   | **Claridad estructural**        | ⭐⭐⭐     | El paper debe tener secciones claras (introducción, método, experimentos, resultados) para facilitar el informe |
| 5   | **Extensión**                   | ⭐⭐       | Preferible papers cortos/medianos (5–20 págs) sobre papers muy largos                                           |

---

## 📚 Temario del Curso (referencia)

Las clases del Prof. Acuña cubrieron:

| Clase | Tema                    | Contenido clave                                                              |
| ----- | ----------------------- | ---------------------------------------------------------------------------- |
| 1     | Introducción            | Neurona biológica → neurona artificial, aprendizaje, RNA, deep learning      |
| 2     | Perceptron              | Clasificación, regresión, aproximación de funciones, regla de aprendizaje    |
| 3     | Adaline                 | Regresión lineal, mínimos cuadrados, máxima verosimilitud, Widrow-Hoff (LMS) |
| 4     | Perceptron Multicapa    | MLP, retropropagación del error (backpropagation), gradiente descendente     |
| 5     | Elaboración modelos MLP | Preprocesamiento, selección de arquitectura, validación, buenas prácticas    |

---

## 🚫 Papers Prohibidos

Los siguientes papers **NO pueden ser seleccionados** (según `papers-prohibidos.md`):

1. ~~Attention Is All You Need (Vaswani et al., 2017)~~ — Transformers
2. ~~Very Deep CNN (Simonyan & Zisserman, 2015)~~ — VGG
3. ~~Empirical Evaluation of GRU (Chung et al., 2014)~~ — GRU
4. ~~Naive SVR and MLP Benchmarks (NNGC 2010)~~ — SVR + MLP
5. ~~Two-hidden-layer ELM (Qu et al., 2015)~~ — Extreme Learning Machine
6. ~~Do Vision Transformers See Like CNNs?~~ — ViT vs CNN

---

## 📊 Análisis Completo de los 15 Papers Elegibles

A continuación, la tabla con **todos** los papers de `RNA-papers-example/` que NO están prohibidos (se excluye también el duplicado `copia-de-adaptive-ensembles...`):

| #   | Paper                                                  | Año  | Págs | Arquitectura                                              | Dataset                                | Tarea                     | Complejidad | Alineación curso | Implementación |
| --- | ------------------------------------------------------ | ---- | ---- | --------------------------------------------------------- | -------------------------------------- | ------------------------- | ----------- | ---------------- | -------------- |
| 1   | **Widrow — 30 Years of Adaptive Neural Networks**      | 1990 | 37   | Perceptron, **Adaline**, **Madaline**, **MLP + Backprop** | Patrones binarios, voz, eco, control   | Clasificación + Regresión | **Media**   | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐     |
| 2   | **LeCun, Bengio & Hinton — Deep Learning (Nature)**    | 2015 | 9    | MLP, CNN, RNN (revisión conceptual)                       | ImageNet, voz, moléculas (múltiples)   | Revisión / Tutorial       | **Baja**    | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐       |
| 3   | **Rosenblatt — The Perceptron**                        | 1958 | 14   | **Perceptron** (1 capa)                                   | Patrones visuales (letras, formas)     | Clasificación binaria     | **Alta**    | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐     |
| 4   | **Goodfellow et al. — GAN**                            | 2014 | 9    | **MLP** (Generador + Discriminador)                       | MNIST, TFD, CIFAR-10                   | Modelado generativo       | **Alta**    | ⭐⭐⭐⭐         | ⭐⭐⭐         |
| 5   | **Hopfield — Neural Networks and Physical Systems**    | 1982 | 5    | **Red de Hopfield** (recurrente)                          | Estados binarios simulados (N=30, 100) | Memoria asociativa        | **Alta**    | ⭐⭐⭐           | ⭐⭐⭐⭐⭐     |
| 6   | **LeCun et al. — Gradient-Based Learning (LeNet-5)**   | 1998 | 46   | CNN + MLP (LeNet-5)                                       | **MNIST** (60k/10k)                    | Clasificación imágenes    | **Alta**    | ⭐⭐⭐⭐         | ⭐⭐⭐         |
| 7   | **Hochreiter & Schmidhuber — LSTM**                    | 1997 | 30   | LSTM (recurrente)                                         | Datos artificiales (long time lag)     | Predicción secuencias     | **Alta**    | ⭐⭐⭐           | ⭐⭐           |
| 8   | **Greff et al. — LSTM Vanilla (Search Space Odyssey)** | 2017 | 15   | LSTM + 8 variantes                                        | TIMIT, IAM, JSB Chorales               | Clasificación secuencias  | **Alta**    | ⭐⭐⭐           | ⭐⭐           |
| 9   | **Adaptive Ensembles of Fine-Tuned Transformers**      | 2024 | 8    | Transformers (DistilBERT, DeBERTa, etc.)                  | DAIGT, Deepfake                        | Clasificación texto       | **Alta**    | ⭐               | ⭐             |
| 10  | **Stacking Transformers (Gstack)**                     | 2024 | 20   | Transformers (Llama-style, 7B)                            | The Pile, C4                           | Modelado lenguaje         | **Alta**    | ⭐               | ⭐             |
| 11  | **Time Series Transformers Review**                    | 2023 | 20   | Transformers para time series                             | ETT, Electricity, Weather              | Survey                    | **Alta**    | ⭐               | ⭐⭐           |
| 12  | **Let's Have a Chat — ChatGPT**                        | 2023 | 12   | GPT-3 + RLHF (Transformer)                                | Benchmarks médicos/educativos          | Survey divulgativo        | **Baja**    | ⭐               | N/A            |
| 13  | **One Hundred Years in AI**                            | 2021 | 82   | General (reporte políticas IA)                            | N/A                                    | Reporte institucional     | **Baja**    | ⭐               | N/A            |
| 14  | **ANN Review Statistics**                              | 1994 | 29   | MLP, RBF, Bayesian (revisión)                             | N/A                                    | Revisión estadística      | **Media**   | ⭐⭐⭐⭐         | ⭐⭐           |
| 15  | **Support Vector Regression Machines**                 | 1997 | 8    | ⚠️ **NO es RNA** (SVR, kernel)                            | Friedman + Boston Housing              | Regresión                 | **Alta**    | ⭐               | ⭐⭐⭐         |

> ⚠️ **Nota sobre papers con extracción deficiente:** `lecun-01a` (MD corrupto/binario), `ann_review_statistics` (PDF escaneado, solo portada extraída), y `lstm-hochreiter-schmidhuber` (OCR muy fragmentado) tienen su contenido original difícil de leer directamente desde el Markdown extraído. Se recomienda leer el PDF original en estos casos.

---

## 🏆 TOP 5 — Mejores Papers para la Tarea

### 🥇 #1: Widrow — «30 Years of Adaptive Neural Networks: Perceptron, Madaline, and Backpropagation» (1990)

| Criterio                        | Evaluación                                                                                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alineación con el curso**     | ⭐⭐⭐⭐⭐ — **Cubre EXACTAMENTE el temario completo** del Prof. Acuña: perceptron → adaline (LMS/Widrow-Hoff) → madaline → MLP con backpropagation      |
| **Facilidad de comprensión**    | ⭐⭐⭐⭐ — Escrito como tutorial histórico. Explica el _principio de mínima perturbación_ y la regla delta de forma intuitiva                            |
| **Facilidad de implementación** | ⭐⭐⭐⭐⭐ — LMS (Widrow-Hoff) se implementa en ~10 líneas de Python. Adaline y perceptron igualmente simples. Backpropagation con explicación detallada |
| **Estructura para el informe**  | ⭐⭐⭐⭐ — Secciones claras: Perceptron → Adaline → Madaline → Backpropagation. Cada una con problema, método, resultados                                |
| **Extensión**                   | ⭐⭐⭐ — 37 páginas, pero se puede enfocar en secciones específicas                                                                                      |

**Ventajas clave:**

- Escrito por **Bernard Widrow**, el inventor del algoritmo LMS (1960) que dio origen al Adaline
- Conecta TODOS los temas vistos en clase en un solo paper
- Explica backpropagation como evolución natural desde perceptron y adaline
- Contiene ejemplos concretos: filtros adaptativos, cancelación de eco, reconocimiento de patrones
- Las implementaciones (LMS, perceptron, backprop) son triviales en Python con numpy

**Desventajas:**

- Notación IEEE de 1990 (alguna terminología añeja)
- 37 páginas: hay que seleccionar secciones para no exceder las 10 págs del informe
- No usa datasets modernos tipo UCI/Kaggle

**Ideal para:** Un informe que recorra la evolución perceptron → adaline → MLP → backprop, mostrando cómo cada arquitectura resuelve limitaciones de la anterior.

---

### 🥈 #2: LeCun, Bengio & Hinton — «Deep Learning» (Nature, 2015)

| Criterio                        | Evaluación                                                                                                                                                           |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alineación con el curso**     | ⭐⭐⭐⭐⭐ — Explica **backpropagation, SGD, MLP, ReLU**, y el concepto de que las capas ocultas "deforman" el espacio de entrada para hacerlo linealmente separable |
| **Facilidad de comprensión**    | ⭐⭐⭐⭐⭐ — **El paper más pedagógico de todos.** Escrito para una audiencia general de Nature. Figuras icónicas (Fig. 1: deformación del espacio)                  |
| **Facilidad de implementación** | ⭐⭐⭐⭐ — No hay experimentos propios que reproducir, pero los conceptos son directamente implementables. Se puede complementar con experimentos propios en MNIST   |
| **Estructura para el informe**  | ⭐⭐⭐⭐ — Secciones: Supervised Learning → Backpropagation → CNNs → RNNs → Representations                                                                          |
| **Extensión**                   | ⭐⭐⭐⭐⭐ — **Solo 9 páginas.** Ideal para poco tiempo                                                                                                              |

**Ventajas clave:**

- Escrito por **3 ganadores del Premio Turing 2018** (Yann LeCun, Yoshua Bengio, Geoffrey Hinton)
- La explicación más clara que existe de cómo el MLP + backpropagation aprende representaciones jerárquicas
- Cubre exactamente lo que el curso pide: tipo de RNA, arquitectura, backpropagation, funciones de activación
- 9 páginas: se lee en una tarde y se entiende todo

**Desventajas:**

- ⚠️ Es un **review de Nature**, no un paper experimental. No tiene experimentos propios que describir en la sección "Experimentación"
- Para la sección de experimentación del informe, habría que **complementar con experimentos propios** (ej. entrenar un MLP en MNIST y reportar métricas)
- No profundiza en derivaciones matemáticas de backprop (las asume conocidas)

**Ideal para:** Un informe conceptualmente sólido, complementado con experimentos propios sencillos (MLP con keras en MNIST o Iris).

---

### 🥉 #3: Rosenblatt — «The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain» (1958)

| Criterio                        | Evaluación                                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Alineación con el curso**     | ⭐⭐⭐⭐⭐ — **El paper ORIGINAL del perceptron.** Es la base de todo lo visto en clases                    |
| **Facilidad de comprensión**    | ⭐⭐⭐ — Notación de 1958, enfoque filosófico-biológico. Requiere paciencia pero es profundamente revelador |
| **Facilidad de implementación** | ⭐⭐⭐⭐⭐ — Un perceptrón se implementa en ~30 líneas de Python                                            |
| **Estructura para el informe**  | ⭐⭐⭐ — Estructura académica clásica pero no tan explícita como papers modernos                            |
| **Extensión**                   | ⭐⭐⭐⭐ — 14 páginas. Manejable                                                                            |

**Ventajas clave:**

- **Paper SEMINAL** que originó el campo de las Redes Neuronales Artificiales
- Introduce el concepto de aprendizaje por corrección de error
- Discute la filosofía de la conexión vs. representación simbólica (el debate que definió la IA)
- Riquísimo en contenido histórico y conceptual para la introducción y conclusiones
- Implementación trivial

**Desventajas:**

- Notación y lenguaje de 1958 (publicado en _Psychological Review_)
- Los experimentos son con patrones visuales simples (no datasets modernos)
- El enfoque es más filosófico/biológico que ingenieril

**Ideal para:** Un informe con fuerte componente histórico-conceptual, que trace el origen de las RNA desde el primer perceptron.

---

### 4️⃣ #4: Hopfield — «Neural Networks and Physical Systems with Emergent Collective Computational Abilities» (1982)

| Criterio                        | Evaluación                                                                                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alineación con el curso**     | ⭐⭐⭐ — Cubre un paradigma diferente (redes recurrentes con aprendizaje Hebbiano), no feedforward. Pero el concepto de neurona artificial y aprendizaje es central |
| **Facilidad de comprensión**    | ⭐⭐⭐ — Elegancia física-matemática (función de energía tipo Ising). Requiere cierta madurez                                                                       |
| **Facilidad de implementación** | ⭐⭐⭐⭐⭐ — Se implementa en ~50 líneas de Python puro. Cero dependencias                                                                                          |
| **Estructura para el informe**  | ⭐⭐⭐⭐ — 5 páginas, muy conciso. Secciones claras: modelo → dinámica → capacidad → simulaciones                                                                   |
| **Extensión**                   | ⭐⭐⭐⭐⭐ — **Solo 5 páginas.** El más corto de todos                                                                                                              |

**Ventajas clave:**

- Paper **bellísimo** que conecta física estadística (modelo de Ising) con neurociencia computacional
- Modelo extremadamente simple de implementar: N neuronas binarias, pesos simétricos, regla de Hebb
- Demuestra propiedades emergentes: memoria asociativa, corrección de errores, generalización
- Solo 5 páginas — se lee en una hora
- Las simulaciones (N=30, N=100) son replicables en minutos

**Desventajas:**

- Es una red **recurrente** con aprendizaje **no supervisado** (Hebbiano), diferente del paradigma feedforward + backpropagation del curso
- Capacidad de almacenamiento muy limitada (~0.15N patrones)
- No usa backpropagation ni gradiente descendente
- Requiere explicar la diferencia con lo visto en clases

**Ideal para:** Un informe que contraste paradigmas (feedforward vs. recurrente) o que explore propiedades emergentes en sistemas neuronales simples.

---

### 5️⃣ #5: Goodfellow et al. — «Generative Adversarial Nets» (2014)

| Criterio                        | Evaluación                                                                                                                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alineación con el curso**     | ⭐⭐⭐⭐ — **Usa MLPs explícitamente.** El paper dice: _"In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation"_ |
| **Facilidad de comprensión**    | ⭐⭐⭐ — El concepto adversarial es intuitivo, pero el entrenamiento (minimax, equilibrio de Nash) requiere base matemática                                                       |
| **Facilidad de implementación** | ⭐⭐⭐ — Hay código disponible, pero el entrenamiento es **inestable** (mode collapse, vanishing gradients). Requiere ajuste cuidadoso                                            |
| **Estructura para el informe**  | ⭐⭐⭐⭐⭐ — Estructura impecable: Abstract → Introduction → Related Work → Adversarial Nets → Theoretical Results → Experiments → Discussion                                     |
| **Extensión**                   | ⭐⭐⭐⭐ — 9 páginas                                                                                                                                                              |

**Ventajas clave:**

- Paper **revolucionario** (35,000+ citas). El framework adversarial es una de las ideas más importantes en deep learning
- Usa MLP + backpropagation + dropout, todo visto en clases
- Experimentos en MNIST, TFD, CIFAR-10 (datasets estándar y accesibles)
- Estructura perfecta para el informe (secciones muy claras)
- El concepto de "dos redes compitiendo" es muy atractivo para el video

**Desventajas:**

- Entrenamiento **notoriamente inestable** (mode collapse, non-convergence)
- Difícil de evaluar: no tiene una función de likelihood explícita
- Requiere entender teoría de juegos (minimax, equilibrio de Nash)
- Para alguien recién aprendiendo RNA, puede ser frustrante lograr que entrene bien

**Ideal para:** Un informe ambicioso que muestre una aplicación creativa de MLP + backpropagation en un framework no convencional.

---

## 📈 Tabla Comparativa del Top 5

| Ranking | Paper                 | Págs | Comprensión | Implementación | Alineación curso | Esfuerzo estimado | ¿Tiene experimentos?              |
| ------- | --------------------- | ---- | ----------- | -------------- | ---------------- | ----------------- | --------------------------------- |
| 🥇      | **Widrow 1990**       | 37   | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐⭐       | **8–10 h**        | ✅ Sí (múltiples)                 |
| 🥈      | **LeCun et al. 2015** | 9    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐       | **6–8 h**         | ❌ Review (requiere complementar) |
| 🥉      | **Rosenblatt 1958**   | 14   | ⭐⭐⭐      | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐⭐       | **7–9 h**         | ✅ Sí (patrones visuales)         |
| 4       | **Hopfield 1982**     | 5    | ⭐⭐⭐      | ⭐⭐⭐⭐⭐     | ⭐⭐⭐           | **5–7 h**         | ✅ Sí (simulaciones)              |
| 5       | **Goodfellow 2014**   | 9    | ⭐⭐⭐      | ⭐⭐⭐         | ⭐⭐⭐⭐         | **10–12 h**       | ✅ Sí (MNIST, TFD, CIFAR-10)      |

---

## ✅ Recomendación Final

### 🥇 Recomendación Principal: **Widrow — «30 Years of Adaptive Neural Networks» (1990)**

**¿Por qué es LA mejor opción?**

1. **Cubre el 100% del temario del curso.** Es el único paper que recorre perceptron → adaline → madaline → MLP con backpropagation de forma integrada. Puedes estructurar tu informe exactamente como las clases del Prof. Acuña.

2. **Implementaciones triviales.** LMS (Adaline) son 10 líneas de Python. El perceptron otras 15. Backpropagation para MLP otras 30. Todo con numpy puro, sin necesidad de GPU ni frameworks complejos.

3. **Conexión directa con las clases.** El Prof. Acuña dedica clases completas a Adaline y al algoritmo LMS de Widrow-Hoff. Este paper fue escrito por el mismísimo Widrow. Es como si el paper y el curso estuvieran sincronizados.

4. **Estructura perfecta para el informe:**
   - **Introducción:** Historia y motivación de las RNA adaptativas
   - **Marco Teórico:** Perceptron → Adaline (LMS) → Madaline → MLP + Backpropagation
   - **Experimentación:** Filtros adaptativos, cancelación de eco, reconocimiento de patrones
   - **Análisis:** Comparación de arquitecturas, principio de mínima perturbación
   - **Conclusiones:** Evolución del paradigma conexionista, limitaciones y legado

5. **Para el video:** La narrativa "de Perceptron a Backpropagation en 30 años" es perfecta para 10–15 minutos.

### 🥈 Alternativa si quieres algo más corto y conceptual: **LeCun, Bengio & Hinton — «Deep Learning» (2015)**

Si prefieres un paper más moderno, más corto (9 págs) y extremadamente bien escrito, esta es tu opción. **Pero ojo:** tendrías que complementar la sección de experimentación con código propio (entrenar un MLP en MNIST/Iris y reportar tus propias métricas). Esto suma ~2–3 horas de trabajo pero te da libertad creativa.

### ⚠️ Qué NO elegiría en tu situación:

- **Transformers / LLMs** (adaptive ensembles, stacking, time series transformers, ChatGPT): demasiado complejos, requieren GPUs, cero relación con lo visto en clases.
- **SVR** (support vector regression): ni siquiera es una red neuronal.
- **LSTM** (ambos): arquitecturas recurrentes complejas, los MD extraídos están muy fragmentados.
- **One Hundred Years in AI / ChatGPT survey**: no son papers técnicos de RNA.

---

## 📎 Referencia Rápida

| Archivo                 | Ruta                                                                         |
| ----------------------- | ---------------------------------------------------------------------------- |
| Paper recomendado (PDF) | `data/raw/RNA-papers-example/Widrow 30years Adaptive Neural Networks.pdf`    |
| Paper extraído (MD)     | `data/processed/RNA-papers-example/widrow-30years-adaptive-neural-networks/` |
| Enunciado de la tarea   | `proyectos/RNA/enunciado/Tarea IC RNA 2026 1.pdf`                            |
| Papers prohibidos       | `proyectos/RNA/papers-prohibidos.md`                                         |
| Clases del profesor     | `data/raw/RNA-Clases/`                                                       |

---

> ✨ **En una frase:** El paper de Widrow es el que te permitirá hacer el mejor informe con el menor esfuerzo, porque **ya sabes todo lo que necesitas saber** de las clases del Prof. Acuña. Solo es cuestión de conectarlo.
