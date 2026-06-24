# 1 Introduccion

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Curso de Fundamentos de Aprendizaje 
Profundo
Introducción 
Universidad de Santiago de Chile
Departamento de Ingeniería Informática
Marzo 2019
Dr. Gonzalo Acuña L.

---

## Página 2

Temario
I. Motivación
II. La neurona biológica 
III. La neurona artificial
IV. Aprendizaje
V. Redes Neuronas Artificiales
VI. Aprendizaje Profundo
VII. Aplicaciones
VIII. Reseña Histórica
Gonzalo Acuña L
USACH-DIINF

---

## Página 3

I.
Motivación
Gran facilidad de seres cognitivos para llevar a 
cabo tareas como:
Reconocimiento de formas
Procesamiento de voz, imágenes, etc.
Dificultad de computadores tipo Von Neumann 
para desempeñar adecuadamente esas tareas.
Interés (al igual que en la evolución técnica 
anterior) en “copiar” el “secreto” de los seres 
cognitivos.
Gonzalo Acuña L
USACH-DIINF

---

## Página 4

Por lo anterior pareció importante 
comprender y emular los mecanismos 
asociados al éxito de los seres cognitivos:
Paralelismo y alta conectividad
Complejidad
Nace una de las ramas de la Inteligencia 
Artificial: Redes Neuronales Artificiales
Gonzalo Acuña L
USACH-DIINF

---

## Página 5

Nuevo paradigma (no-algorítmico) para 
el procesamiento de la información 
(neurocomputación): de aprendizaje y 
adaptación, procesamiento distribuido y 
paralelo.
Nuevas herramientas (computadores más 
rápidos, más baratos)
Entusiasmo inicial, edad media y 
renacimiento.
Gonzalo Acuña L
USACH-DIINF

---

## Página 6

Actualmente aplicaciones en todas las áreas
En aproximación: control, automatización 
modelamiento, predicción, identificación
En clasificación:  reconocimiento patrones, 
extracción de características, cuantización
En el futuro: mayor prudencia y más apoyo 
teórico. Problemas abiertos:  
generalización…
Gonzalo Acuña L
USACH-DIINF

---

## Página 7

II. La Neurona 
Biológica 
Gonzalo Acuña L
USACH-DIINF

---

## Página 8

Gonzalo Acuña L
USACH-DIINF

---

## Página 9

Potencial de reposo (- 60 mV)
Potencial de receptor (información exterior) 
depolarización + 10 mV
Propagación pasiva en membrana  
(amplitud y duración proporcionales a 
estímulo) 
Si importante potencial acción
Gonzalo Acuña L
USACH-DIINF

---

## Página 10

Potencial de acción (+ 100 mV)
Tren de potenciales de frecuencia 
proporcional a amplitud y duración de 
potencial receptor.
Propagación activa en axón, desde cono 
axónico hasta sinapsis.
Na+  adentro.  Después:  K+ afuera.
Gonzalo Acuña L
USACH-DIINF

---

## Página 11

Sinapsis (Ramón y Cajal,  s. XIX)
Retardo en la transmisión de impulso 
modulación por neurotransmisores 
plasticidad
Tipos sinapsis:  axón-dendrita; axón soma; 
axón-axón.
Tipos sinapsis: excitatoria,  inhibitoria.
Gonzalo Acuña L
USACH-DIINF

---

## Página 12

Interconexión
1010 neuronas
Algunas neuronas con hasta 100.000 
sinapsis
Gonzalo Acuña L
USACH-DIINF

---

## Página 13

Gonzalo Acuña L
USACH-DIINF

---

## Página 14

Gonzalo Acuña L
USACH-DIINF

---

## Página 15

III. Neurona artificial
Autómata caracterizado por:
Un estado interno
Señales de entrada
Funciones de agrupamiento y activación
Tipos de neuronas:
Producto punto
Distancia
Gonzalo Acuña L
USACH-DIINF

---

## Página 16

Gonzalo Acuña L
USACH-DIINF

---

## Página 17

Modelo de McCulloch 
y Pitts (1943)
Gonzalo Acuña L
USACH-DIINF

---

## Página 18

a = x1 w1 + x2 w2 + …
Si a > Ө y=1
Si a < Ө y=0
Con este modelo se puede construir cualquier 
función lógica (Booleana)
Con pesos convenientemente determinados se 
podría simular cualquier computador digital
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

AND de 4 entradas
Threshold = 1.5
Threshold = 1.5
Threshold = 1.5
All weights = 1 and all outputs = 1 if active;   0 otherwise
Inputs
Inputs
Outputs
Gonzalo Acuña L
USACH-DIINF

---

## Página 22

Funciones de Activación
Gonzalo Acuña L
USACH-DIINF

---

## Página 23

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

Rectifier Linear Unit (ReLU)
Gonzalo Acuña L
USACH-DIINF

---

## Página 27

IV.Aprendizaje
Gonzalo Acuña L
USACH-DIINF

---

## Página 28

Capacidad de una neurona (o red neuronal) 
para ajustar las conexiones (pesos) de modo 
de obtener una respuesta deseada o que 
satisfaga ciertos criterios
Gonzalo Acuña L
USACH-DIINF

---

## Página 29

Regla de Hebb (1949)
Cuando una neurona i repetida y 
persistentemente excita a una neurona j
algún proceso de crecimiento o metabólico 
se produce en una o ambas neuronas de 
modo que la eficiencia de excitación de i
sobre j aumenta.  activación simultanea 
o síncrona 
Gonzalo Acuña L
USACH-DIINF

---

## Página 30

Regla de Hebb (1949)
wijnew = wijold + α xi yj
Gonzalo Acuña L
USACH-DIINF

---

## Página 31

V. Redes de 
Neuronas 
Artificiales (RNA)
Gonzalo Acuña L
USACH-DIINF

---

## Página 32

Consisten en un conjunto de neuronas 
interconectados entre sí
Queda completamente caracterizado por:
Número de neuronas
Arquitectura de interconexión
Valor de los pesos
Funciones de agrupamiento y activación
Gonzalo Acuña L
USACH-DIINF

---

## Página 33

Las RNA pueden trabajar en dos modos:
Aprendizaje: adapta sus pesos; su arquitectura; sus 
funciones de agrupamiento y activación
Reconocimiento o simulación: se usa la RNA para 
procesar información
Aprendizaje de RNA:
Supervisado (vía ejemplos)
No-Supervisado 
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

Entrenamiento
Problema
Supervisado
No-Supervisado
Memorias
Asociativas
Hopfield
Clasificación
Predicción
Interpolación
Adaline-
Perceptron
MLP – TDNN
LVQ – RBF
Cuantización
LVQ
Kohonen
ART
Gonzalo Acuña L
USACH-DIINF

---

## Página 37

Entrenamiento
Problema
Supervisado
No-Supervisado
Memorias
Asociativas
Hopfield
Clasificación
Predicción
Interpolación
Adaline-
Perceptron
MLP – TDNN
LVQ – RBF
Cuantización
LVQ
Kohonen
ART
Gonzalo Acuña L
USACH-DIINF

---

## Página 38

VI. Aprendizaje Profundo

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

Convolutional NN (CNN)
Gonzalo Acuña L
USACH-DIINF

---

## Página 42

Long Short Term Memory
(LSTM)
Gonzalo Acuña L
USACH-DIINF

---

## Página 43

Autoencoders
Gonzalo Acuña L
USACH-DIINF

---

## Página 44

Generative Adversarial
Neural Nets (GAN)
Gonzalo Acuña L
USACH-DIINF

---

## Página 45

Transformers
Gonzalo Acuña L
USACH-DIINF

---

## Página 46

VII Aplicaciones
Gonzalo Acuña L
USACH-DIINF

---

## Página 47

Gonzalo Acuña L
USACH-DIINF

---

## Página 48

Gonzalo Acuña L
USACH-DIINF

---

## Página 49

VIII 
Reseña Histórica
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

