# 4 Perceptron Multicapa

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Fundamentos Aprendizaje Profundo
Perceptron MulticapaUniversidad de Santiago de Chile
Universidad de Santiago de ChileDepartamento de Ingeniería Informática
Departamento de Ingeniería Informática
Marzo 2019
Dr. Gonzalo Acuña L.

---

## Página 2

Temario
• I. Perceptron Multicapa
• II. Método de Retropropagación del Error
• III. Retropropagación usando gradiente 
descendente
• IV. Mejoras a Gradiente Descendente
Gonzalo Acuña L
USACH-DIINF

---

## Página 3

I.- Perceptron Multicapa
Gonzalo Acuña L
USACH-DIINF

---

## Página 4

Gonzalo Acuña L
USACH-DIINF

---

## Página 5

Gonzalo Acuña L
USACH-DIINF

---

## Página 6

Gonzalo Acuña L
USACH-DIINF

---

## Página 7

Gonzalo Acuña L
USACH-DIINF

---

## Página 8

Gonzalo Acuña L
USACH-DIINF

---

## Página 9

Gonzalo Acuña L
USACH-DIINF

---

## Página 10

Redes Multicapas 
 
 
 
Definición : 
  
 
      Red   en   la   que   sus   neuronas   están 
      ordenadas      en      capas     o     estratos 
      sucesivos.  Cada   capa   recibe  entradas 
      desde la capa previa ( o entrada externa ) 
      y  envía  sus  salidas  a  la capa siguiente. 
      No   hay   conexiones   internas   en  cada 
      capa.      
Gonzalo Acuña L
USACH-DIINF

---

## Página 11

Gonzalo Acuña L
USACH-DIINF

---

## Página 12

Gonzalo Acuña L
USACH-DIINF

---

## Página 13

II.- Método de Retropropagación 
del Error
Gonzalo Acuña L
USACH-DIINF

---

## Página 14

Rumelhart y McClelland: la 
hipótesis conexionista
Gonzalo Acuña L
USACH-DIINF

---

## Página 15

Gonzalo Acuña L
USACH-DIINF

---

## Página 16

X1
X2
1
w11
w12
w21
w22
w31
w32
1
w’11
w’21
w’31
y
Backpropagation
X1
X2
1
w11
w12
w21
w22
w31
w32
1
w’11
w’21
w’31
Pesos Iniciales
Aleatorios
Salida de 
la Red
ˆ
error
y
y


Calculo de la 
salida
Cálculo del
error
Retropropagación 
del error
Modificación de los 
pesos de la Red
Gonzalo Acuña L
USACH-DIINF

---

## Página 17

Gonzalo Acuña L
USACH-DIINF

---

## Página 18

Gonzalo Acuña L
USACH-DIINF

---

## Página 19

Gonzalo Acuña L
USACH-DIINF

---

## Página 20

Retropropagación
X1
X2
1
w11
w12
w21
w22
w31
w32
1
w’11
w’21
w’31
y
1
(
)
t
t
t
t
t
J
w
w
d
w
w









Gonzalo Acuña L
USACH-DIINF

---

## Página 21

• Ejemplo:
• Capa Salida:
1
2
2
1
11
2
21
31
'
1
1
(
)
[ (
'
'
' )
]
2
2
t
t
t
a
J
y
d
f O w
O w
w
d






1
1
11
'
(
)
'
(
)
(1
)
'
t
t
t
t
t
t
t
J
y
d
f
O
y
d y
y O
w










1
2
2
2
2
2
1
( )
1
(1
)
'( )
(1
)
(
)
1
1
(1
)
(1
)
1
1
1
(1
)
'( )
(1
)
x
x
x
x
x
x
x
x
x
x
Sea
f x
e
e
f
x
e
e
x
e
e
e
e
y
y
e
e
f
x
y
y




































Gonzalo Acuña L
USACH-DIINF

---

## Página 22

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
Gonzalo Acuña L
USACH-DIINF

---

## Página 23

• Capa Escondida:
• Si varias salidas:
1
11
1
11
'
11
1
1
1
'
'
(
)
(1
)
'
(1
)
11
1
1
1
'
(1
)
t
t
t
O
J
J
a
(Regla de la cadena)
w
a
O
w
y
d
y
y
w
O
O X
t
t
t
t
'
w
O
O
X

























1
1
1
'
'
(1
)
t
k
jk
k
w
O
O
X







Gonzalo Acuña L
USACH-DIINF

---

## Página 24

Gonzalo Acuña L
USACH-DIINF

---

## Página 25

Gonzalo Acuña L
USACH-DIINF

---

## Página 26

Gonzalo Acuña L
USACH-DIINF

---

## Página 27

Gonzalo Acuña L
USACH-DIINF

---

## Página 28

Gonzalo Acuña L
USACH-DIINF

---

## Página 29

Salidas 
de la Red
Retropropagación
Error
Gonzalo Acuña L
USACH-DIINF

---

## Página 30

X(t+1)
V
Zin(t)
)
(
1
1
t
NL
e
f
Zin



Z(t)
W
Y(t)
X(t)
E(t)
)1
(
)
(



t
t
fE
X
Y
1

Ef


2
)
(
)
(
1
t
t
NL
e
e
f
Zin
Zin





Wj

E(t)

Z(t)
-∆W


X(t)
-∆V
Gonzalo Acuña L
USACH-DIINF

---

## Página 31

Gonzalo Acuña L
USACH-DIINF

---

## Página 32

Gonzalo Acuña L
USACH-DIINF

---

## Página 33

Gonzalo Acuña L
USACH-DIINF

---

## Página 34

Gonzalo Acuña L
USACH-DIINF

---

## Página 35

III.- Retropropagación usando 
gradiente descendente
• Ventajas:
• Implementación simple
– Método estándar que generalmente funciona 
bien
• Desventajas:
– Lento e ineficiente
– Puede quedar atrapado en mínimos locales 
entregando resultados sub-óptimos
Gonzalo Acuña L
USACH-DIINF

---

## Página 36

• Métodos de Gradiente
– En General:
Problema: Convergencia lenta. Tendencia a
quedar atrapada en mínimos locales
1
1
:
(
)
dirección
k
k
amplitud
pasobusqueda
k
k
w
w
h
d
Gradiente w
w
d
w








Gonzalo Acuña L
USACH-DIINF

---

## Página 37

• Ejemplo:
2
1
1
2
1
( )
1
:
1
1 1 ( 2 )
1
1 1 ( 2 )
1
.
k
k
k
J x
x
y
d
Si
x
x
x
x
x
cte










x
J(x)
-1
1
Gonzalo Acuña L
USACH-DIINF

---

## Página 38

IV.- Mejoras a Gradiente 
Descendente
• Momentum
– Añade  porcentaje del último movimiento al 
actual
Gonzalo Acuña L
USACH-DIINF

---

## Página 39

Gonzalo Acuña L
USACH-DIINF

---

## Página 40

La opción de calcular en forma elegante y 
eficiente el gradiente permite tratar el 
problema de optimización con toda la 
batería de métodos de optimización que 
proporciona la optimización en sistemas no-
lineales.
Gonzalo Acuña L
USACH-DIINF

---

## Página 41

Métodos de 
optimización
• Gradiente Conjugado
• Quasi-Newton
• Simulated Annealing
• Algoritmos genéticos
• …etc


2
ˆ
2
1



k
sh
t
t
i
i
i Y
Y
J
Min
¿Deterministas o Estocásticos?Deterministas o Estocásticos?
Gonzalo Acuña L
USACH-DIINF

---

## Página 42

Gradiente Conjugado
Dirección de gradiente
X0
X1
X2
Gradiente
conjugado
1
k
wk
k
d
J
d




Gonzalo Acuña L
USACH-DIINF

---

## Página 43

Fletcher y Reeves...
• Es una extensión del método de gradiente conjugado a 
funciones cualquiera (no necesariamente cuadráticasno necesariamente cuadráticas) 
y  sin  la utilización explícita del  Hesianosin  la utilización explícita del  Hesiano.
• Etapa de inicialización:
– Seleccionar un punto de partida
– Calcular 
• Etapa iterativa
– Determinar       que minimiza                          
en la dirección
– Calcular                                 donde 
0x

0
0
0
x
f
g
d




k
k
k
k
k
d
x
x





1
kd
k
k
k
k
d
g
d







1
1
k
Tk
k
Tk
k
g
g
g
g





1
1

Gonzalo Acuña L
USACH-DIINF

---

## Página 44

Métodos 2º orden tipo Newton
• Taylor de J(w):
0
0
0
0
0
2
0
0
0
0
1
0
0
1
( )
(
)
(
)
(
)
(
)
(1)
2
(1) :
( )
(
)
(
)
(2)
( )
0
0
(
)
(
)
(
)
ij
i
i
j
J w
J
w
w
J w
w
w H w
w
J
J
J
H
w
w w
Derivando
J w
J w
H w
w
mínimo
J w
J w
H w
w
w
w
H
J w

































Gonzalo Acuña L
USACH-DIINF

---

## Página 45

Gonzalo Acuña L
USACH-DIINF

---

## Página 46

• Ejemplo:
• Quasi-Newton:
– H-1 se aproxima en forma recursiva.
– BFGS Broyden, Fletcher, Goldfarb, Shanno
2
0
2
2
1
1
2
0
( )
;
1
2 ;
2
1
1
( 2 )
0
2
1
0
( 2 )
0
2
J w
w
w
J
J
w
w
w
w
w
w
w
















Gonzalo Acuña L
USACH-DIINF

---

## Página 47

Gonzalo Acuña L
USACH-DIINF

---

## Página 48

Métodos Quasi-Newton



k
k
k
k
k
g
x
f
x
x







1
2
1


kx
f
2

es una aproximación 
convenientemente elegida 
de… 
k
G
k
G
Simétrica
Definida positiva
•
Hay muchas formas de 
actualizar la matriz G o su 
inversa S y que satisfacen los 
criterios para anteriores.
k
k
k
q
p
G


k
k
k
k
k
d
x
x
p






1
k
k
k
g
g
q


1
)
(
)
()
(
1
k
k
k
Tk
T
k
k
k
k
k
k
k
k
p
G
q
p
p
G
q
p
G
q
G
G











)
(
)
)
(
1
k
k
k
Tk
T
k
k
k
k
k
k
k
k
q
S
p
q
q
S
p
q
S
p
S
S











Gonzalo Acuña L
USACH-DIINF

---

## Página 49

Levenberg - Marquardt
• Modificación de Gauss-Newton
• Ventajas:
– Bien definido aunque J no sea de rango pleno
– Globalmente convergente  
1
1
[
]
T
T
k
k
k
k
k
k
k
Aproximación
Hessiano
w
w
J J
I
J r





Gonzalo Acuña L
USACH-DIINF

---

## Página 50

Gonzalo Acuña L
USACH-DIINF

---

## Página 51

Gonzalo Acuña L
USACH-DIINF

---

## Página 52

Gonzalo Acuña L
USACH-DIINF

---

