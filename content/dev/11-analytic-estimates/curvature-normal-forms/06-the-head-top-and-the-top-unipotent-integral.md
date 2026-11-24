---
title: The head top and the top unipotent integral
decls:
  - Formalism.FourierDecayAlt.P.pb_headTop_of_mkTop
  - Formalism.FourierDecayAlt.P.pb_exhPic_of_mkTop
  - Formalism.FourierDecayAlt.P.top_unipotent_integral
  - Formalism.FourierDecayAlt.P.PBM.highestUnipotentIntegral
  - Formalism.FourierDecayAlt.P.PBM.top_unipotent_integral_positive
  - Formalism.FourierDecayAlt.P.PBM.vecV_append_singleton_eq_vecV_sliceAt
  - Formalism.FourierDecayAlt.P.PBM.orbJ_mMap
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The head top and the top unipotent integral

This section proves the head formula at the top of a level tower. The head formula says that the top density of a normal form datum is the coefficient of the place at level $r + 1$, at the point that adds one last entry $(1, \zeta)$ to a local point of size $r$. The main analytic input is the top unipotent integral: the vector of a place at a point $h$ with one more entry $(1, \zeta)$ is the vector of the rank zero level, applied to the slice of the function along $h$. We prove this identity by a change of variables in the orbital integral. The head formula is then assembled from it, from the exhaustion picture and from the head weight lemma. The result is a leaf below the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/), and the old entry [the head formula from the top truncation statement](/entry/pb-head-top-of-mk-top/) records the last step.

### Places, points and vectors

Fix a parameter $P$ with rank $r$ and size $k$. A place $p$ has a level tower $T$. The base of the tower is real place data $S$ of rank $r$, with points $z, z'$ in $\mathbb{C}^{2r+k+1}$, representations $\pi, \pi'$ of two unipotent groups $U_W, U_{W'}$, Haar probability measures $\mu_W, \mu_{W'}$ on them, and a measure $\mu_N$. For $0 \le j \le r$ the tower has data $S_j$ of rank $r - j$. The top datum $S_r$ has rank $0$. The tower is normalised: at each level the measures have total mass $1$, the measure $\mu_N$ is the standard one, and $z$, $z'$, $\pi$, $\pi'$ at level $j$ are the restrictions of the base data along the level embedding $\iota$. The place also has a base frame $(\nu', m_0)$.

A local point is a finite list $a = ((n_1, \zeta_1), \dots, (n_s, \zeta_s))$ with $n_b \ge 1$ and $\zeta_b \neq 0$. Its size is $n_1 + \dots + n_s$. A local point $h$ of size $r$ gives a monomial matrix $Z_h = M(\sigma_h, d_h)$ of size $r$, with a permutation $\sigma_h$ and nonzero diagonal $d_h$. Let $T = T(z)$ and $T' = T(z')$ be the values of the hermitian form at $z$ and $z'$. Put

$$\operatorname{G}(h \cdot (1, \zeta)) = |\det Z_h|^2 \bigl(|\zeta|^2 - T T'\bigr).$$

For a function $F$ on the matrices of the base level with values in $\operatorname{Hom}(W_q, W_p)$, the vector $V_p F(a)$ at a local point $a$ of size $r + 1$ is defined as follows. If $\operatorname{G}(a) > 0$, choose $\gamma$ in the group $G_V$ with $\hat Z(\gamma)$ equal to the point matrix of $a$ and with $\gamma$ a frame for $(\nu', m_0)$. Then $V_p F(a)$ is the orbital integral

$$J(\gamma, F) = \int_{SS} \theta \, \Phi_{\gamma, F} \, d\mu_{SS},$$

where $\theta$ is a normalised cut for the radial measure at $\gamma$. If no such cut exists, or if $\operatorname{G}(a) \le 0$, the vector is $0$. The slice of $F$ along $h$ is the function $\operatorname{sl}_h F$ of rank $0$ matrices $y$ given by the partial integral $\Phi_F(\sigma_h, d_h; y)$ of $F$ along the monomial matrix of $h$. The block map $m(Z, \gamma_0)$ puts a matrix $Z$ of size $r$ and a rank $0$ matrix $\gamma_0$ into one matrix of rank $r$.

### The orbital integral on block matrices

**Theorem 1.6.1.** Let $S$ be normalised real place data of rank $r \ge 1$ whose points $z, z'$ are lifts of points $z_0, z'_0$ of rank $0$. Let $\sigma$ be a permutation of $r$ letters and $d$ a diagonal with all entries nonzero, and put $Z = M(\sigma, d)$. Let $\gamma_0 \in G_V$ have rank $0$ and assume that $\gamma = m(Z, \gamma_0)$ is relevant. Assume $\hat Z(\gamma) = M(w, d')$ for a permutation $w$ of $r + 1$ letters and a nonzero diagonal $d'$, with $w^{-1}(a) = \sigma(a)$ for $a < r$. Let $F$ be continuous on $G_V$ with bounded support. Then

$$\begin{aligned} J(\gamma, F) = \int \! &c(x_1, x_2) \\ &\Phi_F\bigl(\sigma, d;\, b(x_1)^{-1} \gamma_0\, b(x_2)\bigr) \, d(\mu_W \times \mu_{W'})(x), \end{aligned}$$

where $b$ is the middle block embedding and $c(x_1, x_2)$ is conjugation by $\pi(x_1)$ and $\pi'(x_2)$.

Lean: `Formalism.FourierDecayAlt.P.PBM.orbJ_mMap`

*Proof.* The bound on the support of $F$ and the continuity give a dominating function for the slice integrand on a set of full measure. With this bound, the outer integral lemma shows two things: the cut integrand is integrable, and its integral equals the iterated integral on the right. The matrix $\gamma$ is in $G_V$ because $\det Z \neq 0$ and $\gamma_0 \in G_V$. The hypothesis on $\hat Z(\gamma)$ and on $w$ gives an explicit normalised cut $\theta_0$ for the radial measure at $\gamma$. So a cut with an integrable integrand exists, and the definition of $J$ takes the value at a chosen cut. The radial measure at $\gamma$ is a Haar measure, so the orbital integral does not depend on the choice of the cut. We replace the chosen cut by $\theta_0$, and the outer integral lemma gives the formula. $\square$

### The vector at an extended point

**Theorem 1.6.2.** Let $S$ be normalised real place data of rank $R \ge 1$ and $S_0$ normalised data of rank $0$, with $z = \iota(z_0)$, $z' = \iota(z'_0)$, $\pi_0(y) = \pi(\iota y)$ and $\pi'_0(y) = \pi'(\iota y)$. Let $(\nu', m_0)$ be a base frame for $S$ and $(\nu'_0, m_{0,0})$ a base frame for $S_0$ with $\nu' = \iota(\nu'_0)$ and $m_0 = \iota(m_{0,0})$. Let $h$ be a local point of size $R$, let $\zeta \neq 0$, and let $F$ have compact coefficients. Then

$$V_S F\bigl(h \cdot (1, \zeta)\bigr) = V_{S_0}(\operatorname{sl}_h F)\bigl((1, \zeta)\bigr).$$

Lean: `Formalism.FourierDecayAlt.P.PBM.vecV_append_singleton_eq_vecV_sliceAt`

*Proof.* The hermitian form is the same on a vector and on its lift, so $T(z) = T(z_0)$ and $T(z') = T(z'_0)$. The point matrix of $h \cdot (1, \zeta)$ is the block matrix of $Z_h$ and the $1 \times 1$ matrix $\zeta$, so its determinant is $\zeta \det Z_h$. This gives the formula for $\operatorname{G}$ above, and $|\det Z_h|^2 > 0$ because $Z_h$ is monomial with a nonzero diagonal.

Case $|\zeta|^2 \le T T'$. Then $\operatorname{G}(h \cdot (1, \zeta)) \le 0$, so the left side is $0$. At rank $0$ the point $(1, \zeta)$ is degenerate for the same reason, so the right side is also $0$.

Case $|\zeta|^2 > T T'$. At rank $0$ there is a frame $\gamma_0 \in G_V$ with $\hat Z(\gamma_0) = \zeta$. The vector at rank $0$ is then the Jacquet integral

$$\int c(y_1, y_2)\, \operatorname{sl}_h F(y_1^{-1} \gamma_0 y_2) \, d(\mu^0_W \times \mu^0_{W'})(y).$$

Put $\gamma = m(Z_h, \gamma_0)$. The slice membership lemma gives $\gamma \in G_V$. The point lemma for block matrices gives $\hat Z(\gamma)$ equal to the point matrix of $h \cdot (1, \zeta)$. The frame lemma for block matrices shows that $\gamma$ is a frame for $(\nu', m_0)$, since $\gamma_0$ is a frame for $(\nu'_0, m_{0,0})$. With $\operatorname{G} > 0$ the vector on the left is the orbital integral $J(\gamma, F)$ for the radial measure of the point permutation, and $\gamma$ is relevant. The compact coefficient condition gives continuity of $F$ on $G_V$ and a bound on its support. So the previous theorem applies with $\sigma = \sigma_h$, $d = d_h$, and the permutation of the extended point satisfies the compatibility with $\sigma_h$. The left side becomes an integral over $\mu_W \times \mu_{W'}$.

Now we change variables. Both Haar measures at rank $R$ have mass $1$, and both measures at rank $0$ have mass $1$. Hence $\mu_W$ is the image of $\mu^0_W$ under the level embedding, and the same holds for $\mu_{W'}$. See [Haar measure](/learn/analysis/#haar-measure). The embedding is a closed embedding, so the integral over the image measure is the integral of the composed function. For almost every pair $(y_1, y_2)$ both entries lie in the unipotent sets, so $\det y_2$ is a unit and $\iota(y_2^{-1}) = \iota(y_2)^{-1}$. The middle block embedding commutes with $\iota$, and $\pi(\iota y_1) = \pi_0(y_1)$, $\pi'(\iota y_2^{-1}) = \pi'_0(y_2^{-1})$. So the two integrands agree almost everywhere once the partial integral along $h$ is written as the slice. The last step unfolds the slice: the size of $h$ is $R$, so the rank of the slice is $R - R = 0$, and the casts between ranks are trivial. $\square$

**Theorem 1.6.3.** Let $p$ be a place with $r \ge 1$, $F$ a function with compact coefficients, $h$ a local point of size $r$ and $\zeta \neq 0$. Let $(\nu'_r, m_{0,r})$ be a frame at the top level whose lifts are $\nu'$ and $m_0$. Then

$$V_p F\bigl(h \cdot (1, \zeta)\bigr) = V_{S_r}(\operatorname{sl}_h F)\bigl((1, \zeta)\bigr).$$

Lean: `Formalism.FourierDecayAlt.P.PBM.top_unipotent_integral_positive`

*Proof.* Apply the previous theorem with $S$ the base of the tower and $S_0 = S_r$. The normalisation of the tower at level $0$ and at level $r$ gives the conditions on the measures. The level conditions of the tower give the lifts of $z$, $z'$, $\pi$, $\pi'$. The base frame of the place gives the frame for $S$, and the frame at the top level is a base frame for $S_r$ because its lifts are the base frame. $\square$

**Theorem 1.6.4.** The identity of the previous theorem holds for every place, with no condition on $r$.

Lean: `Formalism.FourierDecayAlt.P.PBM.highestUnipotentIntegral`

*Proof.* If $r \ge 1$, use the previous theorem. If $r = 0$, a local point of size $0$ is empty, so $h \cdot (1, \zeta) = (1, \zeta)$. The top level of the tower is the base, and the slice along the empty point is $F$ itself up to the cast. The rank zero lemma checks that the two vectors agree. $\square$

**Theorem 1.6.5.** The top unipotent integral holds.

Lean: `Formalism.FourierDecayAlt.P.top_unipotent_integral`

*Proof.* This is the previous theorem. $\square$

### The exhaustion picture and the head formula

The top truncation statement asks, for each place, for smooth cutoffs $b, b'$ with compact support, a smooth weight $\beta$ on the invertible matrices and a nonzero constant $\kappa$. These must satisfy a compactness condition under right translation by upper unipotent matrices. For every function $\Phi$ with the equivariance of the top level, the pullback through these cutoffs must also be equivariant, and so on. The exhaustion picture says the following. For each letter $e$ of a cut word $w$ and each local point $h$ of size $r$, there are two functions $F_1, F_2$ with compact coefficients such that:

1. the vectors of $\Theta_w^e F$ and $\Theta_w^e F_1$ agree at $h \cdot (1, \zeta)$ for all $\zeta$;
2. the word operator at the start of the base datum carries the first state of a radial form of $F_1$ to a radial form of $F_2$;
3. at every $\gamma$ with $\operatorname{GGl}(\gamma) > 0$ the Jacquet function of the slice $\operatorname{sl}_h F_2$ equals the word operator of the top datum, applied to a radial form of the slices of $F$.

**Theorem 1.6.6.** If the top truncation statement holds, then the exhaustion picture holds.

Lean: `Formalism.FourierDecayAlt.P.pb_exhPic_of_mkTop`

*Proof.* The exhaustion picture follows from a general lemma whose inputs are the exceptional implication, the top truncation statement and seventeen facts about the top level. The facts are the unipotent weight at the top, the slice exhaustion, the smoothness, right action, support and equivalence of the pullback, the compact truncation, the existence of a top point, the determinant at exceptional points, the exhaustion of head families, the radial slice at the top, the radial function and the radial extension at exceptional points, the residue at the top level, the regularity of the frame parameter, and the head and level zero pictures. The exceptional implication is proved, and each fact is proved elsewhere in the formalization, so the exhaustion picture holds once the top truncation statement holds. $\square$

The head formula says the following. Let $p$ be a place, $F$ a function with compact coefficients, $w$ a cut word and $h, h'$ local points of size $r$. Let $(X, \mu, L, \mathrm{st})$ be a normal form datum at the top level, and let $\Phi, \Phi'$ be radial forms of the slices of $F$ along $w$ at $h$ and at $h'$. Then for every $x$ in the radial domain, with $\zeta = \zeta_L(x)$,

$$\operatorname{dens}_{L, \mathrm{st}}(w; \Phi, \Phi')(x) = R_p F\bigl(r + 1;\, h \cdot (1, \zeta),\, h' \cdot (1, \zeta)\bigr).$$

Here $\operatorname{dens}$ is the top density and $R_p F$ is the coefficient of the place.

**Theorem 1.6.7.** If the top truncation statement holds, then the head formula holds.

Lean: `Formalism.FourierDecayAlt.P.pb_headTop_of_mkTop`

*Proof.* By the previous theorem the exhaustion picture holds. The exhaustion picture implies the exhaustion statement. For this, take $F_1$ and $F_2$ from the picture. The compact support lemma for $\Theta$ replaces $\Theta_w^e F_1$ by a function $F'$ with compact coefficients that agrees with it on the relevant points and has the same vectors. The radial form of $F_1$ exists, and the top lift of the place carries it to a radial form of $F'$. Two functions whose radial forms are related by the word operator have equal vectors, because the density is constant. With item 1 this shows that the vectors of $\Theta_w^e F$ at $h \cdot (1, \zeta)$ are the vectors of $F_2$, and item 3 is kept. The head formula then follows from three inputs: the top unipotent integral, the exhaustion statement and the head weight lemma. The top unipotent integral turns the vectors of $F_2$ at $h \cdot (1, \zeta)$ into rank zero vectors of the slice. The head weight lemma identifies the top density with the coefficient at level $r + 1$. $\square$

**Remark 1.6.8 (Formalization).** The statement of the top unipotent integral at `HermitianCurvatureProofs/PolynomialHeadTypes.lean:9` writes the rank of the top level as `P.r - P.r`, which is always $0$ (line 13). The general lemma at `HermitianCurvatureProofs/VecVAppendSingletonEqVecVSliceAt.lean:63` takes a rank $\rho$ with the hypothesis $\rho = 0$ and substitutes it on the first line of the proof. It also asks for $R \ge 1$, because the block integral `orbJ_mMap` at `HermitianCurvatureProofs/OuterInt.lean:88` needs it for its dominating bound. So the case $r = 0$ has a separate proof at `HermitianCurvatureProofs/TopUnipotentIntegralRankZero.lean:18`. The general lemma runs with `maxHeartbeats 1000000` (line 61). `top_unipotent_integral` at `HermitianCurvatureProofs/TopUnipotentIntegralPositive.lean:38` is only an alias of `PBM.highestUnipotentIntegral`. The orbital integral in `HermitianCurvature/StatementD.lean:82` picks its cut by choice, so `orbJ_mMap` must prove independence of the cut (`OuterInt.lean:111`) before it can use the explicit cut. In `HermitianCurvatureProofs/PbHeadTopOfMkTop.lean:20` the first argument is `CutEX.exceptional_assumption_holds`, which is a theorem despite its name (`HermitianCurvatureProofs/CutEXAsm.lean:119`). The top truncation statement `CutEX.MkTop` is at `HermitianCurvatureProofs/CutEX2.lean:93` and the head formula `KB.HeadTop` at `HermitianCurvature/RealInputsClosedAdmissibleSettings.lean:228`.
