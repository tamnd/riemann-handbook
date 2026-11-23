---
id: kato-euler-system-integrality
title: The Euler system of zeta classes, by name
kind: theorem
decl: UpperTheory.Kd.K4.kato_eulerSystem_integrality
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.NormProducts.AdmissibleWeightedDataMonoCoef
covers: 1492
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives [`K4.top`](/entry/k4-top/) the name that the proof of [the unramified zeta theorem](/entry/zeta-ur/) uses. That proof passes it, with [the Hodge-Tate law for smoothed zeta classes](/entry/smoothed-zeta-class-hodge-tate-law/) and a nonvanishing result for Hecke projections, to [`kato_global_unit_law_of_smoothed_classes`](/entry/kato-global-unit-law-of-smoothed-classes/), where it is the hypothesis `h4`. The mathematics is in [the entry for `K4.top`](/entry/k4-top/).

## Statement

The statement is the proposition `KatoEulerSystemIwasawaClassStatement`, word for word the statement of `K4.top`. In short: let $\ell$ be an odd prime, $g$ a newform of weight $2e+1$ with $e \geq 1$, $W$ a continuous integral $\ell$-adic representation with the conditions `Nf` and `SrcUr`, and $X$, $N$, $c$, $d$, $g_m$, a function $c_w$ on $\mathbb{Z}/N$ that is not identically zero, and a character $\psi$ that satisfy `AdmWn`, with $g_m(r_0) \in \Gamma_1(N)$ and $\ell \nmid N$. Then there are $c_0$, $m$, a larger coefficient ring, a finite set of places, a zeta system $Y_r$ (`IsZWc`) and a class $y$ such that: each $Y_r$ is a cocycle for $W$ twisted by the inverse cyclotomic character mod $\ell^r$; the $Y_r$ are norm compatible, continuous, locally constant mod $\ell^n$ and integral; at each level $r$, $y$ is congruent to the sum of $Y_r$ twisted by $u^{-e}\chi(u)$; and $\ell^m y$ and $\ell^m Y$ satisfy `Sys`, `IwSys2` and `SpLink`, which we have not unfolded.

## Proof

The proof is the single term `UpperTheory.Kd.K4.top`. Nothing else happens.

## In the Lean code

The theorem is at [line 208 of AdmissibleWeightedDataMonoCoef.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L208), and `top` is at [line 132](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L132). The statement is defined in [SmoothedZetaClassHodgeTateLawStatement.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/SmoothedZetaClassHodgeTateLawStatement.lean#L11). The name says "integrality", but integrality of the $Y_r$ is one clause of eleven. The size 1,492 is the subtree of `top` plus this declaration.
