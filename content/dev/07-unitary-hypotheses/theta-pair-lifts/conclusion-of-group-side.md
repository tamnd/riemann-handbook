---
id: conclusion-of-group-side
title: The host embedding from a group side, in four changes of datum
kind: theorem
decl: GlobalTheory.HeightCounting.TopA.conclusion_of_group_side
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ConclOfGrp
covers: 352
status: drafted
drafted_by: writer@claude
---
This theorem proves `ConclAlt` for a datum $D$ that already has a group side with the right generators. It is step 3 of [a host embedding on a relabelled layer](/entry/exists-side-a-alt/), whose entry states `ConclAlt` in words. The proof changes the datum four times, each time to get more parts of the record.

## Statement

**Theorem.** Assume `AutomorphicFormsFiniteGL`, `RecTExists` (as $h_L$), `DeRhamPotSemistable`, `RayClassFieldSt` and `ChebotarevDegreeOne`. Let $D$ be a datum with empty `Loc`, a character frame $cf$, an embedding $j_E$ and finite types `rep`, such that each $g_k$ is a ray prime of `KQbar D jE` for the modulus $Q_S \cdot q \cdot d$ and `TypesTrue` holds for $D$ and $cf$. Let $\Gamma$ be a group side of $D$ whose generator $\zeta_k$ is the generator of `labDat` $g_k$ for each $k$. Assume `ChiTOk` $D$ $cf$ and `RowDepth` $D$ `rep`. Then `ConclAlt` $h_L$ $D$ $cf$ $j_E$ `rep`.

## Proof

At each change the character frame is copied field by field, and `concl_setK_alt` with the trivial layer `lay0` carries `ConclAlt` back.

1. `exists_rowWD_rowTrue_m_alt` uses `RowDepth` and $h_L$ to give a row datum $R_w$ with `RepresentationParametersHold`.
2. `exists_setAut_wdTie_labConj` gives $D_1 = $ `setAut D …` with the same places `plGw`, a Weil-Deligne tie $T$ with `LabTrue` and `LabConj`, and a row side with the parameters of $R_w$. `exists_kv_of_eq` adapts $\Gamma$ to $D_1$.
3. `exists_cgTrue_charSide` gives $D_2 = $ `setCG D₁ …` with `CGTrueT` and a character side.
4. `exists_nbc_auSide_true_of_isEmpty_loc` gives $D_3 = $ `setBC D₂ C` with an automorphic side that satisfies `AutomorphicSideRealised`.
5. `ParRay.exists_types` uses `RayClassFieldSt` and the ray prime hypothesis to give types $X$ that agree with those of $D_3$ in five parts, the datum $D_4 = $ `setTy D₃ …`, a parameter side and `IotaOk`. `nonempty_plSide` gives a place side, `exists_grp_setTy` moves $\Gamma$ to $D_4$, and `exists_wdSide` uses `DeRhamPotSemistable` to give a Weil-Deligne side.
6. `conclusion_of_au_true_and_types_true` puts the twelve parts into one `CharFrameHostEmbedding` for $D_4$ and proves `ConclAlt` with $L = $ `lay0`.

The labels, `ChiTOk` and `TypesTrue` follow along the agreements.

## In the Lean code

The theorem is in [ConclOfGrp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L127). Steps 3 to 6 are the theorems at lines [109](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L109), [88](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L88), [44](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L44) and [21](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L21). Two lemmas are in [ExistsCgTrueCharSide.lean](lean:Development/AutomorphicArithmetic/Foundations/UnitarySphericalFixing/SatakeParameters/ExistsCgTrueCharSide.lean#L90) and [ExistsTypes.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsTypes.lean#L18).

Odd points:

- `exists_cgTrue_charSide` introduces `AutomorphicFormsFiniteGL` as `_`, and `ParRay.exists_types` does the same with `ChebotarevDegreeOne`. These are the only places where the two hypotheses go, so neither does any work here.
- The names of steps 3 to 5 say what the datum has on input, not what the step adds: `conclusion_of_cusp_galois_true` takes `CGTrueT` and adds the automorphic side.
