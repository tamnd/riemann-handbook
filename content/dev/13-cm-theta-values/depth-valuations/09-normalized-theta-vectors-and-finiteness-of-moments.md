---
title: Normalized theta vectors and the finiteness of moments
decls:
  - GlobalTheory.MomN.transPrime_int
  - GlobalTheory.T.normalizedVector_translates_prime_order_integral
  - GlobalTheory.MomFin.moments_fin
  - GlobalTheory.T.unitPeriodTranslates_moments_finite
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normalized theta vectors and the finiteness of moments

This section proves that the jets of the torsion translates of the normalized theta vectors, sent into $\mathbb{C}_p$ for a split prime $p$, are the moments of measures of norm at most $1$. The measures come from the [theorem on moments of theta translates](/entry/moments-of-translates/), and the norm bound comes from the lattice integrality of the previous section, which we first extend to normalized theta vectors. The result is the analytic input of the [integral jet moments](/entry/jet-moments/) of the next section.

### Characters and the equivariance laws

We keep the datum $D$, the curve ideal $\mathfrak{c}$, the root $\delta$ with $\delta^{12} = \Delta(\varphi_0(\mathfrak{c}))$, the base $B$ and the spaces $V_{N, N'}$ with lattices $\Lambda_{L, L'}$ of the [previous section](/entry/translates-lat-int/). Let $x \mapsto \bar x$ be complex conjugation on $E$.

**Definition 4.9.1.** A function $\chi$ on the fractional ideals of $E$ is an *admissible character* if $\chi(\mathfrak{a}\mathfrak{b}) = \chi(\mathfrak{a})\chi(\mathfrak{b})$ for all ideals with $\mathfrak{a}\bar{\mathfrak{a}} = \mathcal{O}_E$ and $\mathfrak{b}\bar{\mathfrak{b}} = \mathcal{O}_E$, and $\chi(z\mathcal{O}_E) = \prod_{\tau \in \mathcal{T}} \tau(z)^{-1}$ for every $z \in E$ with $z \bar z = 1$. A quadruple $(N, N', L, L')$ is *admissible* if $N$ and $N'$ are even and $L \subseteq E^N$, $L' \subseteq E^{N'}$ are self-dual Hermitian $\mathcal{O}_E$-lattices.

So $\chi$ is multiplicative on the ideals of relative norm one, with a fixed infinity type on the principal ones. For an admissible character and an admissible quadruple, the base gives a *normalized theta vector* $e_\chi(L, L') : V_{N, N'} \to \mathbb{C}$. A unitary pair $(\gamma, \gamma') \in U_N(E) \times U_{N'}(E)$ acts on functions on $V_{N, N'}$ by a pullback $(\gamma, \gamma')^*$, and a change of lattice $\Lambda_{L, L'} \to \Lambda_{L, L''}$ gives an intertwining operator $I$ between the theta spaces.

**Definition 4.9.2.** The normalized vectors satisfy the *equivariance laws* for $\chi$ if for all even $N, N'$ and self-dual lattices:
1. $(\gamma, \gamma')^* e_\chi(L, L') = e_\chi(\gamma L, \gamma' L')$ for every unitary pair;
2. $e_\chi(L, L'') = \chi(\det(L', L''))^{-N/2}\, I\big(e_\chi(L, L')\big)$, where $\det(L', L'')$ is the determinant ideal of $L''$ relative to $L'$;
3. $e_\chi(L_1, L') = \chi(\det(L, L_1))^{N'/2}\, I\big(e_\chi(L, L')\big)$.

### Integrality of the translates

**Theorem 4.9.3 (translates of normalized theta vectors).** Assume that for every datum, curve ideal $\mathfrak{c}$, twelfth root $\delta$, base $B$ and admissible character $\chi$, the normalized vectors satisfy the equivariance laws for $\chi$. Let $\mathfrak{c}$ be a curve ideal, $\delta$ and $B$ as above, $q \neq 2$ a prime with $\left(\frac{-d}{q}\right) = 1$ and $N(\mathfrak{c})$ prime to $q$, $\iota : \mathbb{C} \to \mathbb{C}_q$ a field isomorphism and $(\delta_0, \theta, \Omega)$ a [period datum](/entry/exists-per/) for $\iota$. Let $\chi$ be an admissible character and $(N, N', L, L')$ an admissible quadruple. Let $t \in V_{N, N'}$ be of order prime to $q$ for $\Lambda_{L, L'}$. Then $U_t e_\chi(L, L')$ is lattice integral for $(\iota, \Omega/\iota(\delta_0), \Lambda_{L, L'})$.

Lean: `GlobalTheory.MomN.transPrime_int` (also `GlobalTheory.T.normalizedVector_translates_prime_order_integral`, a second name).

*Proof.* Step 1 (weak approximation). Since $q$ splits and is odd, there are unitary matrices $\gamma, \gamma'$ over $E$ and lattices $M$, $M'$ with $L = \gamma M$, $L' = \gamma' M'$, such that $M$ and $M'$ agree with the standard lattices up to integers $a$ and $b$ prime to $q$.

Step 2 (equivariance). By the first equivariance law, $U_t e_\chi(L, L') = U_t\big((\gamma, \gamma')^* e_\chi(M, M')\big)$. The pullback by a unitary pair commutes with translation up to the change of point: there is a linear map $g$ with $g(\Lambda_{L, L'}) \subseteq \Lambda_{M, M'}$ and $U_t\big((\gamma, \gamma')^* F\big) = (U_{g t} F) \circ g$. The point $g t$ is of order prime to $q$ for $\Lambda_{M, M'}$.

Step 3 (expansion in tensor powers). The translate $U_{g t} e_\chi(M, M')$ is a finite sum $\sum_k c_k U_{s_k} \Theta_{N, N'}$, where the $c_k$ are algebraic with $\|\iota(c_k)\| \leq 1$ and the $s_k$ are of order prime to $q$ for the standard lattice. By the [theorem on tensor powers](/entry/lat-int-u-th-zero/) each term is lattice integral for $\Lambda_{\mathrm{std}}$, and by the sum property so is the sum.

Step 4 (pullback). Since $M$, $M'$ agree with the standard lattices up to $a$ and $b$, the integer $ab$ is prime to $q$ and $ab\, g(y) \in \Lambda_{\mathrm{std}}$ for every $y \in \Lambda_{L, L'}$. The pullback property along $g$ gives the lattice integrality of $U_t e_\chi(L, L') = (U_{g t} e_\chi(M, M')) \circ g$ for $\Lambda_{L, L'}$. $\square$


### The moment statement

Let $p$ be a prime and $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ a ring homomorphism. On $V_{N, N'}$ let $H$ be the Hermitian form of the base, $\kappa(x, y) = e^{-2\pi i \operatorname{Im} H(x, y)}$, and $W_y = \epsilon(y) U_y$ with a sign $\epsilon(y) = \pm 1$. For matrices $x, y \in M_{N' \times N}(E)$ put $h(x, y) = \operatorname{Tr}_{E/K} \sum_{i,j} x_{ij} \bar y_{ij} \in K$, and let $\operatorname{emb}(x) = (\tau(x_{ij}))_{\tau, i, j} \in V_{N, N'}$. Let $Y(L, L')$ be the $\mathcal{O}_E$-module spanned by the matrices $a A$ with $a \in \mathfrak{b}^{-1}$ and $A$ a homomorphism from $L$ to $L'$. A family $b_1, \dots, b_r \in M_{N' \times N}(E)$ is a *$p$-local basis* if it is $K$-linearly independent, $s b_i \in Y(L, L')$ for some $s$ prime to $p$, every $y \in Y(L, L')$ has $s y \in \sum_i \mathcal{O}_K b_i$ for some $s$ prime to $p$, and $\delta \operatorname{emb}(b_i) \in \Lambda_{L, L'}$ for each $i$. For $N_0, n \geq 0$ let $Y_n(N_0)$ be the subgroup of $V_{N, N'}$ generated by the points $\varphi_0(\kappa) N_0 p^{-n} x$ with $x \in \Lambda_{L, L'}$ and $\kappa \in \mathcal{O}_K$ with $\|\lambda(\varphi_0(\bar\kappa))\| \leq p^{-2n}$.

**Definition 4.9.4.** Let $e = (e(N, N', L, L'))$ be a family of functions and $\Omega \in \mathbb{C}_p$. The *moment statement* for $(e, \lambda, \Omega)$ says the following. For every admissible quadruple and every $t \in V_{N, N'}$ of order prime to $p$ for $\Lambda_{L, L'}$ there is $N_0$ prime to $p$ with this property: for every $p$-local basis $b_1, \dots, b_r$ there is a continuous linear form $\mu$ on $C(\mathbb{Z}_p^r, \mathbb{C}_p)$ with $\|\mu\| \leq 1$ such that for all $n \geq 0$ and $y \in Y_n(N_0)$, with $G = W_y U_t\, e(N, N', L, L')$:
1. all Taylor coefficients of $G$ at $0$ are algebraic;
2. for all directions $y'_1, \dots, y'_m \in M_{N' \times N}(E)$ and every continuous $g$ on $\mathbb{Z}_p^r$ with
$$g(a) = \lambda\Big(\kappa\big(\delta \operatorname{emb}\big(\textstyle\sum_i a_i b_i\big), y\big)\Big) \prod_{j=1}^m \Omega^{-1} \sum_{i=1}^r a_i\, \lambda\big(\varphi_0(h(y'_j, b_i))\big) \quad (a \in \mathbb{N}^r),$$
the derivative of the series $\lambda(\mathrm{tay}\, G)$ at $0$ in the directions $\operatorname{emb}(y'_1), \dots, \operatorname{emb}(y'_m)$ equals $\mu(g)$.

So the jets of the twisted torsion translates are the moments of one bounded measure, twisted by the characters $a \mapsto \lambda(\kappa(\cdot, y))$ of $p$-power order.

**Theorem 4.9.5 (finiteness of moments).** Assume:
1. for every datum, curve ideal $\mathfrak{c}$, root $\delta$, base $B$ and admissible character $\chi$, the normalized vectors satisfy the equivariance laws for $\chi$;
2. for the same data, every admissible quadruple and every $t \in V_{N, N'}$ with $a t \in \Lambda_{L, L'}$ for some integer $a > 0$, all Taylor coefficients of $U_t e_\chi(L, L')$ at $0$ are algebraic.

Let $D$, $\mathfrak{c}$, $\delta$, $B$ and an admissible character $\chi$ be given. Let $p \neq 2$ be a prime with $\left(\frac{-d}{p}\right) = 1$ and $N(\mathfrak{c})$ prime to $p$, and let $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ be a ring homomorphism. Then there is $\Omega \in \mathbb{C}_p$ with $\|\Omega\| = 1$ such that the moment statement holds for $(e_\chi, \lambda, \Omega)$.

Lean: `GlobalTheory.MomFin.moments_fin` (also `GlobalTheory.T.unitPeriodTranslates_moments_finite`, a second name).

*Proof.* Step 1 (the period). The host field gives that $d$ is prime with $d \equiv 7 \pmod{16}$, and $p$ is split for $d$. Extend $\lambda$ to a field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_p$. The [existence of period data](/entry/exists-per/) gives $(\delta_0, \theta, \Omega_0)$ for $\iota$. The ratio $\delta/\delta_0$ of the two twelfth roots of discriminants is algebraic, and $\iota(\delta/\delta_0)$ is a unit. Put $\Omega = \Omega_0 N(\mathfrak{c}) \lambda(\delta/\delta_0)$. Then $\|\Omega\| = 1$, since $N(\mathfrak{c})$ is prime to $p$.

Step 2 (the setup). Fix an admissible quadruple and $t$ with $N_0 t \in \Lambda_{L, L'}$, $N_0 > 0$ prime to $p$. A complex linear isomorphism $e : V_{N, N'} \to \mathbb{C}^g$ carries $\Lambda_{L, L'}$ and $H$ to the lattice and the Hermitian form of an admissible setup, in the sense of [the earlier section](/entry/moments-of-translates/). The function $e' = e_\chi(L, L') \circ e^{-1}$ is a theta function of the setup. Hypothesis 2 at $t = 0$ makes its Taylor coefficients algebraic, so $e'$ has algebraic jets for $\delta_0$. A $p$-local basis $b$ goes to a basis $e(\delta \operatorname{emb}(b_i))$ prime to $p$.

Step 3 (the measure). The [theorem on moments of theta translates](/entry/moments-of-translates/) applies to $e'$ and the point $e(t)$, which is prime to $p$. It gives a continuous linear form $\mu$ with the moment property for $U_{e(t)} e'$.

Step 4 (the norm). A moment measure is determined by its moments, since polynomials are dense in $C(\mathbb{Z}_p^r, \mathbb{C}_p)$ by Mahler's theorem. So $\|\mu\| \leq 1$ holds exactly when the moments in the basis directions are those of a measure of norm at most $1$, that is, when $U_{e(t)} e'$ is lattice integral for the lattice of the setup. Now $U_{e(t)} e' = (U_t e_\chi(L, L')) \circ e^{-1}$. The theorem of the previous subsection, which uses hypothesis 1, makes $U_t e_\chi(L, L')$ lattice integral for $\Lambda_{L, L'}$, and the pullback property along $e^{-1}$ (with $s = 1$) carries this to $\mathbb{C}^g$.

Step 5 (the twisted translates). Let $y \in Y_n(N_0)$. The operator $W_y$ agrees with the operator of a standard lift built from an idempotent of $\mathcal{O}_K$, as in the moment property. Hypothesis 2 and the algebraicity of the coefficients of Weil translates give part 1. A continuous function on $\mathbb{Z}_p^r$ is determined by its values on the dense subset $\mathbb{N}^r$, so the function $g$ of part 2 is the test function of the moment property. The pairing of the scaled directions $\delta^{-1} e(\operatorname{emb}(y'_j))$ with the basis matches $\Omega^{-1} \lambda(\varphi_0(h(y'_j, b_i)))$ by the choice of $\Omega$. The moment property then gives part 2. $\square$

**Remark 4.9.6 (Formalization).** The two names with the prefix `GlobalTheory.T.` are second names, proved by `first | exact @…` under `maxHeartbeats 1000000`. The equivariance hypothesis quantifies over all data but is used only at the given base ([UnitPeriodTranslatesMomentsFinite.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/UnitPeriodTranslatesMomentsFinite.lean#L125)). The equality $\|\mu\| = N$ of the moments theorem is discarded at line 116, since the norm bound comes from Step 4. The sign $\epsilon(y)$ is a choice by the axiom of choice for $p \neq 2$ ([ColumnData.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData.lean#L267)). We read the statements of the lemmas of Steps 1, 2 and 5 but not their proofs, and we did not unfold the construction of $e_\chi$ or of the intertwining operators. The word "finite" in the second name does not describe the conclusion, which is a norm bound. The conclusion excludes $p = 2$ and asks only $\|\Omega\| = 1$.
