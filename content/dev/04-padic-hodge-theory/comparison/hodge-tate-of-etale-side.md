---
id: hodge-tate-of-etale-side
title: An injective Hodge-Tate pairing from the étale facts
kind: theorem
decl: CrystallineSemistableComparison.HT.hodgeTate_of_etale_side
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.HodgeTateResidues.HodgeTateComparisonSmoothProjective
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem only passes hypotheses along. It applies [ht_of](/entry/ht-of/) to four proved facts and keeps the fifth hypothesis, the étale facts, as its own. That entry has the content. Its use is in [the injective Hodge-Tate pairing](/entry/hodge-tate-comparison-smooth-projective/), which supplies the étale facts. Below it are 483 declarations.

## Statement

The models, the pairings $P$ (`HTPre`) and the conclusion `HodgeTateMapExists` are as in [the parent entry](/entry/hodge-tate-comparison-smooth-projective/) and [the Hodge-Tate comparison for good reduction](/entry/ht-bij-of/).

**Theorem.** Assume `EtSideS`: for each $\ell$ and $K$, the étale cohomology of models satisfies `EtSide` with respect to smooth models. That is, cup products exist, each $V^j$ of a smooth model has finite dimension, the connected smooth models satisfy duality in the top degree, and each smooth model is covered by finitely many connected smooth models whose pullbacks detect each class. Then for each $\ell$ and $K$ there is a pairing $P$ that is injective on every smooth model and in the top degree of every connected one.

## Proof

The proof is one line:

```
ht_of lvEx kFin dlog_class_exists_unique kTop h
```

The four facts are a level system for the crystalline base (`lvEx`), the finiteness and vanishing of the Hodge pieces (`kFin`), the existence and uniqueness of the dlog first Chern class (`dlog_class_exists_unique`), and the nonvanishing of $c^d$ for a tautological line bundle (`kTop`). We have not unfolded their proofs.

## In the Lean code

The theorem is in [HodgeTateComparisonSmoothProjective.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HodgeTateComparisonSmoothProjective.lean#L17). The inputs are in [LvLink.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/LvLink.lean#L14), [KFin.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/KFin.lean#L14) and [DlogClassExistsUnique.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/DlogClassExistsUnique.lean#L250), which also holds `kTop`. `EtSide` is in [EtSide.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/EtSide.lean#L54).

The hypothesis is `CrystallineSemistableComparison.EtSideS` from [CstSmoothOfEtSide.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/CstSmoothOfEtSide.lean#L16). A second definition with the same short name, `Out.EtSideS`, is in `CstSmooth.lean`. Two theorems are named `hodgeTate_comparison_smooth_projective`: the one in this file, with hypotheses `E4` and `E8`, and the one in `ClosedHT.lean`, which is the parent.
