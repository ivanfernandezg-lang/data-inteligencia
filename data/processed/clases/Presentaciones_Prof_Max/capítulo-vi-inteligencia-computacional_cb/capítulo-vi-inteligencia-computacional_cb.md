# Capítulo VI Inteligencia Computacional_CB

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23/03/2017
1
Inteligencia Computacional
Capítulo VI
“Clasificación Bayesiana”
Profesor: Dr. Max Chacón.
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática
Objetivos
• Cuantificar probabilidad a priori.
• Comprender el costo del error de clasificar
basado en probabilidad a priori.
• Cuantificar el riesgo condicional.
• Usar los conceptos anteriores para obtener un
método
de
clasificación
a
mínimo
riesgo
condicional para un problema multivariado.
• Analizar clasificador Bayesiano simple.
• Obtener un
clasificador mediante
criterio
distribuido, usando el concepto de redes de
clasificación.

![Imagen](images\page001_img01.png)

---

## Página 2

23/03/2017
2
5.1. Clasificación a priori
Supongamos que se requiere clasificar pacientes
que recurren al médico con dolor pectoral, en
pacientes que han sufrido un infarto cardiaco y los
que su dolor es por otra causa.
De un número grande de observaciones n, se puede
obtener que una fracción de ellos n1 pertenece a la
clase c1 (pacientes con infarto) y la fracción n2
pertenece a la clase c2 (pacientes sin infarto)
Con:
n=n1+n2
La probabilidad a priori p(ci) será la
probabilidad de que el próximo paciente
se clasifique en la clase ci.
con i=1,2.
Para un número grande de observaciones
se puede estimar p(ci) por:
n
n
lim
)
c
(
p
i
n
i
∞
→
=
n
n
)
c
(
pˆ
i
i =

![Imagen](images\page002_img01.png)

---

## Página 3

23/03/2017
3
Las probabilidades p(c1) y p(c2) representan el
conocimiento a priori (en términos estadísticos)
de que un paciente tenga infarto o no, antes de
que exista el nuevo paciente a clasificar.
Suponiendo que, basado en estas probabilidades
(pequeño conocimiento) se quiere clasificar un
nuevo paciente, la mejor elección será aquella
que asigna el paciente a la clase que tenga mayor
probabilidad a priori.
Asignar paciente a la clase c2 si p(c2) > p(c1)
En otro caso asignar a c1.
Para un sujeto en particular, la probabilidad
de error de la clasificación será:
p(error de clasificación)=
Se observa que el error de clasificación es
minimizado si se elige c2 y p(c2) > p(c1).



=
=
2
1
1
2
c
C
decide
se
si
)
c
(p
c
C
decide
se
si
)
c
(p

![Imagen](images\page003_img01.png)

---

## Página 4

23/03/2017
4
4.2. Clasificación condicionada
Para tomar una decisión más informada es
necesario usar alguna característica relevante del
paciente que permita distinguir su enfermedad.
Considérese
que
el
médico
tratante
solicita
examen CKMB, que la fracción MB del nivel
Sérico de la enzima Creatinin Fosfokinasa CK
para detectar infarto al miocardio.
Considere x la fracción del nivel sérico de la
enzima. El valor de x debe ser considerado como
una variable aleatoria que puede ser expresada en
términos
probabilísticos
(también
influye
el
tiempo).
El interés será contar con funciones de densidad
de probabilidad condicionales p(x/ci), con i=1,2.
Sea c1 paciente con infarto, c2 sin infarto
p(x/c1) es la función de densidad de probabilidad
para un valor de x dado que el paciente presenta
infarto.
x
p(x/c2)
p(x/c1)
Densidad
Probabilidad

![Imagen](images\page004_img01.png)

---

## Página 5

23/03/2017
5
Esta función de densidad de probabilidad es
llamada Verosimilitud de la clase c1 con respecto
a x y refleja el conocimiento que se tiene de la
aplicación de esta función, la cual sugiere que la
verosimilitud de que un paciente pertenezca a la
clase c1 es grande si p(x/c1) es grande.
Nota: si las dos funciones de distribución están
superpuestas, significa que el conocimiento de la
variable x no discrimina entre sano y enfermo.
Para clasificar el paciente en la clase ci se
requiere reunir el conocimiento a priori p(ci) y el
conocimiento de los valores de x para los
pacientes que pertenecen a las clases ci , p(x/ci).
Para clasificar un paciente dado se requiere la
probabilidad
a
posteriori
p(ci/x),
la
cual
especifica la probabilidad de que el sujeto
pertenezca a la clase ci dado que el valor del
nivel sérico es x.
Tener el valor de x dependerá del hecho
posterior de que la variable de características x
sea medida.
Para dos clases se tiene:
Para obtener el valor de p(ci/x), se requiere
conocer
las
relaciones
de
probabilidades
condicionales.
∑
=
=
2
1
i
i
1
)
x
/
c
(
p

![Imagen](images\page005_img01.png)

---

## Página 6

23/03/2017
6
Sea:
p(ci;x)
la
función
de
densidad
de
probabilidad
conjunta,
p(ci∩x)
que
es
interpretada como la probabilidad de que un
paciente pertenezca a la clase ci y tenga un nivel
sérico x.
De la definición de probabilidad condicional:
p(x) es la probabilidad incondicional de la
variable x.
.2,1
i
   
con
     
)
x
(
p
)
x
/
c
(
p
)
x
;
c
(
p
i
i
=
=
.2,1
i
   
con
     
)
c
(
P
)
c
/
x
(
p
)
x
;
c
(
p
i
i
i
=
=
∑
=
=
2
1
)
(
)
/
(
)
(
i
i
i
c
P
c
x
p
x
p
Usando las definiciones anteriores se tiene el
Teorema de Bayes;
Por lo tanto para conocer p(ci/x) se requiere el
conocimiento a priori y el conocimiento de la
verosimilitud de las clases ci respecto a x.
∑
=
=
2
1
)
(
)
/
(
)
(
)
/
(
)
/
(
i
i
i
i
i
i
c
P
c
x
p
c
P
c
x
p
x
c
p

![Imagen](images\page006_img01.png)

---

## Página 7

23/03/2017
7
5.3. Minimización del Riesgo Condicional
“Un nuevo paciente al cual se han practicado el
examen CKMB con un resultado x, se asigna a la
clase ci que tenga el mayor valor de P(ci /x)”.
A esta regla se le denomina Maximización de la
Probabilidad (o hipótesis) a Posteriori (MAP).
O
En
otras
palabras:
La
regla
de
clasificación
estadística indica que la mejor clasificación será
aquella que minimice la probabilidad de error en la
clasificación (Regla de Clasificación Bayesiana).
{
})
/
(
max
arg
x
c
p
Clase
i
c
MAP
i
=
{
})
(
)
/
(
max
arg
i
i
c
MAP
c
p
c
x
p
Clase
i
=
Se decide por la clase c1 si:
Se decide por la clase c2 si:
Usando
la
función
de
distribución
de
probabilidad a posteriori se puede observar el
punto óptimo de discriminación.
)
)P(c
 p(x /c
)
)P(c
p(x /c
p(x)
)
)P(c
p(x/c
p(x)
)
)P(c
p(x/c
/x)
p(c
/x)
p(c
2
2
1
1
2
1
2
1
2
1
>
>
⇒
>
)
)P(c
 p(x /c
)
)P(c
p(x /c
1
1
2
2
>

![Imagen](images\page007_img01.png)

---

## Página 8

23/03/2017
8
Se denomina Función Discriminante a:
Si se tienen múltiples (m) clases
con: i=1,2,… m
Como di(x) se compara con los otros dj(x),
j=1,2,…,m, el factor de escala p(x) no necesita
ser considerado.
di(x) = p(x/ci)P(ci)
x
p(x/c2)p(c2)
p(x/c1)p(c1)
Densidad
Probabilidad
Punto de 
Discriminación
Áreas de mínimo error
)
(
)
(
)
/
(
)
/
(
)
(
x
P
c
P
c
x
p
x
c
P
x
d
i
i
i
i
=
=
En general di(x) es una función monótona respecto
de x y se puede usar ln(di(x))=Li(x) obteniendo los
mismos resultados.
Li(x)=ln p(x/ci)+ln p(ci)
La elección de la clase se realiza maximizando la
probabilidad a posteriori (MAP).
{
})
(p(c
))
(p(x/c
Clase
i
i
c
MAP
i
ln
ln
 
max
 
arg
+
=

![Imagen](images\page008_img01.png)

---

## Página 9

23/03/2017
9
Ej: Considere un paciente que recibe un examen CKMB
con valor 15% (<10% normal, a las 7 horas) y se quiere
saber si realmente tiene infarto. De las bases de datos del
hospital se sabe que:
- De los pacientes que consultan por dolor agudo al pecho y
se les envía a realizar el examen CKMB, el 60%
tuvo
infarto realmente.
- Además se sabe que el 1% de los pacientes con infarto
tenia un valor de 15% de la fracción CKMB y que solo el
0,3% de los que no tuvo infarto tenían un valor de 15% de
la encima.
Determine si el paciente tiene o no infarto realmente.
Sol: P(I)=0,6; P(
)=0,4;
p(x=15%/I)=0,01;
p(x=15%/ )=0,003.
arg max {p(I/x=15%); p( /x=15%}=
arg max {
}=
arg max{0,006;0,0012}=arg {0,006}= clase I
∴El paciente tiene infarto.
)
I
(
P
)
I
/
%
15
x
(
p
);
I
(
P
)
I
/
%
15
x
(
p
=
=
I
I
I

![Imagen](images\page009_img01.png)

---

## Página 10

23/03/2017
10
5.4. Clasificación Multivariada
Se tienen n pacientes portadores de diferentes
enfermedades y se requiere clasificarlos en m
clases c1, c2, … ,cm (enfermedades y caso
normal) las cuales se dan en proporciones a
priori p(c1), p(c2), … ,p(cm), y se poseen p
características de los pacientes representadas en
el vector de valores reales
=[x1,x2,…xp].
Si la muestra utilizada es significativa, se puede
suponer que la distribución de las variables
aleatorias
es
una
distribución
normal
multivariada.
xv
xv
En este caso, la probabilidad de obtener un
paciente con características
que pertenezca a
la clase ci es:
donde:
= estimación del vector de medias de
las p características de la clase ci.
Σi: Matriz de varianzas-covarianzas de la
clase ci.
)ˆ
(
)ˆ
(
)
(
)
(
/
/
µ
µ
π
v
v
v
v
v
−
Σ
−
−
Σ
=
−
x
x
2
1
2
1
c
x
p
1
i
T
e
2
1
i
2
p
i
xv
µ
v
ˆ

![Imagen](images\page010_img01.png)

---

## Página 11

23/03/2017
11
Considerando el estudio univariado, lo que se
requiere es:
Dado un paciente que posee un vector de
características
, determinar la clase a la cual
pertenece el paciente,
.
Definiendo la probabilidad a como la función
discriminante
y
su
logaritmo
xv
)
(
x
c
p
i
v
{
})
(
)
/
(
max
arg
i
i
c
MAP
c
p
c
x
p
Clase
i
r
=
)
c
(
P
)
c
x
(
p
)
x
(
d
i
i
i
v
r =
)
(
ln
)
(
x
d
x
L
i
i
r
r =
{
})
(
)
(
ln
)
(
i
i
i
c
P
c
x
p
x
L
v
v =
Considerando la función densidad de probabilidad
como una normal multivariada, se tiene:
La clase se obtiene por MAP como:
Por lo tanto, se asigna el paciente representado por
a la clase ci donde se alcanza mayor valor de
.
Esta función de decisión es de tipo cuadrática.
MAP indica elegir la probabilidad a posteriori,
de asignar el paciente
a la clase elegida, la cual,
dado el criterio de decisión, corresponde a la que
tiene una mayor probabilidad a posteriori.
{
}
(
)
)
ˆ
(
)
ˆ
(
ln
)
(
ln
)
ln(
)
(
i
1
i
T
i
i
i
i
x
x
2
1
2
1
c
p
2
2
p
x
L
µ
µ
π
v
v
v
v
v
−
Σ
−
−
Σ
−
=
−
{
}
(
)


−
Σ
−
−
Σ
−
=
−
)
ˆ
(
)
ˆ
(
ln
)
(
ln
)
ln(
max
arg
i
1
i
T
i
i
i
c
MAP
x
x
2
1
2
1
c
p
2
2
p
Clase
i
µ
µ
π
v
v
v
v
 
xv
)
x
(
Li
v
)
(
x
c
p
i
v
xv

![Imagen](images\page011_img01.png)

---

## Página 12

23/03/2017
12
5.5. Calificador Bayesiano Ingenuo (“Naive”).
El clasificador Bayesiano óptimo obtenido por
MAP en la sección anterior supone los atributos
reales y dependientes entre sí.
En un caso mas general se pueden considerar
diferentes tipos de atributos {a1, a2, ..., ap} que
pueden ser reales, nominales o binarios y el
clasificador óptimo será determinado por:
o al usar la verosimilitud y la probabilidad a
priori:
xv
{
})
...,
,
/
(
max
arg
p
2
1
i
c
MAP
a
a
a
c
p
Clase
i
 
  
=
{
})
(
)
/
...,
,
(
max
arg
i
i
p
2
1
c
MAP
c
p
c
a
a
a
p
Clase
i
 
  
=
El problema que presenta este acercamiento al
problema de clasificación es que se requiere
determinar la verosimilitud de cada uno de los p
atributos (conjuntamente) con respecto a las m
clases ci.
Lo cual es una probabilidad muy difícil de
obtener, pues se requiere una cantidad muy
grande
de
datos
para
obtener
todas
las
posibilidades.
Si se consideran todos los aj (j=1..p) reales y que
la distribución de la verosimilitud es normal, se
obtiene el caso anterior.
La Clasificación Bayesiana Ingenua realiza una
suposición simple: todas las probabilidades de los
atributos son condicionalmente independientes
para una clase dada.

![Imagen](images\page012_img01.png)

---

## Página 13

23/03/2017
13
Esto significa que dada una clase, la probabilidad
de observar la conjunción de los {a1, a2, ..., ap}
corresponde al producto de las probabilidades
individuales de los atributos. Esto es:
Sustituyendo esto en el clasificador Bayesiano
óptimo obtenido por MAP, se tiene el clasificador
Bayesiano ingenuo:
Se puede observar que en este caso es muy fácil
estimar los p(ai/cj ) del conjunto de datos.
∏
=
=
p
1
j
i
j
i
p
2
1
c
a
P
c
a
a
a
p
)
/
(
)
/
...,
,
(






=
∏
=
p
1
j
i
j
i
c
NBC
c
a
P
c
p
Clase
i
)
/
(
)
(
max
arg  
•Para el caso de atributos nominales:
Ej: Suponiendo que aj puede tomar 4 valores
k∈{0,1,2,3} entonces:
•Para el caso de atributos reales se puede usar una
distribución normal.
Ej: Se estima la media
y la varianza
del
atributo
y
se
obtiene
la
estimación
de
la
probabilidad como:
.
i
clase
la
de
casos
de
Total
c
clase
la
en
k
a
que
en
casos
N
c
k
a
p
i
j
i
j
 
 
 
 
 
 
 
=
=
=
º
)
/
(ˆ
ja
j
a
σˆ
2
j
a
2
2
j
a
j
a
e
2
1
c
a
p
j
a
i
j
σ
π
σ
ˆ
)
(
ˆ
)
/
(ˆ
−
−
=

![Imagen](images\page013_img01.png)

---

## Página 14

23/03/2017
14
El método se aplica primero con un conjunto de
datos de los cuales se estiman las probabilidades
a priori p(ci) y las verosimilitudes p(aj /ci ) para
todas las clases i.
Esto
se
puede
considerar
la
etapa
de
entrenamiento o aprendizaje del método.
Cuando se presenta una nueva instancia aj = k, de
un conjunto desconocido de datos, se determina
la clase donde el producto de las probabilidades a
priori y verosimilitudes es máxima.

![Imagen](images\page014_img01.png)

---

