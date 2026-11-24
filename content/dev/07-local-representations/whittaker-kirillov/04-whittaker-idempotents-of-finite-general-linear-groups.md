---
title: Whittaker idempotents of finite general linear groups
decls:
  - GlobalTheory.BadShare.rk_lev_lower
  - GlobalTheory.T.rank_levelIdempotent_lower_bound_generic
  - GlobalTheory.BadShare.series_weight_lower_bound
  - GlobalTheory.T.series_representation_weight_lower_bound
  - GlobalTheory.BadShare.badWeight_le
  - GlobalTheory.T.badLabelTuple_weight_le_bound
  - GlobalTheory.BadShare.ShareThm.bad_share
  - GlobalTheory.T.badRows_share_bound_two_primes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Whittaker idempotents of finite general linear groups

This section is the finite field analogue of the Whittaker theory of the previous sections. For a prime $g$, the group $\mathrm{GL}_N(\mathbb{F}_g)$ has idempotents in its group algebra built from characters of unipotent subgroups. We bound from below the rank of such an idempotent on a generic representation, and we bound the share of the idempotent that falls outside a set of good irreducible representations. The last theorem combines two primes and gives a lower bound for the rank of the good part. It is used in [Theorem](/entry/bad-share-win/). For the background, see [generic representations and local factors](/learn/representations/#generic-representations-and-local-factors) and [generic characters](/learn/periods/#generic-characters).

### The group algebra

Let $G$ be a finite group. A function $a \colon G \to \mathbb{C}$ is an element of the group algebra. The product is the convolution
$$(a * b)(x) = \sum_{y \in G} a(y)\, b(y^{-1}x).$$
The unit is the Dirac function $\delta$, with $\delta(1) = 1$ and $\delta(x) = 0$ for $x \neq 1$.

**Definition 4.4.1 (Operator and rank).** Let $(\rho, M)$ be a finite-dimensional complex representation of $G$ and $e \colon G \to \mathbb{C}$. Put $\rho(e) = \sum_{\gamma} e(\gamma)\rho(\gamma)$. The *rank* of $e$ on $\rho$ is $\operatorname{rk}_\rho(e) = \dim \rho(e)M$.

Then $\rho(a * b) = \rho(a)\rho(b)$. So an idempotent $e$ gives a projection $\rho(e)$, and its rank is its trace: $\operatorname{rk}_\rho(e) = \sum_\gamma e(\gamma)\operatorname{tr}\rho(\gamma)$.

**Definition 4.4.2 (Projector).** A function $e$ is a *projector* if $e * e = e$ and $e(x^{-1}) = \overline{e(x)}$ for all $x$.

**Definition 4.4.3 (Central idempotent).** For the character $\chi$ of an irreducible representation of $G$, put $z_\chi(\gamma) = \frac{\chi(1)}{|G|}\chi(\gamma^{-1})$.

This is the classical central idempotent of $\chi$. On an irreducible representation it acts by $1$ if the character is $\chi$, and by $0$ otherwise.

**Definition 4.4.4 (Character idempotent).** Let $S \subset G$ be a subgroup and $\chi$ a character of $S$. Put $\varepsilon_{S,\chi}(\gamma) = \chi(\gamma)^{-1}/|S|$ for $\gamma \in S$, and $\varepsilon_{S,\chi}(\gamma) = 0$ otherwise.

This is a projector. The image of $\rho(\varepsilon_{S,\chi})$ is the space of vectors $x$ with $\rho(u)x = \chi(u)x$ for $u \in S$.

For a finite family of groups $G_v$, $v \in \iota$, and functions $e_v$ on $G_v$, the tensor product is $(\otimes_v e_v)(\gamma) = \prod_v e_v(\gamma_v)$, a function on $\prod_v G_v$. It satisfies $(\otimes a_v) * (\otimes b_v) = \otimes (a_v * b_v)$. For two groups we write $a \otimes b$.

### Level data

Fix a prime $g$ and $N \geq 1$. Let $G_N = \mathrm{GL}_N(\mathbb{F}_g)$. Index rows and columns by $0, \dots, N-1$. Let $U \subset G_N$ be the upper unitriangular group.

**Definition 4.4.5 (Level datum).** A *level datum* $L$ consists of a flag $\sharp \in \{\text{true}, \text{false}\}$, integers $s, k \geq 0$ with $s + k < N$, a nontrivial additive character $\psi$ of $\mathbb{F}_g$ and units $c_0, \dots, c_{N-1} \in \mathbb{F}_g^\times$. Its group $U_L$ is $U$ if $L$ is not sharp. If $L$ is sharp, $U_L$ is the set of $u \in U$ with $u_{a, s+k} = 0$ for $s \leq a < s + k$. Its *edges* are the pairs $(a, a+1)$ if $L$ is not sharp. If $L$ is sharp, the edges are the pairs $(a, a+1)$ with $a + 1 \neq s$ and, when $k > 0$, $a + 1 \neq s + k$, together with the pair $(s-1, s+k)$. Its character is
$$\chi_L(u) = \psi\Big(\sum_{(a,b) \text{ edge}} c_a u_{ab}\Big), \qquad u \in U_L.$$
Its *idempotent* is $e_L = \varepsilon_{U_L, \chi_L}$.

The edges are chosen so that the entries $u_{ab}$ at the edges add under multiplication in $U_L$. So $\chi_L$ is a character of $U_L$ and $e_L$ is a projector. If $L$ is not sharp, $\chi_L$ is a generic character of $U$ and $e_L$ is the Whittaker idempotent. For example, with $N = 5$, $s = 1$, $k = 2$ and $L$ sharp, the edges are $(0, 3)$, $(1, 2)$ and $(3, 4)$.

**Definition 4.4.6 (Generic representation).** A representation $(\rho, M)$ of $G_N$ is *generic* if there are a level datum $L$ that is not sharp and a vector $x \neq 0$ with $\rho(u)x = \chi_L(u)x$ for all $u \in U$.

**Theorem 4.4.7 (Rank of a level idempotent).** Let $(\rho, M)$ be a finite-dimensional generic representation of $G_N$. Let $L$ be a level datum. Put $k' = k$ if $L$ is sharp and $k' = 0$ otherwise. Then
$$\Big(1 - \frac{1}{g}\Big) g^{k'} \leq \operatorname{rk}_\rho(e_L).$$

Lean: `GlobalTheory.BadShare.rk_lev_lower` (also `GlobalTheory.T.rank_levelIdempotent_lower_bound_generic`).

*Proof.* Suppose $L$ is not sharp. The rank of $e_L$ does not depend on the coefficients $c_a$ or on the additive character, only on the shape of $L$: the torus conjugates one such character to another. So we may replace $L$ by the non-sharp datum $L_0$ that witnesses genericity. The vector $x$ lies in the image of $\rho(e_{L_0})$, so the rank is at least $1 \geq 1 - 1/g$.

Suppose $L$ is sharp. We argue by induction on $s$. For $s = 0$ the rows $0, \dots, k-1$ are free above the column $k$, and a generic vector gives at least $(1 - 1/g)g^k$ independent vectors in the image of $\rho(e_L)$. For the step, let $L'$ be the datum with the same data and $s - 1$ in place of $s$. A root exchange, a conjugation that moves one root group of $U_{L'}$ to one root group of $U_L$, shows $\operatorname{rk}_\rho(e_{L'}) \leq \operatorname{rk}_\rho(e_L)$. The induction hypothesis for $L'$ gives the bound. $\square$

### Series representations

Let $\mathcal{S}_N$ be the set of monic squarefree polynomials $f \in \mathbb{F}_g[X]$ of degree $N$ with $f(0) \neq 0$. For $f \in \mathcal{S}_N$ with irreducible factors of degrees $d_1, \dots, d_r$, put
$$T(f) = \prod_{i=1}^{r} (g^{d_i} - 1).$$
This is the order of the maximal torus of $G_N$ attached to $f$: the centralizer of a semisimple element with characteristic polynomial $f$.

**Definition 4.4.8 (Series).** A *series* is a map $\tau$ from $\mathcal{S}_N$ to class functions on $G_N$, injective on $\mathcal{S}_N$, such that for each $f \in \mathcal{S}_N$ there is a simple representation $V_f$ with character $\tau(f)$ that is generic and satisfies
$$\dim V_f \cdot T(f) = \prod_{i=1}^{N} (g^i - 1).$$

For example, the irreducible representations of Deligne-Lusztig type $\pm R_{T,\theta}$ with $\theta$ in general position have this dimension (Digne-Michel, *Representations of Finite Groups of Lie Type*, Chapter 12).

**Theorem 4.4.9 (Weight of a series representation).** Let $\tau$ be a series and $L$ a level datum. Then for each $f \in \mathcal{S}_N$ there is a real number $w$ with
$$(z_{\tau(f)} * e_L)(1) = w\, e_L(1), \qquad w \geq \Big(1 - \frac{1}{g}\Big)\frac{1}{T(f)}.$$

Lean: `GlobalTheory.BadShare.series_weight_lower_bound` (also `GlobalTheory.T.series_representation_weight_lower_bound`).

*Proof.* Let $V = V_f$, $d = \dim V$, $J = |U_L|$ and $r = \operatorname{rk}_{V}(e_L)$. Put $k' = k$ if $L$ is sharp and $k' = 0$ otherwise. For an irreducible character $\chi$ and a projector $e$, $(z_\chi * e)(1) = \frac{\chi(1)}{|G|}\sum_\gamma \chi(\gamma)e(\gamma)$, which equals $d\, r/|G|$ by the trace formula for the rank. Also $e_L(1) = 1/J$. The order of $G_N$ is $g^{N(N-1)/2}\prod_{i=1}^N(g^i - 1)$, and a count of the entries of $U_L$ gives $J \cdot g^{k'} = g^{N(N-1)/2}$. With the dimension formula of the series, $|G_N| = J g^{k'} d\, T(f)$. Hence
$$(z_{\tau(f)} * e_L)(1) = \frac{d\, r}{J g^{k'} d\, T(f)} = \frac{r}{g^{k'}T(f)}\, e_L(1) \cdot J \cdot \frac{1}{J}.$$
So $w = r/(g^{k'}T(f))$. By [Theorem 4.4.7](/entry/rk-lev-lower/), applied to the generic $V$, $r \geq (1 - 1/g)g^{k'}$. $\square$

### The bad share

We now take a finite set $\iota$ of copies of $G_N$. For each $v \in \iota$, let $\tau_v$ be a series and $L_v$ a level datum. Fix $m \geq 0$ and units $\mathrm{ch}_v(j) \in \mathbb{F}_g^\times$ for $v \in \iota$ and $j < m$. A tuple $F = (F_v) \in \mathcal{S}_N^\iota$ is *good* if it satisfies a condition on the roots of the $F_v$ relative to the units $\mathrm{ch}_v(j)$ and their inverses, defined in the chapter on cyclotomic norms. Let $\mathcal{G}$ be the set of good tuples, and put
$$A = \sum_{F \in \mathcal{G}} \bigotimes_{v} z_{\tau_v(F_v)}.$$
This is a central projector of the group algebra of $G_N^\iota$, the sum of the central idempotents of the good tuples.

**Definition 4.4.10 (Admissible primes).** Let $g, q, d$ be primes. The triple is *admissible* if $q$ and $d$ are odd and distinct, $\max(q, d) \geq 16$, $16qd$ divides $g - 1$ and $g \geq 2^{12}$.

**Definition 4.4.11 (Bad bound).** For real numbers $g, f, m, N, q$ put
$$\begin{aligned} \beta(g, f, m, N, q) = {} & \frac{3f}{g} + \frac{23 f\log g}{\sqrt{g}} + 2fm\Big(\frac{1}{4q} + \frac{1 + \log N}{g - 1}\Big) \\ & + \frac{N}{2}\Big(\frac{7}{8}\Big)^{f} + \exp\Big(-\frac{f}{10\log N}\Big). \end{aligned}$$

**Theorem 4.4.12 (Weight of the bad tuples).** Let $N \geq 100000$, let $(g, q, d)$ be admissible and let each $\tau_v$ be a series. Put $E = \bigotimes_v e_{L_v}$. Then there is a real number $w$ with
$$((\delta - A) * E)(1) = w\, E(1), \qquad w \leq \beta\big(g, |\iota|, m, N, \min(q, d)\big).$$

Lean: `GlobalTheory.BadShare.badWeight_le` (also `GlobalTheory.T.badLabelTuple_weight_le_bound`).

*Proof.* For each $v$ and $f$, let $w_v(f)$ be the weight of [Theorem 4.4.9](/entry/series-weight-lower-bound/). Since convolution of tensors is the tensor of the convolutions,
$$((\delta - A) * E)(1) = E(1) - \sum_{F \in \mathcal{G}} \prod_v w_v(F_v)\, E(1).$$
So $w = 1 - \Sigma_w$ with $\Sigma_w = \sum_{F \in \mathcal{G}}\prod_v w_v(F_v)$. Put $\Sigma = \sum_{F \in \mathcal{G}}\prod_v T(F_v)^{-1}$. The lower bound for each $w_v$ and Bernoulli's inequality give
$$\Sigma_w \geq \Big(1 - \frac{1}{g}\Big)^{|\iota|}\Sigma \geq \Big(1 - \frac{|\iota|}{g}\Big)\Sigma.$$
The counting theorem for good tuples gives $\Sigma \geq 1 - (\beta - |\iota|/g)$, under the hypotheses $N \geq 100000$ and admissibility. The mass bound $\sum_{f \in \mathcal{S}_N} T(f)^{-1} \leq 1$ gives $\Sigma \leq 1$. Then $1 - \Sigma_w \leq 1 - \Sigma + (|\iota|/g)\Sigma \leq (\beta - |\iota|/g) + |\iota|/g = \beta$. $\square$

### Two primes

Now let $g_1$ and $g_2$ be primes, with data $\iota_i$, $L^{(i)}$, $\tau^{(i)}$ and $\mathrm{ch}^{(i)}$ as above at $g_i$, and the same $N$, $m$, $q$, $d$. Put $H_i = G_N(\mathbb{F}_{g_i})^{\iota_i}$, $E_i = \bigotimes_v e_{L^{(i)}_v}$ and $A_i$ the good projector at $g_i$. An element $\gamma \in H_i$ is *unipotent* if each component $\gamma_v - 1$ is nilpotent. The projector $E_i$ is supported on unipotent elements, since $U_L \subset U$.

**Definition 4.4.13 (Counting at unipotents).** Let $(\rho, M)$ be a finite-dimensional representation of $H_1 \times H_2$ and $\epsilon \geq 0$. Then $\rho$ *counts at unipotents with error* $\epsilon$ if there is $c > 0$ such that every projector $e$ on $H_1 \times H_2$ that is supported on pairs whose first component is unipotent, or on pairs whose second component is unipotent, satisfies
$$\big|\operatorname{rk}_\rho(e) - c\, \mathrm{Re}\, e(1)\big| \leq \epsilon\, c\, \mathrm{Re}\, e(1).$$

For the regular representation this holds with $\epsilon = 0$ and $c = |H_1 \times H_2|$, since $\operatorname{rk}(e) = |H|e(1)$. It also holds with $\epsilon = 0$ when the character of $\rho$ vanishes on the nontrivial elements with a unipotent component.

**Theorem 4.4.14 (Bad share for two primes).** Let $N \geq 100000$. Let $(g_1, q, d)$ and $(g_2, q, d)$ be admissible. Let all $\tau^{(i)}_v$ be series. Let $(\rho, M)$ be a finite-dimensional representation of $H_1 \times H_2$ that counts at unipotents with error $\epsilon$, where $0 \leq \epsilon < 1$. Put $\beta_i = \beta(g_i, |\iota_i|, m, N, \min(q, d))$. Then
$$\Big(1 - \frac{1 + \epsilon}{1 - \epsilon}\big(\max(0, \beta_1) + \max(0, \beta_2)\big)\Big)\operatorname{rk}_\rho(E_1 \otimes E_2) \leq \operatorname{rk}_\rho\big((A_1 \otimes A_2) * (E_1 \otimes E_2)\big).$$

Lean: `GlobalTheory.BadShare.ShareThm.bad_share` (also `GlobalTheory.T.badRows_share_bound_two_primes`).

*Proof.* Write $E = E_1 \otimes E_2$, $P = \rho(A_1 \otimes \delta)$ and $Q = \rho(\delta \otimes A_2)$. These are commuting projections, since $A_1$ and $A_2$ are central. For projections $P$, $Q$ and any operator $R$ on a finite-dimensional space,
$$\operatorname{rk}(R) \leq \operatorname{rk}(PQR) + \operatorname{rk}((1 - P)R) + \operatorname{rk}((1 - Q)R).$$
Apply this with $R = \rho(E)$. Then $PQR = \rho((A_1 \otimes A_2) * E)$, $(1 - P)R = \rho(((\delta - A_1) * E_1) \otimes E_2)$ and $(1 - Q)R = \rho(E_1 \otimes ((\delta - A_2) * E_2))$. The functions $E$, $((\delta - A_1) * E_1) \otimes E_2$ and $E_1 \otimes ((\delta - A_2) * E_2)$ are projectors, because $\delta - A_i$ is a central projector and $E_i$ is a projector. The first two are supported where the second component is unipotent, and the third where the first is unipotent. So counting at unipotents applies to all three. With $x = c\,\mathrm{Re}\,E(1)$, [Theorem 4.4.12](/entry/bad-weight-le/) gives values $w_1 x$ and $w_2 x$ at $1$ for the last two, with $w_i \leq \beta_i$. Write $D = \operatorname{rk}(E)$, $D_0 = \operatorname{rk}(PQR)$ and $D_i$ for the two other ranks. Then $|D - x| \leq \epsilon x$ gives $x \leq D/(1 - \epsilon)$, and $D_i \leq (1 + \epsilon)w_i x \leq (1 + \epsilon)\max(0, \beta_i)\,D/(1 - \epsilon)$. Insert these in $D \leq D_0 + D_1 + D_2$. $\square$

**Remark 4.4.15 (Formalization).** Each of the four theorems has a wrapper in the namespace `GlobalTheory.T`, proved by `first | exact` at line 7 of its `Statement` file. The good condition is `Formalism.CyclotomicNorms.IsGood`, which we did not unfold; the definition of the good set is in [SamePartIffOfNeZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/SamePartIffOfNeZero.lean#L37). The bad bound takes its second argument under the name `f`, but it is always called with the number $|\iota|$ of factors, not with a polynomial. The counting theorem for good tuples, the root exchange and the base case $s = 0$ of the first theorem were read only as statements. The proof of the first theorem gives rank at least $1$ in the non-sharp case, which is stronger than the stated bound. The chapter is about Whittaker models of $p$-adic groups, but this section is pure finite group theory.
