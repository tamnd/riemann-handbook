---
id: gen-transfer-of-rot-k
title: The gauge transfer from rotation invariance
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.genTransfer_of_rotK
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreDone
covers: 1041
status: drafted
drafted_by: writer@claude
---
This theorem proves `GenTransfer` from one hypothesis, `GTRRotK`. Two theorems use it: `gCore_of_rotK`, which gives the gauge construction `GCore`, and `modelPlaceBuilt2_of_rotK`, which feeds [the smooth transfer at the built place](/entry/model-place-built-holds/) through [the chain below it](/entry/model-place-built2-of-poly-s/). So its parent is the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/). The proof only assembles four lemmas, and the hypothesis is proved as `rotation_K_invariance_holds`.

## Statement

Use the radial space $\mathcal{R}$ of [the compact form of Theorem P](/entry/actual-compact-theorem/), with $T = T_z T_{z'}$. A frame $e$ is a family $e_\rho(\zeta)$ of operators $W_q \to W_p$, indexed by $\rho$ in a finite set of tuples (`M.Ty`), with `IsFrameB`: it is smooth on $\{|\zeta|^2 > T\}$, and for each such $\zeta$ it is an orthonormal basis, for the Hilbert-Schmidt inner product, of a fibre `NF.Fib` at $\zeta$. The transfer `trR` sends $\Phi \in \mathcal{R}$ to the functions $(c, \zeta) \mapsto (|\zeta|^2 - T)^{(k-1)/2} \langle e_\rho(\zeta), \Phi(c, \mu(\zeta)) \rangle$, where $\mu(\zeta)$ is the group element (`muZ`) given by the section `μsec` of the place datum.

**Theorem.** Assume `GTRRotK`. Let the place satisfy `IsPlace`, $k \ge 2$, and let $\mu$ satisfy `CSec` (it is a section, and its stabilizer `NF.Stab` does not depend on $\zeta$ for $|\zeta|^2 > T$). Let $X$ be actual operators and $d$ normal-form data whose level data $L$ satisfy `IsActualLevel`, `IsStarLevel` and the relations `d.Rel`, with $X$ and $d$ having the same matrix `QQ`. Then there is a frame $e$ such that `trR` intertwines:

- $\zeta, \zeta^{-1}, \bar\zeta, \bar\zeta^{-1}$, $G$ and $G^{-1}$ of $L$ with multiplication by the same functions, where $G = |\zeta|^2 - T$;
- each $\kappa(f)$ with the diagonal operator $f(\rho)$;
- $\nabla$ and $\nabla^*$ of $L$ with $\partial_\zeta + a_\rho \bar\zeta / G$ and $-\partial_{\bar\zeta} + a_\rho \zeta / G$ on the $\rho$ component, $a_\rho$ being the real number `aC`;
- the shifts $S_l$ and $S_l^*$, $1 \le l \le k - 1$, with the model shifts `MA.SS`, which move $\rho$ by one in slot $l$ with the weight $\sqrt{N_l(\rho)}$.

We have not unfolded `NF.Fib`, `NF.Stab`, `IsActualLevel` or `d.Rel`.

## Proof

`genTransfer_of_cut` builds the frame in three stages and checks four properties.

1. `gauge_kappa_holds` gives a frame that intertwines each $\kappa(f)$.
2. `gTConn_of_rotK h` changes it to a frame that also intertwines $\nabla$ and $\nabla^*$.
3. `second_shift_gauge_holds` changes it again to intertwine the shifts too.
4. `GT.gauge_function_holds` shows that every family $e$ intertwines the six multiplication operators.

The hypothesis enters only in stage 2. `gTConn_of_leaves` gets curvature and holonomy facts from `gTCRef_of_rotK`, which needs `GTCRefTrace`, proved by `gTCRefTrace_of_rotK` from `GTRRotK` and seven proved lemmas. `GTCRefTrace` gives a reference connection $A_0$ and, for each $\rho$, an integer $n$ with $\mathrm{Re}(\zeta(\alpha_\rho - A_{0,\rho})) = n/2$ on an annulus, where $\alpha_\rho = a_\rho \bar\zeta / G$ (`modA`). The rest is bookkeeping.

## In the Lean code

The theorem is at [CutGCoreDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreDone.lean#L34). `GenTransfer` is in [CutGCoreCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreCut.lean#L46), and `genTransfer_of_cut` is in [CutGCoreGenTransferCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGenTransferCut.lean#L76).

`GTRRotK` is in [CutGCoreGTRRotCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTRRotCut.lean#L30). For the section `TheSec.theSection` and a frame constant in $\zeta$ with `IsFrameB` and the $\kappa$ property, take an operator $R$ on $\mathcal{R}$ that commutes with each $\kappa(f)$ and acts on `DomR` as $\sum_a E_{aa} + s$ with $s \in \mathbb{Z}$. Then for each $\rho$ there is $m \in \mathbb{Z}$ with $\mathrm{trR}(R\Phi)_\rho = (\zeta \partial_\zeta - \bar\zeta \partial_{\bar\zeta} + m)\, \mathrm{trR}(\Phi)_\rho$. It is proved in [CutGCoreGTRRotK.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTRRotK.lean#L10).

`GTRRotK` covers only the section `theSection`, but `GenTransfer` allows any section with `CSec`. The proof of `gTCRefTrace_of_cutK` ([line 143](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTRRotCut.lean#L143)) works at `theSection`, and `radial_gauge_move` (`GTRMove`) moves a frame for one section to a frame for another with the same transfer.
