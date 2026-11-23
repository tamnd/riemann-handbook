---
id: is-const-along-of-ks-mem
title: Moving the Kodaira-Spencer relation from the model to a boundary chart
kind: theorem
decl: GlobalTheory.ChartConst.isConstAlong_of_ks_mem
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DegenerationConstantOfLogKodairaSpencerMem
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem proves [the statement form](/entry/degeneration-constant-of-log-kodaira-spencer-mem/), which is step 4 of [`logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/). It pulls the Kodaira-Spencer relation on the model $Y$ back to the chart $\operatorname{Spec} R_k$ at a boundary point. On the chart, [`isConstAlong_of_kodairaSpencer_zero_chart`](/entry/is-const-along-of-kodaira-spencer-zero-chart/) does the work.

## Statement

The statement is that of [the statement form](/entry/degeneration-constant-of-log-kodaira-spencer-mem/): from $\mathrm{IsKS}(D, \Theta)$ on $U$ with $\Theta \equiv 0 \bmod \mathfrak m$, and a chart $\xi \colon \operatorname{Spec} R_k \to Y$ at a boundary point over the point of $\mathfrak m$, it gives a rational $c_0 \neq 0$ such that `IsConstAlong` holds for $\rho(r) = r(0) + \varepsilon \, (D_R r)(0)$ with rates $c_0 a_i(0)$.

## Proof

1. `LocReg.charZero_of_chart`: $k$ has characteristic $0$.
2. `LocReg.comp_genι_eq_spMap_chartHom`: the map $\operatorname{Spec} R_k \to Y$ is $\operatorname{Spec}$ of a ring map $\chi \colon R \to R_k$, followed by $U \subset Y$.
3. `LocReg.BasisPull.exists_basis_pull`: the frame $v_1, \dots, v_n$ on $U$ pulls back, through the map of semi-abelian schemes, to a frame $v^R_1, \dots, v^R_n$ over $R_k$.
4. `ChartAbLocus.mem_abLocus_iff`: the semi-abelian scheme over $R_k$ is abelian exactly where $t_1 \cdots t_m$ is a unit. So the open set $t_1 \cdots t_m \neq 0$ maps into the interior $X^\circ_F$.
5. `T.cechKodairaSpencer_pullback_semiAbelianMap`: the Kodaira-Spencer relation pulls back along a map of semi-abelian schemes. So $\mathrm{IsKS}(D_R, \chi(\Theta))$ holds on $\operatorname{Spec} R_k$, with the frame $v^R$ and the interior $t_1 \cdots t_m \neq 0$.
6. `valR_mem_maximalIdeal`: each $\Theta_{ab}$ is in $\mathfrak m$, so it vanishes at $x$, the image of the closed point. So $\chi(\Theta_{ab})$ is in the maximal ideal of $R_k$.
7. [`T.isConstAlong_of_kodairaSpencer_zero_chart`](/entry/is-const-along-of-kodaira-spencer-zero-chart/) gives the conclusion. It also takes the linear independence of the $\gamma_i$, which follows from `IsPartOfBasis`.

The rest is bookkeeping: `exists_derivation_top` moves $D_R$ to the ring of global sections of $\operatorname{Spec} R_k$, and the maps $\Gamma(\operatorname{Spec} R_k) \cong R_k$ are cancelled.

## In the Lean code

The theorem is in [DegenerationConstantOfLogKodairaSpencerMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationConstantOfLogKodairaSpencerMem.lean#L62). The helpers `exists_derivation_top` and `valR_mem_maximalIdeal` are at [L32](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationConstantOfLogKodairaSpencerMem.lean#L32) and [L46](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationConstantOfLogKodairaSpencerMem.lean#L46). We read the statements of the lemmas in steps 1 to 5, not their proofs.

Many hypotheses are introduced and never used: $p + q \geq 1$, smoothness, the normal crossings condition, the action matrices $A(a)$ and their hypothesis, the maximality of $\mathfrak m$, the fact that $x$ is on the boundary, `IsEtaleCompletion`, and the pullback of the boundary ideal. The proof only needs the map $\xi$, the map of semi-abelian schemes, the boundary condition on points, `IsMonomial`, `IsPartOfBasis`, and the vanishing of $\Theta$ at $x$. So the result holds for any such map, not only an étale completion. `charZero_of_chart` takes no hypothesis but the map $\xi$ to the base change of $Y$ to $F$.
