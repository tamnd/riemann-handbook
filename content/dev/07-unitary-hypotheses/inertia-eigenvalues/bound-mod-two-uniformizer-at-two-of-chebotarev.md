---
id: bound-mod-two-uniformizer-at-two-of-chebotarev
title: The Selmer order bound when ν is positive (second name)
kind: theorem
decl: GlobalTheory.T.boundModTwoUniformizerAtTwo_of_chebotarev
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BoundModTwoUniformizerAtTwoOfChebotarevStatement
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`bound_mod_two_of_hypothesis`](/entry/bound-mod-two-of-hypothesis/), which has the proof. It is step 3 of [good twists for all coprime powers](/entry/twist-all-powers-of-galois-cohomology-class-field/), where it gives the order bound `ThmC`. Below it are 366 declarations of the proof.

## Statement

Assume the eleven published statements `Cheb`, `PoitouTateTotallyComplex`, `CohDimTwo`, `TameLocal`, `LocalFiniteness`, `LocalTateDuality`, `LocalEulerChar`, `GlobalFiniteness`, `GlobalEulerChar`, `UnramifiedOrthogonality` and `Gen.ArchimedeanSignatureMatching`. The [parent entry](/entry/twist-all-powers-of-galois-cohomology-class-field/) describes them.

**Theorem.** For each datum $D$, each $N$, each twist system $X$ and each Bloch-Kato phase datum $\mathrm{bkP}$ over $X$, `ThmC bkP` holds. That is: at each twist index $i$ with $\nu_i > 0$, the determinant polynomials of the Selmer presentations at suitable auxiliary places have a coefficient of bounded degree whose valuation is at most $v(\ell_i^{\nu_i})$.

The entry [`bound_mod_two_of_hypothesis`](/entry/bound-mod-two-of-hypothesis/) states this in full and defines $\nu_i$.

## Proof

The proof is the tactic `first | exact @bound_mod_two_of_hypothesis | ...` (namespace shortened). The two statements are the same text.

## In the Lean code

The theorem is in [BoundModTwoUniformizerAtTwoOfChebotarevStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BoundModTwoUniformizerAtTwoOfChebotarevStatement.lean#L9). The name speaks of the prime 2 and of a uniformizer at 2. The statement is the case $\nu_i > 0$ for every prime $\ell_i$. For $\ell_i = 2$ this case always holds when $n = tr \ge 1$, but it can also hold for odd $\ell_i$. See [`bound_mod_two_of_hypothesis`](/entry/bound-mod-two-of-hypothesis/).
