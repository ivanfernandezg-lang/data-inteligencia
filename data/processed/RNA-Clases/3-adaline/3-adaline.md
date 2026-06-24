# 3 Adaline

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Fundamentos Aprendizaje Profundo
AdalineUniversidad de Santiago de Chile
Universidad de Santiago de ChileDepartamento de Ingeniería Informática
Departamento de Ingeniería Informática
Marzo 2019
Dr. Gonzalo Acuña L.

---

## Página 2

Temario
• I. El problema de regresión lineal y mínimos 
cuadrados
• II. Máxima Verosimilitud
• III. Entropía e Información
• IV. Adaline
Gonzalo Acuña L
USACH-DIINF

---

## Página 3

I. - El problema de regresión 
lineal y los mínimos cuadrados

---

## Página 9

II.- Máximo de Verosimilitud 
(Maximum Likelihood)

---

## Página 18

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
IV.- Redes Monocapa: Adaline

---

## Página 19

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
• Historia: Widrow - Hoff,  1960
• Al igual que en el caso del Perceptron, se 
desarrolló en forma independiente para 
resolver el problema de clasificación
• Adecuado cuando las clases son 
linealmente separables

---

## Página 20

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 21

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
Regla Delta o LMS (Least Mean 
Squared)
• 1.- Inspirada por la necesidad de diseñar un 
Filtro de Wiener en la práctica, contando 
sólo con información de entrada-salida.
• 2.- Paso 1: Crear una función del Error 
J=f(e). Normalmente una cuadrática.
• 3.- Paso 2: Encontrar el mínimo de J 
jugando sobre el valor de los pesos w del 
Adaline.

---

## Página 22

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 23

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 24

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
• Widrow y Hoff descubrieron que el 
gradiente, útil para ir adaptando los pesos 
siguiendo una regla de gradiente 
descendente, podía ser estimado fácilmente 
a partir del error “instantáneo” (no medio -
como lo exige el método mínimos 
cuadrados) y el vector de entrada al 
Adaline.

---

## Página 25

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

## Página 26

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
Error cuadrático 
 
                   
2
ˆ
2
1






S
s
s
s
S
s
s
y
y
E
E
 
        
con 
  s 
      ŷ    : vectorde valores de salida deseados 
       s  
y     : vector de salida de la red 
 s                           s        s  2 
     E     : 2
1 I ŷ – y I  medida del error cuadrático.         
Para la muestra 
S     : conjunto de muestras (entrenamiento)

---

## Página 27

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática
2
1
( )
( )
1 ( ( )
( ))
2
(
)
(
1)
( )
( ( )
( ))
( )
N
j
j
i
j
i
y t
W X t
J
d t
y t
J
d
w X
X
w
W t
W t
d t
y t
X t


















---

## Página 28

Universidad de Santiago de Chile                                                                                             
Departamento de Ingeniería Informática
Ingeniería Neuronal                                                                                                          
Magíster en Ingeniería Informática

---

