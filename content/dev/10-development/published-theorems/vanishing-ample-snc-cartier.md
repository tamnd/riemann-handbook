---
id: vanishing-ample-snc-cartier
title: Kawamata-Viehweg vanishing, from a divisor on an snc boundary to its components
kind: theorem
decl: GlobalTheory.Div.SncBoundary.vanishing_ample_snc_cartier
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.SncBoundaryAmpleDecomposition
covers: 593
status: drafted
drafted_by: writer@claude
---
This theorem proves the vanishing statement of its second name [`snc_boundary_ample_decomposition`](/entry/snc-boundary-ample-decomposition/), which the [vanishing theorem on a log resolution](/entry/vanishing-log-res-floor/) uses. The input is an effective divisor $\Gamma$ with support in an snc boundary $B$. The proof writes $\Gamma$ as a sum $\sum_j b_j D_j$ of the prime components of $B$, and then calls the vanishing theorem for a relative snc family of line bundles, [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/). Below this theorem are 593 declarations.

## Statement

The statement is the one in [`snc_boundary_ample_decomposition`](/entry/snc-boundary-ample-decomposition/): $k$ a field of characteristic $0$, $Y$ integral, smooth of dimension $n$ and projective over $k$, $B$ a closed set with snc reduced ideal, $\Gamma$ effective with support in $B$ and $\operatorname{mult}_z \Gamma < e$ for all $z$, $A$ ample, and $e[Q] = e[K_Y] + [\mathcal{O}(\Gamma)] + [A]$ in $\operatorname{Pic} Y$. Then $H^i(Y, Q) = 0$ for $i > 0$.

Here $\operatorname{mult}_z$ is the order of the local equation of $\Gamma$ at $z$ when $z$ is a point of codimension $1$, and $0$ at the other points.

## Proof

1. $Y$ is smooth over a field, so it is normal.
2. **The components of $B$.** `SncComp.relSnc_components` gives prime divisors $D_1, \dots, D_r$ with generic points $w_1, \dots, w_r$ (distinct), such that $\operatorname{mult}_{w_j} D_j = 1$, $\operatorname{mult}_v D_j = 0$ for $v \neq w_j$, and each point of codimension $1$ in $B$ is some $w_j$. It also gives sections $\sigma_j$ of $\mathcal{O}(D_j)$ that form a relative snc family over $k$ (the condition `RelSnc`, defined in [`vanishing_ample_snc_charZero`](/entry/vanishing-ample-snc-char-zero/)).
3. **The decomposition.** Since $\Gamma$ is effective, its multiplicities are $\geq 0$. Put $b_j = \operatorname{mult}_{w_j} \Gamma$. Then $\Gamma - \sum_j b_j D_j$ has multiplicity $0$ at each $w_j$, and also at each other point: a point of codimension $1$ where $\Gamma$ has nonzero multiplicity is in the support of $\Gamma$, so in $B$, so it is some $w_j$. On a normal integral scheme a Cartier divisor with all multiplicities $0$ is $0$, because the local ring at a point of codimension $1$ is a discrete valuation ring. So $\Gamma = \sum_j b_j D_j$.
4. **The bounds.** At the generic point of $Y$ the multiplicity is $0$, so $0 < e$. Also $b_j < e$ for each $j$.
5. Substitute the decomposition in the relation in $\operatorname{Pic} Y$. This gives $e[Q] = e[K_Y] + \sum_j b_j [\mathcal{O}(D_j)] + [A]$, and `vanishing_ample_snc_charZero` with $r = e$ gives the vanishing.

## In the Lean code

The theorem is in [SncBoundaryAmpleDecomposition.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SncBoundaryAmpleDecomposition.lean#L110). The lemmas it calls:

- `isReduced_isNormalScheme_isLocallyNoetherian_of_smooth_over_field`, for step 1.
- `GlobalTheory.SncComp.relSnc_components`, in [ExistsPrimeDivisorsSncBoundary.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/ExistsPrimeDivisorsSncBoundary.lean#L154), for step 2.
- Three private lemmas of the same file: `cartierDiv_mult_nonneg_of_eff`, `cartierDiv_eff_of_mult_eq_zero` and `cartierDiv_eq_zero_of_mult_eq_zero`, for step 3.
- `GlobalTheory.Div.vanishing_ample_snc_charZero`, for step 5.

The goal is stated for $\mathcal{O}_Y \otimes Q$ (`twist (structureModule Y) Q`) and the last call proves it for the sheaf of sections of $Q$ (`LB.toMod`). Lean accepts the final `exact`, so the two sheaves agree by unfolding definitions. The hypothesis `IsLocallyNoetherian Y` is redundant: the lemma of step 1 also proves it.
