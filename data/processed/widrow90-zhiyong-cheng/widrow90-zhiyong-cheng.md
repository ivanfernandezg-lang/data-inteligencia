# widrow90-Zhiyong Cheng

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Artificial Neural Networks for The Perceptron, 
Madaline, and Backpropagation Family 
Bernard Widrow and Michael A. Lehr 
Presented by Zhiyong Cheng 
2014-09-08

---

## Página 2

Outline 
•
Algorithm development history 
•
Fundamental Concepts 
•
Algorithms 
Error correction rules 
Single Element: linear & nonlinear 
Layered Network: nonlinear 
Gradient Descent 
Single Element: linear & nonlinear 
Layered Network: nonlinear

---

## Página 3

Algorithm Evolution 
• In 1960, two of the earliest and most important rules for training adaptive 
elements were developed: The LMS algorithm (Widrow and his student) 
and the Perceptron rule (Rosenblatt)  
• Facilitate the fast development of neural networks in the early years:  
Madaline Rule I (MRI) devised by Widrow and his students devised 
Madaline Rule I (MRI) – earliest popular learning rule for NN  with 
multiple adaptive elements. 
Application: speech and pattern recognition, weather forecasting, etc. 
• Breakthourgh: backpropagation training algorithm  
Developed by Werbos in 1971 and  published in 1974 
Rediscovered by Parcker in 1982 and reported in 1984, later on 
Rumelhart, Hinton, and Williams also rediscovered the technique and 
clearly present their ideas, they finally make it widely known.

---

## Página 4

Algorithm Evolution 
• MRI: hard-limiting quantizers (i. 𝑒. , 𝑦= 𝑠𝑔𝑛(𝑥)); easy to 
compute 
• Backpropagation network: sigmoid 
• MR1 -> MRII (Widrow and Winter) in 1987 
• MRII -> MRIII (David Aades in U.S. Naval Weapons Center of 
China Lake, CA) in 1988 by replacing hard-limiting quantizers 
with Sigmoid function 
Widrow and his student first discover that MRIII is 
equivalent to backpropagation.

---

## Página 5

Basic Concepts 
• Adaptive linear combiner 
 
x1 
x2 
x3 
x0 
y 
𝑦= 𝑋𝑘
𝑇𝑊𝑘 
𝑖𝑛𝑝𝑢𝑡 𝑙𝑎𝑦𝑒𝑟 
𝑜𝑢𝑡𝑝𝑢𝑡 𝑙𝑎𝑦𝑒𝑟

---

## Página 6

Basic Concepts 
• An adaptive linear element (Adaline) – linear classifier 
 
𝑦= 𝑠𝑔𝑛(𝑥) 
x1 
x2 
x3 
x0 
y 
𝑜𝑢𝑡𝑝𝑢𝑡= 𝑦= 𝑠𝑔𝑛(𝑋𝑘
𝑇𝑊𝑘) 
𝑖𝑛𝑝𝑢𝑡 𝑙𝑎𝑦𝑒𝑟 
𝑜𝑢𝑡𝑝𝑢𝑡 𝑙𝑎𝑦𝑒𝑟

---

## Página 7

Basic Concepts 
• An adaptive linear element (Adaline) – linear classifier 
 
𝑦= 𝑠𝑔𝑛(𝑥) 
Figures are frim Andrew Ng’s online course

---

## Página 8

Basic Concepts 
• Nonlinear classifiers 
Polynomial discriminant functions 
Multi-element feedforward neural network 
 
Figures are frim Andrew Ng’s online course

---

## Página 9

Basic Concepts 
• Polynomial discriminant function 
Initial feature vector: 
                    [𝑥1, 𝑥2] 
After preprocessor: 
                      𝑥1
2, 𝑥1 , 𝑥1𝑥2, 𝑥2, 𝑥2
2  
 
New feature vector                     
 
   [𝑥1
‘ , 𝑥2
‘ , 𝑥3
‘ , 𝑥4
‘ , 𝑥5
‘ ]  
•
It can provide a variety of nonlinear  
     functions with only a single Adaline   element 
•
Converge faster than layered neural network 
•
A unique global solution 
•
However, layered neural networks can obtain 
better generalization.

---

## Página 10

Basic Concepts 
• Layered neural 
networks 
• Madaline I 
Multiple Adaline elements 
in the first layers 
Fixed logic devices in the 
second layer, such as OR, 
AND, Majority vote etc. 
 
 
 
First layer 
Second layer

---

## Página 11

Basic Concepts 
• Feedforward Network

---

## Página 12

Basic Concepts 
• Feedforward Network 
 
 
 
Layer 1 
Layer 3 
Layer 2 
Layer 4 
Input layer 
Hidden layers 
Output layers

---

## Página 13

The Minimal Disturbance Principle 
Minimal Disturbance Principle: Adapt to reduce the output error for 
the current training pattern, with minimal disturbance to responses 
already learned.  
-> lead to the discovery of the LMS algorithm and the Madaline rules. 
• Single Adaline: Two LMS algorithm, May’s rules and Perceptron rule 
• Simple Madaline: MRI 
• Multi-layer Madalines: MRII, MRIII and Backpropogation algorithm

---

## Página 14

Adaptive algorithms 
Error correction rules: alter the weights to correct a certain 
proportion of the error in the output response to the present input 
pattern,  
 α-LMS algorithm 
    Weight alteration:                             Error correction: 
 
𝑊𝑘+1 = 𝑊𝑘+ 𝛼
𝜀𝑘𝑋𝑘
|𝑋𝑘|2                                   ∆𝜀𝑘= −𝛼𝜀𝑘

---

## Página 15

Adaptive algorithms 
Gradient rules: alter the weights during each pattern presentation 
by gradient descent with the objective of reducing mean-square-
error, average over all training patterns,  
 µ-LMS algorithm 
     Weight alteration:                             Error correction: 
 
Square error

---

## Página 16

Error Correction Rules: Adaline  
Linear rule: α-LMS Algorithm 
• Weight updated rule:  
                    𝑊𝑘+1 = 𝑊𝑘+ 𝛼
𝜀𝑘𝑋𝑘
|𝑋𝑘|2 
• Error:     𝜀𝑘= 𝑑𝑘−𝑊𝑘
𝑇𝑋𝑘 
• Weight change yields an error change  
                        ∆𝜀𝑘=∆(𝑑𝑘−𝑊𝑘
𝑇𝑋𝑘) = −𝑋𝑘
𝑇∆𝑊𝑘 
 
         ∆𝑊𝑘 = 𝑊𝑘+1 − 𝑊𝑘= 𝛼
𝜀𝑘𝑋𝑘
|𝑋𝑘|2 
                   ∆𝜀𝑘= −𝛼
𝜀𝑘𝑋𝑘
𝑇𝑋𝑘
𝑋𝑘2 = −𝛼∆𝜀𝑘 
• Learning rate: 0.1 < 𝛼< 1 
 
A Single Adaline

---

## Página 17

Error Correction Rules: Adaline 
Nonlinear: The perceptron Learning rule 
• α-Perceptron (Rosenblatt)

---

## Página 18

Error Correction Rules: Adaline 
Nonlinear: The perceptron Learning rule 
• Quantizer error:  
 
• Weight update:  
              𝑊𝑘+1 = 𝑊𝑘+ 𝛼
𝜀  
2 𝑋𝑘 
 
     𝛼= 1 
𝜀  > 0 -> 𝑋𝑘= 1, 𝑊𝑘+1= 𝑊𝑘+ 𝛼
|𝜀  |
2 ; 
 
𝜀  > 0 -> 𝑑𝑘= 1, 𝑦𝑘= −1; -> 𝑠𝑘  
𝜀  < 0 -> 𝑋𝑘= 1, 𝑊𝑘+1= 𝑊𝑘−𝛼
|𝜀  |
2  
 
𝜀  = 𝑑𝑘−𝑦𝑘

---

## Página 19

Error Correction Rules: Adaline 
α-LMS vs. Perceptron Rule 
• Value α 
α-LMS – controls stability and speed of convergence 
Perceptron rule – does not affect the stability of the perceptron 
algorithm, and it affects convergence time only if the initial weight 
vector is nonzero 
• α-LMS – both binary and continues responses,  
   Perceptron rule – only with binary desired responses.

---

## Página 20

Error Correction Rules: Adaline 
α-LMS vs. Perceptron Rule 
• Linearly separable training patterns 
Perceptron rule – separate any linearly separable set  
α-LMS - may fail to separate linearly separable set  
• Nonlinearly separable training patterns 
Perceptron rule–goes on forever is not linearly separable,  and often 
does not yield a low-error solution.  
α-LMS - does not lead to unreasonable weight solution

---

## Página 21

Error Correction Rules: Adaline 
Nonlinear: May’s Algorithms 
• May’s Algorithms 
 
 
 
 
 
 
• Separate any linearly separable set 
• For nonlinearly separable set, May’s rule performs much better than 
Perceptron rule because a sufficiently large dead zone tends to 
cause the weight vector to adapt away from zero when any 
reasonably good solution exists

---

## Página 22

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
• First layer:  
   - hard-limited Adaline  
     elements 
• Second layer:  
   - a single fixed threshold logic  
     element

---

## Página 23

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
𝑿 
5 Adalines 
𝑾𝟏 
𝑾𝟐 
𝑾𝟑 
𝑾𝟒 
𝑾𝟓 
0.2 
0.8 
-0.1 
-0.3 
-0.4 
𝑺= 𝑾𝑻𝑿 
𝒔𝒈𝒏(𝒔) 
1 
 1 
-1 
-1 
-1 
MAJ 
-1 
𝒅= −𝟏

---

## Página 24

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
𝑿 
5 Adalines 
𝑾𝟏 
𝑾𝟐 
𝑾𝟑 
𝑾𝟒 
𝑾𝟓 
0.2 
0.8 
-0.1 
-0.3 
-0.4 
𝑺= 𝑾𝑻𝑿 
𝒔𝒈𝒏(𝒔) 
1 
 1 
-1 
-1 
-1 
MAJ 
-1 
𝒅= 𝟏

---

## Página 25

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
𝑿 
5 Adalines 
𝑾𝟏 
𝑾𝟐 
𝑾𝟑
′  
𝑾𝟒 
𝑾𝟓 
0.2 
0.8 
0.4 
-0.3 
-0.4 
𝑺= 𝑾𝑻𝑿 
𝒔𝒈𝒏(𝒔) 
1 
 1 
1 
-1 
-1 
MAJ 
1 
𝒅= 𝟏

---

## Página 26

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
𝑿 
5 Adalines 
𝑾𝟏 
𝑾𝟐 
𝑾𝟑 
𝑾𝟒 
𝑾𝟓 
0.2 
-0.05 
-0.1 
-0.3 
-0.4 
𝑺= 𝑾𝑻𝑿 
𝒔𝒈𝒏(𝒔) 
1 
 -1 
-1 
-1 
-1 
MAJ 
-1 
𝒅= 𝟏

---

## Página 27

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
𝑿 
5 Adalines 
𝑾𝟏 
𝑾𝟐
′  
𝑾𝟑
′  
𝑾𝟒 
𝑾𝟓 
0.2 
0.1 
0.4 
-0.3 
-0.4 
𝑺= 𝑾𝑻𝑿 
𝒔𝒈𝒏(𝒔) 
1 
 1 
1 
-1 
-1 
MAJ 
1 
𝒅= 𝟏

---

## Página 28

Error Correction Rules: Madaline 
Madaline Rule I (MRI) 
• Weights are initially set to small random values 
• Weight vector update: can be changed aggressively using absolute 
correction or can be adapted by the small increment determined by the 
α-LMS algorithm 
• Principle: assign responsibility to the Adaline or Adalines that can most 
easily assume it 
• Pattern presentation sequence should be random

---

## Página 29

Error Correction Rules: Madaline 
Madaline Rule II (MRII) 
Typical two-layer Madaline II architecture

---

## Página 30

Error Correction Rules: Madaline 
Madaline Rule II (MRII) 
• Weights are initially set to small random values 
• Random pattern presentation sequence 
• Adapting the first-layer Adalines 
1.
Select the smallest linear output magnitude 
2.
Perform a “trial adaption” by adding a perturbation ∆𝑠 of suitable amplitude to 
invert its binary output 
3.
If the output error is reduced, remove ∆𝑠, and change the weight of the select 
Adaline using α-LMS algorithm 
4.
Perturb and update oter Adalines in the first layer with “sufficiently small” 𝑠𝑘 
output 
 
- can reversing pairs, triples, etc 
5.
After exhausting possibilities with the first layer, move on to next layer and 
proceed in a like manner 
6.
Random select a new training pattern and repeat the procedure.

---

## Página 31

Steepest-Descent 
• Steep-descent: measure the gradient of the mean-square-
error function and alter the weight vector in the negative 
direction of the measured gradient.  
𝑾𝑘+1 = 𝑾𝑘+ 𝜇(−𝛻𝑘) 
• 𝜇: controls stability and rate of convergence 
• 𝛻𝑘: the value of the gradient at a point on the  
   MSE surface corresponding to 𝑊= 𝑊𝑘 
 
𝑤𝑘 
𝜀𝑘 
𝑤𝑘+1 
𝜇(−𝛻𝑘) 
𝛻𝑘 
∆𝜀𝑘

---

## Página 32

Steepest-Descent – Single Element 
𝝁-LMS algorithm 
• Instantaneous linear error 
 
instead of

---

## Página 33

Steepest-Descent – Single Element 
Linear rules: 𝝁-LMS algorithm 
• Weight update 
 
 
 
 
 
 
 
• 𝜇: controls stability and rate of convergence; 
 
𝑑𝑘and 𝑋𝑘 are 
 independent of 𝑊𝑘

---

## Página 34

Steepest-Descent – Single Element 
Linear rules: 𝝁-LMS algorithm 
• Small 𝜇, and small 𝐾 
• The total weight change during the presentation of 𝐾 of 
training presentations is proportional to  
 
 
 
 
 
 
• 𝜀 is the mean-square-error functions.

---

## Página 35

Steepest-Descent – Single Element 
Nonlinear rules 
 
 
 
 
 
 
 
• Minimize the mean square of the sigmoid error 𝜀𝑘: 
 
Sigmoid nonlinearity

---

## Página 36

Steepest-Descent – Single Element 
Backpropagation: Sigmoid Adaline 
• Instantaneous gradient estimation

---

## Página 37

Steepest-Descent – Single Element 
Madaline Rule III: Sigmoid Adaline 
• The sigmoid function and its derivative function may not be realized 
accurately when implemented with analog hardware 
 
 
 
 
 
• Use a perturbation instead of  the 
derivative of the sigmoid function 
• A small perturbation signal ∆𝑠 is added 
to the sum 𝑠𝑘 
• The effect of this perturbation upon 
output 𝑦𝑘and error 𝜀𝑘 is noted.

---

## Página 38

Steepest-Descent – Single Element 
Madaline Rule III: Sigmoid Adaline 
• Instantaneous gradient estimation 
 
 
 
 
 
 
• Accordingly 
 
 
(∆𝑠 is small)  
OR

---

## Página 39

Steepest-Descent – Single Element 
Backpropagation vs Madaline Rule III 
• Mathematically equivalent if the perturbation ∆𝑠 is small 
 
• Adding the perturbation ∆𝑠 causes a change in 𝜀𝑘 equal to 
 
 
 
(∆𝑠 is small)

---

## Página 40

Steepest-Descent – Multiple Elements 
Backpropagation for Networks 
How backpropagation works 
For an input pattern vector X: 
1. Sweep forward through the system to get an output respond 
vector Y 
2. Compute the errors in each output 
3. Sweep the effects of the errors backward through the network to 
associate a “square error derivative” 𝛿 with each Adaline 
4. Compute a gradient from each 𝛿 
5. Update the weights of each Adaline based upon the corresponding 
gradient

---

## Página 41

Steepest-Descent – Multiple Elements 
Backpropagation for Networks 
𝑎(1) 
𝑎(2) 
𝑎(3) 
𝑎(4) 
Forward Propagation 
𝑎(1) = 𝑿 
𝑎(2) = 𝑠𝑔𝑚((𝑊(1))𝑇𝑎(1)) 
𝑎(3) = 𝑠𝑔𝑚(𝑊(2))𝑇𝑎2  
𝑎(4) = 𝑠𝑔𝑚((𝑊(3))𝑇𝑎(3)) 
Backpropagation 
For each output unit in layer 4 
 
𝛿𝑗
(4) = 𝑎𝑗
(4) −𝑦𝑗 
𝛿(3) = 𝑊(3)𝛿(4).∗𝑠𝑔𝑚′(𝑊(2)𝑎(2)) 
𝛿(2) = 𝑊(2)𝛿(3).∗𝑠𝑔𝑚′(𝑊(1)𝑎(1)) 
Intuition: 𝜹𝒋
(𝒍)= “error” of node 𝒋 in layer 𝒍  
Figures are frim Andrew Ng’s online course

---

## Página 42

Steepest-Descent – Multiple Elements 
Backpropagation for Networks 
• Instantaneous gradient for an Adaline element 
 
 
 
 
• Define that,  
 
   thus, 
 
 
   and

---

## Página 43

Steepest-Descent – Multiple Elements 
Madaline Rule III for Networks 
• The sum squared output response error 
 
• Provide a perturbation by adding ∆𝑠 to a selected Adaline, the 
perturbation propagates through the network, causing the change in the 
sum of the squares of the errors

---

## Página 44

Steepest-Descent – Multiple Elements 
Madaline Rule III for Networks 
• Instantaneous gradient for an Adaline element 
 
 
 
• Since 
 
 
    We can get  
 
• Update weight:

---

## Página 45

Steepest-Descent – Multiple Elements 
Madaline Rule III for Networks

---

## Página 46

Reference 
• B. Widrow and M.E.Hoff, Jr.  Adaptive switching circuits. Technical 
Report 1553-1, Stanford Electron. Labs., Stanford, CA, June 30 1960 
• K. Senne. Adaptive Linear Discrete-time estimation. Phd thesis, 
Technical Report SEL-68-090, Standford Electron. Labs., Stanford, 
CA, June 1968 
• S. Grossberg. Nonlinear neural networks: principles, mechanisms, 
and architectures. Neural networks 1.1 (1988): 17-61. 
• S. Cross, R. Harrison, and R.  Kennedy. Introduction to neural 
networks.  The Lancet 346.8982 (1995): 1075-1079. 
• Andrew NG’s machine learning course in courera 
• LMS tutorials, 
http://homepages.cae.wisc.edu/~ece539/resources/tutorials/LMS
.pdf

---

