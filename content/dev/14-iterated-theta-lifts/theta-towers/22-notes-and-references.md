---
title: Notes and references
decls:
  - GlobalTheory.T.rallis_inner_product_big_theta_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds the step [the hypotheses are not empty](/step/nonempty-hyps/). The separation of rows of Section 7 is its first item, [the separation of rows from Howe duality and Siegel-Weil](/entry/functionals-separate-of-howe-unram-of-siegel-weil/). The row properties of Section 6, [the row properties of the twisted lifts](/entry/theta-lift-row-properties-conj/), enter its second and third items, and they rest on Sections 1 to 5 (cusp forms, approximation by Fock vectors, unfolding and the flip of paths) and on Sections 16, 18 and 19 (the basic properties of theta kernels, the field of class sums and the dictionary of moved jets). The third item ends with [the fit of constant functions](/entry/fourier-coefficient-fit-of-join-alt/) of Section 9, which joins the norm formulas of Section 8, the sizes of Section 12 and [the tower of square constants](/entry/tower-alt-bis/) of Sections 14, 15 and 17. Sections 20 and 21 prove local and global inputs that the same step lists among its hypotheses: the local matching of squares, the nonvanishing at the first occurrence, the cuspidality of lifts, the second order term of the Lie action, a regulariser, frames at the real places and the ties of the class sums.

The Weil representation of the chapter is that of A. Weil (1964), who constructed it as a representation of the metaplectic cover of the symplectic group and proved that the theta distribution is invariant under the rational points. For a dual pair of unitary groups the cover splits over the two groups, once characters $\chi_X$ and $\chi_W$ are fixed; this is the splitting of Kudla, and the exponent $m$ of the splitting at a real place is the exponent that appears in the second order term of Section 21. The moderate growth and the invariance of theta kernels in Section 16 are the classical starting point of the theory of the global theta lift: for $\varphi$ in the Schwartz space of $X \otimes W$ and a cusp form $f$ on $U(W)$,

$$\theta(f, \varphi)(g) = \int_{U(W)(F) \backslash U(W)(\mathbb A)} \theta_\varphi(g, h)\, \overline{f(h)}\, dh$$

converges and is an automorphic form on $U(X)$.

Howe duality enters in two forms. In its classical local form, for a dual pair $(G, G')$ in a symplectic group and an irreducible representation $\pi$ of $G$ that is a quotient of the Weil representation $\omega$, the maximal $\pi$-isotypic quotient of $\omega$ is $\pi \otimes \Theta(\pi)$, where $\Theta(\pi)$ has a unique irreducible quotient $\theta(\pi)$, and $\pi \mapsto \theta(\pi)$ is injective. The unramified case, used in Section 7, is due to Howe (1979), with the explicit correspondence of Satake parameters computed by Rallis (1982). The archimedean case, used in Sections 9 and 20 in the form of a condition on the coinvariants of the polynomial Fock space, is Howe (1989); there the Fock space and the Harish-Chandra modules replace smooth representations. The local matching of squares in Section 20 is the global consequence: a common quotient of two Weil representations factors as a real quotient times a finite part. The commutant argument in its proof is the lemma of Dixmier that an endomorphism of an irreducible module of countable dimension that commutes with the action is a scalar.

The Siegel-Weil formula of Section 7 is, in its classical form, the identity

$$E(g, s_0, \Phi_\varphi) = \kappa \int_{U(X)(F) \backslash U(X)(\mathbb A)} \theta_\varphi(g, h)\, dh$$

between the Siegel Eisenstein series of the section attached to $\varphi$ and the integral of the theta kernel, with $\kappa = 1$ or $2$. Weil (1965) proved it in his range of convergence; Kudla and Rallis (1994) extended it to a regularized form for symplectic and orthogonal pairs, and Ichino (2004) to unitary groups. The regulariser of Section 21 is the device of Kudla and Rallis: a Hecke operator at one good place that kills the terms of the theta integral that do not decay.

The Rallis inner product formula of Sections 8 and 21 states that the Petersson norm of a theta lift is a value of a standard $L$-function times local zeta integrals:

$$\langle \theta(f, \varphi), \theta(f, \varphi') \rangle = c\, L^S(s_0 + \tfrac12, \pi)\, \prod_{v \in S} Z_v(s_0, \varphi_v, \varphi'_v).$$

It comes from the doubling method together with the Siegel-Weil formula, and is due to Rallis (1984), who used it to prove that the first nonzero lift in a Witt tower of a cusp form is cuspidal and that the lifts higher in the tower do not vanish. The nonvanishing at the first occurrence in Section 21 and the step of the tower in Section 17 are the forms of these facts that the chapter uses; on a definite bottom the integrals converge without regularization. For unitary groups the local factors at the real places and the signs that decide which tower carries the first occurrence are studied by Harris, Kudla and Sweet (1996).

The Hecke $L$-functions of the chapter are those of Hecke (1918, 1920) for Grössencharaktere, in the adelic form of Tate's thesis: for a Hecke character $\nu$ of $E$, the complete $L$-function $\Lambda(s, \nu)$ has a meromorphic continuation and a functional equation with a root number that is a product of local epsilon factors. The partial $L$-function $L^{S_0}(s, \nu)$ of Section 17 differs from $\Lambda(s, \nu)$ by the finitely many Euler factors at $S_0$, and the Gauss sums in its epsilon factors are the source of the step ratios.

The representation theory of Section 13 rests on Harish-Chandra: the real analyticity of $K$-finite matrix coefficients (1953) and the classification of discrete series by their Harish-Chandra parameters (1966). The lowest $K$-type of a discrete series is described by the Blattner formula, proved in the form needed by Schmid (1975). The factorization of irreducible admissible representations of adelic groups into local factors is due to Flath (1979), and the theorem of Dixmier and Malliavin (1978) says that a smooth vector is a finite sum of convolutions $\pi(f)v$. The smooth globalization of Harish-Chandra modules in Sections 3, 7 and 21 is the theorem of Casselman and Wallach, see Casselman (1989). At the finite places Section 13 uses the theory of induced representations of Bernstein and Zelevinsky (1977, 1980) and the characters of finite general linear groups of Green (1955).

- R. Howe, θ-series and invariant theory, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 275 to 285.
- R. Howe, Transcending classical invariant theory, J. Amer. Math. Soc. 2 (1989), 535 to 552.
- S. Rallis, Langlands' functoriality and the Weil representation, Amer. J. Math. 104 (1982), 469 to 515.
- S. Rallis, Injectivity properties of liftings associated to Weil representations, Compositio Math. 52 (1984), 139 to 169.
- A. Weil, Sur certains groupes d'opérateurs unitaires, Acta Math. 111 (1964), 143 to 211.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), 1 to 87.
- S. Kudla, Splitting metaplectic covers of dual reductive pairs, Israel J. Math. 87 (1994), 361 to 401.
- S. Kudla and S. Rallis, A regularized Siegel-Weil formula: the first term identity, Ann. of Math. 140 (1994), 1 to 80.
- A. Ichino, A regularized Siegel-Weil formula for unitary groups, Math. Z. 247 (2004), 241 to 277.
- M. Harris, S. Kudla and W. J. Sweet, Theta dichotomy for unitary groups, J. Amer. Math. Soc. 9 (1996), 941 to 1004.
- E. Hecke, Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen, Math. Z. 1 (1918), 357 to 376, and Math. Z. 6 (1920), 11 to 51.
- J. Tate, Fourier analysis in number fields and Hecke's zeta-functions, in J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory*, Academic Press, 1967, Chapter XV.
- Harish-Chandra, Representations of a semisimple Lie group on a Banach space I, Trans. Amer. Math. Soc. 75 (1953), 185 to 243.
- Harish-Chandra, Discrete series for semisimple Lie groups II, Acta Math. 116 (1966), 1 to 111.
- W. Schmid, Some properties of square-integrable representations of semisimple Lie groups, Ann. of Math. 102 (1975), 535 to 564.
- D. Flath, Decomposition of representations into tensor products, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 179 to 183.
- J. Dixmier and P. Malliavin, Factorisations de fonctions et de vecteurs indéfiniment différentiables, Bull. Sci. Math. 102 (1978), 307 to 330.
- W. Casselman, Canonical extensions of Harish-Chandra modules to representations of $G$, Canad. J. Math. 41 (1989), 385 to 438.
- I. N. Bernstein and A. V. Zelevinsky, Induced representations of reductive $p$-adic groups I, Ann. Sci. École Norm. Sup. 10 (1977), 441 to 472.
- A. V. Zelevinsky, Induced representations of reductive $p$-adic groups II, Ann. Sci. École Norm. Sup. 13 (1980), 165 to 210.
- J. A. Green, The characters of the finite general linear groups, Trans. Amer. Math. Soc. 80 (1955), 402 to 447.

**Remark 3.22.1 (Formalization).** The declaration listed for this section is the second name of the Rallis formula for a definite bottom of Section 21 ([BigThetaNormEqRallisInnerProduct.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BigThetaNormEqRallisInnerProduct.lean#L47)). It states the classical inner product formula above for the first theta integral of a bottom triangle, with the squared absolute value integrated over a fundamental domain in place of the Petersson norm, and with the product of the values $\Lambda(s)$ for $1 - e_0 \le s \le h_0$ in place of the standard $L$-value.
