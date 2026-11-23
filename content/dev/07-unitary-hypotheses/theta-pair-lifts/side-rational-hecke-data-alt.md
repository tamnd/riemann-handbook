---
id: side-rational-hecke-data-alt
title: Localization data exist (second name)
kind: theorem
decl: GlobalTheory.T.side_rational_hecke_data_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LocAllExistsStatement
covers: 454
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`locAll_exists_alt`](/entry/loc-all-exists-alt/). It has the same statement, and its proof applies that theorem. The real content is in that entry and in [`ndSpec_exists_alt`](/entry/nd-spec-exists-alt/). Its one caller is [the automorphic side at a stage](/entry/built-ex-of-published-inputs-prime/).

## Statement

The statement is that of [`locAll_exists_alt`](/entry/loc-all-exists-alt/). In short: let $D$ be a datum of type `D7` with the data $A$, $M$, $C$ and `tp` as there. Assume global Artin reciprocity, `ChoiceSide`, `MtInput`, the stability of $\mathrm{LL}_0$ under `star`, the integrality of the exponents `eExp`, the splitting of the places over `pde` and `pde'`, `ChebSplit`, the values of the twist characters, the condition on `OtoLL`, and `BlocksUnique D`. Then for each map `big` there are localization data $L$ and a Hecke specification `Sp` for $L$, with an automorphic specialization and with semisimple residual representations.

The conclusion is `AutomorphicSideExists A M C tp.tup` with its definition unfolded.

## Proof

The proof is one tactic line (namespaces shortened):

```
first | exact @locAll_exists_alt | exact locAll_exists_alt | (intros; apply locAll_exists_alt <;> assumption)
```

The two statements are the same text, character for character, so the first branch suffices.

## In the Lean code

The theorem is in [LocAllExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocAllExistsStatement.lean#L11). It is a pure renaming. The name speaks of "rational Hecke data", but the conclusion is about localization data and automorphic specializations. The older pair `locAll_exists` and `side_rational_hecke_data` has the same form.
