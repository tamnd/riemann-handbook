---
id: slope-bound-of-line-large-degree
title: The slope bound from the line of large degree, restated
kind: theorem
decl: GlobalTheory.T.slope_bound_of_line_large_degree
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.SlopeBoundOfLineLargeDegreeStatement
covers: 1159
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`slopeBound_and_lemmaS_of_siegel`](/entry/slope-bound-and-lemma-s-of-siegel/), which has the content. Its one user is [`given_of_inputs`](/entry/given-of-inputs/), which takes the first half of the conclusion as part 9 of `Top.Given`.

## Statement

Suppose `LineOfLargeDegree.Statement`: for each number field $K$, each $i \ge 1$, each hermitian lattice $F$ of rank $i$ over $K$ and each $\varepsilon > 0$, there are a finite extension $K'$ of $K$ and a nonzero $v \in K'^{\,i}$ with
$$\mu(F) - \tfrac12 \log i - \varepsilon \le \widehat{\deg}_F(v),$$
where $\mu(F)$ is the slope of $F$ and $\widehat{\deg}_F(v)$ is the degree of the line spanned by $v$. Then `SlopeBoundSt` and `Prov.LemmaS` hold.

`SlopeBoundSt` is stated in the [linked entry](/entry/slope-bound-and-lemma-s-of-siegel/). `Prov.LemmaS` is an abbreviation for `SlopeBoundSt`, so the conclusion states one fact twice.

## Proof

The statement is the same as that of `slopeBound_and_lemmaS_of_siegel`, and the proof applies it.

## In the Lean code

The theorem is in [SlopeBoundOfLineLargeDegreeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLineLargeDegreeStatement.lean#L13). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Sl.slopeBound_and_lemmaS_of_siegel | ...
```

The hypothesis is in [KernelsLattice.lean](lean:GroundTheory/HeightsAndTheta/Heights/KernelsLattice.lean#L85). The abbreviation `LemmaS := @SlopeBoundSt` is in [ZhangDimensionPushDownGrassmannianHeightBounds.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/ZhangDimensionPushDownGrassmannianHeightBounds.lean#L35).
