---
id: unitary-integral-compactifications-exist
title: Integral compactifications of unitary moduli schemes exist (statement form)
kind: theorem
decl: GlobalTheory.T.unitary_integral_compactifications_exist
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryIntegralCompactificationsExistStatement
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It proves the statement `UMinSt` by [`uMinSt_holds`](/entry/u-min-st-holds/), which is itself a renaming. The real content is in [the theta compactification](/entry/umin-theta-compactification-exists/). Its one user is [`uPoinStX_sep`](/entry/u-poin-st-x-sep/), whose first step takes from it a normal projective model $Z_o$ over a Dedekind ring $o$, an ample bundle, and the extension properties.

## Statement

**Theorem** (`UMinSt`). Let $E$ be a CM field with the data `Host E`, a hermitian datum of signature $(p, q)$ with $p + q \geq 1$, a level $l$, the moduli scheme $X^\circ$ of `Moduli D l`, and a coefficient field $F$. Then there is an integral compactification of $X^\circ_F$ in the sense of the structure `UCompact`.

The fields of `UCompact` are listed in [the theta compactification](/entry/umin-theta-compactification-exists/).

## Proof

The proof applies `GlobalTheory.UPoinc.uMinSt_holds`.

## In the Lean code

The theorem is in [UnitaryIntegralCompactificationsExistStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryIntegralCompactificationsExistStatement.lean#L13). Its type is `UMinSt`, defined in [ExistsRatPointOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRatPointOfFiniteType.lean#L529). The proof is `first | exact @GlobalTheory.UPoinc.uMinSt_holds | ...`, a tactic that tries the alias in three forms.
