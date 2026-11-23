---
id: second-shift-phase-holds
title: Constant phases put the shifts in model form
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.SSPh.second_shift_phase_holds
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreGTSSPhase
covers: 554
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTSSPhase`, step 4 of [the shift frame in four steps](/entry/g-tss-of-adj-rad-t/). There the shifts $S_l$ act in the frame by constant matrices. It multiplies each frame vector by a constant of modulus one, so that $S_l$ acts by the model shift. The real input is [the extra relations of the normal form](/entry/shift-extra/).

## Statement

A type $\rho$ is a tuple $(\rho_1, \dots, \rho_{k-1})$ of integers with $0 \le \rho_i \le m_i$ (`M.Ty P`). Put $r_i(\rho) = \ell_i + \rho_i$ (`M.rho`) with $\ell_i$ real, and let $e_l$ be the $l$-th unit tuple. For $1 \le l \le k - 1$, $N_l(\rho)$ is the real number `M.Nrm P l ρ`, equal to $-q_0(-r_l(\rho) - 1)$ divided by $\prod_{j \ne l} (r_j(\rho) - r_l(\rho))(r_j(\rho) - r_l(\rho) - 1)$, where $q_0$ is a polynomial fixed by $P$ (`I.qpoly`). The model shift `MA.SS` acts on families $(F_\tau)$ by $(S_l^{\mathrm{mod}} F)_\tau = \sqrt{N_l(\tau - e_l)}\, F_{\tau - e_l}$, and by $0$ when $\tau - e_l$ is not a type.

**Theorem.** Let $P, X, d$ satisfy `GTHyp`. Let $e$ be a frame that intertwines each $\kappa(f)$, $\nabla$ and $\nabla^*$ with the model operators ([the gauge transfer](/entry/gen-transfer-of-rot-k/)). Let $s_l, t_l$ be complex matrices indexed by types such that, under the transfer `trR` of $e$, $S_l$ acts by $s_l$ and $S_l^*$ by $t_l$, and suppose $t_l(\rho, \rho') = \overline{s_l(\rho', \rho)}$. Then there is a frame $e'$ with the same three properties for which $S_l$ and $S_l^*$ act by $S_l^{\mathrm{mod}}$ and its adjoint, for all $1 \le l \le k - 1$.

## Proof

By `SSTr.exists_tr`, for each $\rho$ there is $U_\rho \in \mathcal{R}$ whose transfer is the constant family $\delta_\rho$. Each step applies an operator identity to $U_\rho$.

1. **Support.** The relations `d.Rel` give $\kappa(g) S_l = S_l \kappa(f)$ when $g(\rho + e_l) = f(\rho)$. Hence $s_l(\tau, \rho) = 0$ unless $\tau = \rho + e_l$.
2. **Norm.** `d.Rel` also gives $S_l^* S_l = \kappa(N_l)$. With $t_l = s_l^*$, this gives $|s_l(\rho + e_l, \rho)|^2 = N_l(\rho)$.
3. **Squares.** `actual_start` and $X.\mathrm{QQ} = d.\mathrm{QQ}$ give the start condition for $d$. Then [`shift_extra`](/entry/shift-extra/) gives, for $j \ne l$, $S_j S_l \kappa(r_j - r_l - 1) = S_l S_j \kappa(r_j - r_l + 1)$. With step 1, this relates the two paths from $\rho$ to $\rho + e_l + e_j$.
4. **Phases.** $N_l(\rho) > 0$ when $\rho + e_l$ is a type (`nrmFacts_statement`). Put $w_l(\rho) = s_l(\rho + e_l, \rho) / \sqrt{N_l(\rho)}$, so $|w_l(\rho)| = 1$. The numbers $\sqrt{N_l}$ satisfy the relation of step 3 (`Mx4.corner`), and $|r_j(\rho) - r_l(\rho)| \ge 2$ (`Mx4.gap`), so $r_j - r_l - 1 \ne 0$. Dividing gives the cocycle condition $w_j(\rho + e_l)\, w_l(\rho) = w_l(\rho + e_j)\, w_j(\rho)$.
5. **Trivialization.** `phase_exists` gives, by induction on $\rho_1 + \dots + \rho_{k-1}$, a $u$ with $|u(\rho)| = 1$ and $u(\rho + e_l) = w_l(\rho) u(\rho)$.
6. **New frame.** Put $e'_\rho = u(\rho) e_\rho$. By `trR_phase`, this multiplies the $\rho$ component of the transfer by $\overline{u(\rho)}$. A constant phase keeps the frame property and the $\kappa$ property (`isFrameB_phase`, `kapF_phase`), and the $\nabla$ property because the model $\nabla$ is diagonal. The new coefficient of $S_l$ is $\overline{u(\rho + e_l)}\, s_l(\rho + e_l, \rho)\, u(\rho) = \sqrt{N_l(\rho)}$.

## In the Lean code

The theorem is at [CutGCoreGTSSPhase.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSPhase.lean#L64). It calls `SSTr.exists_tr` ([CutGCoreGTSSTr.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSTr.lean#L67)), `shift_extra`, `actual_start`, and:

- `Mx4.corner` and `Mx4.gap` in [EulerZetaGammaInvIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/EulerZetaGammaInvIdentity.lean#L584);
- `phase_exists` in [CutGCoreGTSSPhaseA.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSPhaseA.lean#L56);
- `trR_phase`, `isFrameB_phase`, `kapF_phase` in [CutGCoreGTConnGaugeA.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTConnGaugeA.lean#L119).

Two parts of `GTHyp` are unused: the section condition `CSec` and `IsActualLevel`.
