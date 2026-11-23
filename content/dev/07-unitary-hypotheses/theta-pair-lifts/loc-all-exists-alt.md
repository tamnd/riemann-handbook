---
id: loc-all-exists-alt
title: Localization data with an automorphic specialization exist
kind: theorem
decl: GlobalTheory.HeightCounting.locAll_exists_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LocAllExists
covers: 453
status: drafted
drafted_by: writer@claude
---
For a datum $D$ and each finite choice `big`, this theorem builds localization data $L$ with a Hecke specification, an automorphic specialization and semisimple residual representations. This is `AutomorphicSideExists`, written out. It is restated as [`side_rational_hecke_data_alt`](/entry/side-rational-hecke-data-alt/), which [the automorphic side at a stage](/entry/built-ex-of-published-inputs-prime/) applies.

## Statement

Let $D$ be a datum of type `D7`, with CM field $E$. Fix a character frame `cf`, an embedding $j_E \colon E \to \overline{\mathbb{Q}}$, coefficient data $A$, rational data $S$ with its operators, eigenvalues and two characters $\theta_k$ of $(\mathbb{Z}/g_k)^\times$, a side datum `Bs`, a family $M$, a norm choice $C$ and a tuple `tp` tied to it.

**Theorem.** Assume global Artin reciprocity and:

1. `ChoiceSide` and `MtInput`;
2. the ring $\mathrm{LL}_0$ is stable under `star`;
3. each exponent `eExp D j g` is an integer;
4. the places of $E$ over the primes `pde` and `pde'` split;
5. `ChebSplit` for `D.nd`;
6. at each twisted place $w$ the twist character $\psi_w$ has values in $\mathrm{LL}$;
7. the map `OtoLL` is injective, and its image is the set of integral elements of a subfield;
8. `BlocksUnique D`.

Then for each `big` there are $L$ of type `LocAll (lay0 D)` and `Sp : NdSpec` for $L$, with an `AutomorphicSpecialisation` and with each residual representation `L.Z.rbar σ λ` semisimple.

`BlocksUnique D` says: two lists of conjugate self-dual blocks with the same total rank and the same local classes at all split places have the same multiset of pairs $(a, d)$.

## Proof

1. [`side_rational_eigen_data_alt`](/entry/side-rational-eigen-data-alt/), with the theorem `heckeStdPlain`, gives the Hecke localization $X$, the twist data $T$ and `Sp`.
2. `side_rational_level_data_alt` gives automorphic data $Y$, base change data $C_b$ and an `AutomorphicSpecialisation`.
3. `locBr_of_autSpec_alt` gives the local bridges $B_r$.
4. `side_rational_character_data_alt` gives the values of the characters $\chi_i$ at the elements `tg k v`: Teichmüller lifts of `chiT k v` or of its inverse.
5. `typeV_iSup_indep_alt` gives equal sums of type spaces for two indices with the same $\mu$ and $j$.
6. From `BlocksUnique`, `ChebSplit` and steps 4 and 5, `locTy_exists` gives the type data $Z$, the three ties, and the semisimplicity of the residual representations.

## In the Lean code

The theorem is in [LocAllExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocAllExists.lean#L17). `LocAll` is in [LocAutHodgeTateWeightsLevelZeroDef.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/LocAutHodgeTateWeightsLevelZeroDef.lean#L372), `BlocksUnique` in [BlocksUnique.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/BlocksUnique.lean#L118), and `locTy_exists` in [IsOpenKerMapRep.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/IsOpenKerMapRep.lean#L115).

- The older `locAll_exists` in [SideRationalHeckeData.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SideRationalHeckeData.lean#L20) has the same shape, with `SideA` in place of `CharFrameHostEmbedding`.
- The hypothesis `HeckeStdPlain` of step 1 is not a hypothesis here. It is the proved theorem `heckeStdPlain` in [HeckeDoubleCosetOperatorsStandardFacts.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HeckeDoubleCosetOperatorsStandardFacts.lean#L671).
- We have read the statements of the lemmas of steps 2 to 6, not their proofs.
