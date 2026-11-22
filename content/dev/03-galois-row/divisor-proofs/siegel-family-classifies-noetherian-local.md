---
id: siegel-family-classifies-noetherian-local
title: A Siegel family classifies principal objects over noetherian local rings (statement form)
kind: theorem
decl: GlobalTheory.T.siegelFamily_classifies_noetherian_local
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesNoetherianLocalStatement
covers: 408
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the noetherian local classification](/entry/exists-point-of-principal/), which passes to the completion. Its one user is [the noetherian classification](/entry/classify-noetherian/), which applies it at each local ring $R_\mathfrak{p}$.

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian local ring, $\beta \colon B_n \to R$, and $c$ a principal Siegel object over $\operatorname{Spec} R$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

The statement is the same as that of `GlobalTheory.SiegelFamLocal.exists_point_of_principal`, and the proof applies it.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesNoetherianLocalStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherianLocalStatement.lean#L11). The proof is `first | exact @GlobalTheory.SiegelFamLocal.exists_point_of_principal | ...`, a tactic that tries the alias in three forms. It differs from [the noetherian statement](/entry/siegel-family-classifies-noetherian/) only by the extra instance `IsLocalRing R`.
