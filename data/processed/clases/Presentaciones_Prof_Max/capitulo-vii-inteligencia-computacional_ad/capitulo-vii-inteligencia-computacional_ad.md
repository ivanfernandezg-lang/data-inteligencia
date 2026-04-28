# Capitulo VII Inteligencia Computacional_AD

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23/03/2017
1
Inteligencia Computacional
Capítulo VII
“Árboles de Decisión”
Profesor: Dr. Max Chacón.
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática
Objetivos
• Comprender la generación de un árbol de decisión.
• Cuantificar la ganancia de información para un
atributo en un conjunto de datos.
• Comprender los algoritmos de generación de los
árboles de decisión.
• Establecer los mecanismos de poda de los árboles de
decisión.
• Comprender los mecanismos de equivalencia de
reglas y la generalización de reglas simples.

![Imagen](images\page001_img01.png)

---

## Página 2

23/03/2017
2
7.1.Definiciones.
Los árboles de decisión fueron presentados por J. R.
Quinlan en 1983, se verá la versión C4.5. Actualmente
existen variaciones de estos algoritmos.
La idea original
se basa en los trabajos de Hoveland y
Hunt de 1950, y Hunt, Marin y Stone 1966, los cuales
están basados en modelos psicológicos de como las
personas aprenden conceptos simples.
La idea básica es lo que se denomina sistemas de
aprendizaje conceptual, los cuales intentan distinguir
características de un conjunto de entrenamiento, que es en
esencia una aplicación del método de divide y conquista.
Considerando una base de datos o sistema de información
procedimental SI=<U, Q, V, f > como fue definida:
–S⊆U universo cerrado: un conjunto finito, no vacío, de n
objetos {x1, x2, …, xn}
–Q: un conjunto finito, no vacío, de p atributos {q1, q2, …,
qp}
–V=
, donde
es un dominio (i indica los posibles
valores de cada atributo o instancias) de cada uno de los
atributos q.
– f:SxQ→V es una función de decisión llamada función de
información, tal que f(x,q)∈Vq para cualquier q∈Q, x∈S.
U
Q
q
q
iV
∈
q
iV

![Imagen](images\page002_img01.png)

---

## Página 3

23/03/2017
3
El SI puede ser representado por una tabla finita de datos,
donde las columnas están indicadas por los atributos y las
filas por los objetos.
Se
denominan
atributos
estudiantes
a
los
atributos
comprendidos entre q1 a qp-1.
Se denomina atributo experto o de características al
atributo qp que separa los n objetos en k clases { ,
, … ,
}.
Objeto
Atributos
S
q1
q2
…
qj
…
qp-1
qp
x1
x2
.
.
1
1
V
1
3V
1
4
V
2
2
V
2
1
V
2
4
V
j
V3
j
V2
j
V4
1
1
−
p
V
p
V1
1
2
−
p
V
p
V2
1
2
−
p
V
p
k
V
p
V1
p
V2
p
k
V
La idea inicial del método de Hunt
construir un árbol de decisión desde un conjunto de
casos de entrenamiento S que consiste de n
ejemplos, pertenecientes a k diferentes clases
{C1,C2,…,Ck} indicadas por el atributo experto qp.
La tarea es dividir el conjunto de entrenamiento S
en conjuntos disjuntos T1, T2, …,Tn, creando una
partición, basada en una característica simple.

### Tabla 1 (Página 3)

| Objeto | Atributos | None | None | None | None | None | None |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S | q
1 | q
2 | … | q
j | … | q
p-1 | q
p |
| x
1 | V1
1 | V2
2 | Vj
3 |  |  | Vp−1
1 | Vp
1 |
| x
2 | V1
3 | V2
1 | V j
2 |  |  | Vp−1
2 | Vp
2 |
| .
. | V1
4 | V2
4 | Vj
4 |  |  | Vp−1
2 | Vp
k |

![Imagen](images\page003_img01.png)

---

## Página 4

23/03/2017
4
Ej: Clasificación automática de objetos
Para analizar el caso más general, considere la
clasificación de figuras geométricas.
Ej: Clasificación de figuras
Clase 1 (1)
Clase 2 (0)
La base de datos operacional será:
T
Carac. 1
Carac. 2
Carac. 3
Carac. 4
Carac. 5
Obj.
Forma
Área
Tono
Sombra
Clase
1
Cuadrado
4 cm2
Blanco
Si
Clase 1
2
Cuadrado
5 cm2
Negro
Si
Clase 2
3
Cuadrado
5,5 cm2
Negro
No
Clase 2
4
Cuadrado
3,9 cm2
Negro
No
Clase 2
5
Cuadrado
3,8 cm2
Blanco
No
Clase 1
6
Triángulo
3,9 cm2
Negro
Si
Clase 1
7
Triángulo
4,6 cm2
Negro
No
Clase 1
8
Triángulo
3,6 cm2
Blanco
Si
Clase 1
9
Triángulo
4,2 cm2
Blanco
No
Clase 1
10
Círculo
3,8 cm2
Negro
Si
Clase 2
11
Círculo
3,7 cm2
Blanco
Si
Clase 2
12
Círculo
4 cm2
Negro
No
Clase 1
13
Círculo
3,7 cm2
Negro
No
Clase 1
14
Círculo
3,8 cm2
Negro
No
Clase 1

### Tabla 1 (Página 4)

| T | Carac. 1 | Carac. 2 | Carac. 3 | Carac. 4 | Carac. 5 |
| --- | --- | --- | --- | --- | --- |
| Obj. | Forma | Área | Tono | Sombra | Clase |
| 1 | Cuadrado | 4 cm2 | Blanco | Si | Clase 1 |
| 2 | Cuadrado | 5 cm2 | Negro | Si | Clase 2 |
| 3 | Cuadrado | 5,5 cm2 | Negro | No | Clase 2 |
| 4 | Cuadrado | 3,9 cm2 | Negro | No | Clase 2 |
| 5 | Cuadrado | 3,8 cm2 | Blanco | No | Clase 1 |
| 6 | Triángulo | 3,9 cm2 | Negro | Si | Clase 1 |
| 7 | Triángulo | 4,6 cm2 | Negro | No | Clase 1 |
| 8 | Triángulo | 3,6 cm2 | Blanco | Si | Clase 1 |
| 9 | Triángulo | 4,2 cm2 | Blanco | No | Clase 1 |
| 10 | Círculo | 3,8 cm2 | Negro | Si | Clase 2 |
| 11 | Círculo | 3,7 cm2 | Blanco | Si | Clase 2 |
| 12 | Círculo | 4 cm2 | Negro | No | Clase 1 |
| 13 | Círculo | 3,7 cm2 | Negro | No | Clase 1 |
| 14 | Círculo | 3,8 cm2 | Negro | No | Clase 1 |

![Imagen](images\page004_img01.png)

---

## Página 5

23/03/2017
5
Particiones
Forma = Cuadrado
Tono = Blanco
Tono = Negro
Forma
Área
Tono
Sombra
Clase
1
Cuadrado
4 cm2
Blanco
Si
Clase 1
5
Cuadrado
3,8 cm2
Blanco
No
Clase 1
2
Cuadrado
5 cm2
Negro
Si
Clase 2
3
Cuadrado
5,5 cm2
Negro
No
Clase 2
4
Cuadrado
3,9 cm2
Negro
No
Clase 2
Particiones
Forma = Triángulo
6
Triángulo
3,9 cm2
Negro
Si
Clase 1
7
Triángulo
4,6 cm2
Negro
No
Clase 1
8
Triángulo
3,6 cm2
Blanco
Si
Clase 1
9
Triángulo
4,2 cm2
Blanco
No
Clase 1

### Tabla 1 (Página 5)

|  | Forma | Área | Tono | Sombra | Clase |
| --- | --- | --- | --- | --- | --- |
| 1 | Cuadrado | 4 cm2 | Blanco | Si | Clase 1 |
| 5 | Cuadrado | 3,8 cm2 | Blanco | No | Clase 1 |

### Tabla 2 (Página 5)

| 2 | Cuadrado | 5 cm2 | Negro | Si | Clase 2 |
| --- | --- | --- | --- | --- | --- |
| 3 | Cuadrado | 5,5 cm2 | Negro | No | Clase 2 |
| 4 | Cuadrado | 3,9 cm2 | Negro | No | Clase 2 |

### Tabla 3 (Página 5)

| 6 | Triángulo | 3,9 cm2 | Negro | Si | Clase 1 |
| --- | --- | --- | --- | --- | --- |
| 7 | Triángulo | 4,6 cm2 | Negro | No | Clase 1 |
| 8 | Triángulo | 3,6 cm2 | Blanco | Si | Clase 1 |
| 9 | Triángulo | 4,2 cm2 | Blanco | No | Clase 1 |

![Imagen](images\page005_img01.png)

---

## Página 6

23/03/2017
6
Particiones
Forma = Círculo
Sombra = Si
Sombra = No
10
Círculo
3,8 cm2
Negro
Si
Clase 2
11
Círculo
3,7 cm2
Blanco
Si
Clase 2
12
Círculo
4 cm2
Negro
No
Clase 1
13
Círculo
3,7 cm2
Negro
No
Clase 1
14
Círculo
3,8 cm2
Negro
No
Clase 1
Árbol
Forma
Sombra
Tono
Clase 1
Cuadrado
Círculo
Triángulo
Clase 2
Clase 1
Clase 2
Clase 1
Si
No
Blanco
Negro

### Tabla 1 (Página 6)

| 10 | Círculo | 3,8 cm2 | Negro | Si | Clase 2 |
| --- | --- | --- | --- | --- | --- |
| 11 | Círculo | 3,7 cm2 | Blanco | Si | Clase 2 |

### Tabla 2 (Página 6)

| 12 | Círculo | 4 cm2 | Negro | No | Clase 1 |
| --- | --- | --- | --- | --- | --- |
| 13 | Círculo | 3,7 cm2 | Negro | No | Clase 1 |
| 14 | Círculo | 3,8 cm2 | Negro | No | Clase 1 |

![Imagen](images\page006_img01.png)

---

## Página 7

23/03/2017
7
7.2. Cálculo de Entropía y Ganancia de información.
El problema consiste en determinar cual de los atributos
estudiantes
(j=1..p-1), caracteriza de mejor forma las
clases Ck.
Considere un problema simple con el factor Vi, que sólo
contiene dos instancias (i=1e i=2) y existen apenas dos
clases (C1 y C2).
Las relaciones entre las instancias de las características Vi
y las clases Ck se pueden relacionar mediante las
probabilidades condicionales entre instancias y clases.
j
iV
Una característica y clase binaria
Si las relaciones se representan en una matriz, se
requiere que sólo un elemento de la fila de la
matriz sea uno, matrices caso ideal.
o
P(v1/c1)
P(v2/c1)
P(v1/c2)
P(v2/c2)
v1
v2
c1
c2




1
0
0
1




0
1
1
0

![Imagen](images\page007_img01.png)

---

## Página 8

23/03/2017
8
Se
mide
la
independencia
de
Vi
y
Ck
mediante
probabilidad conjunta p(vi∩ck) o de juntura p(vi;ck).
Esto es:
– Si son independientes la relación será 1.
– Si
son
completamente
dependientes
p(vi;ck)=p(vi)=p(ck) con lo cual la relación será o
1/p(vi) o 1/p(ck).
Para que esta medida sea cero en el caso de independencia,
se toma el logaritmo en base 2 de la relación, resultando
una medida de información, en bit.
)
c
(
P
)
v
(
P
)
c
;
v
(
p
k
i
k
i
]
bit
[
)
c
(
P
)
v
(
P
)
c
;
v
(
p
ld
k
i
k
i






Esta medida es cero en el caso de ser independientes V y
C.
En el caso de ser completamente dependientes la
información es:
-ld(p(vi)) o
-ld(p(ck)).
Para
cuantificar
la
relación
de
dependencia
entre
cualquiera de los atributos estudiantes Vj y el atributo
experto C, se toma el promedio de la información entre
los atributos.
Este promedio se llama: Ganancia de información.
∑∑






=
i
k
k
i
k
i
k
i
j
c
P
v
P
c
v
p
ld
c
v
p
c
v
Ganancia
)
(
)
(
)
;
(
)
;
(
)
,
(

![Imagen](images\page008_img01.png)

---

## Página 9

23/03/2017
9
Usando
la
definición
de
probabilidad
condicional:
p(vi;ck)=p(ck/vi)P(vi)
se
puede
separar en:
Definiendo
y
(
)
(
)
(
)
(
)
( )
(
)
∑∑
∑∑
−
=
i
k
k
k
i
i
k
i
k
k
i
c
p
ld
c
v
p
v
c
p
ld
c
v
p
C
V
Ganancia
;
/
;
)
,
(
(
)
(
)
(
)
∑∑
=
i
k
i
k
k
i
v
/
c
p
ld
c
;
v
p
α
(
)
( )
[
]
∑∑
=
i
k
k
k
i
c
ldP
c
;
v
p
β
, pero
así
= - información del atributo C.
Aplicando la definición de probabilidad condicional en
α:
( )
(
)
∑
∑
=
k
i
k
i
k
c
;
v
p
c
ldP
β
∑
=
i
k
k
i
)
c
(
P
)
c
;
v
(
p
(
)
∑
k
k
k
c
ldP
)
c
(
P
(
)
(
)
(
)
∑∑
=
i
k
i
k
i
i
k
v
/
c
p
ld
)
v
(
P
v
/
c
p
α
(
)
(
)
(
)
∑
∑
=
i
k
i
k
i
k
i
v
/
c
p
ld
v
/
c
p
)
v
(
P
α
(
)
(
)
(
)
∑∑
=
i
k
i
k
k
i
v
/
c
p
ld
c
;
v
p
α

![Imagen](images\page009_img01.png)

---

## Página 10

23/03/2017
10
Definiendo inf(C/vi) =
,
como la información de la clase C condicionada
(particionada) por la instancia vi del atributo
estudiante Vj.
El promedio de la información de C condicionada
por Vj
será la ponderación de la información
particionada:
Inf(C/V)=
(
)
(
)
(
)
∑
−
k
i
k
i
k
v
/
c
p
ld
v
/
c
p
∑
i
i
i
)
v
/
C
inf(
)
v
(
P
La ganancia (de información) será:
Ganancia(V)= Inf(C)-Inf(C/V)
Realizando
una
analogía
con
el
canal
de
comunicación se tiene que:
Ganancia = I : Información Mutua del Canal
Inf(C)=H(C) entropía del receptor
Inf(C/V) =H(C/V) entropía de error en la recepción
I=H(C) - H(C/V).

![Imagen](images\page010_img01.png)

---

## Página 11

23/03/2017
11
Con esta ganancia es posible determinar cual de
los atributos estudiantes Vj (j=1..p-1) separa o
caracteriza de una forma más adecuada las
clases ck.
Para realizar esto se calcula:
Max (Ganancia(Vj))
j
El atributo j será la raíz del árbol.
Para el ejemplo anterior:
Ganancia(Forma)= Inf(Clase)-Inf(Clase/Forma)
Inf(Clase)= -9/14 ld(9/14) - 5/14 ld(5/14) = 0,94 bit.
Inf(Clase/Forma)= 5/14 (-2/5 ld(2/5) - 3/5 ld(3/5))
+ 4/14 (-4/4 ld(4/4) - 0/4 ld(0/4))
+ 5/14 (-3/5 ld(3/5) - 2/5 ld(2/5))
= 0,694 bit.
Ganancia(Forma)= 0,94 - 0,694 = 0,246

![Imagen](images\page011_img01.png)

---

## Página 12

23/03/2017
12
De
la
misma forma
se
puede
calcular
la
ganancia para los demás atributos estudiantes:
Ganancia(Sombra)= 0,94 - 0,892   = 0,048 bit
Ganancia(Tono)     = 0,94 - 0,8949 = 0,045 bit
Ganancia(Área)      = 0,94 - 0,9371 = 0,0029 bit.
- Modificación de Ganancia
El criterio de ganancia produce buenos resultados para
atributos con cantidades similares números de instancias.
Produce graves distorsiones cuando existen atributos con
diferente numero de instancias.
Si un atributo
(i=1,2,3…n) tiene muchas instancias la
información condicional Inf(C/V), disminuye, aumentando
artificialmente la ganancia.
La ganancia aumenta puesto que:
Ganancia(V)= Inf(C)-Inf(C/V)
j
i
V

![Imagen](images\page012_img01.png)

---

## Página 13

23/03/2017
13
Pero
al
aumentar
las
instancias
también
aumenta
la
información contenida en el atributo (Split information”).
Esto se utiliza para normalizar la Ganancia y generar una
nueva relación denominada Razón de Ganancia.
Así: Split Inf(V) = Inf(V) = H(V)=
Razón Ganancia(V) = Ganancia(V)/Inf(V)
Esta normalización de la ganancia permite eliminar el sesgo
introducido por la medida de información que depende del
número de instancias.
Este factor de corrección puede cambiar la decisión respecto
a los atributos que están mas cercanos a la raíz del árbol.
∑
−
i
i
i
))
v
(
P
(
ld
)
v
(
P
Para el ejemplo anterior:
Split Inf(V) = -5/14 ld(5/14) - 4/14 ld(4/14) - 5/14 ld(5/14)
= 1,577 bit.
la Razón de Ganancia(V) = 0,246/1,577
= 0,156
Razón Ganancia(Sombra)= 0,048/0,98523 = 0,04872
Razón Ganancia(Tono)
= 0,045/0,93977 = 0,04788
Razón Ganancia(Área)
= 0,0029/0,93977 = 0,0031.
Para este caso en particular se mantiene la relación de
importancia de los atributos estudiantes.

![Imagen](images\page013_img01.png)

---

## Página 14

23/03/2017
14
7.3. Poda en árboles de decisión
El método de partición recursiva, continúa subdividiendo
los casos de entrenamiento hasta que cada sub-conjunto
contenga casos de una sola clase o hasta que no existan
mas atributos estudiantes para dividir
El resultado de este proceso es un árbol muy complejo y
muchas
veces
sobre
ajustado
a
los
datos
de
entrenamiento.
La idea básica consiste en remplazar una parte del árbol
por una hoja simple que tenga como clase representante
la clase de mayor frecuencia
En general existen muchas estrategias de poda.
Puede
ser
pre-poda
si
se
realiza
en
la
etapa
de
construcción
del
árbol
o
poda
si
se
realiza
retrospectivamente.
El mecanismo sugerido por Quinlan es la poda, permite
comparar el beneficio de la poda en relación al árbol
original (árbol sobre ajustado).
En el caso de la poda, el árbol de decisión es simplificado
descartando uno o más sub-árboles y reemplazándolo por
hojas.
La clase de la hoja se encuentra buscando los casos de
entrenamiento que se asocian mayoritariamente a una
clase.

![Imagen](images\page014_img01.png)

---

## Página 15

23/03/2017
15
En cada hoja del árbol entrenado se muestra la clase a la
cual se asocia la hoja y la relación (N/E)
N: indica él número total de casos asignados a la hoja
E: número de casos mal clasificados en la clase indicada.
Ej:
Clasificación
de
paciente
según
los
requerimientos
de
enfermería.
Atributos estudiantes:
Tipo de cirugía
{leve, mediana, compleja}
Ambulación
{ayuda, Independiente, camilla}
Dependencia
{auto cuidado, moderado, Intensivo}
Grado de invasión {leve, moderado, grande}
Estado psicológico {tranquilo, irritado, agresivo}
Estado cognitivo
{orientado, desorientado, inconsciente}
Edad
{<50, 50-70, >70}
Atributo experto: 1: baja demanda, 2: alta demanda.
Ej: Requerimientos de enfermería Árbol Entrenado.
Tipo de cirugía = leve
Grado invasión =leve: 1 (151)
Grado invasión =moderado: 1 (1)
Grado invasión =grande
Edad =<50: 1 (6)
Edad =50-70: 1 (9)
Edad =≥70: 2 (1)
Tipo de cirugía = mediana
Ambulación = camilla: 2 (97/3)
Ambulación = ayuda: 2 (4)
Ambulación = independiente
Estado cognitivo = orientado: 1 (2)
Estado cognitivo = desorientado: 2 (1)
Estado cognitivo = inconsciente
Edad =<50: 1 (5/2)
Edad =50-70: 2 (13/2)
Edad =≥70: 1 (1)

![Imagen](images\page015_img01.png)

---

## Página 16

23/03/2017
16
Ej: Requerimientos de enfermería Primera Rama.
El primer sub-árbol
Tipo de cirugía = leve
Grado invasión =leve: 1 (151)
Grado invasión =moderado: 1 (1)
Grado invasión =grande
Edad =<50: 1 (6)
Edad =50-70: 1 (9)
Edad =≥70: 2 (1)
Si se reemplaza esta rama por Tipo de cirugía = leve: 1
(168/1), se cometerá un error de 1 caso al considerarlo
como Tipo 1 cuando es Tipo 2.
Ej: Segunda rama del árbol
Tipo de cirugía = mediana
Ambulación = camilla: 2 (97/3)
Ambulación = ayuda: 2 (4)
Ambulación = independiente
Estado cognitivo = orientado: 1 (2)
Estado cognitivo = desorientado: 2 (1)
Estado cognitivo = inconsciente
Edad =<50: 1 (5/2) (3)
Edad =50-70: 2 (13/2)
Edad =≥70: 1 (1)
Si se reemplaza toda la rama por la hoja Tipo de cirugía
= mediana: 2 (123/11),
se tendrán 11 casos mal
clasificados en contraste a los 7 mal clasificados del
árbol completo.

![Imagen](images\page016_img01.png)

---

## Página 17

23/03/2017
17
Se puede estimar el error en la población con el árbol sin
podar y podado (hoja).
Se usa una distribución de probabilidad conocida con un
cierto límite de confianza.
Hipótesis: La probabilidad de ocurrir E errores en N
ensayos esta dada por una distribución Binomial de
probabilidad p en la población.
B(r,n,p)
E=r el número de errores
N=n el número de ensayos y
p: probabilidad de error esperada en la población.
La densidad está dada por:
Dados n y r, se requiere determinar p para un
cierto nivel de confianza Co%.
Con Co=
esto será PCo(r,n) o PCo(E,N).
Entonces, el número de errores que se tendrá en la
población, para una hoja que en el modelo
clasifica N casos con E errores será:
N x PCo(E,N).
r
n
)
p
1
(
p
r
n
)
r
(
f
−






=
∑
=
r
0
i
)
i(
f

![Imagen](images\page017_img01.png)

---

## Página 18

23/03/2017
18
Quinlan usa un nivel de confianza que denomina
pesimista al 50%, pero como la distribución
Binomial es simétrica, basta con usar Co/2, esto
es un nivel del 25% unilateral.
Para el ejemplo anterior se tiene el siguiente sub-
árbol:
Edad =<50: 1 (6)
Edad =50-70: 1 (9)
Edad =≥70: 2 (1)
La primera hoja: N=6, E=0, de las tablas de la
distribución Binomial P25%(0,6)=0,206.
Si la hoja fuera usada para predecir 6 casos
desconocidos, el error sería: 6x0,206=1,236.
Para la segunda hoja: P25%(0,9)=0,143. Error
población 9x0,143=1,287.
Para la tercera hoja:
P25%(0,1)=0,750. Error población 1x0,75=0,75.
El error para todo el sub-árbol será:
1,236+1,287+0,75=3,273.

![Imagen](images\page018_img01.png)

---

## Página 19

23/03/2017
19
Si este sub-árbol fuera reemplazado por una hoja
correspondiente a la clase Tipo 1 (la más
frecuente), se cubrirían los mismos 16 casos con
un error de un caso.
Su error de predicción sería:
P25%(1,16)= 0,157
El error en la población será:
16x0,157=2,512.
Dado que la hoja presenta un error inferior al sub-
árbol debe ser reemplazado por la hoja de Tipo 1.
Sustituyendo esta hoja, el árbol superior queda:
Grado invasión =leve: 1 (151)
Grado invasión =moderado: 1 (1)
Grado invasión =grande: 1 (16/1)
El número de errores predichos para este árbol
será:
151xP25%(0,151)+1xP25%(0,1)+2,512=4,642.
Si se desea reemplazar este sub-árbol por una hoja
que clasifique en el Tipo 1, el error predicho para
esta hoja será:
168xP25%(1,168)=2,610.
Lo cual es inferior al valor del sub-árbol.
Por lo tanto, el árbol puede ser podado por la hoja
correspondiente.

![Imagen](images\page019_img01.png)

---

## Página 20

23/03/2017
20
7.4. Transformando árboles en reglas
Suponga el siguiente árbol genérico
F  =
0
J =
0:no
J =
1
K =
0: no
K =
1: si
F  =
1
G =
1: si
G =
0
J  =
0: no
J =
1:
K=0: no
K=1: si
Definición: Una regla corresponde a un camino
entre la raíz y cada una de las hojas.
F
G
J
0
1
0
K
K
J
0
0
0
1
1
1
1
1
si
no
0
si
no
no
no
si

![Imagen](images\page020_img01.png)

---

## Página 21

23/03/2017
21
El transcurso entre la raíz y la hoja corresponde a la
condición de la regla, denominado antecedente.
El valor de la hoja es la conclusión de la regla
denominado consecuente.
Si (F=0 ^ J=1 ^ K=1) Entonces si
(F=0 ^ J=1 ^ K=1) Antecedente; si Consecuente
Al tratar de representar todas las posibles reglas que se
representan en un árbol se puede tener una estructura
más compleja que el propio árbol.
Sin embargo es posible observar que el antecedente de
una regla en particular puede contener condiciones
irrelevantes.
Si se examina la rama derecha y la izquierda si
tienen las siguientes reglas
Si (F=0∧J=1∧K=1) entonces la clase es (si)
Si (F=1∧G=1) entonces la clase es (si)
Si (F=1∧G=0∧J=1∧K=1) entonces la clase es (si)
Esta regla puede ser generalizada como:
Si (J=1∧K=1) entonces la clase es (si).
árboles generan reglas redundantes.
¿como se pueden eliminar las condiciones irrelevantes?

![Imagen](images\page021_img01.png)

---

## Página 22

23/03/2017
22
- Reducción de reglas
Sea R una regla que contiene en su antecedente
(A).
R: Si (A) entonces clase (c)
Si se le elimina la condición Ai.
Se tiene una regla (R-) Especializada
R-: Si (A-) entonces clase (c)
La evidencia de la importancia de la condición Ai
debe
ser
encontrada
en
los
casos
de
entrenamiento.
Cada caso en el antecedente generalizado A-
puede pertenecer o no pertenecer a la clase C
Por otro lado puede satisfacer o no satisfacer la
condición Ai.
Esto genera cuatro grupos, que son organizados
en una tabla de contingencia.
Clase C
(casos de A-)
Otras clase
(Casos de A-)
Satisfacen Ai
XP
EP
No satisfacen Ai
XN
EN

### Tabla 1 (Página 22)

| None | Clase C
(casos de A-) | Otras clase
(Casos de A-) |
| --- | --- | --- |
| Satisfacen A
i | X
P | E
P |
| No satisfacen A
i | X
N | E
N |

![Imagen](images\page022_img01.png)

---

## Página 23

23/03/2017
23
Los casos positivos (XP+EP) que satisfacen A- y Ai, son
cubiertos por la regla original R, y los EP son mal
clasificados por la regla R.
Los casos negativos (XN+EN) que satisfacen A-, pero no
satisfacen Ai, pueden ser cubiertos por la regla generalizada
R- pero no por la regla original R. Existen EN errores de
clasificación.
Como la regla generalizada R- cubre todos los casos que
satisfacen a la regla especializada R, el total de casos
cubiertos por R es (XP+EP+ XN+E).
Quinlan propone usar PCo(E,N). Con nivel Co.
-Para la regla especializada R se tiene: PCo(EP, XP+EP).
- Para la regla generaliza R- se tiene:
P-Co(EP+ EN , XP+EP+ XN+EN).
Si P-Co > PCo se elimina Ai.
Permite eliminar una condición Ai
de un
conjunto de antecedentes A.
Si se ordenan todas las posibles condiciones y
sus respectivos errores estimados, es posible
eliminar primero el menor error estimado, para
eliminar la condición que aporta el menor error
estimado.
Luego en una etapa siguiente se calcula nueva
mente los errores estimados para cada una de las
condiciones restantes y se elimina nuevamente
la condición con menor error estimado, y así
sucesivamente.

![Imagen](images\page023_img01.png)

---

