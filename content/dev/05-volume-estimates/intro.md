---
title: Introduction
---
This volume is the volume branch of the literature layer: the proof of the [covolume bound](/step/covolume-bound-of-x-def/) $\mathsf{CovolumeBoundOfX}$. [The literature layer](/proof/literature/) needs this bound as one input of the trunk. Most of the proof is a statement of Arakelov geometry, the positivity statement $\mathsf{DeepStR}$, which [the chapter on the Weil bound](/proof/weil-bound/) states and explains. The name of the Lean folder WeilBound refers to Weil pairings, not to Weil's explicit formula. This volume gives the parts below these two chapters, one declaration in each entry.

The branch has 52,186 declarations. The proof goes in the order of the Weil bound chapter. An absolute Siegel lemma gives a slope bound. Then a tower of integral models of Shimura varieties with good reduction gives the volume theorem, a lower bound for the arithmetic self-intersection numbers of the tower. The volume theorem gives a bound on the mean volume slope, and from that comes $\mathsf{DeepStR}$. The covolume bound is a chain of slope inequalities on hermitian lattices that uses $\mathsf{DeepStR}$. The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Theta pair lifts.** The covolume bound from its seven groups of hypotheses, the height lower bound for the components of a good cover, and the copy of the published Hodge bundle theorems into the hypotheses of the branch.
- **Automorphic kernels.** The good tower and the volume theorem from their inputs, and the absolute Siegel lemma from the bounds on successive minima.
- **Geometry proofs.** The assembly of the volume branch. It includes the lattice families at places above an odd prime $p$, the comparison of Hodge lattices with flags, the bound on the mean volume slope, and the slope bound from the Siegel lemma.
- **Divisibility proofs.** The good tower and the volume theorem, with the constant of the volume theorem made explicit.
- **Core statements** and **proofs.** The swap relation $\mathrm{I8}$ on a good tower, the square systems on flag covers, and the relations between Chern numbers of lattice bundles over a discrete valuation ring.
- **Abelian variety theory.** A form of Hirzebruch-Mumford proportionality for toroidal flag spaces, and the good base and Hodge metric that prove it.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this branch many theorems are second names of other theorems, and some names do not match the statements. The entry says so and points to the theorem with the content.
