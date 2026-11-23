---
id: unitary-integral-compactification-exists-via-theta
title: An integral compactification from theta constants (statement form)
kind: theorem
decl: GlobalTheory.T.unitary_integral_compactification_exists_via_theta
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryIntegralCompactificationExistsViaThetaStatement
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`umin_theta_compactification_exists`](/entry/umin-theta-compactification-exists/), which has the real content. Its one user is [`uMinSt_holds`](/entry/u-min-st-holds/), which is also a renaming.

## Statement

**Theorem** (`UMinSt`). For each CM field $E$ with `Host E`, each hermitian datum of signature $(p, q)$ with $p + q \geq 1$, each level $l$, moduli scheme $X^\circ$ and coefficient field $F$, there is an integral compactification of $X^\circ_F$ in the sense of `UCompact`.

The fields of `UCompact` are in [the entry with the proof](/entry/umin-theta-compactification-exists/).

## Proof

The statement is the same as that of `GlobalTheory.umin_theta_compactification_exists`, and the proof applies it.

## In the Lean code

The theorem is in [UnitaryIntegralCompactificationExistsViaThetaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryIntegralCompactificationExistsViaThetaStatement.lean#L12). The proof is `first | exact @GlobalTheory.umin_theta_compactification_exists | ...`, a tactic that tries the alias in three forms.
