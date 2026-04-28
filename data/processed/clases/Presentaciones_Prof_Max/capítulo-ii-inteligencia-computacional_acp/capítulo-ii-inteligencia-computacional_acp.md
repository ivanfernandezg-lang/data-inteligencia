# Capítulo II Inteligencia Computacional_ACP

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23/03/2017
1
Inteligencia Computacional
Capítulo II
“Análisis de Componentes principales”
Profesor: Dr. Max Chacón
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática.
x1
x2
x3
y1
y3
y2
α2
α1
α3

![Imagen](images\page001_img01.png)

![Imagen](images\page001_img02.png)

---

## Página 2

23/03/2017
2
Se requiere una transformación (yi) que ubique el
primer eje en el sentido de la mayor dispersión de
puntos, luego el segundo eje en la dirección de la
segunda dispersión y así sucesivamente.
Esto permitirá representar de mejor forma la
varianza del conjunto de datos y, eventualmente,
eliminar las componentes de orden mayor que
representen
una
menor
varianza,
lo
cual
es
equivalente a contener menor información.
De geometría analítica se tiene que para una
transformación ortonormal, los ángulos ai son los
cosenos directores de la transformación:
a11 = cos a1 ;
a12 = cos a2 ;
a13 = cos a3
para una transformación ortonormal
Entonces, un nuevo punto (rotado en torno a las
medias) en las coordenadas yi será:
1
2
13
2
12
2
11
=
+
+
a
a
a
)
(
)
(
)
(
13
3
13
2
2
12
1
1
11
1
x
x
a
x
x
a
x
x
a
y
−
+
−
+
−
=

![Imagen](images\page002_img01.png)

---

## Página 3

23/03/2017
3
De esta forma la dispersión de los datos en torno a las
nuevas componentes tendrá una distribución decreciente.
y1
σ2
1
y2
σ2
2
y3
σ2
3
- Cálculo algebraico.
Se
tiene
una
matriz
X
de
datos
con
p
columnas
(componentes de cada caso) y n filas (número de casos).
Se requiere disminuir la dimensión p del vector
que
representa cada caso a una dimensión q, con q<p y perder la
mínima cantidad de información.
Si se trunca directamente el vector
se producirá un error
cuadrático medio igual a la suma de las varianzas de los
elementos eliminados de
.
ixv
ixv
ixv

![Imagen](images\page003_img01.png)

![Imagen](images\page003_img02.png)

---

## Página 4

23/03/2017
4
Se requiere una transformación lineal e invertible T tal que
al truncar T
se produzca una mínima pérdida de varianza.
Se requiere una transformación ortonormal que minimice la
varianza de los nuevos yi para poder truncarlos.
El problema de optimización será:
Dada la combinación lineal:
minimizar
var(
)
s.a.
ixv
X
a
x
a
x
a
x
a
y
j
p
pj
j
j
j
v
v
v
v
v
=
+
+
+
=
...
2
2
1
1
jyv
ij
j
T
i a
a
δ
=
v
v
Sol: Suponiendo que la media de las nuevas componentes
es cero, esto es E[
]=0
var(
) = E[        ] 
Pero, de la transformación
Se tiene:
var(
) = E[                 ]
var(
) =       E[X XT]  
Donde E[XXT] es la matriz de varianzas y co-varianzas, en
el caso que los
estén centrados en la media, es la matriz
de correlación R=E[XXT]
j
av
X
a
y
j
j
v
v =
jyv
jyv
T
jyv
jyv
j
T
T
j
a
X
X
a
v
v
 
T
jav
jyv
jyv
ixv

![Imagen](images\page004_img01.png)

---

## Página 5

23/03/2017
5
Así: Var(
) =
R
Para resolver el problema de optimización con restricciones
se hace uso del Lagranjeano aumentado, esto es, incluir las
restricciones igualadas a cero, ponderadas por una constante
(λj), en la función objetivo.
L(     ) =     R     - λj(            )
Para minimizar
, Usando la derivada de una
forma cuadrática
o
Esta ecuación corresponde al problema de los valores
propios de la matriz R.
0
)
(
=
−
j
j
j
a
I
R
v
λ
0
=
−
j
j
j
a
I
a
R
v
v
λ
0
)
(
=
∂
∂
j
j
a
a
L
v
v
1
−
j
T
j a
a v
v
j
av
T
jav
j
av
j
av
T
jav
jyv
Tiene solución para
≠0 para valores especiales λj
denominados valores propios de R. Los
son los vectores
propios de R.
Si los
son vectores columna al colocarlos en una matriz,
esta será la matriz de transformación
Como la matriz de correlación es simétrica y de valores
reales
positivos,
sus
valores
propios
serán
reales
y
positivos.
Matricialmente:
RT=TL
[
]
p
i
a
a
a
T
v
v
v
, 
...
 ,
,
2
=
j
av
jav
jav

![Imagen](images\page005_img01.png)

---

## Página 6

23/03/2017
6
Con L la matriz de valores propios:
Como
los
vectores
de
T
satisfacen
la
condición
de
ortonormalidad
, entonces TTT=I, esto es TT=T-1.
Pre multiplicando por TT la forma matricial se tiene que:
TTRT=L y en términos vectoriales
R
= λj
Como var(yj)=
R
entonces var(yj)=λj










=
Λ
p
λ
λ
0
0
0
.
0
0
0
1
ij
j
T
i a
a
δ
=
v
v
j
av
T
jav
jav
T
jav
Esto significa que si se ordenan los valores propios en
forma decreciente, es posible obtener lo buscado:
λ1>λ2>λ3> … >λp
Con λ1 el valor propio de mayor valor asociada a la
primera componente principal yi
Si la matriz R es la matriz de correlación entonces los
valores propios son normalizados y
.
Esto significa que cada λi representa un porcentaje de la
varianza de las nuevas coordenadas yi.
∑
=
=
p
i
i
P
1
λ

![Imagen](images\page006_img01.png)

---

## Página 7

23/03/2017
7
Para obtener el vector original basta con multiplicar por la
matriz de transformación transpuesta.
Como Y=TTX al pre-multiplicar por T se tiene: X=TY.
Los
son llamadas las componentes principales y tienen la
misma dimensión que el vector original
.
xv
jyv
- Reducción de dimensionalidad.
Debido a que las componentes principales ahora están
ordenadas en orden decreciente de varianza es posible
eliminar las últimas perdiendo el mínimo de información.
La información esta representada por los valores propios λj.
Si se reduce la dimensión a un punto q<p el error cometido
al truncar en la componente q se puede evaluar sumando la
contribución de las componentes eliminadas
∑
+
=
=
p
q
i
i
P
e
1
100
%
λ

![Imagen](images\page007_img01.png)

---

## Página 8

23/03/2017
8
Este valor esta dado en % si los vectores y valores propios
son extraídos de la matriz R. Si son extraídos de la matriz de
varianzas-covarianzas S , se requiere dividir la suma valores
propios para obtenerlos en porcentaje.
Una forma de examinar el error cometido es obtener la
estimación del vector
después de haber truncado en q las
componentes de los vectores
.
p
q
con
a
y
x
q
i
i
i
<
=∑
=
  
  
ˆ
1
v
v
v
jyv
xˆv
El problema de determinar el valor q en general depende
del problema, puesto que al reducir q se reduce la
dimensionalidad del nuevo espacio de características pero
también aumenta la perdida de información.
Una forma de encontrar un valor para q es graficar la
varianza acumulada en función de q de las componentes
principales.

![Imagen](images\page008_img01.png)

---

## Página 9

23/03/2017
9
Esto es
Debido a que la disminución de los valores propios no
tiene porque ser monótona es posible encontrar un punto
en que el aporte de las últimas componentes sea poco
significativo.
Va(%)
q
 
(%)
1∑
=
=
q
i
i
Va
λ

![Imagen](images\page009_img01.png)

![Imagen](images\page009_img02.png)

---

