---
id: cols-tied-sym-std
title: Standard tied Hermitian column data exist for true column choices
kind: theorem
decl: GlobalTheory.Mem.Col2.TC.colsTiedSym_std
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsStandardColumnComparisonsTrueColumns
covers: 417
status: drafted
drafted_by: writer@claude
---
This theorem builds a record of type `ColsTiedSym` for the datum attached to a choice of true columns, and shows that the record is in standard form. It is below the step [nonempty hypotheses](/step/nonempty-hyps/). The proof calls six lemmas, which do the work, and fills about 24 fields.

## Statement

Let $B$ be a base datum and $X$ a datum of type `PreX` over it, which gives an element $\pi_T(u)$ of $E$ for each word $u$. A *true column choice* $I$ (the Lean `TC B X`, an abbreviation of the structure `ColIn`) is a Hermitian frame, characters, a choice of places of $E$ over those of $F$, and a finite set of character tuples with Hecke characters $\xi$, local constants and indices. Assume that $I$ satisfies `Ok`, that $B$ and $X$ satisfy `Pins` (two compatibilities of frames and uniformizers), that the laws `I.Laws` hold, and that $Z$ is later data for the columns. Let $D$ be the `D7` datum that $I$, the laws and $Z$ assemble.

**Theorem.** There is $C$ of type `ColsTiedSym D` with:

1. for every word $u$, the forms $C_u$ are standard (`StdF`): values, uniformizers, restrictions, $\mathrm{GL}$ part, readings and projections are those of $I$;
2. the level data of $C_u$ project by the standard quotient maps, and the frame at level $J$ is $1$ (`StdLvC`).

A `ColsTiedSym D` is a Hermitian column datum together with a family of forms, one for each word, and about twenty compatibilities between them: equal characteristic data at several levels, equal lattices and projections, a common $\pi_G$, a common $\mathrm{GL}$ part and frame, and compatible characters.

## Proof

1. `T.exists_standardFormComparison_symmetricLevel_members` gives the characters, the forms $F_u$ with the standard properties 1 and 2, and the facts that the $\mathrm{GL}$ parts and characters agree.
2. `T.hermitianColumnChoices_of_formsLevelsClasses` gives levels, classes and values for a Hermitian column datum $H$.
3. `T.stepZeroHermitianLevel_uniformiser_kills_values_alt`, for each word, gives the level zero data and shows that the uniformizer kills the values. Then $H$ and $F$ have the same characteristic data.
4. `T.exists_hermitian_data_carT_of_std` gives the data at $T$ with its compatibilities.
5. `T.hermitianColumns_generators_baseLattices_functionals` gives generators, base lattices and functionals.
6. `TC.spaces_in_coordinates` gives the standard spaces.

The frame constancy and the common $\pi_G$ come from step 1. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsStandardColumnComparisonsTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsStandardColumnComparisonsTrueColumns.lean#L20), with `maxHeartbeats` set to 4000000. `ColIn` is in [TrueColumnChoicesHeckeCharReferenceEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TrueColumnChoicesHeckeCharReferenceEqOne.lean#L165). `ColsTiedSym` is in [BothSym.lean](lean:Formalism/LocalToGlobal/HermitianForms/BothSym.lean#L27). `StdF` and `StdC` are in [LatAtLattice.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/LatAtLattice.lean#L338), and `StdLvC` is in [StdLvPr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/StdLvPr.lean#L68). We have not unfolded `Ok`, `Later`, `FormsTiedSym` or `ColsHermS`, and we have not opened the six lemmas. The folder name speaks of the Iwasawa decomposition, but none appears in the statement.
