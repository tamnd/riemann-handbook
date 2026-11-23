---
id: charpoly-de-rham-homology-abelian-variety-char-p
title: The characteristic polynomial on de Rham homology in characteristic p
kind: theorem
decl: GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charP
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CharpolyDeRhamHomologyAbelianVarietyCharPStatement
covers: 670
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the proof in characteristic p](/entry/charpoly-push/), which has the real content. It gives the characteristic $p$ case of [the characteristic polynomial over an algebraically closed field](/entry/charpoly-push-eq-map-charpoly/).

## Statement

Let $p$ be a prime, $k$ a perfect field of characteristic $p$, $B$ an abelian variety over $k$ of dimension $g$ (the Lean structure `AbVar`), and $f \in \operatorname{End}(B)$. Let $f_*$ be the action of $f$ on $H_1^{\mathrm{dR}}(B)$, the dual of the primitive part of $H^1_{\mathrm{dR}}(B/k)$, and suppose this space has finite dimension. Let $P_f \in \mathbb{Z}[X]$ be the characteristic polynomial of $f$, with $P_f(n) = \deg(n - f)$ for $n \in \mathbb{Z}$.

**Theorem.** $\operatorname{charpoly}(f_* \mid H_1^{\mathrm{dR}}(B))$ is the image of $P_f$ in $k[X]$.

The field need not be algebraically closed.

## Proof

The proof is `exact DeRhamCharpolyP.charpoly_push`. See [the proof in characteristic p](/entry/charpoly-push/).

## In the Lean code

The theorem is in [CharpolyDeRhamHomologyAbelianVarietyCharPStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharPStatement.lean#L10). Its statement is the statement of `GlobalTheory.DeRhamCharpolyP.charpoly_push`, word for word. The proof is a `first` combinator that tries `exact` with and without `@`, then `intros; apply ... <;> assumption`. The file imports `Mathlib` twice.
