---
id: degeneration-constant-of-log-kodaira-spencer-mem
title: Constant degeneration data along a derivation with vanishing Kodaira-Spencer matrix (statement)
kind: theorem
decl: GlobalTheory.T.degeneration_constant_of_logKodairaSpencer_mem
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DegenerationConstantOfLogKodairaSpencerMemStatement
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`ChartConst.isConstAlong_of_ks_mem`](/entry/is-const-along-of-ks-mem/), which has the proof. Its one user is [`ChartDer.logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/), in step 4: there it turns $\Theta \equiv 0 \bmod \mathfrak m$ into constant degeneration data, to which the rigidity of the chart then applies.

## Statement

Use the names of [`logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/): the model $Y$, the affine open $U$ with ring $R$ and a frame, $D \in T_U$, the matrix $\Theta$ with $\mathrm{IsKS}(D, \Theta)$, and the chart ring $R_k = k[[t, u]]$.

**Theorem.** Let $Y$ satisfy the hypotheses of [`hasLogKS`](/entry/has-log-ks/), except that no rigid charts are assumed. Let $\mathfrak m \subset R$ be a maximal ideal with $\Theta_{ab} \in \mathfrak m$, and let $x \in U$ be a boundary point at which $\mathfrak m$ vanishes. Let $\xi \colon \operatorname{Spec} R_k \to Y$ send the closed point to a point $x'$ over $x$, with all the conditions of a rigid chart except `IsRigid`: the semi-abelian scheme over $R_k$ with its map to $G$, the data $P$, the forms $\gamma_i$, `IsMonomial` and `IsPartOfBasis`. Suppose that $\operatorname{Spec} R_k$ maps into $U$. Let $D_R$ be a derivation of $R_k$ that is compatible with $D$ under $R \to R_k$, with $D_R(t_i) = a_i t_i$. Let $\rho(r) = r(0) + \varepsilon \, (D_R r)(0)$. Then there is a rational $c_0 \neq 0$ such that `IsConstAlong` holds for $\rho$ with rates $c_0 a_i(0)$.

## Proof

The statement is the same as that of `GlobalTheory.ChartConst.isConstAlong_of_ks_mem`, and the proof applies it.

## In the Lean code

The theorem is in [DegenerationConstantOfLogKodairaSpencerMemStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationConstantOfLogKodairaSpencerMemStatement.lean#L20). The proof is `first | exact @GlobalTheory.ChartConst.isConstAlong_of_ks_mem | ...`. The type is copied word for word from the theorem it calls. The file imports `Mathlib` twice.
