---
id: modularity-n-of-printed-mult-comp
title: Modularity of three-dimensional Hida families, given multiplicity and local components
kind: theorem
decl: UpperTheory.V.Z.J.D.modularity_n_of_printed_mult_comp
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ModNOf
covers: 690
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ModNAlt}$, the modularity of three-dimensional Hida families. It is a pass-through. Its two users give its result to [`linkedUnlE_alt`](/entry/linked-unl-e-alt/), which feeds the counts I and V of [The window bound VWin](/proof/vwin/).

## Statement

**Theorem.** Assume $\mathrm{HypothesesH'}$, $\mathrm{Mult}$ and $\mathrm{CompOf}$. Then $\mathrm{ModNAlt}$ holds.

$\mathrm{ModNAlt}$ says: for a prime $l$, a CM field $L$ without primitive $l$-th roots of unity, a Hida setting, a residual datum $r$ of dimension 3 with `r.V0ok`, a universal ordinary determinant ring $B$ for $r$ and a weight algebra $\Lambda$, there is an ideal $J$ of $B$ with `B.ModularAlt ι J Λ` and [$\mathrm{Num}(B, \Lambda, J)$](/entry/num-j-prime-alt/). $\mathrm{Mult}$ says that for a cuspidal $\pi$ of $\mathrm{GL}_n$, exactly $a > 0$ of the pieces $\sigma_i$ of each decomposition of the forms on the unitary group satisfy `At π σᵢ`, with $a$ fixed by the weight. $\mathrm{CompOf}$ says that `At π σ` gives `Cp σ w τ` at each split place $w$.

## Proof

The proof is `modularity_n_of_num_j_printed_mult_comp numJ'_alt hH hM hC`. That lemma builds a radical $J$ from unitary Hecke data with $n = 3$ and `QData.empty`, and gets $\mathrm{Num}$ from [`numJ'_alt`](/entry/num-j-prime-alt/).

## In the Lean code

The theorem is in [ModNOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ModNOf.lean#L17), and the lemma in [RadOfDense.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/RadOfDense.lean#L50).

$\mathrm{Mult}$ and $\mathrm{CompOf}$ are hypotheses here, but they are theorems: `mult_free` and `compOf_free` in [CompOfFree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/MultiplicityOne/CompOfFree.lean#L11). Both users pass these two theorems.
