---
id: exists-setting
title: A measured Hida setting for each datum, with transports
kind: theorem
decl: GlobalTheory.St.SpectralData.exists_setting
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsGlobalSetting
covers: 1556
status: drafted
drafted_by: writer@claude
---
For a datum $D$, this theorem builds a Hida setting with measures, an additive character of the adeles, and transports to given forms. It is step 1 of [`exists_spectralData_gap_alt`](/entry/exists-spectral-data-gap-alt/), which adds a full datum and the decay of the archimedean coefficient. That result goes to the step from level three to level four in branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

**Theorem.** Assume `SiegelWeilUnitaryConvergent`, a finite volume statement and a Siegel-Weil formula for unitary groups (stated in [the counting row](/entry/row-counts-of-ties-alt/)). Let $D$ be a datum (`D7`). For each word $u$ let $F(u)$ be a form `Forms0 D u`. Suppose `GapHyp D`: the rank is $r \ge 1801$, and consecutive Harish-Chandra parameters at each real place differ by at least $16 r^{19}$. Then there are a Hida setting $X$ for $D$, an isomorphism $h_b$ from the adelic group of $X$ to the matrix group (`AdBridgeIso`), and a character $\psi$ of $\mathbb{A}_F$ with these properties:

1. the instance of $X$ is `instOf D`, the instance built from the fields of $D$, and the map of CM fields in $X$ is the identity;
2. `MeasTie`: the measures of $X$ are the images under $h_b$ of the product [[Haar measure|VY0HXD3GC4]] on $G_\infty \times G_f$ and of the measures on the unipotent and stabilizer groups;
3. $\psi$ is continuous, of norm 1, trivial on $F$ and nontrivial, and $\psi_\infty(x) = \exp\bigl(2\pi i \sum_w \operatorname{Re} x_w\bigr)$;
4. $\psi$ is compatible with the mass data (`MeasCompatψ`) and with the local volumes at each $w$ (`LocCompatX`);
5. if the level set $K_2$ of $X$ is a subgroup with a unitary character $\chi_2$, then for each word $u$ there is a transport of $X$ to $F(u)$ that matches the lattice, the level subgroup and the character.

A Hida setting is a large structure: a group record `RowsAut`, a basis matching the hermitian space of $D$, discrete series at the real places, a hyperbolic frame with flags, adelic vectors with congruence conditions, local representations, measures and Whittaker-type functions. A transport is an isometry that moves the frame of $X$ to the frame of $F(u)$, with an isomorphism of adele rings and an isometric, equivariant map to coefficient functions. We did not unfold `MeasCompatψ` and `LocCompatX`.

## Proof

1. `BesselNVGap_holds` and `CoefWeightedLoc_holds` give two facts about discrete series, which we did not unfold.
2. `instanceOfRecord D` gives the instance. `latExists_of_forms0` gives a lattice from $F(u_0)$.
3. The closed lemmas `PsiExists_holds`, `RefExists_holds`, `XuExists_holds`, `BunExists_holds`, `PiExists_holds` and `MuExists_holds` give the next fields. Only `BunExists_holds` uses `GapHyp D`.
4. `realPlaceFunctionBlockExists_of_bessel_coef` gives the real place functions, from step 1 and `GapHyp D`. `mExists_holds` gives the remaining block and $h_b$.
5. `rescaleStep3` gives the measures, $\psi$ and properties 2 to 4. This is the only use of the Siegel-Weil hypothesis.
6. `exists_transport` builds each transport from `wittExists`, `genusMatch_holds`, `levelConj_holds`, `hcExists_all` and `jExists_all`, with the identity map of adele rings.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsGlobalSetting.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsGlobalSetting.lean#L45). The Hida setting is in [HidaSetting.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L179), and `GapHyp` in [ConcreteSettingExists.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ConcreteSettingExists.lean#L13).

Property 1 holds by `rfl` and `HEq.rfl` (line 68), so the identification of fields is trivial. The adele ring isomorphism of the transport is `RingEquiv.refl` (line 69).

`CoefWeightedLoc_holds` is `Fact.out` of an instance argument ([CoefWeightedLocHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/CoefWeightedLocHolds.lean#L445)). The instances are in [FactsDS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/WeightedGaugeFactors/FactsDS.lean#L16), imported at line 7, and are proved from lemmas in `ReciprocityTheory`. So these facts are proved, not assumed. The index of direct uses does not show these instances.
