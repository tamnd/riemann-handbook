---
id: upper-theory-v-z-invariant-submodule-monic-polynomial-cix-of-2
title: The twisted trace identity from the kernel estimate and compact truncation
kind: theorem
decl: UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix_of
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.SpectralOperatorNorms.CixOf
covers: 449
status: drafted
drafted_by: writer@claude
---
This theorem proves the trace identity `CIx` of [the entry above](/entry/cix/) from two hypotheses: the kernel estimate `KernX` and the compactness `TruncCpt`. Its proof passes these two hypotheses, with fourteen proved lemmas, to the assembly lemma `cixOf`. It has no content of its own.

## Statement

**Theorem.** Assume:

1. `KernX`. Let $A, A'$ be the lines, $P$ the projection onto them, and $\theta$ a twist that commutes with $P$ and with truncation. Let $R(f) = R(a) M R(g)$ with $a, g$ smooth and $M$ an operator that commutes with $P$ and with the cuspidal projection $P_c$. Let the twisted kernel of $f$ vanish above height $e^{cT}$, and let $\Lambda$ be truncation at a large height $T$. Then $\Lambda R(f) \theta P \Lambda$ is of trace class, and the twisted integral of $f$ minus the cuspidal trace minus its trace has absolute value at most $C e^{NT} \lVert M(1 - P_c - P) \rVert + C e^{-N'T} \lVert M \rVert$.
2. `TruncCpt`. For each such datum, $\Lambda R(a) P$ is compact.

Then `CIx` holds.

## Proof

`cixOf` takes fourteen inputs: `ParEx`, `TrExp`, `EvVal`, `ValBc`, `KillEx2`, `KfBc`, `TruncSpec`, `SepPoly`, `OneSide`, `OneSideX`, `EvEx`, `Kill`, `KillExempt` and `FamEx`. The proof supplies each one from proved lemmas. `KernX` goes only into `oneSideX`, and `TruncCpt` goes only into `famEx`. The real content is in `cixOf` and in these lemmas. [`cix`](/entry/cix/) then removes the two hypotheses with `kernX` and `truncCpt`.

## In the Lean code

The theorem is at [line 13 of CixOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/CixOf.lean#L13). `cixOf` is in [FinsumSum.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/ChebyshevNormEstimates/FinsumSum.lean#L306). `KernX` is in [KillExempt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/KillExempt.lean#L130), and `TruncCpt` and the quantifier `ForAllC` are in [UnipotentBlockPairs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/UnipotentBlockMatrices/UnipotentBlockPairs.lean#L125).
