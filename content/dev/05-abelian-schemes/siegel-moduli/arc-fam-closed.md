---
id: arc-fam-closed
title: Arcs with theta frames exist, with no hypothesis
kind: theorem
decl: GlobalTheory.arcFam_closed
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsArcFamilyPointWithFramesProof
covers: 929
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `ArcFamSt` by applying [`exists_arc_family_point_with_frames_of_laws`](/entry/exists-arc-family-point-with-frames-of-laws/) to seven proven inputs. [Part I from semistable reduction](/entry/part-i-of-semistable-reduction/) passes it to [`partI_of_semistableReduction_of_arcFam`](/entry/part-i-of-semistable-reduction-of-arc-fam/). Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

**Theorem.** `ArcFamSt` holds.

`ArcFamSt` says: for each PEL moduli space $X$ with a model $Y$, each arc datum $a$ (`ArcIn`) over a field or complete discrete valuation ring $O'$ of characteristic $0$, and each odd $m$ that is a unit in $O'$, there are a finite injective map $O'[[X]] \to R_1$ to an integrally closed domain and a point $y_1$ of $X$ over the fraction field of $R_1$. The point lies over the base of $a$, satisfies `TraitData`, and has theta frames of levels $1$ and $m^2$ (`IsFrame`). The entry [`arcFam`](/entry/arc-fam/) gives the full statement.

## Proof

The proof is one application of `exists_arc_family_point_with_frames_of_laws` to:

- `lawsAndExpansions` (`HV`);
- the sixth part of `allSixLaws` (`Laws6`);
- `uniformisation_triples_complete_DVR_torsion` (`UDvrSt`);
- `homExtension_semiAbelian_discreteValuationRing` (`HomExtSt`);
- the two parts of `thetaPoint_determines_and_end_determined_torsion` (`ThetaPtDeterminesSt`, `EndDeterminedOnTorsionSt`);
- `thetaUnifAV_closed` (`ThetaUnifAV`).

The real content is in [`arcFam`](/entry/arc-fam/).

## In the Lean code

The theorem is in [ExistsArcFamilyPointWithFramesProof.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsArcFamilyPointWithFramesProof.lean#L21). It only passes proven lemmas along. `ArcFamSt` is in [ArcFamSt.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/ArcFamSt.lean#L17), and `TraitData`, `IsFrame` and `ArcBase` are in [AdmissiblePadicIntMaximalIdeal.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/AdmissiblePadicIntMaximalIdeal.lean#L56). We have not unfolded `HV`, `Laws6`, `UDvrSt` or `HasArcData`.
