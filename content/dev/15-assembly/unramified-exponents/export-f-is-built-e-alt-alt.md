---
id: export-f-is-built-e-alt-alt
title: The export condition on built points, from a twisted norm choice
kind: theorem
decl: GlobalTheory.ExportFirst.exportF_isBuiltE_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SExport
covers: 2213
status: drafted
drafted_by: writer@claude
---
This theorem proves the export condition `ExportF` on the slot of built points for any parameters $p$, once each point has a twisted norm choice. It turns the global statement into one local statement `ExportAt` at each point, and gets that from [series-realization-of-published-alt](/entry/series-realization-of-published-alt/). Its only user is [export-f-prm-r-alt-alt](/entry/export-f-prm-r-alt-alt/).

## Statement

Assume 27 named hypotheses. We have not unfolded them. By their names they are:

- Galois cohomology: `Cheb`, `PoitouTateTotallyComplex`, `CohDimTwo`, `TameLocal`, `LocalFiniteness`, `LocalTateDuality`, `LocalEulerChar`, `GlobalFiniteness`, `GlobalEulerChar`, `UnramifiedOrthogonality`, `ArchimedeanSignatureMatching`, `GreenbergWiles`;
- class field theory and cusp forms: `RayCharacterArtin`, `CuspRapidDecay`, `ChebotarevDegreeOne`, `GlobalArtinReciprocity`, `ToricDenominator`;
- theta series and Hecke lattices: `SeriesRat`, `SerInt`, `HeckeInt`, `HeckeTransform`, `HeckeReadTie`;
- Galois representations: `AutomorphicFormsFiniteGL`, `CuspUAlt`, `DeRhamPotSemistable`, `CarUAlt`;
- `Conclusion5 D` for each datum $D$.

Let $h_L$ prove [RecTExists](/step/rect-exists-def/) and let $p$ be parameters for $h_L$. Assume $H$: for all large contexts, at each base $B$ with frame $f$ where `KPx B f` holds and the twist datum $T$ is untwisted, each point with a witness of $p.N$, a witness of $p.R$ and `ColPin` has a `TwistNormChoice`.

**Then** `ExportF KPx (IsBuiltE p.s)`: for all large contexts, at each such $B$, $f$, $T$, each core $c$ in the slot `IsBuiltE p.s` satisfies `ExportAt` $(D, c.\mathrm{nch}, c.\mathrm{xd})$, where $D$ is the datum assembled from the stage.

A `TwistNormChoice` is a `TwistedRealJoin` ([TwJoin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TwJoin.lean#L46)): a real side $X$, a series side $Y$ over $X$, a Galois side $G$ (`GalSideAlt`), the field conditions `FieldOk X`, a witness `cg`, and the base tuple condition at each twisted place when $T$ is untwisted.

## Proof

The quantifier "for all large contexts" is kept with `imp`. Fix a core $c$ in the slot. The slot is `positionOf (BuiltE p.s)`, so $c$ comes from a column point $(w, Z, c')$ with a record $b$ of type `Built`. The second part of `BuiltE` (the condition `EntC` on $b$) is dropped. A `suffices` with `rfl` replaces $c$ by $c'$. The fields of $b$ give the witnesses that $H$ needs, and $H$ gives a twisted real join $j$. Then `series_realization_of_published_alt` gives `ExportAt`. Its inputs are the 22 first hypotheses, $j.X$, $j.Y$, $j.\mathrm{gal}$, $j.\mathrm{field}$, the condition `GalHodgeN` from `ghOf'_alt`, `Conclusion5`, the tie `c'.nch_tie` and $j.\mathrm{base}$. `ghOf'_alt` uses $h_L$, the four Galois hypotheses, $j.\mathrm{cg}$ and the label $j.\mathrm{gal}.\mathrm{lab}$.

## In the Lean code

The theorem is at [SExport.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SExport.lean#L20). Its type is the abbreviation `exportF_isBuiltE_tyz` in [ExportFIsBuiltETyz.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportFIsBuiltETyz.lean#L17). It calls:

- `GlobalTheory.T.series_realization_of_published_alt`;
- `UpperTheory.GalS.ghOf'_alt`, at [SHodgeDghOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SHodgeDghOf.lean#L42).

`ExportF` is at [NotBaseCondFalse.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotBaseCondFalse.lean#L55), `IsBuiltE` and `BuiltE` at [ThetaChr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ThetaChr.lean#L85). We have not unfolded `Built`.

The pattern `⟨b, -⟩` discards `EntC b.ker`. So the proof never uses the "E" of `IsBuiltE`. It uses only the record $b$, which the larger slot `IsBuilt` also gives. We have not checked in Lean that the statement for `IsBuilt` compiles with the same proof.
