---
id: amp-sq-nonzero-defect
title: The mean square over terms with a nonzero defect
kind: theorem
decl: GlobalTheory.HL.NonzeroDefect.ampSq_nonzero_defect
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.NonzeroDefectHeightPowerAbsorbsConstants
covers: 430
status: drafted
drafted_by: writer@claude
---
This theorem bounds, in coordinates, the weighted mean square of the oscillating sums over the terms with a nonzero defect. It gives the first clause of `NGAt` in [`ngAt`](/entry/ng-at/), the bound with the saving $q^{-(k-2r-5)}$. It splits the terms into two types and absorbs the constants into a power of the height.

## Statement

Fix a datum $S$ of type `Frames L r k`: a Hermitian form on $V = E^{k+2r+1}$ and two frames $f, f'$ with unipotent groups $N, N'$, as in [`ngAt`](/entry/ng-at/). Let $q$ be the residue field size and $N_0 = N \cap N'$.

- A *term* for a datum $d$ is an $\mathcal{O}$-lattice $\Lambda$ that is a translate $n \Lambda_0(d) = n' \Lambda'_0(d)$ of the standard lattices of both frames, with $n \in N$, $n' \in N'$ and compatibility conditions (`IsTerm`). Its mass is $\mu(\Lambda) = 1/\mathrm{vol}(N_0 \cap \mathrm{Stab}\,\Lambda)$, with a fixed compact subgroup of volume $1$, and its phase is $\omega(d, \Lambda) = \psi(n) \psi'(n')^{-1}$.
- For a property $P$: $a(d, P) = \sum_\Lambda \mu(\Lambda) \omega(d, \Lambda)$ and $m(d, P) = \sum_\Lambda \mu(\Lambda)$, over the $N_0$-orbits of terms with $P$.
- $\mathrm{ampSq}(P) = \sum_d \nu(d) \, |a(d, P_d)|^2$ and $\mathrm{nn} = \sum_d \nu(d) \, m(d, \text{all})$, over orbits of data with a weight $\nu(d)$.
- The *defect* of a term is the index $\beta(d, \Lambda)$ of the lattice $M(d, \Lambda)$ spanned by the vectors $n f_b$ and $\theta^{-1}(n' f'_b - n f_b)$ in $\Lambda \cap (\text{span of both frames})$. The defect is zero (`BBzero`) when the two lattices are equal.
- $H = H_S = q^{v_\theta + a + v_D}$ is the height, with exponents from the valuations of $G$ and of the minors $D_l \bar D_l$.

**Theorem.** If $4r + 7 \leq k$, then
$$\mathrm{ampSq}(\text{defect} \neq 0) \leq H^{39(r+1)^2} \, q^{-(k-2r-5)} \, \mathrm{nn}.$$

## Proof

If no term has a nonzero defect, the left side is $0$. Otherwise take such a term. Then $q \geq 2$ by `order_facts`, and $q \leq H$ by `exponents_and_defect`, so $H \geq 2$. Let $A = 392 \, H^{9(r+1)^2 + 16(r+1)} q^{-(k-2r-5)}$.

1. **Two types.** `ampSq_le_of_hermitianTermTypes_cauchySchwarz` gives $\mathrm{ampSq}(\text{defect} \neq 0) \leq H^{2(r+2)} B$ for any $B$ that bounds two families of sums: the first type with defect $\beta$, for each $\beta$; and the second type with invariants $(\beta, J, \beta_J)$, for each triple.
2. **First type.** `hermitianFrames_firstType_ampSq_bound` bounds it by $8 H^{9(r+1)^2+16(r+1)} q^{-(k-1)} \mathrm{nn}$. This is at most $A \, \mathrm{nn}$, since $k - 1 \geq k - 2r - 5$ (`num_first`).
3. **Second type.** [`hermitianDoubleCoset_secondType_family_ampSq_le`](/entry/hermitian-double-coset-second-type-family-amp-sq-le/) bounds it by $392 \, H^{9(r+1)^2+16(r+1)} q^{-2(k-2r-4)} \mathrm{nn}$. This is at most $A \, \mathrm{nn}$, since $2(k-2r-4) \geq k-2r-5$ (`num_second`).
4. **Constants.** `nonzeroDefect_height_power_absorbs_constants`: since $392 \leq 2^9 \leq H^9$ and $9 + 2(r+2) + 9(r+1)^2 + 16(r+1) \leq 39(r+1)^2$, we get $H^{2(r+2)} \cdot 392 \, H^{9(r+1)^2+16(r+1)} \leq H^{39(r+1)^2}$.

## In the Lean code

The theorem is in [NonzeroDefectHeightPowerAbsorbsConstants.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/NonzeroDefectHeightPowerAbsorbsConstants.lean#L49). It calls:

- `GlobalTheory.T.ampSq_le_of_hermitianTermTypes_cauchySchwarz` (a statement form of `HL.TypesCS.ampSq_le_of_types`);
- `GlobalTheory.T.hermitianFrames_firstType_ampSq_bound` and `GlobalTheory.T.hermitianDoubleCoset_secondType_family_ampSq_le`;
- `GlobalTheory.UnramOrder.order_facts` and `GlobalTheory.HL.Defect.exponents_and_defect`;
- `num_first`, `num_second` and `nonzeroDefect_height_power_absorbs_constants` in the same file.

Lean writes the constant as $98 \cdot H^{9(r+1)^2+12(r+1)} \cdot 4 H^{4(r+1)}$. Both type bounds are weakened to the common factor $q^{-(k-2r-5)}$: the first type saves $q^{-(k-1)}$ and the second $q^{-2(k-2r-4)}$. The module is named after the helper lemma on constants, not after this theorem. We have not unfolded the compatibility conditions in `IsTerm`, the lattice $M(d, \Lambda)$ or the second-type condition `TypeBe`.
