---
id: model-scalar
title: The block scalar, computed in the model
kind: theorem
decl: Formalism.FourierDecayAlt.P.NFx4.SX.model_scalar
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.NormalFormOrderZeroOfParts
covers: 402
status: drafted
drafted_by: writer@claude
---
This theorem gives a closed form for the scalar $C_\rho(u, v)$ (`Cf`) that appears in step 2 of [the curvature of the normal form](/entry/curv/). The scalar depends only on $P$, $\rho$, $u$, $v$. The proof does not expand it. It applies the same block identity `diag_id` to the model data, where the curvature is already known, and compares.

## Statement

Use the types $\rho$, the numbers $r_i(\rho)$, $N_m(\rho)$, $N^{\downarrow}_m(\rho)$ and $a_\rho$ of [the extra relations](/entry/shift-extra/), and $T = T T'$. Put $x_\rho(Y) = \prod_{i=1}^{k-1} (Y + r_i(\rho))$, and let $x^{(m)}_\rho(Y)$ be the same product without the factor $i = m$. Let $w_\rho(Y)$ be the value at $Y$ of the polynomial quotient `M.wC`, whose definition we have not expanded here. Then

$$C_\rho(u, v) = x_\rho(u) w_\rho(v) - x_\rho(v) w_\rho(u) - (u - v) \Bigl( \sum_{m} x^{(m)}_\rho(u)\, x^{(m)}_\rho(v)\, N_m(\rho) - \sum_{m} c_m(\rho; v, u)\, N^{\downarrow}_m(\rho) \Bigr),$$

with $m$ from $1$ to $k - 1$, and $c_m(\rho; v, u) = x^{(m)}_\tau(v)\, x^{(m)}_\tau(u)$ if $\rho = \tau + e_m$ for a type $\tau$, and $0$ otherwise.

**Theorem.** If $P$ satisfies `P.OK`, then for every type $\rho$ and all $u, v \in \mathbb{C}$,

$$C_\rho(u, v) = (u - v)\, x_\rho(u)\, x_\rho(v) \bigl( 2 a_\rho T + (1 + u + v) T \bigr).$$

## Proof

The model algebra `M.A P` is the algebra of matrices indexed by types, with entries in the algebra `M.Pr P.r`, which we have not unfolded. `level_exists_model` gives model level data $L$. Let $d_M = (L, \kappa_M, S^{\mathrm{mod}})$ (`dM`), with $\kappa_M$ the diagonal map and $S^{\mathrm{mod}}_l$ the model shift.

1. $d_M$ satisfies `Hyp` (`model_hyp`).
2. Its matrix $Q$ is the model matrix `M.QQr` (`model_is_normal_form`), so the RTT entry holds (`transfer_rtt_entries`), and $S_m S_m^* = \kappa_M(N^{\downarrow}_m)$ (`shift_norm_relation`).
3. So `diag_id` applies, and gives $(u - v) x_\rho(u) x_\rho(v) \bigl(G^2 (\nabla^* \nabla - \nabla \nabla^*) + (1 + u + v)(\zeta \bar\zeta - G)\bigr) P_\rho = C_\rho(u, v) P_\rho$.
4. In the model, $\zeta \bar\zeta - G = T$, and `m_curvature_proof` gives $\nabla^* \nabla - \nabla \nabla^* = \kappa_M(2 a_\rho T)\, G^{-2}$. Since $G$ commutes with $\kappa_M$, the bracket in step 3 is $\kappa_M(2 a_\rho T) + (1 + u + v) T$.
5. So $(\text{right side} - C_\rho(u, v))\, P_\rho = 0$. The projection $P_\rho$ is not zero (`model_Pj_ne`, from `model_nontrivial`), so the scalar is zero.

## In the Lean code

The theorem is at [NormalFormOrderZeroOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2796). `Cf` is at [line 2549](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2549), and `dM`, `model_hyp`, `model_Pj_ne` are just above the theorem. It calls:

- `level_exists_model` in [LevelNablaStarRelations.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/LevelNablaStarRelations.lean#L545);
- `model_is_normal_form` in [ModelLevelMultiplier.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ModelLevelMultiplier.lean#L23);
- `transfer_rtt_entries` in [TransferRtt.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TransferRtt.lean#L1854);
- `shift_norm_relation` and `m_curvature_proof` in [EulerZetaGammaInvIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/EulerZetaGammaInvIdentity.lean#L832);
- `diag_id` at [line 2743](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2743).

The statement is an identity between explicit functions of $u$ and $v$. The Lean proof gets it by a detour through the model operators, not by algebra on the polynomials.
