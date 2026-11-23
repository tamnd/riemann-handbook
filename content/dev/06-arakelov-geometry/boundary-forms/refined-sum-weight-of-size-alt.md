---
id: refined-sum-weight-of-size-alt
title: The reference exponent bound at the weight of a cover
kind: theorem
decl: GlobalTheory.RefSum.refinedSum_weight_of_size_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RefinedSumWeightOfSizeLe
covers: 1366
status: drafted
drafted_by: writer@claude
---
This theorem proves `ReferenceWeight`: on each good cover, the local exponents of vanishing of sections of a given weight are bounded by a small sum over primes. Its only user is its renaming [refW_of_prints_deepGood_size_flatDeg](/entry/ref-w-of-prints-deep-good-size-flat-deg/), which [the height lower bound](/entry/height-lower-bound-general-alt/) calls. There the bound gives the multiplicity constant `MultiplicityConstantCondition`. Below this theorem are 1,366 declarations.

## Statement

We use the cover statements of [the covolume bound](/entry/top-covol-g-alt-alt/). Fix a point $p$, a level $i$ with $i + 1 < m$, a good cover $Y$ and a weight $u$ with `Quo`. Let $L$ be the integer `lenT`.

For a prime $q$, the *reference exponent* $r_q(G) \in \overline{\mathbb{R}}$ of a weight $G$ is a supremum over complete discrete valuation rings $T$ above $q$ and algebraic integral points $y$ of the tower over $T$: it is the depth of vanishing of the weight $G$ sections at $y$, minus $\varphi/(2500\, v(q))$ for a number $\varphi$ attached to $y$ (`refExp_vp`).

`RefAt` with constant $C$ says: there are a finite set $S$ of primes and numbers $e_q \ge 0$, zero off $S$, with

$$\sum_{q \in S} e_q \log q \le s, \qquad L s \le C\,\mathrm{unitE}, \qquad r_q(G) \le e_q \text{ for each prime } q.$$

**Theorem.** If `PublishedHodgeBundleTheorems`, `DeepGoodness`, `SizeCondition` and `FlatDegreeCondition` hold, then `ReferenceWeight` holds: `RefAt` holds for the tower of $Y$ and the weight $u$ (in the form `wtOf u 0`), with one constant $C$ for all $p, i, Y, u$.

## Proof

The proof is a chain of four steps. It moves the bound from the core tower to the cover, and then from the theta weight $G_u$ (`GOf`) to the weight $u$.

1. `sumPt_of_size_alt`: from `SizeCondition`, an oscillation bound `OscLe` at each prime $q$ that is not one of the host primes $g_k$, with a prime sum as above (`SumPtAlt`).
2. `refCore_of_size_sumPt`: `RefAt` on the core tower at level $i + 1$ for the weight $G_u$ (`ReferenceCore`). At the host primes it uses `supLatticeReferenceExponent_thetaWeight_level_le_one`, at other primes `baseLocusExponent_le_oscillation_nonTypePrime`.
3. `refTheta_of_refCore_alt`: the same bound on each good cover (`ReferenceTheta`), by `refExp_vp_cover_le`.
4. `refinedSum_weight_of_refinedTheta_alt`: the change of weight from $G_u$ to $u$. It adds the bad primes of the cover level to $S$ and bounds $r_q$ by `reference_exponent_valuation_bound`, which uses the bundle and the flat degree.

The rest is bookkeeping with `Closed.and` and `Closed.imp`.

## In the Lean code

The theorem is at [RefinedSumWeightOfSizeLe.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefinedSumWeightOfSizeLe.lean#L16). The proof is one term.

- The hypothesis `DeepGoodness` is never used: the proof binds it as `_`.
- `PublishedHodgeBundleTheorems` and `FlatDegreeCondition` are used only in step 4.
- The proof calls the four steps through `GlobalTheory.T` renamings (`sum_pt_of_size`, `reference_core_of_size_and_sum_point`, `refTheta_of_size_refCore`, `refW_of_prints_size_flatDeg_refTheta`). Each is `first | exact ...` of the lemma named above.
- We have not unfolded `OscLe`, `depthAt_vp`, `HasPhi` or the four lemmas of steps 2 to 4.
