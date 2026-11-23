---
id: conj-lift5
title: A conjugate datum turns a rational theta lift into a theta lift at sigma
kind: theorem
decl: GlobalTheory.ConjRatLiftFive.conj_lift5
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConjugatesOfRationalThetaLiftFromCharacterisatio
covers: 412
status: drafted
drafted_by: writer@claude
---
This theorem is the computation behind [the lift at a non-base embedding](/entry/conjugate-rational-lift-at-non-base-embedding/). Given a conjugate datum at an embedding $\sigma$ over $K$, it shows that $j_\sigma$ of a rational lift is a theta lift for that datum, after a phase operator, a central translation and a scalar of norm 1. We use the notation of [the parent of that entry](/entry/conj-rat-lift5/).

## Statement

**Theorem.** Assume the hypotheses of [the lift at a non-base embedding](/entry/conjugate-rational-lift-at-non-base-embedding/), and in place of the base datum there, a base datum $c_0^L$ with $\mathrm{Comparison}_2$ and with the base change condition from the oscillator model at $i$. Let $\sigma$ be over $K$. Let $\mu'$ be the character of $R$ at $\sigma$, let $\eta'$ be a conjugate of $\eta$ by $\sigma$, let $(c, c_1, H, j)$ be conjugate forms at $\sigma$, and let $(\omega, f_0, f, B, io, th_P)$ be lift data for $(\mu', \eta')$. Then there are a linear map $th \colon H \to H_{i,\sigma}$, a function $u$ with an isometry $U$ of $H_{i,\sigma}$, a central $z \in G$ and $\kappa \in \mathbb{C}$, such that:

1. $th$ is the projection of $th_P$ ($\mathrm{IsProjOf}$);
2. $(u, U)$ is a compatible phase: $|u| = 1$, $u$ has the right invariance, and $U$ multiplies each form by $u$ ($\mathrm{IsCompPhase}$);
3. $|\kappa| = 1$;
4. $U(j_\sigma y) = \kappa \, g_\sigma(z) \, th(j(x))$ whenever $y$ is the rational lift of $x$ with phase $ph$.

## Proof

Let $\mathrm{ev}$ be evaluation at the unit vector $v_0$ at $\sigma$. It is injective, since $\sigma$ is a good embedding. Let $J = U \circ j_\sigma$.

1. **The base lift.** `base_lift5` gives an action of $G$ on the rational forms, a central $z_0$ and a root of unity $\zeta$. For each $x$ it writes the rational lift of $x$ as an explicit element `ratOf` built from a class sum with coefficients $a_k$.
2. **The phase.** [`oneMapConj5`](/entry/one-map-conj5/) gives a phase function $u$, a central $z$ and $\kappa$ with $|\kappa| = 1$. It also gives the equivariance $\mathrm{EquivBy}$ and an identity for each class sum: $\kappa \, th_P(j x)(\otimes v) = \sum_k \sigma(a_k) \, u \cdot \phi(z f_k)$. The second clause of `centralShift_phase_conjReadings_fiveClauses` turns $u$ into the operator $U$.
3. **Equivariance of $J$.** The last field of $\mathrm{IsCompPhase}$ gives $\mathrm{ev}(J f)(g) = u(g)\,\phi(f)(g)$. With $\mathrm{EquivBy}$, the trace facts of `conjugateLift_unique_and_baseDatum` and injectivity of $\mathrm{ev}$, this gives $J(g f) = \sigma(\chi(g)) \, g_\sigma(g) \, J(f)$.
4. **The lift $th$.** By step 2, each value $th_P(j x)(\otimes v)$ is the evaluation of a vector of $H_{i,\sigma}$. The last clause of `conjugateLift_of_characterisationClauses` then gives $th$ with $\mathrm{IsProjOf}$.
5. **The constants.** Take $z_0 z^{-1}$ as the central element and $\sigma(\zeta)\,\sigma(\chi(z_0))\,\sigma(\chi(z))^{-1}\kappa$ as the scalar. Its norm is 1, since $|\chi| = 1$ and $\zeta$ is a root of unity. Injectivity of $j_{\sigma_0}$ identifies $y$ with `ratOf`. Then `conj_abstract` combines steps 3 and 4 into the identity.

## In the Lean code

The theorem is in [ConjugatesOfRationalThetaLiftFromCharacterisatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L71). `IsCompPhase` is in [WeilGramSignature.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilGramSignature.lean#L117). `IsProjOf`, `EquivBy` and `IsClassSum` are in [ReadingsExistRow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReadingsExistRow.lean#L49).

The lemmas it calls: `base_lift5` and `oneMapConj5` in the same file, `exists_reps`, `exists_ev`, `conj_abstract`, and three theorems in the `T` namespace: `centralShift_phase_conjReadings_fiveClauses`, `conjugateLift_unique_and_baseDatum` and `conjugateLift_of_characterisationClauses`. We have not unfolded `ratOf`, `conj_abstract` or the proofs of the three theorems. The proof needs `maxHeartbeats 800000`.
