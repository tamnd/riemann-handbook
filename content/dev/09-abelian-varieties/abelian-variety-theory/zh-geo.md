---
id: zh-geo
title: Extending a theta-level abelian scheme over a projective model
kind: theorem
decl: GlobalTheory.ZH.GeoHalf.zhGeo
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.SemiAbelianSchemeUniformisationExistsGeometric
covers: 1255
status: drafted
drafted_by: writer@claude
---
This theorem proves `ZHGeoSt` from nine hypotheses on abelian and semi-abelian schemes. It is the real content of its chain: [the restatement](/entry/semi-abelian-scheme-uniformisation-exists-geometric/) only calls it, and [`zhGeo_of_semistableReduction`](/entry/zh-geo-of-semistable-reduction/) proves eight of the hypotheses and keeps semistable reduction.

## Statement

**Hypotheses.** Homomorphisms of semi-abelian schemes over a discrete valuation ring extend uniquely from the generic fibre; `SemistableReductionSt` ([top entry](/entry/zarhin-geometric-of-semistable-reduction/)); `ThmUSt` and `UTorsSt` on degeneration data ([next entry](/entry/zh-geo-of-semistable-reduction/)); `Laws` to `Laws5`, five bundles of facts on abelian schemes.

**Conclusion** `ZHGeoSt`. Let $o \subset \Omega$ be a Dedekind domain of finite type over $\mathbb{Z}$ in a field of characteristic zero. Assume:

- a theta system $S$: integers $g$, $N \geq 2$, $r \geq 1$, a root of unity $\zeta \in o$ of order $(rN)^2$, and a projective representation $\rho$ of $\Gamma = (\mathbb{Z}/rN)^{2g}$ on $o^J$, $J$ finite;
- theta values $\theta \colon \Gamma \to \Omega$ in a finitely generated $o$-algebra $R$ with fraction field $\Omega$;
- a realization: a polarized abelian scheme $(A, L)$ over $\operatorname{Spec} R$ with level-$rN$ torsion sections $P_a$, a section $\theta_1$ of $L$ with $\theta_1(P_a) = \theta(a)$, and a basis $(s_j)$ of sections of $L^N$ on which the theta group acts by $\rho$;
- `S.Big`: $N$ and $rN$ are large in terms of $g$;
- a normal integral scheme $Z$, projective over $o$, with function field $\Omega$, and an open set $U_0 \neq \emptyset$ on which $R$ and the inverses of the nonzero $\theta(a)$ are regular;
- a lattice $E(z) \subset \Omega^J$ over each local ring of $Z$, standard on $U_0$ and fixed at $p$-adic points by tests (`IsEE`);
- some vectors that span the dual of each $E(z)$.

Then `ZHOut` is not empty. Its fields:

- a semi-abelian scheme $G$ over $Z$, smooth of relative dimension $g$, quasi-projective, with $G|_{U_0} \cong u_0^* A$ for a map $u_0 \colon U_0 \to \operatorname{Spec} R$;
- a rigidified symmetric cubical line bundle $\mathcal{L}$ on $G$ with $\mathcal{L}|_{U_0} \cong u_0^* L$;
- unique extension of endomorphisms and of some line bundle isomorphisms from the generic fibre;
- each fibre is an extension of an abelian variety by a split torus;
- $G$ is proper exactly where a subgroup $T(z) \subset \Gamma$, defined from `M.Div`, is zero, and there $\mathcal{L}$ is ample;
- torsion sections extend locally;
- a uniformisation by degeneration data over complete normal local rings that meet the abelian locus;
- extensions of $\theta_1$ and of the $s_j$, independent on fibres, that immerse $G$ in projective space over $Z$.

So an abelian scheme with a theta structure over $U_0$ extends to a semi-abelian scheme over $Z$, embedded by theta sections. We know no published theorem with exactly this statement.

## Proof

The proof is `zhGeo_of` applied to twelve theorems. By purpose:

1. **Set-up.** `thetaSystem_hasTests_of_real_point` and `baseFacts_hasGeo_exists_clos` give $p$-adic tests and a closure `Clos` of the abelian scheme.
2. **A first extension.** `exists_semiAbelian_groupScheme_cubical_bundle_closure`, with two theorems on torsion and theta sections, gives a group scheme with a cubical bundle (`ZHPre`).
3. **Its properties.** Five theorems, among them `abelianLocus_eq_trivial_torus_locus_proper` and `thetaSections_independent_on_closed_fibre`, give the abelian locus, the torsion sections and the theta sections.
4. **Assembly.** `nonempty_of_fourProperties_groupScheme`, with `exists_uniformisation_completeLocalNormalDomain` and the extension of homomorphisms, turns these into a `ZHOut`.

## In the Lean code

The theorem is in [SemiAbelianSchemeUniformisationExistsGeometric.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemiAbelianSchemeUniformisationExistsGeometric.lean#L31), `zhGeo_of` in [SecOfIso.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SecOfIso.lean#L52), and `ZHGeoSt` with `ZHOut` in [ImmersedBy.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/ImmersedBy.lean#L109). We have not unfolded `Clos`, `DegData`, `Unif`, `Test`, `M.Div` or `HypS`.

Odd points:

- The last hypothesis of `ZHGeoSt`, on dual lattices, is never used: `zhGeo_of` introduces it as `_` ([SecOfIso.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SecOfIso.lean#L66)).
- Only the second part of `thetaSystem_hasTests_of_real_point` is used; `S.HasTests` is dropped.
