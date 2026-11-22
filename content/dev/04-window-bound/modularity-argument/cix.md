---
id: cix
title: The twisted trace identity on GL(4) with an Eisenstein term
kind: theorem
decl: UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.cix
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.SpectralOperatorNorms.Cix
covers: 601
status: drafted
drafted_by: writer@claude
---
This theorem proves `CIx`, the form of the trace identity for $\mathrm{GL}_4$ with one extra term. It is used in step 1 of [the proof of `indCs_of_gm`](/entry/ind-cs-of-gm/) and is the first hypothesis of [the induced spectrum on GL(4)](/entry/core-ind/). The proof only applies [`cix_of`](/entry/upper-theory-v-z-invariant-submodule-monic-polynomial-cix-of-2/) to two proved lemmas.

## Statement

Let $E$ and $F$ be totally complex, $\theta$ a twist on $\mathrm{GL}_4$ over $E$, and $\mathfrak{e}$, $\mathfrak{f}$ the spectral sides over $E$ (twisted by $\theta$) and over $F$ (untwisted), with a constant $c$ such that the geometric sides match (`GeoPair`). Let $\mathfrak{x}$ be a family (`Fam`) with parameters $(\Lambda, t)$, and suppose that no datum over $F$ has parameters whose base change is $(\Lambda, t)$.

**Theorem.** There is an isometry $N$ that intertwines the two operators $s(0)$ and $s'(0)$ of $\mathfrak{x}$, such that for each $x > 0$ and all large $j$:
$$\mathrm{tr}_{\mathfrak{e}}(\Lambda, t; x, j) + \tfrac12\, \mathrm{tr}_{\mathfrak{x}}(N; x, j) = c \cdot \mathrm{tr}_{\mathfrak{f}}(\text{parameters that base change to } (\Lambda, t); x, j).$$
The first term is the cuspidal trace at $(\Lambda, t)$. The second is the Eisenstein term: the trace of $N$ composed with the operators of $\mathfrak{x}$.

## Proof

The proof is the term `cix_of kernX truncCpt`. Here `kernX` is a truncation kernel estimate and `truncCpt` a compactness fact. The real content is in `cixOf`, which the entry of [`cix_of`](/entry/upper-theory-v-z-invariant-submodule-monic-polynomial-cix-of-2/) describes.

## In the Lean code

The theorem is one line in [Cix.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/Cix.lean#L5). `CIx` is in [KillExempt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/KillExempt.lean#L108). `kernX` is in [ProjInner.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/ProjInner.lean#L123) and `truncCpt` in [TruncCpt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/BorelHeckeBounds/HeckeShiftSums/TruncCpt.lean#L11). We have not unfolded `Side.tr` or `GeoPair`.
