---
id: factor-unif-at-trait
title: The factor of a uniformised group is uniformised along one trait
kind: theorem
decl: GlobalTheory.Mum.FactorTrait.factor_unif_at_trait
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiabelianUniformizationLinearActionTransfer
covers: 462
status: drafted
drafted_by: writer@claude
---
This theorem gives, after a finite extension $R \to R_0$, a cubical line bundle on the factor $G_0$ and a uniformisation of $G_0$ along one complete trait of $R_0$ by a pullback of the factor data $D$. It is restated as [`semiabelian_uniformization_linear_action_transfer`](/entry/semiabelian-uniformization-linear-action-transfer/), and [`factor_unif`](/entry/factor-unif/) turns the trait into a finite extension.

## Statement

The statement is the one of the [restatement entry](/entry/semiabelian-uniformization-linear-action-transfer/). The hypotheses: $R$ satisfies `Base R`, $F \colon D \to D'$ is a factor with `F.Alg`, $U'$ is an $O$-linear uniformisation of $G'$ by $D'$, and $\mathrm{inc}$, $\mathrm{pr}$ split the idempotent $e$ with image $G$. The conclusion: a finite extension $\rho_0 \colon R \to R_0$, a pullback $D_0$ of $D$, the semi-abelian pullback $G_0 = \rho_0^* G$ with a cubical bundle $P$ whose $\Lambda(L_P)$ is the pullback of $\Lambda(L')$ by $\mathrm{inc} \times f \circ \mathrm{inc}$, and a complete discrete valuation ring $W \supseteq R_0$ (injective local map) over which $G_0$ is uniformised by a pullback of $D_0$, with line bundle $L_P$.

## Proof

1. `exists_finExt_cubicalSymmetric_even_factor`: after a finite extension $R \to R_9$, the pullback $G_9$ of $G$ has a cubical bundle $P_9$ with the $\Lambda$ condition that is even on the torus (`EvenOn`), and its generic fibre is a polarised abelian variety $A_9$ with matching line bundle. This is the only step that uses `F.Alg`.
2. `semiabelian_uniformization_linear_action_descent`: from these data, there are a finite extension $R \to R_0$ and $D_0$, $G_0$, $P$ and $A_0$ with the same properties, and with $D_0$ a pullback of $D$. It also gives a clause on traits: for each complete trait $\varphi \colon R_0 \to W$ and each uniformisation $U_W$ of $\varphi^* G_0$ with line bundle the pullback of $L_P$, the data of $U_W$ are a pullback of $D_0$.
3. $R_0$ satisfies `Base`: it is complete, normal and noetherian by `FinExt`, and of characteristic zero since $R \to R_0$ is injective.
4. `exists_uniformisation_completeLocal_evenOnTorus`: $G_0$ with the even bundle $P$ and generic fibre $A_0$ is uniformised over $R_0$ by some data $D''$, with line bundle $L_P$.
5. `exists_trait_of_unif` (same file): `PrimeUnif.exists_cdvr` gives a complete discrete valuation ring $W$ with an injective local map $\varphi \colon R_0 \to W$. The base change law `UT.EndBaseChange.exists_pull`, with laws from `GlobalTheory.firstFiveLaws`, pulls the uniformisation of step 4 back to $\varphi^* G_0$.
6. The clause on traits of step 2 shows that the data over $W$ are a pullback of $D_0$.

## In the Lean code

The theorem is in [SemiabelianUniformizationLinearActionTransfer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiabelianUniformizationLinearActionTransfer.lean#L43), with the helper `exists_trait_of_unif` at [line 20](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiabelianUniformizationLinearActionTransfer.lean#L20). We read the statements of the lemmas of steps 1, 2 and 4, not their proofs.

The data $D''$ of step 4 are used only to produce the uniformisation over $W$. The proof drops the clause `U.gen = gen` of step 4. The file name and the name of the restatement speak of a linear action, but the conclusion has no action of $O$.
