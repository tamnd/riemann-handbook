---
id: irr-row-closed
title: The count rows from the ties, in the closed sense
kind: theorem
decl: GlobalTheory.IrrRowConcrete.irr_row_closed
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IrreducibilityRowOfConcreteAutomorphicData
covers: 530
status: drafted
drafted_by: writer@claude
---
This theorem turns the three ties at each datum of a family into rows with a sharp count, uniformly over a family class. Its renaming [`irreducibilityRow_of_concreteAutomorphicData`](/entry/irreducibility-row-of-concrete-automorphic-data/) gives the second property of the counting row in [`row_counts_of_ties_alt`](/entry/row-counts-of-ties-alt/).

## Statement

Let $\varepsilon_C(c, r, f) = e^{-c\, r f \log r}$ (`epsC`). For rows $A$ of a datum $D$ (`AllRows D`), `CountAllRows A ε` says: $0 \le \varepsilon < 1$, $D^*(e) > 0$, and for $k \in \{0,1\}$ and each set $S$ of tuples, the cylinder count satisfies $|\dim_T - D^*| \le \varepsilon\, D^*$. `LabelCountGoodInjective A` says that the labels of $A$ count $\dim_T$, and that the good tuples are the image of an injective map from the rows of $D$. `AllJoinA A` ties the group record of $A$ to $D$ (`RowsTie`, not unfolded) and asks for idempotents from a nontrivial additive character of $\mathbb{Z}/g_k$.

**Theorem.** Assume `SiegelWeilUnitaryConvergent` and `RowsFinDim`. There is $c_{Ic} > 0$ such that for every family class $\mathcal{C}$ whose families satisfy `TuSize`: if it is [closed](/step/closed-def/) on $\mathcal{C}$ that eventually in $x$ each $D(x,i)$ has $X$, $G$, $\iota$ with `AutTie`, `RowDictTie` and `LabTie`, then it is closed on $\mathcal{C}$ that eventually in $x$ each $D(x,i)$ has rows $A$ with `LabelCountGoodInjective A`, `AllJoinA A` and `CountAllRows A` $(\varepsilon_C(c_{Ic}, r, f))$.

Here $r$ and $f$ are the rank and degree of $D(x,i)$. `RowsFinDim` says that an evaluation map on the automorphic $L^2$ space is injective with a given range.

## Proof

1. [`count_constants_of_siegelWeil`](/entry/count-constants-of-siegel-weil/) gives counting constants $c_{30}(\ell)$ for each list $\ell$, a number $c_{Ic} > 0$ with $c_{Ic} \le c$, and `CountAllPointsClass` for every predicate $P$, which gives the count `CountIdempotentsClass` at each $D(x,i)$ and $c_b > 0$.
2. `countClauses_closed` makes closed on $\mathcal{C}$: eventually, `CountTheoremHypotheses` holds at each $D(x,i)$ with the constants $c_{30}$, and $4r < g_1$.
3. `gapEv_closed_of` makes closed on $\mathcal{C}$: eventually, `GapHyp` holds at each $D(x,i)$.
4. `Closed.and` joins the hypothesis with steps 2 and 3. For $x$ past the largest of the thresholds and past $x_1 + 1$, [`allRows_at_record`](/entry/all-rows-at-record/) gives the rows at each $D(x,i)$.

## In the Lean code

The theorem is in [IrreducibilityRowOfConcreteAutomorphicData.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IrreducibilityRowOfConcreteAutomorphicData.lean#L18). `CountAllRows` and `epsC` are in [IrreducibleOfCountSizes.lean](lean:Formalism/LocalToGlobal/GlobalTheory/IrreducibleOfCountSizes.lean#L64), `LabelCountGoodInjective` in [ArithmeticCylinders.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArithmeticCylinders.lean#L271), and `AllJoinA` in [AllJoin.lean](lean:Formalism/LocalToGlobal/HilbertRowConditions/AllJoin.lean#L18).

Some details:

- The constant $c_{Ic}$ from step 1 is $1/16$.
- The positivity of $c_b$ is read off the case $P = $ true of step 1 (line 23).
- The count is used with every predicate $P$ (line 41), but [`allRows_at_record`](/entry/all-rows-at-record/) uses only one.
- `TuSize` is used only in steps 2 and 3.
