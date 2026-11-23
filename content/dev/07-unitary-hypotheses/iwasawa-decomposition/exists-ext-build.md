---
id: exists-ext-build
title: Building the extension from a transported core
kind: theorem
decl: GlobalTheory.Mem.R3.Rw.ExtBuild.exists_ext_build
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsExtendedColumnDataAllClausesButPlaces
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem builds a fine adelic datum over an enlarged base that agrees with a given one in all clauses of `ExtN`. It is the proof of its second name [`exists_extendedColumnData_all_clauses_but_places`](/entry/exists-extended-column-data-all-clauses-but-places/), step 1 of [`datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/). It splits the work in two: first carry the core over, then build the rest of the datum over the new core. The second part has the content.

## Statement

The words *pinned*, *adelic datum*, *fine*, `Enl0`, `ExtN` are as in the [entry of `datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/).

**Theorem.** Assume the seven named hypotheses. Eventually in the context, for every pinned $w'$ over $B'$, every pinned $w$ over $B$ with `Enl0 B B'`, the same frame and the same `px`, every fine adelic datum $z$ at a later stage $Z$ of $w$ with `GrpTrue`, `GrpAt` and `HoldsL`, and every later stage $Z'$ of $w'$ with `GrpTrue`, `GrpAt` and `VolTieG`, there is a fine adelic datum $z'$ at $Z'$, with the places of residue characteristic in $T'.\mathrm{pl}$, such that `ExtN z z'`.

## Proof

1. `exists_adelicCore_transport_enlargedCoefficientBase_alt` carries the core of $z$ to $Z'$. It needs only `Enl0 B B'`, the equal frames and the core laws of $z$ (the part `CoreP` of `Fine z`). It gives a core $c'$ over $Z'$ with an algebra map from its coefficient field $F$ to $L_{B'}$ such that: the map commutes with the embeddings into $\mathbb C$; its image lies in $L_{B',0}$; its image contains $K_s$; the fourteen core parts of $c'$ equal those of $z$; and $c'$ satisfies the four core laws.
2. [`exists_extendedAdelicData_with_intertwiners_over_enlargedCore`](/entry/exists-extended-adelic-data-with-intertwiners-over-enlarged-core/) takes $c'$ and these facts. It gives $z'$ with core $c'$, with `ExAt`, `InGeo` and `Std`, and with `ExtN z z'`.
3. `Fine z'` needs the core laws of $z'$. They are the laws of $c'$, since the core of $z'$ is $c'$.

`StepW.trans` and `StepW.of_all` put the steps together. The seven hypotheses go only to step 2.

## In the Lean code

The theorem is in [ExistsExtendedColumnDataAllClausesButPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedColumnDataAllClausesButPlaces.lean#L27). It calls:

- `exists_adelicCore_transport_enlargedCoefficientBase_alt`, a second name of `Rw.exists_adelicCore_transport_enlargedCoefficientBase`, which we have not opened;
- `exists_extendedAdelicData_with_intertwiners_over_enlargedCore`;
- `StepW.trans`, `StepW.of_all`, and the definition `CoreP` in [ReadPk.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ReadPk.lean#L61).

Step 1 does not use the seven hypotheses or the pins. The transport lemma has no `StepW` and no context: it holds for every pair of bases.
