---
id: exists-integral-key-invariant-rule-char-zero
title: The key invariant exists in characteristic zero, second name
kind: theorem
decl: GlobalTheory.T.exists_integralKeyInvariantRule_charZero
module: Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.ExistsIntegralKeyInvariantRuleCharZeroStatement
covers: 838
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`KaExists.kaSt`](/entry/ka-st/). It has no proof of its own. Its only caller is [the key rule for half characteristics](/entry/exists-key-rule-char-half/), which passes the result to `T.thetaKeyRule_exists_of_algebraic_invariants`.

## Statement

Assume four statements: the bundle `Out.Laws` of 24 facts about abelian schemes, the analytic uniformisation `ThetaUnifAV` of complex abelian varieties, the statement `TorusAlgebraic` that each torus $\mathbb{C}^g/(\mathbb{Z}^g + \tau\mathbb{Z}^g)$ comes from a principally polarized abelian variety whose theta section is the theta function of a half-integral characteristic, and the descent statement `KeyDesc`. Then `KaSt` holds: for each $g \geq 1$ and each prime $p$ there are integers $c, M \geq 1$ with $p \nmid M$ and a key invariant of weight $4c$ in dimension $g$, integral where $M$ is a unit. The [entry for `kaSt`](/entry/ka-st/) states `KaSt` in full.

## Proof

The proof is `exact @GlobalTheory.KaExists.kaSt`, inside a `first` combinator with two fallbacks that are never reached.

## In the Lean code

The theorem is at [ExistsIntegralKeyInvariantRuleCharZeroStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsIntegralKeyInvariantRuleCharZeroStatement.lean#L21). The type is word for word the type of `kaSt`. The real content is in [`kaSt`](/entry/ka-st/). The name says "integral key invariant rule" and "char zero", but the statement is `KaSt`; the names `KaRule` and `KaSt` in [KaRuleK.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KaRuleK.lean#L36) are the ones to search for.
