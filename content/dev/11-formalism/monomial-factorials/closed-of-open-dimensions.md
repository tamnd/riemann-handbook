---
id: closed-of-open-dimensions
title: Comparing the block dimension over the p-adic numbers and over the fraction field
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_dimensions
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.PositiveOfDimensionChange
covers: 2369
status: drafted
drafted_by: writer@claude
---
This theorem is the fifteenth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_open_base_dims`](/entry/closed-of-open-base-dims/) calls it. It adds a proved comparison of two dimensions to the bound `RestDirQ`, and passes the result on to [`closed_of_open_positive`](/entry/closed-of-open-positive/).

## Statement

The notation is that of [`theorem_A_closed_of_nine_open_bounds`](/entry/theorem-a-closed-of-nine-open-bounds/) and [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/): $V$ is the $\mathbb{Q}_p$-span of the module $S$ of the block datum $G$, and $S^O$ is the $O$-module of the datum $G^O$ over $O$, with $G = $ `gmB` $G^O$. `RestOpen6E D` is stated in [`closed_of_open_base_dims`](/entry/closed-of-open-base-dims/). Let $\mathrm{bRank} = \dim_K \langle S^O \rangle_K$ (`bRank`, that is `blockRank`).

- `RestDimBC`: $\dim_{\mathbb{Q}_p} V \le \mathrm{bRank}$.
- `RestDir`: $\sum_{x \in \mathrm{lv}} r_L(x) \le \mathrm{bRank}$.
- `RestOpen5E D`: as `RestOpen6E D`, with `RestDir` in place of `RestDirQ`.

All are quantified over $a_{\mathrm{top}} \in A^s$, $a_+ \in A$ and blocks $b$ with `Kept`.

**Theorem.** For each datum $D$, `RestOpen6E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `positive_of_dimension_change` proves `RestOpen5E D` from `RestOpen6E D`. It opens the nest with `thr_mono` and keeps `RestBCdim` and `RestPlusB`. It replaces `RestDirQ` by `RestDir`, through `restDir_of`: chain `RestDirQ` with `RestDimBC`.

`RestDimBC` holds with no hypothesis, by `restDimBC_proved`. Let $\iota \colon \mathbb{Q}_p \to K$ be the ring map `iotaX`, the extension to fraction fields of an embedding of $\mathbb{Z}_p$ into $O$. If $V$ has infinite dimension, its `finrank` is $0$ and there is nothing to prove. Otherwise take a $\mathbb{Q}_p$-basis of $V$. Applying $\iota$ to the coefficients sends $S$ into $S^O$ (`map_SSZ`), so it sends $V$ into $\langle S^O \rangle_K$. It also keeps linear independence (`li_map`). So the image of the basis is a $K$-independent family in $\langle S^O \rangle_K$, and $\dim_{\mathbb{Q}_p} V \le \mathrm{bRank}$.

Then `closed_of_open_positive` is applied. The rest is bookkeeping.

## In the Lean code

The theorem is in [PositiveOfDimensionChange.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/PositiveOfDimensionChange.lean#L23), with `RestOpen6` at line 10, `RestOpen6E` at line 14 and `positive_of_dimension_change` at line 18. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `restDir_of` and `RestDimBC`, in [RestDirOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestDirOf.lean#L31). `RestDir` is in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L140).
- `restDimBC_proved`, in [RestDimBCProved.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestDimBCProved.lean#L12), with `iotaX` in PadicIntegersEmbeddingMapPrime.lean, `map_SSZ` in MemIntPolIff.lean and `li_map` in LiMap.lean.

The new fact `RestDimBC` needs neither `HI` nor $C_M \ge 1$. The file and the lemma are named "positive of dimension change", but the step concerns the dimension bound `RestDir`, not the positive part `RestPlusB`, which passes through. The unused lemma `restDir_of_lvl` (see [`theorem_A_closed_of_nine_open_bounds`](/entry/theorem-a-closed-of-nine-open-bounds/)) proves `RestDir` from `RestLvlDim` directly, so it does that link and this one together.
