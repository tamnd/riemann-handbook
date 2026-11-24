---
title: The ascent of Bessel periods
decls:
  - GlobalTheory.T.tameFunctional_kills_fockVacuum_realTranslates
  - GlobalTheory.FockTransl.tame_kills_real_translates
  - GlobalTheory.T.fockConjugates_span_depth_data
  - GlobalTheory.ConjDataTotal.fockTot
  - GlobalTheory.T.bessel_period_gives_fourierJacobi_period_of_lift
  - GlobalTheory.UpFromBessel.upFB
  - GlobalTheory.T.bessel_to_fourierJacobi_nonvanishing_tower
  - GlobalTheory.Asc.RungJac.rungJ
  - GlobalTheory.T.besselToFourierJacobi_mixedPieces_admissible
  - GlobalTheory.PcBF.pieces_bf
  - GlobalTheory.T.besselToFourierJacobi_depthLattice_splits
  - GlobalTheory.AscFin.pcBF_splits
  - GlobalTheory.T.fourierJacobi_step_pieces_admissible_splits
  - GlobalTheory.AscFin.piecesFB_is_and_splits
  - GlobalTheory.AscFin.GoodStd.loc_cls
  - GlobalTheory.T.exists_unfolding_flatMap_ne_zero_fullRank
  - GlobalTheory.AscFinNe.flat_ne_zero
  - GlobalTheory.T.standardAuxiliaryFrames_good_row_grids
  - GlobalTheory.AscFin.GoodStd.std_good
  - GlobalTheory.T.existsGoodGridFrames_of_depthFixed
  - GlobalTheory.AscFin.towerEx_of_depFixed
  - GlobalTheory.T.bessel_period_nonvanishing_ascent_of_depth_data
  - GlobalTheory.Asc.ascent_of_depFixed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The ascent of Bessel periods

This section proves the main result of the chapter. If a column chain of core forms has a nonzero period at the bottom of the grid, then a theta lift of the row form has a nonzero period at the top. The proof climbs the tower one rung at a time and alternates [Bessel and Fourier-Jacobi periods](/learn/periods/#bessel-and-fourier-jacobi-periods), as in [the descent of Ginzburg, Rallis and Soudry](/learn/periods/#the-descent-of-ginzburg-rallis-and-soudry). The result is used in [the separation of real functionals](/entry/real-functionals-separate-of-hypothesis/).

### Tame functionals and Fock vectors

Let $S$ and $T$ be Hermitian spaces and let $\psi$ be a standard additive character. A *theta function* is a function on $\mathrm{Hom}(S, T)(\mathbb{A})$ in the Weil representation, and $\mathrm{heis}(w)$ is the Heisenberg translation by $w$ (see [the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups)). A linear functional $\ell$ on theta functions is *tame* if it is continuous and bounded on each Heisenberg orbit and commutes with integrals of Heisenberg translates. For frames $A$ of $S$ and $B$ of $T$ at the real places, a theta function $f$ is a *Fock vacuum* if it is the Gaussian at the real places, and $\mathrm{pt}(f, P)$ is the Fock vector of $f$ for a polynomial $P$ (see [the Fock model](/learn/theta/#the-fock-model)).

**Lemma 8.13.1 (Tame functionals kill real translates).** Let $\ell$ be tame and $f$ a Fock vacuum for $A$ and $B$. If $\ell(\mathrm{pt}(f, P)) = 0$ for all $P$, then $\ell(\mathrm{heis}(w) f) = 0$ for each $w$ with finite part $0$.

Lean: `GlobalTheory.T.tameFunctional_kills_fockVacuum_realTranslates` (also `GlobalTheory.FockTransl.tame_kills_real_translates`, the proof).

*Proof.* The real points are a complex vector space through the frames, so write $w$ as the Fock point of some $z_0$. Put $F(z) = \ell(\mathrm{heis}(z) f)$. Then $F$ is continuous and bounded. The integral of $F$ against a conjugate monomial times a Gaussian is $\ell$ of a Taylor coefficient of the Bargmann reading of $f$, and that coefficient is a Fock vector of $f$. So all these moments vanish. The Bargmann reproducing formula then gives $F(z_0) = 0$. $\square$

For a row $i < m$ of a grid, let $\kappa \mapsto v_\kappa$ be the first row coset vectors of the pair $(V_{i+1,0}, V_{i,0})$, and let $\Lambda_i$ be the row lattice.

**Theorem 8.13.2 (Fock conjugates span the depth data).** For each grid datum and each $i < m$, let $\ell$ be a tame functional on the theta functions of the row pair at $i$. If $\ell$ kills the conjugates of all Fock vectors of all $v_\kappa$, then $\ell$ kills every $\Lambda_i$ vacuum.

Lean: `GlobalTheory.T.fockConjugates_span_depth_data` (also `GlobalTheory.ConjDataTotal.fockTot`, the proof).

*Proof.* Choose real frames of the two spaces with the orthonormal bases of the grid, so that the Fock vectors of the frames are those of the grid. The conjugate $\bar\ell$ is tame. The previous lemma, applied to $\bar\ell$ and the vacua $v_\kappa$, shows that $\ell$ kills the conjugates of the real translates of all $v_\kappa$. Write an element $w$ of the annihilator of $\Lambda_i$ as $w_\infty + w_f$. The finite translate $\mathrm{heis}(w_f)\bar v_0$ is in the span of the $\bar v_\kappa$, because the Heisenberg commutant permutes the coset vectors. So $\ell$ kills $\mathrm{heis}(w)\bar v_0$. Since $\bar v_0$ is a nonzero vacuum, the irreducibility of tame functionals on vacua gives the claim. $\square$

### One rung

A *Bessel level* $B$ of depth $\sigma$ and a *Jacobi level* $J$ of depth $\sigma + 1$ carry Witt decompositions with $\sigma$ and $\sigma + 1$ hyperbolic planes. A *step* $s$ from $J$ to $B$ is a Weil datum with volumes, and $s.\mathrm{lift}(G, \Phi)$ is the seesaw lift of a form $G$ by a theta function $\Phi$. The *local conditions* $\mathrm{Loc}(s, x, \mathcal{S}, \Gamma_0, K)$ on a set $\mathcal{S}$ of theta functions, a lattice $\Gamma_0$ and a subgroup $K$ say this.

1. $\mathcal{S}$ consists of theta functions and is stable under real translations and under the core annihilator of $\Gamma_0$.
2. The flat map sends $\mathcal{S}$ to $\Gamma_0$ vacua.
3. $K$ is compact open in the finite points and fixes $\mathcal{S}$.
4. If the flat map of $\omega(1, h)\Phi$ is not $0$, then $h = r a k$ with $r x = x u$, $a$ real and $k \in K$.
5. The flat map is not $0$ on $\mathcal{S}$.

**Theorem 8.13.3 (A Bessel period gives a Fourier-Jacobi period).** Let $s$ be a step from $J$ to $B$ with local conditions for $(\mathcal{S}, \Gamma_0, K)$. Let the characters satisfy $\chi_W = \chi_A \chi_z$, with Weil data for $\chi_A$ and $\chi_z$. Let $\varphi$ and $G$ be rapidly decreasing, with $G$ right invariant under $K$. Let $\Xi_1$ and $\Phi_0 \ne 0$ be theta functions with $\mathrm{box}(\Xi_1, \Phi_0)$ a $\Gamma_0$ vacuum. If the Bessel period of $G$ against the lift of $\varphi$ by $\Xi_1$ is not $0$, then there is $\Phi \in \mathcal{S}$ with

$$\mathcal{P}^J\bigl(\varphi,\ s.\mathrm{lift}(G, \Phi),\ \Phi_0\bigr) \ne 0.$$

Lean: `GlobalTheory.T.bessel_period_gives_fourierJacobi_period_of_lift` (also `GlobalTheory.UpFromBessel.upFB`, the proof).

*Proof.* Assume that all these Fourier-Jacobi periods vanish. The vanishing descends to the Bessel side: the handed down Bessel functional $\lambda$ kills the flat map of each translate in $\mathcal{S}$. The functional $\lambda$ is tame. By the local conditions, there is $\Phi \in \mathcal{S}$ whose flat map is a nonzero $\Gamma_0$ vacuum, and the core translates stay in $\mathcal{S}$. Irreducibility of tame functionals on vacua gives that $\lambda$ kills every $\Gamma_0$ vacuum, in particular $\mathrm{box}(\Xi_1, \Phi_0)$. This value is the Bessel period times the pairing of $\Phi_0$ with itself. The pairing is not $0$, because $\Phi_0 \ne 0$ is continuous and periodic. So the Bessel period is $0$, which is false. $\square$

Fix a grid datum, core volumes $v$, frames $F$ with ends fitted and good for lattices $\Gamma_L$, a column chain $\Psi$ and a rapid row form $u$. Let $\mathrm{part}(\rho, \Phi)_n$ be the partial theta lift of $u$ to the row $n$. *Bessel nonvanishing at $k$* means that the Bessel period of $\bar\Psi_{2k+2}$ against $\overline{\mathrm{part}(\rho, \Phi)}_{2k+2}$ is not $0$ for some $(\rho, \Phi)$. *Jacobi nonvanishing at $k$* means that there are a Weil datum for $\eta$ and $(\rho, \Phi, \Phi_0)$, with $\Phi_0$ a $\Gamma_L(k)$ vacuum, such that the Fourier-Jacobi period of $\bar\Psi_{2k+1}$ against $\overline{\mathrm{part}(\rho, \Phi)}_{2k+1}$ and $\Phi_0$ is not $0$.

**Theorem 8.13.4 (Bessel to Fourier-Jacobi along the tower).** Assume that the Fock conjugates span the depth data and that the partial lifts are fixed by the level groups. Then Bessel nonvanishing at $k$ implies Jacobi nonvanishing at $k + 1$.

Lean: `GlobalTheory.T.bessel_to_fourierJacobi_nonvanishing_tower` (also `GlobalTheory.Asc.RungJac.rungJ`, the proof).

*Proof.* Read the Weil data of the grid at row $2k + 2$, and build a step $s$ from the Jacobi frame at $k + 1$ to the Bessel frame at $k$. The good frames give $(\mathcal{S}, \Gamma_0)$ with local conditions, and a nonzero line vacuum $\Phi_0$. The Bessel period is the period of the lift of $\bar\Psi_{2k+3}$ by the conjugate depth vector, so the previous theorem gives $\Phi' \in \mathcal{S}$ with a nonzero Fourier-Jacobi period. As a function of the row theta function, this period is a tame functional. If it killed all conjugate Fock vectors of the coset vectors, the previous theorem on Fock conjugates would make it vanish at $\Phi'$. So it is not $0$ at some $\bar{\mathrm{pt}}(v_\kappa, P)$. Put $P$ and $\kappa$ into $\rho$ and $\Phi$ at row $2k + 2$. The partial lift to row $2k + 2$ does not change, and the lift to row $2k + 3$ is the seesaw lift by this vector. $\square$

### The pieces of a step

A *piece system* $p$ for a step consists of lattices $A_1, A_2$ in $M_{\dim W \times \rho}$, lattices $B_1, B_2$ in $M_{\sigma \times \dim V_0}$, and a core lattice $\Gamma_0$. It is *admissible* for $x$ if all four lattices are finite, $A_1$ and $A_2$ are mutual annihilators under $\psi$ and the symplectic form, and so are $B_1$ and $B_2$, $\psi$ of the generic character is $1$ on the unipotent elements that move $x$ into $A_1$, and $\Gamma_0$ is finite with a nonzero vacuum. It *splits* a lattice $\Gamma$ for $(x, y)$ if each $u \in \Gamma$ is a sum of elements of $A_1, A_2, B_1, B_2$ and $\Gamma_0$, placed by the decompositions, with the base point characters $1$ on the parts in $A_2$ and $B_1$. The *class* $\mathrm{cls}(p, x, y)$ is the set of theta functions that are fixed by $A_1$ and $B_2$, that transform by the characters of $x$ on $A_2$ and of $y$ on $B_1$, and that are $\Gamma_0$ vacua.

Frames $F$ are *standard* if their vectors and decompositions are read off from the column data of the grid.

**Proposition 8.13.5 (Bessel to Fourier-Jacobi pieces).** For standard frames and each $\rho$ with $2\rho + 2 \le m$, the pieces $p_{BF}(\rho)$ are admissible for $x_0$, and they split the row lattice $\Lambda_{2\rho+1}$ for $(x_0, y_{BF})$.

Lean: `GlobalTheory.T.besselToFourierJacobi_mixedPieces_admissible` (also `GlobalTheory.PcBF.pieces_bf`, the proof).

*Proof.* The lattice $A_1$ is finite by the standard parabolic, and $A_2$ is a closure of finite elements. The lattices $B_1$ and $B_2$ are finite and mutual annihilators. Biduality of the depth lattice gives that $A_1$ and $A_2$ are mutual annihilators. The generic character is trivial on the unitriangular part, and the core piece is finite with a nonzero vacuum. The splitting is the next lemma. $\square$

**Lemma 8.13.6 (The depth lattice splits).** Under the same hypotheses, $p_{BF}(\rho)$ splits $\Lambda_{2\rho+1}$ for $(x_0, y_{BF})$.

Lean: `GlobalTheory.T.besselToFourierJacobi_depthLattice_splits` (also `GlobalTheory.AscFin.pcBF_splits`, the proof).

*Proof.* Decompose $u \in \Lambda_{2\rho+1}$ along the Witt decomposition of the source, and then decompose its core part along the target. The source parts lie in $A_1$ and in the closure $A_2$. The core parts lie in the self dual lattice, so in $B_1$, $B_2$ and $\Gamma_0$. The two base point characters are trivial on the depth lattice. $\square$

**Proposition 8.13.7 (Fourier-Jacobi to Bessel pieces).** For standard frames and each $\sigma$ with $2(\sigma + 1) + 2 \le m$, the pieces $p_{FB}(\sigma)$ are admissible for $x_{FB}$, and they split $\Lambda_{2\sigma+2}$ for $(x_{FB}, 0)$.

Lean: `GlobalTheory.T.fourierJacobi_step_pieces_admissible_splits` (also `GlobalTheory.AscFin.piecesFB_is_and_splits`, the proof).

*Proof.* The same lemmas for the Fourier-Jacobi step give finiteness, mutual annihilators, the trivial generic character, the nonzero core vacuum and the splitting. $\square$

**Lemma 8.13.8 (The flat map is not zero).** Let $x_0$ be a rational matrix with linearly independent columns, and let $p$ be admissible for $x_0$. Then there is $\Phi \in \mathrm{cls}(p, x_0, y)$ whose flat map is not $0$.

Lean: `GlobalTheory.T.exists_unfolding_flatMap_ne_zero_fullRank` (also `GlobalTheory.AscFinNe.flat_ne_zero`, the proof).

*Proof.* Take a nonzero core vacuum $g$, a bump $\beta_2$ periodic under $B_2$, and a left inverse of $x_0$. Choose a bump $b$ near $x_0$, periodic under $A_1$, on which the real part of the trace character is positive. Build $\Phi$ from $b$, $\beta_2$ and $g$ in the mixed model. It is in the class. Its flat map is a unitriangular integral of $b$ times a positive real part. The support is compact by full rank, so the integral is not $0$. $\square$

**Lemma 8.13.9 (Local conditions for the class).** Let $x_0$ have linearly independent columns, let $p$ be admissible for $x_0$ and split $\Gamma$, and let $K$ be compact open in the finite points and fix each $\Gamma$ vacuum. Assume that each $h$ for which the unfolding conditions hold at $h$ and at $h\kappa$ for all $\kappa \in K$ has the form $r a k$. Then $\mathrm{Loc}(s, x_0, \mathrm{cls}(p), \Gamma_0, K)$ holds, and each element of the class is a $\Gamma$ vacuum.

Lean: `GlobalTheory.AscFin.GoodStd.loc_cls`.

*Proof.* The splitting puts the class inside the $\Gamma$ vacua, so $K$ fixes it. The class is stable and the flat map gives vacua. A nonzero flat map of $\omega(1, h)\Phi$ gives the unfolding conditions at $h$, and also at $h\kappa$ since $\omega(1, \kappa)\Phi = \Phi$. The previous lemma gives clause 5. $\square$

### Good frames and the ascent

Let $\mathrm{DepFixed}$ say that for each grid datum and each $i < m$, each depth vector of the row pair or the core pair at $i$ is fixed by the level groups of both spaces. Frames are *good* for $\Gamma_L$ if each step has a set with local conditions as above, each line lattice has a nonzero vacuum, and the bottom lattices fit.

**Theorem 8.13.10 (Standard frames are good).** Assume $\mathrm{DepFixed}$. For each grid datum, each $v$ and each standard $F$, the frames $F$ are good for their line lattices.

Lean: `GlobalTheory.T.standardAuxiliaryFrames_good_row_grids` (also `GlobalTheory.AscFin.GoodStd.std_good`, the proof).

*Proof.* By $\mathrm{DepFixed}$ the level groups fix the row vacua, and they are compact open with a local test for the form $r a k$. Apply the previous lemma to the pieces of each step. The box clauses and the bottom data come from the line vacua. $\square$

**Theorem 8.13.11 (Good frames exist).** Assume $\mathrm{DepFixed}$. For each grid datum and each $v$, there are frames whose ends fit $v$ and that are good for some $\Gamma_L$.

Lean: `GlobalTheory.T.existsGoodGridFrames_of_depthFixed` (also `GlobalTheory.AscFin.towerEx_of_depFixed`, the proof).

*Proof.* Standard frames exist and their ends fit. The previous theorem makes them good, with $\Gamma_L$ the line lattices. $\square$

**Theorem 8.13.12 (Ascent of Bessel periods).** Assume $\mathrm{DepFixed}$. Let $\Psi$ be a column chain for $v$ and $u$ a rapid row form with

$$\int_{M} \Psi_0(h)\, u(h)\, dh \ne 0.$$

Then there are $\rho$ and $\Phi$ with $B^{+}_M\bigl(\Psi_m, \theta_\chi(\rho, \Phi, u)\bigr) \ne 0$.

Lean: `GlobalTheory.T.bessel_period_nonvanishing_ascent_of_depth_data` (also `GlobalTheory.Asc.ascent_of_depFixed`, the proof).

*Proof.* The Fock conjugates span the depth data, and $\mathrm{DepFixed}$ makes the partial lifts fixed by the level groups. Take good frames. The bottom rung gives Jacobi nonvanishing at $0$. The rungs from Fourier-Jacobi to Bessel and from Bessel to Fourier-Jacobi climb the tower. At the top, the ends of the frames turn the last Bessel period into $B^{+}$. $\square$

**Remark 8.13.13 (Formalization).** The results are in [TameFunctionalKillsFockVacuumRealTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/TameFunctionalKillsFockVacuumRealTranslates.lean#L28), [FockConjugatesSpanDepthData.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FockConjugatesSpanDepthData.lean#L190), [BesselPeriodGivesFourierJacobiPeriodOfLift.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselPeriodGivesFourierJacobiPeriodOfLift.lean#L64), [BesselToFourierJacobiNonvanishingTower.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselToFourierJacobiNonvanishingTower.lean#L57), [BesselToFourierJacobiMixedPiecesAdmissible.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselToFourierJacobiMixedPiecesAdmissible.lean#L50), [BesselToFourierJacobiDepthLatticeSplits.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselToFourierJacobiDepthLatticeSplits.lean#L19), [FourierJacobiStepPiecesAdmissibleSplits.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FourierJacobiStepPiecesAdmissibleSplits.lean#L19), [ExistsUnfoldingFlatMapNeZeroFullRank.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsUnfoldingFlatMapNeZeroFullRank.lean#L42), [StandardAuxiliaryFramesGoodRowGrids.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/StandardAuxiliaryFramesGoodRowGrids.lean#L122), [ExistsGoodGridFramesOfDepthFixed.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsGoodGridFramesOfDepthFixed.lean#L17) and [BesselPeriodNonvanishingAscentOfDepthData.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BesselPeriodNonvanishingAscentOfDepthData.lean#L21). The rung from Bessel to Fourier-Jacobi uses the data of the step that the frames call the Fourier-Jacobi to Bessel step. The admissibility of pieces tests finiteness with the predicate that holds at all places. The splitting lemma is also the second half of the pieces proposition. We have not unfolded the flat map, the seesaw lifts or the frames, so their descriptions above are read from the names and from the way they are used.
