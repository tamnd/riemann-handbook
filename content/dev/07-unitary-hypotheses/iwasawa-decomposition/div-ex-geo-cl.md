---
id: div-ex-geo-cl
title: Divisor data for the slot with the closed geometry
kind: theorem
decl: GlobalTheory.Mem.Top.Closing.divEx_geoCl
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PublishedInputsImplyConclusion
covers: 341
status: drafted
drafted_by: writer@claude
---
This theorem proves the divisor step `DivEx` for the slot that the [membership theorem](/entry/member-e-closing-alt-alt/) uses: the object component is `OX (geoCl anyGeometry)`. It takes the result of [`divEx_of_ox`](/entry/div-ex-of-ox/) for `OX anyGeometry` and moves it to the closed geometry. The construction of the divisor datum is in [`divEx_prov`](/entry/div-ex-prov/) and [`exists_divT`](/entry/exists-div-t/).

## Statement

The names of [`divEx_prov`](/entry/div-ex-prov/) are used. A *geometric predicate* $\Gamma$ (`GeoP`) is a property of a datum $D$, a core $J$ and a divisor datum $X$. Its closure `geoCl Γ` is the smallest predicate that contains $\Gamma$ and is stable under the operation `setDiv` on $D$, with `coreS` on $J$ and `divTr` on $X$ (`GeoCl`, with the cases `base` and `step`).

**Theorem.** Assume `RayField`, `PrincipalIdealSt` and `CMCurveGoodOutsidePrimeSt`. For each position $R$, norm condition $N$ and side position $S$, `DivEx` holds for the slot $(R, N, S, \mathrm{OX}(\mathrm{geoCl}(\mathrm{anyGeometry})))$.

## Proof

1. [`divEx_of_ox`](/entry/div-ex-of-ox/) gives `DivEx` for the slot $(R, N, S, \mathrm{OX}(\mathrm{anyGeometry}))$.
2. `StepW.trans` with `StepW.of_all` passes to the new slot. Fix $w$, $Z$ and a level 4 object $l$ of the new slot. Its fields, copied one by one, make a level 4 object of the old slot. Step 1 gives a divisor datum $Y$ for it, with `DivT`, `MjAre` and $\kappa_R(\sigma) = \kappa^\sharp$.
3. For an object $O$ over $Y$, step 1 gives a record $o$ of type `OAt anyGeometry`. The record $\langle$`geoCl_of o.geo`, `o.lam`$\rangle$ has type `OAt (geoCl anyGeometry)`, since `geoCl_of` is the case `base`.

## In the Lean code

The theorem is in [PublishedInputsImplyConclusion.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PublishedInputsImplyConclusion.lean#L39). `GeoCl` and `geoCl_of` are in [NotGeoClFalse.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L21).

Odd points:

- The three hypotheses only pass to `divEx_of_ox`, which does not use them. So the theorem holds without them.
- `anyGeometry` is the constant predicate `True`, so `geoCl anyGeometry` is also always true. The geometric part of the object condition is empty for both slots. Only `LamAre` is left.
