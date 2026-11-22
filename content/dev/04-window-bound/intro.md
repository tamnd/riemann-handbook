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
- **Foundation proofs.** The Hecke projector onto the Galois image of a newform, and a congruence between the edge class of a Siegel unit and a Kummer logarithm.
- **Iwahori reduction.** The coefficient law of the zeta class built from Siegel units, its diamond translates, and the Euler system of zeta classes.
- **Automorphic forms**, **automorphic arithmetic** and **abelian variety theory.** Smaller pieces from other Lean folders: rank bounds in the homology of $\mathrm{GL}_n$, a descent from rank two, and a rigidity theorem of Jacquet-Shalika type.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Many theorems in this branch only pass a hypothesis along or give a new name to another theorem. The entry says so and points to the theorem with the content.
