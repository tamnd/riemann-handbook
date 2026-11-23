---
title: The diagonal row and degenerate terms
decls:
  - GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary
  - GlobalTheory.T.diagonalRow_of_siegelWeil_unitary
  - GlobalTheory.Core.Deg.degenerate_and_collisions_uncond
  - GlobalTheory.T.degenerateTerms_and_collisionBounds_uniform_widths
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The diagonal row and degenerate terms

This section proves a bound on the diagonal of the row. For each word $u$ of a row datum, a projection $P_u$ maps a finite dimensional column space into the space of forms. After a normalisation, $P_u^* P_u$ is close to the identity in the Hilbert-Schmidt norm, with an error that we make explicit. The bound comes from an expansion of $P_u^* P_u$ as a sum of terms. We bound the degenerate terms and the pairs of terms with a large overlap without any hypothesis. The pairs of corank one need [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula). The diagonal bound is an input of [the multiplicity row](/entry/global-theory-mi-star-row-alt-alt/) of the open orbit chapter.

**Setting.** Let $D$ be a row datum with ranks $m \geq 2$, $f$ and $k$, two positive integers $g_0$ and $g_1$ of its host, and a finite set of words. For a word $u$, let $C_u$ be the column space, of dimension $d_0(u)$, let $P_u$ be its projection into the space of forms, and let $c_0(u) = \mathrm{vol}_N(u)\, \mathrm{vol}_H(u) / \dim \pi_u$, where $\dim \pi_u$ is the product over the infinite places of the dimensions of the representations of the word. The *Gram operator* is $K_u = c_0(u)^{-1} P_u^* P_u$ on $C_u$, and its *deviation* is
$$\delta(u) = \| K_u - 1 \|_{\mathrm{HS}}^2.$$
Let $D^* > 0$ be the number of the row datum that enters the counts. We write $\mu(L) = m^5 f L$ and $\kappa = k f \log k$.

**Definition 2.26.1 (Diagonal bound).** For real $L$ and $C$, the *diagonal bound* at $(D, u, L, C)$ says
$$\begin{aligned} \delta(u) \leq\ & 4 \big(e^{C \mu(L)} + 1\big)\, \frac{d_0(u)^2}{D^*} \\ & + \big(4 e^{-\kappa/2} + 2 e^{-\kappa}\big)\, d_0(u). \end{aligned}$$

**Definition 2.26.2 (Row statement).** Let $\mathcal{E}$ be a condition on $(D, L, C')$ and let $Q$ be a property of $(D, u, L, C)$. The *row statement* of $Q$ under $\mathcal{E}$ says: for all reals $C_g, c_b, C_u, c_T, C_T$ with $c_b > 0$ and $c_T > 0$, there are $C \geq 1$, $C'_0$ and $C_{\ell, 0}$ such that for all $C' \geq C'_0$ and $C_\ell \geq C_{\ell, 0}$, every true row datum $D$, every $L$ and every word $u$, if $\mathcal{E}(D, L, C')$ holds and the standing hypotheses at $(D, L, C', C_\ell, C_g, c_b, C_u, c_T, C_T)$ hold, then $Q(D, u, L, C)$ holds.

A row datum is *true* if it is the datum of a twisted tower with laws and later data, and if it has a world whose Hida setting has the identity as embedding of $E$. The *standing hypotheses* are the ties of $D$, the mid volume law of the family, the size hypotheses, the data condition and the frame condition at the top. We use the condition $\mathcal{E}_0(D, L, C')$: there are size data with scale $L$ and a constant $C_\Gamma$ with $1 \leq C_\Gamma$ and $8 C_\Gamma \leq C'$, and for every word $u$,
$$d_0(u) = d^*_u\, \big(T_u^{\,k} - 1\big)^f,$$
where $d^*_u$ and $T_u$ are numbers of the word $u$.

**Theorem 2.26.3 (The diagonal row).** Assume the Siegel-Weil formula for unitary groups in the convergent range. Then the row statement of the diagonal bound under $\mathcal{E}_0$ holds.

Lean: `GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary` (also `GlobalTheory.T.diagonalRow_of_siegelWeil_unitary`, a second name).

The hypothesis is a statement, not a proof. It says: for every CM extension $E/F$ and every nondegenerate hermitian matrix $J$ of size $M$, the unitary group has a fundamental domain of finite volume; and for $2n < M$, every hermitian $T$ of size $n$ with $\det T \neq 0$ and every factorizable Schwartz-Bruhat function $\Phi$, the mean over the fundamental domain of the theta sum of $\Phi$ over the vectors $X$ with Gram matrix $T$ is the product of the local densities of $\Phi$ at $T$.

To prove the theorem we first bound the terms of the expansion. Let $X$ be a Hida setting of $D$, let $Y$ be a full setting over $X$ and let $u$ be a word. The expansion of $K_u$ has terms $t$ with an operator $o(t)$, a vector $v(t)$, a row, a weight $G(t) \in \mathbb{R}$, and two flags, *identity* and *generic*. Each pair of terms has a number $s_0(t, t')$. A term is *degenerate* if $G(t) = 0$ and it is not an identity term. A pair is *big* if both terms have $G \neq 0$, they lie in the same row, and $s_0 \geq 2$. For a set $Q$ of pairs, let
$$A(Q) = \Gamma_1 \sum_{(t, t') \in Q} \big| \langle v(t), v(t') \rangle \big|,$$
where $\Gamma_1 > 0$ is the constant of the expansion. Let $S(Q)$ be the same sum with $\mathrm{Re}\, \langle v(t), v(t') \rangle$ in place of the absolute value. A pair is of *corank one* if both terms have $G \neq 0$, they lie in the same row, and $s_0 = 1$. Let $d_u$ be the dimension of $C_u$ for $Y$ and $D^*_C$ the count of $X$.

A property of $(Y, u)$ holds *on the width $c$* if, for all $C_g, c_b, C_u, c_T, C_T$ with $c_b > 0$ and $c_T > 0$, there is a threshold $\theta$ such that it holds for all $C', C_\ell \geq \theta$, all size data with $C_\Gamma \geq 1$, all Hida settings $X$ and finite full settings $Y$ that give the row datum, and all words $u$, under these hypotheses: the ties of $D$, the mid volume law, the counting hypotheses at window width $c$, the concrete tie of $(X, Y)$, and the absolute convergence of the terms.

**Theorem 2.26.4 (Degenerate terms and collisions).** For every real $c$, these two bounds hold on the width $c$:

1. the norms $\|o(t)\|$ over the degenerate terms are summable, and
$$\Big\| \sum_{t \ \mathrm{degenerate}} o(t) \Big\|^2 \leq d_u\, e^{-\kappa};$$
2. the big pairs satisfy
$$A(\mathrm{big}) \leq (g_0 g_1)^{-k f / 2}\, \frac{d_u^2}{D^*_C} + e^{-\kappa/2}\, d_u.$$

Lean: `GlobalTheory.Core.Deg.degenerate_and_collisions_uncond` (also `GlobalTheory.T.degenerateTerms_and_collisionBounds_uniform_widths`, a second name).

The theorem has no hypotheses.

*Proof.* We collect five results and combine them.

1. *Mass ratio.* For a CM field $K$ that satisfies the unramified condition and for $M \geq 3$, the ratio of the masses of the standard lattices of ranks $M$ and $M - 1$ with orthonormal bases is an explicit value. This is proved from the representations by binary hermitian forms, see [the mass formula](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups).
2. *Small terms.* The small bounds hold on all widths without hypotheses, so they hold on the width $c$.
3. *Type bound.* The type bound of the rows holds. It comes from the large gap of the discrete series and multiplicity one of Bessel models.
4. *Degenerate terms.* The type bound gives the bound on the vanishing Gram terms on a window, and then on every width. This is item 1.
5. *Big pairs.* The collision theorem takes the mass ratio, the uniform row amplitude bounds at width $c$, the corank two counts, the small bounds of step 2 and the tie bounds at width $c$. The corank two counts come from the row counts at width $c$, which use the mass ratio. This gives item 2. $\square$

*Proof of the diagonal row.* We use the theorem that a window of width $3$ gives the diagonal row. Its inputs are a decay law of Wu type, the two bounds above at $c = 3$, and the bounds on the corank one pairs, generic and not generic, at width $3$. The decay law is proved. The corank one bounds follow from the Siegel-Weil hypothesis. We now give the proof of the window theorem.

1. *Constants.* The corank one bounds give $C_1, C_2 \geq 0$ such that $S(Q_i) \leq e^{C_i \mu(L)}\, d_u^2 / D^*_C$, where $Q_1$ is the set of corank one pairs of generic terms and $Q_2$ the set of corank one pairs of terms that are not generic. Put $C = \max(C_1, C_2) + 1 \geq 1$, and take as $C'_0$ and $C_{\ell, 0}$ the largest of the four thresholds and $29$.
2. *Hypotheses at width $3$.* Fix $C', C_\ell$, a true $D$, $L$ and $u$ with $\mathcal{E}_0$ and the standing hypotheses. The size data of $\mathcal{E}_0$ have scale $L$ and $8 C_\Gamma \leq C'$. With the size hypotheses, they give the standing hypotheses of the counts. The data condition and the rank law for $d_0$ give the numerical data at width $3$. So the counting hypotheses hold at width $3$.
3. *A concrete setting.* Since $D$ is true, it has ties. With the decay law, this gives a concrete row datum $(X, Y)$ with a tie. The tie makes the terms absolutely convergent.
4. *Four bounds.* At $(X, Y, u)$ we now have the degenerate bound, the big pair bound and the two corank one bounds.
5. *Sizes.* The size hypotheses give $m^4 \leq f$ and $L > 1$, so $y = \mu(L) \geq 1$. Then $e^y \geq 2$, and
$$e^{C_1 y} + e^{C_2 y} \leq 2 e^{\max(C_1, C_2) y} \leq e^{C y}.$$
6. *Conclusion.* The diagonal theorem from four bounds turns these into a bound on $\delta(u)$ with the constant $e^{C y}$. The dimension $d_0(u)$ is the dimension number of the word $u$ in $D$, which is the number in that bound. So it is the diagonal bound at $(D, u, L, C)$. $\square$

**Remark 2.26.5 (Formalization).** The diagonal row is at [DiagonalRowOfSiegelWeilUnitary.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitary.lean#L50), and the window theorem is in [DiagonalRowBoundFromWindowWidthThree.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowBoundFromWindowWidthThree.lean#L38). The term bounds are at [DegenerateTermsAndCollisionBoundsUniformWidths.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DegenerateTermsAndCollisionBoundsUniformWidths.lean#L57). Both second names are at line 45 of the matching Statement files, by a `first | exact` block under one million heartbeats. The row statement is in [NotInhAbsOfGamLe.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/NotInhAbsOfGamLe.lean#L50), the diagonal bound and the rank law in [KerInclOn.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/KerInclOn.lean#L19) (line 26 for the rank law), and the Gram operator in [RelevantZeroGramTerms.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L339). The terms are in [StatementPB.lean](lean:Formalism/HermitianCurvature/StatementPB.lean#L15), the widths in [RowsPtAt.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/RowsPtAt.lean#L13), and the two bounds in [VanishingGramTermsBoundParams.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VanishingGramTermsBoundParams.lean#L65) and [CollSBound.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CollSBound.lean#L9). The Siegel-Weil hypothesis is the proposition at [SiegelWeilUnitaryConvergent.lean](lean:Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean#L46); it is assumed, not proved. The rank law and the scale condition are not proved here: they are part of the condition $\mathcal{E}_0$, so the row holds only for data that satisfy them. The rank law is used only for the numerical data at width $3$. The term bounds hold for every width $c$, also for $c \leq 0$, but only $c = 3$ is used. The thresholds are at least $29$ for a reason we have not traced. We have read the statements, not the proofs, of the mass ratio, the small bounds, the type bound, the collision theorem, the corank one bounds and the diagonal theorem from four bounds.
