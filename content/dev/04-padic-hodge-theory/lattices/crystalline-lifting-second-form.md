---
id: crystalline-lifting-second-form
title: The lifting theorem for crystalline lattices, from the record of Wach hypotheses
kind: theorem
decl: Formalism.MainNotions.WachCoordinates.Br.crystalline_lifting_second_form
module: Formalism.SharpRestriction.LevelLetterCocycles.CrystallineLiftingEveryOrdering
covers: 925
status: drafted
drafted_by: writer@claude
---
This theorem proves the lifting statement `ThmELiftAt` for the fixed ordering $\mathrm{emb}$ of the Wach data $W$, from one record `BrHyp2` of hypotheses. It is the step where the crystalline lattices are turned into the abstract lattices of [theorem E in final form](/entry/theorem-e-final-form/). [The local lifting theorem from local inputs](/entry/local-theorem-of-inputs/) calls it, after it builds the record with `brHyp2_of_rec`.

## Statement

`ThmELiftAt` is stated in the [parent entry](/entry/local-theorem-of-inputs/): a surjection $f \colon T_1 \to T_2$ of crystalline lattices with jumps in windows *lifts with exponent* $e = \mathrm{ePar}(\ldots)$, that is, $\ell^e$ kills each finite cocycle of $T_2$ modulo the image of the finite cocycles of $T_1$ plus coboundaries.

`BrHyp2 W C` has these fields:

- the setting: $s = 1$, $K = K_0$ (unramified), $\ell \ge 5$, $\mathcal{O}$ is a valuation ring for $v$ and is $\ell$-adically complete;
- the Wach lattice lemmas `P5`, `P6` (saturation exactness) and `P9`, and the first Herr complex property `herr`;
- `coreWX`, `coreWR W C`, `ToolsAlg`, `F1`, `F2`, and `HodgeExact` (jumps behave well in short exact sequences);
- `real`: some element of the Wach module of the trivial lattice satisfies `UnitGen`, `BKExt` and, for each `Ring9` structure, `Realised2`.

**Theorem.** If `BrHyp2 W C` holds, then `ThmELiftAt` holds for $\mathrm{emb}$.

We have not unfolded `coreWX`, `coreWR`, `ToolsAlg`, `F1`, `F2`, `UnitGen` and `BKExt`.

## Proof

The proof fixes the data of `ThmELiftAt`. Then:

1. `realised_of` builds the coordinates: lattices $L_1, L_2, L_0$ over $\mathcal{O}[[X]]$ with a map $h \colon L_1 \to L_2$, a uniformiser $\varpi$, and the proofs of `FinalLat` for $L_1, L_2$, `PrimUnit` for $L_0$, the extension data, `WPrimeCuts` and the arcs. The arcs come from `Realised2`, that is, from [`realised2_pf`](/entry/realised2-pf/).
2. `finalNum_of` checks the numerical conditions `FinalNum` for the parameters $\mathrm{sigPar}$, $\mathrm{rrPar}$ and $\mathrm{kapPar}$. It uses the hypothesis `WordOK`.
3. The jumps of $T_2$ lie in $[-h, h]$, since by `HodgeExact` each jump of $T_2$ is a jump of $T_1$.
4. `rho_fieldN` (with `F1`, `F2`) shows that the cocycle set `ZfN C₁ F` of $T_1$ contains the needed cocycles.
5. [Theorem E in final form](/entry/theorem-e-final-form/) gives: $\ell^{\mathrm{parE}}$ times each cocycle of `Zf C₂` is $h$ of a cocycle of `ZfN C₁ F` up to a coboundary.
6. $\mathrm{parE} = \mathrm{ePar}$ by definition (`parE_eq_ePar`). Then `liftF_ofN` translates this into `LiftF` for $f$. It uses `herr`: each finite cohomology class of $T_2$ comes from a Wach cocycle.

## In the Lean code

The theorem is at [CrystallineLiftingEveryOrdering.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingEveryOrdering.lean#L159). `BrHyp2` is at [line 65](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingEveryOrdering.lean#L65) and `realised_of` at [line 99](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingEveryOrdering.lean#L99). `liftF_ofN` is at [FrobeniusCocycleOfRhoData.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusCocycleOfRhoData.lean#L55), and `parE_eq_ePar` at [ExponentWindowSubsetShort.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ExponentWindowSubsetShort.lean#L62).

- The letter condition `Letters`, the first premise of `ThmELiftAt`, is introduced as `_` and not used.
- The constant $C$ of `BrHyp2` enters only through the field `coreWR W C`.
- `crystalline_lifting_every_ordering` (same file) extends the result to every ordering by a rotation of $\mathbb{Z}/n$.
