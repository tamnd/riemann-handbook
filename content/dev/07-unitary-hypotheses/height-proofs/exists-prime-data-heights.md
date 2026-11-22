---
id: exists-prime-data-heights
title: Local point data with the height bounds, from the height inequalities
kind: theorem
decl: GlobalTheory.RunPrimeData.exists_primeData_heights
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsPrimeDataCurveLiftingHeightBounds
covers: 1385
status: drafted
drafted_by: writer@claude
---
This theorem gives, at each prime, a local point datum for a family of forms, with a bound on the sum of the local indices. Its statement form [`exists_primeData_curve_lifting_heightBounds`](/entry/exists-prime-data-curve-lifting-height-bounds/) is used in [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/). The theorem is a pass-through. It applies `exists_primeData_heights_of` to three theorems, and the work is in those.

## Statement

Use the hypotheses of [the statement form](/entry/exists-prime-data-curve-lifting-height-bounds/), with a family $G$ of forms on the algebra $X_j$ and the number $\delta$ of $G$. Let $X_j^+$ be $X_j$ with the valued points of `extAll` added. A local point datum at $\lambda$ (`LocalPointData`) is a map $y$ from the points of $G$ at $\lambda$ to the points of $X_j^+$, a form $g_0$ of weight $w_F$, and integers $c$. It defines an $\mathcal O_\lambda$-module $A_0$ and an index $I_\lambda$: the length of $A_0$ modulo the span of the forms $t_L$ of $G$.

**Theorem.** There are local point data at all $\lambda$ with `InCurve`, `InTie` and `InLiftC`, such that each $I_\lambda$ is finite, $\sum_\lambda I_\lambda \ell(\lambda)$ converges, and

$$2 \sum_\lambda I_\lambda \ell(\lambda) \le \delta \log \delta + 2 \sum_i \operatorname{meanLogSup}(\theta'_i) + \tfrac{8}{3} d(d+4)\,\delta P_{rw} |w_L| + 2(d+4)(d+1)\,\delta (2G_c + 6P_H) |w_L|.$$

Here $d$ is `dimY D j`, $|w_L|$ is the size of $w_L$, $\ell(\lambda) = \log N\lambda / [K:\mathbb{Q}]$, and $G_c, P_H, P_{rw}$ are `gcR`, `phR`, `prwR`. When $j < m$ there is a second bound of the same kind, on the sum of `Net`.

## Proof

The proof is one line:

```
exists_primeData_heights_of heightInequalities_indefinite_liftIndex
  heightInequality_definite_liftIndex exists_realisationPrimeData_curve_lifting
```

`exists_primeData_heights_of` takes the height inequality for $j < m$, the one for $j = m$, and the existence of the data $y$. It builds $g_0$ by `page_hypotheses_at_cusp` and $y$ by the third input. If $\delta = 0$, `NoPoint.heights_no_point` gives `Heights`. Otherwise it splits on $j < m$ or $j = m$ and applies the first or the second input. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsPrimeDataCurveLiftingHeightBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsPrimeDataCurveLiftingHeightBounds.lean#L14). `exists_primeData_heights_of` is in [AuxiliaryCuspFormConstantMonotone.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/AuxiliaryCuspFormConstantMonotone.lean#L96). `Heights` and `LocalPointData` are in [PublishedIntClosHolds.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/PublishedIntClosHolds.lean#L313). We have not unfolded `InCurve`, `InTie`, `InLiftC` or `meanLogSup`. The three inputs are statement forms of `HeightTop.heights_indefinite`, `HeightDefinite.heights_definite` and `PrimeData.exists_real_primeData`.
