---
id: complex-count-regular-marked-points
title: The weighted fixed-point count as a sum over marked pairs
kind: theorem
decl: UpperTheory.Cb.complex_count_regular_marked_points
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.ComplexCountRegularMarkedPoints
covers: 432
status: drafted
drafted_by: writer@claude
---
This theorem rewrites the weighted count `cxTotalM` of fixed points as a sum over classes of *marked* pairs. It is fact 1 of [weighted_count_definite_unitary](/entry/weighted-count-definite-unitary/), which moves the marked sum to definite pairs. The proof regroups a sum: points by the conjugacy class of the element that fixes them, and conjugacy classes against classes of pairs.

## Statement

The group datum $G$, the pairs $P = (\beta, \gamma, c)$ with their polynomial $P_\gamma$ and term $\operatorname{term}(P)$, the marks, and the count $\mathrm{cxTotalM}$ are as in [weighted_count_definite_unitary](/entry/weighted-count-definite-unitary/). Recall: $\mathrm{cxTotalM}(c, f, f')$ sums over classes of forms $\beta$ and classes of points $a$, each with a vector $z_a$ of positive norm at $v$, the value $1/|\mathrm{Stab}(a)|$ times the sum of $f \cdot f' \cdot c(P_y, \mu_y)$ over the elements $y$ of the similitude group of $\beta$ that fix the line of $z_a$; $\mu_y$ is the eigenvalue (`eigL`). A mark $\mu$ of $P$ is an eigenvalue of $\psi_v(\gamma)$ with an eigenvector of positive norm for $H_v \psi_v(\beta^{-1})$.

**Theorem** (`CxCountRegMark`). Assume that exactly one place has signature $(1, n-1)$ ($G.a = 1$), and let $v$ be that place. Let $c \colon F[x] \times \mathbb{C} \to \mathbb{C}$ be any weight, $f$ a test function at a level $L$ whose support consists of regular elements, and $f'$ a test function at $p$. Then

$$\mathrm{cxTotalM}(c, f, f') = \sum_{[P]\ \text{marked by}\ \mu} c(P_\gamma, \mu) \operatorname{term}(P).$$

Unlike its parent, the theorem needs neither $n$ odd nor any condition on reducible $P_\gamma$.

## Proof

1. **The right side by forms** (`markSumC_regroup`). A marked pair has similitude factor $c > 0$ (`pair_sim_pos`), and its mark is unique (`mark_unique`). A class of pairs with $c > 0$ gives a class of forms $\beta$ and a conjugacy class in the similitude group of $\beta$, bijectively on each fibre over a class of forms (`finsum_eq_finsum_finsum_of_fibre_bij`). On each fibre the term of the pair equals a class weight `clsW` of a representative $y$ (`clsW_eq_markTerm`, from `CxReg.class_summand_eq_term_of_a_one`). So the right side is $\sum_\beta \sum_{[y]} \mathrm{clsW}(y)$.
2. **The left side by conjugacy classes** (`cxSumAtM_unfold`). For one form $\beta$, the sum over points is first written over orbits of the similitude group (`cxSumAtM_orbit`). The weight is invariant under conjugation (`cxM_smul_conj`), so `orbit_sum_conj_classes` gives a sum over conjugacy classes $[y]$ of sums over orbits of the centralizer of $y$. `cls_part` shows that each of these is $\mathrm{clsW}(y)$, with `conjugacyClassPart_eq_weight_mul_kottwitzPointSum`.

Step 2 has three inputs from other files:

- for each line of positive norm, only finitely many $y$ fix it with a nonzero value of $f \cdot f'$ (`FinFix.finite_fix_core`);
- only finitely many classes of points have a nonzero contribution (`CxReg.finite_pts_reg`, which uses the regular support of $f$);
- an element $y$ in the support fixes at most one line of positive norm. `CxReg.sep_of_regAf` makes $P_y$ separable, and `separable_formGroup_element_fixes_unique_positive_line` concludes from signature $(1, n-1)$ at $v$.

By the third input, $\mu_y$ depends only on $y$ (`muOf`); on a marked pair it is the mark (`muOf_eq_mark`).

## In the Lean code

The theorem is in [ComplexCountRegularMarkedPoints.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/ComplexCountRegularMarkedPoints.lean#L552), with `markSumC_regroup` at line 446, `cxSumAtM_unfold` at line 251 and `cls_part` at line 216. The statement `CxCountRegMark`, `cxTotalM` and `markSumC` are in [MarkWeightedFixedPointEqDefinitePairOdd.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/MarkWeightedFixedPointEqDefinitePairOdd.lean#L43). `Pair.Mark` is in [ExistsRootSelectionUnitaryRankOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRootSelectionUnitaryRankOne.lean#L195).

`Pair.Mark` asks for *some* place of signature $(1, n-1)$, not for $v$; as $G.a = 1$, this is the same. `markSumC` picks the mark by `choose`; uniqueness makes this harmless. We have not unfolded `term`, `pointSum`, `Pts`, or the proofs of the three inputs and of `class_summand_eq_term_of_a_one`.
