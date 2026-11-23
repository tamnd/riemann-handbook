---
id: u-min-st-holds
title: The statement UMinSt holds
kind: theorem
decl: GlobalTheory.UPoinc.uMinSt_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryIntegralCompactificationsExist
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It is the second of three names for the same statement. It proves `UMinSt` by [`unitary_integral_compactification_exists_via_theta`](/entry/unitary-integral-compactification-exists-via-theta/), a statement form of [the theta compactification](/entry/umin-theta-compactification-exists/), which has the real content. Its one user is [the statement form](/entry/unitary-integral-compactifications-exist/) that [`uPoinStX_sep`](/entry/u-poin-st-x-sep/) cites.

## Statement

**Theorem** (`UMinSt`). For each CM field $E$ with `Host E`, each hermitian datum of signature $(p, q)$ with $p + q \geq 1$, each level $l$, moduli scheme $X^\circ$ and coefficient field $F$, there is a `UCompact` for $X^\circ_F$: a normal projective model $Z$ of $X^\circ_F$ over a Dedekind ring $o$ with fraction field $F$, with an ample bundle and the properties listed in [the theta compactification](/entry/umin-theta-compactification-exists/).

## Proof

The proof is the term `GlobalTheory.T.unitary_integral_compactification_exists_via_theta`.

## In the Lean code

The theorem is in [UnitaryIntegralCompactificationsExist.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryIntegralCompactificationsExist.lean#L16). The file has no other declaration. The chain is `unitary_integral_compactifications_exist`, then `uMinSt_holds`, then `unitary_integral_compactification_exists_via_theta`, then `umin_theta_compactification_exists`: four names for one statement.
