---
title: Cusp forms as canonical forms on a resolution
decls:
  - GlobalTheory.LogCanonicalReflexive.logCanonical_refl_of_boundary
  - GlobalTheory.T.logCanonical_divisor_refl
  - GlobalTheory.LogCanon.log_canonical_pair_iff
  - GlobalTheory.T.log_canonical_criterion_boundary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cusp forms as canonical forms on a resolution

A modular form of weight $\kappa + b$, where $\kappa$ is the canonical weight, is a top form on the Shimura variety with values in the automorphic bundle of weight $b$. The classical criterion says when such a form extends to a holomorphic form on a smooth compactification: exactly when it is a cusp form, that is, when it vanishes along the boundary. This section proves this criterion on the toroidal flag space $Y_0$ and on every smooth projective modification of it. The criterion is what allows the argument on [birationality](/entry/bir-on-of-weight-gaps-large/) and the vanishing theorems ([vanishing theorems and resolution](/learn/geometry/#vanishing-theorems-and-resolution)) to treat cusp forms as sections of adjoint bundles $K \otimes L$ on a resolution.

We keep the notation of [the previous section](/entry/exists-log-pole-along-boundary/): the flag space $Y_0$ of dimension $n$ over $X_0$, its interior $U_0$, the canonical weight $\kappa$ and the automorphic bundles $L_0(\lambda)$ on $Y_0$. For a weight $s$, a section of $L_0(s)$ over $Y_0$ *vanishes on the boundary* if its germ at each point outside $U_0$ lies in the maximal ideal times the stalk of $L_0(s)$. These sections are the cusp forms of weight $s$ on $Y_0$.

**Definition 2.12.1 (Modification).** A *modification* of $Y_0$ along $U_0$ is a scheme $X'$, smooth and projective of relative dimension $n$ over the base, with a morphism $\sigma \colon X' \to Y_0$ that is an isomorphism over $U_0$ and such that $\sigma^{-1}(U_0)$ is dense in $X'$. A *canonical identification* on $X'$ is a section $\omega$ of $K_{X'} \otimes \sigma^* L_0(\kappa)^{-1}$ over $\sigma^{-1}(U_0)$.

The identity of $Y_0$ is a modification when $Y_0$ is itself smooth and projective with $U_0$ dense. A resolution of singularities of the minimal compactification that dominates $Y_0$ gives others ([resolution of singularities](/learn/geometry/#resolution-of-singularities)).

Let $b$ and $s$ be weights with $\kappa + b = s$. For a section $m$ of $L_0(s)$ over $U_0$, the product $\omega \cdot \sigma^* m$ is a section of
$$K_{X'} \otimes \sigma^* L_0(\kappa)^{-1} \otimes \sigma^* L_0(s) = K_{X'} \otimes \sigma^* L_0(b)$$
over $\sigma^{-1}(U_0)$, through the chart identification $L_0(\kappa) \otimes L_0(b) \cong L_0(s)$.

We first treat the identity modification. There the [simple pole](/entry/log-pole-along-boundary-is-simple/) of the canonical identification gives the criterion directly.

**Theorem 2.12.2 (Log canonical criterion on the flag space).** Assume the hypotheses of the second kind and Grothendieck's deformation theory. Let $F$ be algebraically closed in the function field, and assume that the Kodaira-Spencer map of the flag space is an isomorphism at every framed point over every field extension of $F$. Assume that $Y_0$ is smooth and projective with $U_0$ dense, and let $\omega_0$ be a canonical identification on $Y_0$. Let $\kappa + b = s$ and let $m$ be a section of $L_0(s)$ over $U_0$. Then the following are equivalent:

1. $m$ is the restriction of a section of $L_0(s)$ over $Y_0$ that vanishes on the boundary;
2. $\omega_0 \cdot m$ is the restriction of a section of $K_{Y_0} \otimes L_0(b)$ over $Y_0$.

Lean: `GlobalTheory.LogCanonicalReflexive.logCanonical_refl_of_boundary` (also `GlobalTheory.T.logCanonical_divisor_refl`, a second name).

*Proof.* The scheme $Y_0$ is reduced, and $U_0$ is dense. First, $\omega_0$ has a simple pole along the boundary: near each point $y \notin U_0$ there are a reduced equation $t$ of the boundary and a unit $u$ with $t \, \omega_0 = u$ on the interior. The equation $t$ exists because the boundary is a divisor with a reduced local equation at each of its points, and the unit $u$ is given by [Theorem 2.11.4](/entry/log-pole-along-boundary-is-simple/).

Assume 1, so $m$ extends to $g$ vanishing on the boundary. Near $y \notin U_0$ the germ of $g$ vanishes at the boundary points, so $t$ divides it: $g = t h$ with $h$ a local section of $L_0(s)$. Then $\omega_0 m = t \, \omega_0 \, h = u h$ on the interior, and $u h$ is regular near $y$. These local extensions agree on overlaps, since $U_0$ is dense and $Y_0$ is reduced, so they glue to a global section of $K_{Y_0} \otimes L_0(b)$. This gives 2.

Assume 2, so $\omega_0 m$ extends to a global section $k$. Near $y \notin U_0$ put $h = u^{-1} k$. Then $m = t h$ on the interior, and $t h$ is a regular local section of $L_0(s)$ that vanishes at the points of the boundary, because $t$ does. Gluing as before gives an extension of $m$ that vanishes on the boundary. This gives 1. $\square$

Next we pass to an arbitrary modification. The hypotheses on the Kodaira-Spencer map and on $Y_0$ are now proved, not assumed, and the canonical identification on $Y_0$ comes from the published list.

**Theorem 2.12.3 (Log canonical criterion on a modification).** Assume the hypotheses of the second kind and Grothendieck's deformation theory, and let $F$ be algebraically closed in the function field. Let $\sigma \colon X' \to Y_0$ be a modification along $U_0$ with a canonical identification $\omega$. Let $\kappa + b = s$, and let $m$ be a section of $L_0(s)$ over $U_0$. Then the following are equivalent:

1. $m$ is the restriction of a section of $L_0(s)$ over $Y_0$ that vanishes on the boundary;
2. $\omega \cdot \sigma^* m$ is the restriction of a section of $K_{X'} \otimes \sigma^* L_0(b)$ over $X'$.

Lean: `GlobalTheory.LogCanon.log_canonical_pair_iff` (also `GlobalTheory.T.log_canonical_criterion_boundary`, a second name).

*Proof.* The flag space $Y_0$ of a component is smooth, projective and connected, so the identity is a modification. We distinguish two cases.

Let $p + q \ge 1$. By Grothendieck's deformation theory, the Kodaira-Spencer map of the flag space is an isomorphism at every framed point. The published list then gives a canonical identification $\omega_0$ on $Y_0$. By the previous theorem, 1 is equivalent to the extension of $\omega_0 \cdot m$ to a section of $K_{Y_0} \otimes L_0(b)$. Then the birational invariance of the canonical extension, applied to $\omega_0$ and $\omega$, says that $\omega_0 \cdot m$ extends to a section of $K_{Y_0} \otimes L_0(b)$ over $Y_0$ if and only if $\omega \cdot \sigma^* m$ extends to a section of $K_{X'} \otimes \sigma^* L_0(b)$ over $X'$. The reason is that $\sigma$ is an isomorphism over the dense set $U_0$, both spaces are smooth and projective, and a regular top form with values in a pulled back bundle extends over a birational modification of smooth varieties ([line bundles and divisors](/learn/geometry/#line-bundles-and-divisors)). So the extension on $Y_0$ is equivalent to 2.

Let $p + q = 0$. Then the flag space has dimension $0$, so the dense open set $U_0$ is all of $Y_0$, and $\sigma^{-1}(U_0)$ is all of $X'$. Every section over $U_0$ is a global section, and the condition of vanishing on the boundary is empty. So 1 and 2 both hold. $\square$

The forward direction of the criterion is the one used later: a cusp form of weight $\kappa + b$ gives a holomorphic section of the adjoint bundle $K_{X'} \otimes \sigma^* L_0(b)$ on every smooth projective modification. Then Nadel vanishing and the method of [point separation](/learn/geometry/#point-separation) apply to it.

**Remark 2.12.4 (Formalization).** In the case $p + q \ge 1$ the proof uses `flag_tangent_kodaira_spencer_iso`, the canonical identification from the field `p5` of the hypotheses of the second kind (`nonempty_kodairaSpencer_identification_offBoundary`) and `canonicalExtension_birational_invariance`, whose proof we did not read ([LogCanonicalCriterionBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/LogCanonicalCriterionBoundary.lean#L21)). The two directions of the first criterion are `exists_extend_mul_simplePole_of_vanishing` and `extends_vanishing_of_simplePole_mul_extends` in LogCanonicalReflOfBoundary.lean (lines 42 and 51); the simple pole is the predicate `SimplePoleAlong`. Both second names are proved by `first | exact ...` from the first names. We have not unfolded `vanBd`, `canChart` or `Modif`; the definitions above follow their use in the statements.
