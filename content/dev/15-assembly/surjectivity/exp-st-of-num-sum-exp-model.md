---
id: exp-st-of-num-sum-exp-model
title: The exponent bound from the numerical, sum and model statements, under a second name
kind: theorem
decl: GlobalTheory.T.expSt_of_num_sumExp_model
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExpStOfStatement
covers: 1357
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`expSt_of_alt`](/entry/exp-st-of-alt/) under a second name. Its only user is [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/). Below this theorem are 1,357 declarations, one more than below the copy. The work is in [`hasExpBound_at`](/entry/has-exp-bound-at/), which the copy calls at each recorded object.

## Statement

**Theorem.** Assume `ExCut`, `NumStAlt`, `ExponentSumStatement` and `ModelStatement`. Then `ExponentStatement` holds.

- `ExCut` is a statement about an exponent $e_\ell(N, \lambda)$ attached to $N \in \mathbb{N}$, a prime $\ell$ and a sequence $\lambda$ (`LA.exZ`, not unfolded). Suppose that a sequence derived from $\lambda$ (`res N λ`) is antitone and that the numbers `UN N λ a` for $a < N$ lie in an interval of length $h$. Then for each $a \le N$, $e_\ell(N, \lambda) \le e_\ell(a, \lambda) + e_\ell(N - a, \lambda(a + \cdot)) + a (N - a) \lfloor \log_\ell h \rfloor$.
- `NumStAlt`: eventually at points of large families, for each index $j$ there are parameters $P$ and weights $W$ that match the size data (`Dict`) and pass the numerical checks (`NumOk`).
- `ExponentSumStatement`: for each such $(P, W)$, each $t$ and each place $w$, the lattice inclusion `LIncl` holds at the exponent `W.JA P ℓ`, with $\ell$ the residue characteristic of $w$.
- `ModelStatement` is stated in [its entry](/entry/model-st-of-small-frame-gal/).
- `ExponentStatement` is stated in [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/).

## Proof

The proof applies `GlobalTheory.ExpTie.Asm.expSt_of_alt` to the four hypotheses, in the same order. That proof joins the three point statements, chooses $(P_j, W_j)$ for each $j$ from `NumStAlt`, and calls `hasExpBound_at` at each recorded object with `ExCut`.

## In the Lean code

The theorem is in [ExpStOfStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExpStOfStatement.lean#L12), and the copy is in [ExpStOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExpStOf.lean#L20). Its type is the type of the copy. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`. `ExCut` is in [StatementE.lean](lean:Formalism/PieriBlockIdeals/StatementE.lean#L25).

At its one call, only the model statement depends on named hypotheses.
