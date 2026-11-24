---
title: The real branch and the bottom period
decls:
  - UpperTheory.Lit.Branch.realInputE
  - UpperTheory.Lit.Branch.locOK_of_eigen
  - UpperTheory.Lit.Branch.packEx_of_eigen
  - UpperTheory.Lit.Branch.periodNe_of_eigen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The real branch and the bottom period

This section completes the proof that the bottom period of the theta tower does not vanish. The [cusp form period theorem](/entry/exists-cusp-form-theta-period-ne-zero/) of the previous section needs packs: local data at each real place that control an integral of matrix coefficients over the smaller unitary group. This section produces packs from one statement about the branching of discrete series from $\mathrm{U}(n+1)$ to $\mathrm{U}(n)$, the *real branching input*. It then joins the result with the cusp form theorem and a short transfer lemma. The real branching input itself is the [real input for separation](/entry/real-input-e-holds/), and the final theorem is what [real functionals separate](/entry/real-functionals-separate-of-hypothesis/) uses.

### The real branching input

Fix $n \geq 0$, an embedding $e$ of $\mathrm{U}(J_{\varepsilon'})$ into $\mathrm{U}(J_\varepsilon)$ as the stabilizer of a vector, where $\varepsilon$ and $\varepsilon'$ are signatures of ranks $n+1$ and $n$, and a bound $B$. A *branching pair* is a pair $(\pi, \sigma)$ of discrete series of $\mathrm{U}(J_\varepsilon)$ and $\mathrm{U}(J_{\varepsilon'})$ whose Harish-Chandra parameters $\lambda$ and $\mu$ interlace, with gaps at least $2$, gaps at least $1000(n+1)^3$ between entries of opposite signs, and entries of size at most $B$. All integrals over $h$ are over $\mathrm{U}(J_{\varepsilon'})$ with its fixed Haar measure $dh$, and we write $\pi(h)$ for $\pi(e(h))$. Let $\beta(C, n, B)$ be the explicit size function of the separation chapter, and $|g e_0|$ the length of the column of $g$ at the extra basis vector.

**Definition 1.18.1 (Real branching input).** The *real branching input* holds if there is $C > 0$ such that for each branching pair there are a unit vector $v_0$ in the lowest $K$-type of $\pi$, a point $g_0 \in \mathrm{U}(J_\varepsilon)$, a smooth unit vector $w'$ of $\sigma$ and $c > 0$ such that, for $v = \pi(g_0) v_0$, the vector $v$ is smooth and:

1. for every $b$,
$$\int \overline{\langle v, \pi(h) v\rangle}\, \langle b, \sigma(h) w'\rangle\, dh = c\, \langle b, w'\rangle;$$
2. for every $g$ the function $h \mapsto \langle v, \pi(g h) v \rangle$ is integrable and
$$\int |\langle v, \pi(g h) v \rangle|\, dh \leq c\, \beta(C, n, B)\, |g e_0|^{-(2n+7)};$$
3. for $X$ in the Lie algebra of $\mathrm{U}(J_{\varepsilon'})$ of Hilbert-Schmidt norm at most $1$, the same integral with $d\pi(X) v$ in the first slot and $g = 1$ is at most $c\, \beta(C, n, B)$;
4. there is $A$ with $|\langle v, \pi(g) v\rangle| \leq A\, |g|^{-20(n+1)^2}$ for all $g$.

Item 1 says that $w'$ is an eigenvector, with eigenvalue $c$, of the operator on $\sigma$ given by integration against the coefficient of $v$. Items 2 to 4 are bounds with an explicit dependence on $B$.

Two statements on a single branching pair reduce the input to representation theory. An *embedding* of $\sigma$ in $\pi$ is a $\mathrm{U}(J_{\varepsilon'})$-map $j$ from $\sigma$ to $\pi$ that preserves norms, with adjoint $P$.

**Definition 1.18.2 (Large projection).** The *large projection* statement holds if for each branching pair and each unit vector $v_0$ in the lowest $K$-type of $\pi$ there are an embedding $j$ with adjoint $P$ and a point $g_0$ with
$$|g_0| \leq \big(8(n+1)B\big)^{10(n+1)}, \qquad 1 \leq \beta(100, n, B)\, |P \pi(g_0) v_0|.$$

**Definition 1.18.3 (Eigenvector map).** The *eigenvector map* statement holds if for each branching pair, with $d$ the formal degree of $\sigma$, each embedding $j$ with adjoint $P$ and each $v$ with integrable coefficient on $\mathrm{U}(J_{\varepsilon'})$ and $Pv \neq 0$, there are $w \neq 0$, $c$ and a $\mathrm{U}(J_{\varepsilon'})$-map $T$ from $\pi$ to $\sigma$ with $Tv = w$,
$$c \geq \frac{|Pv|^2}{2d},$$
and with $w$ an eigenvector of eigenvalue $c$ as in item 1.

**Theorem 1.18.4 (The real branching input).** If the large projection and the eigenvector map statements hold, the real branching input holds.

Lean: `UpperTheory.Lit.Branch.realInputE`.

*Proof.* Take $v_0$ in the lowest $K$-type of $\pi$. The large projection statement gives $j$, $P$ and $g_0$. Put $v = \pi(g_0) v_0$. Then $v$ is smooth, since $v_0$ is $K$-finite and so smooth. The coefficient of $v$ is integrable on $\mathrm{U}(J_{\varepsilon'})$ by the bound of item 2, which we prove first, and $Pv \neq 0$ since $\beta(100, n, B)|Pv| \geq 1$.

For the bounds, the coefficient $\langle v, \pi(g) v\rangle$ is the coefficient of $v_0$ at $g_0^{-1} g g_0$. The coefficients of a lowest $K$-type vector decay with an explicit power of $|g|$, and the norm laws of the stabilizer embedding control $|g_0^{-1} g g_0|$ in terms of $|g|$ and the bound on $|g_0|$. Integration of a negative power of the norm over balls, with the bound on the volume of balls, gives item 2 with a constant $C_1$ in place of $c\,\beta$, and the same argument with the bound for Lie words in the lowest $K$-type gives item 3 with a constant $C_3$. Item 4 is the pointwise decay.

The eigenvector map statement gives $w \neq 0$, $c$ and $T$. Put $w' = w/|w|$. Item 1 for $w$ is linear in $w$, so it holds for $w'$ with the same $c$. The map $T$ sends smooth vectors to smooth vectors, so $w' = T(v)/|w|$ is smooth. Next, $c > 0$: we have $c \geq |Pv|^2/(2d)$ and $|Pv| \geq \beta(100,n,B)^{-1}$. It remains to put the constants $C_1$ and $C_3$ in the form $c\,\beta(C, n, B)$. The volume of a small ball in $\mathrm{U}(J_{\varepsilon'})$ is at most $\beta(C_2, n, B)/d$, and the ratio of formal degrees is bounded. Together with $1/c \leq 2d\,\beta(100, n, B)^2$ this gives
$$C_1 + C_3 \leq c\, \beta(C, n, B), \qquad C = C_1 + C_3 + C_2 + 201,$$
by the arithmetic of the size function. $\square$

### Packs from the real input

Return to the tower. At the bottom, $Y_0$ has rank $r$ and $V_0$ has rank $r+1$, and $Y_0$ embeds into $V_0$ as the orthogonal complement of a vector. A *local datum* at a real place $\tau$ for models $M_0$ of $\mathrm U(Y_0)$ and $M_P$ of $\mathrm U(V_0)$ and a loss $q$ is a list $(A, B, v_0, g_0, w, c)$ with these properties: $A$ and $B$ are frames that bring the Gram matrices of $Y_0$ and $V_0$ at $\tau$ to signature form and are adapted to the embedding, $g_0$ is a real point, $v_0$ is $K$-finite with decay of order $2(r+1)^2+1$, $w \neq 0$ is smooth, $c \neq 0$, the integral of the coefficient of $\sigma(g_0)v_0$ against the coefficient of $w$ is $c\langle b, w\rangle$, and the far and Lipschitz bounds hold with $e^q|c|$.

**Lemma 1.18.5 (Local data from the real input).** If the real branching input holds, there is $C \geq 0$ such that for large data, all models $M_0$ and $M_P$ and every real place $\tau$ there is a local datum at $\tau$ with loss $6C(r+1)^4 \log b$, where $b$ is the size parameter of the data.

Lean: `UpperTheory.Lit.Branch.locOK_of_eigen`.

*Proof.* Transport the real branching input to the ranks of the tower: for $n = r$ it gives the constant $C$. For large data, the grid parameters satisfy the branching hypotheses: the Harish-Chandra parameters of the discrete series of $M_0$ and $M_P$ at $\tau$ interlace with the required gaps, and their size is at most $B$ with $\log \beta(C, r, B) \leq 6C(r+1)^4 \log b$. Choose frames $A$ and $B$ that extend a signature matrix of $Y_0$ to one of $V_0$. In these frames, the Haar measure of $\mathrm U(Y_0)$ at $\tau$ is a positive multiple of the fixed Haar measure, and the models are conjugate to the standard discrete series with these parameters. Apply the real input to the conjugate pair. Item 1 gives the action clause, with $c$ multiplied by the positive constant of the Haar measures. Items 2 and 4 give the far bound and the decay of order $2(r+1)^2+1$ in the frame, and item 3 gives the Lipschitz bound at the real place. $\square$

**Theorem 1.18.6 (Packs exist).** If the real branching input holds, packs exist, with constant $6C$.

Lean: `UpperTheory.Lit.Branch.packEx_of_eigen`.

*Proof.* Take $C$ from the lemma. For large data and models $M_0$ and $M_P$, choose a local datum at each real place. The local data at all places together give one pack whose vectors are the tensor products of the local vectors and whose loss is the sum of the local losses. This sum is
$$|\mathrm{Tau}| \cdot 6C(r+1)^4 \log b = \mathrm{loss}(6C),$$
the loss in the definition of packs. $\square$

### The bottom period

**Theorem 1.18.7 (The bottom period is not zero).** Assume the theorems on Harish-Chandra modules, Casselman-Wallach and rapid decay, and the real branching input. Then for large data the following holds. Let $M_0$ and $M_P$ be models, $t \in \mathrm{Rows}(M_0)$ nonzero and $w \neq 0$ a smooth vector of $M_0$. Then there are $y \in \mathrm{Core}(M_P)$ and $v$ in the span of pure tensors of $K$-finite vectors of $M_P$ with
$$P_0\big(y(v), t(w)\big) \neq 0.$$

Lean: `UpperTheory.Lit.Branch.periodNe_of_eigen`.

*Proof.* By the theorem on packs, packs exist. Depth pays for every loss, by the theorem on the depth of the grid that this chapter cites. So the [cusp form period theorem](/entry/exists-cusp-form-theta-period-ne-zero/) applies: for large data and each nonzero $t$ there are $y \in \mathrm{Core}(M_P)$ and $v', w'$ with $P_0(y(v'), t(w')) \neq 0$. Fix such data and take $w \neq 0$.

1. Move to $w$. If the integral of $y(v') \circ \iota_0$ against every real translate of $t(w)$ were $0$, then, since the real translates of $w$ span a dense subspace of the irreducible representation $M_0$ and $t$ intertwines, the integral against $t(w')$ would be $0$ too. So there is a real point $h$ with nonzero integral against $t(w)$ translated by $h$.
2. Move the translate to the core side. The period is invariant under the real group of $Y_0$ acting on both sides, so translating $t(w)$ by $h$ is the same as translating $y(v')$ by $\iota_0(h)^{-1}$, and this is $y(v'')$ for a new smooth vector $v''$. So $P_0(y(v''), t(w)) \neq 0$.
3. Move to a $K$-finite vector. By the lemma on $K$-finite values, which uses rapid decay and the theorem on Harish-Chandra modules, if the map $a \mapsto P_0(y(a), t(w))$ vanished on all pure tensors of $K$-finite vectors, it would vanish at $v''$. So there is $v$ in their span with $P_0(y(v), t(w)) \neq 0$. $\square$

**Remark 1.18.8.** The input is a quantitative form of a branching statement for discrete series from $\mathrm{U}(n+1)$ to $\mathrm{U}(n)$. In the large projection statement, $\sigma$ occurs as a closed subrepresentation of the restriction of $\pi$, through $j$, and the integral of item 1 is the projection onto this copy of $\sigma$, written through matrix coefficients. The factor $1/d$ in the eigenvector map statement comes from the Schur orthogonality relation $\int |\langle w, \sigma(h) w\rangle|^2\, dh = |w|^4/d$ for the discrete series. For compact unitary groups the interlacing condition on the parameters is the classical branching rule from $\mathrm{U}(n+1)$ to $\mathrm{U}(n)$; see H. Weyl, *The classical groups* (1939).

**Remark 1.18.9 (Formalization).** The results are in RealBands: `realInputE` ([BranchInput.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/RealBands/BranchInput.lean#L41)), `locOK_of_eigen` and `packEx_of_eigen` (BranchPack.lean, lines 107 and 205), and `periodNe_of_eigen` (BranchPeriod.lean, line 14). The definitions `RealInputE`, `ProjLarge` and `EigMap` are in BranchDefs.lean (lines 11, 26 and 30). In `RealInputE` the action clause carries a factor $\langle w', w'\rangle$, which is $1$ since $|w'| = 1$. The proof of `realInputE` uses `translateCoefficientIntegralBounds_of_unitary_laws`, `translateCoefficientDerivativeIntegralBounds_of_laws`, `volDeg`, `mapSmooth` and `formalDegree_loweringWeight_ratio_le`, and inside it there is a `first | exact Real.rpow_nonneg ... | exact zpow_nonneg ... | positivity`. The lemma `realInputE_transport` (BranchPack.lean, line 18) only rewrites casts. The local datum is the structure `LocOK` (Adapted.lean, line 29); its action clause uses the coefficient `mco` without complex conjugation, so the proof of `locOK_of_eigen` passes to the conjugate model `conjModel`. The pack is assembled from the local data by `realVectors_allPlaces_of_localData`, which this chapter cites. In `periodNe_of_eigen` the depth hypothesis is `GlobalTheory.T.gridDepth_pays_every_loss` (GridDepthPaysEveryLossStatement.lean, line 11), a `first | exact` wrapper over three ways of applying `depth_pays`, and the three steps of the transfer are `GlobalTheory.PeriodNePf.exists_kf` (PeriodNonvanishingOfArchimedeanInputs.lean, line 65), which uses `integral_eq_zero_of_orthogonal_real_translates`, `real_translate` and `period_eq_zero_of_vanishing_on_kFinite_values`; our account of these three lemmas gives their statements, not their proofs. The hypothesis `CasselmanWallach` is passed only to `exists_cusp_form_theta_period_ne_zero`.
