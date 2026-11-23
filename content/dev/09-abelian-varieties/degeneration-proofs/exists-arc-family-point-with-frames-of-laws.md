---
id: exists-arc-family-point-with-frames-of-laws
title: Arc points with theta frames, from seven inputs (statement form)
kind: theorem
decl: GlobalTheory.T.exists_arc_family_point_with_frames_of_laws
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsArcFamilyPointWithFramesOfLawsStatement
covers: 927
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`Ex.arcFam`](/entry/arc-fam/), with the same type. Its only caller is [`arcFam_closed`](/entry/arc-fam-closed/), which supplies the seven inputs from proven theorems and so proves `ArcFamSt` with no hypothesis.

## Statement

**Theorem.** The seven inputs `HV`, `Laws6`, `UDvrSt`, `HomExtSt`, `ThetaPtDeterminesSt`, `EndDeterminedOnTorsionSt` and `ThetaUnifAV` imply `ArcFamSt`.

In short, `ArcFamSt` says: for a PEL moduli space with a model $Y$ over a valuation ring, and for degeneration data $a$ over a ring $O'$ that is a field or a complete discrete valuation ring, there is a point of the moduli space over the fraction field of a finite normal extension $R_1$ of $O'[[X]]$. The point degenerates as $a$ prescribes, and it has a theta frame of level 1 and one of level $m^2$ for each odd $m$ invertible in $O'$. The entry [`arcFam`](/entry/arc-fam/) states `ArcFamSt` and the inputs in full.

## Proof

The proof is the tactic `first | exact @GlobalTheory.Ex.arcFam | ...`. The two types agree, so the first branch closes the goal.

## In the Lean code

The theorem is in [ExistsArcFamilyPointWithFramesOfLawsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcFamilyPointWithFramesOfLawsStatement.lean#L12). It is a renaming, with no content of its own. The real proof is in [`arcFam`](/entry/arc-fam/), and the main construction is in [`ArcPoint.exists_point`](/entry/exists-point/).
