---
id: built-bounds2-cpt-of-leaves
title: The built bounds from their leaves
kind: theorem
decl: Formalism.FourierDecayAlt.P.PBASM.builtBounds2CptOfLeaves
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.BuiltBoundsCompactOfLeaves
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem reduces `BuiltBounds2Cpt` to eight inputs, its leaves. It derives four more local bounds from these inputs and gives eleven facts to the assembly `builtBounds2CptOfParts`. Its second name is [`built_bounds_compact_of_leaves`](/entry/built-bounds-compact-of-leaves/), which [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/) calls with the eight inputs. That entry lists the inputs and the lemmas that prove them; this entry does not repeat them.

## Statement

Write $A$ for the proposition `ThmPActualCpt`, which we do not unfold. `BuiltBounds2Cpt` is the implication from $A$ to the five bounds on a leading-form setting that are stated in [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/).

**Theorem.** Suppose that `RadHead`, `HeadTop`, `DegLift`, `TopLocB`, `DegTop`, `TopRatio` and `GermPartsC` hold, and that $A$ implies the uniform decay bound `DecayUnif`. Then `BuiltBounds2Cpt` holds.

Here `DecayUnif` is the version in the namespace `PBASM`: for each constant $C_b$ there is $C_c$ such that, on each leading-form setting with these constants, the local Gram entries of the cut functions at the points $h \cdot (1, c)$ and $h' \cdot (1, c)$ are bounded by $C (1 + |c|)^{-3}$, and their integrals against `psiL` are bounded by $C (1 + |l|)^{-3}$, with $C$ uniform in the cut index $n$.

## Proof

Assume $A$. The proof builds four bounds that the assembly needs.

1. The standard pairing decay `PStdC` follows from $A$, `RadHead` and `HeadTop` by `pStdC_of`, which is `PBO.pStdCpt_of_heads`.
2. The integral bound `IntB` follows from `PStdC` and `DecayUnif` by `integral_bound_of_parts`.
3. The wave bound `WaveLocB` follows from $A$ and `PStdC` by `waveLocB_of_cpt`. It takes $C_c = 28e$ and applies `wave_local_positive_compact_support`.
4. The lift bound `LiftLocB` follows from $A$ and `DegLift` by `liftLocB_of_cpt`. It applies `lift_local_positive_compact_support`, which gives weights $\Lambda(b, s, v)$ with $0 \le \Lambda \le \mathrm{sz}$ only for $b, s \ge 1$ and $b + s \le r + 1$. The proof sets $\Lambda = 0$ outside this range, so that $\Lambda \ge 0$ holds for all $b, s$.

Then `germLocB_of` gives the germ bound `GermLocB` from `IntB` and `GermPartsC`. The theorem applies `builtBounds2CptOfParts` to these five bounds, to `TopLocB`, `DegTop`, `TopRatio` and `DecayUnif`, and to three proved facts: `positivity_bound`, `vector_valued_types` and `thrPos` (positive thresholds). `builtBounds2CptOfParts` only fixes $A$ and calls `core`. `core` does the analysis: it takes the maximum of the constants $C_c$ of all inputs and passes to the limit along the cut sequence. We have not read `core` in full.

## In the Lean code

The theorem is in [BuiltBoundsCompactOfLeaves.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L45), with `waveLocB_of_cpt` and `liftLocB_of_cpt` at [lines 14 and 20](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L14). The lemmas it calls:

- `pStdC_of` in [GramLocSetCApp.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/GramLocSetCApp.lean#L22);
- `integral_bound_of_parts` in [IntegralBoundOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/IntegralBoundOfParts.lean#L145);
- `germLocB_of` and `GermPartsC` in [WaveLocBOf.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/WaveLocBOf.lean#L15);
- `builtBounds2CptOfParts` and `core` in [BuiltBoundsCompactOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfParts.lean#L263), with `DecayUnif` at [line 84](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfParts.lean#L84).

`TopLocB` is itself an implication from `DegTop`, `VecVTypes` and `TopRatio` ([TopRatio.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TopRatio.lean#L40)). The theorem passes `TopLocB` to `core` unchanged.
