---
title: Introduction
---
This volume is the volume branch of the literature layer: the proof of the [covolume bound](/step/covolume-bound-of-x-def/) $\mathsf{CovolumeBoundOfX}$. [The literature layer](/proof/literature/) needs this bound as one input of the trunk. Most of the proof is a statement of Arakelov geometry, the positivity statement $\mathsf{DeepStR}$, which [the chapter on the Weil bound](/proof/weil-bound/) states and explains. The name of the Lean folder WeilBound refers to Weil pairings, not to Weil's explicit formula. This volume gives the parts below these two chapters, one declaration in each entry.

The branch has 52,186 declarations. The proof goes in the order of the Weil bound chapter. An absolute Siegel lemma gives a slope bound. Then a tower of integral models of Shimura varieties with good reduction gives the volume theorem, a lower bound for the arithmetic self-intersection numbers of the tower. The volume theorem gives a bound on the mean volume slope, and from that comes $\mathsf{DeepStR}$. The covolume bound is a chain of slope inequalities on hermitian lattices that uses $\mathsf{DeepStR}$. The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Theta pair lifts.** The covolume bound from its seven groups of hypotheses, the height lower bound for the components of a good cover, and the copy of the published Hodge bundle theorems into the hypotheses of the branch.
- **The volume theorem from its inputs.** The good tower and the volume theorem from their inputs, and the absolute Siegel lemma from the bounds on successive minima.
- **The assembly of the volume branch.** The lattice families at places above an odd prime $p$, the comparison of Hodge lattices with flags, the bound on the mean volume slope, and the slope bound from the Siegel lemma.
- **Good towers and the volume theorem.** The chain of tower estimates, the antisymmetry of the height defect, and the volume theorem with its constant made explicit.
- **The swap relation on a good tower.** The swap relation $\mathrm{I8}$ from seven statements.
- **Swaps, height defects and theta sections.** The analytic square of an adjacent swap, the sign change of the height defect, and the sup bound and mean log sup of a theta section.
- **Rest terms over primes.** The bound on the rest terms at one prime and summed over primes.
- **Hodge modules and flat sections.** Freeness of the Hodge module, flat sections of near record height, and square systems on flag covers.
- **Chern number relations.** The relations between Chern numbers of lattice bundles over a discrete valuation ring, by a chain of model refinements, and the Mahler measure of a Chow form cut by a linear form.
- **Lie eigenlattices and the Hilbert-Samuel bound.** The degree difference of the Lie eigenlattices of a definite CM object, the geometric Hilbert-Samuel bound, the flat section of the Lie determinant line, and the depth oscillation bounds.
- **The Hodge metric and its Chern integrals.** A form of Hirzebruch-Mumford proportionality for toroidal flag spaces: a good base, its Hodge metric, and Chern integrals as covolumes times flag degrees.
- **The sup norm of a cusp form.** The sup norm is bounded by the Petersson norm.
- **Volumes of fundamental sets.** The total volume of the fundamental sets is at most the level mass.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this branch many theorems are second names of other theorems, and some names do not match the statements. The entry says so and points to the theorem with the content.
