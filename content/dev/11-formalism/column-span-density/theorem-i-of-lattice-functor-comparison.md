---
id: theorem-i-of-lattice-functor-comparison
title: The base-level projection bound from the lattice functor comparison
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_lattice_functor_comparison
module: Formalism.SharpRestriction.GrowthBounds.ColumnSpanDensity.TheoremIOfLatticeFunctorComparison
covers: 518
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to `LatticeFunctorComparison` and `RestCloudMaps`. Its only caller is [the bound from the two-letter model identification](/entry/theorem-i-of-model-identification/), which proves `LatticeFunctorComparison`. The proof removes one hypothesis, `LPRingIndep`, of [the next reduction](/entry/theorem-i-of-finer-open-statements/), and calls it.

## Statement

`SecondPartClosed D` and `RestCloudMaps` are as in [the bound from the explicit minor map](/entry/theorem-i-of-explicit-minor-map/). `LatticeFunctorComparison` is the splitting of a tensor product of two-letter spaces over a finite set $T$ into spaces of weight $\omega_{A-j,B-j}$, integral up to $p^{|T| N}$, as in [the parent entry](/entry/theorem-i-of-model-identification/).

**Theorem.** For each datum $D$, `LatticeFunctorComparison` and `RestCloudMaps` imply `SecondPartClosed D`.

## Proof

Assume `AdmBE D`. `tools_of_admitted_statements` gives the twelve tools `AdmT D`. Its eighth tool `NestedTypeBound D` is `WittIdent ∧ FlatTop ∧ FlatHH`; the proof keeps `WittIdent`. This says that in each Hida setting there is a ring isomorphism $\varphi$ from `WF p n'` onto $W$ with `IsWittIdent σ φ`. We have not unfolded `WF` and `IsWittIdent`.

`lpRingIndep_of''` turns `WittIdent` and `restOIso` into `LPRingIndep`. `RestOIso` says: for two settings $R_1, R_2$ for the same $p, n'$, each ring isomorphism $W_1 \cong W_2$ extends to an isomorphism $O_1 \cong O_2$ that respects the maps $W_i \to O_i$ and sends $w_1$ to $w_2$. `restOIso` proves it. With both, `restRSIso_of` builds an isomorphism of the full settings, and `LPRingIndep` follows: the statement `LPprime` holds in $R_2$ when it holds in $R_1$. Then `theorem_I_of_finer_open_statements` applies.

## In the Lean code

The theorem is in [TheoremIOfLatticeFunctorComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean#L62). `lpRingIndep_of''`, `RestOIso` and `restRSIso_of` are in [LpRingIndepOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/LpRingIndepOf.lean#L51), `LPRingIndep` in [RhoLowerBoundLargeConductor.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/RhoLowerBoundLargeConductor.lean#L157), and `WittIdent` in [ObjBridge.lean](lean:Formalism/SharpRestriction/GrowthBounds/ObjBridge.lean#L14). We have not read the proofs of `restOIso` and `lpRingIndep_of'`.

`WittIdent` is not proved here: it comes from the hypothesis `AdmBE D`, as one of the tools. The proof calls `tools_of_admitted_statements` again in the next reduction; this is bookkeeping.
