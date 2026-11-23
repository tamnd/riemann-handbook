---
id: exists-true-volume-stage-column-choice-step
title: A true volume stage for each pinned column (an instance)
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolumeStage_columnChoiceStep
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsGIs
covers: 471
status: drafted
drafted_by: writer@claude
---
This theorem is a special case of [`exists_trueVolume_stage_of_any_column_choice`](/entry/exists-true-volume-stage-of-any-column-choice/), which has the content. It is used in the proof of [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses](/proof/unitary-hypotheses/). Below it are 471 declarations of the proof.

## Statement

**Theorem.** Eventually in the context, for each pinned column $w$ over a base $B$, there is a stage $G$ (a `GJStage` over the columns of $w$) that satisfies `GIs2`.

`GIs2 K w G` says: at each later stage built on $G$, the volumes are tied (`VolTieG`), the gate numbers are right (`GatNum`), and there is column data at the split primes (`ColumnDataSplitPrimes`). The [general form](/entry/exists-true-volume-stage-of-any-column-choice/) explains each of these.

"Eventually" is the form `StepW Pinned`: the claim holds at large bases in the sense of `EvLgG`, for each column $w$ with a pin (`Nonempty (ColPin w)`).

## Proof

The proof is one term: `exists_trueVolume_stage_of_any_column_choice Pinned`. The general lemma holds for any property $p$ of columns in place of `Pinned`.

## In the Lean code

The theorem is in [ExistsGIs.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGIs.lean#L162). The hypothesis `Pinned` is vacuous here. The general lemma never uses its property $p$: its proof starts with `StepW.of_all` and drops the argument for $p$. So the same conclusion holds for every column, pinned or not. The proof uses only that the context is over the base (`K.Over B.toPre`).
