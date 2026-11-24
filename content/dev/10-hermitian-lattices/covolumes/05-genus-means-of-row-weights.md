---
title: Genus means of row weights
decls:
  - GlobalTheory.RowsOrb.rowsOrbC
  - GlobalTheory.T.rowsGenus_weightedSumComparison
  - GlobalTheory.TypeAsm.rowsMean
  - GlobalTheory.T.rowsMeanC_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Genus means of row weights

This section compares sums over row lattices with sums over a genus of definite lattices. A row lattice $\Lambda$ has a base lattice $\Lambda_0$ in a definite space $W$. We show that the sum of the row weights of the rows whose base lattices lie in one genus, each weighted by an invariant function of the base lattice, is $(T_u - 1)^f$ times the orbit sum of the function over that genus. As a consequence, a bound for orbit sums over each genus by the mass gives a bound for the weighted sum over all rows by the total row mass. The [type bound](/entry/rows-pos-type-p/) uses this for the pairs of terms, through the [pair count](/entry/pair-count-bound-of-siegel-mass/).

We keep the notation of [the pairs over one row lattice](/entry/per-row-c/). In the setting, the word $u$ has a finite set of row lattices $\Lambda$ in $V$, each with its row weight $w(\Lambda)$. The *row mass* is
$$m_{\mathrm{row}}(u) = \sum_{\Lambda} w(\Lambda),$$
the sum over the row lattices of $u$. Let $W$ be a Hermitian subspace of $V$ whose inclusion is an embedding along $F_0$. For a row lattice $\Lambda$ let $\Lambda_0$ be the preimage of $\Lambda + X$ in $W$. This is a lattice in $W$, by a base lattice construction of the setting.

A function $\varphi$ on the lattices of $W$ with values in $[0, \infty]$ is *invariant* if $\varphi(sM) = \varphi(M)$ for every isometry $s$ of $W$ and every lattice $M$. For such $\varphi$ and a lattice $M$ let $\operatorname{orb}_M(\varphi)$ be the orbit sum of $\varphi$ over the genus of $M$, as in the previous section.

### Rows in one genus

**Theorem 2.5.1 (Rows in one genus).** Assume the standing hypotheses of the setting. Let $W$ be a Hermitian subspace whose inclusion is an embedding along $F_0$, let $\varphi$ be invariant and let $\Lambda^\circ$ be a row lattice. Then
$$\sum_{\Lambda} w(\Lambda)\, \varphi(\Lambda_0) = (T_u - 1)^f \operatorname{orb}_{\Lambda^\circ_0}(\varphi),$$
where $\Lambda$ runs over the row lattices with $\Lambda_0$ in the genus of $\Lambda^\circ_0$.

Lean: `GlobalTheory.RowsOrb.rowsOrbC` (also `GlobalTheory.T.rowsGenus_weightedSumComparison`, a second name).

*Proof.* The orthogonal space of the flag modulo $X$ has an anisotropic part. There is an isometry $\epsilon$ from this part onto $W$, and $\Lambda_0$ is the image under $\epsilon$ of the anisotropic part of the quotient lattice of $\Lambda$. The isometry carries genera to genera and orbit sums to orbit sums, so we may work in the anisotropic part. Call $M^\circ$ the lattice there that corresponds to $\Lambda^\circ_0$.

Let $W_b$ be the space spanned by the anisotropic part and the vector $z$ of the word, with $H(z, z) = -T_u$. Consider the unimodular lattices $L$ in $W_b$ for which $z$ is primitive and whose part orthogonal to $z$ is in the genus of $M^\circ$. Let $G_z$ be the stabilizer of $z$. A mean value theorem for rows states that the $G_z$-orbit sum of $\varphi$ over these $L$ is $(T_u - 1)^f \operatorname{orb}_{M^\circ}(\varphi)$. It needs that $T_u$ is prime, the conditions on the primes over $T_u$, that the anisotropic part is totally positive definite, and that the discriminant module of $M^\circ$ is the right one.

It remains to match the rows with these orbits. Each row lattice gives such an $L$, and every such $L$ comes from a row lattice. Two row lattices whose lattices are conjugate under $G_z$ are equal. Hence the map from rows to orbits is a bijection on the rows in the genus. The automorphism group of a row has the same size as the stabilizer of its lattice in $G_z$. So the row weight $w(\Lambda)$ is the inverse of the size of the stabilizer, and the two sums agree term by term. $\square$

### The mean over all rows

**Corollary 2.5.2 (Rows mean bound).** Assume the standing hypotheses of the setting. Let $W$ be a Hermitian subspace whose inclusion is an embedding along $F_0$, let $\varphi$ be invariant and let $B \ge 0$. Assume that
$$\operatorname{orb}_{\Lambda_0}(\varphi) \le m(\Lambda_0)\, B$$
for every row lattice $\Lambda$, where $m$ is the mass. Then
$$\sum_{\Lambda} w(\Lambda)\, \varphi(\Lambda_0) \le m_{\mathrm{row}}(u)\, B,$$
the sum over all row lattices of $u$.

Lean: `GlobalTheory.TypeAsm.rowsMean` (also `GlobalTheory.T.rowsMeanC_holds`, a second name).

*Proof.* Sort the row lattices by the genus of $\Lambda_0$. Fix one genus, given by a row lattice $\Lambda^\circ$. The mass is at most the orbit mass of the genus, that is $m(\Lambda^\circ_0) \le \operatorname{orb}_{\Lambda^\circ_0}(1)$, since the stabilizers in the orbit sum are isomorphic to the automorphism groups of the lattices. Apply the theorem to $\varphi$ and to $\varphi = 1$:
$$\begin{aligned}
\sum_{\Lambda} w(\Lambda)\, \varphi(\Lambda_0) &= (T_u - 1)^f \operatorname{orb}_{\Lambda^\circ_0}(\varphi) \le (T_u - 1)^f\, m(\Lambda^\circ_0)\, B \\
&\le (T_u - 1)^f \operatorname{orb}_{\Lambda^\circ_0}(1)\, B = \Big(\sum_{\Lambda} w(\Lambda)\Big) B,
\end{aligned}$$
where both sums run over the row lattices in the genus. Summing over the genera gives the claim. $\square$

**Remark 2.5.3 (Formalization).** The statements `RowsOrbC` and `RowsMeanC` are definitions in RowsMeanC.lean. The row weight is `wRow`, defined from `Nat.card` of `autLz` in FlagEEqHyperbolic.lean, so it is $0$ when that group is infinite; the row mass is `massRows` (CntPartners.lean, line 207). The orbit sum on the right of the theorem is in `ℝ≥0∞` and uses `ENat.card` of the stabilizer; the helper lemma `cardE` matches `ENNReal.ofReal (Nat.card α)⁻¹` with `(ENat.card α)⁻¹`. The proof of the theorem ([RowsGenusWeightedSumComparison.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowsGenusWeightedSumComparison.lean#L36)) runs under `set_option maxHeartbeats 4000000` and uses `anisotropicOrthogonal_isometric_definiteModel`, `definiteQuotientLattice_eq_image_anisotropicPart`, `isometry_transports_genus_orbitSum`, `isometry_transports_discriminantModule`, `base_lattice_construction_holds`, the mean value theorem `GlobalTheory.Mass.RowMean.main`, `gluedLattices_stable_under_vectorStabilizer`, `rows_eq_of_stabilizer_conjugate_lattices`, `orbSum_eq_sum_reps`, `card_row_automorphisms_eq_lattice_stabilizer`, `orbit_lattice_unimodular_and_primitive` and `exists_row_of_unimodular_lattice_primitive_vector`. The proof of the corollary ([RowsMeanBoundOfGenusMean.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowsMeanBoundOfGenusMean.lean#L144)) uses `sum_le_of_classes` (line 122) and `mass_le_orbMass` (line 72). The second names are proved by a `first | exact ...` combinator under `set_option maxHeartbeats 1000000`.
