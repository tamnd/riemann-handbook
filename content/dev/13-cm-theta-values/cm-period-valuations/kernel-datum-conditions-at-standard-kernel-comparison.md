---
id: kernel-datum-conditions-at-standard-kernel-comparison
title: The kernel conditions at a standard tie, restated
kind: theorem
decl: GlobalTheory.T.kernelDatumConditions_at_standardKernelComparison
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelDatumConditionsAtStandardKernelComparisonStatement
covers: 2307
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`at_of_stdTie`](/entry/at-of-std-tie/). It has the same statement, and its proof applies that theorem. Its user is [`rowAt_of_stdTie`](/entry/row-at-of-std-tie/), which applies it at each selected point of a row. The content is in [`at_of_true_columns`](/entry/at-of-true-columns/), two levels below.

## Statement

Assume `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict` and `IntInert`. Let $D$ be a datum (`D7`), $O$ an object over $D$ and $t$ a tied kernel entry of $O$. Assume:

1. $t$ has a standard tie (`StdTie D O t`);
2. $3 \le$ `D.host.splitBound`, $5 \le d_{l1}$ and $4 \le d_{l2}$ for the constants $O.K$;
3. for every entry $E$ (`OrbitPlaces.Ent D`), the condition `Shape` holds, and each difference $E.\mathrm{row}(u, j, s, 0) - E.\mathrm{row}(u, j, s, 1)$ with $j < m$ and $s$ in `D.host.TT` is at most $2a$.

Then the kernel entry of $t$ satisfies `Pdv.At`. The predicate `Pdv.At` is described in [`at_of_true_columns`](/entry/at-of-true-columns/).

## Proof

Apply `at_of_stdTie`. Nothing else is used.

## In the Lean code

The theorem is at [KernelDatumConditionsAtStandardKernelComparisonStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelDatumConditionsAtStandardKernelComparisonStatement.lean#L10). Its proof is the tactic

```
first | exact @at_of_stdTie | exact at_of_stdTie | (intros; apply at_of_stdTie <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, so the theorem is a renaming.
