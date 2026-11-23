---
id: abelian-cm-comp-laws-bound
title: The mean slope bound for abelian CM fields, second name
kind: theorem
decl: GlobalTheory.T.abelian_cm_comp_laws_bound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.AbelianCmCompLawsBoundStatement
covers: 1169
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the mean slope bound](/entry/top-mean-all/). It has the same statement, and its proof only calls that theorem. [The positivity statement from the volume theorem](/proof/weil-bound/) uses it once, to get the constant $C$ of `DeepStR`. The real content is in [the entry of `top_meanAll`](/entry/top-mean-all/).

## Statement

**Theorem.** Assume `NefRR`, the bundle `Top.Given`, the existence of a full intersection system, the birational pullback formula, `GoodTowerExistsX` and `VolumeTheoremX`. Then there is $C \geq 0$ with this property. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with at least two CM types. Take a datum with $1 \leq q$ and $3q + 1 \leq p + q$, a level that is good at all primes, and the data $(U, h, e)$ with the laws `CompLaws`. Suppose that the primes of $2 \operatorname{disc} E$ and of the level number at most $4\,\#\mathrm{CMType}\,(p+q)^2$, and that all base points have absolute value $x$. Then

$$\texttt{MeanAll}\ U\ x\ \bigl(\log \mathrm{rd}(E) + |\operatorname{Re} L'/L(1,\chi_d)|\bigr)\ C.$$

The [entry of `top_meanAll`](/entry/top-mean-all/) gives all hypotheses and unfolds `MeanAll`.

## Proof

The proof is `top_meanAll`. Nothing else is done.

## In the Lean code

The theorem is in [AbelianCmCompLawsBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianCmCompLawsBoundStatement.lean#L16). The proof is the tactic `first | exact @top_meanAll | ...`, and the first branch closes the goal. The caller is [DeepStROfVolume.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/DeepStROfVolume.lean#L24). The file imports `Mathlib` twice, at lines 1 and 3.

The name speaks of abelian CM fields and of `CompLaws`. These are two hypotheses. The conclusion is a lower bound on the mean slope, and the name does not say so.
