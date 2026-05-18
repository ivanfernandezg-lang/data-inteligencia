# Guía de Ejercicios Resueltos — Análisis de Componentes Principales (PCA)

> **Inteligencia Computacional · USACH · Prof. Max Chacón**
> Capítulo II — Bloque A · PEP 1
> Fuente: `data/raw/Ejercicios/Guía - Análisis de Componentes Principales.pdf`
> Material procesado en: `data/processed/Ejercicios/guía-análisis-de-componentes-principales/`

## Convenciones usadas en esta guía

- **Varianza explicada** (validez del análisis) con $k$ componentes y matriz de correlación con $p$ variables:

  $$\text{VE}_k = \frac{\sum_{i=1}^{k}\lambda_i}{\sum_{i=1}^{p}\lambda_i}\cdot 100\%$$

  Cuando los datos están estandarizados (matriz de correlación), $\sum_{i=1}^{p}\lambda_i = p$.

- **Información perdida** con $k$ componentes:  $\text{IP}_k = 100\% - \text{VE}_k$.
- **Carga (loading)** de la variable $j$ sobre la componente $i$: coeficiente del autovector $v_{ji}$. Se interpreta su signo y magnitud.
- **Biplot**: se proyectan en el plano CP1–CP2 los autovectores ponderados (o no) y las observaciones. Los productos/variables apuntando juntos están correlacionados; los opuestos, anticorrelacionados.

---

## P1 — Comportamiento de consumo alimenticio

### Enunciado

Estudio de consumo en familias francesas. Sujetos clasificados por jefe de hogar: **MA#** (manual), **EM#** (empleado), **PF#** (profesional), donde `#` ∈ {2,3,4,5} es el número de hijos. Variables medidas (7): **Pan, Verduras, Frutas, Carnes, Aves, Lácteos, Vinos**.

**Matriz de correlación**:

|          | Pan  | Verd. | Frut. | Carn. | Aves  | Lác.  | Vinos |
| -------- | ---- | ----- | ----- | ----- | ----- | ----- | ----- |
| Pan      | 1,00 |       |       |       |       |       |       |
| Verduras | 0,59 | 1,00  |       |       |       |       |       |
| Frutas   | 0,20 | 0,87  | 1,00  |       |       |       |       |
| Carnes   | 0,32 | 0,89  | 0,96  | 1,00  |       |       |       |
| Aves     | 0,25 | 0,83  | 0,93  | 0,98  | 1,00  |       |       |
| Lácteos  | 0,86 | 0,66  | 0,33  | 0,37  | 0,23  | 1,00  |       |
| Vinos    | 0,30 | -0,35 | -0,49 | -0,44 | -0,40 | -0,40 | 1,00  |

**Autovalores**: $\lambda_1=4{,}339$;  $\lambda_2=1{,}829$;  $\lambda_3=0{,}625$;  $\lambda_4=0{,}502$;  $\lambda_5=0{,}393$;  $\lambda_6=0{,}099$;  $\lambda_7=0{,}083$.

**Autovectores (CP1, CP2)**:

| Variable | CP1    | CP2    |
| -------- | ------ | ------ |
| Pan      | -0,497 | 0,841  |
| Verduras | -0,972 | 0,131  |
| Frutas   | -0,931 | -0,277 |
| Carnes   | -0,963 | -0,190 |
| Aves     | -0,912 | -0,265 |
| Lácteos  | -0,584 | 0,707  |
| Vinos    | 0,425  | 0,649  |

**Dispersión de las familias en el plano CP1–CP2**:

![Dispersión familias P1](figuras/p1_dispersion_familias.png)

---

### Resolución

**a) Porcentaje de información perdida con sólo CP1 y CP2.**

Suma total de autovalores (debe ser $p=7$ por estar trabajando con la matriz de correlación; los decimales son por redondeo de la guía):

$$\sum_{i=1}^{7}\lambda_i = 4{,}339 + 1{,}829 + 0{,}625 + 0{,}502 + 0{,}393 + 0{,}099 + 0{,}083 = 7{,}870$$

Varianza explicada por CP1 + CP2:

$$\text{VE}_2 = \frac{4{,}339 + 1{,}829}{7{,}870}\cdot 100\% = \frac{6{,}168}{7{,}870}\cdot 100\% \approx 78{,}37\%$$

$$\boxed{\text{Información perdida} \approx 21{,}63\%}$$

**b) Caracterización de las componentes mirando sólo la nube de familias.**

Leyendo el plano CP1–CP2:

| Cuadrante               | Familias dominantes              | Interpretación socioeconómica            |
| ----------------------- | -------------------------------- | ---------------------------------------- |
| I  (CP1>0, CP2>0)       | Predominio **MA**, algunos **EM**| Bajos/medios ingresos, familias grandes  |
| II (CP1<0, CP2>0)       | **EM** y **MA** equilibrados, MA con CP2 más alto | Familias con niños (consumo de lácteos/pan) |
| III (CP1<0, CP2<0)      | Sólo **PF**                      | Profesionales (mayores ingresos)         |
| IV (CP1>0, CP2<0)       | Heterogéneo, predominio **EM**   | Mezcla; consumo más asociado a vino      |

Asumiendo ingreso creciente $\text{MA} < \text{EM} < \text{PF}$:

- **CP1** ordena por **nivel de ingreso** (CP1<0 → mayores ingresos; CP1>0 → menores).
- **CP2** discrimina por **tamaño/composición familiar** (CP2>0 → familias con más niños, mayor consumo de leche y pan).
- Se observa una separación aproximadamente lineal entre los tres tipos de jefes de hogar mediante rectas de pendiente negativa.

**c) Ubicación aproximada de las variables (productos) en el plano CP1–CP2.**

Cada variable se grafica en las coordenadas $(v_{j1}, v_{j2})$ del autovector:

| Producto | (CP1, CP2)       | Cuadrante |
| -------- | ---------------- | --------- |
| Pan      | (-0,497;  0,841) | II        |
| Verduras | (-0,972;  0,131) | II (cerca eje CP1−) |
| Frutas   | (-0,931; -0,277) | III       |
| Carnes   | (-0,963; -0,190) | III       |
| Aves     | (-0,912; -0,265) | III       |
| Lácteos  | (-0,584;  0,707) | II        |
| Vinos    | ( 0,425;  0,649) | I         |

Biplot que entrega la guía oficial (verificación):

![Biplot variables P1](figuras/p1_biplot_variables.png)

**d) Asociación de cada componente con los productos.**

- **CP1 (signo negativo dominante):** carnes, aves, frutas, verduras, lácteos, pan → es un eje de **consumo alimenticio general "de calidad"** (proteínas + frutas/verduras + lácteos). Valores negativos = consumo alto; valores positivos = bajo consumo. El vino es el único con CP1 positivo, contraponiéndose al resto.
- **CP2:** **pan y lácteos** (altos +) versus **carnes, aves, frutas** (negativos). Es un eje de **estilo de dieta familiar** (carbohidratos+lácteos vs. proteínas+vegetales). El vino contribuye también positivamente.

**e) Relación productos ↔ familias.**

Cruzando (b) y (d):

- **PF (profesionales, cuadrante III):** alto consumo de **carnes, aves, frutas, verduras** — coincide con la canasta más cara.
- **EM (empleados, cuadrante II principalmente):** mayor consumo de **pan y lácteos** — típico de familias con más niños.
- **MA (manuales, cuadrantes I y IV):** mayor consumo de **vino**; el resto de la canasta está más limitado.

> **Nota didáctica:** este ejercicio ilustra cómo PCA permite descubrir simultáneamente patrones de variables (productos) y de sujetos (familias) en un único plano factorial, base del análisis exploratorio.

---

## P2 — Caracterización de billetes falsos

### Enunciado

Bancos suizos miden 6 variables sobre billetes (papel originales, plástico originales y falsos):

- **LON**: longitud   ·  **LD**: largo de la diagonal
- **AI**: ancho izquierdo  ·  **AD**: ancho derecho
- **AMI**: ancho margen inferior  ·  **AMS**: ancho margen superior

**Autovalores**: $\lambda = (2{,}58;\ 1{,}34;\ 0{,}76;\ 0{,}56;\ 0{,}50;\ 0{,}26)$ (suman 6,00 = $p$).

**Autovectores (CP1, CP2)**:

| Variable | CP1   | CP2    |
| -------- | ----- | ------ |
| LON      | 0,395 | 0,799  |
| LD       | 0,207 | 0,345  |
| AI       | 0,445 | -0,263 |
| AD       | 0,411 | -0,375 |
| AMI      | 0,347 | -0,072 |
| AMS      | 0,560 | -0,163 |

**Dispersión** (círculos = papel originales, cuadrados = plástico originales, triángulos = falsos):

![Dispersión billetes P2](figuras/p2_dispersion_billetes.png)

Además, sobre **monedas** (6 variables de tamaño) se obtuvo: $\lambda = (1{,}96;\ 1{,}54;\ 1{,}09;\ 0{,}73;\ 0{,}40;\ 0{,}28)$.

### Resolución

**a) Porcentaje de validez del análisis (billetes).**

$$\text{VE}_2 = \frac{2{,}58 + 1{,}34}{2{,}58 + 1{,}34 + 0{,}76 + 0{,}56 + 0{,}50 + 0{,}26}\cdot 100\% = \frac{3{,}92}{6{,}00}\cdot 100\% = \boxed{65{,}33\%}$$

**b) Interpretación de las componentes.**

Todos los coeficientes de CP1 son **positivos**: CP1 mide el **"tamaño general" del billete combinado con el ancho de sus márgenes**. Los pesos más altos son **AMS (0,56), AI (0,45) y AD (0,41)** → CP1 enfatiza los **márgenes y anchos** (forma).

CP2 mezcla signos: **positivo en LON (0,80) y LD (0,35)** y **negativo en AI, AD, AMI, AMS**. CP2 contrapone **longitud/diagonal vs. márgenes y anchos** → indica el **tamaño longitudinal** (formato del billete).

- **CP1 ≈ Forma / márgenes internos** (AI + AD + AMI + AMS).
- **CP2 ≈ Tamaño longitudinal** (LON + LD).

**c) Características de los billetes originales.**

En el biplot:

- **Originales de papel (círculos):** ocupan el cuadrante I → **CP1>0** (mayores márgenes y anchos) y **CP2>0** (más largos).
- **Originales de plástico (cuadrados):** cuadrante IV → **CP1>0** (mayores márgenes) pero **CP2<0** (más cortos que los de papel).

⇒ Los originales (papel y plástico) comparten **márgenes amplios** (CP1 alto), lo que es el rasgo diferenciador clave frente a los falsos. Entre originales, los de papel son **más largos** que los de plástico.

**d) Diferencias entre falsificaciones.**

Los **falsos (triángulos)** se distribuyen en los cuadrantes **II y III** (CP1<0 → márgenes menores). Pero se separan en dos sub-cúmulos:

- **Falsos arriba del eje CP1** (cuadrante II, CP2>0): tienen mayor longitud — intentan imitar a los **originales de papel**.
- **Falsos abajo del eje CP1** (cuadrante III, CP2<0): tienen menor longitud — intentan imitar a los **originales de plástico**.

⇒ Sí existen **dos grupos de falsificaciones**, cada uno apuntando a un tipo de original.

**e) Comparación con el análisis de monedas.**

$$\text{VE}_2^{\text{monedas}} = \frac{1{,}96 + 1{,}54}{1{,}96+1{,}54+1{,}09+0{,}73+0{,}40+0{,}28}\cdot 100\% = \frac{3{,}50}{6{,}00}\cdot 100\% \approx \boxed{58{,}33\%}$$

> **Aclaración:** la versión de respuestas del PDF reporta 58,83 %; recomputando se obtiene **58,33 %** (probable errata de transcripción).

Se pierde aproximadamente **7 puntos porcentuales** respecto a los billetes (65,33 % → 58,33 %). En términos prácticos, **la precisión en monedas es algo menor**: la información se reparte más uniformemente entre componentes (las tres primeras superan 1, regla de Kaiser), por lo que para un análisis riguroso convendría retener **3 componentes** en monedas, con lo que $\text{VE}_3 = 4{,}59/6 \approx 76{,}5\%$.

---

## P3 — Caracterización de servicios hospitalarios

### Enunciado

22.846 ingresos al Hospital de Andalucía. 13 servicios (Medicina Interna, Ginecología, Pediatría, Cirugía, Traumatología, Urología, Digestivo, Otorrinolaringología, Cardiología, Neurología, Hematología, Oftalmología, Psiquiatría) caracterizados por **7 variables**:

| Var. | Significado                                                |
| ---- | ---------------------------------------------------------- |
| NI   | Número de ingresos                                         |
| MO   | Índice de mortalidad                                       |
| RE   | Reingresos al servicio (mismo diagnóstico)                 |
| NE   | Consultas externas                                         |
| ICM  | Índice promedio de complejidad de los pacientes admitidos  |
| ES   | Estancias (promedio de días-cama)                          |
| IF   | Índice de funcionalidad (eficiencia)                       |

$\lambda_1 = 2{,}558$ ; $\lambda_2 = 1{,}829$.

**Vectores propios**:

| Variable | CP1    | CP2    |
| -------- | ------ | ------ |
| NI       | 0,860  | -0,066 |
| MO       | 0,421  | 0,747  |
| RE       | -0,406 | 0,670  |
| NE       | -0,250 | 0,388  |
| ICM      | -0,562 | 0,635  |
| ES       | 0,820  | 0,508  |
| IF       | 0,663  | 0,078  |

**Dispersión de los servicios** (proyectados sobre CP1 vs CP2):

![Dispersión servicios P3](figuras/p3_dispersion_servicios.png)

### Resolución

**a) Validez del análisis.**

Como los datos están estandarizados, $\sum \lambda_i = p = 7$:

$$\text{VE}_2 = \frac{2{,}558 + 1{,}829}{7}\cdot 100\% = \frac{4{,}387}{7}\cdot 100\% \approx \boxed{62{,}67\%}$$

(La guía oficial deja la respuesta como "XX %"; el cálculo correcto bajo la convención estándar es ~62,67 %, suficiente para un análisis exploratorio.)

**b) Ubicación de las variables en el plano CP1–CP2.**

Cada variable se grafica en $(v_{j1}, v_{j2})$:

| Variable | (CP1; CP2)       | Cuadrante | Observación                       |
| -------- | ---------------- | --------- | --------------------------------- |
| NI       | ( 0,860; -0,066) | IV (eje CP1+) | Volumen de ingresos          |
| ES       | ( 0,820;  0,508) | I         | Estancias largas                  |
| IF       | ( 0,663;  0,078) | I (eje)   | Eficiencia                        |
| MO       | ( 0,421;  0,747) | I         | Mortalidad (gravedad)             |
| NE       | (-0,250;  0,388) | II        | Consultas externas                |
| RE       | (-0,406;  0,670) | II        | Reingresos                        |
| ICM      | (-0,562;  0,635) | II        | Complejidad de pacientes          |

**c) Interpretación de cada componente.**

- **CP1 (Demanda / volumen del servicio):** cargas altas y positivas en **NI, ES, IF** (todas relacionadas con cuántos pacientes pasan por el servicio y cuánto tiempo se quedan). Cargas negativas en **RE, NE, ICM**, propias de servicios más ambulatorios y complejos.
  - **CP1 > 0** → servicios de **alta demanda hospitalaria** (mucha cama, muchos ingresos).
  - **CP1 < 0** → servicios **especializados / ambulatorios** (muchos reingresos y consultas externas, menos cama).
- **CP2 (Riesgo / hospitalización vs. ambulatorio):** cargas positivas en **MO, ICM, RE, NE, ES**.
  - **CP2 > 0** → servicios con **mayor probabilidad de hospitalización, complejidad y mortalidad**.
  - **CP2 < 0** → servicios **ambulatorios** de menor riesgo.

**d) Clasificación de los servicios.**

| Servicio              | Cuadrante (CP1, CP2) | Lectura                                                       |
| --------------------- | -------------------- | ------------------------------------------------------------- |
| Medicina Interna      | I  (+, +)            | Alta demanda + alta hospitalización (servicio "estrella" en carga) |
| Cirugía               | I cerca del origen   | Demanda y hospitalización medias                              |
| Traumatología, Urología | IV (+, −)          | Demanda media, predominantemente **ambulatorios**             |
| Ginecología, Pediatría | IV (+, −)           | Alta demanda + ambulatorios                                   |
| Digestivo             | cerca del origen, II | Baja demanda pero **mayor mortalidad** relativa               |
| Otorrino, Cardio, Oftalmo | III (−, −)       | Baja demanda y bajo riesgo                                    |
| Psiquiatría, Hematología, Neurología | II (−, +) | Baja demanda pero **alta complejidad y reingresos**     |

**e) Servicios con mayor carga de trabajo cualitativa y cuantitativa.**

- **Cuantitativa** (volumen): los de **CP1 más positivo** → **Medicina Interna, Ginecología y Pediatría**.
- **Cualitativa** (complejidad, hospitalización): los de **CP2 más positivo** → **Medicina Interna** (que combina ambas) y los del cuadrante II (Psiquiatría, Hematología, Neurología).

⇒ Combinando ambos criterios: **Medicina Interna, Ginecología y Pediatría** son los servicios con mayor carga global.

**f) Servicios más eficientes.**

Para "más eficientes" se busca **alto IF con baja complejidad/mortalidad**: servicios con **CP1 alto pero CP2 bajo** (es decir, mucho volumen procesado, pacientes que no se complican). Esto corresponde a **Cirugía y Traumatología** (alta rotación, casos resueltos sin reingresos masivos).

---

## P4 — Análisis del sector lechero

### Enunciado

ACP en haciendas lecheras de un estado venezolano. 6 variables:

- **SUP**: superficie total       · **VACA**: número total de vacas
- **SANI**: índice sanitario      · **INST**: índice de instalaciones
- **MAQ**: índice de maquinarias  · **PROM**: promedio de leche/vaca

**Autovalores entregados**: $\lambda_1 = 1{,}794$; $\lambda_2 = 1{,}341$ (sólo se entregan los dos primeros).

**Autovectores ponderados por $\sqrt{\lambda_i}$** (cargas factoriales, no autovectores normalizados):

| Variable | CP1   | CP2    |
| -------- | ----- | ------ |
| SUP      |  0,79 |  0,10  |
| VACA     |  0,76 |  0,40  |
| SANI     |  0,44 | -0,48  |
| INST     |  0,32 | -0,48  |
| MAQ      |  0,53 | -0,26  |
| PROM     | -0,01 | -0,80  |

> La figura de la dispersión de las 8 haciendas en el plano CP1–CP2 que aparecía en el original (página 9) **no quedó embebida en el PDF distribuido** (la página está en blanco salvo el encabezado). La información sobre los 8 tipos de hacienda proviene del texto del enunciado y de la pauta de soluciones.

### Resolución

**a) Caracterización de cada componente.**

- **CP1 (Tamaño / Área productiva):** cargas altas y positivas en **SUP (0,79), VACA (0,76), MAQ (0,53)**. Captura el **tamaño y dotación productiva** de la hacienda → **área utilizada y volumen de cabezas (vacas/superficie)**.
- **CP2 (Nivel de tecnificación / industrialización):** carga muy negativa en **PROM (-0,80)** y negativas medias en **SANI (-0,48), INST (-0,48), MAQ (-0,26)**; positiva en **VACA (0,40)**. Como las cargas de PROM, SANI, INST y MAQ tienen el **mismo signo** (negativo), CP2 ordena por **nivel de industrialización**:
  - **CP2 < 0** → haciendas tecnificadas (alto PROM, buenas instalaciones y sanidad).
  - **CP2 > 0** → haciendas extensivas con muchas vacas pero baja productividad por animal.

**b) Tipos de haciendas (8 grupos identificados sobre el plano CP1–CP2).**

Según la pauta oficial:

| Grupo | Tipo de hacienda                          | Lectura factorial                              |
| ----- | ----------------------------------------- | ---------------------------------------------- |
| A, C  | **Haciendas matadero**                    | Mucho ganado, baja producción de leche/vaca    |
| B     | **Hacienda lechera**                      | Alta producción/vaca, buena tecnificación      |
| D, E  | **Haciendas multipropósito**              | Posiciones intermedias en ambos ejes           |
| F     | **Hacienda de crianza, pastoreo y engorde** | Mucha superficie, ganado, baja tecnificación |
| G, H  | **Haciendas muy pequeñas**                | Bajo CP1 (poca superficie y vacas)             |

**c) Porcentaje de validez del estudio.**

Sólo se conocen los dos primeros autovalores. Si los datos están estandarizados (matriz de correlación), $\sum \lambda_i = p = 6$, y entonces:

$$\text{VE}_2 = \frac{1{,}794 + 1{,}341}{6}\cdot 100\% = \frac{3{,}135}{6}\cdot 100\% \approx \boxed{52{,}25\%}$$

Este valor es relativamente bajo; en un análisis riguroso convendría incluir CP3 (no provista en la guía).

> La pauta oficial deja este punto como "Faltan algunos valores propios (?)", confirmando que sólo se publicaron $\lambda_1$ y $\lambda_2$. Bajo la convención estándar de matriz de correlación, el valor calculado es **52,25 %**.

---

## Resumen comparativo de los 4 problemas

| Problema | $p$ | Variables clave | $\lambda_1+\lambda_2$ | VE₂   | Interpretación CP1            | Interpretación CP2                |
| -------- | --- | --------------- | --------------------- | ----- | ----------------------------- | --------------------------------- |
| P1 Familias | 7 | Pan, Verd, Frut, Carn, Aves, Lác, Vinos | 6,168 | **78,4 %** | Calidad/cantidad de canasta (proxy de ingreso) | Tipo de dieta (lácteos+pan vs. proteína+vegetal) |
| P2 Billetes | 6 | LON, LD, AI, AD, AMI, AMS                | 3,92  | **65,3 %** | Forma / márgenes internos      | Tamaño longitudinal               |
| P2 Monedas  | 6 | (6 medidas de tamaño)                    | 3,50  | **58,3 %** | —                              | —                                 |
| P3 Hospital | 7 | NI, MO, RE, NE, ICM, ES, IF              | 4,387 | **62,7 %** | Demanda / volumen              | Hospitalización + riesgo vs. ambulatorio |
| P4 Lechero  | 6 | SUP, VACA, SANI, INST, MAQ, PROM         | 3,135 | **52,3 %** | Tamaño / área productiva       | Nivel de industrialización        |

---

## Errores y observaciones detectadas en el material original

1. **P2-e:** la pauta del PDF reporta **58,83 %**; el cálculo correcto es **58,33 %**. (3,50/6,00 ≠ 0,5883).
2. **P3-a:** la pauta del PDF deja "XX %" sin completar. Bajo convención estándar (suma de autovalores = $p$), la validez es **62,67 %**.
3. **P4 figura:** la página 9 del PDF distribuido no contiene la nube de puntos prometida en el enunciado, sólo encabezado/pie. El análisis del punto (b) se basó en la pauta oficial.
4. **P4-c:** la pauta indica explícitamente "Faltan algunos valores propios (?)" — corregido aquí asumiendo matriz de correlación estandarizada.

---

## Glosario rápido (PEP 1)

- **Matriz de correlación**: matriz $p\times p$ simétrica con $1$ en la diagonal. Sus autovalores suman $p$.
- **Autovalor $\lambda_i$**: varianza explicada por la $i$-ésima componente.
- **Autovector $v_i$**: dirección en $\mathbb{R}^p$ que maximiza la varianza proyectada (sujeto a ortogonalidad con los anteriores).
- **Regla de Kaiser**: retener componentes con $\lambda_i > 1$ cuando se usa matriz de correlación.
- **Biplot**: superposición en el plano CP1–CP2 de observaciones (scores) y variables (loadings).
- **Carga ponderada**: $v_{ji}\cdot\sqrt{\lambda_i}$, equivale a la correlación de la variable $j$ con la componente $i$.
