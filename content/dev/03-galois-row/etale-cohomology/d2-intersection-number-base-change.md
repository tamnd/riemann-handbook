---
id: d2-intersection-number-base-change
title: The power-sum class axiom, second renaming
kind: theorem
decl: UpperTheory.Et.D2.intersectionNumber_baseChange
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleAxioms.A0
covers: 1786
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [a0](/entry/a0/), which restates [s57](/entry/s57/). Its only user is [the power-sum class theorem](/entry/etale-duality-trace-isomorphism/), which applies it to 22 axiom theorems. The content is in [s57](/entry/s57/).

## Statement

**Theorem.** If the axioms A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5 and D1 of the étale chapter hold, then the axiom D2 holds.

D2 says that vector bundles $V$ have power-sum classes $s_k(V) \in H^{2k}(E, \mathbb{Z}/q(k))$ for $q \neq 0$ and $k > 0$. They are natural, additive on direct sums and equal to $c_1(L)^k$ on a line bundle $L$, when $q$ is invertible. See [the power-sum class theorem](/entry/etale-duality-trace-isomorphism/) for the full statement.

## Proof

The proof is the term `a0`. There is nothing else.

## In the Lean code

The theorem is at [A0.lean line 8](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleAxioms/A0.lean#L8). Its statement is `LateralTheory.E.EtaleChapterDTwo`.

- The name is misleading. The statement has no intersection number and no base change.
- Four declarations have this one statement: `LateralTheory.Fix.EtaleChapterDTwo.s57`, its renaming `LateralTheory.Fix.EtaleChapterDTwo.intersectionNumber_baseChange` at [AwSpec.lean line 127](lean:Development/EtaleCohomology/EtaleSheaves/AwSpec.lean#L127), `a0`, and this theorem.
- Of the 22 hypotheses, only D1 is used in the proof of s57.
