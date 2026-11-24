---
title: Weights, flag degrees and root towers
decls:
  - GlobalTheory.T.flag_degree_polynomial_eval
  - GlobalTheory.CompanionTheory.Relay.flag_degree_polynomial_eval
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weights, flag degrees and root towers

This section sets up the objects of the chapter: weights and the flag degree, root models with their intersection functionals, and root towers with their volumes. The flag degree is a combinatorial number, the degree of a line bundle on a product of complete flag varieties. The one theorem of the section says that it equals the analytic degree, the integral of the top power of the Chern form of the standard metric. The volume of a tower is defined with the flag degree, and every estimate of the chapter compares intersection numbers on a tower with the volume times a flag polynomial. For the background see [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) and [arithmetic varieties and intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers).

Throughout, $\Psi$ is a finite set and $N \ge 1$. In the application $\Psi$ is the set of CM types of a host field and $N = p + q$ is the dimension of a hermitian space of signature $(p, q)$. We put

$$
d = \dim \mathrm{Fl} = |\Psi| \cdot \frac{N(N-1)}{2},
$$

the dimension of the product $\mathrm{Fl} = \prod_{\tau \in \Psi} \mathrm{Fl}(\mathbb{C}^N)$ of complete flag varieties.

**Definition 9.1.1 (Weights).** A weight is a function $\lambda \colon \Psi \times \{0, \dots, N-1\} \to \mathbb{R}$. It is dominant if $\lambda(\tau, b) \le \lambda(\tau, a)$ for all $\tau$ and $a \le b$, and regular dominant if the inequality is strict for $a < b$. Its $\ell^1$ norm is $\|\lambda\|_1 = \sum_{\tau, i} |\lambda(\tau, i)|$. Its spread is $\operatorname{spread}(\lambda) = \sum_\tau (\max_i \lambda(\tau, i) - \min_i \lambda(\tau, i))$. The weight $\rho$ is $\rho(\tau, i) = N - 1 - i$.

Let $R = \mathbb{R}[x_{\tau, i}]$ be the polynomial ring in the variables $x_{\tau, i}$, $\tau \in \Psi$, $0 \le i < N$. The variable $x_{\tau, i}$ stands for the first Chern class of the $i$-th graded line of the flag at $\tau$. The linear form of a weight is

$$
\ell_\lambda = -\sum_{\tau, i} \lambda(\tau, i)\, x_{\tau, i}.
$$

**Definition 9.1.2 (Flag degree).** For $F \in R$ put

$$
\deg_{\mathrm{Fl}} F = (-1)^d \sum_{\sigma \colon \Psi \to S_N} \Big(\prod_\tau \operatorname{sgn} \sigma_\tau\Big) \cdot \operatorname{coeff}\Big(F,\ \prod_{\tau, i} x_{\tau, i}^{\,N - 1 - \sigma_\tau(i)}\Big).
$$

The flag degree of a weight is $\deg_{\mathrm{Fl}}(\lambda) = \deg_{\mathrm{Fl}}(\ell_\lambda^{\,d})$.

The functional $\deg_{\mathrm{Fl}}$ is the integral over $\mathrm{Fl}$, written in the Chern roots: a monomial of degree $d$ has integral $\pm 1$ if its exponents at each $\tau$ are a permutation of $(N-1, \dots, 1, 0)$, and $0$ otherwise. For example, let $|\Psi| = 1$ and $N = 2$, so $d = 1$. Then $\ell_\lambda = -\lambda_0 x_0 - \lambda_1 x_1$, and $\deg_{\mathrm{Fl}}(\lambda) = -(-\lambda_0 + \lambda_1) = \lambda_0 - \lambda_1$. This is the degree of the line bundle $\mathcal{O}(\lambda_0 - \lambda_1)$ on $\mathbb{P}^1$. In general one has the Weyl formula

$$
\deg_{\mathrm{Fl}}(\lambda) = d! \prod_{\tau} \prod_{a < b} \frac{\lambda(\tau, a) - \lambda(\tau, b)}{b - a},
$$

the leading term of the Weyl dimension polynomial. It follows from the definition by expanding $\ell_\lambda^{\,d}$ and summing against the signs. So $\deg_{\mathrm{Fl}}(\lambda) > 0$ for a regular dominant weight, and $\deg_{\mathrm{Fl}}(\rho) = d!$.

Now let the flag variety carry its standard hermitian lines: for each pair $(\tau, i)$ the $i$-th graded line of the tautological flag at $\tau$, with the metric induced from the standard hermitian form on $\mathbb{C}^N$. For a word $w = (w_1, \dots, w_d)$ in the pairs $(\tau, i)$ let $\int_{\mathrm{Fl}} w$ be the integral over the complex points of $\mathrm{Fl}$ of the product of the Chern forms of the lines $w_1, \dots, w_d$. The analytic degree polynomial of $\mathrm{Fl}$ is

$$
P_{\mathrm{Fl}} = \sum_{w} \Big(\int_{\mathrm{Fl}} w\Big)\, x_{w_1} \cdots x_{w_d} \in R.
$$

Its value at the point $x_{\tau, i} = \lambda(\tau, i)$ is the multilinear integral evaluated on the diagonal, that is, the integral of the top power of the Chern form of the line of weight $\lambda$.

**Theorem 9.1.3 (Analytic and combinatorial flag degree).** Assume the inputs of the proof theory, and let the arithmetic intersection numbers come from a full intersection system. Let $\Psi$ be nonempty and $N \ge 2$. Then for every weight $\lambda$

$$
P_{\mathrm{Fl}}(\lambda) = \deg_{\mathrm{Fl}}(\lambda).
$$

Lean: `GlobalTheory.T.flag_degree_polynomial_eval` (also `GlobalTheory.CompanionTheory.Relay.flag_degree_polynomial_eval`, a second name)

*Proof.* The integral of Chern forms is symmetric and multilinear in the word $w$, so $P_{\mathrm{Fl}}$ is a homogeneous polynomial of degree $d$. The inputs of the proof theory, applied to a model of $\mathrm{Fl}$ over $\mathbb{Z}$ with its base metric, show that $P_{\mathrm{Fl}}$ is a constant multiple $c\,\Delta$ of the product $\Delta = \prod_\tau \prod_{a < b} (x_{\tau, a} - x_{\tau, b})$. To find $c$, take a word $w$ in which the pair $(\tau, i)$ occurs $N - 1 - i$ times. The flag variety is an iterated tower of projective bundles, and along this tower the integral of $w$ is $1$, since each step is the integral of the Chern form of $\mathcal{O}(1)$ over a fibre. With the symmetry of the integral under permutations of the word, this fixes $c$, and $P_{\mathrm{Fl}}(\lambda) = d! \prod_\tau \prod_{a<b} (\lambda(\tau,a) - \lambda(\tau,b))/(b - a)$. The Weyl formula above identifies the right side with $\deg_{\mathrm{Fl}}(\lambda)$. $\square$

This theorem is used where the arithmetic intersection numbers of the tower are compared with flag polynomials, in the final step of the deep statement.

A root model is an arithmetic variety with a family of hermitian lines indexed by $\Psi \times \{0, \dots, N-1\}$ and one more line.

**Definition 9.1.4 (Root model).** A root model of type $(\Psi, N)$ consists of:

1. an arithmetic variety $X$ of dimension $d + 1$, given by an ideal of a multihomogeneous polynomial ring over $\mathbb{Z}$, that is birational to its generic coordinates;
2. for each $t \in \mathbb{R}$ and each $(\tau, i)$ a smooth conjugation invariant hermitian line $x_t(\tau, i)$ on $X$ whose degree vector does not depend on $t$;
3. a smooth conjugation invariant hermitian line $A$, an integer $k_A > 0$ and an integer $\delta > 0$.

Let $\mathrm{II}$ be an arithmetic intersection system, that is, a rule that attaches to $d + 1$ hermitian lines on an arithmetic variety of dimension $d + 1$ a real number with the axioms of the [arithmetic intersection number](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers). Let $R^+ = R[x_\infty]$, where the extra variable $x_\infty$ stands for $A / k_A$.

**Definition 9.1.5 (Intersection functionals).** For $t > 0$ the arithmetic functional $\mathrm{ar}_t \colon R^+ \to \mathbb{R}$ is linear, vanishes on monomials of degree $\ne d + 1$, and on a monomial $m$ of degree $d + 1$ is

$$
\mathrm{ar}_t(m) = \frac{\mathrm{II}(\text{the lines of } m \text{ at } t)}{\delta\, k_A^{\,m(\infty)}},
$$

where $m(\infty)$ is the exponent of $x_\infty$. The model converges if every $\mathrm{ar}_t(m)$ has a limit as $t \to 0^+$. The limit functional is $\mathrm{PP}(m) = \lim_{t \to 0^+} \mathrm{ar}_t(m)$. The geometric functional $\mathrm{geo}$ is linear, vanishes off degree $d$, and on a monomial of degree $d$ is the integral over the complex points of $X$ of the product of the Chern forms of the lines at $t = 1$, divided by $\delta\, k_A^{\,m(\infty)}$.

So $\mathrm{PP}$ is a top arithmetic intersection number and $\mathrm{geo}$ is a geometric degree. For a weight $\lambda$ and $s \in \mathbb{R}$, the twisted root line is $L_{\lambda, s} = \ell_\lambda + s\, x_\infty$, the hermitian line $-\sum \lambda(\tau, i)\, x_t(\tau, i) + (s/k_A) A$.

**Definition 9.1.6 (Root tower).** A root tower of type $(\Psi, N)$ consists of an index $j$ with $1 \le j < N$, a finite nonempty set $\mathrm{Comp}$ of components, a finite set of bad primes that contains $2$, a weight $\nu$ with rational values, and a root model $M_{B, c}$ for each integer $B$ and each component $c$. The prime $p$ is in $S_B$ if $p \le B$ or $p$ is bad.

The level $B$ grows in the estimates: the models $M_{B, c}$ resolve more of the primes as $B$ grows. The weight $\nu$ gives the twisted weights $\lambda - s\nu$, and the parameter $t$ is tied to $s$ by $t = e^{-1/s^2}$.

**Definition 9.1.7 (Volumes and slopes).** Let $T$ be a root tower. The volume of the component $c$ and the total volume are

$$
\begin{aligned}
\operatorname{vol}(c) &= \frac{\mathrm{geo}_{M_{2,c}}(\ell_\rho^{\,d})}{\deg_{\mathrm{Fl}}(\rho)}, \\
\operatorname{vol}(T) &= \sum_c \operatorname{vol}(c).
\end{aligned}
$$

For $F \in R$ put $\mathrm{PP}_{B, c}(F) = \mathrm{PP}_{M_{B,c}}(F)$ and $\mathrm{PP}_B(F) = \sum_c \mathrm{PP}_{B, c}(F)$. The total top number of a weight is $\mathrm{PB}_B(\lambda) = \mathrm{PP}_B(\ell_\lambda^{\,d+1})$. The slope of a weight $u$ at $c$ is

$$
\operatorname{slope}_B(c, u) = \frac{\mathrm{PP}_{B, c}(\ell_u^{\,d+1})}{(d+1)\operatorname{vol}(c)\deg_{\mathrm{Fl}}(u)}.
$$

The slope is the arithmetic analogue of the normalized height $\widehat{\deg}(\overline{L}^{d+1}) / ((d+1)\deg(L^d))$ of [heights](/learn/arakelov/#heights): if the tower is proportional (next section), the denominator is $(d+1)$ times the geometric degree of $L_u$.

**Remark 9.1.8 (Formalization).** The theorem is stated for an abstract full intersection system, and its proof is in another part of the development: it uses the Vandermonde form of the analytic degree, the dimension of the flag model, the weight form of the flag height polynomial and the Weyl formula for the flag degree, each proved there. The tower of projective bundles is our reading of the chain of cells used to fix the constant. The second name is a relay with the same statement. The integral of Chern forms is written as an integral of potentials over the complex points of the coordinate ideal; we have not unfolded it. The degree $d$ appears in two places under two names, the dimension of the flag variety and the antisymmetric degree, and they are equal.
