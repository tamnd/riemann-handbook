---
id: log-ks-inj-mod-boundary
title: Injectivity of the Kodaira-Spencer relation at a boundary point
kind: theorem
decl: GlobalTheory.ChartDer.logKS_inj_mod_boundary
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerInjectiveModMaximalBoundary
covers: 354
status: drafted
drafted_by: writer@claude
---
This theorem proves the boundary case of the injectivity of the log Kodaira-Spencer relation modulo a maximal ideal. The [statement form](/entry/log-kodaira-spencer-injective-mod-maximal-boundary/) restates it for [`logKS_inj_mod_maximal`](/entry/log-ks-inj-mod-maximal/), which feeds input 7 of [`hasLogKS`](/entry/has-log-ks/). The proof moves to a rigid chart at the boundary point.

## Statement

As in the [statement form](/entry/log-kodaira-spencer-injective-mod-maximal-boundary/): if $\mathrm{IsKS}(D, \Theta)$, $\Theta \equiv 0 \bmod \mathfrak m$, and the point $x$ of $\mathfrak m$ is on the boundary, then $D \in \mathfrak m T_U$.

**Rigid charts.** The hypothesis `HasRigidChart` at a closed boundary point $x'$ gives a field $k$, the ring $R_k = k[[t_1, \dots, t_m, u_1, \dots, u_d]]$ (`ChartRing`, with $t_i$ = `bdParam`), and a map $\xi \colon \operatorname{Spec} R_k \to Y$ with these properties:

- $\xi$ sends the closed point to $x'$; the map of local rings is flat, maps the maximal ideal onto the maximal ideal, and is finite on residue fields (`IsEtaleCompletion`);
- the boundary pulls back to the divisor $t_1 \cdots t_m = 0$;
- a semi-abelian scheme over $R_k$ with a map to $G$, degeneration data $P$ for it, and forms $\gamma_1, \dots, \gamma_m$ that are part of a basis;
- `IsMonomial`: for each $y$ in the character group of $P$, the coordinate of $y$ (`PsiCoord`, not unfolded) is a unit times $\prod_i t_i^{n_i}$ with $\gamma_i(y, y) = 2 n_i$;
- `IsRigid`: let $\rho \colon R_k \to k[\varepsilon]$ be a ring map that kills each $t_i$ and whose reduction kills the maximal ideal. Suppose that the data pulled back along $\rho$ and along its reduction agree, except that each period $\tau(y, z)$ changes by the factor $1 + \varepsilon \sum_i a_i \gamma_i(y, z)$ for some $a_i \in k$ (`IsConstAlong`). Then $\rho$ has no $\varepsilon$ part.

## Proof

1. `T.exists_closedBoundaryPoint_maximalIdeal` gives a closed boundary point $x'$ over $x$. Take a rigid chart $\xi$ at $x'$. All of $\operatorname{Spec} R_k$ maps into $U$ (`top_le_preimage_of_closedPoint`).
2. `ChartDer.logDer_extend_chartRing`: $D$ extends to a derivation $D_R$ of $R_k$ with $D_R(t_i) \in (t_i)$. Write $D_R(t_i) = a_i t_i$.
3. Let $\rho(r) = r(0) + \varepsilon \, (D_R r)(0)$. This is a ring map $R_k \to k[\varepsilon]$ (`constEps`), the tangent vector of $D_R$ at the closed point.
4. [`T.degeneration_constant_of_logKodairaSpencer_mem`](/entry/degeneration-constant-of-log-kodaira-spencer-mem/): there is a rational $c_0 \neq 0$ such that the degeneration data are constant along $\rho$ with rates $c_0 a_i(0)$. This is where $\Theta \equiv 0 \bmod \mathfrak m$ enters.
5. $\rho(t_i) = 0$, as $t_i(0) = (a_i t_i)(0) = 0$. So `IsRigid` gives $(D_R r)(0) = 0$ for all $r$.
6. $k$ has characteristic $0$, as $F$ maps into it. `ConstPointCone.dir_eq_zero_of_const`: if the $\gamma_i$ are symmetric and linearly independent, $\rho$ has no $\varepsilon$ part, and `IsConstAlong` holds with rates $b_i$, then all $b_i = 0$. So $c_0 a_i(0) = 0$, and $a_i(0) = 0$.
7. `T.logVectorField_mem_maxIdeal_smul_of_vanishing`: if $D_R$ maps $R_k$ into its maximal ideal and each $a_i(0) = 0$, then $D \in \mathfrak m T_U$.

In coordinates, steps 5 and 6 say that $D_R = \sum_i a_i t_i \partial_{t_i} + \sum_j b_j \partial_{u_j}$ has $a_i(0) = b_j(0) = 0$. This is our reading; we have not opened the proof of step 7.

## In the Lean code

The theorem is in [LogKodairaSpencerInjectiveModMaximalBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalBoundary.lean#L47). `constEps` is at [L29](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalBoundary.lean#L29). `HasRigidChart` and `IsRigid` are in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L59). We read the statements of the lemmas in steps 1, 2, 6 and 7, not their proofs.

`IsRigid` is the main input. It says that a first-order deformation of the chart with constant degeneration data is trivial, which is close to the conclusion. The action matrices $A(a)$ and the hypothesis $p + q \geq 1$ are passed to step 4, whose proof does not use them.
