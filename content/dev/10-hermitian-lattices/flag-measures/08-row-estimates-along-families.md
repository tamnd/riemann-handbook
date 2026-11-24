---
title: Row estimates along families
decls:
  - GlobalTheory.RowsFive.rowsOne_of
  - GlobalTheory.RowsFive.rows_three_bounds
  - GlobalTheory.T.admissible_family_satisfies_row_estimates
  - GlobalTheory.LoopRowBoundsGap.rows_along_family
  - GlobalTheory.T.loopRowBounds_along_family_largeGaps
  - GlobalTheory.LoopRowsCloseGap.loop_rows_closed_gap
  - GlobalTheory.T.loopRows_of_large_gap_discreteSeries
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row estimates along families

This section proves the row estimates along a family of automorphic data with large gaps. A row is a sum over the terms that belong to one word pair $(u, u')$, and it splits into three kinds: the nondegenerate terms, the degenerate terms and the terms of corank one. For each kind there is a row bound with a constant $C$. The main result gives the three row bounds for every $C$ above an explicit constant, for all large members of an admissible family. The loop row statement then follows for a selection of spectral ties, and it is used by [the loop row bound for a selection of spectral ties](/entry/loop-rows-of-rows-fin-dim-alt/).

### Families and admissibility

A *family* $F$ is a sequence of automorphic data $F(x, i)$ indexed by a real parameter $x$ and an index $i$, together with constants. Among these constants are $C'(F)$, $C_l(F)$, $C_\Gamma(F)$ and a list of output constants. A *family class* $\mathcal C$ is a set of families. A property of families is [closed](/step/closed-def/) on $\mathcal C$ if it holds for each family of $\mathcal C$ for all large $x$ and all $i$.

We say that a property holds *eventually* for a family $F$ if there is $x_0$ such that it holds for $F(x, i)$ for all $x \ge x_0$ and all $i$.

**Definition 3.8.1 (Amplitude package).** An *amplitude package* $U$ is a tuple of real constants
$$U = (c_3, c_H, c_V, c_S, c_4, C_a, C_2, C_h)$$
together with a bound of second order. The first five are count constants and the last three are amplitude constants. The package is *admissible* for a family if the count conditions with $c_3, c_H, c_S, c_4$, the cell volume bound with $c_V$ and the amplitude bounds with $C_a, C_2, C_h$ hold eventually.

For a package $U$ and constants $C_T, A, C_0, C_\Gamma$ put
$$c = \max\big(c_3, 1, |c_H| + 2, |c_V| + 2, |c_S| + 2, |c_4| + 2\big).$$
The *corank one constant* is
$$
\begin{aligned}
C_1(U) = \max\big( & 4\sqrt{A},\ 2\sqrt{2 C_0}\, c,\ C_\Gamma + C_2 (9c + 3), \\
& 4 + 2\big(c^2 + 2 \max(C_h - c, 0)\big)(c + 1) \big).
\end{aligned}
$$
The *row constant* $C_0'(U)$ is the maximum of the nondegenerate constant, the degenerate constant and $C_1(U)$.

### The three row bounds

**Theorem 3.8.2 (Corank one rows).** Let $F$ be a family that meets the five family conditions: the existence of rows, three numbered admissibility conditions, and the Weyl dimension quotient bound. Let $X$ and $Y$ be term ties and loop ties that meet the tie conditions, the injectivity of the word pair terms and the lattice condition on the word pair parameters. Let $U$ be an amplitude package admissible for $F$. Then for every $C \ge C_1(U)$ the corank one row bound with $C$ holds eventually, for all word pairs that meet the counting hypothesis.

Lean: `GlobalTheory.RowsFive.rowsOne_of`.

*Proof.* The proof has four steps.

1. Take the parts of the admissibility of $U$: the count conditions, the cell volume bound and the amplitude bounds, each with its threshold in $x$.
2. Take the family conditions and their thresholds. Let $x_0$ be the maximum of the twelve thresholds.
3. For $x \ge x_0$, the decay length of the family is large enough for the terms of corank one. Collect the conditions at $F(x, i)$ into one set of row hypotheses.
4. The corank one row bound with $C$ is the bound of the corank one terms by an explicit function of $C$, the height, the amplitude and the counting data, times the degree of $u'$. It follows from the row hypotheses and the injectivity of the terms, for $C \ge C_1(U)$. $\square$

**Theorem 3.8.3 (Three row bounds).** Under the hypotheses of the theorem on corank one rows, for every $C \ge C_0'(U)$ the nondegenerate, degenerate and corank one row bounds with $C$ hold eventually, for all word pairs that meet the counting hypothesis.

Lean: `GlobalTheory.RowsFive.rows_three_bounds` (also `GlobalTheory.T.admissible_family_satisfies_row_estimates`, a second name).

*Proof.* Since $C \ge C_0'(U)$, $C$ is at least each of the three constants. The nondegenerate bound, the degenerate bound and the corank one bound each hold eventually. Two properties that hold eventually hold together eventually: take the larger threshold. $\square$

### Constants along a family

**Theorem 3.8.4 (Row bounds along a family).** Assume the Siegel mass ratio, the gap hypothesis and the shifted discrete series bound. Then for all real constants $C_g, c_b, C_u, c_T, C_T, C_0, A, C_1, c_V, C_\Gamma$ there are $C_0'$ and a threshold $t$ with this property. Let $F$ be a family with constant $C_\Gamma$, with $t \le C'(F)$, $t \le C_l(F)$ and the rank hypothesis. Then:

1. eventually, the counting hypothesis gives the form condition for each word $u$;
2. for term ties $X$ and loop ties $Y$ that meet the tie conditions, the injectivity of terms, the lattice condition and eventually the cell volume bound with $c_V$, and for each $C \ge C_0'$, the three row bounds with $C$ hold eventually, for all word pairs that meet the counting hypothesis.

Lean: `GlobalTheory.LoopRowBoundsGap.rows_along_family` (also `GlobalTheory.T.loopRowBounds_along_family_largeGaps`, a second name).

*Proof.* The proof has five steps.

1. The Siegel mass ratio gives uniform count constants $c_3, c_H, c_S, c_4$ and a threshold $t_1$, above which the count conditions hold eventually.
2. The three hypotheses give amplitude constants $C_a \ge 0$, $C_2$, $C_h \ge 0$ and a threshold $t_2$, above which and with the rank hypothesis the amplitude bounds hold eventually.
3. Let $U = (c_3, c_H, c_V, c_S, c_4, C_a, C_2, C_h)$, $C_0' = C_0'(U)$ and $t = \max(40, t_1, t_2)$.
4. The raw mass and genus mass identities hold with no hypothesis. With the gap hypothesis, $40 \le C_l(F)$ and the rank hypothesis, they give the form condition and the five family conditions.
5. Steps 1 and 2, with the cell volume bound, make $U$ admissible for $F$. The theorem on three row bounds gives the conclusion for $C \ge C_0'$. $\square$

### The loop row statement

**Theorem 3.8.5 (Loop rows for large gaps).** Assume the gap hypothesis, the existence of Bessel maps, the shifted discrete series bound, the decay of the Whittaker functions for large gaps, and the finite dimension of rows. Let $\mathcal C$ be a family class whose members satisfy the size condition on the parameter $T_u$, and let a selection of spectral ties be given. Assume that the rank hypothesis with constants $(3, C_{YL} + 1, \tfrac14, 3, \tfrac12, C_{Tu})$ is closed on $\mathcal C$. Then the loop row statement of level $3$ holds for $\mathcal C$ and the selection: for each function $a_F$ of the constant list, it is closed on $\mathcal C$ that, for all word pairs that meet the counting hypothesis, if the selected ties are concrete and the loop series converges absolutely, then the row is big and not scalar with the loop bound.

Lean: `GlobalTheory.LoopRowsCloseGap.loop_rows_closed_gap` (also `GlobalTheory.T.loopRows_of_large_gap_discreteSeries`, a second name).

*Proof.* The proof has five steps.

1. The size condition on $T_u$ makes the gap hypothesis hold eventually, closed on $\mathcal C$. So it suffices to prove the statement for the subclass of families with this property.
2. The standing inputs hold: the unramified Hermitian representation, the weighted local coefficients and three local formulas have no hypothesis; the low and infinite decay are parts of the gap hypothesis; finiteness of the cells follows from the decay of the Whittaker functions and the finite dimension of rows.
3. The theorem on row bounds along a family gives a threshold and a constant for each constant list. The covolume of the stabiliser of a relevant term gives the cell volume constant $c_V$.
4. For families with $C'$ and $C_l$ above the threshold, the first conclusion of step 3 gives the form condition for each word.
5. The loop row statement reduces to the three row bounds for the family with a raised starting point. Build the loop ties from the local Bessel data and the loop term data, and apply the second conclusion of step 3. $\square$

**Remark 3.8.6 (Formalization).** The three row bounds are `RowsND`, `RowsDeg` and `RowsOne`, the package is the structure `UC` with the predicate `UAdm` (DegenerateConstant.lean, line 18), and $C_0'(U)$ is `c0U` (DegenerateConstant.lean, line 423). "Eventually" is `OwnEv` (LeSCSCl.lean, line 26). The corank one bound applies `corank_one_bound_of_injective_terms`, and the bound `oneB` is not unfolded here. The nondegenerate and degenerate bounds are `rowsND_of` and `rowsDeg_of` (AdmissibleFamilySatisfiesRowEstimates.lean, lines 29 and 133), and that file starts with `set_option linter.unusedVariables false` (line 15). The family conditions are `FamilyRowsExist`, `admF6`, `admF7`, `admF8` and `FamilyWeylDimensionVandermondeQuotient`; the tie conditions are `rows_TiesF`, `wordPairTermInjective` and `wordPairBetaLattice`. The inputs of the row bounds along a family are `SiegelMassRatio`, `GapIn.Hyp` and `ThmBpDS`, through `rowCounts_uniform_constants_families`, `amplitude_bounds_uniform_large_gap_families`, `rows_raw_mass_and_genus_mass` and `along_family`. The package `UC` lets the amplitude constants depend on a parameter $C_{pr}$, but in the row bounds along a family they are constant. The loop row statement is `LoopRowS`, and its two conclusions are `RowBig` and `RowNotScalar`, not unfolded here; the reductions are `loopRowS_of_sub` and `loopRowS_of_raised`. The second names of the row bounds along a family and of the loop rows are proved by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic.
