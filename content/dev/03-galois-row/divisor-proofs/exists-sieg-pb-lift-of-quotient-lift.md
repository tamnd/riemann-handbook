---
id: exists-sieg-pb-lift-of-quotient-lift
title: A classifying map lifts over a small extension (statement form)
kind: theorem
decl: GlobalTheory.T.exists_siegPB_lift_of_quotient_lift
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ClassifiedOfSmallStatement
covers: 320
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the lift over a small extension](/entry/classified-of-small/), which has the real content. Its one user is [the classification over local Artinian rings](/entry/siegel-artin-main/), which applies it in the step of an induction on length.

## Statement

Use the Siegel objects over $B_n = \mathbb{Z}[\zeta_n, 1/n]$, "principal", "is the pullback of", and the family $(X, s, u)$ from [the classification over local Artinian rings](/entry/siegel-artin-main/).

**Theorem.** Let $g \geq 1$, $n \geq 3$ odd, and $(X, s, u)$ a family of genus $g$ and level $n$. Let $C$ be a local Artinian ring with maximal ideal $\mathfrak{m}$, and let $e \in \mathfrak{m}$ with $\mathfrak{m} e = 0$. Write $\pi \colon C \to C/(e)$. Let $\beta \colon B_n \to C$ be a ring map and $c$ a principal Siegel object over $\operatorname{Spec} C$. Suppose that each object $c_0$ over $\operatorname{Spec} C/(e)$ that is the pullback of $c$ along $\operatorname{Spec}\pi$ is the pullback of $u$ along some map $\operatorname{Spec} C/(e) \to X$ over $\pi \circ \beta$. Then $c$ is the pullback of $u$ along some $f \colon \operatorname{Spec} C \to X$ with $s \circ f = \operatorname{Spec}\beta$.

## Proof

The statement is the same as that of `GlobalTheory.SmallClassify.classified_of_small`, and the proof applies it.

## In the Lean code

The theorem is in [ClassifiedOfSmallStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassifiedOfSmallStatement.lean#L11). The proof is `first | exact @GlobalTheory.SmallClassify.classified_of_small | ...`, a tactic that tries the alias in three forms. The module name refers to the name of the alias, not to this theorem.
