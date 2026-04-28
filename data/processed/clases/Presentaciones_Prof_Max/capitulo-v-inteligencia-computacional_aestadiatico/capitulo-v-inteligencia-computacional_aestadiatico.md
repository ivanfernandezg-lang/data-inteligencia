# Capitulo V Inteligencia Computacional_AEstadiatico

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

23-03-2017
1
Inteligencia Computacional
Capítulo V
“Análisis Estadístico”
Profesor: Dr. Max Chacón
Universidad de Santiago de Chile
Facultad de Ingeniería
Depto. de Ingeniería Informática
Objetivos:
(Repaso: Dominar los métodos de clasificación basados 
en razón de probabilidades (logística))
– Presentar métodos de clasificación paramétrico y no
paramétrico más conocidos.
– Presentar un método de clasificación basados en
discriminación lineal.
– Comprender
el
método
no
paramétrico
de
discriminación
(clasificación
y
regresión)
mas
simple.
– Comprender la metodología de evaluación de la
clasificación binaria.

![Imagen](images\page001_img01.png)

---

## Página 2

23-03-2017
2
Repaso Regresión Logística
Aquí se considera el caso binario, esto es la variable
dependiente o respuesta y es una variable binaria y∈{0,1}.
Es posible también generalizar a m clases.
La relación con el modelo es mediante la probabilidad de
ocurrencia
de
esta
variable
p=Pr(y=1)∈[0,1]
o 1-
p=Pr(y=0).
Para realizar la estimación
de parámetros
de este
problema no-lineal, se requiere maximizar la probabilidad
conjunta.
Pr(yi=1^ yj=0) ∀i,j.
Principio de máxima verosimilitud.
El estimador de verosimilitud para esta probabilidad es:
La función a maximizar es logaritmo del estimador de
verosimilitud.
con  
(
)



−
−
+
=
−
∑
∏
=
=
−
n
i
i
i
i
i
n
i
y
i
y
i
y
y
i
i
1
1
1
)
1
ln(
)
1(
ln
exp
)
1(
π
π
π
π
(
)
∑
=
−
−
+
=
n
i
i
i
i
i
i
i
y
y
y
l
1
)
1
ln(
)
1(
ln
)
,
(
π
π
π
0
)
,
(
=
∂
∂
i
i
iy
l
β
π
β
π
r
vT
ix
i
e−
+
=
1
1

![Imagen](images\page002_img01.png)

---

## Página 3

23-03-2017
3
Esta ecuación resulta ser trascendental y se debe recurrir a 
métodos iterativos como el método de optimización de 
Newton,  variación del método de Newton-Raphson
(xn+1=xn-f(xn)/f’(xn)) para ecuaciones trascendentales.
con n el índice de las iteraciones,
• H es la matriz de segundas derivadas (Hessiana) de l,
• J es el vector de las primeras derivadas (Jacobiana) de l,
)
1
(
)
1
(
)
1
(
)
1
(
−
−
−
−
+
=
n
n
n
n
n
J
H
H
r
v
v
β
β








∂
∂
∂
=
k
j
jk
l
h
β
β
2
j
j
l
j
β
∂
∂
=
Este modelo aproxima la combinación lineal de las
variables independientes x y los parámetros β a la
probabilidad p mediante una función sigmoide.
π
∑xβ
1
Éste es uno de los modelos mas utilizados cuando la
variable de salida es binaria como es el caso de la
mortalidad, predicción de
la probabilidad de falla de
una máquina o equipo, o probabilidad de ocurrencia de
eventos en general, cuando influyen muchas causas.

![Imagen](images\page003_img01.png)

---

## Página 4

23-03-2017
4
- Interpretación de la regresión logística
En el caso lineal los coeficientes βi representan el
incremento de la variable respuesta y, para un aumento
unitario del predictor xi.
En
la
regresión
logística
el
coeficiente
puede
ser
interpretado como el cambio en la función logística para
un incremento unitario en el predictor. Considere:
Aplicando lo mismo al caso en que la variable xi es cero.
)
1
/(
1
)
1
/(
)1
(
1
)1
(
)
...
...
(
)
...
...
(
)
...
...
(
1
1
0
1
1
0
1
1
0
p
p
i
p
p
i
p
p
i
x
x
x
x
x
x
i
i
e
e
e
x
x
β
β
β
β
β
β
β
β
β
β
β
β
π
π
+
+
+
+
+
=
=
−
=
)
...
...
(
1
1
0
)1
(
1
)1
(
p
p
i
x
x
i
i
e
x
x
β
β
β
β
π
π
+
=
=
−
=
Se tiene
La razón entre estas dos proporciones se denomina razón
de probabilidades o razón de chances (odds ratio).
Esto representa la influencia (o la pendiente) de cada
variable en la probabilidad final.
También es de interés el numerador del OR, denominado
Razón de Riesgo:
Cuanto crese el riesgo (se multiplica) al considerar xi.
)
...
...
(
1
1
1
1
0
)
0
(
1
)
0
(
p
p
i
i
x
x
i
i
e
x
x
β
β
β
β
β
π
π
+
−+
+
=
=
−
=
)
1
/(
1
)
1
/(
)
(
1
)
0
(
)
...
...
(
)
...
...
(
)
...
...
(
1
1
1
1
0
1
1
1
1
0
1
1
1
1
0
p
p
i
i
p
p
i
i
p
p
i
i
x
x
x
x
x
x
i
i
e
e
e
o
x
x
β
β
β
β
β
β
β
β
β
β
β
β
β
β
β
π
π
+
−
+
−
+
−
+
+
+
+
+
+
+
+
=
=
−
=
)
...
...
(
)
...
...
(
1
1
1
1
0
1
1
0
)
0
(
)
0
(
1
)1
(
1
)1
(
 
p
p
i
i
p
p
i
x
x
x
x
i
i
i
i
e
e
x
x
x
x
ratio
odds
β
β
β
β
β
β
β
β
β
π
π
π
π
+
−+
+
+
=
=
=
−
=
−
=
=
)
(
 
i
e
Ratio
Odds
OR
β
=
=
)
...
...
(
1
1
0
)1
(
1
)1
(
p
p
i
x
x
i
i
e
x
x
RR
β
β
β
β
π
π
+
=
=
−
=
=

![Imagen](images\page004_img01.png)

---

## Página 5

23-03-2017
5
7.4.2. Evaluación regresión logística
-Evaluación de los coeficientes.
Similar al caso de la regresión lineal, es posible
contrastar (docimar) la hipótesis de que un coeficiente
aislado es distinto de 0, y sigue una distribución normal
de media 0 y varianza 1.
El contraste se realiza utilizando la el estadístico de
Wald por el cociente entre el valor del coeficiente ( ) y
su correspondiente error estándar.
Esto es:
El cual sigue una distribución normal. Para aceptar H0
Se quiere:
)
ˆ
(
 
ˆ
i
i
Wald
Est
Err
Z
β
β
=
0
ˆ
 :
0
ˆ
 :
0
≠
=
i
a
i
H
H
β
β
α
<
<
)
(
Wald
z
z
P
iβˆ
-Evaluación del modelo
Similar al caso de la regresión lineal donde se mide la
eficiencia de la regresión por la razón entre los errores
cuadrados de la regresión y la suma de errores cuadrados
totales, que resulta en una distribución F.
Análogo al anterior aquí se compara la razón de la
verosimilitud
del
modelo
saturado
(con
todos
los
predictores) y el modelo nulo (con sólo la intercepción):
Con H0:
β1= β2 … βp=0
Ha:
los βi≠0
Se denomina el test de la razón de verosimilitud y se
obtiene usando una distribución de χ2 con p grados de
libertad.
)
ln
(ln
2
ln
2
0
0
2
L
L
L
L
G
−
=






=
n
n
n
n
n
n
L
ln
ln
ln
ln
0
0
1
1
0
−
−
=

![Imagen](images\page005_img01.png)

---

## Página 6

23-03-2017
6
Ej: Modelo para predecir enfermedad cardiaca, datos de Cliveland
Se cuenta con 296 casos obtenidos de la ciudad de Cliveland, con 14
atributos (originalmente 76). 13 características que inciden o son causa
de enfermedad cardiaca y la clase que corresponde a enfermedad o no.
Los atributos son:
Nº
Nombre
Característica
Nº
Nombre
Característica
1
age
Edad (años)
8
thalach
Infartos previos
2
sex
Sexo (0,1)
9
exang
Angina inducida 
por ejercicio (0,1)
3
cp
Dolor Pectoral (1-4)
10
oldpeak
Depresión segm. 
ST,  por ejercicio
4
trestbps
Presión Sanguínea 
(mmHg)
11
slope
Pendiente segm. 
ST por ejerc. (1-3)
5
chol
Colesterol Sérico (mg/dl)
12
ca
Nº vasos 
coloreados por 
fluoroscopia (0-3)
6
fbs
Glucosa ayunas (0,1)
13
thal
Defectos cardiacos 
en ejercicio (1-3)
7
restecg
ECG reposo (0-2)
14
num
Diagnostico de 
enfermedad (0,1)
Solución:
Se transforman los datos en formato .rtff, se leen con el programa
KNIME y se realiza regresión logística con atributo num como la clase
Logit
Variable 
Coeff. Std. Err. z-score 
P>|z| 
1
age
0.0152 
0.025 
0.6061 
0.5444 
2
sex=male
-1.672 
0.5451 -3.0674 
0.0022
3.1
cp=atyp_angina
0.7182 
0.5676 
1.2653 
0.2058
3.2
cp=non_anginal
1.7939 
0.5083 
3.5293 
0.0004
3.3
cp=typ_angina
2.0447 
0.6718 
3.0437 
0.0023
4
trestbps
-0.0225 
0.0114 -1.9823 
0.0474
5
chol 
-0.0042 
0.0041 -1.0278 
0.304 
6
fbs=t 
0.591 
0.6128 
0.9644 
0.3349 
7.1
restecg=normal 
0.4175 
0.3879 
1.0761 
0.2819 
7.2
restecg=st_t_wave_abnormality -0.4738 
2.4689 -0.1919 
0.8478 
Cleveland-14-heart-disease Logistic Regression, KNIME
Log-likelihood = -93.5797,  Number of iterations = 30, Logit 50
Las variables mas significantivas tienen p<0.05.

### Tabla 1 (Página 6)

| Nº | Nombre | Característica | Nº | Nombre | Característica |
| --- | --- | --- | --- | --- | --- |
| 1 | age | Edad (años) | 8 | thalach | Infartos previos |
| 2 | sex | Sexo (0,1) | 9 | exang | Angina inducida
por ejercicio (0,1) |
| 3 | cp | Dolor Pectoral (1-4) | 10 | oldpeak | Depresión segm.
ST, por ejercicio |
| 4 | trestbps | Presión Sanguínea
(mmHg) | 11 | slope | Pendiente segm.
ST por ejerc. (1-3) |
| 5 | chol | Colesterol Sérico (mg/dl) | 12 | ca | Nº vasos
coloreados por
fluoroscopia (0-3) |
| 6 | fbs | Glucosa ayunas (0,1) | 13 | thal | Defectos cardiacos
en ejercicio (1-3) |
| 7 | restecg | ECG reposo (0-2) | 14 | num | Diagnostico de
enfermedad (0,1) |

### Tabla 2 (Página 6)

| Logit | Variable | Coeff. | Std. Err. | z-score | P>|z| |
| --- | --- | --- | --- | --- | --- |
| 1 | age | 0.0152 | 0.025 | 0.6061 | 0.5444 |
| 2 | sex=male | -1.672 | 0.5451 | -3.0674 | 0.0022 |
| 3.1 | cp=atyp_angina | 0.7182 | 0.5676 | 1.2653 | 0.2058 |
| 3.2 | cp=non_anginal | 1.7939 | 0.5083 | 3.5293 | 0.0004 |
| 3.3 | cp=typ_angina | 2.0447 | 0.6718 | 3.0437 | 0.0023 |
| 4 | trestbps | -0.0225 | 0.0114 | -1.9823 | 0.0474 |
| 5 | chol | -0.0042 | 0.0041 | -1.0278 | 0.304 |
| 6 | fbs=t | 0.591 | 0.6128 | 0.9644 | 0.3349 |
| 7.1 | restecg=normal | 0.4175 | 0.3879 | 1.0761 | 0.2819 |
| 7.2 | restecg=st_t_wave_abnormality | -0.4738 | 2.4689 | -0.1919 | 0.8478 |

![Imagen](images\page006_img01.png)

---

## Página 7

23-03-2017
7
Valor p, continuación:
Logit
Variable 
Coeff. Std. Err. 
z-score 
P>|z| 
8
thalach
0.018 
0.0112 
1.6034 
0.1088 
9
exang=yes 
-0.775 
0.4444 
-1.7439 
0.0812
10
oldpeak
-0.3676 
0.2316 
-1.5872 
0.1125 
11.1
slope=flat 
-0.6771 
0.8479 
-0.7985 
0.4246 
11.2
slope=up 
0.5866 
0.9185 
0.6387 
0.523 
12
ca
-1.3642 
0.2857 
-4.7747 
1.80E-6
13.1
thal=normal 
-0.0423 
0.791 
-0.0535 
0.9574 
13.2
thal=reversable_defect 
-1.4582 
0.7779 
-1.8744 
0.0609
Constant
2.8052 
2.8829 
0.973 
0.3305 
Observar Log-likelihood = ln(L)= -93.5797
Modelo 0: n0=160, n1=136, n=296
G=2(-93.58-(160ln160+136ln136-296ln296))
G=2(-93.58+1540.44)=2893.72. Dócima p(
)=0.000
Modelo muy bueno p<<0.05.
Pero hay que ver los test de coeficientes, Zwald, Eliminar
variables donde pWald>0.05.
2
12
χ
Usando KNIME para las 6 variables con p<0.05:
Cleveland-6-heart-disease Logistic Regressio
Log-likelihood = -108.2666, Number of iterations = 30
Logit
Variable 
Coeff. 
Std. Err. 
z-score 
P>|z| 
1
sex=male
-1.0866 
0.4425 
-2.4554 
0.0141 
2.1
cp=atyp_angina
1.3645 
0.5185 
2.6316 
0.0085 
2.2
cp=non_anginal 
1.7781 
0.4467 
3.9807 
6.87E-5 
2.3
cp=typ_angina 
1.645 
0.5924 
2.7771 
0.0055 
3
trestbps 
-0.0188 
0.0098 
-1.9238 
0.0544
4
exang=yes 
-1.1993 
0.3933 
-3.0495 
0.0023 
5
ca 
-1.2246 
0.2228 
-5.4976 
3.85E-8 
6.1
thal=normal 
0.7039 
0.71 
0.9913 
0.3215 
6.2
thal=reversable_defect 
-1.0013 
0.7029 
-1.4245 
0.1543 
Constant 
3.7425 
1.6127 
2.3207 
0.0203 
Observar Log-likelihood = ln(L)= -108.5797
Modelo 0: n0=160, n1=136, n=296
G=2(-108.58+1540.44)=2863.72. Dócima p(
)=0.000
Modelo muy bueno p<<0.05.
2
5
χ

### Tabla 1 (Página 7)

| Logit | Variable | Coeff. | Std. Err. | z-score | P>|z| |
| --- | --- | --- | --- | --- | --- |
| 8 | thalach | 0.018 | 0.0112 | 1.6034 | 0.1088 |
| 9 | exang=yes | -0.775 | 0.4444 | -1.7439 | 0.0812 |
| 10 | oldpeak | -0.3676 | 0.2316 | -1.5872 | 0.1125 |
| 11.1 | slope=flat | -0.6771 | 0.8479 | -0.7985 | 0.4246 |
| 11.2 | slope=up | 0.5866 | 0.9185 | 0.6387 | 0.523 |
| 12 | ca | -1.3642 | 0.2857 | -4.7747 | 1.80E-6 |
| 13.1 | thal=normal | -0.0423 | 0.791 | -0.0535 | 0.9574 |
| 13.2 | thal=reversable_defect | -1.4582 | 0.7779 | -1.8744 | 0.0609 |
|  | Constant | 2.8052 | 2.8829 | 0.973 | 0.3305 |

### Tabla 2 (Página 7)

| Logit | Variable | Coeff. | Std. Err. | z-score | P>|z| |
| --- | --- | --- | --- | --- | --- |
| 1 | sex=male | -1.0866 | 0.4425 | -2.4554 | 0.0141 |
| 2.1 | cp=atyp_angina | 1.3645 | 0.5185 | 2.6316 | 0.0085 |
| 2.2 | cp=non_anginal | 1.7781 | 0.4467 | 3.9807 | 6.87E-5 |
| 2.3 | cp=typ_angina | 1.645 | 0.5924 | 2.7771 | 0.0055 |
| 3 | trestbps | -0.0188 | 0.0098 | -1.9238 | 0.0544 |
| 4 | exang=yes | -1.1993 | 0.3933 | -3.0495 | 0.0023 |
| 5 | ca | -1.2246 | 0.2228 | -5.4976 | 3.85E-8 |
| 6.1 | thal=normal | 0.7039 | 0.71 | 0.9913 | 0.3215 |
| 6.2 | thal=reversable_defect | -1.0013 | 0.7029 | -1.4245 | 0.1543 |
|  | Constant | 3.7425 | 1.6127 | 2.3207 | 0.0203 |

![Imagen](images\page007_img01.png)

---

## Página 8

23-03-2017
8
Usando Weka para el mismo archivo de 6 variables
OR indica que por cada incremento de las variables cp=“dolor
pectoral” y thal=“problemas cardiacos en ejercicios”, el riesgo de
estar con una afección cardiaca aumenta al doble.
Logistic Regression with ridge parameter of 1.0E-8
Coefficients...
Odds Ratios...
Class
Variable                      <50
==========================
sex                                    -1.0866
cp=typ_angina
0.6388
cp=asympt
-1.0063
cp=non_anginal
0.7719
cp=atyp_angina
0.3582
trestbps
-0.0188
exang
-1.1993
ca                                      -1.2246
thal=fixed_defect
0.1175
thal=normal                      0.8214
thal=reversable_defect
-0.8838
Intercept                           4.6312
Class
Variable                      <50
========================
sex                                   0.3374
cp=typ_angina
1.8942
cp=asympt
0.3656
cp=non_anginal
2.1638
cp=atyp_angina
1.4308
trestbps
0.9814
exang
0.3014
ca                                      0.2939
thal=fixed_defect
1.1247
thal=normal                     2.2737
thal=reversable_defect
0.4132
Usando Weka para el mismo archivo de 6 variables
Confision Matrix
=== Summary ===
=== Detailed Accuracy By Class ===
Correctly Classified Instances         249             
84.1216 %
Incorrectly Classified Instances       47              
15.8784 %
Kappa statistic                               0.6791
Mean absolute error                      0.227 
Root mean squared error               0.3354
Relative absolute error                  45.7027 %
Root relative squared error           67.2958 %
Total Number of Instances            296     
TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
0.875     0.199      0.838        0.875     0.856          0.915           <50
0.801     0.125      0.845        0.801     0.823          0.915         >50_1
Weighted Avg.      
0.841      0.165      0.841       0.841      0.841         0.915
a
b
←classified as
140 
20
a = <50
27 
109
b = >50_1

### Tabla 1 (Página 8)

| Logistic Regression with ridge parameter of 1.0E-8
Coefficients... | Odds Ratios... |
| --- | --- |
| Class
Variable <50
==========================
sex -1.0866
cp=typ_angina 0.6388
cp=asympt -1.0063
cp=non_anginal 0.7719
cp=atyp_angina 0.3582
trestbps -0.0188
exang -1.1993
ca -1.2246
thal=fixed_defect 0.1175
thal=normal 0.8214
thal=reversable_defect -0.8838
Intercept 4.6312 | Class
Variable <50
========================
sex 0.3374
cp=typ_angina 1.8942
cp=asympt 0.3656
cp=non_anginal 2.1638
cp=atyp_angina 1.4308
trestbps 0.9814
exang 0.3014
ca 0.2939
thal=fixed_defect 1.1247
thal=normal 2.2737
thal=reversable_defect 0.4132 |

### Tabla 2 (Página 8)

| === Summary === | === Detailed Accuracy By Class === |
| --- | --- |
| Correctly Classified Instances 249
84.1216 %
Incorrectly Classified Instances 47
15.8784 %
Kappa statistic 0.6791
Mean absolute error 0.227
Root mean squared error 0.3354
Relative absolute error 45.7027 %
Root relative squared error 67.2958 %
Total Number of Instances 296 | TP Rate FP Rate Precision Recall F-Measure ROC Area Class
0.875 0.199 0.838 0.875 0.856 0.915 <50
0.801 0.125 0.845 0.801 0.823 0.915 >50_1
Weighted Avg.
0.841 0.165 0.841 0.841 0.841 0.915 |

### Tabla 3 (Página 8)

| a | b | ←classified as |
| --- | --- | --- |
| 140 | 20 | a = <50 |
| 27 | 109 | b = >50_1 |

![Imagen](images\page008_img01.png)

---

## Página 9

23-03-2017
9
4.1. Idea básica del discriminante de Fisher
Hipótesis: Las distribuciones sólo se diferencian por su localización (igual forma y
varianza)
Se trata de minimizar los errores de clasificación
Si xi < C se clasifica en el grupo I
Si xi > C se clasifica en el grupo II
El punto C se denomina punto de corte discriminante:
2
II
I
X
X
C
+
=

![Imagen](images\page009_img01.png)

![Imagen](images\page009_img02.png)

![Imagen](images\page009_img03.png)

---

## Página 10

23-03-2017
10

![Imagen](images\page010_img01.png)

![Imagen](images\page010_img02.png)

![Imagen](images\page010_img03.png)

---

## Página 11

23-03-2017
11
4.2. Discriminante Lineal de Fisher (matemática)
Para discriminar entre poblaciones se pretende separar
poblaciones mediante funciones lineales, para las
cuales se les debe determinar los parámetros de las
funciones lineales β.
Este método no asume restricciones respecto de las
distribuciones, acepto que las varianzas-covarianzas
sean homocedástica, esto es: las matrices de varianzas-
covarianzas deben ser aproximadamente iguales en
cada grupo.
Sea
X
la
matriz
de
datos
de
la
muestra
de
entrenamiento,
que
incluye
sólo
las
variables
independientes (excluye la columna con el factor que
indica la clase a la pertenece la población).
La dimensión de la matriz X es de n filas y p columnas
Xnxp. Con m grupos.
La matriz X será agrupada de acuerdo a m grupos que
separan la población












=
m
X
X
X
X
2
1
p
mp
m
m
m
p
p
x
x
y
x
x
y
β
β
β
β
β
β
+
+
+
=
+
+
+
=
...
...
...
1
1
0
1
1
11
10
1

![Imagen](images\page011_img01.png)

---

## Página 12

23-03-2017
12
Xk es la sub-matriz de la población Ik, que corresponden
a las observaciones de la población Pk.
La varianza total se puede descomponer en cada grupo:
La media en cada grupo de la variable xj será:
Donde Ik, corresponde a cada grupo k=1,…,m.
La media total de la variable xj será el promedio de las
sumas de:
)
)(
(
1
)
,
cov(
1
l
il
n
i
j
ij
l
j
x
x
x
x
n
x
x
−
−
= ∑
=
∑
∈
=
kI
i
ij
k
kj
x
n
x
1
∑
∑
∑∑
∑
=
=
=
∈
=
=
=
=
=
m
k
kj
k
m
k
kj
k
m
k
I
i
ij
n
i
ij
j
x
n
n
x
n
n
x
n
x
n
x
k
1
1
1
1
1
1
1
kj
k
I
i
ij
x
n
x
k
=
∑
∈
Así cada uno de los términos de la covarianza se puede
separar
La covarianza total se puede dividir en la covarianza
dentro de los grupos d(xj,xl) y la covarianza entre los
grupos e(xj,xl).
matricialmente T=D+E
)
)(
(
1
)
,
cov(
1
l
il
n
i
j
ij
l
j
x
x
x
x
n
x
x
−
−
= ∑
=
)
,
(
)
,
(
)
,
(
l
j
l
j
l
j
x
x
e
x
x
d
x
x
t
+
=
)
(
)
(
)
(
)
(
)
(
)
(
l
kl
kl
il
l
il
j
kj
kj
ij
j
ij
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
x
x
−
+
−
=
−
−
+
−
=
−
)
,
(
)
,
(
)
,
cov(
)
)(
(
)
)(
(
1
)
,
cov(
1
1
l
i
l
j
l
j
m
k
l
kl
j
kj
k
m
k
I
i
kl
il
kj
ij
l
j
x
x
e
x
x
d
x
x
x
x
x
x
n
n
x
x
x
x
n
x
x
k
+
=
−
−
+
−
−
=
∑
∑∑
=
=
∈

![Imagen](images\page012_img01.png)

---

## Página 13

23-03-2017
13
Las funciones lineales están dadas por
Condicionando a que la primera (y1) maximiza el
cociente entre la suma de cuadrados entre grupos y la
suma de cuadrados dentro de los grupos, en la muestra
de entrenamiento.
La segunda maximiza lo mismo, pero en el espacio
ortogonal a β1, la tercera igual pero en el espacio
ortogonal a β2 y así hasta el numero de clases.
En general yk es es la combinación lineal de x1 … xp la
mayor discriminación posible entre los grupos después
de yk-1 tal que corr(yk,yj)=0, para j=1, …, (k-1).
x
y
T
k
k
r
r
β
=
ˆ
El desarrollo es similar a la regresión lineal, pero la
variable dependiente y es categórica con k categorías.
Para que el método funcione se requieren al menos dos
grupos y al menos dos casos en cada grupo.
Entonces el número de variables discriminantes debe ser
menor que en numero de casos menos 2; p<(n-2).
Ninguna variable discriminante debe ser función de otra.
El numero de funciones discriminantes debe ser el
mínimo entre el numero de variables y el numero de
grupos menos 1.
Se requiere determinar los β de
forma tal que
la varianza entre los grupos sea mayor, respecto de la
varianza total.
x
y
T
k
k
r
r
β
=
ˆ

![Imagen](images\page013_img01.png)

---

## Página 14

23-03-2017
14
La varianza de los
, puede ser calculada mas
fácilmente al considerar las medias cero
:
Pero
Por lo tanto:
Como se requiere que:
en relación a la
varianza total, esto es
[
]
[
]
[
]
k
T
T
k
k
T
T
k
T
k
k
k
XX
E
XX
E
y
y
E
y
β
β
β
β
r
r
r
r
r
r
r
=
=
=
)
var(
X
y
T
k
β
r
r =
[
]
0
=
ky
E r
[
]
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
)
,
cov(
...
)
,
cov(
...
)
,
cov(
...
)
,
cov(
...
)
,
cov(
1
1
1
1
p
p
p
l
j
p
T
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
XX
E
k
T
k
k
T
k
k
T
k
k
E
D
T
y
β
β
β
β
β
β
r
r
r
r
r
r
r
+
=
=
)
var(
{
}
k
T
k Eβ
β
β
r
r
max






k
T
k
k
T
k
T
E
β
β
β
β
β
r
r
r
r
max
Si se considera la razón de varianzas una función
homogénea, entonces maximizar la razón
es equivalente a:
sujeto a
Al igual que el caso de las componentes principales, se
obtiene
el
lagrangeano
aumentado,
aplicando
multiplicadores de Lagrange:
se obtiene βκ de
Si pre multiplicamos por
y considerando que
{
}
k
T
k Eβ
β
β
r
r
max






k
T
k
k
T
k
T
E
β
β
β
β
β
r
r
r
r
max
1
=
k
T
k Tβ
β
r
r
)1
(
)
(
−
+
=
k
T
k
k
T
k
k
T
E
L
β
β
λ
β
β
β
r
r
r
r
r
0
)
(
=
∂
∂
k
k
L
β
βr
r
0
2
2
=
−
k
k
T
E
β
λ
β
r
r
⇒
=
 
k
k
T
E
β
λ
β
r
r
T
k
β
r
1
=
k
T
k Tβ
β
r
r
λ
β
β
λ
β
β
=
=
k
T
k
k
T
k
T
E
r
r
r
r

![Imagen](images\page014_img01.png)

---

## Página 15

23-03-2017
15
Si se considera el mayor vector característico asociado al
mayor valor característicos λ1, se tendrá el máximo
poder discriminante.
El
valor
característico
λi
asociado
a
la
función
discriminante yi, indica la proporción de la varianza total
explicada por las m funciones discriminantes.
Para obtener mas funciones se continua obteniendo los
vectores característicos de la matriz T-1E asociado a los
valores característicos elegidos en orden decreciente.
La suma de los valores característicos
hasta la q
corresponde a la varianza explicada por estas funciones.
Así el porcentaje de varianza explicado por cada yi del
total de la varianza hasta q será:
∑=
q
j
j
1λ
∑=
q
i
j
i
1
100
λ
λ
- Evaluación análisis discriminante lineal
Analizar los estadísticos:
-F de Snedecor para análisis discriminante.
−λ de Wilks denominado también U-estadístico.
-Matriz de confusión.

![Imagen](images\page015_img01.png)

---

## Página 16

23-03-2017
16
4.3. Métodos no paramétricos
(K-Vecinos mas Cercanos; K Nearest Neighbours)
Idea Básica:
?
Circulo 1: k=5 asignación
Circulo 2: k =10 asignación
El algoritmo solo posee dos etapas:
- Etapa de entrenamiento:
Se requiere un conjunto de entrenamiento suficiente de
ejemplos previamente etiquetados. Cada
ejemplo
posee la clasificación
.
-Etapa de Clasificación:
Cada nuevo ejemplo
es clasificado de acuerdo a la
proximidad de los k vecinos obtenidos del grupo de
entrenamiento.
Donde
y 0 en otro caso.
)
(
,
x
f
x
r
r
q
xr
))
(
,
(
max
arg
)
(
1∑
=
∈
←
k
i
i
e
q
x
f
e
x
f
r
r
δ
ϑ
{
}
m
x
f
,...,
1,
0
)
(
=
∈ϑ
r
,
 
 ,1
)
,
(
b
a
si
b
a
=
=
δ

![Imagen](images\page016_img01.png)

---

## Página 17

23-03-2017
17
Note que la elección de k determina la forma de
clasificación.
- Si k es un valor pequeño, el algoritmo clasifica
localmente de forma que el ruido también es incorporado
en la clasificación
- Si k es un valor grande Se evita el ruido, pero se
introduce sesgo, pues la mayoría de las veces, el resultado
será la clase mayoritaria.
- Que pasa cuando existe la misma cantidad de vecinos?
Se utilizan las probabilidades a priori (clase mayoritaria)
si son iguales se escoge al azar.
- Que valor de K se usa?
Si se realiza una curva de error de clasificación,
dependiendo del numero de vecinos se puede observar
que un numero pequeños y muy grandes llevan a elevar el
error.
error
K
3
7
Existen varias otras alternativas:
- Con rechazo: Se exigen garantías, umbral o mayoría
absoluta.
- Distancia mínima: calcular la distancia solo a los casos
mas cercanos al centriode de cada clase

![Imagen](images\page017_img01.png)

---

## Página 18

23-03-2017
18
- K vecinos ponderado
Una forma simple controlar el numero de vecinos
que participan en la elección de la clase es ponderar la
clasificación del nuevo caso por un peso.
Donde el ponderador es la propia medida de
proximidad o el inverso de la distancia:
De esta manera no es necesario determinar un
numero especifico de k, pues los ejemplos mas distantes no
contribuirán significativamente a la determinación de la
clase o promedio.
- Usar información mutua como ponderador.
))
(
,
(
max
arg
)
(
1∑
=
∈
←
n
i
i
i
e
q
x
f
e
x
f
r
r
δ
ω
ϑ
i
q
i
x
x
r
r −
=
1
ω
4.4. Tablas de contingencia y análisis ROC
Considere un clasificador simple cuyo objetivo es
clasificar el patrón
como perteneciente a una
clase o no.
La
respuesta
del
clasificador
será
T+
para
clasificar el patrón
en la clase C y será T- para el
caso en que no pertenece a la clase C (se clasifica
como
).
En estas condiciones pueden existir dos tipos
diferentes de errores, los cuales se observan en la
siguiente tabla de doble entrada, denominada
tabla de contingencia.
xr
C

![Imagen](images\page018_img01.png)

---

## Página 19

23-03-2017
19
Realidad
Total
T+
VP
FP
VP+FP
T-
FN
VN
FN+VN
Total
VP+FN
FP+VN
n
Clasificado
Verdaderos
VP: Verdaderos Positivos
VN: Verdaderos Negativos
Errores
FN: Falsos Negativos (tipo I)
FP: Falsos Positivos (tipo II)
La exactitud total del modelo es la cantidad de
verdaderos dividido por el total:
Exactitud=(VP+VN)/n
Error=(FP+FN)/n

### Tabla 1 (Página 19)

| None | Realidad | None | None |
| --- | --- | --- | --- |
|  |  |  |  |
| T+ | VP | FP | VP+FP |
| T- | FN | VN | FN+VN |
| Total | VP+FN | FP+VN | n |

![Imagen](images\page019_img01.png)

---

## Página 20

23-03-2017
20
Los indicadores de las bondades del sistema se
obtienen calculando proporciones por columnas
(características del clasificador)
Las predicciones del sistema se obtienen por filas
(características de las predicciones)
Control
T+
VP
FP
VP/(VP+FP)
T-
FN
VN
VN/(FN+VN)
VP/(VP+FN) FP/(FP+VN)
FN/(VP+FN) VN/(FP+VN)
Clasificado
Las proporciones de interés son las siguientes
Nombre
Significado
Probab.
Estimación
Sensibilidad
(Prop. VP)
Frecuencia de los positivos de la
clase C
p[T+|C]
VP/(VP+FN)
Pro. Fal. Neg.
(Prop. FN)
Frecuencia de los negativos de la
clase C
p[T-|C]
FN/(VP+FN)
Especificidad
(Prop.VN)
Frecuencia de los negativos de la
clase
p[T-|    ]
VN/(FP+VN)
Pro. Fal. Pos.
(Prop. FP)
Frecuencia de los Positivos de la
clase
p[T+|    ]
FP/(FP+VN)
Valor Predictivo
Positivo (VPP)
Frecuencia de la clase C con 
resultados positivos del Sis. 
p[C |T+]
Valor Predictivo 
Negativo (VPN)
Frecuencia de la clase    con 
resultados negativos del Sis. 
p [    |T-]
Requiere P[C]
VP/(VP+FP)
Requiere P[C]
VN/(FN+VN)
Prevalencia
Frecuencia de la clase C en la 
población total (U)
P[C]
Evaluación 
Independiente
C
C
C
C
C
C

### Tabla 1 (Página 20)

| None | Control | None | None |
| --- | --- | --- | --- |
|  |  |  |  |
| T+ | VP | FP | VP/(VP+FP) |
| T- | FN | VN | VN/(FN+VN) |
|  | VP/(VP+FN) | FP/(FP+VN) |  |
|  | FN/(VP+FN) | VN/(FP+VN) |  |

### Tabla 2 (Página 20)

| Nombre | Significado | Probab. | Estimación |
| --- | --- | --- | --- |
| Sensibilidad
(Prop. VP) | Frecuencia de los positivos de la
clase C | p[T+|C] | VP/(VP+FN) |
| Pro. Fal. Neg.
(Prop. FN) | Frecuencia de los negativos de la
clase C | p[T-|C] | FN/(VP+FN) |
| Especificidad
(Prop.VN) | Frecuencia de los negativos de la
clase C | p[T-C| ] | VN/(FP+VN) |
| Pro. Fal. Pos.
(Prop. FP) | Frecuencia de los Positivos de la
clase C | p[T+|C ] | FP/(FP+VN) |
| Valor Predictivo
Positivo (VPP) | Frecuencia de la clase C con
resultados positivos del Sis. | p[C |T+] | Requiere P[C]
VP/(VP+FP)
Requiere P[C] |
| Valor Predictivo
Negativo (VPN) | Frecuencia de la clase C con
resultados negativos del Sis. | p [C |T-] | VN/(FN+VN) |
| Prevalencia | Frecuencia de la clase C en la
población total (U) | P[C] | Evaluación
Independiente |

![Imagen](images\page020_img01.png)

---

## Página 21

23-03-2017
21
Nota: Prop. FN = P [T- C]=1- Sensibilidad
Prop. FP = P [T+ ]=1- Especificidad
Características del Sistema Clasificador
(proporciones en columnas)
El mejor clasificador es aquel en que los falsos son cero
⇒Sensibilidad=Especificidad=1
La Sensibilidad indica la bondad del clasificador para
detectar los casos que pertenecen a la clase C.
La Especificidad indica la bondad del clasificador
para detectar los casos que no pertenecen a la clase C
(esto es ∈
).
Estas características indican las bondades del clasificador
pero no aportan indicación de la probabilidad que tiene un
nuevo caso de ser clasificado correctamente en el futuro.
C
C
Características de Predicción (proporciones en filas)
El VPP (
) y VPN (
) se pueden estimar por las
proporciones de las filas de la tabla de contingencia pero estos
valores corresponden a probabilidades sólo cuando la muestra es
similar a la población.
Si se cuenta con la prevalencia P[C], es posible corregir estas
medidas.
Usando la definición de probabilidad condicional
P[C |T+]=P[C∩T+]/P[T+] ; P[
|T-]=P[
∩T-]/P[T-]
y la probabilidad de
P[T+]=P[C∩T+]+ P[
∩T+]
P[T+]=P[T+|C]P[C]+ P[T+|
] P[ ]
P[T-]=P[T-|C]P[C]+ P[T-| ] P[ ]
C
C
C
C
C
C
C
)
/
(ˆ
−
T
C
p
)
/
(ˆ
+
T
C
p

![Imagen](images\page021_img01.png)

---

## Página 22

23-03-2017
22
Se puede calcular estas probabilidades en función
de las proporciones del clasificador
VPP=P[C|T+] =
VPN=P[ |T-]=
Aquí se observa claramente que estas probabilidades
dependen de la prevalencia en la población.
P[C]=1-P[
].
De esta forma el VPP determina la probabilidad de que un
sujeto pertenezca a la clase C dado que el sistema lo
clasifico como T+.
[ ]
[ ]
[ ]






























−
+
=
+
+
+
+
ad
Sensibilid
dad
Especifici
C
P
C
P
C
P
C
T
P
C
P
C
T
P
C
P
C
T
P
)
1(
1
1
[ ]
[ ]
[ ]
1
)
1(
1
1
|
−
−
+
=
−
+
−
−






























ad
Sensibilid
dad
Especifici
C
P
C
P
C
P
C
T
P
C
P
C
T
P
C
P
C
T
P
C
C
 La Curva de Calibración.
(Receiver-Operating Caracteristic, ROC)
Todo
el
desarrollo
anterior
fue
realizado
considerando que el sistema de clasificación decide
por T+ o T- en un nivel fijo.
Supóngase ahora que para decidir la clasificación de
un patrón
se tiene en el sistema un parámetro q
(por ejemplo a una probabilidad que varía entre [0-
1]),
que al variar produce un cambio en la
clasificación del sistema.
Si θ=0,5 se obtendrán valores de VP, FP, FN y VN,
si se varía θ=0.6, se obtendrá otra tabla de valores,
la cual puede resultar una clasificación mejor que la
anterior,
logrando
así
una
especificidad
y
sensibilidad mayor.

![Imagen](images\page022_img01.png)

---

## Página 23

23-03-2017
23
Una representación para ver como varían los
cambios al variar el nivel de decisión es:
Para tener una representación más adecuada se
puede recurrir a la tabla de contingencia.
P[ ]
VP
VN
FP
FN
P[C]
Nivel de decisión
Variable de
Decisión
C
De las características del test (columnas) se sabe que:
Sensibilidad + Prop. FP=1
especificidad + Prop. FN=1.
Entonces sólo se requiere dos de estas variables para
representar el test y cada nivel de decisión será un
punto en el plano.
Al variar continuamente el nivel de decisión se tiene
una curva que representa las incidencias del nivel
sobre el clasificador.
Se usa como variables normalizadas la Sensibilidad
en las ordenadas y la Prop. FN o 1- Especificidad en
las abscisas.

![Imagen](images\page023_img01.png)

---

## Página 24

23-03-2017
24
Curva característica de calibración del sistema
(Curva ROC)
1
1
Sensibilidad
1-Especificidad
Nivel de 
decisión
Para cada posición de la distribución de probabilidades se
tendrán diferentes curvas a medida que se desplaza el nivel
de decisión.
A
A
B
B
C
A
Sens.
Sens.
1-Esp.
1-Esp.
Sens.
1-Esp.
A
A
B
A
B
C
(a)
(b)
(c)

![Imagen](images\page024_img01.png)

---

## Página 25

23-03-2017
25
La curva (c) corresponde al clasificador perfecto y el nivel
de decisión se debe situar en el punto B. La curva (a) no
posee ninguna utilidad y el de la curva (b) corresponde a un
clasificador real.
El problema es determinar para una curva dada ¿cual es el
nivel de decisión ideal?
En general será el punto donde se maximiza la Sensibilidad
y la Especificidad.
Sensibilidad
1-Especificidad
Malo
Bueno
En una curva real, en general, el mejor punto de operación
se logra en el punto de máxima curvatura.
Pero se puede observar que existe un compromiso entre la
Sensibilidad y Especificidad, esto es, se puede aumentar
una en perjuicio de la otra.
Este compromiso dependerá del tipo de clasificación que se
requiere realizar.
Suponga un sistema que realiza diagnóstico de una
enfermedad (examen para detecta una infección) para la
cual el tratamiento en pacientes sanos es inocuo, se puede
privilegiar la Sensibilidad antes de la Especificidad.
En cambio, si el tratamiento para la enfermedad que
diagnostica el sistema es muy riesgoso para el paciente, es
necesario balancear la Sensibilidad y Especificidad.

![Imagen](images\page025_img01.png)

---

