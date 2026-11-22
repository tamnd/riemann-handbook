---
id: siegel-family-classifies-noetherian
title: A Siegel family classifies principal objects over noetherian rings (statement form)
kind: theorem
decl: GlobalTheory.T.siegelFamily_classifies_noetherian
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesNoetherianStatement
covers: 447
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the noetherian classification](/entry/classify-noetherian/), which has the real content. Its one user is [the classification over affine schemes](/entry/exists-classify-affine/), which reduces an arbitrary ring to a noetherian subring and then applies this statement.

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, principal objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian ring, $\beta \colon B_n \to R$ a ring map, and $c$ a principal Siegel object over $\operatorname{Spec} R$ with structure map $\operatorname{Spec} \beta$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

The statement is the same as that of `GlobalTheory.SiegelNoeth.classify_noetherian`, and the proof applies it.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesNoetherianStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesNoetherianStatement.lean#L11). The proof is `first | exact @GlobalTheory.SiegelNoeth.classify_noetherian | ...`, a tactic that tries the alias in three forms. The base map is given as a ring map $\beta$, not as a map of schemes; over an affine base the two are the same. The conclusion has existence only, not uniqueness.
