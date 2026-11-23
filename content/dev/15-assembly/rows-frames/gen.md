---
id: gen
title: Downward integrals that vanish on the lowest types vanish on all Fock vectors
kind: theorem
decl: GlobalTheory.GenRealFock.gen
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RealFockThetaLiftVanishingOfGeneratingVectors
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem says that the downward theta integrals of a form vanish on all Fock vectors once they vanish on the vectors of the lowest types. It is the proof behind the second name [`realFockThetaLift_vanishing_of_generating_vectors`](/entry/real-fock-theta-lift-vanishing-of-generating-vectors/), which [`genInf`](/entry/gen-inf/) uses. The proof checks the three hypotheses of [`forms_vanish_of_io`](/entry/forms-vanish-of-io/), which holds the representation theory.

## Statement

The statement is the one of [`realFockThetaLift_vanishing_of_generating_vectors`](/entry/real-fock-theta-lift-vanishing-of-generating-vectors/). Assume `Given R F` and `R.FullP`. Let $y \in H_V$ with $d(y, \phi_{\iota(x)(w)}, l, g) = 0$ for all $x$ in the lowest types, $w \in E$, $l \in E^*$ and $g \in U(W)(\mathbb A)$. Then $d(y, \phi_P, l, g) = 0$ for all $P \in \mathcal P$, $l$ and $g$.

## Proof

For $g \in U(W)(\mathbb A)$ put $B_g(P, l) = d(y, \phi_P, l, g)$. By `exists_bilin`, each $B_g$ is bilinear on $\mathcal P \times E^*$. Each $\phi_P$ is a theta function (the field `pt_theta` of the theta data), so the integrand is integrable (`integrableOn_downwardThetaLift_integrand`) and $d$ is additive in $f$ and in $l$. Then apply [`equivariant_bilinearForms_vanish_of_io_generation_real`](/entry/equivariant-bilinear-forms-vanish-of-io-generation-real/) to the family $(B_g)_g$. Its three hypotheses hold:

1. (equivariance) for $u$ in the real points $G_\infty$ of $U(V)$, $d(y, \omega(u,1)f, l, g) = d(y, f, l \circ \rho(u), g)$, by `downwardThetaLift_real_points_equivariant`;
2. (Lie stability) if $B_g(P, l) = 0$ for all $g$, and $\phi_{P'}$ is the derivative at $s = 0$ of $\omega(1, \exp(sY))\phi_P$ (the one-parameter group is `oneP`) for $Y$ in the real Lie algebra of $U(W)$, then $B_g(P', l) = 0$ for all $g$, by `thetaLift_vanishing_preserved_by_realLieDerivative`;
3. (lowest types) $B_g(\iota(x)(w), \cdot) = 0$ is the hypothesis.

So each $B_g$ is zero.

## In the Lean code

The theorem is at [RealFockThetaLiftVanishingOfGeneratingVectors.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealFockThetaLiftVanishingOfGeneratingVectors.lean#L93). The helpers `exists_bilin`, `pureTensor_add`, `pureTensor_smul`, `downInt_add_f`, `downInt_smul_f`, `downInt_add_l` and `downInt_smul_l` in the same file build $B_g$.

- The two lemmas of steps 1 and 2 are second names of `downInt_realEquiv` and `GenReal.downInt_lie`. We have not opened those.
- The family is indexed by all of $U(W)(\mathbb A)$, because the Lie lemma assumes vanishing at every $g$.
- `downInt_add_f` and `downInt_smul_f` repeat `downInt_add` and `downInt_smul` of [`genFin`](/entry/gen-fin/)'s file.
