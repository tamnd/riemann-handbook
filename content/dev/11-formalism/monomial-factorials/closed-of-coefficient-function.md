---
id: closed-of-coefficient-function
title: Integral polynomials over a fraction field from coefficient maps
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_coefficient_function
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ClosedOfCoefficientFunction
covers: 2480
status: drafted
drafted_by: writer@claude
---
This theorem is the ninth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_symmetric_windows`](/entry/closed-of-symmetric-windows/) calls it. It turns the hypothesis `RestFunY` on coefficient maps into the span statement `RestYbc`, and passes the rest on to [`closed_of_symmetric_finite`](/entry/closed-of-symmetric-finite/).

## Statement

`RestFunY` is stated in [`closed_of_orthogonal_lattice`](/entry/closed-of-orthogonal-lattice/), `OrthLat` in [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/), and `SymmetryFinitenessWindowLevelDimOnAdmissible D` in [`closed_of_symmetric_windows`](/entry/closed-of-symmetric-windows/).

Let $O$ be a domain, $K$ its fraction field (`KK O` is `FractionRing O`), and $\iota \colon \mathbb{Q}_p \to K$ a ring map. For letters and conditions $(J, M)$, let $Y_K \subseteq K[x]$ be the space `Yjt` and $Y \subseteq \mathbb{Q}_p[x]$ the space `Y`, both cut out by the same support and stability conditions (`YCond`). Let $Y_O = Y_K \cap O[x]$ (`YjtZ`) and $Y_{\mathbb{Z}_p} = Y \cap \mathbb{Z}_p[x]$ (`YZ`), with $x$ the variables.

- `RestYbc`: each $y \in Y_O$ lies in the $K$-span of $\iota(Y_{\mathbb{Z}_p})$, where $\iota$ acts on coefficients.

**Theorem.** For each datum $D$, `RestFunY`, `OrthLat` and `SymmetryFinitenessWindowLevelDimOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The proof is `closed_of_symmetric_finite` applied to `restYbc_of_funY hF`, `hO` and `h`. The work is in `restYbc_of`, which needs two more facts, both proved.

1. `RestDecomp` (`restDecomp_proved`): each $y \in K[x]$ is a finite sum $y = \sum_k b_k\, \iota(f_k(y))$, with $b_k \in K$, each $f_k \colon K \to \mathbb{Q}_p$ additive with $f_k(\iota(a) z) = a f_k(z)$, and $f_k(y)$ the result of $f_k$ on each coefficient. Take a $\mathbb{Q}_p$-basis $b_1, \dots, b_n$ of the span $V$ of the coefficients of $y$, and let $f_k$ be the $k$-th coordinate after a left inverse $K \to V$ of the inclusion.
2. `RestClear` (`restClear_proved`): for each $F \in Y$ there is $e \ge 0$ with $p^e F \in Y_{\mathbb{Z}_p}$. Choose $e$ with $p^e$ larger than the sum of the norms of the coefficients.

Let $y \in Y_O$. Then $y \in Y_K$. Write $y$ as in (1). By `RestFunY`, each $f_k(y)$ is in $Y$. By (2), $p^{e} f_k(y) \in Y_{\mathbb{Z}_p}$ for some $e$. So $\iota(f_k(y)) = \iota(p^e)^{-1}\, \iota(p^e f_k(y))$ is in the $K$-span of $\iota(Y_{\mathbb{Z}_p})$, and so is $y$.

## In the Lean code

The theorem is in [ClosedOfCoefficientFunction.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfCoefficientFunction.lean#L8). The lemmas it calls:

- `restYbc_of_funY`, `restYbc_of`, `restDecomp_proved`, `restClear_proved` and `cmap`, in [RestDecompProved.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestDecompProved.lean#L120). `RestYbc` is in [FinrankEqSpanGen.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/FinrankEqSpanGen.lean#L56).
- `Yjt` and `YjtZ` in [ObjSeg.lean](lean:Formalism/SharpRestriction/GrowthBounds/ObjSeg.lean#L30); `Y` and `YZ` in [GoodCount.lean](lean:Formalism/MahlerMeasure/GoodCount.lean#L55).
- `closed_of_symmetric_finite`, in [SymmetryFinitenessWindowLevelDimOnAdmissible.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SymmetryFinitenessWindowLevelDimOnAdmissible.lean#L29).

The hypotheses `hO` and `h` pass through unchanged. `RestFunY` is not proved in this file; it comes in as `hF` and is supplied higher up, by `restFunY_proved` in [`closed_of_orthogonal_lattice`](/entry/closed-of-orthogonal-lattice/). The spaces `Yjt` and `Y` are built from two different letter types (`ChainLetters` and `Letters`, linked by `gmL`), so the claim that they use "the same" conditions is through `gmL`, which we have not unfolded.
