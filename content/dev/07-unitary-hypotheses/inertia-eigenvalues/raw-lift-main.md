---
id: raw-lift-main
title: The raw theta lift is onto, and its adjoint is injective and conformal on Hecke parts
kind: theorem
decl: GlobalTheory.RawLift.rawLift_main
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.InnerPosOfInnerNe
covers: 582
status: drafted
drafted_by: writer@claude
---
This theorem proves four facts about the theta lift of a real datum $R$, from forms on $U(V_i)$, with $V_i$ positive definite, to cusp forms on $U(W_i)$. Its only user is [`liftRows_injective_and_typeProperties_of_nonvanishing`](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/). That theorem keeps only the second fact and passes it to `saturated`, which does not use it. It lies in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $R$ be a real datum (`RealDat D A Ks`) and $F$ a face, as in the parent entry. For an index $i$ and a type $t$, the datum gives a Weil representation $\omega$ of $U(V_i)(\mathbb A) \times U(W_i)(\mathbb A)$, a finite-dimensional Hilbert space $H_V$ (`R.HV i t`), a finite-dimensional Hilbert space $H_W$ with an isometric embedding onto the space $\mathcal W_i$ of cusp forms of a fixed level and character (`R.Wall i σ₀`), and a theta map $\theta_{i,t} \colon H_V \to \mathcal W_i$ (`R.thF i t`).

A *raw lift* is a linear map $\vartheta \colon H_V \to H_W$ whose composite with the embedding is $\theta_{i,t}$ (`IsRaw`). For a system $c$ of Hecke eigenvalues, $H_W(c)$ (`part R i ∅ c`) is the part of $H_W$ that maps into the joint $c$-eigenspace.

The hypotheses are `CuspRapidDecay`, `Laws R F` (five conditions on levels, group, family, models and theta data), `R.FullP` and `RallisConv D`. The last says: if $V$ is positive definite and $2 \operatorname{rank} W < \operatorname{rank} V$, then for theta functions $f_1, f_2$ and smooth cusp forms $\varphi_1, \varphi_2$ on $U(W)$, the lifts $\theta(f, \varphi)(h) = \int_{[U(W)]} \overline{\theta_f(h,g)}\, \varphi(g)\, dg$ exist and

$$\int_{[U(V)]} \overline{\theta(f_1,\varphi_1)}\, \theta(f_2,\varphi_2) = \operatorname{vol}([U(V)]) \int_{U(W)(\mathbb A)} \langle \omega(g) f_2, f_1 \rangle\, \langle \varphi_1, R(g) \varphi_2 \rangle\, dg,$$

All integrals converge. This is the shape of the first identity of the Rallis inner product formula (S. Rallis, Compositio Math. 52, 1984).

**Theorem.** Under these hypotheses:

1. (`ThOnto`) for each $i$, $\theta_{i,\mu_0}$ maps the span of the image of `R.jV i μ₀` onto $\mathcal W_i$;
2. (`UpInj`) for all $i, t$, each raw lift $\vartheta$ has an injective adjoint $\vartheta^*$;
3. (`InnerPos`) for all $i, t, c$ there is a real $\lambda > 0$ with $\langle \vartheta^* x, \vartheta^* y \rangle = \lambda \langle x, y \rangle$ for $x \in H_W(c)$ and all $y$;
4. (`PartsSpan`) the spaces $H_W(c)$ span $H_W$.

## Proof

Seven local facts come from `Laws` and `FullP`, one lemma each (`levProd_of_laws`, `transLaws`, `levFix`, `vecNe`, `finMult`, `localCoeff_vanishes_offLevel_badPlaces`, `locSmall`). They concern the level, the Hecke pairing, the theta vector $v$ and its matrix coefficient $c_v$. Only `transLaws` uses `CuspRapidDecay`.

The main step is `finSum_of_rallis`. From `RallisConv` and `downwardLift_adjoint_eq_upwardThetaIntegral` it gives $a > 0$ with

$$\langle \vartheta^* x, \vartheta^* y \rangle = a \sum_{\gamma \in U(W_i)(\mathbb A_f)/K} c_v(\gamma)\, \langle x, T_\gamma y \rangle .$$

Then `upInj_holds` gives (2), and `innerNe_spherical` gives (3) with a nonzero complex $\lambda$. The helper `innerPos_of_innerNe` makes $\lambda$ positive real by `adjoint_injective_surjective_and_positive_scalar`, finite-dimensional linear algebra. The same fact says that a map with injective adjoint is onto; with `ratSpan_of_laws`, `rawLift_onto_of_upInj` gives (1). `partsSpan` gives (4).

## In the Lean code

The theorem is at [InnerPosOfInnerNe.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InnerPosOfInnerNe.lean#L47). The definitions are in [LengthPosOfPosDef.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LengthPosOfPosDef.lean#L19).

- `RallisConv` is a hypothesis, not a theorem.
- The parent keeps `UpInj` and drops the other three facts. It passes `UpInj` to `saturated`, whose `intro` discards it ([ExistsAdjointComp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsAdjointComp.lean#L313)). So this theorem does no logical work in the proof.
- `upInj_holds` and `innerNe_spherical` take `FullP` and do not use it; `upInj_holds` also ignores `LevProd`.
