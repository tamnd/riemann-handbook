---
id: has-exp-bound-at
title: The exponent bound at one point
kind: theorem
decl: GlobalTheory.ExpTie.Asm.hasExpBound_at
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExpansionOfNumericsModel
covers: 1355
status: drafted
drafted_by: writer@claude
---
This theorem proves the exponent bound `HasExpBound` for one leaf object at one point of the construction. It bounds the lattice exponents $J_0(w, j)$ at the twisted places $w$ by numbers $J_p(j, l)$ that depend only on the residue characteristic $l$, and it bounds a weighted sum of the $J_p$. Its user is [the exponent statement from the alternative inputs](/entry/exp-st-of-alt/), in branch 2 of [the unitary hypotheses](/proof/unitary-hypotheses/). The local inequality comes from [the bound on the lattice exponent](/entry/jexp-u-le-jrec7/).

## Statement

Fix a point $p$ of the construction, over a number field $L$, with $m$ indices $j$. For each index $j$, each element $t$ of a type $T$ of the point and each finite place $w$ of $L$, the point gives a block datum and a space of forms. These give two lattices $\Lambda_\nabla$ and $\Lambda_\Delta$, and the lattice exponent $J(j, t, w)$ (`JexpU`): the least $J$ with $w^J \Lambda_\nabla \subseteq (\Lambda_\Delta)_{(w)}$, divided by the ramification index of $w$. The numerical datum of the point has $J_0(t, w, j) = J(j, t, w)$ by definition. Let $O$ be a leaf object at $p$, with fields $m, x, \varepsilon, T_2$; put $x_e = x^\varepsilon$ and $b = e^{x_e}$.

Assume:

1. the cut bound `ExCut` for exponents of Weyl modules;
2. $O$ has $m$, $x$, $\varepsilon$ and $T_2$ equal to those of the point;
3. for each $j$, parameters $P_j$ and a weight datum $W_j$ that satisfy `Dict` (they match the point) and `NumOk`;
4. for all $j, t, w$, the inclusion $\mathrm{LIncl}$ at the exponent $J_A(l)$ of $W_j$, where $l$ is the residue characteristic of $w$;
5. for each $j$ and each twisted place $w$ with $l$ in the range of $W_j$, local models at $w$ (`ModelAt`), as in [the inclusion from local models](/entry/l-incl-of-models/).

**Theorem.** With $J_p(j, l) = J^{(7)}_{W_j}(l)$ (`Jrec7`):

- $J_0(\mu_w, w, j) \ge 0$ for each twisted place $w$;
- $J_p \ge 0$, and $\sum_{l \in Q} J_p(j, l) \log l \le 30\, T_2\, m\, b\, x_e^2 + 2 m b$ for each finite set $Q$ of primes;
- $J_0(\mu_w, w, j) \le J_p(j, l_w)$ for each twisted place $w$.

## Proof

1. The first part follows from hypothesis 4 and `exponent_datum_le_of_primePowerLatticeInclusion`, which gives $0 \le J$ from any inclusion.
2. The second part is `sum_exponent_log_le` for $P_j$ and $W_j$. It uses `ExCut`, `NumOk` and the fields `card`, `f`, `special` and `thick` of `Dict`. The fields `log` and `b` of `Dict`, with hypothesis 2, give $x_e = P_j.L$, $b = P_j.b$ and $m = P_j.m$.
3. The third part is [`jexpU_le_jrec7`](/entry/jexp-u-le-jrec7/). Hypothesis 4 supplies its case off the range, and hypothesis 5 its case in the range.

## In the Lean code

The theorem is in [ExpansionOfNumericsModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L50). `HasExpBound` is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L82), and `LeafJSum` and `LeafJExp` are in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L349). The lemmas:

- `exponent_datum_le_of_primePowerLatticeInclusion`;
- `UpperTheory.ExcSet.sum_exponent_log_le`, in [ExcSet.lean](lean:Development/AutomorphicArithmetic/PrimeDiscriminants/ExcSet.lean#L50);
- `jexpU_le_jrec7`, in the same file;
- `splitPartNumbers_exponent_eq_liftExponent` (the identity $J_0 = J$, proved by `rfl`).

Odd points:

- Part 1 uses hypothesis 4 only to get $J \ge 0$. But $J$ is a quotient of two natural numbers, so it is never negative.
- Hypothesis 4 asks for the inclusion at $J_A$ at every place, also in the range. In the range it serves only part 1, and the upper bound there comes from hypothesis 5.
- `expSt_of` in the same file ([line 80](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L80)) and `expSt_of_alt` are the same proof, and both end with this theorem.
