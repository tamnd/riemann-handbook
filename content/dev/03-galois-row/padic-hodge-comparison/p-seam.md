---
id: p-seam
title: The tautological lines give the data for the period map
kind: theorem
decl: CrystallineSemistableComparison.Pb.pSeam
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.SumCoord
covers: 439
status: drafted
drafted_by: writer@claude
---
This theorem bundles four facts into the statement `BocksteinBaseChangeP`. It chooses the tautological lines as the admissible line data on models, and it proves that they have the properties that the crystalline comparison needs. Three of the four parts are one line each. The real content is the period map [`pmap`](/entry/pmap/). It sits below [the geometric steps](/entry/steps-holds/), through `cstSmooth_of_side` and `crystallineComparison.endEx`. Below it are 439 declarations.

## Statement

Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$ inside $\overline{\mathbb{Q}}_\ell$. There is a property `Amp M D` of line data $D$ on a model $M$ over $\mathcal{O}_K$ such that:

1. if `Amp M D`, then the cover $D.f$ is étale;
2. each smooth model $M$ (`M.Sm`) has some $D$ with `Amp M D`;
3. there is a period map `PMap` for smooth models with the data `dat Amp`;
4. for each perfect residue field $r$ of $\mathcal{O}_K$ (`Res l K`), there is a Frobenius map `FMap` for the same data.

## Proof

Take `Amp M D = IsTautologicalLine M.p D`. Then:

1. `isO1_etale` gives part 1.
2. `isO1_exists` gives part 2. It uses only that $M$ is projective over $\mathcal{O}_K$, from `hM.1.1`.
3. `pmap` gives part 3.
4. `fmap r Amp` gives part 4. We have not unfolded `FMap`.

## In the Lean code

The theorem is in [SumCoord.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/SumCoord.lean#L77). The statement is defined in [BocksteinBaseChangeP.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/BocksteinBaseChangeP.lean#L27). The name says "Bockstein" and "base change", but the statement has neither. `Amp` is defined in PerfectoidPullbacks/LieComplementChartContDiffAt.lean, line 16. `fmap` is in PerfectoidPullbacks/Pull.lean, line 28.
