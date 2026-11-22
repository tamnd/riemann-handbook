---
title: Introduction
---
This volume gives the results of the Lean folder `Formalism` that are large enough for an entry of their own. The folder holds the counting and lattice arguments that the proof uses in many places. The results hang from two steps and from one entry of [volume 9](/entry/selmer-bound-at-point-main/):

- [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). It needs the normalizing constant of a mass computation, the local volumes, the compact form of Theorem P and the gauge transfer.
- [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), in [the chapter on theta integrals](/proof/theta-matching/). It needs Theorem A and Theorem I in closed form.

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Local to global.** The normalizing constant in closed form, and the archimedean volume identity `RealBracket`.
- **Period integrals.** The closed formula `OmV` for the local volume of an orbit of frames at a finite place.
- **Hermitian curvature.** The compact form of Theorem P from two facts on radial operators, and the gauge transfer from rotation invariance.
- **Growth bounds.** Theorem A, an averaged bound on the bad share of segment lattices for large constants. Then Theorem I, which reduces to the pairing statement `QPh`, and the mean value bound over a grid.
- **Monomial factorials.** The chain of 20 reductions below Theorem A. Each link adds one proved fact and calls the next link. The real content is in a few links: the orthogonal basis of a lattice over $\mathbb{Z}_p$ for odd $p$, the bound on the bad count of the levels, and the box bound.
- **Theta log coordinates.** The mean bound `theoremMV7` on the bad count of polynomial lattices under the Fock pairing.
- **Admissible designs.** Theorem N5, a bound on the congruence length, from three proved inputs and the field `self_good` that every datum carries.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this volume most theorems pass their hypotheses along, and the names of the links in a chain often name the part that does not change. Several statements take a datum $D$ that they never read. The entry says so and points to the entry with the content.
