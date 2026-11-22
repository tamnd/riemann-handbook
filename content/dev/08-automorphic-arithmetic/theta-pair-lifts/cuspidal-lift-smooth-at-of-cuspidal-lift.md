---
id: cuspidal-lift-smooth-at-of-cuspidal-lift
title: Theta lifts keep cusp forms for all theta functions, from the Fock case
kind: theorem
decl: GlobalTheory.CuspSmoothLift.cuspidal_lift_smooth_at_of_cuspidal_lift
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.CuspidalLiftSmoothAtOfCuspidalLift
covers: 1415
status: drafted
drafted_by: writer@claude
---
This theorem passes from Fock test vectors to all theta functions. Theta lifts with Fock test vectors keep cusp forms, by hypothesis. The theorem proves that theta lifts with any theta function converge on cusp forms and keep them, with their archimedean type. It is used through [a copy](/entry/cuspidal-lift-smooth-at-cusps/) in [the cusp step along the grid](/entry/cusp-step-of-large-flip-run/). Below this theorem are 1,414 declarations.

## Statement

Let $D$ be a datum (`D7`) with `Sizes D`: its rank is larger than $1800$, and a gap condition holds that we do not unfold. Let $R$ be a real datum that meets `RowBase` (a level condition, an admissible family $\theta$ of archimedean embeddings, conditions on measures), and let $G$ be a grid for $R$ that meets `G.Is`. The grid has Hermitian spaces at its nodes and a Weil representation $\omega$ on each arrow.

For a node $X$, a *cusp form of type $X$* is a function $\varphi$ on $G_X(\mathbb A)$ that is smooth automorphic (smooth, $\mathfrak z$-finite, of moderate growth), cuspidal (its constant term along each isotropic frame vanishes), and of the archimedean type that $X$ prescribes (a condition on discrete series vectors that we do not unfold). For an arrow from $X$ to $Y$ with Haar measure $\nu$ and fundamental domain $\mathcal F$ on $X$, and a theta function $\Phi$ (a smooth function on the adelic space of the arrow, quasi-periodic under rational translations), put

$$\theta_\Phi(\varphi)(h) = \int_{\mathcal F} \theta_\Phi(g,h)\,\varphi(g)\,d\nu(g), \qquad \theta_\Phi(g,h) = \bigl(\omega(g,h)\Phi\bigr)(0).$$

**Theorem.** Assume `LiftsCuspidal` and [ThetaLocalInputs](/step/theta-local-inputs-def/). Then for each $D$, $R$ and $G$ as above, `CuspAlongSmooth G` holds: along each arrow of the five kinds below, for each theta function $\Phi$ and each cusp form $\varphi$ of the source type, the integrand is integrable for each $h$, and $\theta_\Phi(\varphi)$ is a cusp form of the target type.

The five kinds are $(i,j) \to (i+1,j)$, $(i,j+1) \to (i,j)$, $P_i \to P_{i+1}$ (with the conjugate kernel), $P_{i+1} \to P_i$, and $X_j \to X_{j+1}$.

`LiftsCuspidal` says that the lift maps the cusp space of the source node into that of the target, for test vectors $f_Q$ (a Fock vacuum vector $f$ times a polynomial $Q$).

## Proof

Each of the five arrows has four lemmas, one for each part of the conclusion.

1. **Integrability.** From rapid decay of cusp forms (the input `cuspRapidDecay`, through `rapidDec_of_cuspForm`) and a growth bound for the kernel (`integrableOn_of_rapidDec` and variants).
2. **Smooth automorphic.** Also from rapid decay, by `lift_isAutFunSm`, `isAutFunSm_thetaLift` or `conj_lift`. On column arrows both spaces are positive definite at each archimedean place, and `thetaLift_isSmoothAutomorphicFunction` uses that instead.
3. **Cuspidal.** Approximate the lift by finite sums of lifts with Fock vectors (`cusp_type_approximation_by_fock_lift` and variants). Apply `LiftsCuspidal` to each term. Pass to the limit with `isCuspFun_of_locApprox` or `isCuspFun_of_approx`. On column arrows, `isCuspFun_of_definite` gives cuspidality from the signature of the target alone, and $\varphi$ plays no role.
4. **Type.** `automorphicForm_uniformLimit_discreteSeries_series`, with the inputs on discrete series, Harish-Chandra modules and Casselman-Wallach, and the same approximation. On column arrows, `definite_unitary_cuspidal_decomposition` writes $\varphi$ as a finite sum, and `smooth_of_theta_lift_finite_sum` lifts the sum term by term.

The rest is bookkeeping.

## In the Lean code

The theorem is in [CuspidalLiftSmoothAtOfCuspidalLift.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/CuspidalLiftSmoothAtOfCuspidalLift.lean#L32). The definitions are in [CuspAlongSmoothRows.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/CuspAlongSmoothRows.lean#L111). The twenty lemmas are the `GlobalTheory.T` lemmas `twisted_theta_*`, `twisted_upward_*`, `twisted_downward_*` and `column*` in the folder `LocalTypeDictionary`. Each is a copy of a lemma in another namespace. We read their proofs, but not the lemmas that they call.

`LiftsCuspidal` is used only in the cuspidal and type parts. The ten integrability and smoothness lemmas take it as an argument and do not use it. The column cuspidality lemma uses neither hypothesis. The hypothesis is not new: `twisted_thetaLift_cuspidal` proves it from `ThetaLocalInputs`.
