---
title: Small members, matching of minors and the bottom constant
decls:
  - GlobalTheory.T.theta_bottom_formula_small
  - GlobalTheory.BotFormula.rallis_bottom_formula_small_rank
  - GlobalTheory.T.smallStage_bottomKernel_eq_term
  - GlobalTheory.BotSmallDict.bottomKernel_eq_classSum_term
  - GlobalTheory.T.rallis_bottom_minor_matching
  - GlobalTheory.BotMatch.theta_bottom_minor_match
  - GlobalTheory.T.bottom_degree_match_real_quotient
  - GlobalTheory.BotMatch.real_quotient_complement_minor
  - GlobalTheory.T.botConst_of_theta_matching
  - GlobalTheory.SqTop.botConst_of_inputs_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Small members, matching of minors and the bottom constant

Section 8 wrote the coordinates of the large member $P$ of a bottom pair as a constant times a theta integral. This section does the same for the small member $P'$, with the second space $A'$ of the bottom triangle in place of $A$. Then it compares the two theta integrals of a triangle: a minor of the first is a constant times an integer combination of minors of the second. Together these facts give the bottom constant: a bound on the valuations of the ratio of the constants of a bottom triangle at two indices. This is one of the twelve joined estimates of [Section 3.9.3](/entry/square-top-term-joined-estimates/).

We keep the notation of Sections 8 and 10, the local inputs, [ThetaIntegralsAgree](/step/theta-integrals-agree-def/), the [local matching](/step/local-matching-def/), $\mathrm{Inp}(D)$ for all $D$ and the small bottom condition. For the small member, $k'_s(\varphi)(g, g')$ is the theta kernel of $A'$ and $W$, and $I'_s(\varphi)(g)$ its theta integral. The unit property at $s$ is that of Section 10.

**Lemma 3.11.1 (Kernel of the small member).** At large scale, for every Weil datum with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there is $\Omega_2 \neq 0$ with this property. For every $s$ and bottom pair $(P, P')$ at $s$ there is $u$ with the unit property at $s$ such that for finite points $g$ over $h$ and $g'$ over $x$ and every tuple $T'$,

$$k'_s(\varphi_{T'})(g, g') = \Omega_2\, u\, P'(x, h, T').$$

Lean: `GlobalTheory.BotSmallDict.bottomKernel_eq_classSum_term` (also `GlobalTheory.T.smallStage_bottomKernel_eq_term`, a second name).

*Proof.* The thresholds can be $0$. If there is no bottom pair at $(\delta, t_0)$, take $\Omega_2 = 1$; the claim is empty. Otherwise fix a bottom pair $(P_0, P_0')$ at some $s_0$. The characters of $X$ on $A'$ and $W$ are trivial at the real places, so the vacuum of $X$ on these spaces is a standard vacuum. The record $\mathrm{Inp}(D)$ gives a constant $\kappa \neq 0$ of the vacuum. Put

$$\Omega_2 = \kappa \prod_\tau \varpi_\tau^{\,a\, n_\tau},$$

where $\varpi_\tau$ is the period of the lattice at $\tau$, $a$ the rank of $P_0'$ and $n_\tau$ its weights. The periods are not $0$, so $\Omega_2 \neq 0$. For a bottom pair at $s$, the vacuum gives a phase $\zeta$ for the vector of $P'$, and the reading of the datum gives a second unit $\zeta'$. Put $u = \zeta \zeta'$. A kernel formula writes $k'_s(\varphi_{T'})(g, g')$ through these numbers and the period of $P'$. The ranks and weights of $P'$ are those of $P_0'$, since all bottom pairs at a stage have the same real data. $\square$

**Theorem 3.11.2 (Bottom formula for the small member).** At large scale, for every Weil datum with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there is $\Omega' \neq 0$ with this property. For every $s$ and bottom pair $(P, P')$ at $s$ there is $u$ with the unit property at $s$ such that for every finite point $g$ over $h$ and every tuple $T'$,

$$I'_s(\varphi_{T'})(g) = \Omega'\, u\, P'(h, T').$$

Lean: `GlobalTheory.BotFormula.rallis_bottom_formula_small_rank` (also `GlobalTheory.T.theta_bottom_formula_small`, a second name).

*Proof.* Take the larger thresholds of a class sum formula for the small stage and of [Lemma 3.11.1](/entry/bottom-kernel-eq-class-sum-term/). The class sum formula gives $\Omega_1 \neq 0$ with

$$I'_s(\varphi_{T'})(g) = \Omega_1 \sum_x |\Gamma_x|^{-1} k'_s(\varphi_{T'})(g, g'_x)$$

for finite points $g'_x$ over the classes $x$; such points exist, since each class has a point of Gram determinant $1$. Insert the lemma in each term. The sum is then $\Omega_2 u P'(h, T')$, and $\Omega' = \Omega_1 \Omega_2$. $\square$

We now compare the minors of the two spaces. For a tuple $T$ of row subsets, $T^c$ is the tuple of complements; the map $T \mapsto T^c$ is a bijection between the tuples of $A$ and of $A'$, since the ranks add up to the rank of $W$.

**Lemma 3.11.3 (Minors at the real places).** Assume Howe duality at the real places, the local inputs, the agreement of theta integrals and the local matching. Let $A$, $A'$ and $W$ be positive definite at every real place, with $\mathrm{rank}\, A + \mathrm{rank}\, A' = \mathrm{rank}\, W$, and let there be Hecke characters $\alpha$, $\beta$ that form a triple with $A$, $A'$ and $W$, with exponents $a$ and $b$ at the real places. Let $q$ and $q'$ be surjective linear maps from the polynomial Fock spaces of $(W, A)$ and $(W, A')$ onto one space $\Pr$, such that each match of the triple factors through $q$ and $q'$ and a finite part. Then there is $\rho \neq 0$ such that for every tuple $T$ there is a sign $\epsilon_T = \pm 1$ with

$$q(\varphi_T) = \rho\, \epsilon_T\, q'(\varphi_{T^c}).$$

Lean: `GlobalTheory.BotMatch.real_quotient_complement_minor` (also `GlobalTheory.T.bottom_degree_match_real_quotient`, a second name).

*Proof.* An equivalence of the real quotient with the bottom invariants identifies $\Pr$ with a line on which the minors of degree $n$ act through determinants. A lemma on this line says that each minor is a fixed constant times a signed complementary minor. The sign comes from the permutation that joins the rows of $T$ and $T^c$. $\square$

**Theorem 3.11.4 (Matching of minors).** At large scale, for every Weil datum with a standard character and every bottom triangle $X$ at $(i, j)$ with constants $c_0$ (the property $\mathrm{IsConst}$ of Section 8), there is $\kappa_0 \neq 0$ with this property. For all $s$, $Q$, $\delta$, $t_0$ and bottom pairs $(P, P')$ at $s$ whose ranks agree with those of $X$, there are integer matrices $M$ and $M'$ with $M' M = 1$ such that for all $g$ and $T$,

$$I_s(\varphi_T)(g) = \kappa_0\, c_0(s) \sum_{T'} M(T, T')\, I'_s(\varphi_{T'})(g).$$

Lean: `GlobalTheory.BotMatch.theta_bottom_minor_match` (also `GlobalTheory.T.rallis_bottom_minor_matching`, a second name).

*Proof.* Howe duality at the real places is part of the local inputs. The local factors of the twisted triangles match, and their theta integrals agree. Take the larger thresholds of the dictionary of definite bottoms (frames, exponents and the kernel) and of the matching at the finite places. The dictionary makes $A$, $A'$ and $W$ definite and gives a triple; [Lemma 3.11.3](/entry/real-quotient-complement-minor/) then gives $\rho$ and the signs. The matching at the finite places gives a constant $\kappa \neq 0$ and the maps $q$, $q'$. The key step is this. Since $X$ has constants $c_0$, the integral $I'_t$ vanishes on the kernel of $q'$, and on the quotient it is either $0$ or injective; so with $\lambda_t = c_0(t) / \kappa$,

$$I_t(\varphi) = \lambda_t\, J_t(q\, \varphi), \qquad I'_t(\varphi') = J_t(q'\, \varphi')$$

for one map $J_t$. Put $\kappa_0 = \rho / \kappa$. The weights of the square bottom pairs agree, so $T \mapsto T^c$ lands in the tuples of $P'$. Take $M(T, T') = \epsilon_T$ if $T' = T^c$ and $0$ otherwise, and $M'$ the inverse signed permutation. $\square$

The bottom constant is the following statement at large scale. Take a bottom triangle $X$ with constants $c_0$, a bottom pair $(P_0, P_0')$ at $\mu_0$ with level $\mathrm{lev}$, a bottom pair $(P, P')$ at $t$ with level $\mathrm{lev} \cdot Q_n(t)$, and nonzero $z$, $z'$ in a number field $L$ whose images are $\|P\|$ and $\|P_0'\|$. Let the grid have integral exponents $d_l$. Then there is $\gamma \in L$, $\gamma \neq 0$, with $c_0(\mu_0) \neq 0$ and $\gamma\, c_0(\mu_0) = c_0(t)$ under the embedding, such that for every place $w$ of $L$ that does not contain $Q_n(t)$,

$$v_w(\gamma) \le v_w(z) + v_w(z') + 6\, d_l(w).$$

**Theorem 3.11.5 (Bottom constant).** Assume the local inputs, the agreement of theta integrals, the local matching, $\mathrm{Inp}(D)$ for all $D$, the small bottom condition and $\mathrm{LNe}$. Then the bottom constant holds.

Lean: `GlobalTheory.SqTop.botConst_of_inputs_alt` (also `GlobalTheory.T.botConst_of_theta_matching`, a second name).

*Proof.* Take the largest thresholds of three facts: the ratio of bottom constants is a ratio of local factors, a Rallis formula at the first occurrence, and the small bottom condition. The first gives $c_0(t) \neq 0$, $c_0(\mu_0) \neq 0$ and $\gamma$ with $\gamma\, c_0(\mu_0) = c_0(t)$; so $\gamma \neq 0$. The second gives $\kappa \neq 0$, and for the pairs at $t$ and at $\mu_0$ units $u_1$, $u_2$ and integer matrices that relate the coordinates of the large member to those of the small member, with the constants $\kappa u_1 c_0(t)$ and $\kappa u_2 c_0(\mu_0)$. Fix a place $w$ that does not contain $Q_n(t)$, and take a prime $p$ under $w$. Then $p \nmid Q_n(t)$, and $p \nmid Q_n(\mu_0) = 1$ at the base tuple. So $u_1 / u_2$ is algebraic and of absolute value $1$ under every embedding into $\mathbb C_p$, and the $p$-adic valuation of the level $\mathrm{lev} \cdot Q_n(t)$ is that of $\mathrm{lev}$. A valuation bound for the proportionality ratio of two bottom pairs, from $\mathrm{Inp}(D)$, gives the inequality for the ratio $(u_1 c_0(t)) / (u_2 c_0(\mu_0))$. Since this ratio is $(u_1/u_2)\, \gamma$ under the embedding, the claim follows. $\square$

**Remark 3.11.6 (Formalization).** The matching of minors ([RallisBottomMinorMatching.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RallisBottomMinorMatching.lean#L27)) takes $\mathrm{Inp}(D)$ and the small bottom condition and uses neither. The kernel of the small member ([SmallStageBottomKernelEqTerm.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SmallStageBottomKernelEqTerm.lean#L34)) has thresholds $0$ and uses only $\mathrm{Inp}(D)$ and the size record; the other four hypotheses are unused, and with no bottom pair the claim is empty. The names with "Rallis" in [RallisBottomFormulaSmallRank.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RallisBottomFormulaSmallRank.lean#L18) and the matching file do not refer to an inner product formula in the statement, and "degree match" in [BottomDegreeMatchRealQuotient.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomDegreeMatchRealQuotient.lean#L18) refers to the minors of degree $n$; the lemma takes Howe duality at the real places as a separate hypothesis although it is a field of the local inputs. The bottom constant is in [BottomConstantOfTheta.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomConstantOfTheta.lean#L22), and its statement is defined in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L139). We have not opened the class sum formula, the dictionary of definite bottoms, the finite place matching, the ratio of local factors, the Rallis formula at the first occurrence or the valuation bound.
