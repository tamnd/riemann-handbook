---
title: Introduction
---
This volume gives the results of the Lean folder `Formalism` that are large enough for an entry of their own. The folder holds the counting and lattice arguments that the proof uses in many places. The results hang from two steps and from one entry of [volume 9](/entry/selmer-bound-at-point-main/):

- [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). It needs the normalizing constant of a mass computation, the local volumes, the compact form of Theorem P and the gauge transfer.
- [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), in [the chapter on theta integrals](/proof/theta-matching/). It needs Theorem A and Theorem I in closed form.

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Cokernel GL counts.** The normalizing constant in closed form, from the split, the archimedean bracket and the local leaves.
- **Closed volume statements.** The archimedean bracket `RealBracket` and the disintegration constant in closed form, the Jacobian of the double coset decomposition, the folding conditions for the Poincaré series, and a polynomial bound on the folding multiplicity.
- **Orbital bounds conclusion.** The archimedean orbit constant from compact stabilizers, the local mass of congruent pairs of frames, the splitting of the level subgroup, and a lower bound for the dimension of the space C_u.
- **Unitary group mass formula.** The closed formula `OmV` for the local volume of an orbit of frames at a finite place, the level splitting from the Heisenberg and Levi parts, and the integral branching maps for interlacing weights.
- **Siegel lattice theory.** The Jacobian disintegration under the limit instance `RhsWLim`, the folding statement from five local steps, and the multiplicity bound from a covering of compact sets.
- **Hermitian curvature proofs.** The compact form of Theorem P from facts on radial operators, and the gauge transfer from rotation invariance. Below them: the normal form of the shift operators, its curvature, the start data at a model level, and the germ expansion by stationary phase.
- **Local to global.** The transformation laws of the moved theta family, and the branching maps for interlacing weights.
- **Growth bounds.** Theorem A, an averaged bound on the bad share of segment lattices for large constants. Then the base-level projection bound of Theorem I and the seven statements on path polynomials that it uses.
- **Monomial factorials.** The chain of reductions below Theorem A. Each link adds one proved fact and calls the next link. The real content is in a few links: the orthogonal basis of a lattice over $\mathbb{Z}_p$ for odd $p$, the bound on the bad count of the levels, and the box bound.
- **Theta log coordinates.** The mean bound `theoremMV7` on the bad count of polynomial lattices under the Fock pairing.
- **Partner mean proofs.** The averaged bad-count bound with free constants, the mean count of small Smith entries along a progression, and the Gram hypothesis from two logarithm bounds.
- **Admissible designs.** Theorem N5, a bound on the congruence length, from the open inputs of the normalized family, a ring datum with a real display, and the field `self_good` that every datum carries.
- **Column span density.** Four routes to the base-level projection bound: from the two-letter model, the lattice functor comparison, the finer open statements, and the explicit minor map.
- **Sharp restriction.** The local lifting statements and the local theory from the admitted conditions.
- **GL3 mean squares.** The Hermitian mass formula by induction on the dimension, and the local identity that does not depend on the lattice.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this volume most theorems pass their hypotheses along, and the names of the links in a chain often name the part that does not change. Several statements take a datum $D$ that they never read. The entry says so and points to the entry with the content.
