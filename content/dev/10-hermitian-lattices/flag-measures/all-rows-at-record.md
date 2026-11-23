---
id: all-rows-at-record
title: Rows with a sharp count at one datum, from the ties
kind: theorem
decl: GlobalTheory.AllRowsAtRecord.allRows_at_record
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.AllRowsAtRecord
covers: 523
status: drafted
drafted_by: writer@claude
---
This theorem builds, at one datum $D$, the rows $A$ with the three properties that the counting row asks for: labels that count, the join conditions, and a count with relative error $e^{-c\, r f \log r}$. [`irr_row_closed`](/entry/irr-row-closed/) applies it at each $D(x,i)$ of a family, with the constants and thresholds chosen there.

## Statement

**Theorem.** Assume `RowsFinDim`. Let $D$ be a datum of rank $r$ and degree $f$, with size data, a Hida setting $X$, a good operator $G$ and a linear isometry $\iota$ from the space `HH` of $D$ to that of $X$. Let $n_0 \in \mathbb{N}$ and $A_{lev}, C_3, c_3, c_b, c \in \mathbb{R}$ with $0 < c \le c_3$. Assume:

1. `GapHyp D`: $r \ge 1801$ and consecutive Harish-Chandra parameters differ by at least $16 r^{19}$;
2. the ties `AutTie`, `RowDictTie` and `LabTie` for $X$, $G$, $\iota$;
3. `CountIdempotentsClass P D n₀ Alev C₃ c₃ cb` for every predicate $P$;
4. `CountTheoremHypotheses` for $D$ and its size data with $n_0, A_{lev}, C_3, c_b$;
5. $4r < g_1$, where $g_0, g_1$ are the two primes of the host of $D$.

Then there are rows $A$ for $D$ with `LabelCountGoodInjective A`, `AllJoinA A` and `CountAllRows A` $(e^{-c\, r f \log r})$.

## Proof

1. `rowsLab_holds` gives labels for the rows of $X$ (`RowsLab X`), from `RowsFinDim`, `GapHyp` and the three ties.
2. Let $\psi_k$ be the standard additive character of $\mathbb{Z}/g_k$ (`ZMod.stdAddChar`). It is nontrivial since $g_k$ is prime (`stdChar_ne`).
3. Let $A$ be `allRowsOfL X ψ hψ hL`, the rows built from $X$, $\psi$ and the labels. `thirdTie_allRows` gives `LabelCountGoodInjective A`. `AllJoinA A` holds with the character $\psi$; its other part comes from `AutTie`, the Harish-Chandra parameters (`hc_X`) and the splitting lemma `splits_X`.
4. `countBase_of` turns `AutTie`, hypothesis 4 and hypothesis 5 into `CountBase`, which includes $D^*(e) > 0$. With it, `tieCountAt_allRowsOf` gives the count hypotheses for $A$. `countCylAt_of`, with hypothesis 3 at $P = $ `PCount` and `pCountTie_holds`, gives for each cylinder $|\dim_T - D^*| \le e^{-c_3 r f \log r} D^*$.
5. `countAllRows_of`: since $c \le c_3$, $r \ge 2$ and $f \ge 1$, the error $e^{-c_3 r f \log r}$ is at most $e^{-c\, r f \log r}$, which lies in $[0, 1)$ as $c > 0$.

## In the Lean code

The theorem is in [AllRowsAtRecord.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AllRowsAtRecord.lean#L67). The cylinder count `CountCylAt` is in [JCount.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/JointConditionsZpowers/JCount.lean#L11) and `CountBase` in [AllRowsOf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/AllRowsOf.lean#L714).

Some details:

- The count itself comes from hypothesis 3. Its source is [`count_constants_of_siegelWeil`](/entry/count-constants-of-siegel-weil/), whose entry notes that `CountIdempotentsClass` does not use its datum argument.
- Hypothesis 3 is asked for every $P$, but only $P = $ `PCount` is used.
- The size data enter only through hypothesis 4.
- `GapHyp` is used in step 1 and for $r \ge 2$.
