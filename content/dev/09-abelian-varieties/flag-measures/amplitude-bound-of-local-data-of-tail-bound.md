---
id: amplitude-bound-of-local-data-of-tail-bound
title: The amplitude bound from local data and a tail bound
kind: theorem
decl: GlobalTheory.TypeAsm.AmpTerms.amplitudeBound_of_localData_of_tailBound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeBoundAtTermsOfLocalData
covers: 911
status: drafted
drafted_by: writer@claude
---
This theorem proves the amplitude bound `AmpP` from good local data (`LocDatC`) and a tail bound (`TailP`). Its statement form is [`amplitudeBound_at_terms_of_localData`](/entry/amplitude-bound-at-terms-of-local-data/), and the result goes to [`typeBound_of_gap`](/entry/type-bound-of-gap/). The proof bounds the vector $v(t)$ of one term by a covolume times a product of local amplitudes, one for each real place.

## Statement

**Theorem.** $\mathrm{LocDatC} \wedge \mathrm{TailP} \implies \mathrm{AmpP}$.

The three statements are in [the statement form](/entry/amplitude-bound-at-terms-of-local-data/). The conclusion is: for each relevant term $t$, $\lVert v(t) \rVert \leq w(t) \sqrt{d_\pi}\, \omega(t)\, a(j(t), \delta(t))$. Here $\omega(t)$ (`omT`) is the infimum of the weights $\omega_N(\Lambda_t)$ of [`FixedForm.main`](/entry/fixed-form-main/) over the normal forms $N$ adapted to the two flags of $t$ (`omI`, `Adapt`).

## Proof

**Constants.** $C_H$ comes from `TailP`. For $C_s \geq 0$, `localBound_productOverPlaces_label` gives $C_1$, and `amplitude_arithmetic` at $C_H$ gives $C_a$; put $C_0 = \max(C_a, 0)$. The thresholds for $C', C_l$ are the maxima of those of `TailP` at $C_1$, of `gapC_holds`, and of $40$ and $1$.

**Sizes.** From `KTwoHypotheses`, the lemma `sizes` gets $m = 2r + 2$, $v \geq 1$, $2v \leq b$, $f \geq 1$, $k \geq 40 r^4$, $k \geq 5r$ and $\mathrm{Tr}(w) > 0$.

**Local data.** `gapC_holds` gives `GapHyp D`. Then `LocDatC` gives a choice $C$ of local data with `GoodLoc`, and `TailP` gives the tail bound at each real place $\tau$.

**One term.** Fix a relevant term $t$, with $1 \leq j(t) \leq r$ (`JPosC_holds`). `localBound_productOverPlaces_label` gives $P > 0$ with $\Delta = P^2$ and a bound for the product over $\tau$ of the degree bounds `degBd`. Let $c = w(t) \sqrt{d_\pi}\, a(j(t), \delta(t))$. For each adapted normal form $N$, we show $\lVert v(t) \rVert \leq c\, \omega_N(\Lambda_t)$:

1. `adaptedNormalForm_gives_real_normal_form` puts the stabilizer at each $\tau$ in normal form; this gives measures $\mu_\tau$. `strict_fundamentalSet_integralStabilizer_exists` gives a fundamental set $K$, and `exists_sigmaFinite_quot` gives quotient measures $\nu_\tau$.
2. `termAmplitude_le_covolume_localAmplitudes` (`FactC`): $\lVert v(t) \rVert \cdot \mathrm{cov} \leq w(t) \cdot \mathrm{vol}(K) \cdot \prod_\tau \lVert J_\tau \rVert_{\mathrm{HS}}$.
3. `integralUnipotent_covolume_finite_bounded` (`CovNC`): $\mathrm{cov} \cdot L \geq 1$, with $L$ = `lossV D`.
4. `integralStabiliser_covolume_le_indexWeight` (`CovTC`): $\mathrm{vol}(K) \leq \omega_N(\Lambda_t)\, v^{k(r-j)f} L$.
5. `amplitude_hsNorm_le_degreeBound_realPlace` bounds each $\lVert J_\tau \rVert_{\mathrm{HS}}$ by $\sqrt{\dim W_\tau}$ times a constant times `degBd`; it uses the tail bound. The product of the $\sqrt{\dim W_\tau}$ is $\sqrt{d_\pi}$ (`prod_sqrt`, `prod_bound`).
6. `amplitude_arithmetic` collects $v^{k(r-j)f} L^2$, the constants and the product of degree bounds into $a(j, \delta)$. The lemma `chain` combines 2 to 6.

**Infimum.** `exists_adaptedNormalForm_relevantTerm` gives an adapted normal form. By `WeightInf.main`, a bound $c\, \omega_N(\Lambda_t)$ for each adapted $N$ gives the bound $c\, \omega(t)$.

## In the Lean code

The theorem is in [AmplitudeBoundAtTermsOfLocalData.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeBoundAtTermsOfLocalData.lean#L113). The lemmas `prod_sqrt`, `prod_bound`, `chain` and `sizes` are in the same file. The others are `GlobalTheory.T.*` statement forms of the propositions `FactC`, `CovNC`, `CovTC`, `GapC` ([ConstC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ConstC.lean#L17)) and `ProdC` ([PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L68)), and `GlobalTheory.amplitude_arithmetic`, `GlobalTheory.DegAsm.WeightInf.main`, `Formalism.L2.SG.KappaOffDiagonal.JPosC_holds`. We read their statements, not their proofs.

The hypothesis `ConcTie` is used for $j(t) \geq 1$ and for the lower bound on `Tr` that `TailP` asks. `Ties` is passed to `TailP` and, through `dsig_tie`, to `LocDatC`. The measure $\mu_\tau$ is scaled by `ENNReal.ofReal 1`, which does nothing. The properties of $\omega(t)$ as an infimum are used only through `WeightInf.main`, whose proof we have not opened.
