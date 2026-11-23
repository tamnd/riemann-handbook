---
id: real-obj-in-infinity-x-jsz
title: The real-place integral bound from uniqueness of Bessel maps
kind: theorem
decl: Formalism.L2.SG.RealObj.EnergyConvJ.BM.realObj_inInfinityX_jsz
module: CompanionTheory.AutomorphicTheory.LocalBesselUniqueness.BesselModels.RealObjInInfinityXJsz
covers: 681
status: drafted
drafted_by: writer@claude
---
This theorem proves the real-place statement `InInfinityX` for a setting with large gaps, given the uniqueness of Bessel maps `UniqGap`. It only passes its hypothesis along. The uniqueness statement is proved in [uniqueness of Bessel maps with a gap](/entry/bessel-map-uniq-gap/). The result goes to the inputs of [HypsAlt](/step/nonempty-hyps/).

## Statement

Assume `UniqGap`. Let $D$ be a datum with `GapHyp D`: $r \geq 1801$, and for each $\tau$ the parameters $b_j$ of $D$ at $\tau$ have consecutive gaps $b_{j+1} - b_j \geq 16 r^{19}$. Let $X$ be a setting over $D$, $u, u'$ two words and $s > 0$. Then `InInfinityX X u u' s` holds. This is the conjunction of three facts:

1. there is a disintegration constant $C > 0$ for $X, u, u', s$;
2. a coordinate condition `CoordOK`;
3. $\int \|\cdot\|_{HS}^2 \, d\nu \leq 1/\deg X$, where the integrand is a squared Hilbert-Schmidt norm of a Gram operator, $\nu$ is a measure `nuM`, and $\deg X = \prod_v d_v$.

We have not unfolded the disintegration, the Gram operator or `nuM`.

## Proof

`inputs2_of` adds `UniqGap` to three proved facts to make `Inputs2`. From this, `stepIntG_holds` gives `StepIntG` and `stepConvG_holds` gives `StepConvG`. Both are statements, under `GapHyp`, about each good point $c$; we have not unfolded them. Then `realObj_inInfinityX_ofG` takes both and calls `inInfinityXAt`.

## In the Lean code

The theorem is in [RealObjInInfinityXJsz.lean](lean:CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/RealObjInInfinityXJsz.lean#L17). `InInfinityX` is in [RealObj.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/RealObj.lean#L172). `UniqGap` is a second copy of the definition `BesselMapUniqGap`. The suffix `jsz` is not explained in the code and does not describe the statement.
