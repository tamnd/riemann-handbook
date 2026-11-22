---
id: et-c-c2
title: Affine curves over an algebraically closed field have étale cohomological dimension at most one
kind: theorem
decl: GlobalTheory.EtC.etC_c2
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SmoothAffineCurveEtaleCohomologicalDimensionLeOn
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom `C2` of the étale cohomology package: on a smooth affine curve over an algebraically closed field, the cohomology with coefficients $\mathbb{Z}/q(i)$ vanishes in degrees at least two. It is one of five fields of the structure `Core` that [the local steps](/entry/steps-holds/) use, next to [the projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/). It is also one of the twenty two axioms that `KunnethLefschetz.upTo` takes.

## Statement

Let $k$ be an algebraically closed field and $q \geq 1$ an integer that is a unit in $k$. Let $B$ be a Dedekind domain that is a finitely generated $k$-algebra. So $\operatorname{Spec} B$ is a smooth affine curve over $k$, or a point when $B$ is a field.

**Theorem.** For all integers $n \geq 2$ and $i$,
$$H^n_{\text{ét}}(\operatorname{Spec} B, \mathbb{Z}/q(i)) = 0.$$

For curves this is a case of Artin's bound on the cohomological dimension of affine varieties (SGA 4, Exp. XIV).

## Proof

The proof splits $n = 2$ from $n \geq 3$.

1. **Degree 2.** `subsingleton_Ht_two_of_isDedekindDomain_of_isAlgClosed`. Its proof picks a primitive $q$-th root of unity in $k$, which makes all twists isomorphic, and reduces to $i = 1$. A class in $H^2(B, \mathbb{Z}/q(1))$ dies on some $B_f$ and on an étale neighbourhood of the zeros of $f$. By the names of the lemmas, an excision argument and a Kummer class that agrees with it near the zeros of $f$ then kill it.
2. **Degree at least 3.** `smoothAffineCurve_tateTwistCohomology_subsingleton_of_ge_three`. If $B$ is a field, it is strictly Henselian, so $\operatorname{Spec} B$ is acyclic. Otherwise $K = \operatorname{Frac} B$ is algebraic over $k(t)$, and the class dies on $K$ by `etale_cohomology_vanishing_algebraic_over_ratFunc`, a vanishing in degrees at least 2 for such fields. So it dies on some $B_f$, and on an étale neighbourhood of the zeros of $f$. A Mayer-Vietoris sequence writes it as the boundary of a class of degree $n - 1 \geq 2$ on the overlap, and that class dies on a finer neighbourhood.

## In the Lean code

The theorem is in [SmoothAffineCurveEtaleCohomologicalDimensionLeOn.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothAffineCurveEtaleCohomologicalDimensionLeOn.lean#L9). `C2` is in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L105). The proof is a case split on $n = 2$ or $n > 2$ with `omega`, and it calls two statement forms:

- `GlobalTheory.T.subsingleton_Ht_two_of_isDedekindDomain_of_isAlgClosed`, for `EtC.smoothAffineCurve_tateTwistCohomology_two_subsingleton` in [SmoothAffineCurveTateTwistCohomologyTwoSubsingle.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothAffineCurveTateTwistCohomologyTwoSubsingle.lean#L14);
- `GlobalTheory.T.smoothAffineCurve_tateTwistCohomology_subsingleton_of_ge_three`, for `EtC.AffineCurve.subsingleton_of_three_le` in [SmoothAffineCurveTateTwistCohomologySubsingleton.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothAffineCurveTateTwistCohomologySubsingleton.lean#L17).

The sketch above is read from these two proofs; we have not opened the lemmas that they call. The cohomology `Ht q (sp B) n i` is the cohomology of $\operatorname{Spec} B$ on the big étale site of all schemes, computed with an injective resolution. The coefficient sheaf `tw q i` is the sheaf made from the free $\mathbb{Z}/q$-module on the primitive $q$-th roots of unity, with $\zeta^a$ identified with $a^i \zeta$; we read it as $\mathbb{Z}/q(i)$ and have not checked this further. "Subsingleton" means that the group is zero. The name of the module says "le on", a cut form of "le one". The statement form `smooth_affine_curve_etale_cohomologicalDimension_le_one` repeats this theorem.
