# Capitulo III Inteligencia Computaional_RA

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23/03/2017
1
Inteligencia Computacional
Capítulo IV
“Reglas de Asociación”
Profesor: Dr. Max Chacón
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática.
Objetivos
 Comprender el entorno de problemas y la génesis de
las reglas de asociación
 Conocer las definiciones formales de las reglas de
asociación
 Comprender y manipular los parámetros necesarios
para evaluar en forma cualitativa una regla
 Comprender
los
problemas
combinatorios
subyacentes a la búsqueda de relaciones frecuentes
 Evaluar las diferentes medidas de calidad de una
regla de asociación
 Dominar los algoritmos para la búsqueda de reglas
frecuentes.

![Imagen](images\page001_img01.png)

---

## Página 2

23/03/2017
2
4.1. Presentación del Problema
El problema de minería en reglas de asociación fue
introducido por Agrawal y col en 1993.
La motivación principal surge de los problemas
que tienen los gerentes de supermercados, donde
existe una gran cantidad de productos, quienes
deben tomar diferentes decisiones como:
– Que productos colocar en venta.
– Como diseñar los cupones de ventas.
– Como colocar la mercadería en los estantes
para
maximizar las ventas, etc.
La idea básica consiste en analizar las compras
que se han realizado en el pasado para mejorar la
calidad de estas decisiones.
Analizar las compras en detalle, sólo fue posible
en los últimos años con la introducción de los
lectores ópticos, lo que ha permitido almacenar la
canasta
de
compras
(“basket-market”),
que
consiste en el conjunto de productos reunidos en
una sola compra (transacción).

![Imagen](images\page002_img01.png)

---

## Página 3

23/03/2017
3
Este análisis no es realizado necesariamente en
una sola compra, pueden ser compras realizadas
por un cliente durante un periodo de tiempo.
Un ejemplo típico es:
“El 30% de las compras que contienen cerveza y
papas fritas, también contienen maní salado” y el
2% de todas las compras del supermercado
contienen los tres productos.
Esta aseveración se puede expresar como una
regla:
Si A Entonces B (c,s)
Donde:
– A es el conjunto de productos (atributos) de la
condición de la regla, denominado Antecedente.
– B es el conjunto de productos (atributos) de la
conclusión de la regla, denominado Consecuente.
– c (30%) se denomina confianza de la regla.
– s (2%) se denomina soporte de la regla.

![Imagen](images\page003_img01.png)

---

## Página 4

23/03/2017
4
El problema general de minería de datos en
reglas de asociación consiste en encontrar, en
una base de datos, la totalidad de las reglas que
cumplen con un conjunto de restricciones como
pueden ser:
– soporte mínimo y confianza mínima.
Antes de considerar este problema general (más
restrictivo) es conveniente considerar problemas
más relajados que pueden ser de gran interés
para la toma de decisiones.
Ej:
– Encontrar todas las reglas que tienen “coca-cola”
como consecuente.
- Ayuda a la planificación de la tienda para
aumentar la venta de coca-cola.
– Encontrar todas las reglas que tienen “salsa verde”
en el antecedente.
- Ayuda a determinar que productos pueden ser
impactados si se discontinua la venta de “salsa
verde”.

![Imagen](images\page004_img01.png)

---

## Página 5

23/03/2017
5
Ej:
– Encontrar todas la reglas que tienen “ketchup” en el
antecedente y “mostaza” en el consecuente.
- Ayuda a realizar el pedido de un producto
adicional (mostaza) que puede ser vendido junto
con ketchup.
– Encontrar todas las reglas que tienen productos
localizados en los estantes x e y en la tienda.
- Ayuda a planificar los estantes, determinando si
las ventas de los productos en los estantes x
están
relacionadas
con
las
ventas
de
los
productos de los estantes y.
Los
problemas
generales
y
específicos
enunciados
anteriormente
tienen
una
gran
variedad de aplicaciones que no se relacionan
necesariamente con la organización de ventas.
Algunos ejemplos son:
– Descubrir la canasta de compras mínima para un
tipo de cliente.
– Análisis de marketing cruzado (dado un grupo de
productos cual es la preferencia por otro tipo de
productos).
– Diseño de catálogos de ventas.
– Detección de fraudes
– Análisis de pérdidas.

![Imagen](images\page005_img01.png)

---

## Página 6

23/03/2017
6
Considere una base de datos o Sistema de
Información operacional SI=<U, Q, V, f >
como la definida en el Capítulo I.
– S⊆U universo cerrado: un conjunto finito, no
vacío, de n objetos {x1, x2, …, xn}. Denominados
transacciones (compras).
– Q: un conjunto finito, no vacío, de p atributos {q1,
q2, …, qp}, llamados también productos o ítems.
– V=
, donde
es el dominio (i indica los
posibles valores de cada atributo o instancias)
de cada uno de los productos (atributos) q.
U
Q
q
q
iV
∈
q
iV
Las
instancias
de
estos
atributos
son
consideradas siempre como binarias, pueden
ser nominales pero se debe realizar una etapa
de
codificación
para
transformarlas
en
binario.
1
1
V
2
2
V
j
V1
1
p
1
V
−
p
1
V
1
1
V
2
1
V
j
2
V
1
p
2
V
−
p
2
V
1
2
V
2
2
V
1
2
−
p
V
p
V1
j
V1
Transacciones
Productos (Atributos)
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

### Tabla 1 (Página 6)

| Transacciones | Productos (Atributos) | None | None | None | None | None | None |
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
2 |  | Vj
1 |  | Vp−1
1 | Vp
1 |
| x
2 | V1
1 | V2
1 |  | Vj
2 |  | Vp−1
2 | Vp
2 |
| .
. | V1
2 | V2
2 |  | Vj
1 |  | Vp−1
2 | Vp
1 |

![Imagen](images\page006_img01.png)

---

## Página 7

23/03/2017
7
Sea S un conjunto de transacciones donde cada
transacción
xi
contiene
un
conjunto
de
productos tal que xi ⊆V.
Se dice que cada transacción xi contiene un
conjunto A de
algunos productos en V, si A
⊆xi.
Una regla de asociación es una implicación de
la forma:
A ⇒B
Donde A⊂V, B⊂V y (A∩B)V=∅
4.2. Definiciones Formales
Definición:
Soporte:
El soporte de un conjunto A de transacciones
Sop(A), se define como el número de transacciones
de los atributos de A que toman el valor verdadero.
Soporte de una regla:
El soporte de una regla A ⇒B, Sop(A⇒B), es el
numero de transacciones en el conjunto S tal que A
y B son verdaderos simultáneamente.

![Imagen](images\page007_img01.png)

---

## Página 8

23/03/2017
8
Para mantener esta cantidad normalizada se
usa, en general, como una proporción de las
transacciones conjuntas entre A y B y el
número total de transacciones del conjunto S
(se indica con n).
Al valor normalizado se denominará soporte
normalizado
Sopn(A⇒B) = Sop(A⇒B) / n.
Nótese que este soporte normalizado es la
estimación de la probabilidad de la intersección
entre A y B (probabilidad de juntura).
confianza: La confianza de la regla A ⇒B ,en el
conjunto S, es la proporción entre el número de
casos de A y B que aparecen conjuntamente en S
contenidos en el número de casos de A.
Esto es:
n
)
B
A
(
Sop
)
B
A
(
pˆ
)
B
A
(
Sopn
s
⇒
=
∩
=
⇒
=
)
A
(
Sop
)
B
A
(
Sop
)
B
A
(
Conf
c
∩
=
⇒
=

![Imagen](images\page008_img01.png)

---

## Página 9

23/03/2017
9
Al dividir el numerador y denominador por n.
Sabiendo que:
el soporte de A dividido por n es la estimación de la probabilidad
de A,
y con la definición de probabilidad condicional.
se puede obtener
Por lo tanto, la confianza de la regla A⇒B representa la
probabilidad que se encuentren los productos B en la
transacción dado que ésta también contiene los productos
del conjunto A.
n
/)
A
(
Sop
n
/)
B
A
(
Sop
c
∩
=
).
A
(
Sopn
n
/)
A
(
Sop
)
A
(
Pˆ
=
=
)
A
/
B
(
pˆ
)
A
(
Pˆ
)
B
A
(
pˆ
n
/)
A
(
Sop
n
/)
B
A
(
Sop
=
∩
=
⇒
4.3. El Problema de la Minería de Reglas
El problema general se puede plantear como:
Dado el conjunto B ⊆V, encontrar todos los
posibles sub-conjuntos A ⊆V que cumplan con
un conjunto dado de restricciones, las cuales
pueden ser: mínimo Soporte, mínima Confianza
o alguna métrica
individual o común que las
involucre a ambas.
Así cuando se requiere encontrar:
–todas las reglas confiables se entenderá que es el
conjunto de todas las reglas que cumplen con una
confianza mínima minconf.
–todas las reglas frecuentes se entenderá que es el
conjunto de todas las reglas que cumplen con un
soporte mínimo minsop.

![Imagen](images\page009_img01.png)

---

## Página 10

23/03/2017
10
Considerando el conjunto B como dado y siendo
verdadero.
El
conjunto
A
puede
tener
dos
alternativas.
–Una conjunción, en cuyo caso A⊆V será verdadero
ssi todas las condiciones de A son verdaderas:
V1∧V2∧….∧Vm.
–Una disyunción, en cuyo caso A⊆V será verdadero
ssi una o mas condiciones de A son verdaderas:
V1∨V2∨….∨Vm.
Este problema en su forma general, para ambos
tipos de reglas, resulta ser un problema NP-duro.
Sin
embargo
instancias
específicas
de
este
problema general pueden ser analizadas para
obtener tratabilidad.
Los problemas considerados en este capítulo
considerarán
el
tratamiento
de
reglas
conjuntivas.
La búsqueda de los posibles conjuntos A se
realiza agregando condiciones al conjunto, esto
se denomina especialización de la regla.
Por el contrario, cuando el antecedente de la
regla contiene menos condiciones se dice que la
regla está más generalizada.

![Imagen](images\page010_img01.png)

---

## Página 11

23/03/2017
11
Ej:
Sea: A1= V1∧V2 y A2= V1∧V2∧V3, A1 es
mas general que A2, puesto que A1 contiene a
A2, y |A1|< |A2|.
Para encontrar todas las posibles reglas se
requiere un algoritmo que genere todas las
posibles combinaciones y realizar una pre-poda
de forma tal que al usar las restricciones se
detenga la búsqueda para evitar la explosión
combinatoria.
El
problema
del
cumplimiento
de
las
restricciones está asociado con la monotonicidad
de
la
restricción,
en
función
de
la
especialización.
Si
se
tienen
dos
especializaciones
del
antecedente, se generan dos reglas tales que
|A1|<|A2| y dos restricciones o medidas med(Ai)
i=1,2, asociadas a cada una de las reglas.
Se
dice
que
la
medida
es
monótona
si:
med(A1) ≤med(A2).
La medida es anti-monótona si:
med(A1) ≥med(A2).
Para realizar una pre-poda eficiente se requiere
usar restricciones monótonas o anti-monótonas.
Con lo cual se descartan ramas completas en el
proceso de especialización.

![Imagen](images\page011_img01.png)

---

## Página 12

23/03/2017
12
Al analizar el Soporte se puede observar que
esta medida es
anti-monótona. Puesto que la
especialización de la regla lleva a mantener o
disminuir el soporte.
Ej:
Si A1= V1∧V2 y A2= V1∧V2∧V3 ⇒|A1|< |A2|, para
un B dado.
Ocurrirá que Sop(A1⇒B) ≥Sop(A2⇒B)
Puesto que : Sop(A1⇒B)=P( V1∧V2∩B)
y Sop(A2⇒B)=P(V1∧V2∧V3∩B)
El caso de la Confianza es diferente puesto que
al
especializar
la
regla,
su
soporte
puede
mantenerse
o
disminuir.
El
soporte
del
antecedente también puede disminuir, pero
en
una proporción mayor que el soporte de la regla,
en cuyo caso la razón entre los dos, que
corresponde a la confianza, puede aumentar.
Dado:
Sop(A1⇒B)=P(V1∧V2∩B)
y Sop(A1)=P(V1∧V2)
Sop(A2⇒B)=P(V1∧V2∧V3∩B)↓
y Sop(A2)=P(V1∧V2∧V3)↓
↓
o Sop(A2⇒B)=P(V1∧V2∧V3∩B)= y Sop(A2)=P(V1∧V2∧V3)↓

![Imagen](images\page012_img01.png)

---

## Página 13

23/03/2017
13
V
1
V
2
V
3
B
1
1
0
0
1
1
0
0
1
1
0
0
1
1
0
1
1
1
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
0
1
1
1
0
5
3
10
5
5
3
10
5
2
2
2
2
1
1
1
2
2
1
1
3
2
1
2
1
1
=
⇒
=
=
⇒
=
=
=
⇒
=
=
⇒
∧
∧
=
∧
=
)
A
(
Sop
)
B
A
(
Sop
)
A
(
Conf
)
A
(
Sop
)
B
A
(
Sop
)
A
(
Conf
)
A
(
Sop
;
)
B
A
(
Sop
)
A
(
Sop
;
)
B
A
(
Sop
V
V
V
A
V
V
A
V
1
V
2
V
3
B
1
1
0
0
1
1
0
0
1
1
0
0
1
1
0
0
1
1
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
5
5
10
5
5
5
10
5
2
2
2
2
1
1
1
2
2
1
1
3
2
1
2
1
1
=
⇒
=
=
⇒
=
=
=
⇒
=
=
⇒
∧
∧
=
∧
=
)
A
(
Sop
)
B
A
(
Sop
)
A
(
Conf
)
A
(
Sop
)
B
A
(
Sop
)
A
(
Conf
)
A
(
Sop
;
)
B
A
(
Sop
)
A
(
Sop
;
)
B
A
(
Sop
V
V
V
A
V
V
A

### Tabla 1 (Página 13)

| V
1 | V
2 | V
3 | B |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 |

### Tabla 2 (Página 13)

| V
1 | V
2 | V
3 | B |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |

![Imagen](images\page013_img01.png)

---

## Página 14

23/03/2017
14
4.4. Combinatoria de la Búsqueda
El
problema
consiste
en
encontrar
un
algoritmo que permita generar todas las
posibles combinaciones para un antecedente
y, en el proceso de generación de las reglas,
interrumpir
la
especialización
usando
medidas monótonas para una pre-poda.
Sea V={1,2,3,4} un conjunto de antecedentes del cual se
requiere generar todas las posibles combinaciones.
Cada nodo g en el árbol es representado por dos grupos:
– Uno llamado cabeza h(g) que representa la regla para el nodo.
– Uno llamado cola t(g) que representa todas las posibles
combinaciones (ordenadas) que pueden ser agregadas a la cabeza
para formar una regla.
1
3
4
2
1,2
1,2,3
1,2,3,4
1,3
1,4
1,2,4
1,3,4
2,3,4
2,3
3,4
2,4

![Imagen](images\page014_img01.png)

---

## Página 15

23/03/2017
15
El algoritmo inicial presentado por Agrawal
utiliza esta combinatoria para generar el árbol
paso a paso y va realizando una pre-poda por
soporte.
Cuando encuentra un nodo h(g) cuyo soporte es
inferior
al
minsop
entonces
no
genera
las
combinaciones t(g), puesto que todas ellas no
cumplirán con minsop.
Con respecto a la confianza propone simplemente
ordenar la totalidad de las reglas generadas y
entregar sólo las que cumplen con minconf.
La propuesta actual es mantener las “mejores
reglas” (ej: las más confiables) en una lista y
recorrer el árbol por anchura. Si no se consigue
agregar nuevas reglas a la lista se detiene el
proceso.
Las variaciones de este algoritmo consisten en
ordenar la lista de las mejores reglas según una
medida de calidad de la regla que permita dejar el
número mínimo de reglas confiables fuera de la
lista.

![Imagen](images\page015_img01.png)

---

## Página 16

23/03/2017
16
Como una forma de evaluar de mejor manera la
confianza, se han generado diferentes medidas o
métricas de calidad que ayuden a seleccionar el
conjunto de las mejores reglas.
En general a estas medidas se les exige que sean
monótonas en confianza, o soporte y confianza,
pero manteniendo uno de ellas constante.
Esto
no
supera
el
problema
de
la
no-
monotonicidad de la confianza pero, para casos
particulares permite realizar una búsqueda más
efectiva.
4.5. Medidas de Calidad
Análisis de monotonicidad de las medidas o
métricas de calidad
 Lift: Una medida usada en las herramientas de
minería de datos producidas por IBM.
En términos de probabilidades estimadas se sabe que:
Conf(A⇒B)=p(B∩A)/P(A) y que P(B)=Sop(B)/n.
Por lo tanto lift(A⇒B)= p(B∩A)/(P(A)P(B)).
)
B
(
Sop
)
B
A
(
conf
 n
lift
⇒
=

![Imagen](images\page016_img01.png)

---

## Página 17

23/03/2017
17
Lo
cual
representa
una
medida
de
independencia entre A y B. Esto es, lift tendrá
su valor más bajo (1) cuando A y B sean
completamente independientes.
Es fácil ver que esta medida es monótona en
confianza, puesto que al especializar la regla,
lift disminuye proporcional a c, puesto que
P(B) se mantiene constante para el proceso de
especialización.
• Convicción:
Una
medida
similar
a
la
anterior, que mantiene la monotonicidad en
confianza.
Usando
estimación
de
probabilidades
y
factorizando el numerador por n, se tiene:
[
])
B
A
(
conf
1
n
Sop(B)
- n
convicción
⇒
−
=
[
]




∩
−
−
=
)
A
(
P
)
B
A
(
p
)
A
(
P
n
 )
B
(
P
1
n
convicción
[
]
)
B
A
(
P
)
A
(
P
)
B
(
P
)
A
(
P
∩
−
−
=
1

![Imagen](images\page017_img01.png)

---

## Página 18

23/03/2017
18
sabiendo que:
y que
Esto también representa la independencia de A y
B y es monótona en confianza.
)
B
(
P
1
)
B
(
P
−
=
)
B
A
(
p
)
A
(
P
)
B
A
(
P
∩
−
=
∩
)
B
A
(
P
)
B
(
P
)
A
(
P
convicción
∩
=
Medidas monótonas en soporte y confianza.
• Laplace:
Donde la constante k es un entero mayor que 1
Puesto que la confianza c=p(B/A)=p(A∩B)/p(A) y
Sop(A⇒B)=p(A∩B), se puede reemplazar en el
denominador P(A)=Sop(A⇒B)/c.
Quedando
k
)
A
(
Sop
1
B)
Sop(A
)
B
A
(
Laplace
+
+
⇒
=
⇒
k
c
/)
B
A
(
Sop
1
)
B
A
(
Sop
Laplace
+
⇒
+
⇒
=

![Imagen](images\page018_img01.png)

---

## Página 19

23/03/2017
19
Si la confianza se fija en un valor c, al disminuir el
Sop(A⇒B)
por
efecto
de
la
especialización,
el
denominador disminuirá mas rápido que el numerador
puesto que k>1, haciendo que la medida disminuya.
En el peor caso se mantendrá la relación si k no es lo
suficientemente grande en relación a c.
Por lo tanto, la medida es monótona en soporte,
manteniendo el confianza constante.
Si el soporte se mantiene constante y la confianza
disminuye, al especializar la regla, esto hace aumentar el
denominador, lo que hará que la medida disminuya.
Por lo tanto, la medida es monótona en confianza, para
un soporte constante.
• Ganancia:
con 0<θ<1.
Aplicando el mismo concepto anterior P(A)=Sop(A⇒B)/c y
factorizando por Sop(A⇒B) se tiene:
Gan(A⇒B)=Sop(A⇒B)(1 - θ/c)
Si la confianza se mantiene constante y c>θ se observa
claramente que la ganancia disminuirá al disminuir el
soporte de la regla, puesto que son proporcionales.
Si el soporte de la regla se mantiene constante, la ganancia
disminuirá al disminuir la confianza, puesto que aumenta la
relación q/c, aumentando el sustrayendo, y la diferencia (1-
θ/c) disminuirá.
Lo cual implica que la medida será monótona en confianza
para soporte constante y viceversa.
)
(
 
B)
Sop(A
)
(
A
Sop
B
A
Gan
θ
−
⇒
=
⇒

![Imagen](images\page019_img01.png)

---

## Página 20

23/03/2017
20
• Métrica de Piatetsky-Shapiro (P-S)
Esta métrica presenta la misma estructura que la
anterior al considerar θ =Sop(B)/n, como la
probabilidad del consecuente.
Las condiciones de monotonicidad se pueden
estudiar en forma similar a la ganancia.
n
)
B
(
Sop
)
A
(
Sop
)
B
A
(
Sop
)
B
A
(
S
P
−
⇒
=
⇒
−

![Imagen](images\page020_img01.png)

---

