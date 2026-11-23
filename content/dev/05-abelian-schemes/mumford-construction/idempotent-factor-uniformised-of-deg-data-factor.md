---
id: idempotent-factor-uniformised-of-deg-data-factor
title: The image of an idempotent is uniformised by the factor data (statement)
kind: theorem
decl: GlobalTheory.T.idempotentFactor_uniformised_of_degData_factor
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentFactorUniformisedOfDegDataFactorStatement
covers: 466
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.factor_unif`](/entry/factor-unif/), which has the real content. Its proof only calls that theorem. It is step 7 of [`has_of_base`](/entry/has-of-base/): once the large data $D'$ are uniformised, the factor $G$ cut out by an idempotent is uniformised by the small data $D$, after a finite extension.

## Statement

Let $R$ satisfy `Base R`, with fraction field $K$. Let $D$ and $D'$ be degeneration data over $R$ for $\mathfrak{m}$, and let $F \colon D \to D'$ be a factor with `F.Alg`, with ring $O$, idempotent $e$ and element $f$ (see [`exists_pelOK_factor`](/entry/exists-pel-ok-factor/)). Suppose given:

- a semi-abelian $G'$ over $R$, a polarised abelian variety $A'$ over $K$ and a uniformisation $U'$ of $G'$ by $D'$ with generic fibre $A'$, with line bundle $L'$;
- actions of $O$ on $A'$ (with the Rosati condition, `PolAV.OAct`) and on $G'$ (`RingAct`), such that $U'$ is $O$-linear (`OLinear`: on the generic fibre, on the abelian part of each thickening, and on the torus through $a \mapsto a^*$ on the lattice);
- a semi-abelian $G$ over $R$ and group maps $\mathrm{inc} \colon G \to G'$, $\mathrm{pr} \colon G' \to G$ with $\mathrm{pr} \circ \mathrm{inc} = 1$ and $\mathrm{inc} \circ \mathrm{pr} = e$.

**Theorem.** There are a finite injective extension $\rho \colon R \to R_1$ with $R_1$ again complete, normal and noetherian (`FinExt`), a pullback $D_1$ of $D$ to $R_1$, the group pullback $G_1 = \rho^* G$ with its projection $\beta$, and a uniformisation $U_1$ of $G_1$ by $D_1$, whose line bundle $L_1$ satisfies

$$\Lambda(L_1) \cong (\beta \times \beta)^* (\mathrm{inc} \times f \circ \mathrm{inc})^* \Lambda(L').$$

Here $\Lambda(L) = m^*L \otimes p_1^*L^{-1} \otimes p_2^*L^{-1} \otimes 0^*L$ (`abelian₂`). So the polarisation of $G_1$ is the one that $f$ and $L'$ induce on the factor.

## Proof

The proof is `Mum.factor_unif`.

## In the Lean code

The theorem is in [IdempotentFactorUniformisedOfDegDataFactorStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentFactorUniformisedOfDegDataFactorStatement.lean#L13). The proof is the tactic `first | exact @GlobalTheory.Mum.factor_unif | ...`. The two statements are identical.
