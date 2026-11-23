---
id: closed-of-open-directions
title: The averaged bad-share bound from four open bounds
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_directions
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ThresholdsMonoNormalized
covers: 2317
status: drafted
drafted_by: writer@claude
---
This theorem is a link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_open_positive`](/entry/closed-of-open-positive/) calls it. It composes two implications and has no mathematical content of its own. The content is in [`openE_of_open4`](/entry/open-e-of-open4/) and [`restTM_closed`](/entry/rest-tm-closed/).

## Statement

`RestOpen4E D` and `RestOpenE D` are stated in [`openE_of_open4`](/entry/open-e-of-open4/).

**Theorem.** For each datum $D$, `RestOpen4E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

The proof is one term:

```
closed_of_open_conditions D (openE_of_open4 D h)
```

`openE_of_open4` turns `RestOpen4E D` into `RestOpenE D`. Then `closed_of_open_conditions` proves the bad-share bound from `RestOpenE D`. Its proof adds three proved bounds with `restAllE_of_open`: `RestFree` from `restFree_proved`, a ratio bound from `ratioCondition_of_segFacts` and a depth bound from `restDepth_proved`. It then applies `theorem_A_closed_of_all_remaining_bounds`, which we have not followed.

## In the Lean code

The theorem is in [ThresholdsMonoNormalized.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ThresholdsMonoNormalized.lean#L50). `closed_of_open_conditions` and `restAllE_of_open` are in [ClosedOfOpenConditions.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfOpenConditions.lean#L45), lines 34 to 46.

The name speaks of directions. The direction bound `RestDir` is still an open hypothesis here, and it passes through `openE_of_open4` unchanged.
