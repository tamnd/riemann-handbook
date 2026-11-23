---
id: umin-theta-compactification-exists
title: An integral compactification as a normalization of a theta map
kind: theorem
decl: GlobalTheory.umin_theta_compactification_exists
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryIntegralCompactificationExistsViaTheta
covers: 311
status: drafted
drafted_by: writer@claude
---
This theorem builds an integral compactification of the unitary moduli scheme $X^\circ_F$. It maps $X^\circ_F$ to projective space over a localization $o$ of $\mathcal{O}_F$ by theta constants, and normalizes. Through three renamings ([the via-theta form](/entry/unitary-integral-compactification-exists-via-theta/), [`uMinSt_holds`](/entry/u-min-st-holds/) and [the statement form](/entry/unitary-integral-compactifications-exist/)) the result goes to step 1 of [`uPoinStX_sep`](/entry/u-poin-st-x-sep/).

## Statement

Fix a CM field $E$ with `Host E`, a hermitian datum $D$ of signature $(p, q)$ with $p + q \geq 1$, a level, the moduli scheme $X^\circ$, and a number field $F \subset \mathbb{C}$ of coefficients. Let $g = \tfrac{[E:\mathbb{Q}]}{2}(p + q)$.

**Theorem** (`UMinSt`). There is a `UCompact` for $X^\circ_F$, that is:

1. *Base.* A Dedekind domain $o \subset F$ of finite type over $\mathbb{Z}$ with fraction field $F$, in which $M'$ (from the level), $d$ (from the host) and $\operatorname{disc}(E)$ are units.
2. *Model.* A normal scheme $Z$, projective over $o$, with a dense open immersion $X^\circ_F \to Z \times_o F$ over $F$, whose image is also dense in $Z$. Write $i \colon X^\circ_F \to Z$.
3. *Bundle.* An ample line bundle $\mathcal{O}_Z$ and $N \geq 1$ such that $f^*\mathcal{O}_Z \cong (\det\omega_Y)^{N}$ for each model $Y$ of $X^\circ_F$ over $F$ with a map $f$ to $Z \times_o F$ that extends $i$, when $\det\omega_Y$ is a line bundle.
4. *Extension* (`ext`). Let $R$ be a local domain with `Mum.Base`, $t$ a semi-abelian scheme over $R$ with a uniformization `PELUnif` at the maximal ideal, and $y$ a point of $X^\circ_F$ over $\operatorname{Frac} R$ linked to $t$ by `GenOf`. Then $i \circ y$ extends to an $R$-point of $Z$ over any given $\operatorname{Spec} R \to \operatorname{Spec} o$ that is compatible.
5. *Theta integrality* (`thetaInt`). For each theta system realized over a point of $X^\circ_F$ that is generic, and each normal model $M$ of its field with a map $M \to Z$, at each point of $M$ some theta constant $\vartheta_a$ is nonzero and every ratio $\vartheta_b/\vartheta_a$ is regular there.

## Proof

1. `exists_baseRing_away` gives $o = \mathcal{O}_F[1/(3M'd\operatorname{disc}E)]$.
2. Choose $j$ with $81^g g! < 3^{j} \cdot 81$. Put $m = 3^{j+4}$ and $n + 1 = m^{4g}$. Then $m \in o^\times$.
3. `moduliScheme_coefficientField_normal_noetherian_separated`: $X^\circ_F$ is normal, locally noetherian, of characteristic zero, separated and of finite type over $F$.
4. `thetaMap_abelianScheme_normal_charZero_base`, with `polFib_univ` (the fibres of the universal object are polarized abelian varieties of dimension $g$): a theta map $f \colon X^\circ_F \to \mathbb{P}^n_o$ of level $m$ (`ThMap`).
5. `thetaMap_finite_geometricFibres_of_large_level`: $f$ has finite fibres on geometric points. The bound on $j$ is used here.
6. `integral_normal_model_dense`: let $Z$ be the normalization of $\mathbb{P}^n_o$ in $X^\circ_F$ along $f$. Then $p \colon Z \to \mathbb{P}^n_o$ is finite, $Z$ is normal, and clause 2 holds.
7. `isProjOver_and_isAmpleLB`: $Z$ is projective over $o$ and $\mathcal{O}_Z = p^*\mathcal{O}(1)^{8(n+1)!}$ is ample.
8. Clause 3 with $N = 4((n+1)!)^2$ is `theta_map_pull_O1_power`. Clause 4: `uniformisedPoint_extends_along_thetaMap` extends the point into $\mathbb{P}^n_o$, and `finite_morphism_valuative_lifting_normal_domain` lifts it through the finite map $p$. Clause 5 is `thetaConstants_projectively_integral_normalModels`.

## In the Lean code

The theorem is in [UnitaryIntegralCompactificationExistsViaTheta.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryIntegralCompactificationExistsViaTheta.lean#L78), with `exists_baseRing_away` and `integral_normal_model_dense` in the same file. `UCompact` is in [ExistsRatPointOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRatPointOfFiniteType.lean#L370). The normalization is Mathlib's `Scheme.Hom.normalization`. The proof reads from `Mum.Base R` an instance that makes $R$ integrally closed (line 137); we have not unfolded `Mum.Base`, `PELUnif`, `GenOf` or `UOver`.

The name `UMinSt` suggests a minimal compactification. Nothing in `UCompact` asks that $Z$ be minimal: it is any normal projective model with clauses 1 to 5.
