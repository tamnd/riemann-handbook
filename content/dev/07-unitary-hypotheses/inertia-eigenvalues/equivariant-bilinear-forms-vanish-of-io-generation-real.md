---
id: equivariant-bilinear-forms-vanish-of-io-generation-real
title: Equivariant forms on the Fock space vanish if they vanish on the lowest types, the statement form
kind: theorem
decl: GlobalTheory.T.equivariant_bilinearForms_vanish_of_io_generation_real
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.EquivariantBilinearFormsVanishOfIoGenerationRealStatement
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`forms_vanish_of_io`](/entry/forms-vanish-of-io/) and proves it by calling that theorem. Its only user is [`gen`](/entry/gen/), which applies it to the family of forms given by the downward theta integral, one form for each point $g$ of the adelic group of $W$.

## Statement

Fix a datum $R$ (`RealDat D A Ks`) with a face $F$, a step $i$ of the chain and an index $t$. Let $\mathcal P$ be the polynomial ring of the Fock model at step $i$, let $(E, \rho)$ be the finite-dimensional coefficient representation `R.cV i`, and let $\iota$ be the map `R.ioP i` from the lowest types into $\operatorname{Hom}(E, \mathcal P)$. Assume `Given R F` and `R.FullP`. Let $(B_j)_{j \in I}$ be bilinear forms on $\mathcal P \times E^*$ that are equivariant for the real points of $U(V)$, whose common kernel is stable under the real Lie algebra of $U(W)$, and that vanish on the image of $\iota$. Then each $B_j$ is zero.

## Proof

The proof is `first | exact @GlobalTheory.GenByIo.forms_vanish_of_io | ...`. It applies that theorem. The statements are identical.

## In the Lean code

The theorem is in [EquivariantBilinearFormsVanishOfIoGenerationRealStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EquivariantBilinearFormsVanishOfIoGenerationRealStatement.lean#L18). The target is in [EquivariantBilinearFormsVanishOfIoGenerationReal.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EquivariantBilinearFormsVanishOfIoGenerationReal.lean#L21).
