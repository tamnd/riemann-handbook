---
id: parts
title: The thirty-one facts behind the surjectivity of the Hodge-Tate map
kind: theorem
decl: CrystallineSemistableComparison.Onto.parts
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.HodgeSurjectivity.HtBijOf
covers: 999
status: drafted
drafted_by: writer@claude
---
This theorem fills in the 31 fields of the structure `Parts`, which [the Hodge-Tate comparison for good reduction](/entry/ht-bij-of/) uses to prove that the Hodge-Tate map is surjective. It has no argument of its own: each field is a lemma proved elsewhere. Below it are 999 declarations, nearly all of the 1,058 below that theorem.

## Statement

`Parts` is a conjunction of 31 statements. Twenty are facts, and eleven are implications between other facts. By subject:

1. Sites and covers. The subsites over opens and over a closed subscheme are cosieves, compatible with intersection and base change (`SiteLaws`). Pullback along a monomorphism (`OnIso`) and restriction to a Zariski cover (`ZarAbs`) give isomorphisms on cohomology. A map of systems of complexes that is bijective on each nonempty intersection of a cover is bijective on the whole space, a Mayer-Vietoris statement (`MVBij`). With `OneSurj` and `CovDesc`, these are the descent facts.
2. Kähler forms. On an affine open with $d$ coordinates, the cohomology in weight $a$ is the module of $a$-forms $\Omega^a$ in degree $a$, and $0$ in other degrees (`AffOm`). The others are `OmNat`, `FormLaws`, `DWedge`, `DLog`, `OmKun`, `FormCup` and `FirstChernCoboundary`.
3. Charts and cup products: `ChartLaws`, `ChartBij`, `DivCover`, `IsoBij` and `CupLaws`.
4. Lower dimension. Each smooth model is a retract of a smooth model of relative dimension two more (`Retract`).
5. Implications: `ZarRelOf`, `AffRelOf`, `RelLiftOf`, `RelInjOf`, `ConeKillOf`, `RelKillOf`, `KunAffOf`, `SlantOf`, `KillOf3`, `OntoOf3` and `OntoLow`. For example, `OntoLow` says that `CupLaws`, `Retract` and `HodgeTateSurjectiveOfTopDegreeInjective` give `OntoAll`, the surjectivity for all smooth models.

We have not unfolded most of these statements. The descriptions above come from the definitions that we read.

## Proof

Each field is a named lemma. Some are applied to others: `div` is `divisor_cover_of_chart_laws chartLaws_pf`, `inj` is `relInjOf_pf topRes_pf`, and `kill` is `relKillOf topRes_pf formUniq_pf omRes_pf`. The field `bij` is `chartBij_of` applied to twelve facts, most of them other fields. The rest is bookkeeping.

## In the Lean code

The theorem is in [HtBijOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HtBijOf.lean#L43), and `Parts` is in [OntoAllOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/OntoAllOf.lean#L6). In the same file, `Parts.hodgeKill`, `Parts.slant'` and `ontoAll_of` combine the fields. The field types are in [CosieveRes.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/CosieveRes.lean#L86), [CosieveBot.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/CosieveBot.lean#L74), [FormLaws.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/FormLaws.lean#L35), [FirstChernCoboundary.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/FirstChernCoboundary.lean#L16), [HodgeKill.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HodgeKill.lean#L63), [TowerRallisLemma.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/TowerRallisLemma.lean#L35) and [HodgeTateFromSandwich.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HodgeTateFromSandwich.lean#L35). The file name `TowerRallisLemma` does not match its content: it holds `OntoOf3` and `KillOf3`. Many proofs are imported from the folder `AutomorphicSpectrum/Proofs/BlockDecomposition`, a name unrelated to p-adic Hodge theory.
