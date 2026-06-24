# 2 Perceptron

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Fundamentos Aprendizaje Profundo
PerceptronUniversidad de Santiago de Chile
Universidad de Santiago de ChileDepartamento de Ingeniería Informática
Departamento de Ingeniería Informática
Marzo 2019
Dr. Gonzalo Acuña L.

---

## Página 2

I . Introducción
Gonzalo Acuña L
USACH-DIINF

---

## Página 3

• Hay un problema transversal que es el de
la “aproximación de funciones” que en
el caso de sistemas estáticos puede
diferenciarse en al menos otros dos
subproblemas:
Clasificación
Regresión
Gonzalo Acuña L
USACH-DIINF

---

## Página 4

• Clasificación:
– Se
trata
de
aproximar
una
función
que
represente la probabilidad de pertenencia de un
cierto objeto -caracterizado por un conjunto de
variables de entrada, continuas o discretas- a
una clase determinada (salida con valores
discretos).
Ejemplo:
reconocimiento
de
caracteres.
y = f(x, w)
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

• Clasificación y funciones discriminantes
• Cómo se puede realizar una 
clasificación?
–Mediante el uso de funciones 
discriminantes que están definidas en el 
espacio de vectores que se desea 
clasificar y producen un valor real que se 
puede comparar.

---

## Página 10

• Se   tiene   una   función (gi) por clase (si)   
• La regla de clasificación es:
u Є si si gi (u ) > gj ( u );  j ≠ i
• Para  problemas  de dos clases se puede 
reducir a una función: g(u ) = g1(u ) – g2 (u), 
luego u Є s1 g( u ) > 0 y u  Є  s2 si no. 
Gonzalo Acuña L
USACH-DIINF

---

## Página 11

• Regresión:
– Se trata de aproximar la función generadora 
(desconocida) de un cierto proceso mediante 
otra que mapee elementos del conjunto de 
variables de entrada pertinentes en otros del 
conjunto de variables de salida. Usualmente 
aquí se trata con valores continuos. 
y = f(x, w)
Gonzalo Acuña L
USACH-DIINF

---

## Página 12

II. Perceptron
Gonzalo Acuña L
USACH-DIINF

---

## Página 13

Frank Rosenblatt, 1957 
Gonzalo Acuña L
USACH-DIINF

---

## Página 14

• In a 1958 New York Times article, 
Rosenblatt conveys an ambitious 
(prescient?) vision of the future of machine 
learning. The article refers to Rosenblatt’s 
perceptron as “the embryo of an electronic 
computer that [the Navy] expects will be 
able to walk, talk, see, write, reproduce 
itself and be conscious of its existence.”
Gonzalo Acuña L
USACH-DIINF

---

## Página 15

• Idea base:  Entender capacidad de 
organismos para reconocimiento perceptivo 
recuerdo y pensamiento:
– Cómo la información del mundo físico es percibida y/o 
detectada por un sistema biológico ?
– De qué forma la información es almacenada o 
recordada ?
– Cómo la información almacenada en la memoria 
influye para el reconocimiento y el comportamiento ?
Gonzalo Acuña L
USACH-DIINF

---

## Página 16

Gonzalo Acuña L
USACH-DIINF

---

## Página 17

Gonzalo Acuña L
USACH-DIINF

---

## Página 18

• Red de “3 capas” la última de ellas con 
función de transferencia de tipo umbral 
lógico diseñada para tarea de clasificación
• retina - células de asociación – unidad de 
decisión
Gonzalo Acuña L
USACH-DIINF

---

## Página 19

Gonzalo Acuña L
USACH-DIINF

---

## Página 20

Gonzalo Acuña L
USACH-DIINF

---

## Página 21

• Clasificación lineal mediante Perceptron
• El Perceptron realiza una función discriminante lineal:
g (u)  =  a1 u1 + a2 u2 + ...+ an un + a n+ 1 =  a . u      
El     valor    asociado    a    g( u )   =   0   corresponde      a      
la      frontera,   un hiperplano, que separa las dos clases. 
•
Los     perceptrones    son   adecuados    sólo       para      
clases       linealmente    separables.
•
El problema de aprendizaje se  reduce  a encontrar un 
hiperplano  que  separa a las clases. 
Gonzalo Acuña L
USACH-DIINF

---

## Página 22

Gonzalo Acuña L
USACH-DIINF

---

## Página 23

a
y
X0
X1
w0
w1
0
0
1
1
a
X
X






0
1
0
1
1
X
X







X0
X1
B
B
B
B
A
A
A
A
A

Gonzalo Acuña L
USACH-DIINF

---

## Página 24

REGLA DE APRENDIZAJE 
                                   _ 
y ( x ) = Ø ( W • X)  :  Salida del perceptron           
ŷ ( x )  =   Salida deseada Є { 1, –1 }  
                                                                             
ΔW k = 
η 
(
 
ŷ
 
(
 
x k ) -y ( xk ) ) · xk          
       
WK+1 = 
WK + ∆ WK 
 
         ó 
∆WK  =   0 si la salida es correcta 
            + 2 η 
X
k  Si ŷ ( xk )  = 1 , y ( Xk ) =-1 
- 2η 
X
k  Si ŷ ( xk  )  = -1 ,y ( Xk  ) =1 
  
n > o;  { X1..... Xk }: Secuencia de entrada  
Gonzalo Acuña L
USACH-DIINF

---

## Página 25

• Convergencia del algoritmo de aprendizaje
del Perceptron:
Está demostrada para problemas linealmente
separables y lo logra en un número finito de
pasos (Haykin, Neural Networks and Learning
Machines, 2009)
Gonzalo Acuña L
USACH-DIINF

---

## Página 26

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 27

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 28

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 29

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 30

• Espacio de salida para compuerta  AND
(1,1)
(1,0)
(0,1)
(0,0)
1.5 = w1*I1 + w2*I2
Input 1
Input 2
Gonzalo Acuña L
USACH-DIINF

---

## Página 31

• Espacio de salida para compuerta XOR 
•
=> necesidad de capa oculta
(1,1)
(1,0)
(0,1)
(0,0)
Input 1
Input 2
Gonzalo Acuña L
USACH-DIINF

---

## Página 32

Gonzalo Acuña L
USACH-DIINF

---

