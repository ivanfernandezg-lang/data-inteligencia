# widrow90-Xuanchong Li

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Artiﬁcial Neural Networks of The Perceptron, Madaline,
and Backpropagation Family
Bernard Widrow
Micheal A. Lehr
Presented by Xuanchong Li
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
1 / 41

---

## Página 2

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
2 / 41

---

## Página 3

Algorithms History 1960s - 1990s
1960: Least Mean Square (LMS) algorithm (Widrow and his
student), Perceptron rule (Rosenblatt)
Mid 1960s: Madaline (Multiple adaptive linear elements) rule I (MRI)
and application in speech, weather forecasting, pattern recognition
(Widrow and his student)
1971: Backpropagation (Werbos). It was ﬁrst ignored by community,
then re-discovered in 1982 by Parker, ﬁnally became famous with
work of Rumehart, Hinton, and Williams.
1987: Madaline Rule II (MRII) by Widrow and his student. The goal
is for adapting multiple players network
1988: Madaline Rule III (MRIII) by David Andes. Widrow and his
student found it is mathmatically equivalent to backpropagation
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
3 / 41

---

## Página 4

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
4 / 41

---

## Página 5

Adaptive linear combiner
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
5 / 41

---

## Página 6

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
6 / 41

---

## Página 7

Adaptive linear element (Adaline)
Basic building block used in neural networks
Adaptive threshold logic element: an adaptive linear combiner +
hard-limiting quantizer
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
7 / 41

---

## Página 8

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
8 / 41

---

## Página 9

Polynomial Preprocessor
Fixed preprocessing network + a single adaptive element
The choice of preprocessing function matters a lot
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
9 / 41

---

## Página 10

Madaline I
One of the earliest trainable layered neural networks.
A layer of ADALINE + ﬁx logic device (AND, OR, MAJ)
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
10 / 41

---

## Página 11

Feedforward Network
All layers are adaptive
Exp. a fully-connected three-layer feedforward adaptive network
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
11 / 41

---

## Página 12

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
12 / 41

---

## Página 13

The Minimal Disturbance Principle
Minimal Disturbance Principle: Adapt to reduce the output error for
the current training pattern, with minimal disturbance to responses
already learned.
It is behind every learning algorithm in the paper.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
13 / 41

---

## Página 14

Two Classes of Rules
Error correction rules: alter the weights of a network to correct a
certain proportion of the error in the output response to the present
input pattern
Steepest descent rules: alter the weights during each pattern
presentation by gradient descent with the objective of reducing
mean-square-error, average over all training patterns
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
14 / 41

---

## Página 15

Outline
1
Algorithms History
2
Fundamental Concepts
Adaptive linear combiner
Linear Classiﬁer: Adaptive linear element (Adaline)
Non-linear Classiﬁers
3
Learning Algorithms
Principle and Rules
Algorithm Details
Error correction rules
Steepest Descent Rules
4
Invariance of Neural Network
5
Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
15 / 41

---

## Página 16

Linear Rules
α-LMS Algorithm
Linear Rule: alter the weights of the adaptive threshold element with
each pattern presentation to make an error correction which is
proportional to the error itself.
Follows Error Correction Rule
Weight update rule:
Wk+1 = Wk + α ϵkXk
|Xk|2
Error at k: ϵk = dk −W T
k Xk
Error Change: ∆ϵk = −αϵk
Weights are usually initialized as 0.
Learning Rate: 0.1 < α < 1, controls stability and convergence rate.
Self-normalizing: choice of α does not depend on the magnitude of
the input signals.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
16 / 41

---

## Página 17

Non-linear Rules
Perceptron
A non-linear algorithm: weights change is collinear with the input
pattern vector and the linear error.
Follows Error Correction Rule
Weight update rule:Wk+1 = Wk + α
eeϵk
2 Xk
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
17 / 41

---

## Página 18

α-LMS V.S. Perceptron
α Value
α-LMS: controls stability and speed of convergence
Perceptron rule: does not aﬀect the stability of the perceptron
algorithm, and it aﬀects convergence time only if the initial weight
vector is nonzero
Binary or continuous response
α-LMS: both binary and continuous response
Perceptron: only binary
Linearly separable training patterns
α-LMS: may fail to separate linearly separable set
Perceptron: separate any linearly separable set
Nonlinearly separable training patterns
α-LMS: does not lead to unreasonable weight solution
Perceptron: goes on forever is not linearly separable, and often does
not yield a low-error solution. Usually end up with a small norm weight
vector.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
18 / 41

---

## Página 19

May’s Algorithm
Non-linear error correction rule
Introduce the ”deadzone” γ
Separate any linearly separable set; For nonlinearly separable set,
Mays rule performs much better than Perceptron rule because a
suﬃciently large dead zone tends to cause the weight vector to adapt
away from zero when any reasonably good solution exists
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
19 / 41

---

## Página 20

Multi-element Networks
Madaline Rule I (MRI)
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
20 / 41

---

## Página 21

Multi-element Networks
Madaline Rule I (MRI)
If an error happens, pick the ADALINE with smallest |sk| to adapt.j
Weights are initially set to small random values
Weight vector update: can be changed aggressively using absolute
correction or can be adapted by the small increment determined by
the α-LMS algorithm
Principle: assign responsibility to the Adaline or Adalines that can
most easily assume it
Pattern presentation sequence should be random
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
21 / 41

---

## Página 22

Madaline Rule I (MRI) example
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
22 / 41

---

## Página 23

Madaline Rule I (MRI) example
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
23 / 41

---

## Página 24

Madaline Rule I (MRI) example
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
24 / 41

---

## Página 25

Madaline Rule I (MRI) example
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
25 / 41

---

## Página 26

Madaline Rule II (MRII)
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
26 / 41

---

## Página 27

Madaline Rule II (MRII)
Weights in both layers are adaptive
Weights are initially set to small random values
Random pattern presentation sequence
Adapting the ﬁrst-layer Adalines
Select the smallest linear output magnitude
Perform a “trial adaption” by adding a ∆s perturbation of suitable
amplitude to invert its binary output
If the output error is reduced, remove ∆s, and change the weight of
the select Adaline using α-LMS algorithm
Perturb and update other Adalines in the ﬁrst layer with suﬃciently
small sk output
After exhausting possibilities with the ﬁrst layer, move on to next layer
and proceed in a like manner
Random select a new training pattern and repeat the procedure.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
27 / 41

---

## Página 28

Steepest Descent Rules
Single Threshold Element
Objective of adaptation: reduce error averaged over the training set
rather than reducing a given proportion of the error in each
presentation of training data.
The most common error: mean-square-error (MSE)
Wk+1 = Wk + µ(−▽k). µ: controls stability and convergence speed.
In practice, it works with on data at a time. It minimizes MSE
approximately.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
28 / 41

---

## Página 29

Steepest Descent Rules
Linear Rules
The steepest descent rule is linear if weight changes are proportional
to the linear error
Linear Combiner:
ϵ2
k = (dk −X T
k Wk)2 = d2
k −2dkX T
k Wk + WkXkX T
k Wk
MSE: E[ϵ2
k] = E[d2
k] −2E[dkX T
k ]Wk + W T
k E[XkX T
k ]Wk
PT ≜E[dkX T
k ], R ≜E[XkX T
k ]
▽k = ∂E[ϵ2
k]
∂Wk = −2P + 2RWk
Set the gradient to zero: W ∗= R−1P (Wiener weight vector)
Need to compute R−1 and P?
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
29 / 41

---

## Página 30

Steepest Descent Rules
µ-LMS Algorithm
Obtain accurate estimate of W ∗without computing R−1 and P
Use instantaneous gradient ˆ▽k =
∂ϵ2
k
∂Wk . It is a unbiased estimate of
the true gradient.
Weight update: Wk+1 = Wk + µ(−ˆ▽k) = Wk + 2µϵkXk
µ controls stability and convergence speed. Training data should be
in random order.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
30 / 41

---

## Página 31

µ-LMS V.S. α-LMS
α-LMS: Wk+1 = Wk + α ϵkXk
|Xk|2 , µ-LMS: Wk+1 = Wk + 2µϵkXk
α-LMS is self-normalization, with the parameter α determining the
fraction of the instantaneous error to be corrected with each adaption.
µ-LMS is constant-coeﬃcient linear algorithm.
In practice, α-LMS usually converges faster than µ-LMS.
µ-LMS converges to minimum MSE solution (Wiener solution), while
α-LMS converges to a biased solution.
Normalized training set: eX k ≜
Xk
|Xk|, edk ≜
dk
|Xk|.
α-LMS achieves minimum MSE solution for normalized training set.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
31 / 41

---

## Página 32

Steepest Descent Rules
Sigmoid Adaline
Sigmoid Adaline: extend the Adaline to include the use of a sigmoid
in place of the signum.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
32 / 41

---

## Página 33

Backpropagation for Sigmoid Adaline
yk = sgm(sk)
Use instantaneous gradient: ˆ▽k = −2eϵksgm′(sk)Xk
Update weights: Wk+1 = Wk + µ(−ˆ▽k) = Wk + 2eϵksgm′(sk)Xk
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
33 / 41

---

## Página 34

Madaline Rule III (MRIII) for Sigmoid Adaline
Motivation: the backpropagation algorithm requires accurate
implementation of sigmoid function hardware. Need another way to
compute the gradient, which does not rely on the accurate function
hardware.
Adding a small perturbation signal ∆s to sk, record the eﬀect on yk
and ϵk.
ˆ▽k =
∂eϵ2
k
∂Wk = ∂eϵ2
k
∂sk
∂sk
∂Wk = ∂eϵ2
k
∂sk Xk ≈

∆eϵ2
k
∆s

Xk ≈2eϵk

∆eϵk
∆s

Xk
Wk+1 = Wk −µ

∆eϵ2
k
∆s

Xk or
Weightsupdate : Wk+1 = Wk −2µeϵk

∆eϵk
∆s

Xk
Backpropagation and MRIII are mathmatically equivalent if the
perturbation ∆s is small. MRIII is robust even with the analog
implementation.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
34 / 41

---

## Página 35

Backpropagation for Networks
Intuition: propagate the error backward from the output layer to the
ﬁrst layer
For an input pattern vector X:
Sweep forward through the system to get an output respond vector Y
Compute the errors in each output
Sweep the eﬀects of the errors backward through the network to
associate a “square error derivative” δ with each Adaline
Compute a gradient from each δ
Update the weights of each Adaline based upon the corresponding
gradient
More details are in the next talk.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
35 / 41

---

## Página 36

MRIII for Networks
Same idea as MRIII for sigmoid Madaline
Measure the sum square output response error
ϵ2 = (d1 −y1)2 + (d2 −y2)2 = ϵ2
1 + ϵ2
2
∆(ϵ2)
∆s
= ∆(ϵ2
1+ϵ2
2)
∆s
≈∂ϵ2
∂s
ˆ▽k =
∂ϵ2
k
∂Wk = ∂ϵ2
k
∂sk
∂sk
∂Wk = ∂ϵ2
k
∂sk Xk ≈∆ϵ2
k
∆s Xk
Wk+1 = Wk −µ∆ϵ2
k
∆s Xk
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
36 / 41

---

## Página 37

Invariance of Neural Network
Neural network should be invariant to translation, rotation and scale
change of the input pattern.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
37 / 41

---

## Página 38

Invariance to up-down, left-right translation
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
38 / 41

---

## Página 39

Invariance to up-down, left-right translation
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
39 / 41

---

## Página 40

Invariance to up-down, left-right translation
The roles of the various Adalines interchange.
The “key” weights (W1) can be randomly chosen or manufactured.
the rotation and scale invariance can be obtained in the same way.
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
40 / 41

---

## Página 41

Summary
Bernard Widrow, Micheal A. Lehr (Stanford)Artiﬁcial Neural Networks of The Perceptron, Madaline, and Backpropagation Family
Presented by Xuanchong Li
41 / 41

---

