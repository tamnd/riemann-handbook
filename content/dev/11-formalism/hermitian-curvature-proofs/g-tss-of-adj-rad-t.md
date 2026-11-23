---
id: g-tss-of-adj-rad-t
title: The shift frame in four steps
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj_radT
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.cut_GCore_GTSS
covers: 569
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTSS`, the existence of [a frame for the shift operators](/entry/second-shift-gauge-holds/), from two hypotheses: the pointwise adjoint relation `GTSSAdjPt` and the local form `GTCLRadT` of the actual operators. Its user [`gTSS_of_adj`](/entry/g-tss-of-adj/) proves the second one. The proof assembles four lemmas with `gTSS_of_cut`. Most of the work is in the fourth, [the phase change](/entry/second-shift-phase-holds/).

## Statement

`GTSS` is stated in [the entry for `second_shift_gauge_holds`](/entry/second-shift-gauge-holds/), and `GTSSAdjPt` and `GTCLRadT` in [the entry for `gTSS_of_adj`](/entry/g-tss-of-adj/).

**Theorem.** `GTSSAdjPt` and `GTCLRadT` imply `GTSS`.

## Proof

Fix the data, and a frame $e$ that intertwines each $\kappa(f)$, $\nabla$ and $\nabla^*$ with the model operators. Let $A$ be the annulus $|\zeta|^2 > T$.

1. **Local form.** `gTSSLocal_of_radT` proves `GTSSLocal` from `GTCLRadT`: there are smooth functions $s_l(\rho', \rho)$ and $t_l(\rho', \rho)$ on $A$ such that, under the transfer, $S_l$ acts by $F \mapsto \bigl(\sum_\rho s_l(\rho', \rho) F_\rho\bigr)_{\rho'}$ and $S_l^*$ by the same formula with $t_l$.
2. **Constant coefficients.** `second_shift_constant` proves `GTSSConst`: since $e$ also intertwines $\nabla$ and $\nabla^*$, each $s_l(\rho', \rho)$ and $t_l(\rho', \rho)$ is constant on $A$.
3. **Adjoint.** The hypothesis `GTSSAdjPt` gives $t_l(\rho, \rho') = \overline{s_l(\rho', \rho)}$ on $A$. The proof uses it only at the point $\zeta_0 = |T| + 1$ of $A$. This is enough because both sides are constant.
4. **Phase.** `SSPh.second_shift_phase_holds` proves `GTSSPhase`: from constant matrices $s_l$, $t_l = s_l^*$ as above, it multiplies each $e_\rho$ by a constant of modulus one and gets a frame in which $S_l$ acts as the model shift.

The rest is bookkeeping: `gTSS_of_cut` uses `fnZ_congr` to replace the functions $s_l$, $t_l$ by their constant values.

## In the Lean code

The theorem is at [cut_GCore_GTSS.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/cut_GCore_GTSS.lean#L9). Its proof is

```
gTSS_of_cut (gTSSLocal_of_radT hR) hA SSC.second_shift_constant SSPh.second_shift_phase_holds
```

- `gTSS_of_cut` and the four statements `GTSSLocal`, `GTSSAdjPt`, `GTSSConst`, `GTSSPhase`: [CutGCoreGTSSCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSCut.lean#L89).
- `gTSSLocal_of_radT`: [CutGCoreGTSSLocal.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSLocal.lean#L7). It calls `second_shift_slice_derivative`, `second_shift_slice_operator` and `second_shift_matrix_form`, which we have not opened.
- `second_shift_constant`: [CutGCoreGTSSConst.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSConst.lean#L180). We have read only its first lines.
- `second_shift_phase_holds`: [CutGCoreGTSSPhase.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSPhase.lean#L64).

`GTSSPhase` asks for no smoothness of $s_l$ and $t_l$, since they are constants there.
