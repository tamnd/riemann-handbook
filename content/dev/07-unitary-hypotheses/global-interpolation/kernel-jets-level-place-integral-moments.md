---
id: kernel-jets-level-place-integral-moments
title: The integral jet moments, a second name
kind: theorem
decl: GlobalTheory.T.kernelJets_levelPlace_integralMoments
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.KernelJetsLevelPlaceIntegralMomentsStatement
covers: 1600
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the integral jet moments](/entry/jet-moments/). That entry has the content. Its user is [the five kernel laws on the true chains](/entry/laws-true-fam/), which passes it to the two kernel bounds `trueChainKernels_bound_conjugatePrimePlaces` and `trueChainKernels_bound_levelPrimePlaces`. Those bounds give the laws `KerBar` and `KerP`.

## Statement

**Theorem.** `JetMoments` holds.

`JetMoments` says: for each admissible datum, each prime $T(u)$ of the datum prime to the norm of the curve ideal, each place $w$ and each embedding $\iota$ into $\mathbb{C}_{T(u)}$ that induces $w$, there are unit weights $u_\tau$ such that the images under $\iota$ of the jet sums lie in the closure of the integral combinations of the point tables, at the places that are seen and at the places that are not seen. It is stated in full in [the integral jet moments](/entry/jet-moments/).

## Proof

The proof applies `GlobalTheory.MomTop.jetMoments`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [KernelJetsLevelPlaceIntegralMomentsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/KernelJetsLevelPlaceIntegralMomentsStatement.lean#L7). The proof is a `first | exact ... | ...` combinator with three tries, each with the same lemma. Line 6 sets `maxHeartbeats 1000000`, which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames the theorem there.
