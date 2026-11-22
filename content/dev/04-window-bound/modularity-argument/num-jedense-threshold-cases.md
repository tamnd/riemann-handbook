---
id: num-jedense-threshold-cases
title: The multiplicity comparison on a Hida family, from the dimension count
kind: theorem
decl: UpperTheory.V.Z.Desc.V0.numJEDenseThresholdCases
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.CountE
covers: 682
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{NumJEAlt}$. [Its restatement `numJ'_alt`](/entry/num-j-prime-alt/) gives it to [modularity of three-dimensional Hida families](/entry/modularity-n-of-printed-mult-comp/). It is a pass-through: it supplies the eight inputs of the lemma `numJE_alt`.

## Statement

**Theorem.** $\mathrm{NumJEAlt}$ holds.

$\mathrm{NumJEAlt}$ is $\mathrm{NumJAlt}$ of [the restatement](/entry/num-j-prime-alt/) without the hypothesis `r.V0ok`: for points $x, y$ over $J$ of the same weight, $x$ arithmetic and $y$ good, $1 \le \mu_\varepsilon(x) \le \mu_\varepsilon(y)$.

## Proof

The main input is $\mathrm{ZEqDimEAlt}$, from `z_eq_dim_e_of_count_e_res_eq_inv_loc_kir` applied to [`countE'_alt`](/entry/count-e-prime-alt/) and local statements. It says: there are a finitely supported $a \colon \mathrm{GL}_n(L_{v_0}) \to \mathbb{Z}$ and an $N$ prime to $l$ such that any two dimensions $D, D'$ of the part of `zPart` cut by $(a, N)$ (`IsDimEAlt`) satisfy $1 \le D = D'$.

`numJE_alt` then argues so. If $J$ is the unit ideal, the zero module works. Otherwise `datHecke` builds $M$ and `EEx` the idempotent $\varepsilon$ from $(a, N)$. `absDimE` shows that $\mu_\varepsilon(x)$ and $\mu_\varepsilon(y)$ are such dimensions, so $1 \le \mu_\varepsilon(x) = \mu_\varepsilon(y)$.

## In the Lean code

The theorem is in [CountE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CountE.lean#L23), `numJE_alt` in [TNumJE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TNumJE.lean#L171), and $\mathrm{ZEqDimEAlt}$ in [ZEqDimE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ZEqDimE.lean#L56). We have not opened `absDimE` or `datHecke`.

The proof gets equality, and the statement keeps only the inequality. The name says "dense threshold cases"; the statement is a multiplicity comparison.
