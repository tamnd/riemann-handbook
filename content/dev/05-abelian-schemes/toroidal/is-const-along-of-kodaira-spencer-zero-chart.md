---
id: is-const-along-of-kodaira-spencer-zero-chart
title: On a boundary chart, a vanishing Kodaira-Spencer matrix gives constant degeneration data (statement)
kind: theorem
decl: GlobalTheory.T.isConstAlong_of_kodairaSpencer_zero_chart
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsConstAlongOfKodairaSpencerZeroChartStatement
covers: 307
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`KSConst.isConstAlong_of_ks_zero`](/entry/is-const-along-of-ks-zero/), which has the proof. Its one user is [`ChartConst.isConstAlong_of_ks_mem`](/entry/is-const-along-of-ks-mem/), which pulls the Kodaira-Spencer relation from the model $Y$ back to a chart and then applies this theorem on the chart.

## Statement

The setting is one chart, with no model. Let $k$ be a field of characteristic $0$ and $R_k = k[[t_1, \dots, t_m, u_1, \dots, u_d]]$. Let $G$ be a semi-abelian scheme over $R_k$ with PEL structure (`SAB`), with degeneration data $P$ at the maximal ideal (`PELUnif`). Let $\gamma_1, \dots, \gamma_m$ be linearly independent bilinear forms on the character group of $P$ with `IsMonomial`. Suppose that $G$ is abelian exactly where $t_1 \cdots t_m$ is a unit. Let $v_1, \dots, v_n$ be a frame of the tangent vectors of $G$ along the zero section over $R_k$.

**Theorem.** Let $D$ be a derivation of $R_k$ with $D(t_i) = q_i t_i$. Let $\Theta$ satisfy $\mathrm{IsKS}(D, \Theta)$ for $G$, with interior the open set $t_1 \cdots t_m \neq 0$. Suppose that each $\Theta_{ab}$ is in the maximal ideal. Let $\rho(r) = r(0) + \varepsilon \, (D r)(0)$. Then there is a rational $c \neq 0$ such that `IsConstAlong` holds for $\rho$ with rates $c \, q_i(0)$.

`IsConstAlong` is spelled out in [`logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/): along $\rho$ the data agree with their reduction, except that each period $\tau(y, z)$ changes by the factor $1 + \varepsilon \sum_i a_i \gamma_i(y, z)$, here with $a_i = c \, q_i(0)$.

## Proof

The statement is the same as that of `GlobalTheory.KSConst.isConstAlong_of_ks_zero`, and the proof applies it.

## In the Lean code

The theorem is in [IsConstAlongOfKodairaSpencerZeroChartStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsConstAlongOfKodairaSpencerZeroChartStatement.lean#L16). The proof is `first | exact @GlobalTheory.KSConst.isConstAlong_of_ks_zero | ...`. The type is copied word for word from the theorem it calls.
