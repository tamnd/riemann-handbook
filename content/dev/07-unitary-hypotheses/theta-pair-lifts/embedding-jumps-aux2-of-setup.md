---
id: embedding-jumps-aux2-of-setup
title: The bound at the primes q and d from the setup, restated
kind: theorem
decl: GlobalTheory.T.embedding_jumps_aux2_of_setup
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PolynomialBoundSetup
covers: 1325
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the bound at q and d from the setup](/entry/theorem-bqd-main-alt-alt/), and its proof only cites that theorem. Its user is [the closing of the family bound](/entry/nlink-close-main-alt-alt/), which takes from it a constant $C$ and a polynomial $Q$ and puts them in the constants of the family. The content is in [the Selmer length bound at twisted places](/entry/twisted-place-selmer-length-bound-of-local-duality/), through [the bound at q and d](/entry/theorem-bqd-main-alt-alt/).

## Statement

**Theorem.** There are a real $C$ and a polynomial $Q$ in three variables with the following property. Assume the seven hypotheses $\mathrm{Hyp}_2$. For each datum $D$, size data $L$ and hub datum $X$ with the setup `SetupAlt` for some $C_2$, the bound at q and d holds for the family $\rho$ of $X$, with $C$ and $Q$.

The bound at q and d is stated in [the entry above](/entry/theorem-bqd-main-alt-alt/).

## Proof

The proof is the term `TheoremBQD.main_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [PolynomialBoundSetup.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PolynomialBoundSetup.lean#L11). The proof is `first | exact @TheoremBQD.main_alt_alt | ...`, a tactic that tries three ways to apply the other theorem. The two statements are the same, word for word.

The name is not clear. "aux2" refers to the conclusion `EmbeddingTypeJumps.Conclusion2`, and the statement has no embedding and no jumps. The file name `PolynomialBoundSetup` is also the name of a different file in `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues`, which defines the polynomial $Q$.
