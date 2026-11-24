---
title: Notes and references
decls:
  - UpperTheory.V.FW.ferreroWashington
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds two groups of results of the [modularity chapter](/entry/vwin-of-hypotheses-h-e-alt/). Sections 1 to 5 give the class group and Tate-Shafarevich inputs of the window bound: the theorem of [Ferrero and Washington](/entry/ferrero-washington/) goes to [the window bound from the hypotheses](/entry/vwin-of-hypotheses-h-e-alt/), and [Theorem B for windows](/entry/thm-bab-of-lemma-k/), [the minus part](/entry/thm-bc-free-of/) and [the character bound](/entry/iv/) go to [the window bound from four counts](/entry/of-four-alt/). Sections 6 and 7 give the [frames](/entry/frame-ex/) and the [propagation in rank three](/entry/components-good-rank-three/), which also go to [the window bound from the hypotheses](/entry/vwin-of-hypotheses-h-e-alt/). Sections 8 and 9 give the deformation inputs of the symplectic and unitary cases: [the existence of models](/entry/ex-model/) and [the trace inequality](/entry/galois-rep-ineq-of-all-irreducible-nonvanishing/) go to [the main theorem for big images](/entry/main-big/), [models for unitary groups](/entry/exists-model/) go to [the unramified one-character theorem](/entry/one-char-unram-u/), [the space of lifts](/entry/space-ex/) goes to [the rank four theorem](/entry/main4-alt/), and [block extensions](/entry/bl/) go to [the theorem on finiteness and irreducibility](/entry/fin0-no-end-all-irr-of-good-con-purity-aut/).

Section 1 proves the theorem of Ferrero and Washington in the form of a bound for the $l$-rank of class groups along the cyclotomic tower. The classical form is that the Iwasawa invariant $\mu$ of the cyclotomic $\mathbb{Z}_l$-extension of an abelian number field is $0$ (Ferrero and Washington; Washington, Chapter 7). With Iwasawa's formula for the orders of the class groups of the layers (Iwasawa 1959; Washington, Chapter 13), $\mu = 0$ is equivalent to a bound for the $l$-ranks that does not depend on the layer. The proof follows Sinnott, through the annihilation of the minus part by Stickelberger elements (Washington, Chapter 6) and a reflection theorem (Washington, Chapter 10, §10.2).

Sections 3 to 5 are the Euler system method for the minus part. The Gauss sum system is Kolyvagin's Euler system of Gauss sums, and the induction of Section 4 is Kolyvagin's argument in the form of Rubin's appendix to Lang's book. The classical form of the bound of Section 5 is that, for an odd character $\chi$ of order prime to $l$, the order of the $\chi$-eigenspace of the $l$-part of the class group of an abelian field is at most the $l$-part of a generalized Bernoulli number $B_{1, \chi^{-1}}$; Mazur and Wiles proved the equality, which is the main conjecture of Iwasawa theory over $\mathbb{Q}$ (Washington, Chapter 15). The Lean form twists by $\chi_O^{-e}$ and bounds a Tate-Shafarevich group by $B_{e+1, \psi}$, with a factor that clears the denominators. The generalized Bernoulli numbers are those of Washington, Chapter 4, §4.1. Rubin's book gives the general form of the method, with Kolyvagin systems and the bound for Selmer groups in Chapters 4 and 5.

Sections 6 and 7 are an argument by connectedness for deformation rings of polarized ordinary representations. The deformation rings are those of Mazur, whose finiteness condition $\Phi$ on the field of the kernel is used in Sections 6 and 9. The connectedness of the minimal primes of a ring cut out by few equations in a regular ring is the theorem of Hartshorne on complete intersections. The method of passing a property from one irreducible component of a deformation ring to the others through their intersections is due to Taylor, in his work on Ihara avoidance. The Lean form of Section 6 states the Euler characteristic formula of Tate as an inequality that the frame assumes; its classical source is Neukirch, Schmidt and Wingberg, Chapter VIII, §8.6.

Sections 8 and 9 are the method of Ribet. In its first form, Ribet built from a congruence between an Eisenstein series and a cusp form an irreducible Galois representation whose reduction is a nonsplit extension, and from it a class in the minus part of the class group of $\mathbb{Q}(\mu_p)$. The lattice construction of Section 9 makes such an extension. Urban used the same method for $\mathrm{GSp}_4$ and the Klingen Eisenstein ideal. The trace inequality of Section 8 is the converse direction in the form of Mazur and Wiles: a lower bound for the congruences between the reducible representation and the irreducible points, by the length of a Selmer group. The Lean form measures the congruences by the valuations of the traces at one element $g$, and it uses a model with explicit equations in place of a Hecke algebra.

- B. Ferrero and L. C. Washington, The Iwasawa invariant $\mu_p$ vanishes for abelian number fields, Ann. of Math. (2) 109 (1979), 377 to 395.
- R. Hartshorne, Complete intersections and connectedness, Amer. J. Math. 84 (1962), 497 to 508.
- K. Iwasawa, On $\Gamma$-extensions of algebraic number fields, Bull. Amer. Math. Soc. 65 (1959), 183 to 226.
- V. A. Kolyvagin, Euler systems, in The Grothendieck Festschrift, Vol. II, Progr. Math. 87, Birkhäuser, 1990, 435 to 483.
- S. Lang, Cyclotomic Fields I and II, combined 2nd ed., Grad. Texts in Math. 121, Springer, 1990, with an appendix by K. Rubin.
- B. Mazur, Deforming Galois representations, in Galois Groups over $\mathbb{Q}$, Math. Sci. Res. Inst. Publ. 16, Springer, 1989, 385 to 437.
- B. Mazur and A. Wiles, Class fields of abelian extensions of $\mathbb{Q}$, Invent. Math. 76 (1984), 179 to 330.
- J. Neukirch, A. Schmidt and K. Wingberg, Cohomology of Number Fields, 2nd ed., Grundlehren Math. Wiss. 323, Springer, 2008, Chapter VIII.
- K. Ribet, A modular construction of unramified $p$-extensions of $\mathbb{Q}(\mu_p)$, Invent. Math. 34 (1976), 151 to 162.
- K. Rubin, Euler Systems, Ann. of Math. Stud. 147, Princeton University Press, 2000, Chapters 4 and 5.
- W. Sinnott, On the $\mu$-invariant of the $\Gamma$-transform of a rational function, Invent. Math. 75 (1984), 273 to 282.
- R. Taylor, Automorphy for some $l$-adic lifts of automorphic mod $l$ Galois representations. II, Publ. Math. Inst. Hautes Études Sci. 108 (2008), 183 to 239.
- E. Urban, Selmer groups and the Eisenstein-Klingen ideal, Duke Math. J. 106 (2001), 485 to 525.
- L. C. Washington, Introduction to Cyclotomic Fields, 2nd ed., Grad. Texts in Math. 83, Springer, 1997, Chapters 4, 6, 7, 10, 13 and 15.
