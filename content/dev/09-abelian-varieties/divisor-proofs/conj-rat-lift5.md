---
id: conj-rat-lift5
title: Galois conjugates of a rational theta lift
kind: theorem
decl: GlobalTheory.ConjRatLiftFive.conjRatLift5
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConjugatesOfRationalThetaLiftFromCharacterisatio
covers: 619
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ConjRatLift5}$: a rational [[theta|6WB6TKE70H]] lift has a unique rational form, and its conjugates under the complex embeddings are again theta lifts, up to a phase and a central shift. It is the proof behind the [restated form](/entry/conjugates-of-rational-theta-lift-from-characterisation/), which is used below the step [the hypotheses are nonempty](/step/nonempty-hyps/).

## Statement

Let $R$ be a real datum. For each index $i$ and each embedding $\sigma \colon L \to \mathbb{C}$ of the coefficient field, $R$ gives a space $H_{i,\sigma}$ of forms, an action of a finite group by $g_\sigma$, and a $\sigma$-semilinear map $j_\sigma$ from the rational forms into $H_{i,\sigma}$. For the base embedding $\sigma_0$ it gives a map $j_V$ from rational vectors into a space $H_V$ and a theta lift $\theta \colon H_V \to H_{i,\sigma_0}$. Say that $y$ is a *rational lift* of $x$ with phase $ph$ if $j_{\sigma_0}(y) = ph \cdot \theta(j_V(x))$. Say that $\sigma$ is *over $K$* if $\sigma$ and $\sigma_0$ agree on the field $K$ of the datum.

**Theorem.** Assume the conditions $\mathrm{Core5}$, $\mathrm{IsStdChar}$, $\mathrm{FWTie}$, $\mathrm{BarTie}$, $\mathrm{IoExt}$, $\mathrm{LUnif}$ and $\mathrm{OMPins}$ on $R$, and the condition $\mathrm{OneMapOf}$ at index $i$ with the phase $ph$. Then:

1. each rational $x$ has exactly one rational lift $y$ with phase $ph$;
2. for each base datum $c_0^L$ and each $\sigma$ over $K$, $\mathrm{ConjAt}(R, i, \sigma, ph, c_0^L)$ holds;
3. for each $\sigma$ not over $K$, $\bar\sigma$ is over $K$ and $\langle j_\sigma y, j_\sigma y' \rangle = \overline{\langle j_{\bar\sigma} y, j_{\bar\sigma} y' \rangle}$ for all $y, y'$.

$\mathrm{ConjAt}$ says: there is a conjugate datum (characters $\mu', \eta'$, adelic forms $H$, a Weil representation and a theta lift $th$), a phase $u$ with its operator $U$, a central element $z$ and a scalar $\kappa$ with $|\kappa| = 1$, such that $U(j_\sigma y) = \kappa \, g_\sigma(z) \, th(j(x))$ whenever $y$ is the rational lift of $x$. At $\sigma_0$ one has $u = 1$. We have not unfolded the other hypotheses.

## Proof

The proof first derives three facts: evaluation at the unit vector is injective (`evInj_of_isModels_of_tie`), the forms evaluate (`fw.evaluates`), and $j_{\sigma_0}$ is injective, because $\mathrm{LUnif}$ says that $j_{\sigma_0}$ keeps linearly independent families independent (`inj_of_indep`).

1. `base_lift5` writes each rational lift as a class sum, so a lift exists. It is unique since $j_{\sigma_0}$ is injective.
2. If $\sigma = \sigma_0$, `conjAt_base5` takes $u = 1$ and $U$ the identity. Otherwise the proof calls [`conjugateRationalLift_at_nonBaseEmbedding`](/entry/conjugate-rational-lift-at-non-base-embedding/).
3. This is the third clause of `centralShift_phase_conjReadings_fiveClauses`, with `labels_overK` and `overK_iff_good_ofFive`.

## In the Lean code

The theorem is in [ConjugatesOfRationalThetaLiftFromCharacterisatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L227). `ConjRatLift5` and `GalOut` are in [FormalDegreeUpperC.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FormalDegreeUpperC.lean#L101). `IsRatLift`, `OverK` and `ConjAt` are in [WeilGramSignature.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilGramSignature.lean#L134).

The hypotheses $\mathrm{IsStdChar}\,D\,\psi\,(-1)$ and $\mathrm{IoExt}\,R$ are introduced as `_` at [line 228](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L228) and are never used.
