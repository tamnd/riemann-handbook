---
id: row-at-of-std-tie
title: The kernel conditions hold along a row of standard ties
kind: theorem
decl: GlobalTheory.Pdv.rowAt_of_stdTie
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.RowAtOfStdTie
covers: 2327
status: drafted
drafted_by: writer@claude
---
This theorem proves the second part of the service row `ServH`: the kernel entry of each selected bundle satisfies the conditions `Pdv.At`. Its user is [`servH_row`](/entry/serv-h-row/), which joins it with the row of local models. The theorem turns a pointwise result into a row. The pointwise result is [`at_of_true_columns`](/entry/at-of-true-columns/), reached through the renaming [`kernelDatumConditions_at_standardKernelComparison`](/entry/kernel-datum-conditions-at-standard-kernel-comparison/) and the pass-through [`at_of_stdTie`](/entry/at-of-std-tie/). The real content is in `at_of_true_columns`.

## Statement

A *row condition* `RowE Q Lk E` on a slot $Q$ and a link $L_k$ says: for all parameters $\kappa$ large in the sense of `ParEv`, and for each point $K$ of a family above a threshold $x_0$, the property $E$ holds at each bundle point $\beta$ of $Q$ and each link $(c, b)$. A *row* `Row Q Lk H` says that there is some $E$ with `RowE Q Lk E` such that $H(\mathcal A, \sigma)$ holds for every class $\mathcal A$ and selection $\sigma$ for $E$. Both are in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L261).

**Theorem.** Assume `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict` and `IntInert` (stated in [`servH_row`](/entry/serv-h-row/)). Let $Q$ be a slot, $L_k$ a link and `ker` a choice of tied kernel entry for each bundle. If `RowE` holds for "the entry `ker b` has a standard tie" (`StdTie`), then
$$\mathrm{Row}\ Q\ L_k\ \bigl(\mathrm{AtAll}\ (D, O, c, b) \mapsto \mathrm{Pdv.At}\ O.\mathrm{ex}\ (\mathrm{ker}\ b).\mathrm{ent}\bigr),$$
that is, every selected point satisfies `Pdv.At`.

## Proof

1. `shape_uniform` gives, for each $\varepsilon$, a threshold $x_0(\varepsilon)$. For every family $F$ and every $x \ge x_0(\varepsilon)$ with $x > x_1(F)$, it gives three facts about the datum $F.D(x, i)$: the condition `Shape` for every entry, a bound $\le 2a$ on a difference of row values, and $3 \le$ `splitBound`.
2. The new row condition is $E$ = "$x_0(\varepsilon) \le x$ and `StdTie`". The first half holds for all parameters (`ParEv.of_all`). `RowE.and` adds the hypothesis.
3. At a selected point, the first half of $E$ gives $x \ge x_0(\varepsilon)$, so step 1 applies. The two conditions $5 \le d_{l1}$ and $4 \le d_{l2}$ come from `Fm.fixed`, which fixes $d_{l1} = 5$ and $d_{l2} = 4$ for every family. Then `kernelDatumConditions_at_standardKernelComparison` gives `Pdv.At`.

## In the Lean code

The theorem is at [RowAtOfStdTie.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RowAtOfStdTie.lean#L13). The lemmas it calls:

- `GlobalTheory.ShapeUniform.shape_uniform` in [ThreeLeSplitAt.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ThreeLeSplitAt.lean#L389);
- `ParEv.of_all`, `RowE.and` and a `mono` step, general facts about rows in the same file as `RowE`;
- `kernelDatumConditions_at_standardKernelComparison`.

The bound $3 \le$ `splitBound` does not depend on the entry, but `shape_uniform` states it for each entry. The proof gets it by applying the result to one entry built with `OrbitPlaces.ofKer` and zero data.
