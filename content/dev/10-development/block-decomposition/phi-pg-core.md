---
id: phi-pg-core
title: The extension for the twisted Jacquet functor, from the closed and open cells
kind: theorem
decl: GlobalTheory.CompanionTheory.BZPhiPG.phiPG_core
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.PhiPgCommutationHolds
covers: 615
status: drafted
drafted_by: writer@claude
---
This theorem proves the exact sequence of [the twisted Jacquet functor on a mirabolic product](/entry/phi-pg/), with the three representations written as compactly induced spaces. Its only user casts the indices and rewrites the spaces.

## Statement

We use the notation of the parent entry. Let $\psi$ be a continuous unitary character of $k$, $\tau$ a smooth representation of $P_{i+2}$ and $\sigma$ a smooth representation of $\mathrm{GL}_{t+1}(k)$. Let $N = P_{i+t+3}$, the mirabolic group of $\tau \times \sigma$.

- $X$ (`XR'`) is the compact induction to $N$, from the subgroup `HPG` of block form, of $\tau\nu^{(t+1)/2} \otimes \sigma\nu^{-(i+2)/2}$.
- $C$ (`RC`) is the compact induction from `MirabolicParabolic` of $(\Psi\tau)\nu^{(t+1)/2} \otimes (\sigma|_P)\nu^{-(i+1)/2}$.
- $O$ (`RO`) is the compact induction from `HPG` of $(\Phi\tau)\nu^{(t+1)/2} \otimes \sigma\nu^{-(i+1)/2}$.

**Theorem.** $\Phi X$ has a subrepresentation isomorphic to $O$, with quotient isomorphic to $C$.

By `xr_eq`, `rc_eq` and `ro_eq`, the spaces $X$, $C$, $O$ are $\tau \times \sigma$, $\Psi\tau \times \sigma|_P$ and $\Phi\tau \times \sigma$ by definition.

## Proof

The proof is the cell argument of Bernstein and Zelevinsky (Ann. Sci. ENS 10 (1977), Section 4). Let $U$ be the unipotent subgroup `MirUin` of $N$, with the character $\theta$ (`mirChar`) from $\psi$. Then $\Phi X$ is the quotient of $X$ by the span of the $u f - \theta(u) f$, twisted by $\nu^{-1/2}$. Let $Z$ (`Cl`) be the closed set of $p \in N$ where $i+1$ fixed entries of $p^{-1}$ vanish.

1. `mirabolic_cell_structure_data` gives: $U$ is normal, $\ker\theta$ is open, $Z$ is closed, stable under `HPG` on the left and under $U$ on the right, and the compact subgroups of $U$ form a directed family.
2. Two evaluation maps send $f \in X$ to functions on the smaller mirabolic group. The closed one integrates $f$ over $t+1$ entries of the last column against $\psi^{-1}$ of the last coordinate, then takes untwisted coinvariants. The open one integrates with no character after a permutation matrix, then takes $\psi$-twisted coinvariants. Both carry the factor $\nu^{-1/2}$.
3. `twisted_jacquet_closed_open_sequence` is an abstract lemma. From the data of step 1, two linear maps into injective models of $C$ and $O$, and eleven properties of the maps, it gives the extension. The properties are: $\theta$-equivariance, compatibility with the action of $N$, image in the model, surjectivity, the closed map kills functions that vanish on $Z$, and two localisation facts (`AvgVanish`). They come from `evaluation_maps_linear`, `closed_evaluation_equivariant`, `open_evaluation_equivariant`, `aC_eCl`, `aO_eOl`, `closed_evaluation_induced`, `open_evaluation_induced`, `closed_evaluation_surjective`, `open_evaluation_surjective`, `closed_evaluation_vanishing_on_open`, `average_vanishes_closed_cell` and `average_vanishes_open_cell`.

The functions supported off $Z$ give the subrepresentation $O$, and the restriction to $Z$ gives the quotient $C$.

## In the Lean code

The theorem is in [PhiPgCommutationHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PhiPgCommutationHolds.lean#L175). The evaluation maps `eC`, `eO` and the set `Cl` are in [AvgVanish.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AvgVanish.lean#L52). The abstract lemma is proved by `Glue.extension` in [TwistedJacquetClosedOpenSequence.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TwistedJacquetClosedOpenSequence.lean#L259). We have not read the proofs of the twelve evaluation lemmas.

The theorem does not need $\psi \ne 1$. The identifications `xr_eq`, `rc_eq` and `ro_eq` (L88 to L95) are `rfl` proofs that need `maxHeartbeats 1000000`.
