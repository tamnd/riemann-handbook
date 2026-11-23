---
id: lattice-family-ck-relations
title: The Chern number relations for the bundles of a lattice family, restated
kind: theorem
decl: GlobalTheory.T.lattice_family_ckRelations
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModelsStatement
covers: 709
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`CkTop.ckRelations_of_model`](/entry/ck-relations-of-model/), which has the content. Its one user is [the Chern number relations for flag pairs](/entry/top-rel-relations/), which uses it in its first step and then moves the relations from the bundles to the flag pairs.

## Statement

Let $O$ be a discrete valuation ring of characteristic $0$ and $\Omega$ a field over $O$. Let $x$ be coordinates $x_{k,i} \in \Omega$ such that the coordinate ideal of $x$ is a model over $O$ of dimension $d$ (`IsModelOver`) and the function field of $x$ is all of $\Omega$. Let $p$ be a prime, $w \in O$, $\chi$ a family of maps $F \to O$, $\varphi$ a permutation of the labels $\Sigma$, and $D$ a lattice family (`IsLatticeFamily`). Let $\mathrm{Lie}, W, \Omega_1, \Omega_{\mathrm{HT}}$ be chart bundles whose lattices on each chart are those of $D$ (`HasBundles`).

**Theorem.** The relations `CkRelations` hold for $\mathrm{Lie}, W, \Omega_1, \Omega_{\mathrm{HT}}$: for each $1 \leq k \leq d + 1$ and each homogeneous $Q$ of degree $d + 1 - k$ there is $h \colon \Sigma \to \mathbb{R}$ with

$$c_k(\mathrm{Lie}_\tau, W_\tau) + c_k(\Omega_{1,\tau}, \Omega_{\mathrm{HT},\tau}) = h(\tau) - \frac{\lambda_k(\mathrm{Lie}_\tau)}{p - 1}, \qquad p^k h(\tau) = h(\varphi\tau) + \lambda_k(\mathrm{Lie}_{\varphi\tau}).$$

The numbers $c_k$ and $\lambda_k$ are those of [the parent entry](/entry/top-rel-relations/).

## Proof

The statement is the same as that of `ckRelations_of_model`, and the proof applies it.

## In the Lean code

The theorem is in [DescentRelationsFromModelsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModelsStatement.lean#L9). The proof is the tactic `first | exact @ckRelations_of_model | ...`, whose first branch is a direct application. `CkRelations` is in [IsLatticeFamily.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/IsLatticeFamily.lean#L42).
