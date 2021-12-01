# drafts

## General Form
$$
\begin{aligned}
f(x) + g(z)
\end{aligned}
Objectif:
f(x) + g(z)$
\\
{\text{Subject to: }}
Ax + Bz = C
\\
\text{with: }
x \in \mathbb R^n, z \in \mathbb R^m, A \in \mathbb R^{p\times n}, B \in \mathbb R^{p\times m}, C \in \mathbb R^p
$$

## General Solution
Augmented Lagrangian:
$$
L_\rho(x,z,u) = f(x)+g(z)+u^T(Ax+Bz-C)+\frac{\rho}{2}||Ax+Bz-C||^2_2
$$
And repeat 
$$
\left[
\begin{matrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1
\end{matrix}
\right]
$$
$$
\left\{
\begin{matrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1
\end{matrix}
\right\} \tag{1}
$$

$$
{\underset {x\in S\subseteq X}{\operatorname {arg\,max} }}\,f(x):=\{x\mid x\in S\wedge \forall y\in S:f(y)\leq f(x)\}.
$$

$$
\mathcal{GB} = \mathop{\text{max}}\limits_{\mathcal{G}} \ \mathcal{U}(\mathcal{G(s)}) \ \text{subject to} \ \text{l}_{r}(\mathcal{G(s)}) = 1, \ \forall s \in S. \tag{1}

\mathcal{AaBbCcLlPp}

\mathop{AaBbLPx}
$$