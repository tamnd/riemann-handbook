---
id: fix-k-holds
title: The fixed-point count on the tower holds
kind: theorem
decl: UpperTheory.Gal.FixZ.FixK_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IsogenyEtaleTranslation.TrFEtHolds
covers: 1789
status: drafted
drafted_by: writer@claude
---
This theorem proves `FixK`, the count of fixed points of Hecke correspondences on the towers of fibre powers. It is the second hypothesis of [ksHodge_of_geo](/entry/ks-hodge-of-geo/) in [kodaira_spencer_of_weight_one](/entry/kodaira-spencer-of-weight-one/). The proof only applies [tower_fixed_points_of_isogeny_data](/entry/tower-fixed-points-of-isogeny-data/) to five proved facts. The real content is in that entry and in [fixedPoints_int_base_holds](/entry/fixed-points-int-base-holds/).

## Statement

`FixK` says, in short: let $T$ be a tower of fibre powers over $\mathbb{C}$ at the standard base point, $N \mid N'$ two levels, $h$ a Hecke element and $\alpha$ a diagonal endomorphism with nonzero even entries. Take two maps from level $N'$ to level $N$: the transition map for $1$, and the one for $h$ followed by $\alpha$. The points where the two maps agree form a finite set $F$, each with a tangent matrix $A_x$ such that $\det(1 - A_x) \neq 0$, and the sum of $\det(1 - yA_x)/\det(1 - A_x)$ over $F$ is an index times a weighted count `cxTotalM` of group elements. The full statement is in [tower_fixed_points_of_isogeny_data](/entry/tower-fixed-points-of-isogeny-data/).

**Theorem.** `FixK` holds.

## Proof

It is `tower_fixed_points_of_isogeny_data` applied to five facts from `PAdicWittLattices`:

- `G3.sysOf_holds`: an integral Hecke element $h$ comes from a system of endomorphisms, up to a scalar $k$;
- `G3.relComp_holds`: the relation `Rel` between level structures, along a homomorphism and a Hecke element, is reflexive and composes (we have not unfolded `Rel`);
- `G3.witUniq_holds`: the maps (on the base and on the abelian scheme) that realize a Hecke translation are unique;
- `G3.isogFEt_holds`: an isogeny with a quasi-inverse up to a positive integer is finite étale and onto, in characteristic zero;
- `G3.powSm_holds`: fibre powers of the universal abelian scheme are smooth and separated, and projective in the compact case.

## In the Lean code

The theorem is in [TrFEtHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IsogenyEtaleTranslation/TrFEtHolds.lean#L7). The five statements are in [TransCancel.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/TransCancel.lean#L69), and their proofs in [FibrePowerTowerAdmissibleLevel.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/FibrePowerTowerAdmissibleLevel.lean#L70).
