---
id: exp-st-of-alt
title: The exponent bound from three point statements
kind: theorem
decl: GlobalTheory.ExpTie.Asm.expSt_of_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExpStOf
covers: 1356
status: drafted
drafted_by: writer@claude
---
This theorem proves the exponent statement `ExponentStatement` from a combinatorial inequality and three statements at points of families. It is the only content of its caller [`expSt_of_num_sumExp_model`](/entry/exp-st-of-num-sum-exp-model/), which is a renaming. The result goes to [`exponent_bound_of_unitaryThetaStandardTheorems_alt`](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/) in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The local work is in [`hasExpBound_at`](/entry/has-exp-bound-at/), which is 1,355 of the 1,356 declarations below this theorem.

## Statement

Families $F$, the class `FamHyp` and the predicate `Closed` are as in the [step on `Closed`](/step/closed-def/). At a point $p$ of $F$ at height $x$ and index $i$, write $L = L(x,i)$ and let $j$ run over the lift indices.

**Theorem.** Assume:

1. `ExCut`: for all $N$, $\lambda$, a prime $\ell$, $lo \in \mathbb Z$ and $w \in \mathbb N$ such that `res N λ` is antitone and $lo \le \mathrm{UN}(N, \lambda, a) \le lo + w$ for $a < N$, and for each $a \le N$, the exponent `exZ` at $N$ is at most the sum of the exponents at $a$ and at $N - a$ (shifted), plus $a(N-a)\log_\ell w$;
2. `NumStAlt`: in the closed sense, eventually at points $p$ with `More p`, for each $j$ there are parameters $P_j$ and weights $W_j$ with `Dict L j P_j W_j` and `NumOk P_j W_j`;
3. `ExponentSumStatement`: for each such $(j, P, W)$, each $t$ and each place $w$, a lattice inclusion `LIncl` holds at level `W.JA P` at the prime under $w$;
4. `ModelStatement`: for each such $(j, P, W)$ and each twisted place $w$ in the range `W.WRange P`, the local model `ModelAt p j P W w` holds (a cover by Hida settings in which the prime is not a unit).

Then `ExponentStatement` holds. That is, in the closed sense for `FamHyp`, eventually at points, for each record object $O$ and all $C, C_H$, the bound `HasExpBound` holds. It says: the exponents $J_0(w, j)$ at twisted places are nonnegative, and there are numbers $J_p(j, \ell) \ge 0$ with $J_0(w,j) \le J_p(j, \ell_w)$ and $\sum_{\ell \in Q} J_p(j,\ell) \log \ell \le E_J$ for each finite set $Q$ of primes.

## Proof

`Closed.and` joins the three point statements into one. The proof takes the largest of their three height thresholds, and the constant $c_0 = 0$ for the record objects. At a point, it chooses $P_j$ and $W_j$ from statement 2. Then [`hasExpBound_at`](/entry/has-exp-bound-at/) gives the bound, from `ExCut`, statements 3 and 4, and four equalities (`m_eq`, `x_eq`, `eps_eq`, `realisedChain_torus_eq`) that come from the hypothesis `RecAt` on the object. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExpStOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExpStOf.lean#L20). The four statements are in [ModelStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStatement.lean#L22), [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L43) and [StatementE.lean](lean:Formalism/PieriBlockIdeals/StatementE.lean#L25). We have not unfolded `exZ`, `Dict`, `NumOk` or `LIncl`.

The proof is the same text, line for line, as the proof of `expSt_of` in [ExpansionOfNumericsModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L80). There the statements use `AtPts`, with the point condition `Rows`. Here they use `AtPtsAlt`, with the point condition `PointConditions'`.

The conditions on the constant record $c$ (`c0 ≤ c.C` and `ConstBad c`) are not used: the proof takes $c_0 = 0$ and ignores both. The file has an empty `section Point` that only declares variables. In `exponent_bound_of_unitaryThetaStandardTheorems_alt`, `ExCut`, `NumStAlt` and `ExponentSumStatement` are proved theorems, so only `ModelStatement` carries hypotheses.
