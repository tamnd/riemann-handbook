---
id: shift-extra
title: The extra relations of the normal form
kind: theorem
decl: Formalism.FourierDecayAlt.P.shift_extra
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.NormalFormOrderZeroOfParts
covers: 540
status: drafted
drafted_by: writer@claude
---
This theorem proves `NF.SExtra`: four relations among the operators of normal-form data follow from the basic relations `d.Rel` and the start condition on the matrix `QQ`. [The phase change](/entry/second-shift-phase-holds/) uses one of them, the twisted commutation of two shifts. The proof assembles four lemmas; the curvature relation is [`curv`](/entry/curv/).

## Statement

Let $A$ be a ring with an involution and a $\mathbb{C}$-algebra structure. Normal-form data $d$ in $A$ (`Q.NFData`) are level data $L$ (elements $\zeta, \bar\zeta, G, G^{-1}, \nabla, \nabla^*$ of $A$ and others), an algebra map $\kappa$ from functions on types to $A$, and elements $S_l$ of $A$. Types, $r_i(\rho)$, $e_l$ and $N_l$ are as in [the phase change](/entry/second-shift-phase-holds/). $N^{\downarrow}_l$ (`M.NrmDown`) is the same kind of quotient, with the polynomial taken at $-r_l(\rho)$. From $d$ one builds a $2 \times 2$ matrix $Q(Y)$ over $A$ (`d.QQ`). The relations `d.Rel` say: $\kappa$ respects the involution; $\kappa(f)$ commutes with $\nabla$, $\nabla^*$ and the level functions; $S_l$ commutes with the level functions and with the elements $p$, $\bar p$; $\kappa(g) S_l = S_l \kappa(f)$ when $g(\rho + e_l) = f(\rho)$; $\nabla S_l = S_l \nabla - \bar\zeta G^{-1} S_l$ and $\nabla^* S_l = S_l \nabla^* - \zeta G^{-1} S_l$; and $S_l^* S_l = \kappa(N_l)$.

The start condition `Wd.IsStart Q q` says: $Q(Y)$ is Hermitian for real $Y$, $Q$ satisfies an RTT relation, a determinant condition with the function $q$, and $q$ is real on the real line. Here $q(Y) = -T T' \prod_{i=1}^{k} (Y + \tfrac12 + u_i)(Y + \tfrac12 + u'_i)$ (`M.qC`).

**Theorem.** Let $P$ satisfy `P.OK`, and let $d$ satisfy `IsStarLevel`, `d.Rel` and the start condition. Then, with $T = T T'$:

1. $\nabla^* \nabla - \nabla \nabla^* = \kappa(2 a_\rho T)\, G^{-1} G^{-1}$, where $a_\rho$ is the real number `M.aC`;
2. $S_l S_l^* = \kappa(N^{\downarrow}_l)$ for $1 \le l \le k - 1$;
3. $S_j S_l\, \kappa(r_j - r_l - 1) = S_l S_j\, \kappa(r_j - r_l + 1)$ for $j \ne l$;
4. $S_l^* S_j = S_j S_l^*$ for $j \ne l$.

## Proof

`hyp_of_rel` keeps four of the six relations of `d.Rel` (the involution, the commutation of $\kappa$, the shift rule for $\kappa$, and $S_l^* S_l = \kappa(N_l)$) as the structure `Hyp`. Then `ssDown` gives 2, [`curv`](/entry/curv/) gives 1 using 2, `ssComm` gives 3 and `ssMixed` gives 4. Each of these compares both sides after right multiplication by the projections $\kappa(\delta_\rho)$ (`ext_right`). We have read only the statements of `ssDown`, `ssComm` and `ssMixed`.

## In the Lean code

The theorem is at [NormalFormOrderZeroOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2912). `SExtra` and `RelExtra` are in [ActualZetaSmooth.lean](lean:Formalism/HermitianCurvature/ActualZetaSmooth.lean#L44), `NFData`, `QQ` and `Rel` in [StatementQ.lean](lean:Formalism/HermitianCurvature/StatementQ.lean#L1026), and `IsStart` in [StatementWd.lean](lean:Formalism/HermitianCurvature/StatementWd.lean#L79).

- `hyp_of_rel` and `Hyp`: [line 1653](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L1653).
- `ssDown`: [line 1897](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L1897); `ssMixed`: [line 2247](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2247); `ssComm`: [line 2427](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2427).
- `curv`: [line 2865](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2865).

The hypothesis `IsStarLevel` is never used: the proof binds it as `_`. Two relations of `d.Rel` are also dropped by `hyp_of_rel`: the commutation of $S_l$ with the level functions and the rule for $\nabla S_l$. The theorem is restated as `nf_sExtra` in [HeisenbergConjugationMeasurePreserving.lean](lean:Formalism/HermitianCurvature/HeisenbergConjugationMeasurePreserving.lean#L2110).
