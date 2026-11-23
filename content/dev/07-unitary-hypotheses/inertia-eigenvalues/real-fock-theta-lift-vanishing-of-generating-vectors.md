---
id: real-fock-theta-lift-vanishing-of-generating-vectors
title: Downward integrals that vanish on the lowest types vanish on all Fock vectors, the statement form
kind: theorem
decl: GlobalTheory.T.realFockThetaLift_vanishing_of_generating_vectors
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RealFockThetaLiftVanishingOfGeneratingVectorsStatement
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem is a second name with no content of its own. It states the result of [`gen`](/entry/gen/) and proves it by calling that theorem. Its only user is [`genInf`](/entry/gen-inf/), in step 2 of its proof.

## Statement

Use the notation of [`genInf`](/entry/gen-inf/) and [`forms_vanish_of_io`](/entry/forms-vanish-of-io/): the downward integral $d(y, f, l, g)$, the Fock vectors $\phi_P$ for $P \in \mathcal P$, the coefficient space $E$ and the map $\iota$ (`R.ioP i`) from the lowest types $L$ to $\operatorname{Hom}(E, \mathcal P)$. Assume `Given R F` and `R.FullP`. Let $y \in H_V$ with $d(y, \phi_{\iota(x)(w)}, l, g) = 0$ for all $x \in L$, $w \in E$, $l \in E^*$ and $g \in U(W)(\mathbb A)$. Then $d(y, \phi_P, l, g) = 0$ for all $P \in \mathcal P$, $l$ and $g$.

## Proof

The proof is `first | exact @GlobalTheory.GenRealFock.gen | ...`. It applies that theorem. The statements are identical.

## In the Lean code

The theorem is at [RealFockThetaLiftVanishingOfGeneratingVectorsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealFockThetaLiftVanishingOfGeneratingVectorsStatement.lean#L18). The target is at [RealFockThetaLiftVanishingOfGeneratingVectors.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealFockThetaLiftVanishingOfGeneratingVectors.lean#L93). The file sets `maxHeartbeats` to 1,000,000 for a proof of one line.
