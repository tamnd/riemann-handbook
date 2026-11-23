---
id: covolume-integral-unipotent-radical-real-points
title: The covolume of the integral unipotent radical, statement form
kind: theorem
decl: GlobalTheory.T.covolume_integral_unipotentRadical_real_points
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CovolumeIntegralUnipotentRadicalRealPointsStatement
covers: 376
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`covolume_N`](/entry/covolume-n/). Its only user is [`CovDom.main`](/entry/cov-dom-main/), which supplies the data of the global datum. The content is in [`covolume_N`](/entry/covolume-n/).

## Statement

**Theorem.** Let $E/F$ be a CM extension of number fields that is unramified at all finite primes. Let $J$ be a nondegenerate Hermitian matrix of size $n = 2r + k + 1$ over $E$, and let $\Lambda$ be a self-dual lattice for $J$. Let $P$ be a frame, $f$ a dual tuple, $A_w$ model matrices at the infinite places $w$ of $E$, and $s_0, \dots, s_{r-1} > 0$ scales, with the conditions listed in [the entry below](/entry/covolume-n/). Then fundamental domains for the integral unipotent group exist. Each of them has measure
$$|d_F|^{-(k+1)r^2 - 4(r^3 - r)/3 - 3r/2}\Bigl(\prod_{a} s_a^{\,4(r-a)+2k}\Bigr)^{\#\{w\}}$$
for the product over $w$ of the Lie algebra Haar measures with scale 1 on the model unipotent group.

## Proof

The proof is the term `GlobalTheory.SnMass.VolN.covolume_N`. There is nothing else.

## In the Lean code

The theorem is at [CovolumeIntegralUnipotentRadicalRealPointsStatement.lean line 7](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeIntegralUnipotentRadicalRealPointsStatement.lean#L7). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The largest exponent, at $a = 0$, is $4r + 2k$.
