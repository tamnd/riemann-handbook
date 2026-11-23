---
id: s-fino-and-second-no-of-s-finl-prime
title: Spectral finiteness and second nonvanishing, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.sFino_and_secondNo_of_sFinl'
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FiniteLevelAndSecond
covers: 572
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [`sFino_and_secondNo_of_rat_cusp_finl`](/entry/s-fino-and-second-no-of-rat-cusp-finl/), in the same file, and it proves it by calling that theorem. The real content is in [`secondNo_of_sMt_sRat_sCusp_sFinl`](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/). Its only user is [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/), step 4, which needs both halves of the conclusion at the constant $c_{\mathrm{Dep}}$.

## Statement

Assume `DiscreteSeriesCover`, `CasselmanWallach`, `HarishChandraModules`, `PublishedInputsThirdLayerAlt`, `SerN`, `DatExt`, `WeightCaseCondition`, `DiscreteSeriesExists` and `PhtCmp`. Let $h_L$ be an element of `RecTExists`, and assume the stage statements `SMt`, `RationalityStatementThirdPlaceSeries hL` and `CuspStatement' hL`. Let $c \in \mathbb R$ and assume `FinitenessListStatement hL c`. Then `SpectralFiniteness hL c` and `SecondNonvanishing hL c` hold. The entries [`sFino_and_secondNo_of_rat_cusp_finl`](/entry/s-fino-and-second-no-of-rat-cusp-finl/) and [`secondNo_of_sMt_sRat_sCusp_sFinl`](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/) say what these mean.

## Proof

The proof is the other theorem. The rest is bookkeeping.

## In the Lean code

The theorem is at [FiniteLevelAndSecond.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FiniteLevelAndSecond.lean#L125). Its statement is the text of `GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl` (line 116). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with that theorem in each branch.

The caller passes the same term `by first | exact hA.a5 | exact hA.a7` for `CasselmanWallach` and for `HarishChandraModules`; the tactic picks the field by its type. The name ends in `sFinl'`, for the hypothesis `FinitenessListStatement`; the other hypotheses are not in the name.
