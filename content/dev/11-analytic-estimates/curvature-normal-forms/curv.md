---
id: curv
title: The curvature of the normal form
kind: theorem
decl: Formalism.FourierDecayAlt.P.NFx4.SX.curv
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.NormalFormOrderZeroOfParts
covers: 452
status: drafted
drafted_by: writer@claude
---
This theorem computes the commutator $\nabla^* \nabla - \nabla \nabla^*$ for any normal-form data whose matrix $Q$ satisfies the RTT relation. It is relation 1 of [the extra relations of the normal form](/entry/shift-extra/). The proof reads one entry of the RTT relation on each block $\kappa(\delta_\rho)$, and gets the value of a scalar from [the model computation](/entry/model-scalar/).

## Statement

Use the notation of [the extra relations](/entry/shift-extra/): a ring $A$ with involution and $\mathbb{C}$-algebra structure, normal-form data $d$ in $A$, the matrix $Q(Y) = (Q_{ab}(Y))_{a, b \in \{0, 1\}}$ (`d.QQ`), and the function $q$ (`M.qC`).

**Theorem.** Suppose that $d$ satisfies `Hyp` (the four relations kept by `hyp_of_rel`), that $P$ satisfies `P.OK`, that $Q$ satisfies the start condition for $q$, and that $S_m S_m^* = \kappa(N^{\downarrow}_m)$ for $1 \le m \le k - 1$. Then

$$\nabla^* \nabla - \nabla \nabla^* = \kappa\bigl(\rho \mapsto 2 a_\rho T\bigr)\, G^{-1} G^{-1},$$

where $T = T T'$ and $a_\rho$ is the real number `M.aC P ρ`.

## Proof

Let $P_\rho = \kappa(\delta_\rho)$. By `ext_right`, it is enough to prove the identity after right multiplication by each $P_\rho$.

1. **One RTT entry.** From the start condition, `rtt_ent` gives $(u - v)[Q_{01}(u), Q_{10}(v)] = Q_{11}(u) Q_{00}(v) - Q_{11}(v) Q_{00}(u)$ for all $u, v \in \mathbb{C}$. This has the form of the defining relations of the Yangian $Y(\mathfrak{gl}_2)$ (A. Molev, *Yangians and Classical Lie Algebras*, AMS 2007, Section 1.1).
2. **The block.** `diag_id` multiplies this by $P_\rho$ on both sides. With the formula for $Q$ and `op_identity`, it gets
$$(u - v)\, x_\rho(u)\, x_\rho(v) \bigl( G^2 (\nabla^* \nabla - \nabla \nabla^*) + (1 + u + v)(\zeta \bar\zeta - G) \bigr) P_\rho = C_\rho(u, v)\, P_\rho,$$
where $x_\rho(Y) = \prod_{i=1}^{k-1} (Y + r_i(\rho))$ and $C_\rho(u, v)$ is the explicit scalar `Cf`. This step uses $S_m S_m^* = \kappa(N^{\downarrow}_m)$.
3. **The scalar.** [`model_scalar`](/entry/model-scalar/) gives $C_\rho(u, v) = (u - v)\, x_\rho(u)\, x_\rho(v) \bigl(2 a_\rho T + (1 + u + v) T\bigr)$.
4. **Two pairs of points.** For $\operatorname{Im} Y \ne 0$, $x_\rho(Y) \ne 0$, since each $r_i(\rho)$ is real. Take $(u, v) = (i, 2i)$ and $(2i, 3i)$ and cancel the nonzero factor. In the level data, $\zeta \bar\zeta - G$ is a scalar $T_L$ (`d.L.TT`). The difference of the two identities gives $T_L P_\rho = T P_\rho$. Then the first one gives $G^2 (\nabla^* \nabla - \nabla \nabla^*) P_\rho = 2 a_\rho T\, P_\rho$.
5. Multiply on the left by $G^{-1} G^{-1}$, which commutes with $\kappa$.

## In the Lean code

The theorem is at [NormalFormOrderZeroOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2865). It calls:

- `rtt_ent` ([line 1982](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L1982)), which reads `rtt_relation_entries` off the RTT field of the start condition;
- `diag_id` ([line 2743](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/NormalFormOrderZeroOfParts.lean#L2743)), with `blk_12_21'`, `blk_21_12'`, `rhs_diag` and `op_identity`;
- `model_scalar`, `ext_right`, `kap_Pj` and `kc_GGi`.

The hypothesis `P.OK` is used only by `model_scalar`. Only the RTT field of the start condition is used; the Hermitian and determinant fields are not. The proof also shows that the scalar $T_L$ of the level data agrees with $T T'$ on each block, a fact that the hypotheses do not state directly.
