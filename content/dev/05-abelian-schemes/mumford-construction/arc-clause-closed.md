---
id: arc-clause-closed
title: The archimedean arc condition holds without hypotheses
kind: theorem
decl: GlobalTheory.arcClause_closed
module: Development.AbelianVarietyTheory.Proofs.UniformizationProofs.ArcClauseClosed
covers: 719
status: drafted
drafted_by: writer@claude
---
This theorem proves the toroidal archimedean condition with no hypotheses. It only passes three proved inputs to [`T.holomorphic_degenerationArc_of_uniformisation`](/entry/holomorphic-degeneration-arc-of-uniformisation/), which is a second name of [`HolomorphicArc.main`](/entry/holomorphic-arc-main/). The real content is in that entry. The result is one of the inputs below [the step EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

`ToroidalArchimedeanCondition` holds. In words: take a CM field $E$, a datum (an $\mathcal{O}_E$-lattice with a unimodular alternating form), a level, a fine moduli scheme, and a normal projective model $Y$ that holds the moduli space as a dense open part and carries a semi-abelian scheme. Then each formal arc $\chi \colon \operatorname{Spec} \mathbb{C}[[X]] \to Y$ whose generic point lies in the moduli space has a holomorphic arc (`HolArc`). That is, $\chi$ is the expansion of an analytic family on a half plane $\operatorname{Im} w > T$. The [entry for `HolomorphicArc.main`](/entry/holomorphic-arc-main/) gives the full list of hypotheses and fields.

## Proof

The proof is one term. It applies `T.holomorphic_degenerationArc_of_uniformisation` to:

1. `T.abelianScheme_laws_unconditional.1`, of type `Out.Laws`;
2. `T.abelianScheme_laws_unconditional.2`, of type `Out.Laws2`;
3. `T.thetaUniformisation_complexAbelianVariety`, of type `ThetaUnifAV`.

## In the Lean code

The theorem is at [ArcClauseClosed.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ArcClauseClosed.lean#L10). It has three users. The structure `Known` takes it as the field `n5` in `ArcCM.known_holds`. The lemmas `coeff_neg_eq_zero` in CuspFormBoundGoodPointsExtendsAllPoints.lean and `main_of_lemmas` in ExistsNormalAtOfUnif.lean apply it to a concrete arc. The type `ThetaUnifAV` is also proved under two other names, `thetaUnifAV_all` and `T.theta_uniformisation_complex_abelian_varieties`. The field `theta` of `known_holds` uses the first.
