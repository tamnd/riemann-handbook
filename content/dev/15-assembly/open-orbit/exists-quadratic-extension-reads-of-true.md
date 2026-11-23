---
id: exists-quadratic-extension-reads-of-true
title: Quadratic extension data exist, in statement form
kind: theorem
decl: GlobalTheory.T.exists_quadratic_extension_reads_of_true
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ReadsExistsStatement
covers: 351
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`readsExists_alt`](/entry/reads-exists-alt/). Its only user is [the column side of a geometric family](/entry/col-side-alt/), which takes from it, in step 2 of its proof, one quadratic extension datum $J(t)$ with `J.Reads` for each index $t$. The real content is in `readsExists_alt`.

## Statement

The statement is word for word the statement of [`readsExists_alt`](/entry/reads-exists-alt/). In short: let $W$ be a real package with `AllFamilyConditions W`, $u$ a word and $a$ a geometric family with `a.Is` and `a.True`. Assume that the commuting datum `commOf (pk_z W) u a.g` of the geometry of $a$ is good (`Is`). Then for each $t$ there is a quadratic extension datum $J$ for $a$ and $t$ with `J.Reads`.

## Proof

The proof applies `readsExists_alt`. Nothing else happens.

## In the Lean code

The theorem is at [ReadsExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsExistsStatement.lean#L18). The proof is the tactic `first | exact @GlobalTheory.Fam.readsExists_alt | ...`, so the theorem only passes its hypotheses along. The hypothesis on the commuting datum comes, in [the column side](/entry/col-side-alt/), from `famCh_is_and_tuples_is_of_colOK` in step 1.
