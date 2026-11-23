---
id: log-kodaira-spencer-injective-mod-maximal-boundary
title: Injectivity of the Kodaira-Spencer relation modulo a boundary maximal ideal (statement)
kind: theorem
decl: GlobalTheory.T.logKodairaSpencer_injective_mod_maximal_boundary
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerInjectiveModMaximalBoundaryStatement
covers: 355
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`ChartDer.logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/), which has the real content. Its one user is [`logKS_inj_mod_maximal`](/entry/log-ks-inj-mod-maximal/), which splits input 7 of [`hasLogKS`](/entry/has-log-ks/) into an interior case and a boundary case. This theorem is the boundary case.

## Statement

**Theorem.** Assume the hypotheses of [`hasLogKS`](/entry/has-log-ks/) on $Y$, and use its names. Let $U$ be an affine open with ring $R$, with a frame $v_1, \dots, v_n$ and action matrices $A(a)$. Let $D \in T_U$, let $\Theta$ be an $n \times n$ matrix over $R$ with $\mathrm{IsKS}(D, \Theta)$, and let $\mathfrak m \subset R$ be a maximal ideal with $\Theta_{ab} \in \mathfrak m$ for all $a, b$. Suppose that there is a point $x \in U \setminus X^\circ_F$ at which each $f \in \mathfrak m$ vanishes. Then $D \in \mathfrak m T_U$.

As $\mathfrak m$ is maximal, $x$ is the closed point of $U$ that $\mathfrak m$ defines. So the extra hypothesis says that this point is on the boundary.

## Proof

The statement is the same as that of `GlobalTheory.ChartDer.logKS_inj_mod_boundary`, and the proof applies it.

## In the Lean code

The theorem is in [LogKodairaSpencerInjectiveModMaximalBoundaryStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalBoundaryStatement.lean#L16). The proof is `first | exact @GlobalTheory.ChartDer.logKS_inj_mod_boundary | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
