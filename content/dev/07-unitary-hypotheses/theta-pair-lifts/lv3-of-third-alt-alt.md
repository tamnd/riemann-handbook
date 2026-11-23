---
id: lv3-of-third-alt-alt
title: A level 3 record at one stage
kind: theorem
decl: GlobalTheory.HeightCounting.Fin3.lv3_of_third_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FinitenessOfHyp
covers: 608
status: drafted
drafted_by: writer@claude
---
At one stage $x$ with a `StrictHenselianAcyclicLevel` datum $l$, this theorem builds a record of type `Lv3` whose set `Wt` and norm choice agree with those of $x$. Its caller [`sFin_and_sFinl_of_theta_data_exists`](/entry/s-fin-and-s-finl-of-theta-data-exists/) uses it at every stage to prove `FinitenessStatement` and `FinitenessListStatement`, item 6 of [the stage statements](/entry/all-stages-of-specializations-alt/).

## Statement

Fix $P$ of type `Pre2 K w`, a stage $x$ of $P$ and $l$ as above, with its data $A$, $M$ and norm choice $\chi$. Let $N$ give a type of extra data for each core datum `NormChoiceCore`.

**Theorem.** Assume `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `PublishedInputsThirdLayerAlt`, `ArchimedeanComparison' hL` and `RowsAt P`. Assume also:

1. ($h_E$) if the automorphic side exists for $(A, M, \chi)$, then for large enough coefficient data the localized datum $D'$ is `Large` and its $\eta_j(v)$ equal those of $P$, for $1 \le j \le m$;
2. ($h_X$) there is a theta datum `xd` whose sets `xd0 i j b` are all full for $1 \le j \le m$ (`XdAll`);
3. ($h_N$) each core datum that satisfies `extensionWithLaw` and the list condition `ListPin` for all $c$ with `ListSt c x` has an element of $N$.

Then for each `S : SExt` and `Γ : GeoP` there are $Z$ and a record $v$ of type `Lv3` for the parameters `parametersOfExtension N S Γ`, with $v.\mathrm{Wt} = P.\mathrm{Wt}$ and `Kept χ v.nch`.

`Kept` says that two norm choices agree in their Galois data, twist data, forms and twist fields. Hypothesis 1 is the statement `EtaStatement'` at $(P, x, l)$; see [`sEta_alt_alt_alt`](/entry/s-eta-alt-alt-alt/).

## Proof

1. [`builtEx_of_published_inputs'`](/entry/built-ex-of-published-inputs-prime/) and $h_E$ give localization data $L$ with $D' = $ `withLoc L` large and with the right $\eta_j$.
2. `nonempty_allL_of_archCmp` gives a datum `AllLevelsData l L` from `ArchimedeanComparison'`.
3. From `RowsAt P` and the $\eta_j$, `exists_base_level_rXs_and_yRel` gives a row side $p$, row data $t$ with `RXs t`, and a reading $Y_1$ related to $L$.
4. `exists_core_and_listPin` gives a core $c$ with `extensionWithLaw` and the list condition, and $h_N$ gives an element of $N$ at $c$.
5. The record $v$ is assembled from these parts. Its norm choice is `characterChoiceLocal L l`, and `kept_characterChoiceLocal` gives `Kept`.

## In the Lean code

The theorem is in [FinitenessOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinitenessOfHyp.lean#L61). The structure `Lv3` is in [NonzeroPlacesOverPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L132), and `Kept` is in [StrictHenselianAcyclic.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/StrictHenselianAcyclic.lean#L83).

- The theorem is a near copy of `lv3_of_third` in the older file [FinitenessOfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FinitenessOfHyp.lean#L211), with `PublishedInputsThirdLayerAlt` and `RecTExists` in place of `PrN` and `LocalLanglandsGL`.
- The caller takes $N = $ `extensionWithLaw` and $N = $ `extensionWithList c`, and proves $h_N$ in one line each time.
- We have not unfolded `NormChoiceCore`, `RowsT` or `ThData`.
