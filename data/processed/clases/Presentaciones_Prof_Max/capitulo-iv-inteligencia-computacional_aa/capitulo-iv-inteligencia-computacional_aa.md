# Capitulo IV Inteligencia Computacional_AA

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23/03/2017
1
Inteligencia Computacional
Capítulo IV
“Análisis de Agrupamientos”
Profesor: Dr. Max Chacón.
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática.
Objetivos
 Establecer diferencias entre agrupamientos jerárquicos
y no jerárquicos
 Comprender los conceptos de similaridad en espacios
n-dimensionales como un concepto de distancia
 Comprender la estructuración de un agrupamiento
jerárquico
 Cuantificar las medidas de similaridad y su aplicación
a la agrupación
 Comprender
los
algoritmos
básicos
de
los
agrupamientos
 Comprender las medidas de calidad para evaluar
agrupamientos.

![Imagen](images\page001_img01.png)

---

## Página 2

23/03/2017
2
3.1. Medidas de Similaridad
 La
medida
fundamental
para
el
agrupamiento, es la similaridad (asociación,
proximidad) o la distancia en ℜn.
 Similaridades:
 Una similaridad debe cumplir las condiciones 
de una distancia (una distancia corresponde a 
una disimilaridad):

No-negatividad: d(x,y) ≥ 0

La distancia de una instancia (observación) 
así misma es  cero,  d(x,x) = 0

Simetría: d(x,y) = d(y,x)

Desigualdad Triangular:      
d(x,y) ≤ d(x,z) + d(z,y)

![Imagen](images\page002_img01.png)

---

## Página 3

23/03/2017
3
Las medidas de similaridad más conocidas son
las de distancia.
Para dos vectores
e
∈ℜn
dependiendo del valor de p se generan los
siguientes casos particulares
- p=1 Distancia de Manhattan (block):
- p=2 Distancia Euclidiana:
∑
=
−
=
−
n
i
i
i
y
x
y
x
1
v
v
∑
=
−
=
−
n
i
i
i
y
x
y
x
1
2
v
v
- p→∞Distancia de Schebyshev:
Otras sin ponderar:
Distancia de Camberra:
i
i
n
i
y
x
y
x
−
=
−
=
...
2,1
max
v
v
∑
=
+
−
=
n
i
i
i
i
i
Camb
y
x
y
x
D
1

![Imagen](images\page003_img01.png)

![Imagen](images\page003_img02.png)

---

## Página 4

23/03/2017
4
- Distancias
de
formas
cuadráticas,
la
más
general es la distancia de Mahalanobis:
con M una matriz definida positiva.
 La principal característica de esta distancia es
que
representa
las
interrelaciones
entre
las
características individuales. Pero no es fácil
obtener un escalamiento adecuado cuando las
componentes
están
representadas
en
rangos
diferentes.
)
(
)
(
1
y
x
M
y
x
y
x
T
v
v
v
v
v
v
−
−
=
−
−
-Distancia de Bhattaharaya
Con:
Si M=I la distancia es la Euclidiana.
- Distancia de Hamming (caso binario)
Sea x e y dos vectores binarios del mismo largo 
(n).
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
−
−
−
−
2
2
2
2
1
1
0
0
0
...
0
0
...
0
n
M
σ
σ
σ
∑
=
−
=
−
n
i
i
i
i
y
x
y
x
1
2
2)
(
σ
v
v
∑
=
⊕
n
i
i
i
y
x
1

![Imagen](images\page004_img01.png)

---

## Página 5

23/03/2017
5
Es importante notar que todas las funciones de
distancia tienden a un modelo de región convexa
en el espacio n-dimensional de las características.
Medidas de Correlación:
- Correlación de Pearson (r)   [-1,1]
y
y
x
x
y
y
x
x
r
r
r
r
r
r
r
r
−
−
−
−
)
(
)'
(
∑
∑
∑
=
=
=
−
−
−
−
=
n
i
i
n
i
i
n
i
i
i
y
y
x
x
y
y
x
x
y
x
r
1
2
1
2
1
)
(
)
(
)
)(
(
)
,
(
r
r
•Correlación de Spearman (r) (variables 
cuantitativas y ordinales)     [-1,1]
•Para calcular d se parean las dos variables, luego 
una es ordenadas en rangos (ej: se ordena x, menor 
valor de x se asigna 1, al segundo 2, etc), la 
segunda variable (y) se le asignan los rangos 
correspondientes a sus valores, el valor d será la 
diferencia entre los rangos de x e y. Cuando hay 
valores iguales se toma el promedio entre rangos 
consecutivos.
)1
(
6
1
)
,
(
2
1
2
−
−
=
∑
=
n
n
d
y
x
n
i
i
r
r
ρ

![Imagen](images\page005_img01.png)

---

## Página 6

23/03/2017
6
- Correlación de Cramer (V)      [0,1]
c2: diferencias al cuadrado entre valores 
observados y esperados de la tabla de contingencia 
general, tamaño rxs.
q: mínimo entre las filas y columnas de la tabla 
de contingencia min{r,s}.
n: total de casos.
Otros: 
- Correlación de Kendall (t)
- Coeficiente de Goodman-Kruskal (g)
)1
(
)
,
(
2
−
=
q
n
y
x
V
χ
r
r
Similaridad de variables binarias:
Se usa como base la tabla de contingencia de 2x2
- Euclidiana binaria:    Eb(x,y) =
- Diferencia de tamaño: Dt(x,y)= 
x
¬x
y
a
b
¬y
c
d
c
a +
2
2
)
(
)
(
d
c
b
a
c
b
+
+
+
−

### Tabla 1 (Página 6)

|  | x | ¬x |
| --- | --- | --- |
| y | a | b |
| ¬y | c | d |

![Imagen](images\page006_img01.png)

---

## Página 7

23/03/2017
7
-Diferencia de tamaño: 
Dt(x,y)  = 
-Diferencia de configuración:
- DCb(x,y) =   
[0,1]
-Varianza binaria:  
-Vb(x,y)  =
2
2
)
(
)
(
d
c
b
a
c
b
+
+
+
−
2)
(
d
c
b
a
bc
+
+
+
2)
(
4
d
c
b
a
c
b
+
+
+
+
- Dispersión:  Db(x,y)  =          
[0,1]
- Coeficiente Pi: p(x,y) = 
esta similaridad es la versión binaria del 
coeficiente de correlación de Pearson.
2)
(
d
c
b
a
bc
ad
+
+
+
−
)
)(
)(
)(
(
d
c
d
b
c
a
b
a
bc
ad
+
+
+
+
−

![Imagen](images\page007_img01.png)

---

## Página 8

23/03/2017
8
- Coeficiente de Hamann: H(x,y) =  
[-1,1]
-Coeficiente de Jaccard:  J(x,y) =  
- Ochiai:   Och(x,y)=      
•
[0,1] 
versión binaria del coseno.
)
(
)
(
)
(
d
c
b
a
c
b
d
a
+
+
+
+
−
+
c
b
a
a
+
+
)
)(
(
c
a
b
a
a
+
+
Para un conjunto de características son ordenadas en
una matriz de similaridad (o disimilaridad) que será
una matriz triangular (pxp) donde los pares (fila,
columna)
representan
las
relaciones
entre
las
características del conjunto de datos.
Las matrices de similaridad son el insumo para aplicar
los algoritmos de agrupamientos y contienen toda la
información
necesaria
respecto
de
los
objetos
o
patrones que serán agrupados.
Los principales objetivos del análisis de agrupamiento
son:
– Exploración de Datos.
– Reducción de Datos.
– Predicciones basadas en grupos establecidos.

![Imagen](images\page008_img01.png)

---

## Página 9

23/03/2017
9
Los métodos de agrupamientos se pueden dividir
en:
– Agrupamiento Jerárquico
– Agrupamiento no Jerarquico.
3.2. Agrupamiento Jerárquico
La metodología jerárquica trabaja con los datos de
entrada previamente normalizados y dispuestos
sobre vectores o matrices de datos.
Se intenta formar estructuras en forma de árboles
que establecen las relaciones entre los datos.
La forma de representación se denomina árbol jerárquico o 
dendrograma.
Las entidades de la raíz representan toda la colección de
datos indistintamente.
En la dirección ascendente aparecen las relaciones que se
van estableciendo entre los datos para formar grupos.
x1
x2
x3
x4
x5

![Imagen](images\page009_img01.png)

---

## Página 10

23/03/2017
10
Un árbol jerárquico es una secuencia anidada de
particiones de los individuos en g grupos, donde
g varía de 1 a n.
Las
particiones
se
desarrollan
en
orden
ascendente.
Un árbol es una familia de grupos donde cada
rama contiene cierto número de nodos. Cada
nodo
desciende
de
una
rama
y
así
sucesivamente. Ninguna línea que forme el árbol
debe interceptarse.
Distancias
entre
grupos
x1 x2 x3
x4
x5
x6    x7
x8 x9 x10
x11    x12     x13
10
8
0
3
4
7

![Imagen](images\page010_img01.png)

---

## Página 11

23/03/2017
11
Al considerar una cierta distancia, como por
ejemplo 7, se observan tres grupos bien definidos.
Los individuos se encuentran muy cercanos unos
con otros dentro de cada agrupación.
– Primero se agrupan todos los individuos a
distancias menores que 3.
– Luego los individuos o grupos a distancias
entre 3 y 4.
– Se repite el proceso anterior para distancias
superiores.
Algoritmo:
1. Comenzar con n grupos, donde cada uno de
los grupos sólo contiene un individuo.
2. Unir los dos individuos más cercanos (Ej:
individuos i y j, en grupo simple k). Por lo
tanto ahora se encuentran (n-1) grupos.
3. La diferencia entre este nuevo grupo a
cualquier otro individuo t, es definida como:
min(
).
t
k
x
x
v
v −
Método principal para la construcción de los
árboles jerárquicos. También se denomina
agrupamiento por vecinos.

![Imagen](images\page011_img01.png)

---

## Página 12

23/03/2017
12
Algoritmo:
4.
Unir los dos grupos más cercanos, pero
considerando el grupo formado en el paso ii).
5.
Construir una nueva diferencia entre los
grupos que quedaron al realizar los pasos
anteriores esto es (n-2) grupos.
6.
Continuar combinando los grupos, siempre
reduciendo el número de los grupos en uno y
la diferencia resultante entre los nuevos
grupos
es
definida
nuevamente
por
los
grupos más cercanos.
7.
Repetir los pasos anteriores hasta obtener la
cantidad de grupos deseados.
Notar que la agrupación se va realizando al reducir
los grupos de uno en uno (unión simple).
Los diferentes algoritmos que se obtienen con esta
técnica sólo varían en la forma de seleccionar las
distancias (paso iii).
En general existen tres formas de seleccionar las
distancias:
t
k
x
x
v
v −
Distancia mínima min(                )
Conjunto K
Conjunto T

![Imagen](images\page012_img01.png)

---

## Página 13

23/03/2017
13
t
k
x
x
v
v −
Distancia mínima max(                )
Conjunto K
Conjunto T
Conjunto K
Conjunto T
Distancia promedio
∑
∈
∈
−
=
T
x
K
x
t
k
kt
t
k
x
x
T
car
K
car
d
v
v
)
(
)
(
1
Estos algoritmos son denominados “algoritmos
aglomerativos”. Puesto que usan una serie de
uniones
entre
los
vecinos
próximos,
comenzando desde n grupos hasta terminar
formando sólo un grupo de los n individuos.

![Imagen](images\page013_img01.png)

---

## Página 14

23/03/2017
14
3.3. Algoritmo de la k medias
Los métodos no jerárquicos se caracterizan porque
el número de grupos es determinado previamente e
ingresado
como
parámetro
al
sistema
de
clasificación (ingresado por el usuario).
Las ideas centrales son:
– Escoger una partición inicial de los datos y luego
alterar los miembros de los grupos para obtener
nuevas (mejores) agrupaciones.
– Escoger una partición y asignar a la partición un
representante llamado centroide de la misma.
Básicamente existen dos formas para escoger el
centroide:
– Determinar el promedio entre los integrantes de
cada grupo y el dato que más se asemeje a él,
exponerlo como centroide del grupo.
– Calcular la media entre los integrantes de cada
grupo y este valor exponerlo como centroide.

![Imagen](images\page014_img01.png)

---

## Página 15

23/03/2017
15
La elección adecuada dependerá del problema al
cual se enfrente y del algoritmo que se escoja
para efectuar el agrupamiento.
El creador del método MacQueen (1967) usa el
término de k-medias para denotar a un proceso
que forma k grupos usando distancias mínimas
entre los n datos de entrada y los centroides o
medias de cada grupo.
i.
Formar k agrupaciones con los datos
de entrada en forma aleatoria.

![Imagen](images\page015_img01.png)

---

## Página 16

23/03/2017
16
ii.
Determinar el centroide ck de cada grupo
calculando la media entre los integrantes
del grupo .
iii.
Calcular la distancia entre un patrón xi y
los centroides ck , dik para k=1,2,…K.
iv.
Asignar
el
patrón
xi
al
grupo
cuya
distancia al centroide fue menor. Esto es:
))
(
arg(
...
ik
K
k
d
min
k
1
0
=
=
d
d

![Imagen](images\page016_img01.png)

![Imagen](images\page016_img02.png)

---

## Página 17

23/03/2017
17
v.
Después de
cada
asignación,
recalcular
el
centroide del grupo al cual se le adhirió un
nuevo integrante o perdió uno.
vi.
Repetir los pasos iii) al v) hasta que no ocurra
ningún cambio en el sentido de que no emigren
datos a otros grupos o no se muevan los
centroides.
El esfuerzo total desde la configuración inicial 
hasta la agrupación final, está dado por los 
siguientes valores:
–
k(2n – k) iteraciones.
–
(k –1)(2n – k) comparaciones.
–
n – k actualizaciones de los centroides.
Los estudios de la influencia del ordenamiento 
inicial de los datos muestran que este orden tiene 
un efecto pequeño al tratarse de agrupaciones 
muy separadas.

![Imagen](images\page017_img01.png)

![Imagen](images\page017_img02.png)

---

## Página 18

23/03/2017
18
Usando conjuntos de prueba, los autores
muestran que el orden en los datos de
entrada no altera más que un 0.07% el
agrupamiento
entre
un
tipo
de
ordenamiento inicial y otro.
El método converge a un mínimo local.
MacQueen
propuso
una
variación
al
algoritmo de las k-medias, basado en la
adaptación del número de grupos desde la
asignación inicial hasta los resultados finales.
Usa como punto de partida la agrupación
realizada por el algoritmo de las k-medias.
Adicionalmente
al
parámetro
k
usa
los
parámetros de Cohesión Co y de Refinamiento
Re.

![Imagen](images\page018_img01.png)

---

## Página 19

23/03/2017
19
3.4. Algoritmo de las k Medias adaptivo
Sea
el centroide del grupo i .
El parámetro de cohesión será:
El parámetro de Refinamiento será:
(promedio entre centroides)
icr
j
i
j
i
c
c
min
Co
v
v −
=
∀,
ij
d
=
Re
Algoritmo
El primer paso corresponde al último paso de
las k-medias.

![Imagen](images\page019_img01.png)

![Imagen](images\page019_img02.png)

---

## Página 20

23/03/2017
20
i.
Se
recalculan
las
distancias
de
los
centroides a cada sujeto (pt).
–
Si d(ci,pt)<Co ⇒se juntan al grupos,
asignar los restantes patrones a los
grupo más cercanos.
–
Si d(ci,pl)≥Re ⇒se genera un nuevo
grupo, con un solo patron inicialmente
d >Re
d <Co
Nuevo 
grupo
ii.
Después
de
reasignar
patrones
se
recalculan los centroides de cada uno de los
grupos.
iii.
Repetir los pasos I y II hasta que no existan
más modificaciones

![Imagen](images\page020_img01.png)

![Imagen](images\page020_img02.png)

---

## Página 21

23/03/2017
21
iv.
Al permitir que los grupos con centroides
cercanos se unan, el método evita crear
distinciones que dividan artificialmente a los
grupos.
v.
Mediante la creación de nuevos grupos es
posible observar una mejor distribución de
los grupos, puesto que puntos alejados no
son forzados a pertenecer a algún grupo
establecido.
vi.
Al utilizar esta modificación al algoritmo de
las k-medias puro se elimina la restricción
de obtener k grupos y la cantidad de grupos
en general aumenta, pero las distribuciones
son mejores.
vii. Al ejecutar este algoritmo con distintos
valores para los parámetros C y R, se
puede observar que la relación de los
parámetros R y C es importante y se
logran mejores agrupaciones cuando R >
C.

![Imagen](images\page021_img01.png)

---

## Página 22

23/03/2017
22
3.5.
Evaluación
de
los
métodos
de
agrupamientos
En general los métodos no-jerárquicos se pueden evaluar
usando algún criterio de optimalidad (minimización)
para las estructuras de grupos resultantes.
La forma más común es adoptar una suma de  las 
varianzas ponderadas.
∑∑
∑∑
=
=
=
=
=
−
=
k
1
i
n
1
j
2
ij
ij
k
1
i
n
1
j
2
i
j
ij
d
u
c
x
u
Q
r
r
Donde:
• k número de grupos.
• n número de patrones.
• uij son los elementos de la matriz de particiones U que
almacena los resultados de los agrupamientos al interior de los
grupos.
•
centroide del grupo j.
jcr
Los elementos de esta matriz satisfacen las
siguientes condiciones:
– uij∈{0,1}
–
para i=1,…,k
–
para j=1,…,n
Existen
varios
índices
para
evaluar
la
clasificación. Mediante estos índices es posible
obtener el número k que se considera como un
parámetro inicial en el método de las k medias
puros.
∑
=
<
<
n
1
j
ij
n
u
o
1
u
k
1
i
ij =
∑
=

![Imagen](images\page022_img01.png)

---

## Página 23

23/03/2017
23
También es posible usar estos métodos u otros
similares para decidir el nivel de corte de los
algoritmos aglomerativos.
– Fukuyama y Sugeno, 1989
Con
el centroide de la totalidad de los datos.
∑∑
=
=




−
−
−
=
k
1
i
n
1
j
2
i
2
i
j
ij
FS
c
c
c
x
u
)
U
(
Ind
r
r
r
r
cr
– Xie y Beni, 1991
Existe una infinidad de variaciones de estos métodos 
y sistemas híbridos que incluyen clasificación 
Bayesiana, conjuntos difusos, conjuntos rugosos y 
otros.
j
i
j,i
k
1
i
n
1
j
2
i
j
ij
XB
c
c
min
  
n
c
x
u
)
U
(
Ind
r
r
r
r
−
−
= ∑∑
=
=

![Imagen](images\page023_img01.png)

---

## Página 24

23/03/2017
24
Una aplicación muy utilizada actualmente es la
introducción de una variable de contexto que es
asociada a cada patrón.
Con esto es posible realizar el agrupamiento en
función de las variables de contexto. En este caso
el proceso de minería basado en el agrupamiento
actúa como un filtro al focalizarse en un conjunto
específico de datos.
También es posible relacionar los patrones con
características semánticas para realizar búsquedas
inteligentes en texto.

![Imagen](images\page024_img01.png)

---

