---
id: min-st5
title: A theta compactification of the Siegel moduli scheme by a theta map
kind: theorem
decl: GlobalTheory.SiegMinTop.minSt5
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MinimalSiegelCompactificationExists
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem builds a projective normal compactification $Z$ of the Siegel moduli scheme $X$ over $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$: it maps $X$ to projective space by theta constants and normalizes. It also gives a finite cover of $Z$ with a semi-abelian scheme $G$, on which a power of the Hodge bundle of $G$ is the pullback of $\mathcal{O}_Z(1)$. It proves $\mathrm{MinSt5}$ through [the statement form](/entry/minimal-siegel-compactification-exists/), which is input 2 of [the toroidal compactification](/entry/siegel-toroidal-pol-charts/).

## Statement

$\mathrm{MinSt5}$ and its clauses 1 to 4 are in [the statement form](/entry/minimal-siegel-compactification-exists/).

## Proof

Fix $g$, odd $n \geq 3$ and a Siegel family with base $X$ and universal abelian scheme $A$.

1. **Choices.** Take an odd prime $\ell \mid n$. `exists_isE8_isSharpBasis` gives an $8 \times 8$ matrix $W$ with `IsE8 W` and a basis adapted to it. `siegelModuli_integral_normal_locallyNoetherian`: $X$ is integral, normal and locally noetherian.
2. **The theta map.** `exists_polarised_E8ThetaPower_over_moduli` gives a polarized abelian scheme $P$ over $X$ of dimension $8g$: the product $A^8$ with the polarization given by $W$, and a rigidification. `siegelThetaMap_deepLevel_finite_fibres` gives $j_0$. Put $m = \ell^{j_0+1}$, a unit in $\Lambda_n$. `exists_thetaMap_eighthPower_siegelModuli` gives a theta map $f \colon X \to \mathbb{P}^N_{\Lambda_n}$ of level $m$, with $N + 1 = m^{32g}$. By the choice of $j_0$, $f$ has finite geometric fibres.
3. **The compactification.** `exists_finite_normalisation_projective_quasiFinite` gives a normal integral $Z$, a finite $p \colon Z \to \mathbb{P}^N$ and a dense open immersion $i \colon X \to Z$ with $p \circ i = f$. `finite_over_projectiveSpace_projective_ample_twist`: $Z$ is projective over $\Lambda_n$ and $\mathcal{O}_Z(1) := p^*\mathcal{O}(1)^{\otimes 8}$ is ample.
4. **The cover.** `exists_realisedThetaSystem_normalLevelModel` gives a ring $o$ finite over $\Lambda_n$, a field $\Omega$ and a realized theta system over a point of $X$. `exists_normal_projective_toric_minor_model` gives a normal projective model $M$ of $\Omega$ over $o$, with a semi-abelian scheme $G_8$. `levelCover_openImmersion_normalisedThetaClosure` and `level_cover_image_open_finite_over_moduli` give a dense open $U \subset M$ and a finite surjective $c \colon U \to X$. `eighth_power_first_factor_theta_model` gives $G$ over $M$ with $G|_U = c^*A$ and $\omega_{G_8} \cong \omega_G^{8}$.
5. **The map $\pi \colon M \to Z$.** Symmetric functions $e$ of the theta constants are projective coordinates of $f$ at the generic point (`exists_symmetric_theta_constants_eq_thetaMap_coords`). `thetaConstant_pow_eq_unit_mul_symmetricFunction` relates $e$ to the theta constants by `SameScale`, which we have not unfolded. So $e$ defines $h \colon M \to \mathbb{P}^N$ (`exists_projSpace_map_of_tuple_hasDivisor`), and $h|_U = f \circ c$ (`eq_of_same_generic_projective_coords`). As $M$ is normal and $p$ is finite, $h$ lifts to $\pi$ with $\pi|_U = i \circ c$ and $p \circ \pi = h$ (`normal_scheme_extension_through_finite_cover`). The local lemma `lemProper` shows that $\pi$ is proper and surjective and that $Z$ is noetherian.
6. **Theta integrality.** `siegelThetaConstants_projectively_integral_anyBase` gives `ThetaInt` for $f$, hence for $i$.
7. **The bundle.** `TupleBundle.exists_lb_of_hasDiv` gives a line bundle $\delta$ on $M$ with the theta constants as sections. Then $h^*\mathcal{O}(1) \cong \delta^{(N+1)!}$ (`pull_O1_section_coordinates_power`) and $\delta^{8} \cong \omega_{G_8}^{4}$ (`thetaConstantBundle_pow_eight_iso_detHodge_pow_four`). In the Picard group, $\pi^*\mathcal{O}_Z(1) \cong h^*\mathcal{O}(1)^{8} \cong \omega_G^{32 (N+1)!}$.

## In the Lean code

The theorem is in [MinimalSiegelCompactificationExists.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinimalSiegelCompactificationExists.lean#L78), with `lemProper` (line 40) and `lemGen` (line 59) in the same file. Most lemmas in steps 1 to 7 are `GlobalTheory.T` statement forms of lemmas in other namespaces. We have not opened their proofs. Step 7 compares classes in a Čech Picard group (`CechPic.cls_eq_iff`).

As in the [unitary case](/entry/umin-theta-compactification-exists/), nothing in `MinAt5` asks that $Z$ be minimal. $Z$ has the shape of the minimal compactification of Faltings and Chai, *Degeneration of Abelian Varieties* (1990), Chapter V, but we have not compared the statements.
