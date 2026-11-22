---
id: see-saw-lattice-frame-pins-finite-integral-laws
title: Finite integral laws from lattice frame pins (restatement)
kind: theorem
decl: GlobalTheory.T.seeSaw_latticeFramePins_finiteIntegralLaws
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawLatticeFramePinsFiniteIntegralLawsStatement
covers: 1356
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the finite integral laws from pinned level data](/entry/pins-finite-integrals/). It adds no mathematics. Its user is [`lawsLinks_of_geo_rows_cols_alt`](/entry/laws-links-of-geo-rows-cols-alt/), which applies it to the data of a geometric family in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in the entry [pins-finite-integrals](/entry/pins-finite-integrals/).

## Statement

Let $D$ be a datum, $c$ a common datum with its conditions (`c.Is`) and with the last step measure condition (`c.VolLast`), and $v$ level data with `v.Is`. Let $k$ be a nonarchimedean local field, $o$ a lattice shape datum over $k$ that fits $v$ off the level places (`ShapeOff v o`), and $G_1, \dots, G_n$ local data that pin the level of $v$ (`GPin G`). Then there are units $\varepsilon$, bilinear operators, reals $r > 0$, integers $e$ and nonzero constants $a_j$ with the following property: $v$ has nonzero volume ratios $\kappa$, the modified level data $v'$ satisfy `Is`, and each family of tuples that meets twelve local conditions satisfies the finite integral laws `LocFin`, `ValX` and `ValLastX`.

The full list of conditions is in the entry [pins-finite-integrals](/entry/pins-finite-integrals/).

## Proof

The proof is the term `pins_finiteIntegrals`, tried in three forms by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic. The statements are the same, so the first form works.

## In the Lean code

The theorem is at [SeeSawLatticeFramePinsFiniteIntegralLawsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLatticeFramePinsFiniteIntegralLawsStatement.lean#L13). It only passes its hypotheses along to `GlobalTheory.SeeSaw.pins_finiteIntegrals`. A second caller, `GlobalTheory.Fam.lawsLinks_of_geo_rows_cols` in [TrueGeometryFamilyColumnData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyColumnData.lean#L53), uses it in the same way.
