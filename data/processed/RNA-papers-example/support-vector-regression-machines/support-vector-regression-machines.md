# Support-vector-regression-machines

> Extraído automáticamente con `pdf_extractor.py`

---

## Página 1

Support Vector Regression Machines 
Harris Drucker· 
Chris J.C. Burges" 
Linda Kaufman" 
Alex Smola·· 
Vladimir Vapoik + 
*Bell Labs and Monmouth University 
Department of Electronic Engineering 
West Long Branch. NJ 07764 
**BellLabs 
+ AT&T Labs 
Abstract 
A new regression technique based on Vapnik's concept of support 
vectors is introduced. We compare support vector regression (SVR) 
with a committee regression technique (bagging) based on regression 
trees and ridge regression done in feature space. On the basis of these 
experiments, it is expected that SVR will have advantages in high 
dimensionality space because SVR optimization does not depend on the 
dimensionality of the input space. 
1. Introduction 
In the following, lower case bold characters represent vectors and upper case bold 
characters represent matrices. Superscript "t" represents the transpose of a vector. y 
represents either a vector (in bold) or a single observance of the dependent variable in the 
presence of noise. yCp) indicates a predicted value due to the input vector x(P) not seen in 
the training set. 
Suppose we have an unknown function G(x) (the "truth") which is a function of a vector 
x (termed input space). The vector xt = [.XI,X2, ... ,Xd] has d components where d is 
termed the dimensionality of the input space. F(x, w) is a family of functions 
parameterized by w. w is that value of w that minimizes a measure of error between 
G(x) and F(x, w). Our objective is to estimate w with w by observing the N training 
instances Vj, j=l, .. ·,N. We will develop two apprOximations for the truth G(x). The first 
one is F 1 (x, w) which we term a feature space representation. One (of many) such 
feature vectors is: 
Zt_[x2 ... X2d X X 
... x·x· ... Xd 
X·-J X 
... x 1] 
-
I, 
, 
, 1 2, 
, 
I l' ' 
-I u' .. , d, 
which is a quadratic function of the input space components. Using the feature space 
representation, then F 1 (x, w) = z tw , that is, F 1 (x, w) is linear in feature space although

![Imagen](images\page001_img01.png)

---

## Página 2

156 
H. Drucker, C. J. Burges, L. Kaufman. A. Smola and V. Vapnik 
it is quadratic in input space. In general, for a p'th order polynomial and d'th 
dimensional input space, the feature dimensionality / of w is 
p+d-l 
. 
/ = L CJ-l 
;=d-l 
h 
Cn 
n! 
were 
k = k !(n-k)! 
The second representation is a support vector regression (SVR) representation that was 
developed by Vladimir Vapnik (1995): 
N 
F2(x,w)=L(at-a;)(v~x+1)P + b 
;=1 
F 2 is an expansion explicitly using the training examples. The rationale for calling it a 
support vector representation will be clear later as will the necessity for having both an 
a and an a rather than just one multiplicative constant. In this case we must choose the 
2N + 1 values of a; at and b. If we expand the term raised to the p'th power, we find/ 
coefficients that multiply the various powers and cross product terms of the components 
of x. So, in this sense Fl looks very similar to F2 in that they have the same number of 
terms. However F} has/free coefficients while F2 has 2N+1 coefficients that must be 
determined from the N training vectors. 
We let a represent the 2N values of aj and at. The optimum values for the components 
of w 
or a depend on our definition of the loss function and the objective function. Here 
the primal objective function is: 
N 
ULL[Yj-F(vj, w)]+11 w 112 
j=l 
where L is a general loss function (to be defined later) and F could be F 1 or F 2, Yj is the 
observation of G(x) in the presence of noise, and the last term is a regularizer. The 
regularization constant is U which in typical developments multiplies the regularizer but 
is placed in front of the first term for reasons discussed later. 
If the loss function is quadratic, i.e., we L[·]=[·J2, and we let F=F 1, i.e., the feature space 
representation, the objective function may be minimized by using linear algebra 
techniques since the feature space representation is linear in that space. This is termed 
ridge regression (Miller, 1990). In particular let V be a matrix whose i'th row is the i'th 
training vector represented in feature space (including the constant term "1" which 
represents a bias). V is a matrix where the number of rows is the number of examples 
(N) and the number of columns is the dimensionality of feature space f Let E be the tx/ 
diagonal matrix whose elements are 11U. y is the Nxl column vector of observations of 
the dependent variable. We then solve the following matrix formulation for w using a 
linear technique (Strang, 1986) with a linear algebra package (e.g., MA TLAB): 
Vly = [VtV +E] w 
The rationale for the regularization term is to trade off mean square error (the first term) 
in the objective function against the size of the w vector. If U is large, then essentially we 
are minimizing the mean square error on the training set which may give poor 
generalization to a test sel. We find a good value of U by varying U to find the best 
performance on a validation set and then applying that U to the test set.

![Imagen](images\page002_img01.png)

---

## Página 3

Support Vector Regression Machines 
157 
Let us now define a different type of loss function termed an E-insensitive loss (Vapnik, 
1995): 
L _ { 
0 
if I Yj-F2(X;,w) 1< E 
-
I Yj-F 2(Xj, w) I - E 
otherwise 
This defines an E tube (Figure 1) so that if the predicted value is within the tube the loss 
is zero, while if the predicted pOint is outside the tube, the loss is the magnitude of the 
difference between the predicted value and the radius E of the tube. 
Specifically, we minimize: 
N 
N 
1 
U(~~ • + ~~) + "2(w tw) 
where ~j or ~. is zero if the sample point is inside the tube. If the observed point is 
"above" the tube, l;; is the positive difference between the observed value and E and aj 
will be nonzero. Similary, 
~j. will be nonzero if the observed point is below the tube 
and in this case a7 will be nonzero. Since an observed point can not be simultaneously 
on both sides of the tube, either aj or a7 will be nonzero, unless the point is within the 
tube, in which case, both constants will be zero. If U is large, more emphasis is placed on 
the error while if U is small, more emphasis is placed on the norm of the weights leading 
to (hopefully) a better generalization. The constraints are: (for all i, i=1,N) 
Yi-(wtVi)--b~~; 
(wtvi)+b-yj~~; 
l;; *~ 
~~ 
The corresponding Lagrangian is: 
1 
N 
N 
N 
L=-(wtw) + U(L~*j + L~i) -
La;[yi-{wtvi)-b+E~;*] 
2 
i=1 
i=1 
i=1 
N 
N 
- Lai[(wtvi)+b-Yi+E~i] -
L(17~7+Y;~i) 
i=1 
i=1 
where the 1i and aj are Lagrange multipliers. 
We find a saddle point of L (Vapnik. 1995) by differentiating with respect to Wi , b, and ~ 
which results in the equivalent maximization of the (dual space) objective function: 
N 
N 
1 N 
W(a,a*) = -E~(a7 +Clj)+ ~yj(a~ -Clj) -
"2.~ (a7-Clj)(a;-ai)(v~vj + 11 
1=1 
1=1 
I.J=I 
with the constraints: 
~Clj~U 
~aj·~U 
i=1, ... ,N 
N 
N 
La; = Lai 
i=1 
i=1 
We must find N Largrange multiplier pairs (ai, (7). We can also prove that the product of 
Cl; and a; is zero which means that at least one of these two terms is zero. A Vi 
corresponding to a non-zero Clj or a; is termed a support vector. There can be at most N 
support vectors. Suppose now, we have a new vector x(P), then the corresponding

![Imagen](images\page003_img01.png)

---

## Página 4

158 
H. Drucker. C. J Burges, L Kaufman, A. Smola and V. Vapnik 
prediction of y(P) is: 
N 
y(P) = L(a: - ai)(vfx(p) + 1)P+b 
i=1 
Maximizing W is a quadratic programming problem but the above expression for W is 
not in standard fonn for use in quadratic programming packages (which usually does 
minimization). If we let 
then we minimize: 
subject to the constraints 
where 
A . = a~ 
1-'1 
I 
N 
'1N 
~i+N = Clj 
i=1, ... ,N 
L~i = L~; and 
05~i~U i=1,··· ,2N 
;=1 
N+l 
C'=[E-YloE-Y2, ... ,E-YN,E+Yl ,E+Y2, ... ,E+YN] 
Q= [! :] 
djj = (vfVj + 1)P 
i,j = 1, ... ,N 
We use an active set method (Bunch and Kaufman, 1980) to solve this quadratic 
programming problem. 
2. Nonlinear Experiments 
We tried three artificial functions from (Friedman, 1991) and a problem (Boston 
Housing) from the UCI database. Because the first three problems are artificial, we 
know both the observed values and the truths. Boston Housing has 506 cases with the 
dependent variable being the median price of housing in the Boston area. There are 
twelve continuous predictor variables. This data was obtaining from the UCI database 
(anonymous ftp at ftp.ics.ucLedu in directory Ipub/machine-learning-databases) In this 
case, we have no "truth", only the observations. 
In addition to the input space representation and the SVR representation, we also tried 
bagging. Bagging is a technique that combines regressors, in this case regression trees 
(Breiman, 1994). We used this technique because we had a local version available. In the 
case of regression trees, the validation set was used to prune the trees. 
Suppose we have test points with input vectors xfP) i=1,M and make a prediction yr) 
using any procedure discussed here. Suppose Yi is the actually observed value, which is 
the truth G(x) plus noise. We define the prediction error (PE) and the modeling error 
(ME): 
1 M 
ME=-L(YrLG(Xj»2 
M ;=1 
1 M 
PE=-L(YfPL y;)2 
M i=1 
For the three Friedman functions we calculated both the prediction error and modeling

![Imagen](images\page004_img01.png)

---

## Página 5

Support Vector Regression Machines 
159 
error. For Boston Housing, since the "truth" was not known, we calculated the prediction 
error only. For the three Friedman functions, we generated (for each experiment) 200 
training set examples and 40 validation set examples. The validation set examples were 
used to find the optimum regularization constant in the feature space representation. The 
following procedure was followed. Train on the 200 members of the training set with a 
choice of regularization constant and obtain the prediction error on the validation set. 
Now repeat with a different regularization constant until a minimum of prediction error 
occurs on the validation set. Now, use that regularizer constant that minimizes the 
validation set prediction error and test on a 1000 example test set. This experiment was 
repeated for 100 different training sets of size 200 and validation sets of size 40 but one 
test set of size 1000. Different size polynomials were tried (maximum power 3). Second 
order polynomials fared best. For Friedman function #1, the dimensionality of feature 
space is 66 while for the last two problems, the dimensionality of feature space was 15 
(for d=2). Thus the size of the feature space is smaller than that of the number of 
examples and we would expect that a feature space representation should do well. 
A similar procedure was followed for the SVR representation except the regularizer 
constant U, £ and power p were varied to find the minimum validation prediction error. 
In the majority of cases p=2 was the optimum choice of power. 
For the Boston Housing data, we picked randomly from the 506 cases using a training set 
of size 401, a validation set of size 80 and a test set of size 25. This was repeated 100 
times. The optimum power as picked by the validations set varied between p=4 and p=5. 
3. Results of experiments 
The first experiments we tried were bagging regression trees versus support regression 
(Table I). 
1#1 
1#2 
1#3 
Table I. Modeling error and prediction error 
on the three Friedman problems (100 trials). 
bagging 
SVR 
bagging 
SVR 
1# trials 
ME 
ME 
PE 
PE 
better 
2.26 
.67 
3.36 
1.75 
100 
10,185 
4,944 
66,077 
60,424 
92 
.0302 
.0261 
.0677 
.0692 
46 
Rather than report the standard error, we did a comparison for each training set. That is, 
for the first experiment we tried both SVR and bagging on the same training, validation, 
and test set. If SVR had a better modeling error on the test set, it counted as a win. Thus 
for Friedman 1#1. SVR was always better than bagging on the 100 trials. There is no clear 
winner for Friedman function #3. 
Subsequent to our comparison of bagging to SVR, we attempted working directly in 
feature space. That is. we used F 1 as our approximating function with square loss and a 
second degree polynomial. The results of this ridge regression (Table TI) are better than 
SVR. In retrospect, this is not surprising since the dimensionality of feature space is 
small (/=66 for Friedman #1 and.t=15 for the two remaining functions) in relation to the 
number of training examples (200). This was due to the fact that the best approximating 
polynomial is second order. The other advantages of the feature space representation in

![Imagen](images\page005_img01.png)

---

## Página 6

160 
H. Drucker; C. J. Burges, L Kaufman, A. Smola and V. Vapnik 
this particular case are that both PE and ME are mean squared error and the loss function 
is mean squared error also. 
Table ll. Modeling error for SVR and 
feature space polynomial approximation. 
SVR 
feature 
space 
#1 
.67 
.61 
#2 
4,944 
3051 
#3 
.0261 
.0176 
We now ask the question whether U and E are important in SVR by comparing the results 
in Table I with the results obtaining by setting E to zero and U to 100,000 making the 
regularizer insignificant (Table DI). On Friedman #2 (and less so on Friedman #3), the 
proper choice of E and U are important. 
Table m. Comparing the results above with those obtained by setting 
E to zero and U to 100,000 (labeled suboptimum). 
optimum 
suboptimum 
ME 
ME 
#1 
.67 
.70 
#2 
4,944 
34,506 
#3 
.0261 
.0395 
For the case of Boston Housing, the prediction error using bagging was 12.4 while for 
SVR we obtained 7.2 and SVR was better than bagging on 71 out of 100 trials. The 
optimum power seems to be about five. We never were able to get the feature 
representation to work well because the number of coefficients to be determined (6885) 
was much larger than the number of training examples (401). 
4 Conclusions 
Support vector regression was compared to bagging and a feature space representation on 
four nonlinear problems. On three of these problems a feature space representation was 
best, bagging was worst, and SVR came in second. On the fourth problem, Boston 
Housing, SVR was best and we were unable to construct a feature space representation 
because of the high dimensionality required of the feature space. On linear problems, 
forward subset selection seems to be the method of choice for the two linear problems we 
tried at varying signal to noise ratios. 
In retrospect, the problems we decided to test on were too simple. SVR probably has 
greatest use when the dimensionality of the input space and the order of the 
approximation creates a dimensionality of a feature space representation much larger than 
that of the number of examples. This was not the case for the problems we considered. 
We thus need real life examples that fulfill these requirements. 
5. Acknowledgements 
This project was supported by ARPA contract number NOOOl4-94-C-1 086.

![Imagen](images\page006_img01.png)

---

## Página 7

Support Vector Regression Machines 
161 
6. References 
Leo Breiman, "Bagging Predictors", Technical Report 421, September 1994, Department 
of Statistics, University of California Berkeley, CA Also at anonymous ftp site: 
ftp.stat.berkeley.edulpub/tech-reports/421.ps.Z. 
Jame R. Bunch and Linda C. Kaufman, " A Computational Method of the Indefinite 
Quadratic Programming Problem", Linear Algebra and Its Applications, Elsevier-North 
Holland, 1980. 
Jerry Friedman, "Multivariate Adaptive Regression Splines", Annal Of Statistics, vol 19, 
No.1, pp. 1-141 
Alan J. Miller, Subset Selection in Regression, Chapman and Hall, 1990. 
Gilbert Strang, Introduction to Applied Mathematics, Wellesley Cambridge Press, 1986. 
VladimirN. Vapnik, The Nature of Statistical Learning Theory, Springer, 1995. 
Figure 1: The p ... .meters for the support vector 
regression.

![Imagen](images\page007_img01.png)

---

