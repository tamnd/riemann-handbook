---
id: factor-unif
title: The image of an idempotent is uniformised by the factor data
kind: theorem
decl: GlobalTheory.Mum.factor_unif
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentFactorUniformisedOfDegDataFactor
covers: 465
status: drafted
drafted_by: writer@claude
---
This theorem proves that the factor $G$ of a uniformised semi-abelian $G'$, cut out by an idempotent, is uniformised by the factor data $D$ after a finite extension of the base. It is restated as [`idempotentFactor_uniformised_of_degData_factor`](/entry/idempotent-factor-uniformised-of-deg-data-factor/), step 7 of [`has_of_base`](/entry/has-of-base/). The work is in [`factor_unif_at_trait`](/entry/factor-unif-at-trait/); this proof turns one complete trait into a finite extension.

## Statement

The statement is the one of the [restatement entry](/entry/idempotent-factor-uniformised-of-deg-data-factor/), which defines all objects. In short: $R$ satisfies `Base R`; $F \colon D \to D'$ is a factor with `F.Alg`, ring $O$, idempotent $e$ and element $f$; $U'$ is an $O$-linear uniformisation of a semi-abelian $G'$ by $D'$ with line bundle $L'$; and $G$ is a semi-abelian scheme with $\mathrm{inc} \colon G \to G'$, $\mathrm{pr} \colon G' \to G$, $\mathrm{pr} \circ \mathrm{inc} = 1$, $\mathrm{inc} \circ \mathrm{pr} = e$.

**Theorem.** There are a finite extension $\rho \colon R \to R_1$, a pullback $D_1$ of $D$, the group pullback $G_1 = \rho^* G$ by $\beta$, and a uniformisation $U_1$ of $G_1$ by $D_1$ with $\Lambda(L_1) \cong (\beta \times \beta)^* (\mathrm{inc} \times f \circ \mathrm{inc})^* \Lambda(L')$.

## Proof

1. [`semiabelian_uniformization_linear_action_transfer`](/entry/semiabelian-uniformization-linear-action-transfer/) gives a finite extension $\rho_0 \colon R \to R_0$, a pullback $D_0$ of $D$, the pullback $G_0 = \rho_0^* G$ with a cubical line bundle $P$ that satisfies the $\Lambda$ condition, and a uniformisation along one trait: a complete discrete valuation ring $W$ with an injective local map $\varphi \colon R_0 \to W$, a uniformisation $U_W$ of $\varphi^* G_0$ by a pullback $D_W$ of $D_0$, whose line bundle is the pullback of $P$.
2. $R_0$ again satisfies `Base`: it is complete, normal and noetherian by `FinExt`, and of characteristic zero because $\rho_0$ is injective (`charZero_of_injective_ringHom`).
3. `exists_finiteExtension_uniformisation_of_trait_unif`: the trait gives a finite extension $\rho_1 \colon R_0 \to R_1$, a pullback $D_1$ of $D_0$, and a uniformisation $U_1$ of $G_1 = \rho_1^* G_0$ by $D_1$ with $L_1 \cong \beta_1^* L_P$. The same lemma is step 5 of [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).
4. `FinExtComp.finExt_comp_isPullDeg`: $\rho_1 \circ \rho_0$ is a finite extension and $D_1$ is a pullback of $D$.
5. `lbIso_lam_pull_of_isGrpPullback`: the isomorphism of $\Lambda(L_P)$ with the pullback of $\Lambda(L')$ pulls back along $\beta_1$ to an isomorphism for $\Lambda(L_1)$.

The rest is bookkeeping: group pullbacks compose (`IsGrpPullback.comp`), and so do the squares $\beta \times \beta$.

## In the Lean code

The theorem is in [IdempotentFactorUniformisedOfDegDataFactor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentFactorUniformisedOfDegDataFactor.lean#L20). The lemmas `finExt_comp_isPullDeg` and `lbIso_lam_pull_of_isGrpPullback` are in [FinExtCompIsPullDeg.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FinExtCompIsPullDeg.lean#L14) and [ExistsMumfordBundlePullbackGrpPullback.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMumfordBundlePullbackGrpPullback.lean#L16). We read their statements, not their proofs.

The hypothesis `F.Alg` is not used here; it is only passed to the transfer lemma. The conclusion keeps no link between $U_1$ and the action of $O$.
