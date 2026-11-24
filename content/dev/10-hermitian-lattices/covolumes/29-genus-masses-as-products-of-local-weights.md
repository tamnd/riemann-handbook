---
title: Genus masses as products of local weights
decls:
  - GlobalTheory.T.mass_genus_local_data_product_local_weights
  - GlobalTheory.Unfold.mass_genus_local_weights
  - GlobalTheory.Mass.RowsRawMass.main
  - GlobalTheory.rowNGP_of_siegelWeil
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Genus masses as products of local weights

This section contains three results that the step [nonempty hypotheses](/step/nonempty-hyps/) uses about masses. The first says that the mass of a genus of local data, as defined in [Section 2.15.5](/entry/weights-add-up-to-mass/), is a constant times a finite product of local weights; this is the mass law assumed in [Section 2.27.2](/entry/generic-mass-le-height-pow-mul-glue-sum/). The second computes the total row mass over a flag at a split prime and the mass of each row lattice, in terms of the mass of the standard self-dual lattice of [Section 2.21.5](/entry/mass-bounds/). The third derives the row positivity property from a Siegel-Weil statement for unitary groups.

### The mass law

We keep the notation of [Section 2.15.5](/entry/weights-add-up-to-mass/). Let $u$, $u'$ be words, $F$ and $F'$ flags of rank $r_S$ with parameters $T_u$ and $T_{u'}$, and $w$ a point. Let $Z$ be local data of the setting and $(F_p, F'_p)$ a pair of local flags at each finite place $p$. A family $d = (d_p)_p$ of local data has a *mass* $\operatorname{mass}(d)$: the sum, over the classes $o$ of families in the genus of $d$ under the rational group $H_0(F, F')$, of $1 / |\operatorname{Stab}(o)|$. For two local data $d_p$, $d'_p$ at $p$ the *local weight* is
$$\operatorname{wt}(d_p, d'_p) = \frac{1}{\operatorname{vol}(\operatorname{Stab} d'_p : \operatorname{Stab} d_p)},$$
the inverse of the relative volume of the stabilizer of $d'_p$ with respect to the stabilizer of $d_p$. We have not unfolded the relative volume.

**Theorem 2.29.1 (The mass of a genus is a product of local weights).** Assume that the integral Gram matrix of $(F, F')$ is the matrix of the point $w$, that the Gram value of $(F, F')$ is nonzero, that the local flags are based at $T_u$, $T_{u'}$, $F$ and $F'$, and that they are relatively generic at every $p$. Let $d_0$ be a family of local data with a local term over $d_{0,p}$ at every $p$, and assume that there is a global lattice $\Lambda_0$ such that for almost all $p$ some term over $d_{0,p}$ has abelian part equal to the completion of $\Lambda_0$. Then there is $V_1 > 0$ such that for every family $d$ with a term over $d_p$ at every $p$ and with $d_p = d_{0,p}$ for almost all $p$,
$$\operatorname{mass}(d) = V_1 \prod_p \operatorname{wt}(d_{0,p}, d_p).$$
The product is a finite product in the sense of the formalization: it runs over the places where the factor differs from $1$, and is $1$ if there are infinitely many such places.

Lean: `GlobalTheory.Unfold.mass_genus_local_weights` (also `GlobalTheory.T.mass_genus_local_data_product_local_weights`, a second name).

*Proof.* The rational isometries fixing the frames $F$ and $F'$ embed into the product of the local unitary groups $U_{W_0, p}$ of the complements; this uses the hypothesis on the Gram matrix and the relative genericity. There is a global lattice $\Lambda_0$ over the local data $d_0$. At each $p$ the group $U_{W_0, p}$ acts on the local data, so that local moves are the action and the stabilizer of a datum is its stabilizer for the action. The stabilizers of $d_{0,p}$ are commensurable with the stabilizers of the completions of $\Lambda_0$, and equal to them for almost all $p$. An abstract restricted product formula for masses then applies: the embedded rational group preserves the completions of $\Lambda_0$ at almost all places, its double cosets with respect to the local lattice stabilizers are finite in number, and the rational isometries fixing the frames in a conjugate stabilizer form a finite set. It gives $V_1 > 0$ with
$$\operatorname{mass}(d) = V_1 \prod_p \operatorname{wt}(d_{0,p}, d_p)$$
once the mass of the genus of $d$ is written as a sum over the orbits of the rational group, and the local weight is identified with the inverse volume ratio of the stabilizers for the action. $\square$

This is the usual form of the Siegel mass formula in the language of adelic groups: the mass of a genus is a covolume of an adelic stabilizer, and changing the stabilizer at finitely many places multiplies it by the local index ratios. See Siegel (1935) for quadratic forms and Gan, Hanke and Yu (2001) for the comparison of local volumes.

### The rows at a split prime

Let $u$ be a word whose parameter $T = T_u$ is a prime, at least $3$, that splits completely in $E$; let $f$ be the number of primes of $E$ over $T$ counted as in the setting, so that $N_T = T^f$. Let $F_0$ be a flag with parameter $T$ whose form is the hyperbolic one and whose point is the one of $u$. Recall from [Section 2.14.3](/entry/row-lattice-of-local-standard/) that a *row lattice* for $F_0$ is a lattice $\Lambda$ in the genus of the reference lattice, fixed by the flag in the sense of the setting, whose isotropic part is the standard one. Each row lattice $\Lambda$ has the *row weight* $\operatorname{wRow}(\Lambda) = 1/|\operatorname{Aut}(\Lambda, F_0)|$ and the definite lattice $L_0(\Lambda)$ of rank $k$ cut out by the flag. A finite set $s$ of row lattices is a *set of representatives* if every row lattice is the image of exactly one element of $s$ under the stabilizer of $F_0$. Its *row mass* is
$$\operatorname{mass}_{\mathrm{rows}}(F_0, s) = \sum_{\Lambda \in s} \operatorname{wRow}(\Lambda).$$
Let $m_j$ be the mass of the standard self-dual lattice of rank $j$.

**Theorem 2.29.2 (Row masses at a split prime).** Under these assumptions, for every set $s$ of representatives,
$$\operatorname{mass}_{\mathrm{rows}}(F_0, s) = m_k\,(T^k - 1)^f.$$
For every row lattice $\Lambda$,
$$\operatorname{mass} L_0(\Lambda) = \frac{\operatorname{mass}_{\mathrm{rows}}(F_0, s)}{(T - 1)^f}, \qquad m_k\, N_T^{\,k-1} \le \operatorname{mass} L_0(\Lambda).$$

Lean: `GlobalTheory.Mass.RowsRawMass.main`.

*Proof.* There is a row lattice $\Lambda_0$. The gluing lemma for masses, applied with the lift number and the genus of the row lattices, gives
$$\operatorname{mass}_{\mathrm{rows}}(F_0, s) = (T-1)^f \operatorname{mass} L_0(\Lambda)$$
for every row lattice $\Lambda$, which is the second identity. At a prime that splits completely, the lattice $L_0(\Lambda)$ is an orthogonal sum, and its mass is
$$\operatorname{mass} L_0(\Lambda) = m_k \Bigl(\frac{T^k - 1}{T - 1}\Bigr)^f, \qquad m_k\, N_T^{\,k-1} \le \operatorname{mass} L_0(\Lambda).$$
Applied to $\Lambda_0$, the gluing identity gives the first identity. $\square$

### Row positivity from Siegel-Weil

**Theorem 2.29.3 (Row positivity from the Siegel-Weil formula).** Assume the convergent Siegel-Weil statement for unitary groups: for every CM extension $E/F$ and every nondegenerate Hermitian matrix $J$ over $E$, the theta integral converges and equals the product of the local Siegel densities. Then the row positivity property holds: for all constants $C_g, c_b, C_w, c_T, C_T, C_0$ with $c_b > 0$ and $c_T > 0$ there are $C_4 \ge 0$ and $C'_0$, $C_{l,0}$ such that for all $C' \ge C'_0$, $C_l \ge C_{l,0}$, every setting with the base hypotheses and every pair of standard words $u, u'$ whose double coset operator is absolutely convergent, the operator satisfies the row nongeneric bound with the constant $\varepsilon_{\mathrm{NG}}(C_4)$.

Lean: `GlobalTheory.rowNGP_of_siegelWeil`.

*Proof.* The Siegel-Weil statement gives choice data for the step at every infinite place, and the uniqueness of the gap at infinity makes the real objects of the setting lie at infinity for every pair of words. A theorem from the Siegel-Weil statement and the step choice data then gives the row positivity. $\square$

**Remark 2.29.4.** The theorem is conditional. It assumes the Siegel-Weil formula for unitary groups in its convergent range; the proof does not establish it. For the classical case see Weil (1965), and for unitary groups Ichino (2004).

**Remark 2.29.5 (Formalization).** The mass `massA` is in [LocClosed.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LocClosed.lean#L79) and the local weight `LocNG.Datum.wt` is `1 / volRel (Stab d) (Stab d0)` in [IsTermOver.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/IsTermOver.lean#L160). The theorem `mass_genus_local_weights` is in [MassGenusLocalDataProductLocalWeights.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/MassGenusLocalDataProductLocalWeights.lean#L26); the product is the finite product `∏ᶠ`, and the identity is stated in `ℝ≥0∞` as `ENNReal.ofReal (V1 * ...)`. Its main steps are `frameFixingIsometries_embed_prod_localUnitary`, `exists_globalLattice_over_localInnerData`, `localLatticeStabilisers_commensurable_almostEverywhere`, `mass_genus_restricted_product` and `genusMass_eq_sum_over_rationalGroup_orbits`; the proof above is our reading of them. The constant $V_1$ comes out of the abstract lemma `mass_genus_restricted_product`, and we have not checked whether it equals $\operatorname{mass}(d_0)$. The row statement is the property `stLem3L0` in [CongruenceAtSplitFrobeniusHolds.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CongruenceAtSplitFrobeniusHolds.lean#L524), proved by `RowsRawMass.main` in [RowsRawMassAndGenusMass.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowsRawMassAndGenusMass.lean#L33) from `gluing_mass_of_lift_number_genus`, `mass_rowLattice_orthogonal_split_prime` and `RowEx.main`. The row lattices `IsRowLat`, the representatives `IsRowReps` and the row weight `wRow` are in [FlagEEqHyperbolic.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/FlagEEqHyperbolic.lean#L99); the masses `massU`, `massS`, `massRows` and the norm `NT` are in [CntPartners.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CntPartners.lean#L157), and `L0X` is in [IsPrimitiveSub.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/IsPrimitiveSub.lean#L320). The hypothesis `SiegelWeilUnitaryConvergent` is in [SiegelWeilUnitaryConvergent.lean](lean:Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean#L46) as `SiegelWeilAt`, the conjunction of `FinVol` and `SiegelDensities`, which we did not unfold further; the conclusion `RowNGP` is in [RowsPos.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean#L37), and the property `RowNG` in it is not unfolded. The proof of `rowNGP_of_siegelWeil` in [RowPositivityOfSiegelWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean#L10) is one term: `rowNGP_of_siegelWeil_of_stepChoice` applied to `stepChoiceDataC_of_siegelWeil_inInfinity`, `realObj_inInfinityX_jsz` and `uniqGap_holds`.
