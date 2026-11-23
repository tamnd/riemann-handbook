---
id: siegel-family-exists-unique-classify-scheme
title: A Siegel family classifies principal Siegel objects over every scheme, statement form
kind: theorem
decl: GlobalTheory.T.siegelFamily_existsUnique_classify_scheme
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyExistsUniqueClassifySchemeStatement
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the classification by a Siegel family](/entry/exists-unique-classify/). [The moduli with an action of an order](/entry/act-sieg-exists-rep/) calls it to get, for each principal Siegel object $z$ over $S$, the unique map $f \colon S \to X$ to the base of the family along which the universal object pulls back to $z$.

## Statement

The statement is word for word the statement of `GlobalTheory.SiegFamAll.existsUnique_classify`. Let $g \geq 1$, $n \geq 3$ odd, and $F$ a Siegel family of genus $g$ and level $n$ over $\mathbb{Z}[\zeta_n, 1/n]$, with base $X$ and universal principal object $u$. Then for each scheme $S$ over $\mathbb{Z}[\zeta_n, 1/n]$ and each principal Siegel object $c$ over $S$, there is a unique $f \colon S \to X$ over the base ring such that $c$ is a pullback of $u$ along $f$ (`SiegPB`). The definitions are in the entry for `existsUnique_classify`.

## Proof

The proof is one tactic line: `exact @GlobalTheory.SiegFamAll.existsUnique_classify`. All the content is in [the entry for `existsUnique_classify`](/entry/exists-unique-classify/).

## In the Lean code

The theorem is in [SiegelFamilyExistsUniqueClassifySchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyExistsUniqueClassifySchemeStatement.lean#L11). The proof is `first | exact @existsUnique_classify | ...`, with two fallback tactics. The parent `ActSieg.exists_rep` calls this name, not `existsUnique_classify`.
