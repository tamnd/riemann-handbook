---
title: Notes and references
decls:
  - GlobalTheory.T.exists_isAt_of_placed_framed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds item 7 of the step [the hypotheses are not empty](/step/nonempty-hyps/), and through it branch 3 of [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). Both use the main theorem of Section 1, [the open parameter statements](/entry/open0-of-unitary-group-hypotheses/), with its proof [the open parameter statements of the parameter set of dependence](/entry/open-orbit-of-unramified-exponents-alt/). Ten of its twelve rows come from other chapters. The defect row is proved in Section 18 and the label row in Section 19. The multiplicity row is the long chain. Section 2 reduces it to the period identity for a true package of Section 3. Section 3 reduces that to the family conditions of Section 4 and the period identity of Section 16. Sections 5 to 15 build the inputs of the family conditions, and Section 17 makes the true packages from the bundle witnesses. All published inputs are taken from [the literature](/proof/literature/), and the list in Section 1 names them.

Section 1 is a bookkeeping argument: each row is proved from earlier rows and from a sublist of the published statements. The statements that matter most for this chapter are older than the chapter. The Casselman-Wallach theorem on smooth globalization is due to Casselman (1989) and Wallach (1992, Chapter 11). The finiteness theorem and the classification of the discrete series are Harish-Chandra (1966, 1968). The rapid decay of cusp forms on Siegel sets is in Harish-Chandra's notes (1968, Chapter I) and in Moeglin and Waldspurger (1995, Chapter I). The factorization of smooth vectors is Dixmier and Malliavin (1978). The unramified Howe duality, which step 4 takes from another chapter, goes back to Howe (1979, 1989).

Section 2 passes from rows that hold at all points to rows that hold eventually, by the filter argument of the rows of [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/). The period identity it asks for is a global identity between a period of theta vectors and a product of local data. Its background is the Gross-Prasad conjecture, from Gross and Prasad (1992) for orthogonal groups and from Gan, Gross and Prasad (2012) for all classical groups, and its refined form with local factors, from Ichino and Ikeda (2010) and, for unitary groups, from N. Harris (2014). The chapter does not prove these conjectures. It proves one identity of this shape for the packages it builds. The diagonal row of the multiplicity theorem uses a second form of the convergence of the Siegel-Weil integral. Weil (1965) proved the convergence and the formula in his range. Kudla and Rallis (1994) gave the regularized form for symplectic and orthogonal pairs, and Ichino (2004) gave it for unitary groups. See [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

Section 3 uses the Weil representation of a unitary dual pair. Weil (1964) built it, and Kudla (1994) split the metaplectic cover over unitary pairs, so that the representation is linear on the unitary groups. See [the Weil representation](/learn/theta/#the-weil-representation). The doubling method of the published list is from Piatetski-Shapiro and Rallis, in Gelbart, Piatetski-Shapiro and Rallis (1987, Part A). See [the doubling method](/learn/theta/#the-doubling-method).

Section 4 assembles the family conditions from four constructions. Of the published inputs it takes, strong approximation for the special unitary group is the theorem of Kneser and Platonov for simply connected groups (Platonov and Rapinchuk 1994, Chapter 7). See [strong approximation](/learn/groups/#strong-approximation). The other three inputs enter through Sections 9, 10 and 13.

Sections 5, 11 and 12 work with Bessel data on the space $X_0$. A Bessel datum here is a vector, an embedding of unitary groups and a frame. These are the data of the Bessel models of Gan, Gross and Prasad (2012), which generalize the restriction problem of Gross and Prasad (1992). The uniqueness of these models over a nonarchimedean field rests on the multiplicity one theorem of Aizenbud, Gourevitch, Rallis and Schiffmann (2010), and over the real numbers on that of Sun and Zhu (2012), and Gan, Gross and Prasad (2012) reduce the general Bessel case to these. The chapter does not use the uniqueness theorem. The comparison of two translates in Sections 5 and 12 is internal: two placed framed data are compared through the level set $J_W$ and the centre of $G_f(X_0)$.

Sections 6, 7 and 8 build the local data at the places of a twist set. The local quadratic extension and its characters at each place are the setting of local class field theory (Neukirch 1999, Chapter V). The rescaling of Section 7 uses the place laws of a seesaw. Seesaw pairs are due to Kudla (1984). See [seesaw pairs](/learn/theta/#seesaw-pairs). The volumes of Section 8 are indices of compact open subgroups, read through a reduction map, and the argument is internal.

Sections 9 and 10 build the column side and the link conditions. They use the discrete series cover and the Harish-Chandra modules, from Harish-Chandra (1966) and the globalization of Casselman (1989) and Wallach (1992, Chapter 11). Section 10 also uses strong approximation (Platonov and Rapinchuk 1994, Chapter 7).

Section 13 builds the geometric family at a point. Its vacuum vectors and line vectors are vectors of the Weil representation (Weil 1964). See [the Fock model](/learn/theta/#the-fock-model). Section 14 chooses the lattices and the frames. Lattices in hermitian spaces over local fields are classified by the methods of O'Meara (1963, Chapter VIII) for quadratic forms, and by Shimura (1964) for unitary groups. See [hermitian lattices](/learn/groups/#hermitian-lattices-and-the-mass-formula). Section 15 checks the clauses of a placed datum. Its proof turns the level group conditions into lattice conditions place by place, and uses that a lattice is fixed by an element exactly when its completions are.

Section 16 proves the period identity from the family conditions. The theta vectors of the proof are global theta lifts, and the classification of the discrete series (Harish-Chandra 1966) and the rapid decay of cusp forms (Harish-Chandra 1968, Chapter I) are its published inputs. See [the global theta lift](/learn/theta/#the-global-theta-lift). Section 17 is internal: a bundle witness and the point conditions give a true package.

Section 18 proves the defect row, the row form of [the definite side condition](/step/definite-side-condition-def/). Its published inputs are the Weil representation (Weil 1964), the existence of discrete series and the finiteness theorem (Harish-Chandra 1966, 1968), and the rapid decay of cusp forms.

Section 19 proves the label row. The green statement is a statement on the characters of the finite general linear groups, whose classification is due to Green (1955). The polynomial ring of Zelevinsky is the Hopf algebra of the representations of all $\mathrm{GL}_n(\mathbb{F}_q)$ (Zelevinsky 1981), modelled on the ring of Bernstein and Zelevinsky (1977) for $p$-adic groups. The type labels of the proof use global Artin reciprocity (Neukirch 1999, Chapter VI).

- A. Aizenbud, D. Gourevitch, S. Rallis and G. Schiffmann, Multiplicity one theorems, Ann. of Math. 172 (2010), 1407 to 1434.
- J. Bernstein and A. V. Zelevinsky, Induced representations of reductive $p$-adic groups I, Ann. Sci. École Norm. Sup. 10 (1977), 441 to 472.
- W. Casselman, Canonical extensions of Harish-Chandra modules to representations of $G$, Canad. J. Math. 41 (1989), 385 to 438.
- J. Dixmier and P. Malliavin, Factorisations de fonctions et de vecteurs indéfiniment différentiables, Bull. Sci. Math. 102 (1978), 307 to 330.
- W. T. Gan, B. H. Gross and D. Prasad, Symplectic local root numbers, central critical $L$-values, and restriction problems in the representation theory of classical groups, Astérisque 346 (2012), 1 to 109.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254, Springer, 1987, Part A.
- J. A. Green, The characters of the finite general linear groups, Trans. Amer. Math. Soc. 80 (1955), 402 to 447.
- B. H. Gross and D. Prasad, On the decomposition of a representation of $\mathrm{SO}_n$ when restricted to $\mathrm{SO}_{n-1}$, Canad. J. Math. 44 (1992), 974 to 1002.
- Harish-Chandra, Discrete series for semisimple Lie groups II, Acta Math. 116 (1966), 1 to 111.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Springer, 1968, Chapter I.
- R. N. Harris, *The refined Gross-Prasad conjecture for unitary groups*, Int. Math. Res. Not. IMRN 2014, no. 2, 303 to 389.
- R. Howe, $\theta$-series and invariant theory, in *Automorphic Forms, Representations and L-Functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 275 to 285.
- R. Howe, Transcending classical invariant theory, J. Amer. Math. Soc. 2 (1989), 535 to 552.
- A. Ichino, A regularized Siegel-Weil formula for unitary groups, Math. Z. 247 (2004), 241 to 277.
- A. Ichino and T. Ikeda, On the periods of automorphic forms on special orthogonal groups and the Gross-Prasad conjecture, Geom. Funct. Anal. 19 (2010), 1378 to 1425.
- S. S. Kudla, Seesaw dual reductive pairs, in *Automorphic Forms of Several Variables*, Progr. Math. 46, Birkhäuser, 1984, 244 to 268.
- S. S. Kudla, Splitting metaplectic covers of dual reductive pairs, Israel J. Math. 87 (1994), 361 to 401.
- S. S. Kudla and S. Rallis, A regularized Siegel-Weil formula: the first term identity, Ann. of Math. 140 (1994), 1 to 80.
- C. Moeglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Cambridge Tracts in Math. 113, Cambridge Univ. Press, 1995, Chapter I.
- J. Neukirch, *Algebraic Number Theory*, Grundlehren Math. Wiss. 322, Springer, 1999, Chapters V and VI.
- O. T. O'Meara, *Introduction to Quadratic Forms*, Grundlehren Math. Wiss. 117, Springer, 1963, Chapter VIII.
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Pure Appl. Math. 139, Academic Press, 1994, Chapter 7.
- G. Shimura, Arithmetic of unitary groups, Ann. of Math. 79 (1964), 369 to 409.
- B. Sun and C.-B. Zhu, Multiplicity one theorems: the Archimedean case, Ann. of Math. 175 (2012), 23 to 44.
- N. R. Wallach, *Real Reductive Groups II*, Pure Appl. Math. 132-II, Academic Press, 1992, Chapter 11.
- A. Weil, Sur certains groupes d'opérateurs unitaires, Acta Math. 111 (1964), 143 to 211.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), 1 to 87.
- A. V. Zelevinsky, *Representations of Finite Classical Groups: a Hopf Algebra Approach*, Lecture Notes in Math. 869, Springer, 1981.

**Remark 4.20.1 (Formalization).** The declaration listed for this section is the statement form of [the Theorem on translates](/entry/exists-is-at-of-placed-framed/) of Section 5, at [ExistsIsAtStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAtStatement.lean#L22). None of the classical theorems named above is proved in the Lean development. Each enters as a hypothesis, under the name of a published statement, and the chapter passes these hypotheses from theorem to theorem. The lemma `localBesselMultiplicityOne` used in Section 19 does not state the theorem of Aizenbud, Gourevitch, Rallis and Schiffmann or that of Sun and Zhu: it concludes type labels.
