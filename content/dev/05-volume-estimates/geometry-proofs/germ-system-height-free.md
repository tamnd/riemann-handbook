---
id: germ-system-height-free
title: Freeness at every stalk of a component, restated
kind: theorem
decl: GlobalTheory.T.germ_system_height_free
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.GermSystemHeightFreeStatement
covers: 529
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`hfree_at_component_stalks`](/entry/hfree-at-component-stalks/), which is itself a second name of [`hodge_free_every_stalk`](/entry/hodge-free-every-stalk/). The content is in [`HodgeFreeStalk.at_point`](/entry/at-point/) and [`hfree_geom`](/entry/hfree-geom/). Its users are `exists_hodgeLat` and `hodgeLat_model`, which build Hodge lattices on a model below [`topCovolSlim2_use_alt_alt`](/proof/literature/).

## Statement

Let $E$ be a CM field with host datum $H$, and give $\mathcal{O}_E$ the star map of complex conjugation. Let $t$ be a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action and a cubical line bundle. Let $\xi \colon \operatorname{Spec}\Omega \to X$ be a point with $\operatorname{char}\Omega = 0$, $M$ a model of the Lie algebra of $t$ at $\xi$ on $\Omega^d$, and $S$ a germ system: a formal germ $g_0$ at $\xi$, a formal germ $g_x$ at the stalk of each specialization $x$ of $\xi$, and isomorphisms between them over $\Omega$. Suppose:

1. `PowFns t`: for each $n$, the map on global functions of the $n$-th power of $t$ is bijective;
2. `IsCptGen ξ`: the stalk of $X$ at the image of $\xi$ maps bijectively onto $\Omega$, and each stalk at a specialization maps injectively to $\Omega$;
3. `HChar` for $g_0$ with exponent $r$;
4. `FibPF` at each specialization of residue characteristic $p > 0$.

Then `HFree` holds for each $g_x$ with the same $r$. The conditions `HChar`, `HFree` and `FibPF` are stated in [the entry on the geometric case](/entry/hfree-geom/).

## Proof

The statement is the same as that of `hfree_at_component_stalks`, and the proof applies it.

## In the Lean code

The theorem is in [GermSystemHeightFreeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/GermSystemHeightFreeStatement.lean#L11). `GermSys`, `HChar` and `HFree` are in [GermSys.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GermSys.lean#L19). The name says "height", but no height appears in the statement. The file that proves it calls the same property "Hodge free".
