---
id: lifting-step-theorem-t-of-bhatt-scholze-fontaine
title: The lifting step from Bhatt-Scholze and Fontaine, restated
kind: theorem
decl: GlobalTheory.T.liftingStep_theoremT_of_bhattScholze_fontaine
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftingStepTheoremTOfBhattScholzeFontaineStatement
covers: 2990
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`TheoremTClosing.main`](/entry/theorem-tclosing-main/). Its only user is [the local lifting exponent](/entry/theorem-t-all-records/). The content is in [`TheoremTClosing.main`](/entry/theorem-tclosing-main/) and below it in [the lift of a surjection of good lattices](/entry/lift-surjection-good-crystalline-lattices/).

## Statement

**Theorem.** Assume `BhattScholzeCrystallineLattices` (crystalline lattices are realized by prismatic $F$-crystals, functorially) and `FontaineBcris` (injectivity, the fundamental exact sequence and regularity for the ring $B_{\mathrm{cris}}$ of the code). Let $C \ge 40$ be an integer. Then for each datum $D$ and local data $HW$, $F$: if the six local inputs `Adm2 D HW F` hold, then `Conclusion2 D C` holds.

`Conclusion2 D C` is stated in full in [the local lifting exponent](/entry/theorem-t-all-records/).

## Proof

The proof is the term `GlobalTheory.TheoremTClosing.main`.

That proof does this. It sets $a = (\ell - 1)!$ and $e = \ell^a - 1$. It enlarges the coefficient field $L$ to a field $L'$ with data `HasUnr a` and `TameDescentExponentData`, and reduces to $L'$ by `theoremT_descend_smaller_coefficients`. It replaces the characters of inertia by a set $\Sigma' \subseteq \mathbb{Z}/e$ stable under multiplication by $\ell$ (`exists_tameField_goodLattice_potentiallyCrystalline`). Then `lift_surjection_good_crystalline_lattices` gives the exponent $7(Nr' + \eta(N + r'))$, and `maxFrobeniusOrbitLengthDiff_bounds_zmod` gives $4r' \le N^2$. Since $7 \le C$, the exponent with $C$ follows. The bound $C \ge 40$ is used to get $40(HN^2 + N^3) < \ell$.

## In the Lean code

The theorem is at [LiftingStepTheoremTOfBhattScholzeFontaineStatement.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingStepTheoremTOfBhattScholzeFontaineStatement.lean#L11). Its type is the type of `TheoremTClosing.main`, word for word. The implication `Adm2 → Conclusion2` is the definition `HodgeTateFromSandwich` in [ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L224).

- **The hypothesis `Adm2` is not used.** In [LiftingStepTheoremTOfBhattScholzeFontaine.lean line 39](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingStepTheoremTOfBhattScholzeFontaine.lean#L39), the proof introduces it as `_`. So the theorem proves `Conclusion2 D C` outright from the two published statements.
- The name `HodgeTateFromSandwich` does not describe the statement. The conclusion is a lifting exponent for $H^1_f$.
- This page has not unfolded `HasUnr`, `TameDescentExponentData` or `IsGood`.
