---
id: arithmetic-hilbert-samuel-bound
title: The arithmetic Hilbert-Samuel bound from the quoted theorems, second name
kind: theorem
decl: GlobalTheory.T.arithmeticHilbertSamuelBound
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArithHilbertSamuelBoundOfQuotedTheoremsStatement
covers: 688
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/). Its only user is [hsClaimS_component_geo](/entry/hs-claim-s-component-geo/), which applies it to the hermitian data of a component at line 32 of its file. Below this theorem are 688 declarations.

## Statement

`Quoted` is a structure with eight fields, of types `KawamataViehweg`, `L2ExtensionLogCanonical`, `SerreHolomorphicSections`, `NefNumerics`, `ChowFormExists`, `ChowFormIntExists`, `ChowFormHyperplaneSection` and `ProperIntersectionLength`. The names point to quoted theorems of the literature. We have not unfolded these types.

**Theorem.** `Quoted` implies `GeoBound`. That is: for every number field $F$, every hermitian data $X$ over $F$ and every $\Lambda_0$ with `GeoHyp X Λ₀`, and every height $h$ of the image of $X$, the inequality `HSClaimS` holds with the constant $26$ and the numbers $T$, $D$, $n$, $\Lambda$, $\beta$, $\Lambda_D$, $\Lambda_T$, $\log\Lambda_0$, `del`, $h$, $d$ and $\deg M_T$ of $X$.

The full form of `GeoBound` and of `HSClaimS` is in [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/).

## Proof

The proof is `exact geoBound_of_quoted'`, inside a `first | ...` that tries three forms of the same call.

## In the Lean code

The theorem is at [ArithHilbertSamuelBoundOfQuotedTheoremsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelBoundOfQuotedTheoremsStatement.lean#L13). The theorem has no content of its own. The proof of [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/) is itself a short assembly, and the bound is proved in `HSShortTop.geoBound_of_abstract`.
