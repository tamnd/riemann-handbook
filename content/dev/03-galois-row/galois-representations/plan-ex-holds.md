---
id: plan-ex-holds
title: Plans exist for each space of weight one
kind: theorem
decl: UpperTheory.Gal.Int.Geo.Pl.planEx_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.PrimeLevelLocalization.SpecTopHolds
covers: 1934
status: drafted
drafted_by: writer@claude
---
This theorem proves `PlanEx`, the third input of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/). For each space $U$ of automorphic forms that meets the hypotheses of [GeoOne](/step/geo-one-def/), it gives a *plan*: the group-theoretic data from which that entry builds a tower of Shimura varieties. The proof is an assembly. Below this theorem are 1,934 declarations.

## Statement

Take the hypotheses of $\mathrm{GeoOne}$: a CM field $E$, a prime $\ell$, an odd weight $a$, places $w_0$ and $v'$ above $\ell$, and a space $U$ with the conditions at $w_0$ and $v'$.

A plan has four groups of data.

1. **The group.** An auxiliary prime $p$, a group datum $D$ at $p$ of rank $a$, a group $G$ (`HTGroup`) with a link to $D$, and an isomorphism of the field of $D$ with $E$.
2. **The Hecke side.** A level $N$, a family of Hecke elements $g_j$ of level $N$, and their eigenvalues $\theta_j \in \overline{\mathbb{Q}}_\ell$.
3. **The twist.** An algebraic Hecke character $\kappa$ of $E$ with infinity type $m$, and an antitone weight $\lambda$.
4. **The test function.** A function $f$ in the Hecke algebra of level $N$, with integral support, that satisfies a spectral condition `Spec` for $\lambda$ and $\theta$. We have not unfolded `Spec`.

A plan also carries a congruence condition: at all but finitely many good split places $w$ not above $\ell$, $\kappa$ is unramified at $w$, and a sequence $\vartheta$ made from the eigenvalues at $w$ (`CongGrp`) relates by `HasRoots` to the Satake parameters of $U$ at $w$ twisted by $\kappa(w)^{-1}$. We have not unfolded `CongGrp` and `HasRoots`.

A plan is *Hodge-Tate at $v$* if $\kappa$ is unramified at $v$, the group is good at a place over $v$, and each weight jump of $U$ at an embedding over $v$ is $h_i - m_\tau$ for an exponent $h$ of the weight. A plan is *congruent at $w$* if the congruence condition holds at $w$ for each set of Satake parameters of $U$ at $w$.

**Theorem.** Under these hypotheses:

1. there is a plan that is Hodge-Tate at $v'$;
2. for each good place $w$ not above $\ell$ with Satake parameters, there is a plan that is Hodge-Tate at $v'$ and congruent at $w$;
3. for each place $w$ above $\ell$ that meets the conditions, there is a plan that is Hodge-Tate at $v'$ and at $w$, and a plan that is Hodge-Tate at $v'$ and congruent at $w$.

## Proof

1. `specTop_holds` proves `SpecTop`: outside each finite set of primes there is a prime $r_0 \neq p$ such that, at each level $N$ divisible by $r_0$, each family of Hecke elements that pass the test `Seen` has a test function with the spectral condition. It is `specTopG wtOf_holds` (930 declarations).
2. `vecEx_holds` (184) and `expOf_holds` (26) prove `VecEx` and `ExpOf`.
3. `exists_unitaryGroupDatum_of_vector_exponent_spectral` takes these three facts, adds twelve facts proved in the same folder, and calls `planEx_of`.

`planEx_of` applies one lemma, `master`, four times, with different sets of places. `master` builds the plan: `DatEx` gives $p$ and $D$, `VecEx` gives $\kappa$ and $\lambda$, `SiteEx` gives $N$, the family $g_j$ is the set of elements that pass `Seen`, and `SpecTop` gives $f$. The rest is bookkeeping.

## In the Lean code

The theorem is in [SpecTopHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/SpecTopHolds.lean#L9). The assembly is in [ExistsUnitaryGroupDatumOfVectorExponentSpectral.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/ExistsUnitaryGroupDatumOfVectorExponentSpectral.lean#L37), `planEx_of` and `master` are in [SameKTrans.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PrimeLevelLocalization/SameKTrans.lean#L207), and `PlanEx` and `Plan` are in [PackExOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PackExOf.lean#L82).

Two points are odd. `planEx_of` drops two hypotheses of `PlanEx` as `_` in its `intro`: `NonSplitSet` and `SphOffU`. And `specTopG` proves `SpecTopG`, a copy of `SpecTop` ([ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean#L139)).
