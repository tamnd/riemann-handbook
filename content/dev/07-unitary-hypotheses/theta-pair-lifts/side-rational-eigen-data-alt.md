---
id: side-rational-eigen-data-alt
title: A Hecke specification exists (second name)
kind: theorem
decl: GlobalTheory.T.side_rational_eigen_data_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.NdSpecExistsStatement
covers: 325
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ndSpec_exists_alt`](/entry/nd-spec-exists-alt/). It has the same statement, and its proof applies that theorem. The real content is in that entry. Its one caller is [`locAll_exists_alt`](/entry/loc-all-exists-alt/), where it gives the first fields of the localization data.

## Statement

The statement is that of [`ndSpec_exists_alt`](/entry/nd-spec-exists-alt/). In short: let $D$ be a datum of type `D7` with the data $A$, $M$, $C$ and `tp` of [`locAll_exists_alt`](/entry/loc-all-exists-alt/). Assume global Artin reciprocity, `HeckeStdPlain`, and the hypotheses 1 to 7 of that entry (all but `BlocksUnique`). Then for each map `big` that gives a finite set of complex numbers at each place, there are a Hecke localization $X$, twist data $T$ over $X$, and a datum of type `NdSpec A.pl M C big X T`.

## Proof

The proof is one tactic line (namespaces shortened):

```
first | exact @ndSpec_exists_alt | exact ndSpec_exists_alt | (intros; apply ndSpec_exists_alt <;> assumption)
```

The two statements are the same text, character for character, so the first branch suffices.

## In the Lean code

The theorem is in [NdSpecExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NdSpecExistsStatement.lean#L11). It is a pure renaming. The name speaks of "rational eigen data", but the conclusion is the existence of a Hecke specification `NdSpec`. The caller gives `HeckeStdPlain` from the proved theorem `heckeStdPlain`, so that hypothesis is discharged one level up.
