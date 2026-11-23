---
id: base-one
title: The rank one Siegel-Weil measure identity, with the local mass fact supplied
kind: theorem
decl: PositivityTheory.Rg.Base1.baseOne
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.BaseOneSide.BaseOneOf
covers: 479
status: drafted
drafted_by: writer@claude
---
This theorem proves `BaseOne`, the rank one case of the Siegel-Weil identity for measures. It is the base of the induction in [`densEq`](/entry/dens-eq/). It is a pass-through: it applies [`baseOne_of`](/entry/base-one-of/) to the proved fact `massOne`. That entry has the content.

## Statement

**Theorem.** Let $E/F$ be a CM extension, let $J$ be a nondegenerate $1\times1$ Hermitian matrix and let $T\neq0$ be a $1\times1$ Hermitian matrix. Then `SWMeasC J T` holds: for all standard measures and Gram fibre measures, the theta measure of $\{X:\operatorname{gram}(X)=T\}$ is an Euler product with constant $c$, and $c=\Lambda/2$ for every limit $\Lambda$ of $\prod_v(1-e_vNv^{-s})$ as $s\to1^{+}$.

The statement is given in full in [`baseOne_of`](/entry/base-one-of/).

## Proof

Apply `baseOne_of` to `massOne`. `massOne` proves `MassOne`: for almost all finite places $v$, the local Gram fibre measure of the standard lattice, at a unit, times $(1-e_v/Nv)^{-1}$, equals $1$. Its proof uses `trace_form_coords`, `rational_integral_units` and `count_good`; I have not unfolded them.

## In the Lean code

The theorem is in [BaseOneOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BaseOneSide/BaseOneOf.lean#L28):

```
theorem baseOne : BaseOne := baseOne_of PositivityTheory.SiegelWeilFormula.BaseOne.massOne
```

`BaseOne` and `MassOne` are in [Pieces.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/Pieces.lean#L10). `massOne` is in [MassOne.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/MassOneBase/MassOne.lean#L20). Its size, 479, is one more than that of `baseOne_of`.
