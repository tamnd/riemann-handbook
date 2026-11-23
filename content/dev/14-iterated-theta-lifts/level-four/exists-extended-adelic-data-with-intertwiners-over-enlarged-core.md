---
id: exists-extended-adelic-data-with-intertwiners-over-enlarged-core
title: An extended adelic datum over a given core (second name)
kind: theorem
decl: GlobalTheory.T.exists_extendedAdelicData_with_intertwiners_over_enlargedCore
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsExtendedAdelicDataWithIntertwinersOverEnlaStatement
covers: 348
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`datExt_rest`](/entry/dat-ext-rest/), which has the proof. It is step 2 of [`exists_ext_build`](/entry/exists-ext-build/): given a core over the enlarged base, it builds the rest of the adelic datum.

## Statement

The setting is that of [`exists_ext_build`](/entry/exists-ext-build/): the seven named hypotheses, bases $B$ and $B'$ with `Enl0 B B'`, a fine adelic datum $z$ over $B$, and a later stage $Z'$ over $B'$.

**Theorem.** Eventually in the context, in this setting, let $c'$ be a core over $Z'$ with an algebra map from its coefficient field $F$ to $L_{B'}$. Assume:

1. the map commutes with the embeddings into $\mathbb C$;
2. its image lies in $L_{B',0}$, and contains $K_s$;
3. the fourteen core parts of $c'$, `H` to `iota`, equal those of $z$ (as `HEq`);
4. $c'$ satisfies `LawsCore` and `Canon`, $p + q \ge 1$ for each signature, and its `pb` is that of the frame $f'$.

Then there is an adelic datum $z'$ at $Z'$, with the places of residue characteristic in $T'.\mathrm{pl}$, such that its core is $c'$, its real datum satisfies `ExAt`, its geometry satisfies `InGeo`, `Std` holds, and `ExtN z z'`.

These are exactly the facts that `exists_adelicCore_transport_enlargedCoefficientBase_alt` gives in step 1 of `exists_ext_build`.

## Proof

The proof is the tactic `first | exact @datExt_rest | ...` (namespace shortened), which tries three ways to apply `datExt_rest`. The two statements are the same text.

## In the Lean code

The theorem is in [ExistsExtendedAdelicDataWithIntertwinersOverEnlaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedAdelicDataWithIntertwinersOverEnlaStatement.lean#L22). `datExt_rest` is in [ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean#L53).

No intertwiner appears in the statement, although the name says "with intertwiners". The fourteen equalities of item 3 are written out as a conjunction, not as a named structure.
