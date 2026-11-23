---
id: base-facts-has-geo-exists-clos
title: Base facts, geometric tests and a projective closure of a theta-level abelian scheme
kind: theorem
decl: GlobalTheory.ZH.baseFacts_hasGeo_exists_clos
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.BaseFactsHasGeoExistsClos
covers: 563
status: drafted
drafted_by: writer@claude
---
This theorem is the set-up step of [`zhGeo`](/entry/zh-geo/). From a theta system with uniformised $p$-adic tests, it gives the facts on the base, geometric tests, and a projective closure of the abelian scheme over a normal model, with four properties of its $p$-adic points. It only assembles eight lemmas.

## Statement

We use the names of [`zhGeo`](/entry/zh-geo/): a theta system $S$ over $o \subset \Omega$, a realization $\rho$ by a polarized abelian scheme $(A, L)$ over $\operatorname{Spec} R$, a normal model $Z$ (`RatModel`) with an open set $U_0$ and a lattice $E(z)$ over each local ring (`EE`).

**Theorem.** Assume `UT.LL` (the bundles `Laws` to `Laws5`) and `UTorsSt` (the torsion of a uniformised abelian variety over a complete discrete valuation ring is the image of the torsion of its degeneration data). Assume `S.Big`, `S.Over₀ M U₀`, `S.IsEE M U₀ EE` and `ρ.HasU`. Then:

1. `BaseFacts`: $Z$ is a Jacobson space, and the subgroups $T(z)$, $H(z)$ of $\Gamma$ and the lattices $E(z)$ satisfy freeness, stability and integrality conditions; at a $p$-adic test point, $H(z)$ is the kernel of the label map of the test;
2. `ρ.HasGeo`: each $p$-adic point of $R$ integral on $o$ has a geometric test (see [the next entry](/entry/has-geometric-test-of-has-uniformised-test/));
3. there is a closure $Q$ (`Clos`): an integral scheme $P$, proper over $Z$ and projective over $o$, that contains the pullback of $A$ over $U_0$ as a cartesian open piece, with a line bundle $\mathcal{O}(1)$, theta coordinates, and on an affine cover of $Z$ local sections that immerse $P$ and whose coordinates are bases of $E(z)$;
4. there is an extension `Q.Ext` (flatness and finiteness of $Z$ over $\mathbb{Z}$, normality, $U_0 \ne \emptyset$, an abelian scheme of relative dimension $g$ over $U_0$, an open group part $G \subset P$ and a unit section), whose core has `HasTests`, `Indep`, `Fib` and `HasCharts`.

The four core properties are on points $y \colon \operatorname{Spec} \mathcal{O}_{\mathbb{C}_p} \to Z$ with generic point in $U_0$. `HasTests`: each such $y$ has a test. `Indep`: if two such points have the same reduction, a point of $G$ over the first gives one over the second with the same reduction. `Fib`: each point of the special fibre of $G$ over $y$ comes from the group scheme of the test. `HasCharts`: near each point of $Z$ there are charts of $G$ that split the test groups.

## Proof

1. `S.HasTests` follows from `ρ.HasU`: the uniformised test at $y_0$ contains a test of $S$.
2. `baseFacts_of_isEE` gives `BaseFacts`.
3. [`T.hasGeometricTest_of_hasUniformisedTest`](/entry/has-geometric-test-of-has-uniformised-test/) gives `ρ.HasGeo`.
4. `T.nonempty_abelianSchemeProjectiveClosure` gives $Q$, and `T.nonempty_closureExtension_abelianScheme` gives the extension.
5. `T.closure_tests_exist_and_reduction_independent` gives `HasTests` and `Indep`, from `HasGeo` and `S.Big`.
6. `T.fibre_eq_specialFibre_of_reduction_indep` gives `Fib` from `Indep`.
7. `T.hasGradedCharts_near_generic_point_closure` gives `HasCharts`.

## In the Lean code

The theorem is in [BaseFactsHasGeoExistsClos.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/BaseFactsHasGeoExistsClos.lean#L22). `Clos`, `Ext` and `BaseFacts` are in [BaseFacts.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/BaseFacts.lean#L14), the core properties in [IsNormalSchemeSp.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/IsNormalSchemeSp.lean#L90), and `HasU`, `HasGeo` in [IsBasisB.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/IsBasisB.lean#L119).

`UTorsSt` is used only in step 3. We have not unfolded `RatModel`, `Over₀`, `IsEE`, `M.Div`, `Crd`, `ImmBy` or the core `Test`, and we have not opened the proofs of the lemmas.
