# Lasso: L1-constrained fitting for statistics and data mining

- [Lasso: L1-constrained fitting for statistics and data mining](#lasso-l1-constrained-fitting-for-statistics-and-data-mining)
- [Intro](#intro)
- [Objectif](#objectif)
- [ADMM: Alternating Direction Method of Multipliers](#admm-alternating-direction-method-of-multipliers)
  - [Prerequisite: Lagrangian](#prerequisite-lagrangian)
  - [General form ADMM](#general-form-admm)
  - [Convergence and convergence rate](#convergence-and-convergence-rate)
  - [Scaled form ADMM](#scaled-form-admm)
  - [Invertibility](#invertibility)
- [Return to Lasso Problem](#return-to-lasso-problem)
  - [Subgradient](#subgradient)
  - [lasso directly](#lasso-directly)
  - [lasso with ADMM](#lasso-with-admm)
  - [Proximal Gradient Descent](#proximal-gradient-descent)
- [Other methods: Coordinate Descent](#other-methods-coordinate-descent)
- [Reference](#reference)

# Intro

The Lasso is a shrinkage and selection method for linear regression. It minimizes the usual sum of squared errors, with a bound on the sum of the absolute values of the coefficients. It has connections to soft-thresholding of wavelet coefficients, forward stagewise regression, and boosting methods.

# Objectif

Consider the **Lasso** problem
$$\underset{\beta}{min} \frac{1}{2}||y-X\beta||^2_2 + \lambda ||\beta||_1$$

# ADMM: Alternating Direction Method of Multipliers

## Prerequisite: Lagrangian

To be finished

## General form ADMM

Consider a general form of the **Lasso** problem
$$\underset{x,z}{min} f(x)+g(z) \text{ subject to } Ax+Bz=C$$
We define **augmented Lagragian**, for a parameter $\rho > 0$,
$$L_\rho(x,z,u) = f(x) + g(z) + u^T(Ax+bz-C) + \frac{\rho}{2}||Ax+Bz-c||^2_2$$
with a repetition, for $k = 1,2,3,...$
$$
\begin{aligned}
x^{(k)} &= \underset{x}{argmin} \ L_\rho(x,z^{(k-1)},u^{(k-1)}) \\
z^{(k)} &= \underset{z}{argmin} \ L_\rho(x^{(k)},z,u^{(k-1)}) \\
u^{(k)} &= u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-C)
\end{aligned}
$$

## Convergence and convergence rate

To be finished

## Scaled form ADMM

(Everything goes under euclidean space $\mathbb R^n$, we recall that $\langle x,y\rangle = x^Ty$)

Denote $w = u/ \rho$, Lagrangian becomes

$$
\begin{aligned}
L_\rho(x,z,u)  &= f(x) + g(z) + u^T(Ax+bz-C) + \frac{\rho}{2}||Ax+Bz-c||^2_2 \\
&= f(x)+g(z)+\rho w^T(Ax+bz-C) \\
&\quad +\frac{\rho}{2}(||Ax+Bz-c+w||^2_2 + ||w||^2_2 - 2w^T(Ax+Bz-C+w)) \\
&=f(x) + g(z) + \frac{\rho}{2}||Ax+Bz-c+w||^2_2 - \frac{1}{2}||w||^2_2
\end{aligned}
$$

where we recall that $||X||^2_2 = X^TX$,
and ADMM updates become
$$
\begin{aligned}
x^{(k)} &= \underset{x}{argmin} \ f(x)+\frac{\rho}{2}\| Ax+Bz^{(k-1)}-C+w^{(k-1)} \|^2_2 \\
z^{(k)} &= \underset{z}{argmin} \ g(z)+\frac{\rho}{2}\| Ax^{(k)}+Bz-C+w^{(k-1)} \|^2_2 \\
w^{(k)} &= w^{(k-1)}+Ax^{(k)}+Bz^{(k)}-C
\end{aligned}
$$

## Invertibility

The matrix $X^TX+\rho I$ is always invertible. In fact, it's symmetric positive definite.

A similar case is that the square matrix's positivity ensure the inversibility

$$
\begin{aligned}
    M \text{ is positive } &\Leftrightarrow \forall X \in M_{n,1}(\R), X^TMX>0 \\
    &\Leftrightarrow \forall \lambda \in Sp(M), \exist X \in M_{n,1}(\R), \lambda \|X \|^2 = X^TMX>0 \\
    &\Leftrightarrow \forall \lambda \in Sp(M), \lambda \in \R^*_+ \\
    &\Leftrightarrow M \text{ is triangularizable with positive eigenvalues } \\
    &\Leftrightarrow det(M) > 0 \\
    &\Leftrightarrow M \text{ is invertible }
\end{aligned}
$$

# Return to Lasso Problem

This part begins with some prerequisite notions.

## Subgradient

__*Definition:*__ (Generalized Gradient)
A subgradient of $f$ (convex) at $x$ is any $g$ 
s.t. 
$$f(y) \geq f(x) + g^T(y-x) \text{ for all }y$$

__*Should verify:*__ existence of g (in $\mathbb R^1$ case). From the definition of convexity, 
$$
\begin{aligned}
    & \forall x,y \in \mathbb R^n,f(tx+(1-t)y) \leq tf(x)+(1-t)f(y) \\
    \implies & \forall x,y \in \mathbb R^n, x<z<y, \frac{f(x)-f(z)}{x-z}<\frac{f(x)-f(y)}{x-y}<\frac{f(z)-f(y)}{z-y} \\
    \implies & \text{At x } \in \mathbb R^n, \text{left derivative } f^{'}(x^{-}) \text{ and right derivative } f^{'}(x^{+}) \text{ exist} \\
    \implies & g \in [min(f^{'}(x^{-}),f^{'}(x^{+})), max(f^{'}(x^{-}),f^{'}(x^{+}))] \\
\end{aligned}
$$
And the set above is never empty. So g always exist.

__*Notice:*__ subgradient $g$ can take one value if $f$ is differentiable, so that the left and right derivative constraints given by convexity can be respected. Otherwise, $g$ can be only gradient of $f$ at $x$

$$
(\R^1\text{ case) When } f \text{ is diffentiable, }, f^{'}(x^{-})=f^{'}(x^{+})\text{ , and } g = f^{'}(x)
$$

__*Notice*__ Higher dimension case can be extended from $\R^1$ case. As properties in higher dim imply $\R^1$ properties.

__*Definition*__ Subdifferential: set of subgradients
$$
\partial f(x) = \{ g \in \R^n: g \text{ is a subgradient of } f \text{ at } x \}
$$

__*Property*__ If $f$ differentiable at $x$, then $\partial f(x) = \{ \nabla f(x) \}$

__*Subgradient Optimality Condition (General)*__ 
$$f(x^*) = min \  f(x) \iff 0 \in \partial f(x^*)$$

__*First-order Optimality Condition*__: $min \  f(x)$ subject to $x \in C$ solved at $x \iff \nabla f(x)^T(y-x) \geq 0 ,\ \forall x \in C$
$$
\begin{aligned}
x = \underset{x}{argmin}\ f(x)+I_C(x) &\iff 0 \in \partial(f(x)+I_C(x)) \\
& \iff 0 \in \{ \nabla f(X) \} + N_C(x) \\
& \iff -\nabla f(x) \in N_C(x) \\
& \iff -\nabla f(x)^T x \geq -\nabla f(x)^T y, \ \forall y \in C \\
& \iff \nabla f(x)^T(y-x) \geq 0
\end{aligned}
$$
with indicator $
    I_C(x) = \left\{
	\begin{array}{ll}
		0 & x \in C \\
		+\infty & x \notin C
	\end{array}\right.
$ and $N_C(x) = \partial(I_C(X))$ 
$$\begin{aligned}
    & \implies g\in C, \forall x,y \in C, I_C(y) \geq I_C(x) + g^T(y-x) \\
    & \implies g^T(y-x) \leq 0, \ \forall y \in C \\
    & \implies  g^Tx \geq g^Ty, \ \forall y \in C \\
    & \implies  N_C(x) = \{ g \in \R^n, \ g^Tx \geq g^Ty ,\ \forall y \in C \}
\end{aligned}$$

## lasso directly

Deduce from $\underset{\beta}{min} \ \frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1$
$$
\begin{aligned}
   \text{lasso solved at } \beta & \iff 0 \in \partial(\frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1) \\
    & \iff 0 \in -X^T(y-X\beta)+\lambda \partial(||\beta||_1) \\
    & \iff X^T(y-X\beta) = \lambda v
\end{aligned}
$$
With $\frac{\partial X^TX}{\partial X} = 2X
$
and $v \in \partial(||\beta||_1) \implies v_i \in \left\{
\begin{array}{ll}
        \{+1\} & \beta_i>0 \\
        \{-1\} & \beta_i<0 \\
        [-1,1] & \beta_i=0 \\
\end{array}\right. \\
$

__*Problem*__: $X^TX$ is not necessarily invertible

## lasso with ADMM
General form of ADMM at [here](#scaled-form-admm)

**Lagragian**: 
$$
L_\rho (\beta, \alpha, u) = \frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1 + u^T(\beta-\alpha) + \frac{\rho}{2}||\beta-\alpha||_2^2
$$

Scaled with $w = u/\rho
$, we get
$$
\begin{aligned}
L_\rho(\beta, \alpha, w) & = \frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1 + \rho w^T(\beta-\alpha) + \frac{\rho}{2}||\beta-\alpha+w-w||_2^2 \\
    & = \frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1 +  \rho w^T(\beta-\alpha+w) - \rho w^Tw\\
    & \quad \ + \frac{\rho}{2}(||\beta-\alpha+w||_2^2+||w||_2^2 -2(\beta-\alpha+w)w^T ) \\
    & = \frac{1}{2}||y-X\beta||_2^2 + \lambda||\beta||_1 + \frac{\rho}{2}||\beta-\alpha+w||_2^2 - \frac{\rho}{2}||w||_2^2\\
\end{aligned}
$$

**ADMM** steps:

first
$
\begin{aligned}
\beta = \underset{\beta}{argmin} \ L_\rho(\beta,\alpha,w)
& = \underset{\beta}{argmin} \ \frac{1}{2}||y-X\beta||_2^2 + \frac{\rho}{2}||\beta-\alpha+w||_2^2 \\
& = -X^T(y-X\beta) + \rho(\beta-\alpha+w) \\
\iff \beta  = (X^TX+\rho I)^{-1}(&X^Ty+\rho(\alpha-w))
\end{aligned}
$
then
$
\alpha = \underset{\beta}{argmin} \ \lambda||\alpha||_1+ \frac{\rho}{2}||\beta-\alpha+w||_2^2
$, use the subgradient optimality condition, we get
$$\alpha_i = S_{\lambda/\rho}(\beta_i-w_i), \text{ where } \alpha_i \in \left\{
\begin{array}{ll}
        \{+1\} & \alpha_i>0 \implies \beta_i+w_i > \frac{\lambda}{\beta} \\
        \{-1\} & \alpha_i<0 \implies \beta_i+w_i < \frac{\lambda}{\beta} \\
        [-1,1] & \alpha_i=0 \implies \beta_i+w_i = \frac{\lambda}{\beta} \\
\end{array}\right. \\
$$
so, 
$
\alpha_i = \left\{
\begin{array}{ll}
\begin{aligned}
        &\beta_i+w_i-\frac{\lambda}{\beta} & \beta_i+w_i > \frac{\lambda}{\beta} \\
        & 0  &-\frac{\lambda}{\beta}\leq \beta_i+w_i > \frac{\lambda}{\beta} \\
        &\beta_i+w_i+\frac{\lambda}{\beta} &\beta_i+w_i < -\frac{\lambda}{\beta} \\
\end{aligned}
\end{array}\right.
$

finally, $w = w+\beta-\alpha$

## Proximal Gradient Descent

Proximal operators are used when a function is not differentiable

# Other methods: Coordinate Descent
To be finished

# Reference
[CMU Convex Optimisation](http://www.stat.cmu.edu/~ryantibs/convexopt/)

[Regression Shrinkage and Selection via the Lasso](http://www-personal.umich.edu/~jizhu/jizhu/wuke/Tibs-JRSSB96.pdf)