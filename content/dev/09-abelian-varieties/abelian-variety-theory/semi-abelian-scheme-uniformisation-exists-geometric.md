---
id: semi-abelian-scheme-uniformisation-exists-geometric
title: Extending a theta-level abelian scheme over a projective model (statement)
kind: theorem
decl: GlobalTheory.T.semiAbelianScheme_uniformisation_exists_geometric
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.SemiAbelianSchemeUniformisationExistsGeometricStatement
covers: 1256
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`ZH.GeoHalf.zhGeo`](/entry/zh-geo/), which has the real content. Its proof only calls that theorem. Its one user is [`zhGeo_of_semistableReduction`](/entry/zh-geo-of-semistable-reduction/), which proves all hypotheses but semistable reduction.

## Statement

Suppose the following nine statements hold.

- For semi-abelian schemes $G, G'$ over a discrete valuation ring $T$ with fraction field $K$, each homomorphism of group schemes $G_K \to G'_K$ is the restriction of exactly one homomorphism $G \to G'$.
- `SemistableReductionSt`: semistable reduction for polarized abelian varieties over finite extensions of $\mathbb{Q}_p$.
- `ThmUSt`: existence of degeneration data and a uniformisation for a semi-abelian scheme over a complete DVR of characteristic zero.
- `Laws`, `Laws2`, `Laws3`, `Laws4`, `Laws5`: five bundles of facts on abelian schemes.
- `UTorsSt`: the torsion points of the generic fibre, read off from the degeneration data.

Then `ZHGeoSt` holds: an abelian scheme with a theta structure of level $rN$ over an open set $U_0$ of a normal projective model $Z$ extends to a semi-abelian scheme over $Z$ with a cubical line bundle and theta sections that embed it. The [entry for `zhGeo`](/entry/zh-geo/) unfolds `ZHGeoSt`, and [the next entry](/entry/zh-geo-of-semistable-reduction/) unfolds the hypotheses.

## Proof

The proof is `ZH.GeoHalf.zhGeo`.

## In the Lean code

The theorem is in [SemiAbelianSchemeUniformisationExistsGeometricStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemiAbelianSchemeUniformisationExistsGeometricStatement.lean#L19). The proof is the tactic `first | exact @GlobalTheory.ZH.GeoHalf.zhGeo | ...`. The two statements are identical, so the first `exact` closes the goal.

The name says that a uniformisation of a semi-abelian scheme exists. The conclusion `ZHGeoSt` is larger: the uniformisation is one field, `unif`, of the structure `ZHOut`, which also asks for the extension of the group, the line bundle, the theta sections and a projective immersion.
