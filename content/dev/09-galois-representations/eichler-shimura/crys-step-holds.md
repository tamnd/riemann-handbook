---
id: crys-step-holds
title: A piece of a tower with a good model is crystalline
kind: theorem
decl: UpperTheory.Gal.Seam.crysStep_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.Closed
covers: 4188
status: drafted
drafted_by: writer@claude
---
This theorem proves `CrysStep`, the crystalline step of [the local steps](/entry/steps-holds/). It also goes into [the Hodge-Tate jump step](/entry/jump-step-holds/). The proof only passes one theorem to another. The content is in [the crystalline step from the comparison theorem](/entry/crys-step-of/).

## Statement

Let $E$ be a number field, $\ell$ a prime, and $H$ a nice tower over $E$ with eigenvalues $\theta$ (see [the local steps](/entry/steps-holds/) for these words). Let $\rho \colon G_E \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ be a continuous piece of $H$. Let $w$ be a place of $E$ above $\ell$, and suppose that $H$ has a cover over the valuation ring $\mathcal{O}_{(w)}$ of $w$ in $E$ that is onto. Then $\rho$ is crystalline at $w$ (`CrysAt`).

## Proof

The proof is `crysStep_of cstSmooth.1`. The theorem `cstSmooth` proves `CstSmooth`, which is three statements:

1. `SmoothModelCrystalline`: the étale cohomology of the generic fibre of a smooth projective model over $\mathcal{O}_K$ is crystalline.
2. `DeRhamComparisonSmooth`.
3. `CrysPhi`.

Only the first is used. `cstSmooth` is `Close.cstSmooth_of_side HT.etSideS`, a comparison theorem proved from a statement `EtSideS` about the étale side. Of the 4,188 declarations below this theorem, 4,182 are below `crysStep_of`. So most of the proof of `cstSmooth` is also used outside this theorem, and its declarations are counted under a higher entry.

## In the Lean code

The theorem is in [Closed.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/Closed.lean#L9), with `cstSmooth` two lines above it.

- `crysStep_of`, in [LocTowerHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/LocTowerHolds.lean#L25).
- `cstSmooth`, in the same file, and `HT.etSideS`, in [ClosedHT.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/ClosedHT.lean#L15).

`CstSmooth` has two definitions with the same body: `CrystallineSemistableComparison.CstSmooth` in [CstSmoothOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/CstSmoothOf.lean#L38) and `CrystallineSemistableComparison.Out.CstSmooth` in [CstSmooth.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/CstSmooth.lean#L18). `cstSmooth` has the first type, and its proof `Close.cstSmooth_of_side` has the second. Lean accepts this because both unfold to the same proposition. The proof then goes through three renamings: `Close.cstSmooth_of_side`, `Out.cstSmooth_of_side`, and `cstSmooth_of_side`, which is `cstSmooth_of_p Pb.pSeam`.
