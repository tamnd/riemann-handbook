---
id: lintegral-hs-norm-sq-amp-j-le
title: The square integral of the Bessel amplitude is at most the dimensions over the formal degree
kind: theorem
decl: GlobalTheory.Amp.SchurNorm.lintegral_hsNormSq_ampJ_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LintegralHilbertSchmidtNormSqBesselAmplitudeLe
covers: 541
status: drafted
drafted_by: writer@claude
---
This theorem bounds the mean square of the amplitude between two Bessel models of a square integrable representation. It is the content behind [its renaming](/entry/lintegral-hilbert-schmidt-norm-sq-bessel-amplitude-le/), which serves the step [nonempty hypotheses](/step/nonempty-hyps/). The proof reduces the bound to a bound for matrix coefficients by the formal degree. It does this with a change of normalisation.

## Statement

Let $G$ be the unitary group of the model form of size $2r+k+1$, with Haar measure $\mu_G$. The hypotheses are:
- `StdSm`: $\sigma$ is an irreducible unitary representation of $G$, the unit vector $w = v_0/\|v_0\|$ is smooth, and the Schur orthogonality relation holds with formal degree $d > 0$;
- `SideIrr` for $(z, \pi, \mu_S)$ and for $(z', \pi', \mu_{S'})$: $\pi$ and $\pi'$ are irreducible unitary representations of the stabilizers of $z$ and $z'$ on nonzero finite-dimensional spaces $W_p$ and $W_q$;
- `IsQuotMeas`: the measures $\nu_S$ and $\nu_{S'}$ are quotients of $\mu_G$ by $\mu_S$ and $\mu_{S'}$;
- `MultOne`: any two Bessel maps for the character $\psi_c$ are proportional on smooth vectors, and the same for $\psi_{c'}$;
- $B$ and $B'$ are Bessel maps for these data;
- with $\Phi(g) = B(\sigma(g)v_0)$, the integral of $\|\Phi\|^2$ over $\nu_S$ is $c_0 \dim W_p$, for some $c_0 > 0$; the same holds for $\Phi'$ with $\dim W_q$;
- for every smooth $v$, the integral of $\|B(\sigma(g)v)\|^2$ is proportional to $\|v\|^2$, and the same for $B'$;
- `IsDis`: $\nu$ is concentrated on the regular set and disintegrates $\mu_G$ over the double cosets.

**Theorem.** With $J(\gamma) = c_0^{-1}\int \langle \Phi'(x), \cdot\,\rangle\, \Phi(\gamma x)\, d\mu_G(x)$,
$$\int \|J(\gamma)\|_{HS}^2\, d\nu(\gamma) \le \frac{\dim W_p \cdot \dim W_q}{d}.$$

## Proof

1. **One side.** The local lemma `exists_isEll_smul` gives a Bessel map $l$ with the `IsEll` property and a scalar $t$ with $|t|^2 = c_0 \dim W_p\, d$, such that $B(\sigma(g)v_0) = t\, l(\sigma(g)w)$ on $G$. Its proof uses the density of smooth vectors, a factorisation of the Bessel map through rank one maps, and `MultOne`. The size of $t$ comes from the norm identity $\int \|l(\sigma(x)w)\|^2\, d\nu_S = \|w\|^2/d$.
2. **Both sides.** The same lemma gives $l'$ and $t'$ with $|t'|^2 = c_0 \dim W_q\, d$.
3. **Scaling.** The lemma `ampJ_of_smul` gives $J = c_0^{-1}\, t\, \bar t'\, J_1(\Psi, \Psi')$, with $\Psi(g) = l(\sigma(g)w)$. `amplitude_eq_ampJ_and_bessel_eq_doubleIntegral` identifies $J_1$ with the operator `OO`. The lemma `hsNormSq_smul` gives $\|J\|_{HS}^2 = \dim W_p \dim W_q\, \|d \cdot \mathrm{OO}\|_{HS}^2$, because $c_0^{-2}|t|^2|t'|^2 = \dim W_p \dim W_q\, d^2$.
4. **The bound.** `lintegral_hsNormSq_matrixCoeff_le_formalDegree` gives $\int \|d\cdot\mathrm{OO}(\gamma)\|_{HS}^2\, d\nu \le 1/d$. Multiply by $\dim W_p \dim W_q$.

The lemmas of steps 1 and 4 are not unfolded here.

## In the Lean code

The theorem is at [LintegralHilbertSchmidtNormSqBesselAmplitudeLe.lean line 121](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LintegralHilbertSchmidtNormSqBesselAmplitudeLe.lean#L121). The helpers `hsNormSq_smul`, `ampJ_of_smul` and `exists_isEll_smul` are at lines 18, 27 and 44. The amplitude `ampJ` is at [RelevantZeroGramTerms.lean line 412](lean:Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L412), and the hypotheses are in [MatrixOfBesselTwoSidedAction.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean#L57). The bound does not depend on $c_0$, because $c_0$ cancels in step 3. The decay exponent $a$ in `StdSm` is only passed along.
