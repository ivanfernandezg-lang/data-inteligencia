# 5 Elaboracion Modelos con MLP

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Fundamentos Aprendizaje Profundo
Elaboración Modelos con MLPUniversidad de Santiago de Chile
Universidad de Santiago de ChileDepartamento de Ingeniería Informática
Departamento de Ingeniería Informática
Marzo 2019
Dr. Gonzalo Acuña L.

---

## Página 2

Pasos para elaboración de 
modelos con Perceptrones 
Multicapa
Gonzalo Acuña L
USACH-DIINF

---

## Página 3

Paso 1:  Exhaustivo análisis de 
sistema
• En este análisis se debe dejar establecido el 
número y tipo de variables de entrada y salida del 
modelo, la posibilidad de reducir la dimensión del 
problema disminuyendo el número de variables 
involucradas, etc...
• Es realmente imprescindible usar un modelo 
neuronal? Porqué no utilizar modelos clásicos 
existentes?  RED NEURONAL: SEGUNDA 
MEJOR SOLUCIÓN !!
• Si se decide utilizar un modelo neuronal, se cuenta 
con los datos que representen adecuadamente el 
fenómeno a modelar y en la cantidad suficiente?

---

## Página 4

Paso 2:  Preprocesamiento
• Datos: un modelo neuronal es de tipo “caja 
negra”. Son modelos de interpolación (NUNCA 
DE EXTRAPOLACIÓN) que dependen 
FUERTEMENTE de calidad y cantidad de datos 
disponible.
• Calidad:  relacionada con el grado con que los 
datos disponibles representan la función que se 
está aproximando. Deseable: obtenerlos siguiendo 
un plan de experiencias adecuadamente diseñado.
Gonzalo Acuña L
USACH-DIINF

---

## Página 5

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
Gonzalo Acuña L
USACH-DIINF

---

## Página 6

• Datos (ejemplos): 
• Cantidad:  es extremadamente importante pues 
sólo una cantidad de datos adecuada nos permitirá 
identificar en forma correcta los parámetros 
(pesos) de nuestro modelo neuronal. 
• Si la cantidad de datos es pequeña, NO 
PODEMOS PRETENDER elaborar un modelo 
neuronal complejo. 
Gonzalo Acuña L
USACH-DIINF

---

## Página 7

• Examinar atentamente (visualmente) los 
datos. Detectar y en lo posible eliminar 
“outliers” (errores gruesos), vacíos, etc...
• Una atenta examinación visual permite a 
veces detectar correlación entre variables y, 
por lo tanto, reducir dimensionalidad, etc...
Gonzalo Acuña L
USACH-DIINF

---

## Página 8

Gonzalo Acuña L
USACH-DIINF

---

## Página 9

• Normalización de variables: Necesaria cuando 
intervienen variables con diferentes unidades y por 
lo tanto amplitudes a veces varios órdenes de 
magnitud diferentes. 
• Ejemplo1 : Xn = (X-Xmin)/(Xmax-Xmin);  Xn € (0,1)
• Ejemplo2:  Xn = 2*(X-Xmin)/(Xmax-Xmin) – 1; Xn € (-1,1)
•
Xmax = 1,1 máximo valor de datos; Xmin = 0,9 mínimo valor de datos
• Es necesario, a la salida, realizar la 
desnormalización correspondiente.
Gonzalo Acuña L
USACH-DIINF

---

## Página 10

Gonzalo Acuña L
USACH-DIINF

---

## Página 11

Paso 3: Diseño del MLP
(problemas pequeños o medianos)
• Número de neuronas de entrada y de salida, 
dependiente del análisis de sistema 
anteriormente analizado.
• Número de neuronas de capa intermedia 
Nc:
– Lo importante es que dicho número de lugar a 
una cantidad de parámetros (pesos) Nw tal que:
• Nw < (Número de ejemplos) / 10
Gonzalo Acuña L
USACH-DIINF

---

## Página 12

• El número de pesos Nw de un perceptron 
multicapas, con 1 capa entrada con Ne 
neuronas, una capa oculta con Nc neuronas 
y una capa de salida con Ns neuronas es:
Nw = (Ne+1)*Nc+(Nc+1)*Ns
Gonzalo Acuña L
USACH-DIINF

---

## Página 13

• Por lo tanto, si se tiene una red con 3 
entradas, 4 neuronas en la capa oculta y 2 
salidas, su cantidad de pesos es:
Nw = (3+1)*4+(4+1)*2 = 26
Luego, se requiere de AL MENOS 260 ejemplos 
en el conjunto de entrenamiento para identificar 
los parámetros de esta red.
Gonzalo Acuña L
USACH-DIINF

---

## Página 14

• Funciones de transferencia: la ventaja de los modelos 
neuronales y lo que los hace poderosos para aproximar 
funciones complejas es su capacidad de utilizar funciones 
de transferencia de tipo sigmoidal (facilita la 
retropropagación).
• Un criterio usual es que, dado que está demostrado que 
basta una sola capa oculta con un adecuado número de 
neuronas para aproximar con un grado de precisión 
arbitrario cualquier función no lineal [Funahashi, 89, 
Cybenko, 89, Hornik et al., 89, Hornik, 91], utilizar 
funciones sigmoidales en la capa oculta y funciones 
lineales en la de salida.
• Sin embargo también pueden usarse sigmoides en la salida.
Gonzalo Acuña L
USACH-DIINF

---

## Página 15

Paso 4: Entrenamiento
• El entrenamiento supervisado de una red 
neuronal es un proceso muy delicado 
debido a la complejidad que ostenta la 
superficie de la función error, la que puede 
poseer numerosos mínimos locales, puntos 
silla, etc...
Gonzalo Acuña L
USACH-DIINF

---

## Página 16

• Hay tres problemas principales que pueden surgir 
durante entrenamiento:
– 1   Sesgo
– 2.- Sobreparametrización
– 3.- Sobreaprendizaje
Los dos últimos dan lugar a un fenómeno similar que 
afecta la capacidad de “generalización” de la red (alta 
varianza).
Gonzalo Acuña L
USACH-DIINF

---

## Página 17

1.- Problema de gran sesgo (bias)
y(x)
x
Gonzalo Acuña L
USACH-DIINF

---

## Página 18

Como disminuir el sesgo?
1.- Logrando llegar a un mejor mínimo local para 
lo cual es importante realizar una buena 
cantidad de entrenamientos diferentes partiendo 
desde pesos iniciales aleatoriamente escogidos 
(20 o más intentos).
2.- Aumentando prudentemente el número de 
neuronas en la capa oculta
Gonzalo Acuña L
USACH-DIINF

---

## Página 19

Gonzalo Acuña L
USACH-DIINF

---

## Página 20

2.- Problema de gran varianza (sobreparametrización y 
sobreentrenamiento)
y(x)
x
Gonzalo Acuña L
USACH-DIINF

---

## Página 21

Gonzalo Acuña L
USACH-DIINF

---

## Página 22

Gonzalo Acuña L
USACH-DIINF

---

## Página 23

Formas de evitar los problemas anteriores:
1.- Trabajar siempre con dos conjuntos durante 
entrenamiento: 
conjunto de entrenamiento
conjunto de test (prueba)
Lo ideal es visualizar el comportamiento de la 
función error en forma simultánea en ambos 
conjuntos
Gonzalo Acuña L
USACH-DIINF

---

## Página 24

Grafico de función error en conjuntos 
aprendizaje (-) y test (---)
Número 
iteraciones
Mínimo error de test
Error
Gonzalo Acuña L
USACH-DIINF

---

## Página 25

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
1.- “Early stopping”:  la idea es detener el 
proceso de aprendizaje apenas el error sobre el 
conjunto de test comience a aumentar. Se evita, 
de esta manera, que la red neuronal modelice el 
ruido que pueden contener los datos.
Gonzalo Acuña L
USACH-DIINF

---

## Página 26

No. parámetros red
Error
Gonzalo Acuña L
USACH-DIINF

---

## Página 27

Característica de los conjuntos  de aprendizaje y 
prueba:
Ambos deben ser numerosos y los ejemplos que 
los compongan deben ser representativos del 
fenómeno subyacente que se quiere modelar
Gonzalo Acuña L
USACH-DIINF

---

## Página 28

Otros métodos utilizados:
2.- Validación cruzada:  se elaboran distintos 
modelos neuronales a partir del uso de los 
ejemplos disponibles para aprendizaje 
confeccionando de distinta forma los conjuntos 
de aprendizaje y test.  Se escoge aquel modelo 
que da mínimo error sobre conjunto de test.
Gonzalo Acuña L
USACH-DIINF

---

## Página 29

Gonzalo Acuña L
USACH-DIINF

---

## Página 30

Gonzalo Acuña L
USACH-DIINF

---

## Página 31

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
Gonzalo Acuña L
USACH-DIINF

---

## Página 32

3.- Poda: la idea es comenzar con una red 
neuronal con una gran cantidad de pesos e ir 
“podando” dichos pesos bajo ciertos criterios 
que también incluyen la adición de términos a 
la función objetivo, los análisis de sensibilidad, 
etc… 
Gonzalo Acuña L
USACH-DIINF

---

## Página 33

4.- Regularización:  se trata de agregar términos 
a la función objetivo de tal manera que al 
minimizarla se penalice la complejidad del 
modelo.
Gonzalo Acuña L
USACH-DIINF

---

## Página 34

Gonzalo Acuña L
USACH-DIINF

---

## Página 35

Gonzalo Acuña L
USACH-DIINF

---

## Página 36

Gonzalo Acuña L
USACH-DIINF

---

## Página 37

Gonzalo Acuña L
USACH-DIINF

---

## Página 38

Gonzalo Acuña L
USACH-DIINF

---

## Página 39

Gonzalo Acuña L
USACH-DIINF

---

## Página 40

Gonzalo Acuña L
USACH-DIINF

---

## Página 41

Gonzalo Acuña L
USACH-DIINF

---

## Página 42

Paso 5: Generalización
Para probar la capacidad de generalización de la 
red, o sea sus resultados sobre un conjunto 
distinto de datos, es importante haber reservado 
ejemplos para confeccionar un tercer conjunto, 
el CONJUNTO DE GENERALIZACIÓN.
Este debe ser tan representativo del fenómeno a 
modelar como los anteriores (aprendizaje y 
test).
Gonzalo Acuña L
USACH-DIINF

---

## Página 43

3.- Aproximación correcta de la función subyacente 
GENERALIZACIÓN
y(x)
x
Gonzalo Acuña L
USACH-DIINF

---

## Página 44

Es importante chequear la capacidad de 
generalización, lo que también se conoce como 
VALIDACIÓN del modelo neuronal.
Gonzalo Acuña L
USACH-DIINF

---

## Página 45

Índices Validación Clasificadores
Matriz Confusión
Gonzalo Acuña L
USACH-DIINF

---

## Página 46

Gonzalo Acuña L
USACH-DIINF

---

## Página 47

Gonzalo Acuña L
USACH-DIINF

---

## Página 48

Índices para validación numérica 
de modelos (regresión)
Índices de error usados:
: Valores predichos.
: Valores observados
N : Número total de datos.
: Valor medio de las observaciones.
i
ip
m
i
i
p
p



'
m
i
i





'
m









n
i
i
n
i
i
i
p
RMS
1
2
1
2




N
p
RSD
n
i
i
i




1
2













n
i
i
i
n
i
i
i
p
p
IA
1
2
1
2
'
'
1


Gonzalo Acuña L
USACH-DIINF

---

