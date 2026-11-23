---
id: cm-arc-datum-family-functional-bounded-linear-on-cusp-forms
title: Each functional of the CM arc family is linear and bounded on cusp forms (statement form)
kind: theorem
decl: GlobalTheory.T.cmArcDatumFamily_functional_bounded_linear_on_cuspForms
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmArcDatumFamilyFunctionalBoundedLinearOnCuspForStatement
covers: 630
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`numGood_of_famQ`](/entry/num-good-of-fam-q/), which has the real content. Its one user is [`qat_of_kill_detect`](/entry/qat-of-kill-detect/), which needs, for each form outside the kernel $\mathcal{K}$, a functional with the arithmetic bounds `NumGood`.

## Statement

Use $K$, $S_\kappa$, $M_\kappa$, the sup norms $\|F\|_\sigma$, the family `FamQ` and the coefficient functional $\phi_d$ from [the entry for `qat_of_kill_detect`](/entry/qat-of-kill-detect/).

**Theorem.** Assume `Known` and `GamAt T`, and let $j \in [1, m)$. Let $K_1 \supseteq K$ be a number field and $d$ an arc datum over $K_1$ in the family. Then there is a $K$-linear map $\phi \colon S_\kappa \to K_1$ with $\phi(F) = \phi_d(F)$ for all $F$, such that `NumGood` holds for $\phi$ on $M_\kappa$ with the sup norms, the finite defect $\beta = $ `beOf E n A` and the constants $C_{\mathrm{arch}} = $ `CarchAt` and $B_{\deg} = $ `BdegAt`.

[The entry for `numGood_of_famQ`](/entry/num-good-of-fam-q/) defines `NumGood`.

## Proof

The statement is the same as that of `GlobalTheory.ArcCM.numGood_of_famQ`, and the proof applies it.

## In the Lean code

The theorem is in [CmArcDatumFamilyFunctionalBoundedLinearOnCuspForStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFamilyFunctionalBoundedLinearOnCuspForStatement.lean#L9). The proof is `first | exact @GlobalTheory.ArcCM.numGood_of_famQ | ...`, a tactic that tries the alias in three forms. The word "bounded" in the name stands for `NumGood`, which bounds the functional at the finite and at the infinite places. The hypothesis $j < m$ is not used by `numGood_of_famQ`.
