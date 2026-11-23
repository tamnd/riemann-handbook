---
id: log-kodaira-spencer-injective-mod-maximal-ideal
title: The log Kodaira-Spencer map is injective modulo a maximal ideal (statement form)
kind: theorem
decl: GlobalTheory.T.logKodairaSpencer_injective_mod_maximalIdeal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerInjectiveModMaximalIdealStatement
covers: 379
status: drafted
drafted_by: writer@claude
---
This theorem is input 7 of the [log Kodaira-Spencer isomorphism](/entry/has-log-ks/): the Kodaira-Spencer map is injective modulo each maximal ideal. It is the statement form of [`logKS_inj_mod_maximal`](/entry/log-ks-inj-mod-maximal/), which has the proof.

## Statement

Use the setting and the names of [`hasLogKS`](/entry/has-log-ks/): a model $Y$ that is smooth of relative dimension $n_0$, with simple normal crossings boundary and rigid charts at the closed boundary points, and $p + q \geq 1$. Let $U$ be an affine open with ring $R$ and a frame $v_1, \dots, v_n$ on $U$, with matrices $A(a)$ for $a \in \mathcal{O}_E$.

**Theorem.** Let $D \in T_U$ be a log derivation and $\Theta \in M_n(R)$ with $\mathrm{IsKS}(D, \Theta)$. Let $\mathfrak m$ be a maximal ideal of $R$. If every entry of $\Theta$ is in $\mathfrak m$, then $D \in \mathfrak m T_U$.

## Proof

The proof is one line: it applies `GlobalTheory.logKS_inj_mod_maximal`.

## In the Lean code

The theorem is in [LogKodairaSpencerInjectiveModMaximalIdealStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalIdealStatement.lean#L16). Its statement is the same as that of `logKS_inj_mod_maximal`, word for word, and the proof is the tactic `first | exact @GlobalTheory.logKS_inj_mod_maximal | ...`. It is a second name and adds nothing.
