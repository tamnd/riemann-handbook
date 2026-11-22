---
title: Introduction
---
This volume gives the shared results of the Lean folder `AutomorphicArithmetic` that are large enough for an entry of their own. A result goes here, not under one branch of the proof, when its nearest owner in the proof is a step of the proof chapters. The volume has 36 entries. They hang from three steps:

- [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), in [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). This step needs the theta lifts of the row test, the separation of functionals, the fitted function, the multiplicity equality and the tower identity.
- [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), in [the chapter on the literature layer](/proof/literature/). This step fills nine bundles of published theorems. Several of its fields come from this volume.
- [EveryCharacter from the Galois row](/step/every-character/), the last step of the proof. Four of its inputs on frames and global matching come from this volume.

The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Theta pair lifts.** Five properties of the theta lifts of the row test, with the unfolding of the theta integral, the smoothness of cuspidal lifts and the assembly of jets. Then the separation of functionals, the fitted function at large families, the equality of cuspidal multiplicities on two unitary groups by a comparison of trace formulas, and the tower identity for square constants. Last, the theorems that fill the bundles of published results: the toroidal compactification of Siegel spaces, the arithmetic Hilbert-Samuel theorem, Chern-Weil theory for good metrics, the CM inputs of `JoinOut`, and the Weil representation of split U(n,n).
- **Automorphic arithmetic.** The Siegel-Weil formula for unitary groups in the convergent range, the prismatic Dieudonné functor with its Hodge filtration, and the twisted trace on multiplicity spaces of GL_n(C).
- **Foundations.** The existence of run frames and their growth bound, and global matching from the base change fundamental lemma for the unit element.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this volume about half of the theorems are second names or only pass hypotheses along. Many of the theorems "of literature" take the record `O` of open statements and never use it, so the code proves those results itself. Several names do not match their statements. The entry says so and points to the theorem with the content.
