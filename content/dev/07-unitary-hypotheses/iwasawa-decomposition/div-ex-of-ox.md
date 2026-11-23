---
id: div-ex-of-ox
title: Divisor data when the object slot is OX anyGeometry, with three unused hypotheses
kind: theorem
decl: GlobalTheory.Mem.Top.DivRec.divEx_of_ox
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.TupPinsOfMuIsW
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It is [`divEx_prov`](/entry/div-ex-prov/) with three more hypotheses, which the proof discards. Its only caller is [`divEx_geoCl`](/entry/div-ex-geo-cl/). The real content is in [`divEx_prov`](/entry/div-ex-prov/) and [`exists_divT`](/entry/exists-div-t/).

## Statement

**Theorem.** Assume `RayField`, `PrincipalIdealSt` and `CMCurveGoodOutsidePrimeSt`. Let $\mathcal{S}$ be a slot with object component $\mathcal{S}.O_x = $ `OX anyGeometry`. Then `DivEx 𝒮` holds: each level 4 object has a divisor datum $Y$ with `DivT`, `MjAre`, $\kappa_R(\sigma) = \kappa^\sharp$, and a position object for each object over $Y$.

## Proof

The proof is `fun _ _ _ 𝒮 hOx => divEx_prov 𝒮 hOx`. The three hypotheses are bound to `_` and not used.

## In the Lean code

The theorem is in [TupPinsOfMuIsW.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L211).

The names of the hypotheses suggest class field theory and good reduction of CM curves: a ray class field, a principal ideal statement and good reduction outside a prime. We have not unfolded them. None of them enters the proof, so the theorem holds without them, and `DivEx` for this slot rests only on the construction in [`exists_divT`](/entry/exists-div-t/).
