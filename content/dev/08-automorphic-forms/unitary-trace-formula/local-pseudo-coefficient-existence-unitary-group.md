---
id: local-pseudo-coefficient-existence-unitary-group
title: Existence of pseudo-coefficients for U(p, q), restated
kind: theorem
decl: GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LocalPseudoCoefficientExistenceUnitaryGroupStatement
covers: 1295
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`localPC_holds`](/entry/local-pc-holds/), and that entry has the real content. It gives the statement $\mathrm{LocalPC}$ to the [comparison of cuspidal multiplicities](/entry/unitary-theory-of-harish-chandra-langlands-alt/), as the first of the nine inputs of `multEq_of_sides`. Below this theorem are 1,295 declarations; all but one are below `localPC_holds`.

## Statement

**Theorem.** $\mathrm{LocalPC}$ holds.

$\mathrm{LocalPC}$ says: let $r$ be odd, let $G = U(p,q)$ be the [[unitary group|0R9R0Y1HDK]] of $\operatorname{diag}(\pm 1)$ in $\mathrm{GL}_r(\mathbb{C})$, and let $\mu$ be a Haar measure on $G$. Let $D$ be a [[discrete series|9AB7HYGPEK]] representation of $G$ with Harish-Chandra parameter $\lambda \in \mathbb{Z}^r$, where $\lambda_a - \lambda_{a+1} \geq 100\, r^4$ for each $a$. Then $D$ has a pseudo-coefficient $f$: a smooth, compactly supported, bi-$K$-finite function with $\operatorname{tr} D(f) = 1$, with $\operatorname{tr} \pi(f) = 0$ for each other irreducible unitary $\pi$, with orbital integrals $0$ at non-elliptic regular semisimple elements, and with orbital integrals at elliptic regular elements given by the conjugate of the character of $D$. The [entry for `localPC_holds`](/entry/local-pc-holds/) states each condition in full.

## Proof

The proof is the term `localPC_holds`. The rest is bookkeeping.

## In the Lean code

The theorem is in [LocalPseudoCoefficientExistenceUnitaryGroupStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalPseudoCoefficientExistenceUnitaryGroupStatement.lean#L7). The statement $\mathrm{LocalPC}$ is in [RangeShape.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RangeShape.lean#L36).

The proof is the tactic `first | exact @localPC_holds | exact localPC_holds | (intros; apply localPC_holds <;> assumption)`. The two types are the same, so the first branch suffices. The declaration adds nothing to `localPC_holds` except the name in the namespace `T`.
