---
id: exists-true-volume-stage-of-any-column-choice
title: A stage with the true volumes and local gates for each column
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolume_stage_of_any_column_choice
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsGIs
covers: 470
status: drafted
drafted_by: writer@claude
---
This theorem chooses, for a column $w$ over a large base, a stage whose volumes are the true volumes of the unitary quotients and whose local gates come from a family of local identifications. Its instance at pinned columns is [`exists_trueVolumeStage_columnChoiceStep`](/entry/exists-true-volume-stage-column-choice-step/), which goes to [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/). Below this theorem are 470 declarations of the proof.

## Statement

A stage `GJStage B C` over the columns $C$ of a base $B$ holds: a volume $\mathrm{vol}(W) > 0$ for each hermitian space $W$, a Haar datum, theta jets with their places and words, a global datum `gx`, and gates `gat`: for each word $u$ and place $v$, a local group datum at the residue characteristic of $v$.

`GIs2 K w G` says that for each later stage $D$ built on $G$:

1. `VolTieG D`: for each hermitian space $W$ with admissible signatures, each volume measure $\mu$ of the right signature and each fundamental domain $\mathcal{F}$ of the group `GQ W`, $\mu(\mathcal{F}) = \mathrm{vol}(W)$;
2. `GatNum`, a count of the gates;
3. there is column data at the split primes (`ColumnDataSplitPrimes`): tied hermitian columns, gate ties, a lattice comparison and group compatibility data with the recursion condition `IsRecG`, and the condition `OmegaCompatible` for the constant $\delta$ of the column, which we did not unfold.

**Theorem.** Let $p$ be any property of columns. Eventually in the context (the form `StepW p`), for each column $w$ with $p$ there is a stage $G$ with `GIs2 K w G`.

## Proof

1. `TrueColsTest.later` gives a later stage $Z_0$ of $w$. It uses that the context lies over the base.
2. `exists_standardColumnComparisons_trueColumns`, a second name of [`colsTiedSym_std`](/entry/cols-tied-sym-std/), gives tied symmetric columns $C$ at $Z_0$ with the standard conditions `StdC` and `StdLvC`.
3. `exists_isLocalFamily` gives gates $g$ of the right dimension with `IsLocalFamily`: local identifications at each place, characters $\psi$ away from the level, a standard basis and embeddings, with $g$ equal to `gatOf` of these data.
4. Take $G$ to be $Z_0.G$ with the true volumes and the true global datum (`GJStage.withTrue`), and with the gates $g$. By `gIs2_iff`, `GatNum` follows from `IsRecG`, so two conditions remain.
5. `volumesAgreeAdelic_of_trueVolume`, a second name of `Vol.volTieG_of_trueVol`, proves `VolTieG`. Its proof calls `unitaryAdelicQuotientVolume_is_volume`.
6. `nonempty_columnLocalData_of_standardConcreteFamily` builds the column data. It gets `IsRecG` from `isRecG_of_isLocalFamily` and the full hermitian columns from `exists_fullHermitianColumns_trueColumns`. `omTied_withTrue` gives `OmegaCompatible`. Two twelfth roots $\delta, \delta'$ of the discriminant differ by a factor $u$ with $u^{12} = 1$, so the Eisenstein invariants $g_2, g_3$ of their lattices differ by $u^{-4}$ and $u^{-6}$. Here $u^4$ is a cube root of unity and $u^6 = \pm 1$. The coefficient field contains the cube roots of unity, so $g_2$ and $g_3$ stay in it.
7. `isLocalFamily_stages` moves `IsLocalFamily` from $Z_0$ to the later stage. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsGIs.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGIs.lean#L146).

- The property $p$ is never used. The proof starts with `StepW.of_all fun K B f T w hO _ _`, and drops the arguments for `Forced` and for $p$. So the theorem holds for all columns at once.
- `isLocalFamily_stages` ([line 79](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGIs.lean#L79)) is proved by a `run_tac` block that assigns the hypothesis to the goal with `m.assign`. This skips the elaborator's type check. The kernel still checks the term, so the two `IsLocalFamily` statements must be definitionally equal.
- We did not unfold `GatNum` or `IsRecG`.
