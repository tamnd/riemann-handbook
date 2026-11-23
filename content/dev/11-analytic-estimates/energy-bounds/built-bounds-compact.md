---
id: built-bounds-compact
title: The built bounds, from the top truncation
kind: theorem
decl: Formalism.FourierDecayAlt.P.built_bounds_compact
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.BuiltBoundsCompact
covers: 1013
status: drafted
drafted_by: writer@claude
---
This theorem proves `BuiltBounds2Cpt` with no hypothesis. It is a relay: it applies one theorem to one proved fact. Its only user is [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/), which is a renaming of this theorem. The real content is in [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/).

## Statement

**Theorem.** `BuiltBounds2Cpt` holds.

`BuiltBounds2Cpt` is stated in words in [the entry above this one](/entry/pb-built-bounds2-cpt/). In short: if `ThmPActualCpt` holds, then for each $C_b$ there are $C_c$ and $C_4 \ge 1$ such that each leading-form setting with these constants (`IsLeadingFormSetting`) satisfies five groups of local bounds: positivity (`ThmPPos`), `IntAll`, the wave bounds, the lift bounds and the sum form `SumFormConcrete` with constant $C_4$.

## Proof

The proof is one line:

```
pb_builtBounds2Cpt_of_mkTop top_truncation_of_averages
```

`top_truncation_of_averages` proves `MkTop`. It applies `CutMK.mkTop_of_avgs` to a right and a left average formula (`right_average_formula`, `left_average_formula`). [`pb_builtBounds2Cpt_of_mkTop`](/entry/pb-built-bounds2-cpt-of-mk-top/) turns `MkTop` into `BuiltBounds2Cpt`. The entry for that theorem states `MkTop`.

## In the Lean code

The theorem is in [BuiltBoundsCompact.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompact.lean#L6). `top_truncation_of_averages` is in [CutEXMkTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEXMkTop.lean#L259), and `BuiltBounds2Cpt` in [ArchimedeanUniformConstantsCompactSupport.lean](lean:Formalism/HermitianCurvature/ArchimedeanUniformConstantsCompactSupport.lean#L13).

The size of this theorem is 1,013, and that of `pb_builtBounds2Cpt_of_mkTop` is 1,012. So the subtree of `top_truncation_of_averages` is not counted here. The reason: `head_top` in [RadialExhaustion.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialExhaustion.lean#L6) also uses it, as `pb_headTop_of_mkTop top_truncation_of_averages`, and `head_top` has other users. The chain of three theorems through `MkTop` is therefore the same as the single term `built_bounds_compact_of_head_top head_top`.
