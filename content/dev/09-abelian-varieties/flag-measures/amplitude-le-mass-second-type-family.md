---
id: amplitude-le-mass-second-type-family
title: Cancellation in one family of second-type terms, statement form
kind: theorem
decl: GlobalTheory.T.amplitude_le_mass_secondType_family
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeLeMassSecondTypeFamilyStatement
covers: 408
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`amp_le_mass`](/entry/amp-le-mass/). Its only user is [`family_bound`](/entry/family-bound/), where it is the cancellation step. The content is in [`amp_le_mass`](/entry/amp-le-mass/).

## Statement

The notation $a(d, P)$, $m(d, P)$ and $q$ is in [the entry for `ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/). The family $\mathcal{F}(\beta, J, \beta_J)$ is defined in [the entry for its mean square](/entry/hermitian-double-coset-second-type-family-amp-sq-le/).

**Theorem.** Let $S$ be a datum of type `Frames L r k` over a nonarchimedean local field of characteristic $0$, with $4r + 7 \leq k$. Then for all $\beta, J, \beta_J$ and every datum $d$:
$$\bigl|a\bigl(d, \mathcal{F}(\beta, J, \beta_J)\bigr)\bigr| \leq 7 \, q^{1 - (k - 2r - 3)} \, m\bigl(d, \mathcal{F}(\beta, J, \beta_J)\bigr).$$

The first half of `basic_inequality` gives the trivial bound $|a| \leq m$. Since $k \geq 4r + 7$, the exponent $1 - (k - 2r - 3) = 2r + 4 - k$ is at most $-2r - 3$, so the theorem says that the phases cancel and save a factor $7 q^{2r+4-k}$.

## Proof

The proof is the term `GlobalTheory.HL.AmpCancel.amp_le_mass`. There is nothing else.

## In the Lean code

The theorem is at [AmplitudeLeMassSecondTypeFamilyStatement.lean line 9](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeLeMassSecondTypeFamilyStatement.lean#L9). The two statements have the same text, so the first branch of the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` closes the goal. The file sets `maxHeartbeats` to 1,000,000 for this one line. In Lean both sides are in $[0, \infty]$: the left side is `ENNReal.ofReal ‖S.amp d _‖`, and the mass is an extended real.
