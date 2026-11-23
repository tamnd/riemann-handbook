---
id: local-cores
title: The local core facts, bundled
kind: theorem
decl: Formalism.FourierDecayAlt.P.HilbertSchmidtNorm.localCores
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.SecondDerivativeHolds
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem proves `LocalCores`, a conjunction of 32 propositions. It is a bundle: its proof is a tuple of 32 lemmas, one for each conjunct, and it adds nothing. [The applied pair bound](/entry/pb-applied/) gives it, with the companion bundle `globalCores`, to `t_PairBoundFromLocal`. The content is in the 32 lemmas, which have no entries of their own.

## Statement

The conjuncts that we have read are facts about kernels $k \colon \alpha \times \alpha \to \mathbb{C}$ that are positive semidefinite on a finite set $F$ (`PSDOn F k`), or about local systems built from such kernels. By role:

- Closure rules: `SchurProduct` says that a finite product $\prod_p k_p(x, y)$ of positive semidefinite kernels is positive semidefinite. This is the Schur product theorem (Horn and Johnson, *Matrix Analysis*, 2nd ed., Section 7.5). `ProductDomination` does the same for differences $\prod_p K_p - \prod_p k_p$, `DiagScale` for $a(x) a(y) k(x, y)$ with real $a$, and `BlockDiagPSD` for setting to $0$ the entries between different fibres of a map.
- Assembly rules: `KernelOfLocal` and `GlobalOfLocal` build a global kernel or a global system that is `Ok` from local pieces, given product and scaling rules.
- Bookkeeping: `PSDAgree` says that three definitions of a positive semidefinite kernel in the code agree.

The other conjuncts come from `StatementJ` (product, scaling, phase, outside, pullback, unit head, majorant and axiom rules for local systems, and `LocalKernelPSD`), from `TC` (two domination facts) and from `A5` (nine facts on Gram kernels, single blocks and theta functions, ending with `LemmaAAssemble`). We have not unfolded them.

**Theorem.** `LocalCores` holds.

## Proof

Each conjunct is one lemma, from `jx_pSDAgree` to `latticeAverage_of_gram`. There is no other step.

## In the Lean code

The theorem is in [SecondDerivativeHolds.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SecondDerivativeHolds.lean#L13). `LocalCores` is in [StatementPB.lean](lean:Formalism/HermitianCurvature/StatementPB.lean#L337). The kernel facts above are in [StatementJ.lean](lean:Formalism/HermitianCurvature/StatementJ.lean#L19) (lines 19, 617 to 628, 755, 780 and 891). The user is `pbApplied` in [TheoremS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremS.lean#L19).

Several conjuncts are implications from other conjuncts: `KernelOfLocal` assumes `SchurProduct` and `DiagScale`, and `GlobalOfLocal` assumes `ProductLemma` and `ScaleOk`. The bundle proves each of them as an implication and does not use one conjunct to prove another.

The names do not describe the content. The file is called `SecondDerivativeHolds` and the namespace is `HilbertSchmidtNorm`, but the file holds only this bundle and `globalCores`. No second derivative and no Hilbert-Schmidt norm appear in it.
