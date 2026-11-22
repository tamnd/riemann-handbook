---
title: Introduction
---
This volume is the Galois row: the branch of the proof below the theorem `galoisLocalGlobalStrong_recParameter`. The trunk needs one hypothesis from it, the statement [Row0b](/step/row0b-def/) with the local condition [IsRecT](/step/is-rect-def/). It says that each regular algebraic polarized cuspidal representation $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$, for a CM field $E$, has an $\ell$-adic Galois representation $\rho_\pi$, and that $\rho_\pi$ matches $\pi$ at each place under the local Langlands correspondence. [Volume 2](/proof/galois-row/) gives the top of the proof. This volume gives the parts below it, one declaration in each entry.

The branch has 51,591 declarations. Their order here follows the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Galois representations.** The main line. The row comes from theta lifts ([the step](/step/galois-representations-of-theta-lift/)) and from a geometric statement, the Galois row in weight one ([GeoOne](/step/geo-one-def/)). GeoOne is proved from the cohomology of a tower of Shimura varieties: the local steps (Eichler-Shimura, crystalline comparison, Hodge-Tate weights), the Hodge cohomology of a tower of Kuga-Sato varieties and a holomorphic Lefschetz formula. The chapter ends with local-global compatibility at places with Iwahori level and the Siegel-Weil formulas that the theta lift uses.
- **Étale cohomology**, in two chapters from two Lean folders: finiteness and duality, the trace isomorphism, proper base change, and the Frobenius step of the crystalline comparison.
- **Weil bound.** One entry from that Lean folder: a bijection of Hodge-Tate weights used by the comparison of crystalline and semistable representations.
- **Divisor proofs.** The projective bundle formula, and the families of abelian varieties with level structure that make the tower: their existence as quasi-projective schemes and the representability of the moduli problems.
- **Abelian variety theory** and **étale clopen descent.** The Lefschetz fixed point formula for finite étale correspondences, in the forms that prove the hypothesis of [the main theorem of the first chapter](/entry/geometric-realization-of-weight-one/), and the lifting of charts along finite covers.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Where a Lean statement is weaker than the standard theorem, or a proof only passes a hypothesis along, the entry says so.
