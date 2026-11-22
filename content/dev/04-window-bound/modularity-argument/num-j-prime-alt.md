---
id: num-j-prime-alt
title: The multiplicity comparison on a Hida family, restated
kind: theorem
decl: UpperTheory.V.Z.J.D.numJ'_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ModNOf
covers: 683
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{NumJAlt}$, an input of [modularity of three-dimensional Hida families](/entry/modularity-n-of-printed-mult-comp/). It is a pass-through: a restatement of [`numJEDenseThresholdCases`](/entry/num-jedense-threshold-cases/).

## Statement

**Theorem.** $\mathrm{NumJAlt}$ holds.

$\mathrm{NumJAlt}$ says: assume $\mathrm{HypothesesH'}$, $\mathrm{Mult}$ and $\mathrm{CompOf}$. Let $l$ be a prime, $L$ a CM field, $s$ a Hida setting, $1 \le n \le 4$, $V$ a level with $V.S' = s.S$, $r$ a residual datum of dimension $n$ with `r.V0ok`, $B$ the universal ordinary determinant ring, $\Lambda$ a weight algebra that is a domain, and $J$ a radical ideal of $B$ that comes from unitary Hecke data (`R.IsJ B K J`). Then $\mathrm{Num}(B, \Lambda, J)$ holds.

$\mathrm{Num}(B, \Lambda, J)$ says: there are a module $M$ over $B$ and $\Lambda$, a datum `Dat` for $(\Lambda, J, M)$ and an idempotent $\Lambda$-endomorphism $\varepsilon$ of $M$ such that, for points $x, y$ of $B$ that vanish on $J$, of the same weight, with $x$ arithmetic, $y$ good and both irreducible,

$$1 \le \mu_\varepsilon(x) \le \mu_\varepsilon(y).$$

We have not unfolded the multiplicity $\mu_\varepsilon$ (`muE`).

## Proof

The proof applies `numJEDenseThresholdCases` and drops `r.V0ok`. Its conclusion $\mathrm{NumE}$ has the same body as $\mathrm{Num}$.

## In the Lean code

The theorem is in [ModNOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ModNOf.lean#L15). $\mathrm{NumJAlt}$ is in [NumJ.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/NumJ.lean#L26). `Num` is in [AbsGood.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/AbsGood.lean#L21) and `NumE` in [EigBoxE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CuspidalDescent/GLDenseRanges/EigBoxE.lean#L102).

The hypothesis `r.V0ok` of $\mathrm{NumJAlt}$ is not needed. `Num` and `NumE` are one definition with two names.
