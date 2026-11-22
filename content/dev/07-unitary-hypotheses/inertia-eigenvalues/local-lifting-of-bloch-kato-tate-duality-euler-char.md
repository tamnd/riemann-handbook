---
id: local-lifting-of-bloch-kato-tate-duality-euler-char
title: The local colength bound from Bloch-Kato and Tate, restated
kind: theorem
decl: GlobalTheory.T.localLifting_of_blochKato_tateDuality_eulerChar
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremAOfBlochKatoTateDualityEulerCStatement
covers: 1180
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the closing of the local bound](/entry/theorem-a-closing/). Its only user is [the twisted place bound](/entry/twisted-place-bound-closing/), which applies it with $C = 160$ to get the local hypothesis `admA 160`. The content is in [the closing of the local bound](/entry/theorem-a-closing/) and below it in [the integrality bound for large constants](/entry/integrality-from-metric-of-large-constant/).

## Statement

**Theorem.** Assume three statements of local Galois cohomology:

- `BlochKatoLocal`: for each prime $\ell$ and each finite extension $K$ of $\mathbb{Q}_\ell$, a dimension formula, a rational duality and an integral duality for the Bloch-Kato subspaces $H^1_f$;
- `LocalTateDualityK`: local Tate duality for finite $\ell$-power torsion modules over $K$;
- `LocalEulerCharK`: the local Euler characteristic formula $\#H^1 = \#H^0 \cdot \#H^2 \cdot (\#M)^{[K:\mathbb{Q}_\ell]}$.

Then for each datum $D$, all local data $HW$, $F$, $Cm$ over it, and each real $C \ge 160$, the local bound `Conclusion1 D C` holds.

`Conclusion1 D C` is a bound on the colength of the map on $H^1_f$ given by a surjection of crystalline lattices. It is stated in full in [the closing of the local bound](/entry/theorem-a-closing/).

## Proof

The proof is the term `GlobalTheory.theoremA_closing`. There is nothing else.

## In the Lean code

The theorem is at [LocalLiftingTheoremAOfBlochKatoTateDualityEulerCStatement.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremAOfBlochKatoTateDualityEulerCStatement.lean#L11). Its type is the type of `theoremA_closing`, word for word. The proof is a `first` combinator that tries `exact @theoremA_closing` first.

- The name says "local lifting", and the module name says "Theorem A". The conclusion `Conclusion1` is defined as `TheoremBLocal` in [ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L54), and `TheoremBLocal` is built from a predicate `thmA`. So the letters A and B do not agree. The outline has a separate entry for [a Theorem B lifting](/entry/local-lifting-theorem-b-of-bloch-kato-tate-duality-euler-char/); this page does not compare the two.
