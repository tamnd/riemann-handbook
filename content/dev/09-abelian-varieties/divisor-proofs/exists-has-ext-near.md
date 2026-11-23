---
id: exists-has-ext-near
title: A semi-abelian extension over an affine neighbourhood
kind: theorem
decl: GlobalTheory.Desc.exists_hasExt_near
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSemiAbelianExtensionNearPoint
covers: 645
status: drafted
drafted_by: writer@claude
---
This theorem proves [its statement form](/entry/exists-semi-abelian-extension-near-point/): near each point of a normal base, the abelian scheme extends to a semi-abelian scheme. It reduces the problem to an affine open $\operatorname{Spec} R$ with $R$ a noetherian normal domain, and passes it to [`hasExt_opensRange`](/entry/has-ext-opens-range/), in the same file.

## Statement

The hypotheses are those of [the semi-abelian extension from charts](/entry/descent-semi-abelian/). The conclusion: for each $s \in S$ there is an open $U \ni s$ such that $A|_{j^{-1}(U)}$ extends to a semi-abelian scheme over $U$, as group schemes.

## Proof

1. **An affine domain.** $S$ is noetherian and normal. So its irreducible components are open, and $s$ lies in one, $Z$. Choose an affine open $U = \operatorname{Spec} R$ with $s \in U \subseteq Z$. Then $U$ is irreducible and normal, so $R$ is a noetherian integrally closed domain.
2. **The affine case.** `hasExt_opensRange` gives the extension over the image of $\operatorname{Spec} R \to S$, which is $U$. Its proof, in the same file, goes as follows.
   - Since $j$ is dense, $X \cap U$ is a nonempty open of $\operatorname{Spec} R$. It contains a basic open $D(f)$ with $f \neq 0$.
   - The restriction of $A$ to $D(f)$ is still an abelian scheme with a relatively ample line bundle. Each chart of $(j, A)$ at a point of $U$ restricts to a chart of $(D(f) \to \operatorname{Spec} R, A|_{D(f)})$ (`Chart.nonempty_restrict`). Here one needs the generic point of $\operatorname{Spec} R'$ (for the complete ring $R'$ of the chart) to map into $D(f)$. This holds because the chart is flat and $\operatorname{Spec} R$ is irreducible.
   - [`extendsToSemiAbelian_away_of_charts`](/entry/extends-to-semi-abelian-away-of-charts/) extends $A|_{D(f)}$ to a semi-abelian scheme $G$ over $\operatorname{Spec} R$.
   - $G$ restricted to $X \cap U$ and $A|_{X \cap U}$ are two semi-abelian schemes that agree over the dense open $D(f)$. So they are isomorphic, by `semiAbelianHomExtension_holds`: over a noetherian normal base, a homomorphism of semi-abelian schemes over a dense open extends uniquely. Hence $G$ extends all of $A|_{X \cap U}$ (`HasExt.of_dense`).

The rest is bookkeeping with open immersions.

## In the Lean code

The theorem is at [ExistsSemiAbelianExtensionNearPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L176). The affine case `hasExt_opensRange` is at [line 111](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L111), `Chart.nonempty_restrict` at [line 85](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L85) and `HasExt.of_dense` at [line 27](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L27).

- `extendsToSemiAbelian_away_of_charts` is a second name for `Desc.hasExt_awayMap_of_charts`, which we have not unfolded. It carries most of the 645 declarations.
- `semiAbelianHomExtension_holds` proves `SemiAbelianHomExtension` at [GeometricallyConnectedSplitTorusAff.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SemiabelianTori/GeometricallyConnectedSplitTorusAff.lean#L15). Its statement is the extension property just given. We have not unfolded its proof.
- The irreducible component is made open by `IsNormalScheme.component`, which we have not unfolded.
