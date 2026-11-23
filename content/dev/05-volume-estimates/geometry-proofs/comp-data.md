---
id: comp-data
title: A reference root origin at one generic point of the model
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.TopTower.comp_data
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ExistsGoodRootTower
covers: 400
status: drafted
drafted_by: writer@claude
---
This lemma does the work on one component in [the construction of the good tower](/entry/exists-good-tower/). For a generic point $x$ of the integral model $Y$, it gives an analytic system, fixed data and a reference root origin whose generic point is $x$. The caller applies it to each component and uses its output for the reference part of the good origin and for the first condition of `Extra`.

## Statement

Assume `Top.Given`, `FlatLineGenerator` and `FlatLineGeneratorComponent`. Let $Y$ be a global integral model with split components over a datum with $p, q \geq 1$, and let $x$ be a point of $Y$ with no proper generization. Then there are an analytic system $\mathrm{Sys}$ indexed by $\mathrm{RootIx} \cup \{\mathrm{none}\}$, fixed data $F$, a root model $R$ and a root origin $o$ of $Y$ for $R$ and $F$ with the empty set of primes, such that:

1. the generic point of $F$ is $x$;
2. $n(\tau, i) = -k_A q' \, i$ for each root index $(\tau, i)$, with $k_A, q'$ the integers of $F$;
3. the flag of $o$ has degree $1$, the realization of $o$ has $J = \top$, and the line of $R$ is ample in the sense of `AmpleQ`;
4. the realization is embedded (`Cmp.IsEmbedded`) and its projection $\pi$ is bijective;
5. for each $\tau$, the last index $i$ (with $i + 1 = p + q$) and each $t$, the potential of $\mathrm{Sys}$ at $(\tau, i)$ and its negative are plurisubharmonic;
6. the local lifts of condition 1 of `Extra`: near each point there are holomorphic $\lambda$, nonzero multiples of the point map of $F$, whose affine charts have injective differential.

## Proof

1. The stalks of $Y$ are domains, because $Y$ is normal. `T.isCptGen_residue_field_generic` then shows that $\operatorname{Spec} \kappa(x) \to Y$ is a component generic point (`IsCptGen`, not unfolded).
2. `T.exists_reference_geometry_same_generic`, with `ResKStatement` from `Top.Given`, gives a reference geometry $G$ with the same generic point.
3. `T.exists_holomorphic_section_of_analytic`, with the two flat generator statements, gives an analytic realization $A$ of $G$ whose projection has a holomorphic inverse.
4. Let $\nu(\tau, i) = -i$. It is strictly decreasing in $i$. `T.exists_effective_weight_section` gives $k, q' > 0$ and $s \neq 0$ that is effective for the weight $k q' \nu$.
5. `T.effective_scaled_weight_of_retraction` turns $A$, $k$, $q'$, $s$ into $F$, $R$ and $o$, with conditions 1 to 4 and 6. Condition 5 is the field `flat` of $A$. The rest is bookkeeping.

## In the Lean code

The lemma is in [ExistsGoodRootTower.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsGoodRootTower.lean#L20). It calls the five lemmas above, each through its statement file.

The proof takes `ResKStatement` by position, as `hG.2.2.2.2.1`. The weight $\nu$ here is the weight of the tower in [`exists_good_tower`](/entry/exists-good-tower/), and condition 2 is the field `nu_eq` of the tower origin. The name `comp_data` says only "data for a component".
