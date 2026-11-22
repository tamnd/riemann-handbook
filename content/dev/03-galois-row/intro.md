---
title: Introduction
---
This volume is the Galois row: the branch of the proof below the theorem `galoisLocalGlobalStrong_recParameter`. The trunk needs one hypothesis from it, the statement [Row0b](/step/row0b-def/) with the local condition [IsRecT](/step/is-rect-def/). It says that each regular algebraic polarized cuspidal representation $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$, for a CM field $E$, has an $\ell$-adic Galois representation $\rho_\pi$, and that $\rho_\pi$ matches $\pi$ at each place under the local Langlands correspondence. [Volume 2](/proof/galois-row/) gives the top of the proof. This volume gives the parts below it, one declaration in each entry.

The branch has 51,591 declarations. Their order here follows the proof from the top down. In each chapter, the larger subtree comes first.

The chapters:

- **Galois representations.** The main line. The row comes from theta lifts ([the step](/step/galois-representations-of-theta-lift/)) and from a geometric statement, the Galois row in weight one ([GeoOne](/step/geo-one-def/)). GeoOne is proved from the cohomology of a tower of Shimura varieties: the local steps (Eichler-Shimura, crystalline comparison, Hodge-Tate weights), the Hodge cohomology of a tower of Kuga-Sato varieties and a holomorphic Lefschetz formula. Then the congruences that cut a representation down to the generic part, the Weil representation of a unitary dual pair, and the Siegel-Weil formulas that the theta lift uses.
- **Étale cohomology.** Finiteness and duality, the trace isomorphism, proper base change and Gabber's affine analogue for henselian pairs, and the Frobenius relation of the crystalline comparison.
- **Étale sheaves.** The cup product with coefficients $\mathbb{Z}/q(i)$: it is associative, has a unit, and commutes with pullback, as do the Chern and Kummer classes.
- **p-adic Hodge comparison.** The Hodge-Tate pairing and its injectivity, the Hodge isomorphism by Čech maps, the nonvanishing of $c^d$ for a de Rham Chern class, and crystalline descent along the Teichmüller lifts.
- **Divisor proofs.** The largest chapter. The projective bundle formula. Triviality of $\mathbb{Z}/q$-torsors over a strict henselisation and the Picard group of its generic fibre. The moduli schemes of the tower: Siegel objects classified over affine, noetherian, complete and Artinian bases, the finite scheme of adjoint ring actions, polarized homomorphisms, Harris-Taylor isogenies and the universal first-order deformation. Characteristic polynomials on de Rham homology.
- **Étale clopen descent** and **automorphic arithmetic.** The projective bundle formula for the trivial bundle, by induction on the rank, and the Lefschetz fixed point formula for finite étale correspondences. The scheme of clopen subgroups of a finite étale group, the count of marked fixed points, and the basic facts on the period rings.
- **Adelic lattice proofs.** Finiteness of class numbers, from finiteness of double cosets for a rational subgroup of SL.
- **Frames, charts and fixed points.** Breuil-Kisin frames for semistable lattices with bounded Hodge-Tate jumps, and the second names of the chart lift and of the Lefschetz formula.
- **Division in compact groups.** The statement `DivWCoreLac`, which gives the lacunary element that the Galois representations chapter uses to cut a representation.

An entry tells what the declaration says in standard mathematics, how the Lean proof goes, and what is odd in the Lean code. Where a Lean statement is weaker than the standard theorem, or a proof only passes a hypothesis along, the entry says so. Many names here do not match their statements: for example, a family of thirteen lemmas is called `intersectionNumber_baseChange` and none of them is about intersection numbers. On schemes, the projective bundle formula in the code covers only the trivial bundle.
