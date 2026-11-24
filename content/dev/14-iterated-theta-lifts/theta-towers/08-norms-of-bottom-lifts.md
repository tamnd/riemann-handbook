---
title: Norms of bottom theta lifts
decls:
  - GlobalTheory.NormRatio.theta_lift_petersson_norm_eq_rallis_integral
  - GlobalTheory.NormRatio.petersson_norm_bottom_theta_lift_eq
  - GlobalTheory.NormBigProof.normBig_alt
  - GlobalTheory.T.normBig_of_lNe
  - GlobalTheory.T.bottomTheta_kernel_finiteDimensional
  - GlobalTheory.BotFormula.rallis_bottom_formula_large_rank
  - GlobalTheory.T.theta_bottom_formula_large
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Norms of bottom theta lifts

This section computes the norm of the large member of a bottom pair as a nonzero constant times a product of values of a Hecke $L$-function, and it writes the coordinates of a bottom pair as a constant times a theta integral. The main input is the Rallis inner product formula for two anisotropic Hermitian spaces. Both results go into the nonvanishing of bottom pairs, which is one of the twelve joined estimates of [Section 3.9.3](/entry/square-top-term-joined-estimates/).

We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/). For each datum $D$ we also fix a record $\mathrm{Inp}(D)$ of facts about $D$ that we have not unfolded.

**Theorem 3.8.1 (Rallis inner product formula).** Let $A$ and $B$ be Hermitian spaces over a CM extension, of ranks $a < d$, with Weil representation $\omega$, and let $\theta(\varphi)$ be the global theta lift of a Schwartz function $\varphi$ from $A$ to $B$. If the theta integrals converge absolutely, then the Petersson inner product $\langle \theta(\varphi), \theta(\varphi') \rangle$ is a value of a partial $L$-function of the character of $B$, divided by a normalizing factor, times a product of local doubling integrals of $\varphi$ and $\varphi'$.

This is the inner product formula of S. Rallis, *Injectivity properties of liftings associated to Weil representations*, Compositio Math. 52 (1984); see [the Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula). It comes from the doubling method and the Siegel-Weil formula. We state it only in this rough form, and we have not compared the Lean form below with the source.

We use it in the anisotropic case. Let $P$ be a pair of ranks $a \le d$ with a weight vector $n$, and let $X$ be a theta datum for $P$ with Hermitian spaces $A$ of rank $a$ and $B$ of rank $d$, both with Witt index $0$. For a tuple $T$ of the pair, $X$ gives a Fock vector $\varphi_T$ and a polynomial $p_T$, the minor polynomial of $T$. Let $m(d)$ be the mass of the classes of rank $d$ at the maximal integral level, so $m(d) = \sum_h |\Gamma_h|^{-1}$.

**Theorem 3.8.2 (Norm of one bottom theta lift).** Assume the local inputs and $\mathrm{Inp}(D)$. Let $X$ be an exact theta datum for $P$, with a maximal level $K_0$ and Haar measure $\mu_0$ on the group of $B$. Let $\mathfrak m$ be a good modulus with a finite set $S$ of finite places, let $P$ be standard at $\mathfrak m$ with an offset $o$ such that $o + a \le d$ and $1 \le a < d$, and let the character $\chi_B$ be unramified off $S$. Let $\Lambda$ be the holomorphic continuation of the partial $L$-function of $\chi_B^{-1}$ away from $S$. Then for every tuple $T$,

$$\begin{aligned} \langle \theta(\varphi_T), \theta(\varphi_T) \rangle &= m(d)\, m(a)\, \frac{\prod_{k < a} \Lambda(d/2 - k)}{\Delta_S(a, d; \tfrac{d-a}{2})} \\ &\quad \cdot \langle p_T, p_T \rangle\, \ell(\mathfrak m, a, d - a)\, v(\delta, t_0, a, d). \end{aligned}$$

Here $\Delta_S$ is the normalizing factor, $\langle p_T, p_T \rangle$ is the Fock inner product of the minor polynomial, $\ell$ is a local norm and $v$ is the norm of the vacuum vector. We have not unfolded these four.

Lean: `GlobalTheory.NormRatio.theta_lift_petersson_norm_eq_rallis_integral`.

*Proof.* The theta datum gives doubling data with a Cartan decomposition and a covolume one measure. The finite data of $P$ give a self-dual lattice at each finite place off $S$, and the Fock vector $\varphi_T$ is spherical off $S$. So the data are unramified off $S$. The doubling integrand of $\varphi_T$ is integrable, since the coefficients of $\varphi_T$ are constant on a compact set. Both spaces have Witt index $0$, since their Gram matrices are definite. The Rallis inner product formula for this bottom case then writes $\langle \theta(\varphi_T), \theta(\varphi_T) \rangle$ as the product of the values $\Lambda(d/2 - k)$ for $k < a$, the normalizing factor and the local doubling integral, with the volumes of $A$ and $B$. The volumes are the masses $m(a)$ and $m(d)$. The local integral is the inner product of $\varphi_T$ with itself, which is $\langle p_T, p_T \rangle$ times the local norm and the vacuum norm. $\square$

A bottom stage $(i, j)$ of the grid has two ranks $b > b'$. Put $e_0 = \lfloor (b - b')/2 \rfloor$ and $h_0 = \lfloor (b + b')/2 \rfloor$. A bottom pair at an index $t$ is a pair $(P, P')$ of pairs of ranks $(b, b + b')$ and $(b', b + b')$, with fixed characters, standard data and a level at the ideal $\mathfrak m_t$ of the grid at $t$. The norm of $P$ is the weighted sum

$$\|P\| = \sum_h \frac{1}{|\Gamma_h|} \sum_T |P(h, T)|^2$$

over the classes $h$ of the level group of $P$ and the tuples $T$. We say that $\Lambda$ is an $L$-function of a Hecke character $\nu$ if $\Lambda$ is entire and equals $\prod_v (1 - \nu(v) Nv^{-s})^{-1}$ for $\mathrm{Re}\, s > 1$, the product over the places where $\nu$ is unramified. Let $\nu_t = \nu_H(t, i, j)$ be the character of the stage at $t$.

**Theorem 3.8.3 (Norm of a bottom pair).** Assume the local inputs, $\mathrm{Inp}(D)$ and the size record of $D$. Let $G$ be a grid over a good level character, $(P, P')$ a bottom pair at $t$ for the stage $(i, j)$, and $\Lambda$ an $L$-function of $\nu_t$. Then

$$\|P\| = N(\delta, t_0, a, d, n) \prod_{s = 1 - e_0}^{h_0} \Lambda(s),$$

where $N$ is an explicit factor: the constant $c(a, n)$ times the masses $m(d)\, m(a)$, a Fock sum $F(a, d, n)$ and the vacuum norm $v(\delta, t_0, a, d)$, divided by $\Delta(a, d; \tfrac{d-a}{2})$.

Lean: `GlobalTheory.NormRatio.petersson_norm_bottom_theta_lift_eq`.

*Proof.* The ideal $\mathfrak m_t$ is a good modulus. A dictionary gives a theta datum $X$ for $P$ with spaces of ranks $a$ and $d$, and writes $\|P\|$ as $c(a, n)$ times an index $[K : J]$ times $\sum_T \langle \theta(\varphi_T), \theta(\varphi_T) \rangle$. The character of $B$ is $\nu_t$, up to a power of its finite part, so the values of $\Lambda$ are those of the partial $L$-function of $\chi_B^{-1}$. We apply [Theorem 3.8.2](/entry/theta-lift-petersson-norm-eq-rallis-integral/) to each $T$. The ranks give $d = 2 h_0$, so the values $d/2 - k$ for $k < a$ are the integers from $1 - e_0$ to $h_0$. The index, the local norm and the two normalizing factors are linked by a lemma, and the rest is algebra. $\square$

The next result says that the constant does not depend on $t$. We use the condition $\mathrm{LNe}$ that, at large scale, for every stage and index $t$ there is an $L$-function of $\nu_t$ with no zero at the integers $s$ with $1 - e_0 \le s \le h$, where $h$ is the half rank of the stage. Here a statement holds at large scale if there is $C_{F,0}$ such that for all $\varepsilon$ and $C_F \ge C_{F,0}$ there are $C_0$ and $x_0$ such that it holds for all $C \ge C_0$, all data with size data of exponent $\varepsilon$, $x \ge x_0$ and the size record, all good level characters and all grids at the constants $(1, C_F, b)$.

**Theorem 3.8.4 (Norm of the large member).** Assume the local inputs, $\mathrm{Inp}(D)$ for all $D$, and $\mathrm{LNe}$. Then at large scale, for all $\delta$, $t_0$, $i$ and $j$ there is $A \neq 0$ such that for every $t$, every bottom pair $(P, P')$ at $t$ and every $L$-function $\Lambda$ of $\nu_t$,

$$\|P\| = A \prod_{s = 1 - e_0}^{h_0} \Lambda(s).$$

Lean: `GlobalTheory.NormBigProof.normBig_alt` (also `GlobalTheory.T.normBig_of_lNe`, a second name).

*Proof.* Take the largest thresholds of $\mathrm{LNe}$ and of two consequences of [Theorem 3.8.3](/entry/petersson-norm-bottom-theta-lift-eq/): the norm of the large member of a bottom pair is not $0$, and for bottom pairs $P$ at $t$ and $P_0$ at $t_0$ with $L$-functions $\Lambda$ and $\Lambda_0$,

$$\|P\| \prod_s \Lambda_0(s) = \|P_0\| \prod_s \Lambda(s).$$

Suppose a bottom pair $(P_0, P_0')$ exists at some index $t_0$. Let $\Lambda_0$ be the $L$-function of $\nu_{t_0}$ that $\mathrm{LNe}$ gives. Since $h_0$ is at most the half rank, $\prod_s \Lambda_0(s) \neq 0$. Put $A = \|P_0\| / \prod_s \Lambda_0(s)$; it is not $0$. The ratio formula gives the claim. If no bottom pair exists, take $A = 1$, and the claim is empty. $\square$

We turn to the coordinates. A bottom triangle $X$ at the stage $(i, j)$ is a triple of Hermitian spaces $A$, $A'$ and $W$ with theta data; it gives a theta kernel $k_s(\varphi)(g, y)$ and a theta integral $I_s(\varphi)(g)$ at each index $s$. For a tuple $T$ let $\varphi_T$ be its minor function. A point $g$ of the group of $W$ is a finite point over $h$ if its finite part is $h$; we have not unfolded this. For a bottom pair, $P(x, h, T)$ is the term of $P$ at the class $x$, and

$$P(h, T) = \sum_x |\Gamma_x|^{-1} P(x, h, T)$$

is its coordinate. Let $Q_n(s)$ be the integer of the grid at $s$.

**Lemma 3.8.5 (Kernel at the bottom).** Assume the local inputs, the agreement of theta integrals [ThetaIntegralsAgree](/step/theta-integrals-agree-def/), the [local matching](/step/local-matching-def/), $\mathrm{Inp}(D)$ for all $D$, and the small bottom condition. Then at large scale, for every Weil datum with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there is $\Omega_0 \neq 0$ with this property. For every $s$ and bottom pair $(P, P')$ at $s$ there is an algebraic number $u \neq 0$, of absolute value $1$ under every embedding into $\mathbb C_p$ for every prime $p \nmid Q_n(s)$, such that for finite points $g$ over $h$ and $y$ over $x$,

$$k_s(\varphi_T)(g, y) = \Omega_0\, u\, \overline{P(x, h, T)}.$$

Lean: `GlobalTheory.T.bottomTheta_kernel_finiteDimensional`.

*Proof.* This is [the kernel identity](/entry/bottom-theta-kernel-finite/), with the same statement. Its proof joins two facts at large scale: the theta parameters of the triangle match the pair, with a constant $\kappa \neq 0$ and the number $u$, and the weights of the pair are constant. The minors of the theta kernel of the triangle are then a constant $\Omega \neq 0$ times a conjugate jet, and $\Omega_0 = \Omega \bar\kappa$. $\square$

**Theorem 3.8.6 (Bottom formula).** Under the assumptions of the lemma, at large scale, for every Weil datum with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there is $\Omega \neq 0$ with this property. For every $s$ and bottom pair $(P, P')$ at $s$ there is an algebraic $u \neq 0$ with the same unit property, such that for every finite point $g$ over $h$ and every tuple $T$,

$$\overline{P(h, T)} = \Omega\, u\, I_s(\varphi_T)(g).$$

Lean: `GlobalTheory.BotFormula.rallis_bottom_formula_large_rank` (also `GlobalTheory.T.theta_bottom_formula_large`, a second name).

*Proof.* Take the larger thresholds of [Lemma 3.8.5](/entry/bottom-theta-kernel-finite-dimensional/) and of a class sum formula, which gives $v \neq 0$ with

$$I_s(\varphi_T)(g) = v \sum_x |\Gamma_x|^{-1} k_s(\varphi_T)(g, y_x)$$

for chosen finite points $y_x$ over the classes $x$; such points exist. Insert the lemma: $I_s(\varphi_T)(g) = v\, \Omega_0\, u\, \overline{P(h, T)}$. Put $\Omega = (v \Omega_0)^{-1}$ and replace $u$ by $u^{-1}$, which is algebraic and has the unit property, since $\lambda(u)\lambda(u^{-1}) = 1$. $\square$

**Remark 3.8.7 (Formalization).** The ratio lemma of the norm theorem, in [ThetaLiftPeterssonNormEqRallisIntegral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftPeterssonNormEqRallisIntegral.lean#L115), takes $\mathrm{LNe}$ and does not use it, and its thresholds are $0$. The norm of a bottom pair is a weighted sum of coordinates, and it is a Petersson norm only through the dictionary of the proof. The kernel lemma is named for finite dimensionality, but it states a kernel identity ([BottomThetaKernelFiniteDimensional.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomThetaKernelFiniteDimensional.lean#L55)); "large rank" in the name of the bottom formula is not a condition of it either. The small bottom condition is a hypothesis, but it is proved with no hypothesis elsewhere. The norm theorem and the norm of one bottom pair have copies with the hypothesis $\mathrm{Hypotheses}_2$ in place of the local inputs, in [NormBigOfNonvanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormBigOfNonvanishing.lean#L18) and [HeckeLFunctionBottomPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeLFunctionBottomPair.lean#L378). We have not opened the dictionary, the class sum formula or the Rallis formula for the bottom case.
