---
id: quasi-affine-equivalence-intersection-number-base-change
title: The restriction lemma for QA rings, second name
kind: theorem
decl: UpperTheory.Et.QuasiAffineEquivalence.intersectionNumber_baseChange
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleAxioms.EquivalenceQuasiAffine
covers: 344
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [a33](/entry/a33/). Its only user is [the affine proper base change](/entry/affine-proper-base-change/), which passes it on as the lemma `EqvQA`. The content is in [a33](/entry/a33/).

## Statement

A ring is *QA* if it is a quotient of an absolutely integrally closed domain.

**Theorem.** Assume the axioms A1, A9, B1 and B2. Let $S$ be a QA ring and $J$ an ideal of $S$ that lies in the Jacobson radical and such that idempotents lift from $S/J$ to $S$. Let $q \neq 0$ be a unit in $S$. Then restriction $H^n(\operatorname{Spec} S, \mathbb{Z}/q(i)) \to H^n(\operatorname{Spec} S/J, \mathbb{Z}/q(i))$ is bijective for all $n$ and $i$.

## Proof

The proof is the term `a33`. There is nothing else.

## In the Lean code

The theorem is at [EquivalenceQuasiAffine.lean line 74](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleAxioms/EquivalenceQuasiAffine.lean#L74). Its statement is `LateralTheory.E.t_E1Cut.EqvQA`.

- The name is misleading. The statement has no intersection number and no base change.
- The namespace `QuasiAffineEquivalence` is also misleading: QA means a quotient of an absolutely integrally closed domain, not quasi-affine.
- Four sibling lemmas, in other files, have the same short name `intersectionNumber_baseChange`. Each supplies one more input of [the affine proper base change](/entry/affine-proper-base-change/).
