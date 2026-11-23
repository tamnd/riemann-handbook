---
id: cov-nformula-pf-main
title: The closed formula for the unipotent covolume
kind: theorem
decl: GlobalTheory.CovNFormulaPf.main
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CovolumeUnipotentIntegralNormalisedHaar
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem proves the proposition `CovNFormula`. That proposition gives the covolume of the integral unipotent radical at the infinite places in closed form. The step [nonempty hypotheses](/step/nonempty-hyps/) needs it as one of the inputs with no hypotheses. Its users are [`loop_rows_closed_gap`](/entry/loop-rows-closed-gap/) and a renaming `T.covolume_unipotentIntegral_normalisedHaar`. The volume computation is in [`transportedFundDomain_volume_classical`](/entry/transported-fund-domain-volume-classical/). This theorem only changes the normalisation of the Haar measure.

## Statement

Let $D$ be the global datum, with CM field $E$ over the totally real field $F$. Let $r$ and $k$ be the integers `D.R.rS` and `D.R.k`, and let $f$ be the number of elements of the index set `Tau`. Let $v$ be `D.host.v`. Then $2v = |d_E|^{1/[E:\mathbb Q]}$ is the root discriminant of $E$.

**Theorem.** For every setting $X$, every `Full` record $Y$, every $\theta > 0$, every choice $C$ and every word $u$,
$$\mathrm{covN}(C, u) = \bigl(\theta\,(2v)^{r^2 + r/2}\bigr)^{f}.$$

Here $\mathrm{covN}(C,u)$ is the real number $\mu^{f}(\mathrm{tr}(F_N(u)))$. The set $F_N(u)$ is the fundamental domain for the integral unipotent group, a field of $Y$. The map tr sends it to $f$ copies of the model unipotent group $N$. The measure $\mu$ on $N$ is the Lie algebra Haar measure with scale $\kappa = (2v)^{-rk}\theta$.

## Proof

1. The Haar measure on $N$ with scale 1 is sigma-finite. This comes from `haarLie_isHaarOn_Nset`.
2. The definition of the Haar measure is $\kappa$ times the image of Lebesgue measure. So the measure with scale $\kappa$ is $\kappa$ times the measure with scale 1.
3. The local lemma `pi_const_smul'` says that the product of $f$ copies of $c\mu$ is $c^f$ times the product of copies of $\mu$.
4. The [volume formula](/entry/transported-fund-domain-volume-classical/) gives the measure with scale 1 as $(2v)^{(r^2 + rk + r/2)f}$.
5. The product is $((2v)^{-rk}\theta)^f (2v)^{(r^2+rk+r/2)f}$. The factor $(2v)^{rk}$ cancels. The lemma `rdE_ge_one` gives $2v \ge 1$, so the power rules for real exponents apply.

## In the Lean code

The theorem is at [CovolumeUnipotentIntegralNormalisedHaar.lean line 21](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeUnipotentIntegralNormalisedHaar.lean#L21). The helper `pi_const_smul'` is at [line 13](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeUnipotentIntegralNormalisedHaar.lean#L13). The proposition and the exponent `eN` are at [LoopBCovN.lean line 18](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopBCovN.lean#L18). In that file `covWinN_of`, `covWinN_sizes` and `covN_pos` take the proposition as a hypothesis. The scale $(2v)^{-rk}\theta$ is the normalisation in the file name. It removes the dependence of the volume on $k$.
