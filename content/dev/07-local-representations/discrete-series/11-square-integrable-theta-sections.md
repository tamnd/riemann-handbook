---
title: Square integrable theta sections
decls:
  - ReciprocityTheory.ChartRestriction.G.I2.propA_core
  - ReciprocityTheory.ChartRestriction.G.I2.propA
  - ReciprocityTheory.ChartRestriction.G.I2.zeroMode
  - ReciprocityTheory.ChartRestriction.G.I2.perFactor_of
  - ReciprocityTheory.ChartRestriction.G.I2.tOf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Square integrable theta sections

This section proves two kinds of bounds for holomorphic theta sections on a complex torus. The first is an interpolation result: a polynomial jet of degree at most $c$ at the origin is the jet of a theta section whose $L^2$ norm is at most a fixed multiple of the Gaussian norm of the polynomial. The second is a pointwise bound for theta sections of level one on a torus with complex multiplication, relative to their $L^2$ norm, at points that generate the lattice up to a bounded index. The interpolation result is used in [Theorem 10.20.3 of Volume 6](/entry/prop-a-holds/), and through it in the construction of sections with a large derivative. The pointwise bound is used in the step [every character of the literature](/step/every-character-of-literature/).

Background: [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori), [[theta function|2F5CYQJVAF]], [Hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes), [[Hermitian form|48P4A1CX85]], [abelian varieties with complex multiplication](/learn/theta-functions-cm/#abelian-varieties-with-complex-multiplication).

**Definition 3.11.1 (Theta datum).** Let $\iota$ be a finite set, $V = \mathbb{C}^\iota$ with the norm $|v|$, and $H(v, w) = \sum_i v_i \overline{w_i}$. A theta datum $Y$ is an $\mathbb{R}$-basis $b$ of $V$ with $2|\iota|$ elements, with lattice $\Lambda = \mathbb{Z}b$, such that $\operatorname{Im} H$ is integral on $\Lambda$ and every homomorphism $\Lambda \to \mathbb{Z}$ is $y \mapsto \operatorname{Im} H(x, y)$ for some $x \in \Lambda$, together with a function $\kappa$ on $V$ with $|\kappa| = 1$ on $\Lambda$. For $q \in \mathbb{N}$, $\mathrm{Sec}_q(Y)$ is the space of holomorphic $F$ on $V$ with $F(v + \gamma) = \kappa(\gamma) e^{q\pi H(v,\gamma) + q\pi H(\gamma,\gamma)/2} F(v)$ for $\gamma \in \Lambda$. The pointwise norm is $|F(v)|^2 e^{-q\pi |v|^2}$, and $\|F\|_q^2$ is its average over the fundamental domain of $b$. The datum satisfies the cocycle condition at $q$ if $\kappa(\gamma + \gamma') = \kappa(\gamma)\kappa(\gamma') e^{-i\pi q \operatorname{Im} H(\gamma, \gamma')}$ on $\Lambda$.

**Definition 3.11.2 (Gaussian norm and jets).** For functions $F, G$ on $V$ put $\langle F, G \rangle_q = \int_V F \overline{G} e^{-q\pi|v|^2}\,dv$ and $N_q(F) = (\operatorname{Re}\langle F, F\rangle_q)^{1/2}$. For a multi-index $\alpha$, $D^\alpha F$ is the complex derivative $\partial^\alpha F(0)$. $\mathcal{P}_c$ is the span of the monomials $z^\alpha$ with $|\alpha| \le c$, and the jet of order $c$ is $J_c F = \sum_{|\alpha| \le c} D^\alpha F / \alpha! \cdot z^\alpha$.

The interpolation result takes two inputs. The packing count says that a set of points in $\mathbb{R}^n$ in a ball of radius $R$ with pairwise distances at least $\delta \le R$ has at most $(3R/\delta)^n$ elements. The Gaussian tail bound says: if $h_i \ge R_0 > 0$, $16(2g + 1) \le R_0^2$, and every set of indices with $h_i \le R$ has at most $(3R/R_0)^{2g}$ elements for $R \ge R_0$, then $\sum_i e^{-h_i^2/16} \le 2 \cdot 9^g e^{-R_0^2/16}$.

**Theorem 3.11.3 (Theta interpolation, sharp constant).** Assume the packing count and the Gaussian tail bound. Let $Y$ be a theta datum, $q \ge 1$, $c \in \mathbb{N}$ and $R_0 > 0$. Assume the cocycle condition at $q$, $R_0 \le \sqrt{q\pi}\,|\gamma|$ for every nonzero $\gamma \in \Lambda$, $270 \le R_0^2$ and $90(|\iota| + c) \le R_0^2$. Then for every $j \in \mathcal{P}_c$ there is $\beta \in \mathrm{Sec}_q(Y)$ with $D^\alpha \beta = D^\alpha j$ for $|\alpha| \le c$ and $\|\beta\|_q^2 \le 2 \operatorname{Re}\langle j, j\rangle_q$.

Lean: `ReciprocityTheory.ChartRestriction.G.I2.propA_core`

*Proof.* For $a \in V$ put $U_a F(v) = e^{q\pi H(v, a) - q\pi H(a, a)/2} F(v - a)$ and $\Theta F = \sum_{\gamma \in \Lambda} \kappa(\gamma) U_\gamma F$. We use the following facts, which are separate lemmas. For $F \in \mathcal{P}_c$ the series converges, $\Theta F$ is holomorphic, and the derivatives $D^\alpha$ sum term by term. $\Theta F$ is in $\mathrm{Sec}_q(Y)$. $\|\Theta F\|_q^2 = \operatorname{Re}\langle \Theta F, F\rangle_q$. For $G \in \mathcal{P}_c$, $\langle U_a F, G\rangle_q = \langle J_c U_a F, G\rangle_q$ and $|\langle U_a F, G\rangle_q| \le K e^{-q\pi|a|^2/16} N_q(F) N_q(G)$ with $K = 2^{1 + 3(|\iota| + c)/2}$. The sum of $e^{-q\pi|\gamma|^2/16}$ over the nonzero $\gamma \in \Lambda$ is at most $2 \cdot 9^{|\iota|} e^{-R_0^2/16}$. Finally, the two inequalities on $R_0$ give $K \cdot 2 \cdot 9^{|\iota|} e^{-R_0^2/16} \le 1/2$.

First, $\kappa(0) = 1$: the cocycle condition at $\gamma = \gamma' = 0$ gives $\kappa(0)^2 = \kappa(0)$, and $|\kappa(0)| = 1$. Define $T = J_c \circ \Theta$ on $\mathcal{P}_c$. It is $\mathbb{C}$-linear, because $\Theta$ and $J_c$ are linear on smooth functions.

Let $F, G \in \mathcal{P}_c$. Expand $\langle J_c \Theta F, G\rangle_q$ as $\sum_\alpha D^\alpha \Theta F / \alpha! \cdot \langle z^\alpha, G\rangle_q$, sum the derivatives over $\gamma$, and use $\langle U_\gamma F, G\rangle_q = \langle J_c U_\gamma F, G\rangle_q$ for each $\gamma$. This gives $\langle TF, G\rangle_q = \langle \Theta F, G\rangle_q = \sum_\gamma \kappa(\gamma) \langle U_\gamma F, G\rangle_q$. The term $\gamma = 0$ is $\langle F, G\rangle_q$. The other terms have absolute value at most $K e^{-q\pi|\gamma|^2/16} N_q(F) N_q(G)$, since $|\kappa(\gamma)| = 1$. With the tail bound,
$$
|\langle TF, G\rangle_q - \langle F, G\rangle_q| \le \tfrac{1}{2} N_q(F) N_q(G).
$$
At $G = F$ the real part gives $\tfrac12 N_q(F)^2 \le \operatorname{Re}\langle TF, F\rangle_q$. If $TF = 0$, then $N_q(F) = 0$, and a polynomial with zero Gaussian norm is zero. Thus $T$ is injective. As $\mathcal{P}_c$ has finite dimension, $T$ is surjective.

Choose $F \in \mathcal{P}_c$ with $TF = j$, and put $\beta = \Theta F \in \mathrm{Sec}_q(Y)$. For $|\alpha| \le c$, $D^\alpha \beta = D^\alpha J_c \beta = D^\alpha j$. Next, $\|\beta\|_q^2 = \operatorname{Re}\langle \Theta F, F\rangle_q = \operatorname{Re}\langle TF, F\rangle_q = \operatorname{Re}\langle j, F\rangle_q$. The Cauchy-Schwarz inequality gives $\operatorname{Re}\langle j, F\rangle_q \le N_q(j) N_q(F)$. With the lower bound above, $\tfrac12 N_q(F)^2 \le N_q(j) N_q(F)$, so $N_q(F) \le 2N_q(j)$. Hence $\|\beta\|_q^2 \le N_q(j) N_q(F) \le 2 N_q(j)^2 = 2\operatorname{Re}\langle j, j\rangle_q$. $\square$

**Theorem 3.11.4 (Theta interpolation).** Assume the packing count and the Gaussian tail bound. Let $Y$ be a theta datum on $\mathbb{C}^\iota$, $q, c \in \mathbb{N}$ and $R_0 \in \mathbb{R}$ with $1 \le q$, the cocycle condition at $q$, $0 < R_0$, $R_0 \le \sqrt{q\pi}\,|\gamma|$ for every nonzero $\gamma \in \Lambda$, $270 \le R_0^2$ and $90(|\iota| + c) \le R_0^2$. Then for every polynomial $p$ in the coordinates of total degree at most $c$ there is $\beta \in \mathrm{Sec}_q(Y)$ with $D^\alpha \beta = D^\alpha p$ for every $\alpha$ with $|\alpha| \le c$, and
$$
\|\beta\|_q^2 \le 6 \int_V |p(v)|^2 e^{-q\pi |v|^2}\,dv.
$$

Lean: `ReciprocityTheory.ChartRestriction.G.I2.propA`

*Proof.* The function $v \mapsto p(v)$ is in $\mathcal{P}_c$. Apply the sharp form to it. Then $\operatorname{Re}\langle p, p\rangle_q$ is the integral on the right, which is nonnegative, and $2 \le 6$. $\square$

**Definition 3.11.5 (CM datum).** Let $E$ be a CM field with $f = [E:\mathbb{Q}]/2$ and root discriminant $r_d = |d_E|^{1/[E:\mathbb{Q}]}$. A CM datum $X$ is a dimension $d(\tau)$ for each embedding $\tau: E \to \mathbb{C}$ with $d(\tau) + d(\bar\tau) = r$, the space $V = \mathbb{C}^{\mathrm{Idx}}$ with $\mathrm{Idx} = \{(\tau, i) : i < d(\tau)\}$, on which $\alpha \in \mathcal{O}_E$ acts by $\tau(\alpha)$ on the coordinates $(\tau, i)$, a lattice $L$ stable under $\mathcal{O}_E$ on which $\operatorname{Im} H$ is integral and perfect, and a sign $\epsilon: L \to \{\pm 1\}$ with $\epsilon(x + y) = \epsilon(x)\epsilon(y)\cos(\pi \operatorname{Im} H(x, y))$ and $\epsilon(x) = 1$ if $\operatorname{Im} H(\alpha x, x) = 0$ for all $\alpha$. $\mathrm{Sec}(1,1)$ is the space of holomorphic $s$ on $V$ with $s(v + \gamma) = \epsilon(\gamma) e^{\pi H(v,\gamma) + \pi H(\gamma,\gamma)/2} s(v)$ for $\gamma \in L$, with $N(s, w) = |s(w)|^2 e^{-\pi|w|^2}$ and $\|s\|^2$ the average of $N(s, \cdot)$ over a fundamental domain.

**Definition 3.11.6 (Parameters).** Parameters $P$ consist of $q$, $R_0$ and $m$ subject to a list of numerical conditions. Put $g_A = fr$, $d^* = 2fm$, $\kappa_0 = 4 r_d^7 (d^*)^2$, $\theta = (f R_0^2 r_d^{21}/q)^{1/2}$, and let $\lambda_1$ be the first minimum of $L$. The phase is $\varphi = 2f/(r_d^2 \lambda_1^2)$ if $\lambda_1 < \theta$ and $\varphi = 0$ otherwise. Put $p_1 = 1 + g_A \log(1 + 6\sqrt{g_A q})$, $p_2 = \log(2(3d^*)^{d^*})$ and $p_3 = r(p_1 + p_2 + d^*)$.

**Definition 3.11.7 (Split sublattice).** For a subgroup $I \subseteq V$ let $I_{\mathbb{R}}$ be its real span and $u_I(x)$ the orthogonal projection of $-ix$ to $I_{\mathbb{R}}$. Then $\langle u_I(x), a\rangle = \operatorname{Im} H(x, a)$ for $a \in I_{\mathbb{R}}$. $I$ is split for $P$ if: $I \subseteq L$ is saturated, $\mathcal{O}_E$-stable and isotropic for $\operatorname{Im} H$; $\epsilon = 1$ on $I$; $\dim I_{\mathbb{R}} = 2f\rho$ with $\rho \le m$; $I \ne 0$ if and only if $\lambda_1 < \theta$; and four metric conditions hold. One of them is used below: if $x_1, \dots, x_k \in L$ and the vectors $u_I(\alpha x_j)$ for $\alpha \in \mathcal{O}_E$ span $I_{\mathbb{R}}$, then $\varphi \le \sum_j |u_I(x_j)|^2/2$.

To a split $I$ the formalization attaches a theta datum $Y_B$. Its space is $\mathbb{C}^{g_B}$, identified with the orthogonal complement of the complex span of $I_{\mathbb{R}}$. Its lattice is the projection of $\{x \in L : \operatorname{Im} H(x, a) = 0 \text{ for } a \in I\}$, and its $\kappa$ is $\epsilon^q$.

**Theorem 3.11.8 (Zero mode).** Let $I$ be split for $P$, assume the packing count, and let $s \in \mathrm{Sec}(1,1)$. Then there is $\beta \in \mathrm{Sec}_1(Y_B)$ with the following properties.

1. For all $w \in V$ and $T, M \in \mathbb{R}$: if $\sum_{y \in F} e^{-\pi |u_I(w) - y|^2} \le T$ for every finite set $F$ of points $u_I(x)$ with $x \in L$, and the pointwise norm of $\beta$ is at most $M$ everywhere, then $N(s, w)^{1/2} \le M^{1/2} T$.
2. There are $a_1, \dots, a_n \in I$, $n = \dim_{\mathbb{R}} I_{\mathbb{R}}$, with nonzero determinant $\Delta$ in an orthonormal basis of $I_{\mathbb{R}}$, such that $|\Delta| \, 2^{-n/2} \|\beta\|_1^2 \le \|s\|^2$.

Lean: `ReciprocityTheory.ChartRestriction.G.I2.zeroMode`

*Proof.* Take $\beta$ to be the zero Fourier mode of $s$ along $I$: on the complement, $\beta(t)$ is the integral over $t' \in (0,1]^n$ of $G(t + \sum_i t'_i b_i)$, where $b_i$ is a $\mathbb{Z}$-basis of $I$, $G(v) = s(v) e^{-(\pi/2)\sum_k H(v, e_k)^2}$, and $e_k$ is an orthonormal basis of $I_{\mathbb{R}}$. The four claims (membership in $\mathrm{Sec}_1(Y_B)$, property 1, the choice $a = b$ with $\Delta \ne 0$, and the norm inequality) are separate lemmas. $\square$

The next statement uses the sup bound for theta data: for every theta datum $Y$ on $\mathbb{C}^\iota$, $q \ge 1$, $F \in \mathrm{Sec}_q(Y)$ and $v$,
$$
\begin{aligned}
|F(v)|^2 e^{-q\pi|v|^2} \le{}& 2 q^{|\iota|} \Bigl(1 + \frac{4\sqrt{2|\iota|}}{\sqrt{q\pi}\,\lambda_1(Y)}\Bigr)^{2|\iota|} \|F\|_q^2.
\end{aligned}
$$
It also uses a list of nine elementary inputs on lattices and determinants, which contains the packing count and a Hadamard bound.

**Theorem 3.11.9 (Per factor bound).** Let $E$ be a CM field, assume the nine inputs and the sup bound, let $I$ be split for $P$ with $0 < \varphi$, and let $s \in \mathrm{Sec}(1,1)$. Then for every $w \in V$ there is $y \in L$ with
$$
\begin{aligned}
\frac{N(s, w)^{1/2}}{\|s\|} \le{}& e^{p_1 + p_2 + d^*} (\kappa_0 \varphi)^{d^*/4} \\
&\cdot e^{-(\pi/2)|u_I(w) - u_I(y)|^2}.
\end{aligned}
$$

Lean: `ReciprocityTheory.ChartRestriction.G.I2.perFactor_of`

*Proof.* Take $\beta$ and $a$ from the zero mode theorem. Apply the sup bound to $Y_B$ with $q = 1$. Since $g_B \le g_A$, the first minimum of $Y_B$ is at least $\theta$, and $\sqrt{q}\,\theta \ge 1$, the factor in the sup bound is at most $e^{2p_1}$. Thus the pointwise norm of $\beta$ is at most $M = e^{2p_1}\|\beta\|_1^2$.

A separate lemma gives $y \in L$ such that every Gaussian sum in property 1 is at most $T = 2(3d^*)^{d^*} e^{-(\pi/2)|u_I(w) - u_I(y)|^2}$. Property 1 gives $N(s, w)^{1/2} \le e^{p_1}\|\beta\|_1 T$. If $\|\beta\|_1 = 0$, the left side is $0$ and the claim holds. Otherwise put $c = |\Delta| 2^{-n/2} > 0$. Property 2 gives $\sqrt{c}\,\|\beta\|_1 \le \|s\|$, so $\|s\| > 0$. A covolume lower bound for $I$, which uses the Hadamard bound, and a separate estimate give $c^{-1/2} \le e^{d^*}(\kappa_0\varphi)^{d^*/4}$. Then
$$
\begin{aligned}
N(s, w)^{1/2} &\le e^{p_1} T c^{-1/2} \cdot \sqrt{c}\,\|\beta\|_1 \\
&\le e^{p_1} T e^{d^*} (\kappa_0\varphi)^{d^*/4} \|s\|,
\end{aligned}
$$
and $2(3d^*)^{d^*} = e^{p_2}$. $\square$

**Theorem 3.11.10 (Pointwise bound at generators).** Assume the nine inputs, the existence of a split sublattice for all parameters, the sup bound, and the dimension bound $\dim \mathrm{Sec}_q(Y) \le q^{|\iota|}$. Let $E$ be a CM field, $X$ a CM datum, $P$ parameters, $r_1 \ge 2$, and $a_1, \dots, a_r \in V$ with $r_1^2 a_j \in L$, such that every $x \in L$ is $\sum_j \alpha_j r_1^2 a_j + r_1 y$ with $\alpha_j \in \mathcal{O}_E$ and $y \in L$. Let $s \in \mathrm{Sec}(1,1)$ be nonzero. If $0 < \varphi$, then
$$
\begin{aligned}
\prod_{j=1}^r \frac{N(s, a_j)^{1/2}}{\|s\|} \le{}& e^{p_3} (\kappa_0\varphi)^{r d^*/4} e^{-\pi\varphi/r_1^4}.
\end{aligned}
$$
If $\varphi = 0$, the product is at most $e^{r p_1}$.

Lean: `ReciprocityTheory.ChartRestriction.G.I2.tOf`

*Proof.* Let $0 < \varphi$. Take a split $I$ and apply the per factor bound to each $a_j$. This gives $y_j \in L$ and, with $C = e^{p_1 + p_2 + d^*}(\kappa_0\varphi)^{d^*/4}$ and $D_j = |u_I(a_j) - u_I(y_j)|^2$, a bound of the product by $C^r e^{-(\pi/2)\sum_j D_j}$. Here $C^r = e^{p_3}(\kappa_0\varphi)^{r d^*/4}$. Put $x_j = r_1^2 a_j - r_1^2 y_j \in L$. A separate lemma, which uses the generation hypothesis, shows that the vectors $u_I(\alpha x_j)$ span $I_{\mathbb{R}}$. The split condition gives $\varphi \le \sum_j |u_I(x_j)|^2/2$. As $u_I$ is $\mathbb{R}$-linear, $|u_I(x_j)|^2 = r_1^4 D_j$, so $\varphi \le (r_1^4/2)\sum_j D_j$ and $e^{-(\pi/2)\sum_j D_j} \le e^{-\pi\varphi/r_1^4}$.

Let $\varphi = 0$. A separate lemma, which applies the sup bound to $X$ as a theta datum, bounds each factor by $e^{p_1}$. The product of $r$ factors is at most $e^{r p_1}$. $\square$

**Remark 3.11.11 (Formalization).** The sharp form gives the factor $2$, and the stated form weakens it to $6$ ([PaThDiffLe.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/PaThDiffLe.lean#L259)). The pointwise bound at generators takes the dimension bound as a hypothesis and does not use it, and it does not use $s \ne 0$ ([PerFactor.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/PerFactor.lean#L19)). The wrapper `perFactor` also drops the dimension bound and $s \ne 0$ ([PerFactor.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/PerFactor.lean#L14)). The per factor bound takes all nine inputs and uses two of them ([L2NonnegGT.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/L2NonnegGT.lean#L113)). We did not open the convergence, membership and unfolding lemmas for $\Theta$, the jet identity, the translate bound, the tail sum, the numerical inequality, the three facts on the zero mode, the Gaussian sum lemma, the covolume bound, the span lemma, the phase zero lemma, or the proofs of the sup bound and of the existence of split sublattices.
