---
id: arc-fam
title: Arc points with theta frames of level one and level m squared
kind: theorem
decl: GlobalTheory.Ex.arcFam
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsArcFamilyPointWithFramesOfLaws
covers: 926
status: drafted
drafted_by: writer@claude
---
This theorem proves `ArcFamSt` from seven inputs. It takes a point of the moduli space over a power series ring and enlarges the ring twice to add theta frames. Through its [statement form](/entry/exists-arc-family-point-with-frames-of-laws/) it goes to [`arcFam_closed`](/entry/arc-fam-closed/), and from there to [part I of semistable reduction](/entry/part-i-of-semistable-reduction/), where `ArcFamSt` gives the arcs of the models.

## Statement

**Inputs.** `HV` (the five bundles `Laws` to `Laws5` of facts on abelian schemes, and four statements in the namespace `DVR`); `Laws6` (the statement `UnifUniqSt`); `UDvrSt` (a semi-abelian scheme with $\mathcal{O}_E$ action over a complete discrete valuation ring, polarized on the generic fibre and split over the closed point, has a uniformisation `PELUnif` with `TorsionIso`); `HomExtSt` (homomorphisms of semi-abelian schemes extend uniquely from the generic fibre over a discrete valuation ring); `ThetaPtDeterminesSt` (over an algebraically closed field, theta null values at a large odd level determine a polarized abelian variety with level structure); `EndDeterminedOnTorsionSt` (an endomorphism is fixed by its action on enough torsion); `ThetaUnifAV` (complex uniformisation).

**Conclusion** `ArcFamSt`. Let $E$ be a CM field, $D$ a PEL datum, $l$ a level, $X_o$ the moduli space, $c$ a coefficient datum and $W_0 \subset \mathbb{C}$ a valuation ring. Let $Y$ be a model of $X_o$ over the valuation ring $V = c.V(W_0)$ of the coefficient field, with a semi-abelian scheme $G$ and a line bundle $L$. Let $b \colon V \to O'$, where $O'$ is a field ($\varpi = 1$) or a complete discrete valuation ring with uniformizer $\varpi$ (`ArcBase`). Let $a$ be an arc (`ArcIn`): degeneration data over $O'$ with an $\mathcal{O}_E$ action, a positive definite form, level points and the signature of $D$. Let $m$ be odd and invertible in $O'$. Then there are a domain $R_1$ and a finite injective map $O'[[X]] \to R_1$, with $R_1$ integrally closed, and a point $y_1 \colon \operatorname{Spec} \operatorname{Frac} R_1 \to X_{o,F}$ of the moduli space over the coefficient field, such that:

1. `TraitData`: $y_1$ lies over $b$; at each complete discrete valuation ring $W$ under $R_1$, the point lands in the abelian locus if $X$ is a unit in $W$, and has the arc data $a$ after a finite extension of $W$ if it is not;
2. there is a theta frame of level 1 at $y_1$, a single section $\theta$;
3. there is a theta frame of level $m^2$ at $y_1$.

A frame of level $N$ (`IsFrame`) is a family of sections of $L^N$ at $y_1$ that, at each complete discrete valuation ring $W$ under $R_1$, is a basis of the sections over $W$.

## Proof

1. [`ArcPoint.exists_point`](/entry/exists-point/) gives $R_1$ and $y_1$ over $b$, with `RealAt` and `ThetaInt`.
2. `GoodTrait.range_subset_abLocus` (from `ThetaInt`) and `Trait.hasArcData_at_trait` (from `RealAt`) give the two halves of `TraitData`.
3. `T.exists_single_polarisation_generator_all_traits` gives a finite extension $R_2$ of $R_1$ with a level-1 frame.
4. `Mono.mono` carries `TraitData` and `RealAt` from $R_1$ to $R_2$.
5. `OneBasis.exists_isFrame_pow_sq` gives a finite extension $R_3$ of $R_2$ with a level-$m^2$ frame.
6. `Mono.mono` carries `TraitData` and the level-1 frame from $R_2$ to $R_3$.

The ring $R_3$ and the image of $y_1$ give `ArcFamSt`.

## In the Lean code

The theorem is in [ExistsArcFamilyPointWithFramesOfLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcFamilyPointWithFramesOfLaws.lean#L20). `ArcFamSt` is in [ArcFamSt.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/ArcFamSt.lean#L17), and `IsFrame`, `ArcBase` and `TraitData` are in [AdmissiblePadicIntMaximalIdeal.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/AdmissiblePadicIntMaximalIdeal.lean#L56).

The lemmas are in [AdmissibleBaseOfCompleteDvr.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/AdmissibleBaseOfCompleteDvr.lean#L190) (`hasArcData_at_trait`), [ExistsValuationSubring.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsValuationSubring.lean#L56) (`range_subset_abLocus`), [MemRangeIffOfFinite.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/MemRangeIffOfFinite.lean#L163) (`exists_isFrame_pow_sq`) and [IsFramePull.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/IsFramePull.lean#L49) (`mono`).

All seven inputs are passed unchanged to each of the six lemmas, which are stated for all data at once (`AllA`). We have not unfolded `ArcIn`, `HasArcData`, `Model`, `UnifUniqSt` or the four `DVR` statements in `HV`.
