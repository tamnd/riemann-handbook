---
id: weighted-count-definite-unitary
title: The weighted fixed-point count as a sum over definite pairs
kind: theorem
decl: UpperTheory.Gal.Cnt.weighted_count_definite_unitary
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.DefiniteTraceForms.WeightedCountDefiniteUnitary
covers: 820
status: drafted
drafted_by: writer@claude
---
This theorem rewrites the weighted count `cxTotalM` of fixed points as a sum over classes of *definite* pairs, with a weight that sums over the roots of a polynomial. It is the first group-side input $h_1$ of [ksHodge_of_geo](/entry/ks-hodge-of-geo/). There, `GroupTop_of` joins it with [the trace identity for definite forms](/entry/cnt-trace-definite-forms-identity/) to turn the count into an automorphic trace.

## Statement

Let $G$ be a group datum `HTGroup p`: a CM field $F$, a central simple $F$-algebra $C$ of dimension $n^2$ with an involution of the second kind, and at each infinite place $v$ of $F$ a map $\psi_v \colon C \to M_n(\mathbb{C})$ and a hermitian matrix $H_v$ of signature $(1, n-1)$ or $(0, n)$. Assume that exactly one place $v$ has signature $(1, n-1)$ ($G.a = 1$), and that $n$ is odd.

A *pair* is $(\beta, \gamma, c)$ with $\beta \in C^\times$ fixed by the involution, $\gamma \in C^\times$ a similitude of $\beta$ with factor $c \in \mathbb{Q}^\times$, with local conditions at the finite places and at $\infty$, and $\gamma$ regular: its minimal polynomial $P_\gamma$ over $F$ has degree $n$ and is separable. A *definite pair* (`DPair`) has the same data, but the condition at $\infty$ is replaced by this: the form $H_v \psi_v(\beta^{-1})$ is positive definite at $v$ and negative definite at the other places. Each pair carries a term $\operatorname{term}(P)$, a sum of values of the test functions $f$ (away from $p$) and $f'$ (at $p$).

**Theorem** (`MarkWeightedFixedPointEqDefinitePairOdd`). Let $c \colon F[x] \times \mathbb{C} \to \mathbb{C}$ be any weight. Let $f$ be a test function at a level $L$ whose support consists of regular elements (`RegAf`), and $f'$ a test function at $p$. Assume that each marked pair with reducible $P_\gamma$ has term $0$. Then

$$\mathrm{cxTotalM}(c, f, f') = \sum_{[P]\ \text{definite},\ P_\gamma \text{ irreducible}} \Bigl(\sum_{\mu} c(P_\gamma, \mu)\Bigr) \operatorname{term}(P),$$

where $\mu$ runs over the roots of $P_\gamma$ under the embedding $v$ (`rootSum`). The left side is the weighted count of fixed points in [fixedPoints_int_base_holds](/entry/fixed-points-int-base-holds/): a sum over classes of forms and points of $1/|\mathrm{Stab}|$ times $f \cdot f' \cdot c(P_y, \mu_y)$, where $\mu_y$ is the eigenvalue of $y$ at the fixed point (`eigL`).

## Proof

The proof is `markWeightedFixedPoint_definitePair_odd_of_counts` applied to:

1. [complex_count_regular_marked_points](/entry/complex-count-regular-marked-points/) (`CxCountRegMark`): $\mathrm{cxTotalM}(c)$ equals the sum over classes of *marked* pairs of $c(P_\gamma, \mu) \operatorname{term}(P)$. A mark $\mu$ is an eigenvalue of $\psi_v(\gamma)$ with an eigenvector of positive norm for $H_v\psi_v(\beta^{-1})$.
2. `finitely_many_marked_classes_term_degree_one`: only finitely many marked classes have a nonzero term.
3. `marked_field_pairs_sum_eq_definite_pairs_sum` (`MoveDefInv`): for each choice $\mathrm{sel}$ of a root at $v$ for each polynomial, the sum over marked pairs with irreducible $P_\gamma$ and mark $\mathrm{sel}(P_\gamma)$ equals the sum over definite pairs with irreducible $P_\gamma$.

The argument: enumerate the $n$ roots of each monic polynomial of degree $n$ as $\mathrm{sel}_1, \dots, \mathrm{sel}_n$ (`exists_root_enum`). A mark is a root of $P_\gamma$, it is unique, and the roots are distinct. So the marked sum splits as a sum over $i$ of the marked sums with mark $\mathrm{sel}_i$; the reducible pairs drop out by the hypothesis. Fact 3 moves each of these to definite pairs. Summing over $i$ gives the root sum. Fact 2 and a bijection of classes (`cls_equiv_dcls_irr`) give the finiteness needed to exchange the sums.

## In the Lean code

The theorem is in [WeightedCountDefiniteUnitary.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/DefiniteTraceForms/WeightedCountDefiniteUnitary.lean#L10). The statement is in [MarkWeightedFixedPointEqDefinitePairOdd.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/MarkWeightedFixedPointEqDefinitePairOdd.lean#L50), and the proof in [MarkWeightedFixedPointDefinitePairOddOfCounts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MarkWeightedFixedPointDefinitePairOddOfCounts.lean#L32). `Pair`, `Mark` and `term` are in [ExistsRootSelectionUnitaryRankOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRootSelectionUnitaryRankOne.lean#L58), and `DPair` and `dSumIrr` in [DiagHermitianTrivialOfSumFourSquares.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DiagHermitianTrivialOfSumFourSquares.lean#L15).

Points to note:

- The hypothesis on reducible marked pairs is not proved here. In `groupTop_of` ([PGroupTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/PGroupTop.lean#L26)) it is the field `pairs` of the condition `Good` on the test function, and the regularity of the support is the field `reg`.
- We have not unfolded `term`, the stabilizers in `cxTotalM`, or the proofs of facts 1 to 3.
