---
title: Notes and references
decls:
  - PositivityTheory.Rg.Wsf.weilSiegelFormula
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter proves the Siegel-Weil formula for unitary dual pairs in three forms. The convergent form, [the Weil-Siegel formula](/entry/weil-siegel-formula/), feeds [Howe duality for unitary groups](/entry/weil-unitary/) and the theta lifts of the following chapters. The form at the centre, [the field statement](/entry/field/), and the standard form of Section 15 feed the literature route of [every character](/step/every-character-of-literature/) through [the literature statement](/entry/siegel-weil-std-of-literature/), where they replace the citation of Kudla and Rallis and of Ichino. The archimedean computations of Sections 6 to 9 and the continuation of Section 16 feed the direct route of [every character](/step/every-character/), the latter through the multiplicativity of Siegel Eisenstein series. All of this sits inside [the proof](/proof/siegel-weil/).

**Section 1.** The Gram fibre measures are Siegel's local densities in measure form. Siegel introduced them for quadratic forms in the Hauptsatz (Siegel 1935), as limits of the number of solutions of congruences, and Weil (1965) recast them as fibre measures of the map $X \mapsto \operatorname{gr}(X)$, which is the form used here. The hyperbolic stage, which adds a hyperbolic plane and integrates over the new coordinates, is the inductive device of Weil (1965), Chapter III.

**Section 2.** The singular case, where the Gram matrix is $0$, is Weil's reduction of the Siegel formula to the mass formula for isotropic vectors. The measure form, stated for all nonnegative functions at once, follows Weil (1965) and the adelic treatment in Weil (1982).

**Section 3.** The identity of a Fourier coefficient of the Siegel Eisenstein series with an Euler product of local integrals is the computation of the singular series, due to Siegel (1935) for quadratic forms and to Shimura (1982, 1983, 1997) in the generality of Hermitian forms. Shimura's confluent hypergeometric functions on tube domains are the archimedean factors, and his Euler products give the finite ones.

**Section 4.** The Siegel-Weil formula in the absolutely convergent range is Weil's theorem (Weil 1965), with the big cell argument via Poisson summation on Hermitian matrices. The unitary case in the convergent range is treated by Ichino (2004), Section 2, and the isotropic convergent case for orthogonal groups by Kudla and Rallis (1988, part II). The Weil representation itself is that of Weil (1964).

**Section 5.** The formula at the point $s_0 = (m - n)/2$, outside the range of absolute convergence, is the regularised Siegel-Weil formula. The first term identity is Kudla and Rallis (1994), its unitary analogue is Ichino (2004), and the general case for classical groups is Yamana (2014). The second term identity is Gan, Qiu and Takeda (2014). Our treatment works through the Fourier coefficients and does not use the regularised theta integral.

**Section 6.** The Gaussian laws at a real place compute the Weil representation on Gaussian vectors in the Schrödinger model. These computations are in Kudla and Rallis (1988) and in the doubling setup of Harris, Kudla and Sweet (1996).

**Section 7.** Holomorphy of the leading terms of the Siegel Eisenstein series below the middle uses the normalising factors of the local intertwining operators. For the convergent and near central range this is in Kudla and Rallis (1994), and for unitary groups in Ichino (2004) and Yamana (2014).

**Section 8.** The Gaussian moments are integrals of polynomials against a Gaussian over Hermitian matrices, and the invariant theory reduces them to determinants. Hua (1963) computes the related integrals over the classical domains, and Shimura (1982) computes them as special values of confluent hypergeometric functions.

**Section 9.** The archimedean Whittaker integral of the Siegel Eisenstein series is Shimura's confluent hypergeometric function (Shimura 1982). Its value at the Siegel-Weil point, a Gram density, is the archimedean case of the local Siegel-Weil formula.

**Section 10.** The rank one and binary bases are the cases $n = 1$ and $n = 2$, where the Eisenstein series lives on $U(1,1)$ or $U(2,2)$ and the counts are classical. For $n = 1$ the theta integral counts representations by a Hermitian form, as in Siegel (1935).

**Section 11.** Unfolding along an isotropic vector and averaging over the stabiliser is Weil's argument (Weil 1965), with Siegel's mean value theorem (Siegel 1945) for the unipotent radical.

**Section 12.** The proof that the theta measure of isotropic vectors is the Euler product of local fibre measures, with constant $1$, follows Siegel's proof of the Hauptsatz (Siegel 1935) through a lattice point count with an error term. The local averages identify the fibre measures as limits of volumes, which is Siegel's definition of the local densities.

**Section 13.** The convergence of the series over Hermitian matrices modulo integral ones is Siegel's convergence of the singular series (Siegel 1935), in the inductive form of Hua (1963) for integrals over classical domains. The vanishing of coefficients that no frame represents is the Hasse principle for Hermitian forms and the signature obstruction at the real places. The matching of the frame integral with Fock vectors uses the Schrödinger and Fock models of the Weil representation (Weil 1964).

**Section 14.** The unramified Whittaker integral is the local factor of the singular series, computed by Shimura (1983, 1997) for Hermitian forms. The ramified finite place integral is entire and its value at the Siegel-Weil point is a Gram density; this is the local Siegel-Weil formula at a finite place, as in Kudla and Rallis (1988) and Ichino (2004).

**Section 15.** The standard formula is the comparison of Fourier coefficients and constant terms of Kudla and Rallis (1988) and Ichino (2001, 2004). The constant term of the Siegel Eisenstein series along a maximal parabolic is computed by the Bruhat decomposition, as in Langlands (1976) and Kudla and Rallis (1994). The fact that $K$-finite functions correspond to polynomials in the Fock model is the standard description of the $K$-finite vectors of the Weil representation.

**Section 16.** The Epstein zeta function and its functional equation are Hecke's method in the adelic form of Tate (1967), Chapter XV, and of Godement and Jacquet (1972). Jacquet and Shalika (1981) use the mirabolic Eisenstein series built from it. Continuation by walls and gluing over tubes is a version of Langlands's method (Langlands 1976) for Eisenstein series of maximal parabolics, and the gluing across tubes uses Bochner's tube theorem (Bochner 1938).

### References

- S. Bochner, A theorem on analytic continuation of functions in several variables, Ann. of Math. 39 (1938), 14 to 19.
- W. T. Gan, Y. Qiu and S. Takeda, The regularized Siegel-Weil formula (second term identity) and the Rallis inner product formula, Invent. Math. 198 (2014), 739 to 831.
- R. Godement and H. Jacquet, Zeta Functions of Simple Algebras, Lecture Notes in Math. 260, Springer, 1972.
- M. Harris, S. Kudla and W. J. Sweet, Theta dichotomy for unitary groups, J. Amer. Math. Soc. 9 (1996), 941 to 1004.
- L.-K. Hua, Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains, Transl. Math. Monogr. 6, Amer. Math. Soc., 1963.
- A. Ichino, On the regularized Siegel-Weil formula, J. Reine Angew. Math. 539 (2001), 201 to 234.
- A. Ichino, A regularized Siegel-Weil formula for unitary groups, Math. Z. 247 (2004), 241 to 277.
- H. Jacquet and J. Shalika, On Euler products and the classification of automorphic representations I, Amer. J. Math. 103 (1981), 499 to 558.
- S. Kudla and S. Rallis, On the Weil-Siegel formula, J. Reine Angew. Math. 387 (1988), 1 to 68.
- S. Kudla and S. Rallis, On the Weil-Siegel formula II: the isotropic convergent case, J. Reine Angew. Math. 391 (1988), 65 to 84.
- S. Kudla and S. Rallis, A regularized Siegel-Weil formula: the first term identity, Ann. of Math. 140 (1994), 1 to 80.
- R. P. Langlands, On the Functional Equations Satisfied by Eisenstein Series, Lecture Notes in Math. 544, Springer, 1976.
- G. Shimura, Confluent hypergeometric functions on tube domains, Math. Ann. 260 (1982), 269 to 302.
- G. Shimura, On Eisenstein series, Duke Math. J. 50 (1983), 417 to 476.
- G. Shimura, Euler Products and Eisenstein Series, CBMS Regional Conf. Ser. Math. 93, Amer. Math. Soc., 1997.
- C. L. Siegel, Über die analytische Theorie der quadratischen Formen, Ann. of Math. 36 (1935), 527 to 606.
- C. L. Siegel, A mean value theorem in geometry of numbers, Ann. of Math. 46 (1945), 340 to 347.
- J. Tate, Fourier analysis in number fields and Hecke's zeta-functions, in J. W. S. Cassels and A. Fröhlich (eds.), Algebraic Number Theory, Academic Press, 1967, Chapter XV.
- A. Weil, Sur certains groupes d'opérateurs unitaires, Acta Math. 111 (1964), 143 to 211.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), 1 to 87.
- A. Weil, Adeles and Algebraic Groups, Progr. Math. 23, Birkhäuser, 1982.

**Remark 4.17.1 (Formalization).** The declaration listed for this section, `weilSiegelFormula`, is the Weil-Siegel formula in the convergent range, the main statement of the chapter that the notes above place in the literature. It is also listed in Section 4.
