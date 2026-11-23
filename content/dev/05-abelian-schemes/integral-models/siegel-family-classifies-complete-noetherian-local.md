---
id: siegel-family-classifies-complete-noetherian-local
title: A Siegel family classifies principal objects over complete noetherian local rings (statement form)
kind: theorem
decl: GlobalTheory.T.siegelFamily_classifies_complete_noetherian_local
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesCompleteNoetherianLocalStatement
covers: 402
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the classification over complete local rings](/entry/classified-of-complete/), which has the real content. Its one user is [the noetherian local classification](/entry/exists-point-of-principal/), which applies it to the completion of a noetherian local ring.

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian local ring with maximal ideal $\mathfrak{m}$, complete for the $\mathfrak{m}$-adic topology. Let $\beta \colon B_n \to R$ and let $c$ be a principal Siegel object over $\operatorname{Spec} R$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

The statement is the same as that of `GlobalTheory.SFamCompl.classified_of_complete`, and the proof applies it.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesCompleteNoetherianLocalStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocalStatement.lean#L11). The proof is `first | exact @GlobalTheory.SFamCompl.classified_of_complete | ...`, a tactic that tries the alias in three forms. Completeness is the Mathlib predicate `IsAdicComplete (IsLocalRing.maximalIdeal R) R`, which includes that $R$ is $\mathfrak{m}$-adically separated.
