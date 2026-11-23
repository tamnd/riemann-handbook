---
id: lintegral-hilbert-schmidt-norm-sq-bessel-amplitude-le
title: The square integral of the Bessel amplitude, statement form
kind: theorem
decl: GlobalTheory.T.lintegral_hilbertSchmidtNormSq_besselAmplitude_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LintegralHilbertSchmidtNormSqBesselAmplitudeLeStatement
covers: 542
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`lintegral_hsNormSq_ampJ_le`](/entry/lintegral-hs-norm-sq-amp-j-le/). It serves the step [nonempty hypotheses](/step/nonempty-hyps/). Its users are `schurSt_of_big_tie` and `schurSt_of_big_tie_uniform`. They have no entries. The content is in [`lintegral_hsNormSq_ampJ_le`](/entry/lintegral-hs-norm-sq-amp-j-le/).

## Statement

Let $G$ be the unitary group of the model form of size $2r + k + 1$. Let $\sigma$ be a unitary representation of $G$ on a Hilbert space with formal degree $d$, and let $v_0 \ne 0$ be a vector whose normalisation is smooth. Let $B$ and $B'$ be Bessel maps into finite-dimensional spaces $W_p$ and $W_q$. Put $\Phi(g) = B(\sigma(g) v_0)$ and $\Phi'(g) = B'(\sigma(g) v_0)$.

**Theorem.** Suppose that multiplicity one holds on each side, that $\|\Phi\|^2 = c_0 \dim W_p$ and $\|\Phi'\|^2 = c_0 \dim W_q$ on the quotients with some $c_0 > 0$, and that $\nu$ disintegrates the Haar measure over the regular double cosets. Then
$$\int \bigl\|J_{c_0}(\Phi, \Phi')(\gamma)\bigr\|_{HS}^2 \, d\nu(\gamma) \le \frac{\dim W_p \cdot \dim W_q}{d}.$$

Here $J_{c_0}$ is the amplitude `ampJ`. [The entry below](/entry/lintegral-hs-norm-sq-amp-j-le/) lists all hypotheses.

## Proof

The proof is the term `GlobalTheory.Amp.SchurNorm.lintegral_hsNormSq_ampJ_le`. There is nothing else.

## In the Lean code

The theorem is at [LintegralHilbertSchmidtNormSqBesselAmplitudeLeStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LintegralHilbertSchmidtNormSqBesselAmplitudeLeStatement.lean#L10). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The users call it at [AmplitudeSchurBoundUniformConstants.lean line 52](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/AmplitudeSchurBoundUniformConstants.lean#L52) and [MeasurableBcWeight.lean line 261](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/MeasurableBcWeight.lean#L261).
