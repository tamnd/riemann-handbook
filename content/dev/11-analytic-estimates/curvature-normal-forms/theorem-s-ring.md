---
id: theorem-s-ring
title: Theorem S for a star algebra
kind: theorem
decl: Formalism.FourierDecayAlt.P.theorem_S_ring
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.ConnectionRaisingConstantEq
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThmSRing` with no hypothesis. It builds normal-form data from a matrix $Q$ that satisfies the spectral hypotheses. [The assembled normal form](/entry/normal-form-from-module-statement/) applies it to the actual operators. The proof joins three steps: a block form, a connection and a norm.

## Statement

Let $A$ be a ring with a star and a $\mathbb{C}$-algebra structure. Let $P$ be parameters with `P.OK`, with $k$ and the set of types $\rho$ (`M.Ty P`). Let $L_0$ be a pre-level in $A$: elements $\zeta, \bar\zeta, G, G^{-1}, T$ and families $p_l, \bar p_l, c_l, \bar c_l$ with their inverses, with fixed commutation laws. Let $Q : \mathbb{C} \to M_2(A)$ and let $\kappa$ be an algebra map from functions on types to $A$. Index rows and columns by $0, 1$.

`SHyp` asks: $\zeta^* = \bar\zeta$, $T^* = T$, $c_l^* = \bar c_l$, $p_l^* = -\bar p_l$; $Q$ is a start matrix for $q_C$ (`Wd.IsStart`, not unfolded); the entries $Q(Y)_{10}$ commute for all $Y$; $Q(Y)_{11} = G\, x_\kappa(Y)$; $\kappa$ respects the star and commutes with the operators of $L_0$; $Q$ is polynomial in $Y$ and $Q(Y)_{10} = -Y^k \bar\zeta$ plus terms of lower degree; six commutation rules of the entries with $\zeta$ and $\bar\zeta$; the entries commute with the coordinate operators.

**Theorem.** Under `SHyp`, there is normal-form data $d = (L, \kappa, (S_l))$ with $L$ extending $L_0$, $L$ a star level, `d.Rel`, and $Q(Y) = Q_d(Y)$ for all $Y$.

## Proof

The proof applies `NFx2.thmSOfSteps` to six facts on types (`Mx3.tyInterlaces`, `tyComplete`, `rhoUp`, `nrmFacts`, `realPoints`, `wExact`) and to four steps.

1. **Block form** (`NFx2.sb_main`). Let $\ell(Y) \in A$ be the element built from $L_0$, $Q$ and $\kappa$ (`lA`, not unfolded), and put $\pi_\rho = \kappa(\delta_\rho)$. There are $b_\rho \in A$ and shifts $S_l$ such that, for regular $Y$, the block $\pi_{\rho'} \ell(Y) \pi_\rho$ is $(b_\rho - Y \bar\zeta G^{-1}) \pi_\rho$ on the diagonal, plus $(Y + r_l(\rho) + 1)^{-1} G^{-1} S_l \pi_\rho$ for each $l$ with $\rho'$ one step above $\rho$ in direction $l$ (`M.Up`). Each $S_l$ raises the type under $\kappa$ and commutes with the operators of $L_0$.
2. **Connection** (`NFx2.sc_main`). There is $L$ extending $L_0$ with $\nabla = -\sum_\rho \pi_\rho b_\rho \pi_\rho - \tfrac12 \bar\zeta G^{-1}$ and $\nabla^* = (\nabla)^*$. It is a star level, the relations `RelCore` hold, and the entries $(1,0)$, $(0,1)$, $(1,1)$ of $Q$ and $Q_d$ agree.
3. **Norm** (`NFx2.sn_main`). $S_l^* S_l = \kappa(N_l)$ for $1 \le l \le k - 1$, and the entries $(0,0)$ agree.
4. `NFx2.relIsCoreNorm`: `d.Rel` is `RelCore` and `RelNorm` together. This is a regrouping of conjuncts.

The four entries then give $Q = Q_d$.

## In the Lean code

The theorem is in [ConnectionRaisingConstantEq.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ConnectionRaisingConstantEq.lean#L2592). The statement and the steps are in [StatementNF.lean](lean:Formalism/HermitianCurvature/StatementNF.lean#L322).

Odd points:

- `NFx2.sb_main` ([line 844](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ConnectionRaisingConstantEq.lean#L844)) ignores its three inputs `TyInterlaces`, `TyComplete`, `RhoUp`. `NFx2.sn_main` ([line 1387](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ConnectionRaisingConstantEq.lean#L1387)) ignores the same three. `NFx2.sc_main` ignores `P.OK`.
- `P.theorem_S_of_steps` is declared twice in the same namespace: at [line 2590](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ConnectionRaisingConstantEq.lean#L2590) and in [InterpolationInverseMatrixSumIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/InterpolationInverseMatrixSumIdentity.lean#L858). `QNFAsm.lean` imports both files. Lean does not accept an import of two files that declare the same name, so this needs a check.
