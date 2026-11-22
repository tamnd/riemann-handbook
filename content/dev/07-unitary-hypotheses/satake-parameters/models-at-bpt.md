---
id: models-at-bpt
title: Local models at a constructed point
kind: theorem
decl: GlobalTheory.Svd.modelsAt_bpt
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TuplesHaveLocalModelsAtConstructedPointOverTrueC
covers: 2859
status: drafted
drafted_by: writer@claude
---
This theorem shows that the object of a constructed point has local models, when the core of the point comes from a column with a part. It moves the result for column objects to the point, in two steps. Its user is the renaming [`tuplesHaveLocalModels_at_constructedPoint_over_trueColumns`](/entry/tuples-have-local-models-at-constructed-point-over-true-columns/), and through it [`servH_row`](/entry/serv-h-row/). The real content is in [`modelsAt_of_part`](/entry/models-at-of-part/), through its renaming `tuplesHaveLocalModels_of_standardColumnObjects` (2,851 declarations).

## Statement

- A *constructed point* $\beta$ over a context $K$ (`BPt K`) has a core $c$, a layer $Y$ with object equal to $c.O$ (field `hY`), a part $p$ of $Y$ and further conditions. Its datum `β.D` is `setDiv D (nPrime p.L) p.ht`: the datum $D$ of $Y$ with the division lattices replaced by the lattices `nPrime p.L` and the heights replaced by `p.ht`. Here `nPrime p.L u` is the span of the products $a y$ with $a$ in an ideal `Iu` and $y$ in the lattice `NuLat u`.
- `positionOf HasPart` holds at a core when it equals a core at a column $w$ and an index $Z$, for which a `Part w Z` exists. A `Part` has nine fields (pins, a column, an error bound, a tuple tie, a kernel and others). We have not unfolded them.
- `ModelsAt D O` is an implication. If the lattices of $O$ are tied (`LatTied`) and $2\, r_G \le k$, then `ModelsOK` holds. `ModelsOK` gives a base equation and a lattice chain with conditions at each site. We have not unfolded it fully.

**Theorem.** Assume `AdmAtEnt2` and `CurveEx` (see [`servH_row`](/entry/serv-h-row/)). Let $\beta$ be a constructed point whose core is in `positionOf HasPart`. Then `ModelsAt β.D β.O`.

## Proof

1. Let $X$ be the stages of $\beta$. We show `ModelsAt X.toD7 O` for every object $O$ over $X$ whose image `ofObj O` is the object of the core. By `positionOf_ind`, it is enough to do this at a column $w$ and an index $Z$ with a `Part w Z`. The part moves along the equation to a `Part w Z (ofObj O)`. Then [`tuplesHaveLocalModels_of_standardColumnObjects`](/entry/tuples-have-local-models-of-standard-column-objects/) gives `ModelsAt`.
2. Apply step 1 to the object `β.Y.obj β.p` of the layer. The equation holds by `ofObj_obj` (true by definition) and `β.hY`.
3. `tuplesLocalModels_of_otherDivisionLatticesHeights` says that `ModelsAt D O` implies `ModelsAt (setDiv D N h) (O.tr N h)` for all lattices $N$ and heights $h$. With $N$ = `nPrime β.p.L` and $h$ = `β.p.ht` this is `ModelsAt β.D β.O`.

## In the Lean code

The theorem is at [TuplesHaveLocalModelsAtConstructedPointOverTrueC.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TuplesHaveLocalModelsAtConstructedPointOverTrueC.lean#L10). `ModelsAt` is at [HasPartAnd.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L13), `BPt` at [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L67), and `positionOf_ind` at [PositionOfIntro.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/PositionOfIntro.lean#L101).

The last step closes by definition: `β.D` and `β.O` unfold to the transported datum and object. The transport lemma is a renaming of `modelsAt_tr`, whose proof keeps the lattice chain and applies two lemmas saying that the site conditions do not depend on the division lattices. The hypotheses `AdmAtEnt2` and `CurveEx` are used only in step 1.
