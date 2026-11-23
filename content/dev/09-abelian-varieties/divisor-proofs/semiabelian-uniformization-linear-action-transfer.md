---
id: semiabelian-uniformization-linear-action-transfer
title: The factor of a uniformised group is uniformised along one trait (statement)
kind: theorem
decl: GlobalTheory.T.semiabelian_uniformization_linear_action_transfer
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiabelianUniformizationLinearActionTransferStatement
covers: 463
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.FactorTrait.factor_unif_at_trait`](/entry/factor-unif-at-trait/), which has the real content. Its proof only calls that theorem. It is step 1 of [`factor_unif`](/entry/factor-unif/), which turns its trait into a finite extension.

## Statement

The hypotheses are those of [`factor_unif`](/entry/factor-unif/), defined in the [entry for its restatement](/entry/idempotent-factor-uniformised-of-deg-data-factor/): $R$ satisfies `Base R`; $F \colon D \to D'$ is a factor with `F.Alg`, ring $O$, idempotent $e$ and element $f$; $U'$ is an $O$-linear uniformisation of a semi-abelian $G'$ by $D'$ with line bundle $L'$; and $\mathrm{inc} \colon G \to G'$, $\mathrm{pr} \colon G' \to G$ split the idempotent $e$, with $G$ semi-abelian.

**Theorem.** There are:

1. a finite injective extension $\rho_0 \colon R \to R_0$ (`FinExt`) and a pullback $D_0$ of $D$ to $R_0$;
2. the group pullback $G_0 = \rho_0^* G$ by $\beta_0$, which is semi-abelian, with a cubical line bundle $P$ (`CP`) such that $\Lambda(L_P) \cong (\beta_0 \times \beta_0)^* (\mathrm{inc} \times f \circ \mathrm{inc})^* \Lambda(L')$;
3. a complete discrete valuation ring $W$ with an injective local map $\varphi \colon R_0 \to W$, the group pullback $G_W = \varphi^* G_0$ by $\beta$, and a uniformisation $U_W$ of $G_W$ by data $D_W$ that pull back $D_0$, with $L_{U_W} \cong \beta^* L_P$.

Here $\Lambda(L) = m^*L \otimes p_1^*L^{-1} \otimes p_2^*L^{-1} \otimes 0^*L$ (`abelian₂`).

## Proof

The proof is `Mum.FactorTrait.factor_unif_at_trait`.

## In the Lean code

The theorem is in [SemiabelianUniformizationLinearActionTransferStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiabelianUniformizationLinearActionTransferStatement.lean#L13). The proof is the tactic `first | exact @GlobalTheory.Mum.FactorTrait.factor_unif_at_trait | ...`. The two statements are identical.

The name speaks of a transfer of a linear action. The conclusion has no action of $O$: it gives a cubical bundle on the factor and a uniformisation of the factor along one trait.
