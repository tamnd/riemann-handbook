---
id: cut-effective-divisor
title: Cutting a vertical divisor by an effective divisor, statement form
kind: theorem
decl: GlobalTheory.T.cut_effective_divisor
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.CutEffectiveDivisorStatement
covers: 459
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It states `CutByEffectiveDivisor.Statement` and proves it by a call to [`CutClosed.main`](/entry/cut-closed-main/), which has the real content. It sits below [the relations for flag pairs](/entry/top-rel-relations/), in the part of the proof that computes intersection numbers on models over a discrete valuation ring.

## Statement

Let $O$ be a discrete valuation ring with a uniformizer $\varpi$, let $P$ be a model of relative dimension $d + 1$ in a ring of multihomogeneous polynomials over $O$, let $f/g$ be a vertical divisor of degree $b$ on $P$, and let $s \notin P$ be multihomogeneous of degree $c$. Assume that $f/g$ is a vertical divisor on each horizontal component of $\operatorname{div}(s)$. Then the intersection number of $\operatorname{div}(f/g)$ with $c$ and a list $L$ of degrees equals the intersection number of $\operatorname{div}(s)$ with $f/g$ and $L$. The exact form, with all definitions, is in [`CutClosed.main`](/entry/cut-closed-main/).

## Proof

The proof is `first | exact @CutClosed.main | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [CutEffectiveDivisorStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/CutEffectiveDivisorStatement.lean#L5). It fixes the universe of $O$ to `0`. It has two direct users: `verticalDivisorsCommute`, which derives from it that two vertical divisors commute, and `segreFlagClosureCut`, a step on Segre flags. We have not traced the chain of lemmas that links them to the relations for flag pairs.
