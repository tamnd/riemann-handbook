---
id: zh-geo-of-semistable-reduction
title: The theta-level extension from semistable reduction
kind: theorem
decl: GlobalTheory.zhGeo_of_semistableReduction
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ZarhinGeometricOfSemistableReduction
covers: 1257
status: drafted
drafted_by: writer@claude
---
This theorem proves `ZHGeoSt` from one hypothesis, semistable reduction. It takes [the restatement of `zhGeo`](/entry/semi-abelian-scheme-uniformisation-exists-geometric/), which has nine hypotheses, and proves eight of them with theorems of the Lean code. The real content is in [`ZH.GeoHalf.zhGeo`](/entry/zh-geo/). The result goes to [the statement form](/entry/zarhin-geometric-of-semistable-reduction/) with the same type.

## Statement

**Theorem.** If `SemistableReductionSt` holds, then `ZHGeoSt` holds.

`SemistableReductionSt` is stated in [the entry above](/entry/zarhin-geometric-of-semistable-reduction/), and `ZHGeoSt` in [the entry for `zhGeo`](/entry/zh-geo/).

## Proof

The proof fills the other eight hypotheses of `semiAbelianScheme_uniformisation_exists_geometric` and passes $S$ along.

1. `homExtension_semiAbelian_dvr` proves `HomExtSt`. Let $T$ be a discrete valuation ring with fraction field $K$, and let $G, G'$ be semi-abelian schemes over $\operatorname{Spec} T$. Then each homomorphism $G_K \to G'_K$ of group schemes extends to exactly one homomorphism $G \to G'$. Its proof calls `existsUnique_hom_extension_semiAbelian_dvr` with a finiteness input from `card_torsion_abelianVariety`.
2. `allSixLaws` proves `Laws` to `Laws6`. The proof keeps the first five. They are bundles of facts on abelian schemes; `Laws` alone has 24 fields, among them `rigidity`, `cube`, `square`, `weil` and `weilNondeg`. We have not unfolded their statements.
3. `ZH.thmU_and_uTors` proves `ThmUSt` and `UTorsSt`. `ThmUSt` says: let $V$ be a complete DVR of characteristic zero, $A$ a polarized abelian variety over $\operatorname{Frac} V$, and $G$ a commutative semi-abelian scheme over $V$ whose closed fibre is an extension of an abelian variety by a split torus. Suppose $A$ satisfies `HypS`, and fix an isomorphism of group schemes $G_{\operatorname{Frac} V} \cong A$. Then there are degeneration data $D$ and a uniformisation of $G$ by $D$ that induces this isomorphism. `UTorsSt` says: for each such uniformisation, each algebraically closed field $F$ over $\operatorname{Frac} V$ and each $k \geq 1$, there is a map $f$ from the points `QkPt` of $D$ to the points of $A$ over $F$. It agrees with the relation `QkToAkU` of the uniformisation, it reaches each $k$-torsion point, its fibres are the classes of `QkPt.Equiv`, it is additive, and it takes the pairing `WeilQkIs` of $D$ to the Weil pairing of $A$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ZarhinGeometricOfSemistableReduction.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ZarhinGeometricOfSemistableReduction.lean#L19). The lemmas it calls:

- `homExtension_semiAbelian_dvr`, in [HomExtensionSemiAbelianDiscreteValuationRing.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/HomExtensionSemiAbelianDiscreteValuationRing.lean#L21). `HomExtSt` is in [HomExtSt.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/HomExtSt.lean#L18).
- `allSixLaws`, in [AllSixAbelianSchemeLawsHold.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/AllSixAbelianSchemeLawsHold.lean#L22).
- `ZH.thmU_and_uTors`, in [UniformisationExistenceAndTorsionStatements.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/UniformisationExistenceAndTorsionStatements.lean#L20). `ThmUSt` and `UTorsSt` are in [UTorsSt.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/UTorsSt.lean#L12).
- `T.semiAbelianScheme_uniformisation_exists_geometric`.

The shapes of `ThmUSt` and `UTorsSt` are those of the theory of degeneration data of Mumford and of Faltings and Chai (*Degeneration of Abelian Varieties*, Springer 1990, Chapters II and III). We have not unfolded `DegData`, `Unif`, `HypS` or `QkPt`, so we do not claim that they match the book.

The hypothesis `SemistableReductionSt` is not proved here, but the Lean code proves it elsewhere, as `GlobalTheory.SS.semistableReductionSt` in [SemistableReductionPpavPadicField.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemistableReductionPpavPadicField.lean#L19). The file name says "Zarhin", but the statement does not mention Zarhin or any construction that we can tie to his name.
