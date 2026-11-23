---
id: log-canonical-refl-of-boundary
title: Cusp forms as canonical forms on the flag space
kind: theorem
decl: GlobalTheory.LogCanonicalReflexive.logCanonical_refl_of_boundary
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.LogCanonicalReflOfBoundary
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem proves, on the flag space $\bar X$ itself, that a section $m$ of $L(\kappa + b)$ over the interior is a cusp form if and only if $\omega_0 \cdot m$ is a global section of $K_{\bar X} \otimes L(b)$. Its only user is its second name [logCanonical_divisor_refl](/entry/log-canonical-divisor-refl/), which [log_canonical_pair_iff](/entry/log-canonical-pair-iff/) calls. The geometric input is that $\omega_0$ has a simple pole along the boundary. Below this theorem are 338 declarations.

## Statement

We use the notation of [log_canonical_pair_iff](/entry/log-canonical-pair-iff/): $\bar X$, its dense interior $U$, the boundary $D$, the automorphic bundles $L(\lambda)$, and the canonical weight $\kappa$.

**Theorem.** Assume `Hypotheses''`, `GrothendieckDeformation` and `FnAlgClosed`. Assume the Kodaira-Spencer isomorphism `KSIso` at each framed point over each field, and that $\bar X$ is smooth of relative dimension $n$, projective and geometrically connected (`IsVariety₀`). Let $\omega_0$ be a canonical identification for $\bar X$: a nowhere zero section of $K_{\bar X} \otimes L(\kappa)^{-1}$ over $U$ that matches the Kodaira-Spencer map. Let $s = \kappa + b$ and let $m$ be a section of $L(s)$ over $U$. Then $m$ extends to a global section of $L(s)$ that vanishes along $D$ if and only if $\omega_0 \cdot m$ extends to a global section of $K_{\bar X} \otimes L(b)$.

## Proof

The key fact is `SimplePoleAlong U C ω₀`: each point $y \in D$ has a neighbourhood $V$ with charts and two functions $t, u$ on $V$ such that

- $t$ is a reduced equation of $D$: $t$ is a unit exactly on $U$, and $t$ divides each function on an open $W \subseteq V$ whose germs vanish on $D$;
- $u$ is a unit, and $t\,\omega_0 = u$ on $V \cap U$ in the charts.

So $\omega_0 = u/t$ near $D$. This is the Lean form of $L(\kappa) \cong K_{\bar X}(D) = \Omega^n(\log D)$.

1. **The simple pole.** At $y \in D$, `boundary_divisor_has_reduced_equation` gives $V$ and a reduced equation $t$. Then [exists_simple_log_pole_along_boundary](/entry/exists-simple-log-pole-along-boundary/) gives a smaller $V'$, the charts and the unit $u$ with $t\,\omega_0 = u$.
2. **Cusp form to canonical form.** If $m = g|_U$ with $g$ vanishing on $D$, then `exists_extend_mul_simplePole_of_vanishing` extends $\omega_0 \cdot g$: locally $g = t g'$, so $\omega_0 g = u g'$ is regular.
3. **Canonical form to cusp form.** If $\omega_0 \cdot m = G|_U$, then `extends_vanishing_of_simplePole_mul_extends` gives $g$ with $g|_U = m$ that vanishes on $D$: locally $m = t u^{-1} G$.

Both lemmas use that $\bar X$ is reduced and $U$ is dense. The rest is bookkeeping: $\sigma$ is the identity, so pulling back along it is a bijection, and its off-boundary open set is $U$.

## In the Lean code

The theorem is at [LogCanonicalReflOfBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/LogCanonicalReflOfBoundary.lean#L20). `SimplePoleAlong` is in [SimplePoleAlong.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SimplePoleAlong.lean#L24).

- `exists_extend_mul_simplePole_of_vanishing` and `extends_vanishing_of_simplePole_mul_extends` restate `exists_extend_mul_of_simplePole` and `extends_vanishing_of_mul`. We have not opened their proofs, nor `BdEquation.exists_reduced_boundary_equation` behind the reduced equation.
- `GrothendieckDeformation` goes only to `exists_simple_log_pole_along_boundary`, and the lemma behind that name ignores it (line 136 of [ExistsSimpleLogPoleAlongBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsSimpleLogPoleAlongBoundary.lean#L136)). So it is not used in this proof.
