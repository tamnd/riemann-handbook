---
id: slope-bound-of-large-degree-line
title: The Lie slope bound from the Siegel lemma and the key degree bound, restated
kind: theorem
decl: GlobalTheory.T.slope_bound_of_large_degree_line
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.SlopeBoundOfLargeDegreeLineStatement
covers: 851
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`TopSlope.slopeBound`](/entry/top-slope-slope-bound/), which has the content. Its one user is [`slopeBound_and_lemmaS_of_siegel`](/entry/slope-bound-and-lemma-s-of-siegel/), which supplies the second hypothesis from the reduction lemmas `key_bad_reduction_holds` and `key_degree_of_bad_reduction`.

## Statement

Suppose:

1. `LineOfLargeDegree.Statement`, the absolute Siegel lemma: for each number field $K$, each hermitian lattice $F$ of rank $i \ge 1$ over $K$ and each $\varepsilon > 0$, there are a finite extension $K'/K$ and $v \ne 0$ with $\mu(F) - \frac12 \log i - \varepsilon \le \widehat{\deg}_F(v)$;
2. `KeyDegSt`, the key degree bound: there is $C \ge 0$ such that each principally polarized semi-abelian datum $D$ over a number field $L$, with Lie bundle of rank $g \ge 1$ and $h = \max(-\widehat{\deg}_n B, 0)$, has, after a finite extension, a theta section whose theta mean-square norms $b_\sigma$ satisfy $\operatorname{mean}_\sigma \log b_\sigma \le \frac{h}{2} + C g$.

Then `SlopeBoundSt` and `Prov.LemmaS` hold. `SlopeBoundSt` is the bound $\mu_{\max}(\overline{B}) \le C' \log(2 + \operatorname{rk} B + h)$ for the Lie bundle $\overline{B}$, stated in full in [the parent entry](/entry/slope-bound-and-lemma-s-of-siegel/). `Prov.LemmaS` is an abbreviation for `SlopeBoundSt`.

## Proof

The statement is the same as that of `TopSlope.slopeBound`, and the proof applies it.

## In the Lean code

The theorem is in [SlopeBoundOfLargeDegreeLineStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLargeDegreeLineStatement.lean#L12). The proof is the pattern `first | exact @GlobalTheory.CompanionTheory.Ar.Sl.TopSlope.slopeBound | …`. `KeyDegSt` is in [IsThetaMeanSquareNorm.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsThetaMeanSquareNorm.lean#L122). Its name differs from that of [`T.slope_bound_of_line_large_degree`](/entry/slope-bound-of-line-large-degree/), two levels up, only in the order of the words. The two theorems have different hypotheses.
