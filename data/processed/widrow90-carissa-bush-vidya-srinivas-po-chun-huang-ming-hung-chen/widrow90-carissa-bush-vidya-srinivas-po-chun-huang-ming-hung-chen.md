# widrow90-Carissa Bush, Vidya Srinivas, Po-Chun Huang, Ming Hung Chen

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

30 Years of Adaptive Neural Networks:  
Perceptron, Madaline, and Backpropagation
Widrow et. al.
Carissa Bush, Vidya Srinivas, Po-Chun Huang, Ming Hung Chen

---

## Página 2

Introduction
●
Machine learning concepts have been around for a while
●
Many ideas were discovered, and re-discovered independently again
●
Many ideas were biologically-inspired
●
Everything started with simple concepts
2

---

## Página 3

The Adaptive Linear Combiner  
●
Outputs a weighted sum of inputs
●
Each input has an associated weight
●
Weights can be discrete or continuous
●
Weights can be adapted
3

---

## Página 4

Binary Classiﬁcation and Linear Separability
Binary Classiﬁcation
●
Target task is to classify input patterns into two groups:  positive and negative
Linear Separability
●
A set of input patterns is linearly separable if 
there exists a line  that can separate points 
with positive labels from points with negative 
labels
4

---

## Página 5

An Adaptive Linear Classiﬁer: Adaline  
Adaptive Linear 
Combiner
Signum Threshold 
Element
± 1
Input 
Vector
●
Performs binary classiﬁcation task
●
Is able to realize linear separating boundaries
●
These boundaries perfectly classify linearly separable datasets 
5

---

## Página 6

Realizing Nonlinear Separating Boundaries
6

---

## Página 7

Nonlinear Classiﬁers: Feature Maps  
●
If the input patterns are not separable in the original input space, map them 
to a higher-dimensional space where they are linearly separable 
Feature Map
Adaline
± 1
Input 
Vector
7

---

## Página 8

8
𝜙: Our feature map

---

## Página 9

Nonlinear Classiﬁers: Feature Maps

---

## Página 10

Nonlinear Classiﬁers: Madaline I 
●
If the input patterns are not separable in the original input space, use a 
nonlinear combination of linear separating  boundaries to realize a 
nonlinear separating boundary
Fixed Logic Element 
(Nonlinear)
± 1
Input 
Vector
Adaline
Adaline
10

---

## Página 11

11

---

## Página 12

Nonlinear Classiﬁers: Feedforward Networks
●
Combines multiple Adalines in layers and feeds outputs of one layer to inputs 
of the next layer
12

---

## Página 13

Adaptation - the Minimal Disturbance Principle  
Error-correction (EC) rules 
●
Alter the weights of a network to 
correct error in the output 
response to the present input 
pattern
13
Steepest descent (SD) rules 
●
Alter the weights of a network by 
gradient descent 
●
Reduce error averaged over all 
input patterns

---

## Página 14

Error Correction Rules: Single Threshold 
Element
14

---

## Página 15

EC Single Threshold Element
●
Every new input pattern starts a new adaptation cycle
●
Goal is to update weights to reduce error
●
Linear rules will make corrections directly proportional to the error
●
Nonlinear rules will make corrections that are not directly proportional to the error
15
Single Input Pattern
Adaline
Error Correction 
Rule
Error
Updated Weights

---

## Página 16

EC Single Threshold Element: α-LMS
●
Weight update is independent of input pattern magnitude
●
Choice of α controls stability and speed of convergence
16

---

## Página 17

EC Single Threshold Element: Perceptron Rule
17

---

## Página 18

EC Single Threshold Element: Perceptron Rule
●
Adds or subtracts input patterns to weights to correct for error
●
Guaranteed to converge for any linearly separable input patterns
●
No guarantees of convergence for input patterns that aren’t linearly separable
18

---

## Página 19

EC Single Threshold Element: May’s Rules
●
 All desired responses are +1 or -1 
●
Deﬁnes a “dead zone” or margin around 0, denoted by ±𝛾
Increment Adaptation Rule
●
Input pattern falls outside margin: weight vector is adapted by Perceptron rule
●
Input pattern falls within margin:  weight vector is adapted by normalized 
variant of ﬁxed increment Perceptron rule 
19

---

## Página 20

EC Single Threshold Element: May’s Rules
Modiﬁed Relaxation Adaptation Rule
●
Input pattern falls outside margin and correctly classiﬁed: weight vector is not 
modiﬁed
●
Input pattern falls within margin or is misclassiﬁed:  weight vector is adapted 
by normalized variant of ﬁxed increment Perceptron rule 
●
If 𝛾 (dead-zone) is set to ∞, this turns into α-LMS
20

---

## Página 21

Error Correction Rules - Multi-Element 
Networks
21

---

## Página 22

Madaline Rule I (MRI)
●
Allows the adaptation of a ﬁrst-layer element because the logic element is 
ﬁxed
●
The second layer consists of a single ﬁxed-threshold-logic element which 
may be OR gate, AND gate, majority-vote-taker, etc.
22
Fixed Logic Element 
(Nonlinear)
Input 
Vector
Adaline
Adaline
.
.
.
First layer
Second layer

---

## Página 23

Madaline Rule I: Adaptation
●
The weights of the Adalines are initially 
set to small random values
●
Weight vector can be adapted by any of 
the single error-correction rules
○
Reverse the Adaline’s output
○
𝛂-LMS
○
Perceptron
●
Main idea: Assign responsibility to the 
Adaline or Adalines that can most easily 
assume it
23

---

## Página 24

Madaline Rule I
●
Job assigner assigns responsibility
●
Load sharing is important
●
Pattern presentation sequence 
should be random
●
The adaptation process could hang 
up in local optima
●
Obeys the minimal disturbance rule
24

---

## Página 25

Madaline Rule II (MRII)
●
Extended from MRI
●
Used for multilayer binary networks
●
Weights are initially set to small 
random values
●
Training patterns are presented in a 
random sequence
●
Could hang up in local optima
25

---

## Página 26

Madaline Rule II: Adaptation
●
The goal is to reduce Hamming error
●
If the network produces an error, adapt ﬁrst layer
○
Trial adaptation: inverting its binary output
○
Done without adaptation: add a perturbation Δs
○
If output error is reduced, remove perturbation Δs and adapt selected 
Adalines by 𝛂-LMS
○
If the error is not reduces, no weight adaptation
●
Exhaust all Adalines in ﬁrst layer 
●
Repeat for all layers
26

---

## Página 27

Steepest Descent Rules: Single Threshold 
Element
27

---

## Página 28

Steepest Descent Rules - Motivation
28

---

## Página 29

Steepest Descent Rules - The µ-LMS algorithm
29
●
Crude gradient used in place of the actual gradient
●
Instantaneous gradient determined from a single input pattern
●
𝜇 is the learning constant that determines stability and convergence rate
●
For the mean-squared error, this equation is:

---

## Página 30

Steepest Descent Rules - 𝛼-LMS and 𝜇-LMS Comparison 
30
LMS instantaneous gradient
LMS instantaneous gradient
self-normalizing
not self-normalizing
more difﬁcult to analyze
easier to analyze
faster convergence
slower convergence
may converge to biased point
always converges in mean to 
minimum
𝛼-LMS
𝜇-LMS

---

## Página 31

Steepest Descent Rules - Adaline with Sigmoid
31

---

## Página 32

Steepest Descent Rules - Backpropagation
32

---

## Página 33

Steepest Descent Rules - MRIII Algorithm
33

---

## Página 34

Steepest Descent Rules - Nonlinear Elements
34

---

## Página 35

Steepest Descent Rules - Multi-Element Networks
35

---

## Página 36

Backpropagation
●
Process:
○
Input → Output
○
Find errors of the output
○
Sweep the effects of the errors 
backwards through the network to 
associate a “squared error derivative” 
(𝛿) with each Adaline
○
Use the 𝛿 to determine the gradient
○
Update the weights based on the 
gradient
○
Repeat for all layers
36

---

## Página 37

37
Multi-Element Networks: Madaline Rule III

---

## Página 38

MRIII vs Backpropagation
●
MRIII essentially equivalent to Backpropagation 
○
Same arguments for each of the Adaline elements
○
The Δs, perturbation, is small
○
Adaption is applied to all elements in the network at once
38

---

## Página 39

MRII vs. MRIII
MRII:
●
Discontinuous and nonlinear
●
Not possible to use 
instantaneous gradients to 
update weights
●
Problems with running into 
local minima
MRIII: 
●
All Adalines are adapted
○
Those with analog sums 
closest to zero are usually 
adapted stronger
39

---

## Página 40

What is still being used today
●
Different methods are best in different 
applications
●
Used Less:
○
Linear Classiﬁcation
○
Single elements
○
Single-layer
●
Used More:
○
Multi-layer
○
Multi-element
○
Backpropagation
40

---

## Página 41

Questions?
41

---

## Página 42

Appendix
42

---

## Página 43

Nonlinear Classiﬁers: Feature Maps  
●
Consider the following example
Original Space: 1D
Mapped Space: 2D
Feature Map: 
Points: 1, 2, 3
Mapped Points:
●
1 → (1, 1)
●
2 → (2,4)
●
3 → (3,9)
Linear boundary: x1
2 - 4x1 + 3.5
x1
x1
x1
2
43

---

## Página 44

44
Multi-Element Networks: Backpropagation

---

## Página 45

Backpropagation Example
45

---

## Página 46

Nonlinear Classiﬁers: Feedforward Networks
●
Different layers can have different activation functions
46

---

## Página 47

Nonlinear Classiﬁers: Adaptation
●
Can compute error signal at output vector
●
Adaptation of output layer possible
●
What do we do about adaptation of hidden layers?
47

---

## Página 48

EC Single Threshold Element: Perceptron Rule
48

---

## Página 49

Steepest Descent Rules - The µ-LMS algorithm
49
PT
R

---

## Página 50

Steepest Descent Rules - The µ-LMS algorithm
50
Xk
●
The learning constant 𝜇 determines 
stability and convergence rate
●
                                     , the algorithm
converges mean to W*

---

