---
title: Introduction
---
This volume is the window bound: the branch of the proof below the theorem [vwin_of_row](/step/vwin-of-row/). From the row hypothesis [Row0b](/step/row0b-def/), it proves the statement [VWin](/step/vwin-def/). VWin bounds a weighted sum of lengths of Tate-Shafarevich groups of $\mathbb{Q}_l/\mathbb{Z}_l$ with twists by powers of the cyclotomic character. The fields in the sum are those that a primitive Dirichlet character and two auxiliary primes cut out of a cyclotomic field. [The chapter on VWin](/proof/vwin/) gives the statement in full and the top of the proof. This volume gives the parts below it, one declaration in each entry.

The branch has 55,805 declarations. The proof has two layers. The top layer is bookkeeping: it puts the row hypothesis into a structure, proves a long list of statements with names from the literature, and packs them into the structure `HypothesesH'`. The lower layer is a count. The length of each Tate-Shafarevich group splits into the part at $l = 2$ and the two eigenspaces of complex conjugation, and each prime $l$ falls into one of the cases I, II, III, IV, V or Z. Each case has its own bound. The entries here follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Modularity argument.** The main line. It starts with the passes from `vwin_of_row` down to [the four counts](/proof/vwin/). Then come the inputs to the counts, in this order:
  - Case I: the vanishing of two Bloch-Kato Selmer groups, from [an Euler system of zeta classes](/entry/zeta-ur/) for an ordinary two-dimensional representation.
  - Cases II and III: the automorphy of four-dimensional symplectic representations, with [automorphic induction](/entry/ind-cs/) from $\mathrm{GL}_2$ over a quadratic extension to $\mathrm{GL}_4$.
  - Case V: three-dimensional seeds, from [the automorphy of a twisted adjoint](/entry/adjoint-automorphy-w-of-printed-hida-window/) and [a transfer of eigenforms](/entry/spec-out-s/) from a definite $U(2)$ to $U(3)$.
  - The bound on $H^2$ ([Lemma K](/entry/lemma-k-lit-n-alt/)), [the slopes of Satake parameters](/entry/slope-all/), and the builder of [the package `HypothesesH'`](/entry/published-hypotheses-from-patching-alt/).
- **Foundation proofs.** The Hecke projector onto the Galois image of a newform, a tower of modular functions with algebraic coefficients, and a congruence between the edge class of a Siegel unit and a Kummer logarithm.
- **Iwahori reduction.** The coefficient law of the zeta class built from Siegel units, its diamond translates, and the Euler system of zeta classes.
- **Weight one forms and weight raising.** The Hilbert Eisenstein series of weight one as a theta integral, its q-expansion, and a trace formula with only elliptic terms that raises the weight of an ordinary eigenform.
- **Patching and forms congruent to 1.** Hilbert modular forms of level one close to 1 p-adically, the Hecke ideal that cuts out the automorphic points, and the length bounds for the patched module.
- **Homological stability.** The homology of $\mathrm{GL}_n$ over a ring of finite stable range is stable, and the rank bound in odd degree over a ring of integers.
- **Rankin-Selberg nonvanishing.** The partial Rankin-Selberg L-function as a ratio of entire functions, its nonzero limit at 1, and the rigidity theorem of Jacquet and Shalika.
- **Semi-local Kirillov theory.** A cuspidal vector with a prescribed Whittaker function on the semi-local mirabolic subgroup.
- **Descent from imaginary quadratic fields.** A conjugation-invariant cusp form comes from the rationals, through two twisted periods and a theta lift.
- **Good reduction.** The criterion of Néron, Ogg and Shafarevich and the theorems of Serre and Tate.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Many theorems in this branch only pass a hypothesis along or give a new name to another theorem. The entry says so and points to the theorem with the content.
