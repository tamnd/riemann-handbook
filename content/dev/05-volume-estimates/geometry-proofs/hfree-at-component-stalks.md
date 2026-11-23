---
id: hfree-at-component-stalks
title: Freeness at every stalk of a component, second name
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Flat.hfree_at_component_stalks
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.GermSystemHeightFree
covers: 528
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its proof is the term `PositivityTheory.Xgn.hodge_free_every_stalk`, with no other step. Its one user is the statement form [`germ_system_height_free`](/entry/germ-system-height-free/), which gives the statement in words. The content is in [`hodge_free_every_stalk`](/entry/hodge-free-every-stalk/), [`HodgeFreeStalk.at_point`](/entry/at-point/) and [`hfree_geom`](/entry/hfree-geom/).

## Statement

The statement is that of [`germ_system_height_free`](/entry/germ-system-height-free/): for a semi-abelian scheme $t$ with $\mathcal{O}_E$-action over $X$, a generic point $\xi$ in characteristic $0$ and a germ system $S$ at $\xi$, if the characteristic polynomial condition `HChar` holds for the germ at $\xi$ and the fibre condition `FibPF` holds at the specializations of positive residue characteristic, then the freeness condition `HFree` holds for the germ at every specialization of $\xi$.

## Proof

The proof is `hodge_free_every_stalk`. That proof has three steps, which we record so that the reader sees where the work is. First `hchar_iso` moves `HChar` from the germ at $\xi$ to the germ at a specialization $x$, base changed to $\Omega$, along the isomorphism of the germ system. Then `hchar_of_map` moves it down to the stalk at $x$, since the map from the stalk to $\Omega$ is injective. Last, `at_point` proves `HFree` at the stalk: in residue characteristic $0$ by `hfree_char0`, and in residue characteristic $p$ by base change to a geometric point (`formal_germ_base_change`), [`height_char_free_geometric`](/entry/height-char-free-geometric/) there, and descent by `hfree_of_map`.

## In the Lean code

The theorem is in [GermSystemHeightFree.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/GermSystemHeightFree.lean#L19). The lemma it calls is in [HodgeFreeEveryStalk.lean](lean:Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/HodgeFreeEveryStalk.lean#L178). The two names describe one statement. The file imports several statement forms (`characteristic_polynomial_free_generators`, `formal_germ_base_change` and others) that the one-line proof does not use; the lemmas of HodgeFreeEveryStalk.lean use them.
