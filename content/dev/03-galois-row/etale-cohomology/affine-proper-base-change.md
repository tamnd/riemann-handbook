---
id: affine-proper-base-change
title: Restriction to the closed part of a henselian pair
kind: theorem
decl: UpperTheory.Et.affine_proper_base_change
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.AffineProperBaseChange
covers: 589
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom E1 of the étale chapter. It is the input E1 of [proper base change](/entry/proper-base-change/), and it is also used by [the finiteness theorem](/entry/etale-finiteness-of-duality/). All of these lie below [Steps holds](/entry/steps-holds/). Its proof gives ten inputs to `etaleCohomology_descent_of_cech_cover`, which holds the content. We describe that proof here.

## Statement

**Theorem.** Let $(A, I)$ be a henselian pair, and let $q$ be a unit in $A$. Then for all $i$, restriction
$$H^n(\operatorname{Spec} A, \mathbb{Z}/q(i)) \to H^n(\operatorname{Spec} A/I, \mathbb{Z}/q(i))$$
is bijective in all degrees $n$.

This is the affine analogue of proper base change of Gabber (Israel J. Math. 87, 1994), for these coefficients.

## Proof

The inputs are five axiom theorems (A1, A9, B1, B2, B4) and five lemmas: `Cover`, `HensIdem`, `EqvQA`, `DescStep` and `CechLevels`. A ring is *QA* if it is a quotient of an absolutely integrally closed domain. A pair $(C, J)$ is *good* if $J$ lies in the Jacobson radical of $C$ and idempotents lift from $C/J$ to $C$.

If $q = 0$, then $A$ is the zero ring, and the map is an isomorphism. Otherwise the proof shows, by induction on $m$, that for every $B$ and $J$ such that $(C, JC)$ is good for every integral $B$-algebra $C$, restriction from $B$ to $B/J$ is bijective in degrees below $m - 1$ and injective in degree $m - 1$. By `HensIdem`, the henselian pair $(A, I)$ has this property.

1. For $m = 0$, all groups in negative degree are $0$, by A9.
2. For the step, `Cover` gives an integral map $B \to A'$, surjective on spectra, with $A'$ a QA ring. `CechLevels` gives a map $\psi$ from the Čech nerve of $\operatorname{Spec} A'/JA' \to \operatorname{Spec} B/J$ to that of $\operatorname{Spec} A' \to \operatorname{Spec} B$. Each level of $\psi$ is the restriction for an integral $B$-algebra, so the induction applies to it. At level $0$, `EqvQA` gives a bijection in all degrees, for the QA ring $A'$.
3. `DescStep` then raises the bound by one for $\psi$. By B4 (Čech descent along integral surjections), the two nerves compute the cohomology of $\operatorname{Spec} B$ and $\operatorname{Spec} B/J$. This transfers the bound to $B \to B/J$.

The content of `EqvQA` is in [a33](/entry/a33/).

## In the Lean code

The theorem is at [AffineProperBaseChange.lean line 26](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/AffineProperBaseChange.lean#L26). The proof it calls is at [EtaleCohomologyDescentOfCechCover.lean line 61](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomologyDescentOfCechCover.lean#L61). E1 is stated in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L134).

- The five lemmas are passed as `EtaleCovers.intersectionNumber_baseChange`, [`QuasiAffineEquivalence.intersectionNumber_baseChange`](/entry/quasi-affine-equivalence-intersection-number-base-change/) and three more of the same name. No intersection number or base change appears in their statements.
- `t_E1Cut.goal_of` in EtaleDegreeZeroCohomologyEquivLocallyConstantFun.lean (line 116) takes the same five lemmas. `etaleCohomology_descent_of_cech_cover` repeats that proof.
- E1 has no hypothesis $q \neq 0$. The case $q = 0$ is the zero ring.
- A third user is `KunnethLefschetz/EtSideGood.lean`, at line 36. We have not unfolded `DescStep` or `CechLevels`.
