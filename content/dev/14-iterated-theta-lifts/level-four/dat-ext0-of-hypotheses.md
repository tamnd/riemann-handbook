---
id: dat-ext0-of-hypotheses
title: Fine adelic data extend to an enlarged base
kind: theorem
decl: GlobalTheory.Mem.R3.Rw.datExt0_of_hypotheses
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.AdelicDataExtendLargerFieldsOfHyp
covers: 599
status: drafted
drafted_by: writer@claude
---
This theorem proves `DatExt0`: a fine adelic datum over a base extends to each enlarged base, with the same core, the same real datum and the same marked places. It is the proof of its second name [`adelicData_extend_largerFields_of_hypotheses`](/entry/adelic-data-extend-larger-fields-of-hypotheses/). It joins two results: one that builds the extension and checks every clause but the places, and one that checks the places.

## Statement

The objects are those of the column construction. A base $B$ has a field $L_B$ with an embedding $L_B \to \mathbb C$, a subfield $L_{B,0}$ and a coefficient field $K_s$. A column datum $w$ over $B$ is *pinned* if it has a `ColPin`. An *adelic datum* $z$ (`Dat`) at a later stage $Z$ of $w$, with a set $W_t$ of places, has a core with a coefficient field $F \subset L$, a real datum $R$, a geometric half, pins, a level and twist data. It is *fine* (`Fine`) if $R$ satisfies `ExAt`, the geometry satisfies `InGeo`, the core satisfies its laws (`LawsCore`, `Canon`, $p + q \ge 1$ for each signature, and its `pb` is that of the frame), and `Std` holds.

$B'$ *enlarges* $B$ (`Enl0 B B'`) if they have the same underlying pre-base, $K_s$ has the same image in $\mathbb C$, the image of $L_{B,0}$ lies in that of $L_{B',0}$, and the image of $L_B$ lies in that of $L_{B'}$.

**Theorem.** Assume the seven named hypotheses `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay`, `CasselmanWallach`, `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `HarishChandraFinite`. Then, eventually in the context, the following holds for every pinned column datum $w'$ over a base $B'$. Let $w$ be a pinned column datum over $B$ with `Enl0 B B'`, the same frame and the same `px`. Let $z$ be a fine adelic datum at a later stage $Z$ of $w$, with `GrpTrue`, `GrpAt` and `HoldsL`. Let $Z'$ be a later stage of $w'$ with `GrpTrue`, `GrpAt` and `VolTieG`. Then there is a fine adelic datum $z'$ at $Z'$, with the places $\{v : \text{residue characteristic of } v \in T'.\mathrm{pl}\}$, such that `Ext z z'`.

`Ext z z'` has two parts. `ExtN` says that $z'$ has the same core parts (fourteen of them, `H` to `iota`), the same parts of the real datum, and the same data at each index $i$, as $z$. These are equalities across the change of type (`HEq`). The last clause `W1` says: if a place $v$ of $L_B$ lies below a place $v'$ of $L_{B'}$ (`Below`: integers with the same image in $\mathbb C$ lie in both or in neither), then $v$ is in the marked set $W_1(z)$ if and only if $v'$ is in $W_1(z')$ (both taken with the weight function 0).

## Proof

1. [`exists_extendedColumnData_all_clauses_but_places`](/entry/exists-extended-column-data-all-clauses-but-places/) gives a fine $z'$ with `ExtN z z'`.
2. `extendedData_nonzero_index_places_correspond_alt` says that every fine $z'$ with `ExtN z z'` satisfies the clause `W1`. It compares lattice indices at $v$ and $v'$ under a field map $L_B \to L_{B'}$.
3. `StepW.and` joins the two, and `ExtN.ext` adds the clause `W1` to `ExtN` to give `Ext`.

The seven hypotheses go to both parts unchanged.

## In the Lean code

The theorem is in [AdelicDataExtendLargerFieldsOfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AdelicDataExtendLargerFieldsOfHyp.lean#L29). `DatExt0` and `Enl0` are in [IsBaseEnlargementFixedCoefFieldOfCoeffEnlargemen.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsBaseEnlargementFixedCoefFieldOfCoeffEnlargemen.lean#L22); `ExtN` and `ExtN.ext` are in [Forms.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/Forms.lean#L20).

`extendedData_nonzero_index_places_correspond_alt` is itself a second name of `TwistedPlaceExtensions.extendedData_nonzero_index_places_correspond`. We have not unfolded `W1`; the name says that it is the set of places with a nonzero lattice index. Step 1 dominates 362 of the 599 declarations under this theorem.
