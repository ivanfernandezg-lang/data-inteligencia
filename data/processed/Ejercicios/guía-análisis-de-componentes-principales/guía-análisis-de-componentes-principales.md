# Guía - Análisis de Componentes Principales

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 1 de 15 
 
Guía de ejercicios Capítulo II 
Análisis de Componentes Principales 
1. Objetivos de la Unidad 
# 
Descripción 
Preguntas 
1. 
Describir los fundamentos matemáticos del modelo Análisis de Componentes 
Principales (PCA).  
Todas 
2. 
Aplicar el modelo PCA en un conjunto de datos perteneciente a un problema 
específico. 
Todas

---

## Página 2

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 2 de 15 
 
2. Preguntas 
P1. Comportamiento de consumo alimenticio 
Un estudio del consumo de diferentes familias francesas intenta una caracterización mediante 
análisis de componentes principales. Las familias (sujetos) se caracterizan por su condición 
socioeconómica, clasificando el tipo de trabajo de los jefes de hogar, y por sus tamaños 
considerando el número de hijos. Los jefes de hogar tienen las siguientes características: (MA#) 
trabajador manual, (EM#) empleado, (PF#) profesional. Donde el símbolo # puede tomar los valores 
2, 3, 4 o 5 y representa el número de hijos de las familias. Se mide el consumo promedio de los 
siguientes productos (atributos o variables originales x1): Pan, Verduras, Frutas, Carnes, Aves, 
Lácteos y Vinos. 
La matriz de correlación de los productos es la siguiente: 
 
Pan 
Verduras 
Frutas 
Carnes 
Aves 
Lácteos 
Vinos 
Pan 
1,00 
 
 
 
 
 
 
Verduras 
0,59 
1,00 
 
 
 
 
 
Frutas 
0,20 
0,87 
1,00 
 
 
 
 
Carnes 
0,32 
0,89 
0,96 
1,00 
 
 
 
Aves 
0,25 
0,83 
0,93 
0,98 
1,00 
 
 
Lácteos 
0,86 
0,66 
0,33 
0,37 
0,23 
1,00 
 
Vinos 
0,30 
-0,35 
-0,49 
-0,44 
-0,40 
-0.40 
1,00 
 
Después de realizar un análisis de componentes principales, los valores propios para las 
componentes son λ1=4,339; λ2=1,829; λ3=0,625; λ4=0,502; λ5=0,393; λ6=0,099; λ7=0,083 
Los vectores propios las dos primeras componentes se muestran en la siguiente tabla: 
 
Componente 1 
Componente 2 
Pan 
-0,497 
0,841 
Verduras 
-0,972 
0,131 
Frutas 
-0,931 
-0,277 
Carnes 
-0,963 
-0,19 
Aves 
-0,912 
-0,265

---

## Página 3

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 3 de 15 
 
Lácteos 
-0,584 
0,707 
Vinos 
0,425 
0,649 
 
La distribución de los grupos familiares en el espacio de las dos primeras componentes principales 
se muestra en la siguiente figura: 
 
a) Determine el porcentaje de información que se pierde en el estudio con solo las dos primeras 
componentes. 
b) Intente una caracterización de las componentes inspeccionando sólo la distribución de las 
familias en el plano de las dos componentes. 
c) Dibuje en forma aproximada los productos consumidos (atributos o variables originales) en 
el espacio de las componentes. 
d) Asocie cada componente a los productos consumidos. 
e) Intente relacionar los productos consumidos por las familias y sus condiciones 
socioeconómicas y/o tamaños. 
 
 
 
  
Comp. 1 
Comp. 2 
P
EM
PF
MA
MA
PF
PF
MA
MA
EM
EM
EM

---

## Página 4

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 4 de 15 
 
P2. Caracterización billetes falsos 
Para caracterizar billetes falsos los bancos suizos realizaron un análisis que consistía en tomar 
medidas de los billetes. Para el análisis tenía tres grupos diferentes de billetes. Originales de papel, 
originales de plástico y billetes falsos. Cada billete fue caracterizado por las siguientes variables:  
LON 
: 
Longitud del billete. 
LD 
: 
Largo de la Diagonal del billete. 
AI 
: 
Ancho Izquierdo del billete. 
AD 
: 
Ancho Derecho del billete. 
AMI 
: 
Ancho Margen Inferior del billete 
AMS 
: 
Ancho Margen Superior del billete. 
A continuación, se realizó un análisis de componentes principales con los siguientes 
resultados:  
- Valores propios: 2,58; 1,34; 0,76; 0,56; 0,50; 0,26. 
- Vectores propios para las dos primeras componentes: 
 
Componente 1 
Componente 2 
LON 
0,395 
0,799 
LD 
0,207 
0,345 
AI 
0,445 
-0,263 
AD 
0,411 
-0,375 
AMI 
0,347 
-0,072 
AMS 
0,560 
-0,163 
 
La distribución de los diferentes tipos de billetes se muestra en la siguiente figura (originales de 
papel en círculos, originales de plástico en cuadrados y falsos en triángulos):

---

## Página 5

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 5 de 15 
 
 
 
 
Se realizó un trabajo similar con monedas midiendo 6 variables de tamaño de éstas y los valores 
propios del análisis fueron los siguientes: 1,96; 1,54; 1,09; 0,73; 0,40; 0,28. 
a) Determine el porcentaje de validez del análisis. 
b) Interprete cada una de las componentes 
c) Identifique las principales características de los billetes originales. 
d) Determine si existen diferencias entre las falsificaciones. 
e) Para el análisis de las monedas, ¿se logrará tener una precisión similar a la de los billetes? 
 
 
 
  
CP
CP2

---

## Página 6

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 6 de 15 
 
P3. Caracterización servicios hospitalarios 
Un estudio del Hospital de Andalucía (España) analizó 22.846 ingresos para intentar caracterizar 
los diferentes servicios (o unidades) del hospital. Los servicios analizados fueron los siguientes: 
Medicina 
Interna, 
Ginecología, 
Pediatría, 
Cirugía, 
Traumatología, 
Urología, 
Digestivo, 
Otorrinolaringología, Cardiología, Neurología, Hematología, Oftalmología y Psiquiatría. Para 
caracterizar los servicios se midieron 7 variables: 
NI 
: Número de ingresos. 
MO 
: Índice de mortalidad. 
RE 
: Número de reingresos al servicio (por el mismo diagnóstico). 
NE 
: Número de consultas externas al servicio. 
ICM  
: índice promedio de la complejidad de los pacientes admitidos. 
ES 
: Número de estancias por servicio (promedio de días cama usados en cada servicio). 
IF 
: Índice de funcionalidad (representa la eficiencia del servicio) 
El resultado del análisis de componentes principales muestra los siguientes resultados para las dos 
primeras componentes: 
Valor propio 1: 2,558 
Valor propio 2: 1,829 
Vector propio 1: [0,860; 0,421; -0,406; -0,250; -0,562; 0,820; 0,663] 
Vector propio 2: [-0,066; 0,747; 0,670; 0,388; 0,635; 0,508; 0,078]

---

## Página 7

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 7 de 15 
 
 
a) Determine la validez del análisis. 
b) Ubique las variables medidas en el plano de las dos primeras componentes. 
c) Interprete cada componente. 
d) Clasifique los servicios según la interpretación de cada componente. 
e) Seleccione los servicios con mayor carga de trabajo cualitativa y cuantitativa. 
f) Determine los servicios más eficientes.

---

## Página 8

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 8 de 15 
 
P4. Análisis sector lechero 
En un estado venezolano se utilizó ACP para analizar la situación del sector lechero. Las variables 
utilizadas fueron: SUP: superficie total de la hacienda; VACA: número total de vacas; SANI: índice 
sanitario; INST: índice de las instalaciones; MAQ: índice de maquinarias; PROM: Promedio de la 
lecha/vaca. Los resultados del ACP fueron los siguientes: 
Valores propios: 1,794; 1,341. 
Vectores propios ponderados por la raíz de cada valor propio: 
 
Componente 1 
Componente 2 
SUP 
0,79 
0,10 
VACA 
0,76 
0,40 
SANI 
0,44 
-0,48 
INST 
0,32 
-0,48 
MAQ 
0,53 
-0,26 
PROM 
-0,01 
-0,80 
 
Determine una caracterización de las componentes principales, al examinar la relación con las 
variables originales. 
Al graficar las haciendas en el plano de las dos primeras componentes principales se pueden 
caracterizar 8 tipos de haciendas con problemas particulares, como se muestra en la figura. Utilice 
esta información para identificar los tipos de haciendas. Determine además el porcentaje de validez 
del estudio.

---

## Página 9

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 9 de 15

---

## Página 10

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 10 de 15 
 
Respuestas 
P1. Comportamiento de consumo alimenticio 
a) Rpta.: 21,6% 
b) Rpta.: Al caracterizar los componentes a partir de las distribuciones de los sujetos en el 
plano, es posible apreciar que en cuadrante I (rango de valores CP1 y CP2 positivos) 
predominan los trabajadores manuales (#MA), y en menor número los empleados (#EM). El 
cuadrante II (rango de valores CP1 negativos y CP2 positivos) se sitúan en menor cantidad 
empleados (#EM) y trabajadores manuales (#MA) por igual, siendo estos últimos los sujetos 
con los valores más altos de CP2 de todo el análisis. En cuadrante III (rango de valores CP1 
y CP2 negativos) se sitúan sólo sujetos profesionales (#PF). Finalmente, el cuadrante IV 
(con rango de valores CP1 positivos y CP2 negativos) es el más heterogéneo dado que se 
encuentran los tres tipos de jefes de hogares predominando los empleados.   Data la 
homogeneidad de las muestras en los cuadrantes I y III, al suponer un orden de ingresos 
decreciente de los tres tipos de jefes de hogares (#MA < #EM < #PF), relacionamos valores 
positivos de ambos componentes a sujetos con menores ingresos, y los negativos a mayores 
ingresos. También, podemos visualizar una separación lineal entre los 3 tipos de jefes de 
hogares de acuerdo a su consumo, por rectas con pendientes negativas. 
 
Dado que el análisis se basa en el consumo de distintos productos alimenticios, a priori se 
presume que la dirección de los vectores propios correspondientes a los alimentos más 
caros como las carnes apuntarán al cuadrante IV. 
c) Rpta.:

---

## Página 11

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 11 de 15 
 
 
 
d) Rpta.: De acuerdo con la visualización de los vectores propios y componentes, los vectores 
correspondientes a carnes, aves, fruta, y verduras tienen una mayor proximidad al rango de 
valores negativos del componente 1. Los lácteos y el pan se ubican en el cuadrante III 
(valores CP1 negativos y CP2 positivos). De acuerdo con la evaluación previa, se situaría 
como productos de valor medio. Finalmente los vinos se relacionan a los valores positivos 
de ambos componentes. 
e) Rpta.: A partir del plano podemos inferir que los Profesionales (jefes de familia con mayores 
ingresos) consumen carne, aves, verduras y frutas. Los empleados representan el segmento 
con más hijos menores dado el consumo de leche y pan, y los trabajadores manuales 
consumen en mayor cantidad vino.

---

## Página 12

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 12 de 15 
 
P2. Caracterización billetes falsos 
a) Varianza explicada =  
𝑆𝑆𝑆𝑆𝑆𝑆(𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇)
𝑠𝑠𝑠𝑠𝑠𝑠(𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇)∗100
 
 
 
 
        = 
2,58 + 1,34
(2,58 + 1,34 + 0,76 + 0,56 + 0,50 + 0,26)∗100 = 65,33333333% 
 
b) Componente 
1: 
Forma 
del 
billete 
/ 
Márgenes 
internos 
(AMI 
+ 
AMS) 
Componente 2: Tamaño del billete (LON + LD) 
 
 
c) Se podría decir que los billetes originales tienen mayores márgenes internos. Así, los billetes 
de papel tienen menos márgenes que los de plástico. Por otro lado, los billetes de papel son 
considerablemente 
más 
grandes 
que 
los 
billetes 
de 
plástico 
 
d) Considerando el análisis que se hizo para los billetes originales y las componentes (forma - 
tamaño), es posible apreciar como entre los billetes falsos se tienen claras diferencias de 
tamaño. Esto se podría interpretar como que los billetes falsos que se encuentran arriba del 
eje CP1 podrían buscar imitar a los de papel, mientras los que se encuentran debajo del 
mismo 
eje, 
podrían 
buscar 
imitar 
a 
los 
de 
plástico. 
 
e) Varianza 
explicada 
= 
1,96 + 1,54
(1,96+1,54+1,09+0,73+0,40+0,28)∗100 =  58,83%

---

## Página 13

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 13 de 15 
 
Dado que para el análisis con las monedas se tiene un 58,83% de la varianza explicada, 
versus un 65,33% en los billetes, se podría indicar que se tiene un 6.5% menos de esta 
varianza para las monedas. Dependiendo de la importante y rigurosidad de la investigación, 
esto podría ser un margen importante, pero, aun así, se podría decir que se tendría una 
precisión similar.

---

## Página 14

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 14 de 15 
 
P3. Caracterización servicios hospitalarios 
a) Rpta.: XX % 
b) Rpta.: 
 
c) Rpta.: El componente 1 se relaciona con los servicios hospitalarios de mayor demanda; mientras que 
el componente 2 en su rango de valores positivos se relaciona con los servicios hospitalarios con mayor 
probabilidad de hospitalización, en forma contraria sus valores negativos se asocian a prestaciones 
ambulatorias. 
d) Rpta.: De acuerdo con el análisis de componentes Medicina Interna es el servicio más demandado 
con mayor hospitalización; Cirugía posee menor demanda y grado de hospitalización; Traumatología, 
Urología, son servicios ambulatorios con menor demanda que Ginecología, Pediatría. El servicio 
Digestivo posee una baja demanda, pero una alta probabilidad de mortandad; Otorrinolaringología, 
Cardiología, Oftalmología son servicios con menor demanda y riesgo; mientras que los servicios de 
Psiquiatría, Neurología, Hematología, poseen baja demanda pero un alto nivel de complejidad y 
reingreso número de consultas externas. 
e) Rpta.: Los servicios con mayor carga de trabajo cualitativa, y cuantitativa son Medicina Interna, 
Ginecología y Pediatría. 
f) Rpta.: Los servicios más eficientes corresponden a Cirugía y Traumatología.

---

## Página 15

Facultad de Ingeniería 
Departamento de Ingeniería 
Informática 
INTELIGENCIA COMPUTACIONAL 
Guía de ejercicios Capítulo II  
Análisis de Componentes Principales 
 
 
 
Página 15 de 15 
 
P4. Análisis sector lechero 
a) Características Componentes: 
CP1: Área utilizada por vaca  
CP2: Nivel industrialización  
 
 
b) Tipos de haciendas: 
A y C = Haciendas matadero 
B = Haciendas lechera 
D y E = Haciendas multipropósito 
H y G = Haciendas muy pequeñas 
F = Haciendas Crianza, pastoreo y engorde 
 
c) Faltan algunos valores propios (?)

---

