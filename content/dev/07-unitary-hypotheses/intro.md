---
title: Introduction
---
This volume gives the parts below [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). That chapter is about the last node of the trunk. From about sixty named statements on unitary groups and automorphic forms, the theorem `RecTExists` and a "closed bound" on families, it proves that the record `HypsAlt NL DefiniteSideCondition` is nonempty. The record then goes to [the top of the proof](/proof/trunk/) together with the window bound VWin.

The node has three branches. Branch 1 builds the record from rows (88,131 declarations). Branch 2 proves the two estimates `SurjectiveOntoX` and `LambdaLowerBound₂` (19,399). Branch 3 proves the twelve open parameter statements (12,608). The chapter explains the top of each branch. This volume gives the parts below them, one declaration in each entry. The entries follow the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Theta pair lifts.** The top of all three branches. In branch 1: the rows of `AllRowsAlt`, the service row from global Artin reciprocity, the large base lattices, and the step [`final_alt_alt`](/entry/final-alt-alt/) that turns the closed bound into `NL`. In branch 2: the map onto X and its exponent bound. In branch 3: the multiplicity condition from fourteen published inputs, and the definite side condition.
- **Flag measures.** The carrier bound for spectral ties, the nineteen hypotheses of Theorem S, and the count of automorphic forms on unitary groups from the volume step.
- **Cokernel GL counts** and **local to global.** The local cut and the count of partner lattices, from three deep inputs that hold outright.
- **Hermitian curvature** and **Hermitian curvature proofs.** Model places and the built bounds at the infinite places.
- **Satake parameters.** The service row `ServH` from six hypotheses, and the local models at constructed points.
- **Global interpolation.** The row of column valuations at bundle points, the five point laws on true chains, and the moments of kernel jets.
- **Iwasawa decomposition.** The member statement `MemberE` from the construction steps, and three Hecke facts.
- **Inertia eigenvalues** and **level letter cocycles.** The local lifting theorems A, B, C, E and T on crystalline lattices, from statements of Bloch and Kato, local Tate duality, the Euler characteristic formula, Bhatt and Scholze, and Fontaine.
- **Decorated lattice proofs.** The theta chain: each step multiplies inner products by a positive constant times a partial $L$-value, and the top theta map has an injective adjoint. Then the place laws on see-saw pins.
- **Weil bound.** The residue of the Siegel Eisenstein series at $s = t/2$, which has no hypotheses.
- **Height proofs**, **divisor proofs**, **jet harmonics** and **automorphic arithmetic.** The run bounds and the height bounds for prime data, the exponent bounds and lattice inclusions from local models, the depth bounds at good primes, and the packages at inert primes.
- **The small chapters.** Flag stabilizer tensors, abelian variety theory, Frobenius fibre curves, inert coprime lemmas, unramified integrals, twisted operators, distinguished unit ideals, automorphic spectrum, theta shift proofs, local ring cardinality and Pieri column minors. Each holds the lemmas of one Lean folder that the chapters above call. Their entries link back to their callers.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. In this volume many theorems are second names of other theorems, and many take hypotheses that they never use. Several names do not match the statements. The entry says so and points to the theorem with the content.
