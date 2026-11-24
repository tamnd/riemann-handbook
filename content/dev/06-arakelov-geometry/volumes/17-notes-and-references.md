---
title: Notes and references
decls:
  - GlobalTheory.T.good_tower_volume_theorem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter proves the volume theorem for good root towers and three groups of results around it. The volume theorem, with the existence of good towers from [the chapter on good towers](/entry/good-tower-volume-of-reduced/), is the volume part of Step 4 of [the Weil bound](/proof/weil-bound/): it gives the lower bound for the mean slope with one constant along every tower. The deep statement on mean slopes of the last section feeds the [self-intersection and volume estimate](/entry/top-covol-slim2-use-alt-alt/) and the [deep statement for volumes](/entry/deep-st-r-of-volume/). The mass bound feeds the [local volume factor](/entry/tamagawa-local-volume-factor/), and the finite covolume of the adelic quotient feeds the [finiteness statement](/entry/adelic-covolume-finite/). For the background see [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles), [arithmetic varieties and intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers), [heights](/learn/arakelov/#heights), [arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness), [hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes) and [the Hodge bundle](/learn/arakelov/#the-hodge-bundle-and-zarhins-trick).

**Weights, flag degrees and the tower conditions.** The intersection numbers of hermitian line bundles on arithmetic varieties go back to Arakelov for arithmetic surfaces and to Faltings, who added the Riemann-Roch theorem and the Noether formula in that setting. Gillet and Soulé extended the theory to all dimensions with arithmetic Chow groups, and their arithmetic Riemann-Roch theorem is the source of the comparison of degrees with volumes. The equality of the flag degree with the integral of the top power of the Chern form is a case of the classical statement that the degree of an ample line bundle is the volume of its curvature form. The conditions of the second section (proportionality, nefness, semipositivity, the height bounds) are in the form used by Zhang for positive line bundles, and the antisymmetry is our reading of the symmetry of the arithmetic intersection pairing.

**The remainder, the base lower bound and the chain.** The power sum formula and the remainder over the primes are local computations, one prime at a time, and the bound for the remainder does not depend on the primes. The chain of tower estimates is a combination of the successive minima inequalities and the arithmetic Hilbert-Samuel formula. The successive minima inequalities for heights of points against the height of the variety are due to Zhang. The arithmetic Hilbert-Samuel formula is due to Gillet and Soulé, with the version for semipositive metrics of Abbes and Bouche. The heights of subvarieties are those of Bost, Gillet and Soulé.

**Height bounds for points and reference towers.** The bounds I5 and I6 reduce to a local sandwich of the Hodge component at each bad prime. The local input is a comparison theorem for Hodge-Tate lattices, which the chapter takes as given from the chapter on good towers; we do not give a reference for its proof here. The reference towers and the bound I1 compare two integral models of the same variety in common coordinates. The same idea, that two models differ by vertical terms at finitely many primes, is in the comparison of heights under isogeny of Faltings.

**Constant sections, flat root lines and Frobenius links.** The flat degree of the third group is a degree of a hermitian line with a flat section, so it is a sum of local terms and a value of a logarithmic derivative of an $L$-function; in this shape it is close to the Chowla-Selberg formula, but the chapter proves its statement only in the form it needs. The theory of complex multiplication used for the CM types and the reflex field is in Shimura's book.

**Uniformization and equal volumes.** The uniformization of the complex points of a unitary Shimura variety by products of complex balls is the classical description of the analytic space of a Shimura variety as a finite union of arithmetic quotients; GAGA, in the form of Serre, identifies the analytic and the algebraic objects. The comparison of a geometric degree with a ball volume is a case of the proportionality theorem of Hirzebruch, extended by Mumford to the noncompact case. The integral models and their compactifications are those of Faltings and Chai for Siegel varieties and of Lan for PEL type.

**The volume theorem.** The volume theorem is the assembly of the previous sections. The uniformity of the constant in the field, the datum and the level is what the Weil bound needs; it comes from the fact that every input is bounded by the root discriminant and the logarithmic derivative of the $L$-function of the host.

**The mass of the components.** The volumes of arithmetic quotients of semisimple groups are computed by the Siegel mass formula and in general by Prasad's volume formula. The Riemannian volume of the compact group, against which the Haar measure is normalised, is the formula of Macdonald. Gross gives the motive of a reductive group and the form of the mass in terms of special values of $L$-functions. The chapter does not use these exact formulas: it proves an explicit upper bound with a packing argument in tubes around a fundamental domain, and the constants are not optimal.

**Finite adelic covolume.** The finiteness of the covolume of an arithmetic group in a semisimple group is the theorem of Borel and Harish-Chandra. The passage between adelic quotients and finite unions of arithmetic quotients by a double coset decomposition is standard, see Weil's book on adeles. The dictionary between finite adelic points of a unitary group and hermitian lattices is the local to global principle for lattices.

**Bigness and the Hilbert-Samuel inputs.** The bound of the self-intersection of a nef hermitian line bundle by its arithmetic volume is a consequence of the continuity of the arithmetic volume of Moriwaki and of the bigness criterion of Yuan. The arithmetic Fujita approximation of Chen and of Yuan gives the volume as a limit of self-intersections. The absolute Siegel lemma is in the form of Bombieri and Vaaler, with the slopes of hermitian lattices of Bost and Chen. Resolution of singularities in characteristic zero is the theorem of Hironaka. Moriwaki's book collects the Arakelov theory of the chapter in one place.

- S. J. Arakelov, *Intersection theory of divisors on an arithmetic surface*, Izv. Akad. Nauk SSSR Ser. Mat. 38 (1974), 1179 to 1192.
- G. Faltings, Calculus on arithmetic surfaces, Ann. of Math. 119 (1984), 387 to 424.
- G. Faltings, Endlichkeitssätze für abelsche Varietäten über Zahlkörpern, Invent. Math. 73 (1983), 349 to 366.
- H. Gillet and C. Soulé, Arithmetic intersection theory, Publ. Math. IHÉS 72 (1990), 93 to 174.
- H. Gillet and C. Soulé, An arithmetic Riemann-Roch theorem, Invent. Math. 110 (1992), 473 to 543.
- J.-B. Bost, H. Gillet and C. Soulé, Heights of projective varieties and positive Green forms, J. Amer. Math. Soc. 7 (1994), 903 to 1027.
- A. Abbes and T. Bouche, Théorème de Hilbert-Samuel « arithmétique », Ann. Inst. Fourier 45 (1995), 375 to 401.
- S. Zhang, Positive line bundles on arithmetic varieties, J. Amer. Math. Soc. 8 (1995), 187 to 221.
- S. Zhang, Small points and adelic metrics, J. Algebraic Geom. 4 (1995), 281 to 296.
- X. Yuan, Big line bundles over arithmetic varieties, Invent. Math. 173 (2008), 603 to 649.
- A. Moriwaki, Continuity of volumes on arithmetic varieties, J. Algebraic Geom. 18 (2009), 407 to 457.
- A. Moriwaki, *Arakelov Geometry*, Transl. Math. Monogr. 244, Amer. Math. Soc., 2014.
- H. Chen, *Arithmetic Fujita approximation*, Ann. Sci. Éc. Norm. Supér. (4) 43 (2010), 555 to 578.
- E. Bombieri and J. Vaaler, On Siegel's lemma, Invent. Math. 73 (1983), 11 to 32.
- G. Shimura, *Abelian Varieties with Complex Multiplication and Modular Functions*, Princeton Univ. Press, 1998.
- J.-P. Serre, Géométrie algébrique et géométrie analytique, Ann. Inst. Fourier 6 (1956), 1 to 42.
- D. Mumford, Hirzebruch's proportionality theorem in the non-compact case, Invent. Math. 42 (1977), 239 to 272.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergeb. Math. Grenzgeb. (3) 22, Springer, 1990, Chapters IV and V.
- K.-W. Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, London Math. Soc. Monogr. 36, Princeton Univ. Press, 2013, Chapter 6.
- A. Borel and Harish-Chandra, Arithmetic subgroups of algebraic groups, Ann. of Math. 75 (1962), 485 to 535.
- G. Prasad, Volumes of S-arithmetic quotients of semi-simple groups, Publ. Math. IHÉS 69 (1989), 91 to 117.
- I. G. Macdonald, The volume of a compact Lie group, Invent. Math. 56 (1980), 93 to 95.
- B. H. Gross, On the motive of a reductive group, Invent. Math. 130 (1997), 287 to 313.
- A. Weil, *Adeles and Algebraic Groups*, Progr. Math. 23, Birkhäuser, 1982.
- H. Hironaka, Resolution of singularities of an algebraic variety over a field of characteristic zero, Ann. of Math. 79 (1964), 109 to 203 and 205 to 326.
