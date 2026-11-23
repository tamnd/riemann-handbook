---
id: row-a-at-g-at-built-alt
title: The arithmetic row at generator places, at built points
kind: theorem
decl: GlobalTheory.Fc.row_aAtG_at_built_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowAAtGAtBuilt
covers: 585
status: drafted
drafted_by: writer@claude
---
This theorem proves the row `aAtG` of the record `AllRowsAlt` with no hypothesis. It is one of the rows of step 3 of [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), and it becomes the field `aAtG` of [HypsAlt](/step/hyps-alt-def/). The proof puts the slot in the form that [`holds_at_bundlePoints_of_trueColumns`](/entry/holds-at-bundle-points-of-true-columns/) asks for. That lemma dominates 574 of the 585 declarations below this theorem, and the content is in [`row_aAtG_of_rowPin`](/entry/row-a-at-g-of-row-pin/).

## Statement

Let $\mathcal S$ be slots with $\mathcal S.R_x = $ `RX`, and let $L_k$ be any linkage of bundles. Write `Lg1`, `IsBuiltE 𝒮` and `IsGoodE 𝒮` as in [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/).

`H_aAtG 𝒜` says: it is [closed](/step/closed-def/) on the class `W3 𝒜` that there is a constant $C_1$ with two properties. First, eventually in $x$, at each index of the family, `UsedTuplesBoundByConstant (D x i) (L x i) errX C1` holds. This says: for $i \in \{0, 1\}$, each place $w$ with `Over D i w`, each word $u$ with $T(u)$ different from the residue characteristic of $w$, each used tuple $\mu$ and each relevant $\varphi$ and $F$, the period coordinate is the image of some $y \in L$ with $y = 0$ or

$$v_w(y) \ge -\sum_j v_{ij}(u, w) - C_1\, c_{\mathrm{err}}(D, L).$$

Here $v_w$ is `vG D w`, the sum is over the lifts $j$, and $v_{ij}$ and $c_{\mathrm{err}}$ come from the error data `errX`.

Second, `familySizeBoundAtTypePrime F C1`. We have not unfolded the second property.

**Theorem.** `Lg1 KPx (IsBuiltE 𝒮) (IsGoodE 𝒮) (fun S => Row S Lk (fun 𝒜 _ => H_aAtG 𝒜))` holds.

## Proof

1. Take the large base slot $R$ that is always true; `largeBaseProperty_true` gives its large base condition.
2. `holds_at_bundlePoints_of_trueColumns` reduces the row to one claim: each point of the slot `IsGoodE 𝒮` has a part (`HasPart`) at which `RowPin` holds for each tuple $a$. `RowPin` asks, for each word $u$, for a linear isomorphism from the space of the period at $u$ and $a$ to the ambient space at $a$, with four compatibilities.
3. A good point is built, so it carries a built datum $b$. `builtC_hasPart` gives the part. Rewrite $b.\mathrm{rx}$ by the hypothesis $\mathcal S.R_x = $ `RX`; then `rowFormsMatchPeriodMap_of_furtherProperties` gives `RowPin`.

## In the Lean code

The theorem is at [RowAAtGAtBuilt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowAAtGAtBuilt.lean#L10). `H_aAtG` is at [LevelPrimeColumnValuationsAtBundlePoints.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LevelPrimeColumnValuationsAtBundlePoints.lean#L21), `UsedTuplesBoundByConstant` at [AdmissibleAtGeneratorPlaces.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L25), `RowPin` at [JetSplitAmb.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JetSplitAmb.lean#L35).

The lemmas: `largeBaseProperty_true`, `holds_at_bundlePoints_of_trueColumns` (a renaming of `row_aAtG_of_rowPin`), `positionOf_mono`, `builtC_hasPart`, `rowFormsMatchPeriodMap_of_furtherProperties` (a renaming of `RX.rowPin_of_rx`).

Odd points:

- The row `H_aAtG 𝒜` does not mention the selection, so $L_k$ plays no part.
- The large base condition asks for nothing, as noted in [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/).
