---
id: tate-twist-cohomology-generic-fibre-hensel-line-subsingleton
title: Vanishing of the first cohomology of the generic fibre of a strictly henselian line
kind: theorem
decl: GlobalTheory.LocAcycDegOne.tateTwistCohomology_genericFibre_henselLine_subsingleton
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TateTwistCohomologyGenericFibreHenselLineSubsing
covers: 916
status: drafted
drafted_by: writer@claude
---
This theorem proves that $H^1(\operatorname{Spec}(K \otimes_T A), \mathbb{Z}/q(i)) = 0$ for a strictly henselian local ring $A$ over $T[x]$. It does so by the Kummer sequence: units of the generic fibre are $q$-th powers, and its Picard group has no $q$-torsion. Its second name [subsingleton_ht_one_genericFibre_of_sh_etale_cover](/entry/subsingleton-ht-one-generic-fibre-of-sh-etale-cover/) carries it to the [local steps](/entry/steps-holds/). Below this theorem are 916 declarations; 777 of them are below the Picard step [picL](/entry/pic-l/).

## Statement

Let $T$ be a local domain in which each monic polynomial of positive degree has a root (`AIC T`), with fraction field $K$, and let $q \geq 1$ be invertible in $T$. Let $A$ be a strictly henselian local ring (`SH A`: henselian, with separably closed residue field) that is a $T[x]$-algebra, such that each element of $A$ is in the image of a map $E \to A$ of $T[x]$-algebras from an étale $T[x]$-algebra $E$. Write $A_K = K \otimes_T A$.

**Theorem.** For each $i \in \mathbb{Z}$, $H^1(\operatorname{Spec} A_K, \mathbb{Z}/q(i)) = 0$.

## Proof

1. $q$ is a unit in $A_K$. The cyclotomic polynomial $\Phi_q$ is monic of positive degree, so it has a root in $T$, and so in $A_K$ (`exists_cyclotomic_root`).
2. With these two facts, `tateTwistCohomology_spec_twist_independent` gives an isomorphism $H^1(\operatorname{Spec} A_K, \mathbb{Z}/q(i)) \cong H^1(\operatorname{Spec} A_K, \mathbb{Z}/q(1))$. So it suffices to take $i = 1$.
3. `kummer_etale_vanishing` proves the statement `B6h1`: if $q$ is a unit in a ring $R$, each unit of $R$ is a $q$-th power, and $\operatorname{Pic} R$ has no $q$-torsion, then $H^1(\operatorname{Spec} R, \mathbb{Z}/q(1)) = 0$. This is what the Kummer sequence $1 \to \mu_q \to \mathbb{G}_m \xrightarrow{q} \mathbb{G}_m \to 1$ gives (Milne, *Étale Cohomology*, 1980, Chapter III). We have not opened its Lean proof.
4. The two inputs for $R = A_K$:
   - `unitsL`: each unit of $A_K$ is a $q$-th power. It writes $A$ as a quotient of a strictly henselian ring $O$ that is a directed union of localizations of étale $T[x]$-algebras at primes (`surj_of_strictHenselisation_polynomial_alt`), and then calls `henselian_directed_union_subalgebras`.
   - [picL](/entry/pic-l/): each $c \in \operatorname{Pic} A_K$ with $c^q = 1$ is trivial.

## In the Lean code

The theorem is in [TateTwistCohomologyGenericFibreHenselLineSubsing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TateTwistCohomologyGenericFibreHenselLineSubsing.lean#L36). The lemmas:

- `unitsL` (line 14), `picL` (line 19) and `exists_cyclotomic_root` (line 24) in the same file;
- `GlobalTheory.T.tateTwistCohomology_spec_twist_independent` in TateTwistCohomologySpecTwistIndependentStatement.lean;
- `GlobalTheory.T.kummer_etale_vanishing`, of type `GlobalTheory.EtC.B6h1`, in KummerVanishingStatement.lean; `B6h1` is in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L94);
- `GlobalTheory.T.surj_of_strictHenselisation_polynomial_alt` and `GlobalTheory.T.henselian_directed_union_subalgebras`, whose statements only we have read.

The coefficient $\mathbb{Z}/q(i)$ is `tw q i`, and $H^n$ is `Ht q (sp R) n i`. The namespace `LocAcycDegOne` suggests a use in local acyclicity in degree one; we have not traced it.
