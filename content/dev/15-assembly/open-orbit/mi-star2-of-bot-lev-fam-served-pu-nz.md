---
id: mi-star2-of-bot-lev-fam-served-pu-nz
title: The period identity from the bottom, level and family conditions
kind: theorem
decl: GlobalTheory.MiTop.miStar2_of_bot_lev_fam_served_puNZ
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MiStar2OfFamilies
covers: 300
status: drafted
drafted_by: writer@claude
---
This theorem proves the period identity `MIstar2` for a real pack $W$ by joining three lemmas. Its only user is the renaming [`mi_star2_of_pu_nz`](/entry/mi-star2-of-pu-nz/), which is step 4 of [the period identity from the family conditions](/entry/mi-star2-of-all-true-alt-alt/). Its hypotheses are listed in the entry of the renaming.

## Statement

Assume `DiscreteSeriesClassification`, `CuspRapidDecay` and `HarishChandraModules`. Let $W$ be a real pack with `BottomHypotheses W`, `LevelHypothesis W`, `FamilyAllConditions W` and `FamilyServedCondition W`, and assume `PuNZ D`. Then `MIstar2` holds for the coefficient space of $W$, with the vectors $e_V$ of the realisation and the space $s_{EE}$.

## Proof

1. **Descent into the even part.** `descent_eV_mem_level_alt` uses `BottomHypotheses` and `LevelHypothesis`. It shows that for each $t$ and $F$, the theta image $\Theta_t(j_R(e_V(t, F)))$ lies in the space `EEl true`. Its proof takes the level data $s$ of `LevelHypothesis`, the models of the bottom hypotheses, and the descent lemma `CxPass.descent_of_types`.
2. **The joint condition.** `joint_of_famAllQ_of_servedQ` uses `CuspRapidDecay` and `HarishChandraModules`. It turns the family conditions and the served condition into `JointCondition W`: a central element $z$ and, for each word $u$, bottom data $d$ with a pin at $z$, an operator $U$ with $\|U\varphi\| = r\|\varphi\|$ for some $r > 0$, nonzero coefficients $c_t$ with a unit condition, and a linear relation `d.Rel U c` between periods.
3. **The identity.** `joint_star_product_nonvanishing_alt` uses `DiscreteSeriesClassification`, `CuspRapidDecay`, `BottomHypotheses`, the results of steps 1 and 2 and `PuNZ D`. It gives `MIstar2`.

## In the Lean code

The theorem is at [MiStar2OfFamilies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamilies.lean#L23). The proof is one term. It calls:

- `GlobalTheory.MiTop.descent_eV_mem_level_alt` in [DescentEVMemLevel.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DescentEVMemLevel.lean#L25);
- `GlobalTheory.T.joint_of_famAllQ_of_servedQ` in [JointOfFamAllQStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/JointOfFamAllQStatement.lean#L19), a renaming of `MiTop.joint_of_famAllQ_alt`;
- `GlobalTheory.T.joint_star_product_nonvanishing_alt` in [MiStar2AtRealisationStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2AtRealisationStatement.lean#L19), a renaming of `MiTop.miStar2_at_realisation_alt`.

We have not opened the two originals.

`LevelHypothesis` is used only in step 1. `HarishChandraModules` is used only in step 2, and `DiscreteSeriesClassification` only in step 3. [The entry above the renaming](/entry/mi-star2-of-all-true-alt-alt/) notes that `FamilyServedCondition` holds for every pack, so that hypothesis costs nothing. The name of `joint_star_product_nonvanishing_alt` speaks of nonvanishing, but its conclusion is `MIstar2`; the nonvanishing is the hypothesis `PuNZ`.
