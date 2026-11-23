---
id: line-of-key-degree
title: The line bound from the key degree bound, restated
kind: theorem
decl: GlobalTheory.T.line_of_key_degree
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.LineOfKeyDegreeStatement
covers: 811
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`LineProof.line_of_key`](/entry/line-of-key/), which has the content. Its one user is [`TopSlope.slopeBound`](/entry/top-slope-slope-bound/), which takes the constant $C$ from it in its first line.

## Statement

**Theorem.** `KeyDegSt` implies `LineSt`.

Let $D$ be a principally polarized semi-abelian datum over a number field $L$ (the Lean structure `PPData`), with Lie bundle $\overline{B}$ of rank $g$, and $h = \max(-\widehat{\deg}_n \overline{B}, 0)$. Write $|x|_\sigma$ for the hermitian length of $x \in B$ at $\sigma \colon L \to \mathbb{C}$, and $\operatorname{mean}_\sigma$ for the sum over $\sigma$ divided by $[L:\mathbb{Q}]$.

- `KeyDegSt`: there is $C \ge 0$ such that each $D$ with $g \ge 1$ has, over a finite extension $L'$ and an extension $D'$, a section $\theta$ of the polarization whose theta mean-square norms $b_\sigma$ at all archimedean frames satisfy $\operatorname{mean}_\sigma \log b_\sigma \le \frac h2 + Cg$.
- `LineSt`: there is $C \ge 0$ such that for each $D$ and each $x \ne 0$ in $B$,
$$-\operatorname{mean}_\sigma \log |x|_\sigma \le C \log(2 + g + h).$$

## Proof

The statement is the same as that of `LineProof.line_of_key`, and the proof applies it.

## In the Lean code

The theorem is in [LineOfKeyDegreeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/LineOfKeyDegreeStatement.lean#L12). The proof is the pattern `first | exact @GlobalTheory.CompanionTheory.Ar.Sl.LineProof.line_of_key | …`. Both `KeyDegSt` and `LineSt` are in [IsThetaMeanSquareNorm.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsThetaMeanSquareNorm.lean#L122).
