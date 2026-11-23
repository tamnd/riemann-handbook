---
id: normal-form-from-module-statement
title: The normal form of the actual operators, assembled
kind: theorem
decl: Formalism.FourierDecayAlt.P.normalFormFromModule_statement
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.QNFAsm
covers: 429
status: drafted
drafted_by: writer@claude
---
This theorem proves `NormalFormFromModule` with no hypothesis. It is a pass-through: it fills the five inputs of a general reduction with five proved theorems. The real content is in [Theorem S for a star algebra](/entry/theorem-s-ring/), which holds 318 of the 429 declarations below. Through `normal_form_actual` and `level_start_actual` in the same file, it lies below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

## Statement

Fix data $(W_p, W_q, P, z, z', \pi, \pi')$ with `IsPlace`. Let $\mathcal{R}$ (`RadSp`) be the space of smooth $\mathrm{Hom}(W_q, W_p)$-valued functions that are equivariant under $\pi$ and $\pi'$. A record $X$ of type `ActualOps` is a family of operators on $\mathcal{R}$, among them a $2 \times 2$ matrix $Q_X(Y)$ for each $Y \in \mathbb{C}$.

`NormalFormActual` says: for each such $X$ there is normal-form data $d = (L, \kappa, (S_l))$ such that $L$ is the actual level of $X$ and a star level, $d$ satisfies `d.Rel`, and $Q_X = Q_d$. Here $Q_d$ is the matrix built from $d$, as in [the extra relations of the normal form](/entry/shift-extra/).

**Theorem.** The five statements `ActualStart`, `ZetaComm`, `Leading`, `RadialDecompositionSpectral` and `ActualOpsExist` together imply `NormalFormActual`.

## Proof

The proof applies the general reduction `normal_form_from_module` to [`theorem_S_ring`](/entry/theorem-s-ring/), `actual_pre_level`, `actual_hypotheses_of_parts`, `level_coordinates_commute` and `types_complete`.

Inside the reduction, `ActualPreLevel` gives a pre-level $L_0$ for $X$, the spectral hypotheses give $\kappa$, and Theorem S gives $d$ with $L$ extending $L_0$. The rest is bookkeeping.

## In the Lean code

The theorem is in [QNFAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/QNFAsm.lean#L13). The statement is in [StatementQ.lean](lean:Formalism/HermitianCurvature/StatementQ.lean#L1110). The caller `normalFormActual_of_fromModule` ([InvariantOperatorUnderJacquet.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/InvariantOperatorUnderJacquet.lean#L92)) fills the five hypotheses with proved theorems.

Odd points:

- The reduction `NFx3.normalFormFromModuleOfParts` drops the hypothesis `ActualOpsExist` with `_` ([InterpolationInverseMatrixSumIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/InterpolationInverseMatrixSumIdentity.lean#L139)). So that hypothesis of `NormalFormFromModule` is never used.
- The same file proves `actual_spectral_hypotheses` at line 9. This theorem does not use it, and passes the uninstantiated `actual_hypotheses_of_parts` instead.
