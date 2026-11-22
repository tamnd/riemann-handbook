---
id: carrier-p
title: The carrier bound for spectral ties
kind: theorem
decl: GlobalTheory.CarrierGap.carrierP
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.OffK0Closed
covers: 4919
status: drafted
drafted_by: writer@claude
---
This theorem proves the carrier bound `CarrierP` with no hypothesis. Its only user is [`offDiag`](/entry/carrier-gap-off-diag/), which passes it to [`theoremS_leaves_of_carrierG`](/entry/theorem-s-leaves-of-carrier-g/) as one of the 19 hypotheses of Theorem S. The proof assembles proved inputs. Most of its subtree is below [`carrierNeedsFromD`](/entry/carrier-needs-from-d/) and [`lemma_model`](/entry/lemma-model/).

## Statement

`CarrierP` says: there are $C_4 \ge 1$ and $C_{A,0}$ such that, for each $C_A \ge \max(C_{A,0}, 1)$ and constants $C_0 \ge 1$, $C_G \ge 0$, $C_\Delta > 4$, $c_T > 0$, $C_b > 0$ with $c_T C_b > 1$, there is $k_0$ with the following property. For all further constants (with $c_b, c_{Tf} > 0$) there are thresholds $C'_0$ and $C_{l,0}$ such that, for $C' \ge C'_0$ and $C_l \ge C_{l,0}$, the carrier condition `CarrierFull` holds with the constants $C_4$ and $C_A$ for each datum $D$, size data $L$, spectral ties $T$ and words $u \neq u'$, under these hypotheses: $D$ has ties, $k_0 \le k$ for the global size datum, the standing hypothesis `Hyp0`, the identification $e$ of the infinite places agrees with the setting of $T$, the size hypothesis `J.SzHyp`, $i_0 = i'_0$, a point representation exists (`PtRepExists`), and the pin condition `NuQPin`. `CarrierFull` asks for local spaces $W_p, W_q$ at each infinite place, a Hida setting, level towers and more. We have not unfolded it to the end.

## Proof

1. [`carrierNeedsFromD`](/entry/carrier-needs-from-d/) gives three inputs: the compact form of Theorem P (`ThmPActualCpt`), the model places (`ModelPlaceBuilt2`) and the built bounds (`BuiltBounds2Cpt`).
2. `liftAt3_exists` gives a constant $C_b$ with the lift property `LiftAt3`.
3. `kFinDense_holds` gives `KFinNZ`. With `uniqGap_holds`, `xPinsP_ofG` gives the pins `XPinsP`, and `xLeavesP_of_pinsPG` gives the leaves `XLeavesP`. `carrierXSideP_of_leaves` turns them into the side bound `CarrierSideBoundPositive` for $C_b$.
4. `carrierP_of_compact_model` takes these, with [`lemma_model`](/entry/lemma-model/), and gives `CarrierP`.

## In the Lean code

The theorem is at [OffK0Closed.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean#L665). `CarrierP` is in [TheoremSClosedP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSClosedP.lean#L20) and `carrierP_of_compact_model` in [CarrierInputExistsCompact.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/CarrierInputExistsCompact.lean#L27).

The lemmas: `carrierNeedsFromD`, `liftAt3_exists`, `lemma_model`, `xPinsP_ofG`, `xLeavesP_of_pinsPG`, `carrierXSideP_of_leaves`, `carrierP_of_compact_model`.

The proof is a near copy of `carrierP_of_kfin4` in [CarrierXPinsP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/CarrierXPinsP.lean#L318). That theorem takes `CSTarget4`, which is the statement of `carrierNeedsFromD`, and the uniqueness `BesselMapUniq` as hypotheses. Here the versions with the suffix "G" use the gap form `UniqGap` instead, which `uniqGap_holds` proves. A third copy, `carrierP_of_kFinite` (line 309), uses the non-compact inputs.
