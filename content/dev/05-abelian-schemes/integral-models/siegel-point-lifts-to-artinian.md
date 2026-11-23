---
id: siegel-point-lifts-to-artinian
title: Principal Siegel objects over local Artinian rings are classified (statement form)
kind: theorem
decl: GlobalTheory.T.siegel_point_lifts_to_artinian
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelPointLiftsToArtinianStatement
covers: 374
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the classification over local Artinian rings](/entry/siegel-artin-main/), which has the real content. Its one user is [the classification over complete noetherian local rings](/entry/classified-of-complete/), which applies it to the rings $R/\mathfrak{m}^{e+1}$ for each $e$.

## Statement

Use the Siegel objects of genus $g$ and level $n$ over $B_n = \mathbb{Z}[\zeta_n, 1/n] \subset \mathbb{C}$, and the condition "principal", from [the representability of Siegel moduli](/entry/sd-rep-of-coprime/). Use the family $(X, s, u)$ of [the entry with the proof](/entry/siegel-artin-main/).

**Theorem.** Let $g \geq 1$ and let $n \geq 3$ be odd. Let $(X, s, u)$ be such a family of genus $g$ and level $n$. Let $C$ be a local Artinian ring, $\beta \colon B_n \to C$ a ring map, and $c$ a principal Siegel object over $\operatorname{Spec} C$. Then there is a map $f \colon \operatorname{Spec} C \to X$ with $s \circ f = \operatorname{Spec}\beta$ such that $c$ is the pullback of $u$ along $f$.

## Proof

The statement is the same as that of `GlobalTheory.SiegelArtin.main`, and the proof applies it.

## In the Lean code

The theorem is in [SiegelPointLiftsToArtinianStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelPointLiftsToArtinianStatement.lean#L11). The proof is `first | exact @GlobalTheory.SiegelArtin.main | ...`, a tactic that tries the alias in three forms. "Is the pullback of $u$ along $f$" is `SiegPB c F.univ f`, defined in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L50).

The name says that a point lifts. The statement says more: it gives a classifying map for each principal object over $C$, with no point given in advance.
