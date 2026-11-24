---
title: Notes and references
decls:
  - GlobalTheory.Unf.unfoldings_of_chain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The results of this chapter feed three steps of [the Bessel seesaw proof](/proof/bessel-seesaw/). The unfolding laws of the [Theorem on chains](/entry/unfoldings-of-chain/), with the [evaluation form](/entry/eval-bf-of-descent/) of the Bessel unfolding, are the input of [the row chain unfolding](/entry/iter-chain/), and through it of the step [the nonempty hypotheses](/step/nonempty-hyps/). The local flat maps at split places ([Fourier-Jacobi to Bessel](/entry/flat-fb-holds/) and [Bessel to Fourier-Jacobi](/entry/flat-bf-of-laws/)), the [archimedean facts on record](/entry/arch-on-record-closed/) and the [standard form at an inert place](/entry/std-cayley-of-inert/) compute the local factors of the unfolded periods in the same step. The archimedean facts rest on two results of the literature, the classification of the discrete series with the Blattner properties and the theory of Harish-Chandra modules. The [mixed model formulas](/entry/mixed-source/) and the [value at the origin](/entry/value-at-origin/) are used in all the unfoldings. The [quantitative Mahler criterion](/entry/ht-min-of-reduced/) gives the growth bound near the cusps in the step [every character of the row](/step/every-character-of-row/).

### The Weil representation and its mixed models

The Weil representation goes back to Weil (1964), who built it for the metaplectic cover of a symplectic group over a local field and over the adeles. The Schrödinger model, the mixed models attached to a polarization of one factor of a dual pair, and the formulas for the action of a Levi factor and of a unipotent radical are in Chapter 2 of Mœglin, Vignéras and Waldspurger (1987). For unitary dual pairs the Weil representation depends on a choice of splitting characters $\chi_S$ and $\chi_T$; Kudla (1994) gave the splittings, and Harris, Kudla and Sweet (1996) used them for the theta correspondence of unitary groups. The value of the Levi factor at the origin, $|\det a|^{\dim T/2}\chi_T(\det a)$ in the classical normalization, is the formula of these sources. In this chapter the Weil datum is an abstract family of operators that satisfies these formulas, so the formulas are hypotheses on the datum and the theorems derive the consequences that the chain needs. See [the Weil representation](/learn/theta/#the-weil-representation) and [the Heisenberg and metaplectic groups](/learn/groups/#the-heisenberg-and-metaplectic-groups).

### Seesaw pairs and periods

Seesaw dual pairs were introduced by Kudla (1984). If $U(V_0) \supset U(A) \times U(L)$ and $U(S) \times U(S) \supset U(S)$ form a seesaw, the theta kernel of the larger pair restricts to a product of theta kernels, and an inner product of a theta lift against a function on the small group becomes an inner product of the other kind. The last seesaw identity of Section 3 is the pointwise form of this statement for theta kernels.

The Bessel and Fourier-Jacobi periods in the form used here are those of Gan, Gross and Prasad (2012). Unfolding a Bessel period of a theta lift into a Fourier-Jacobi period, and the other way round, is the method of the descent of Ginzburg, Rallis and Soudry (1999), and the use of these unfoldings for the nonvanishing of periods is in Ginzburg, Jiang and Rallis (2004). The factorization of the global periods into local integrals is the subject of Ichino and Ikeda (2010) for orthogonal groups. The local flat maps of Section 4 are the local forms of the unfolding at a split place, where the unitary group is a general linear group and the Weil representation is the natural action on Schwartz functions. See [the descent of Ginzburg, Rallis and Soudry](/learn/periods/#the-descent-of-ginzburg-rallis-and-soudry).

### Local inputs

The archimedean facts are the vanishing of the early theta lifts in a tower and the identification of the first occurrence, as in Rallis (1984), together with the results on the lowest $K$-type of a theta lift, which use Howe (1989), the classification of the discrete series by Harish-Chandra (1966) and Blattner's formula of Hecht and Schmid (1975). The Cayley rule at an inert place is the computation of a vacuum matrix coefficient in the lattice model, see [the Fock model](/learn/theta/#the-fock-model) and [lattices in quadratic and Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

### Mahler's criterion

Mahler's compactness theorem is in Mahler (1946); Chapter V of Cassels (1959) gives the theorem with the reduced bases in the form used in Section 6. The passage from lattices to an arithmetic subgroup of a reductive group, with finitely many classes of bounded type, is the reduction theory of Borel and Harish-Chandra (1962). The quantitative form, with an explicit power $t^{b}$, follows from the proof of Mahler's theorem: the vectors of a reduced basis have lengths bounded by a power of the inverse of the shortest length.

### Sources

- Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), 143 to 211.
- Mœglin, Vignéras and Waldspurger, *Correspondances de Howe sur un corps $p$-adique*, Lecture Notes in Math. 1291, Springer, 1987, Chapter 2.
- Kudla, *Seesaw dual reductive pairs*, in Automorphic Forms of Several Variables, Progr. Math. 46, Birkhäuser, 1984, 244 to 268.
- Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), 361 to 401.
- Harris, Kudla and Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), 941 to 1004.
- Gan, Gross and Prasad, *Symplectic local root numbers, central critical L-values, and restriction problems in the representation theory of classical groups*, Astérisque 346 (2012), 1 to 109.
- Ginzburg, Rallis and Soudry, *On explicit lifts of cusp forms from $\mathrm{GL}_m$ to classical groups*, Ann. of Math. 150 (1999), 807 to 866.
- Ginzburg, Jiang and Rallis, *On the nonvanishing of the central value of the Rankin-Selberg L-functions*, J. Amer. Math. Soc. 17 (2004), 679 to 722.
- Ichino and Ikeda, *On the periods of automorphic forms on special orthogonal groups and the Gross-Prasad conjecture*, Geom. Funct. Anal. 19 (2010), 1378 to 1425.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), 1 to 111.
- Hecht and Schmid, *A proof of Blattner's conjecture*, Invent. Math. 31 (1975), 129 to 154.
- Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989), 535 to 552.
- Rallis, *On the Howe duality conjecture*, Compositio Math. 51 (1984), 333 to 399.
- Cassels, *An Introduction to the Geometry of Numbers*, Springer, 1959, Chapter V.
- Mahler, *On lattice points in $n$-dimensional star bodies I*, Proc. Roy. Soc. London Ser. A 187 (1946), 151 to 187.
- Borel and Harish-Chandra, *Arithmetic subgroups of algebraic groups*, Ann. of Math. 75 (1962), 485 to 535.

**Remark 7.7.1 (Formalization).** The declaration listed for this file is the one of Section 3; it is listed again because it is the root of the chain that the notes above describe. Several statements of the chapter take their hypotheses as Prop-valued fields of a structure, so a reader who checks a statement against the classical one must read the structure as part of the statement.
