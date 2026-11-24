---
title: Split pairs and the equations of the theta family
decls:
  - Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_car
  - Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_all
  - Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_gen
  - Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SquareSplitPairs.eqP_of_pair
  - Formalism.L2.PairingIndexBounds.Eq.SqG.eulerProduct_eq_of_curve_ideal
  - Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_outright
  - Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_all
  - Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_gen
  - Formalism.L2.PairingIndexBounds.Eq.SquareSplitPairs.eqP_of_pair
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Split pairs and the equations of the theta family

In [Section 1.23.6](/entry/l2-pairing-index-bounds-eq-j-eq-p-of-neg/) the equations of the theta family were reduced to a split of each square of self-dual lattice pairs. In this section we get these splits from a matrix statement on two self-dual lattices, the split pairs, and from the theorem that every CM field that is unramified over its real subfield has split pairs. Then we remove the hypothesis $\delta \ne 0$ and the hypothesis that the base is standard. This gives the equations for every base over a curve ideal and a twelfth root, which is the input of [the nonempty hypotheses](/step/nonempty-hyps/). We use the notation of Section 23.

**Definition 1.24.1 (Split pairs).** The field $E$ has split pairs if for each even $N$, all self-dual $L', L'' \subset E^N$ and each $n \in \mathcal{O}_E \setminus \{0\}$, there is a matrix $e$ over $E$ that maps $L'$ into $L'$ and $L''$ into $L''$, such that each of the three matrices
$$e^2 - e, \qquad \bar{e}^{t} e, \qquad \overline{(1 - e)}^{t}(1 - e)$$
maps each $y \in L' \cup L''$ to $n m$ for some $m \in L' \cap L''$. Split pair generation is the statement that every CM field $E$ that is totally complex, whose conjugation is complex conjugation at every embedding, and in which for each maximal ideal $\mathfrak{P}$ of $\mathcal{O}_E$ there is $x \in \mathcal{O}_E$ with $x - \bar{x} \notin \mathfrak{P}$, has split pairs.

**Theorem 1.24.2 (Equations from split pairs).** Let $\mathfrak{c}$, $\delta \ne 0$, $B$ and $\chi$ be as in the theorem on the norm condition in Section 23, and assume that $E$ has split pairs. Then the theta family satisfies the equations.

Lean: `Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SquareSplitPairs.eqP_of_pair` (also `Formalism.L2.PairingIndexBounds.Eq.SquareSplitPairs.eqP_of_pair`, the same statement for the second kind of datum).

*Proof.* Split pairs give square splits for $B$. The triangle laws hold for a standard base with a curve ideal and a nonzero twelfth root. Apply the theorem on a split square in Section 23. $\square$

**Theorem 1.24.3 (Equations from split pair generation).** Let $\mathfrak{c}$, $\delta \ne 0$, $B$ and $\chi$ be as in the theorem on the norm condition in Section 23, and assume split pair generation. Then the theta family satisfies the equations.

Lean: `Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_gen` (also `Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_gen`, the same statement for the second kind of datum).

*Proof.* The field $E$ of the host is a CM field, its conjugation is complex conjugation at each embedding, and $E$ is unramified over its real subfield, which gives for each maximal $\mathfrak{P}$ an integer $x$ with $x - \bar{x} \notin \mathfrak{P}$. Split pair generation then gives split pairs for $E$. Apply the theorem on split pairs. $\square$

**Corollary 1.24.4 (Nonzero twelfth roots).** In the theorem, the hypothesis $\delta \ne 0$ can be left out.

Lean: `Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_all` (also `Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_all`, the same statement for the second kind of datum).

*Proof.* The lattice $\Lambda(\mathfrak{c})$ of a curve ideal has discriminant $\Delta \ne 0$. If $\delta = 0$, then $\Delta = \delta^{12} = 0$, which is false. $\square$

**Theorem 1.24.5 (Equations of the theta family).** Let $\mathfrak{c}$ be a curve ideal, $\delta$ a twelfth root for $\mathfrak{c}$, $B$ a base over $(D, \mathfrak{c}, \delta)$ and $\chi$ a splitting character. Then the theta family of $B$ and $\chi$ satisfies the equations.

Lean: `Formalism.L2.Ker.Cd.PairingIndexBounds.Eq.SqG.eqP_car` (also `Formalism.L2.PairingIndexBounds.Eq.SqG.eulerProduct_eq_of_curve_ideal`, the same statement for the second kind of datum, and `Formalism.L2.PairingIndexBounds.Eq.SqG.eqP_outright`, the step for a standard base of the second kind).

*Proof.* Each base over a curve ideal and a twelfth root is standard. Split pair generation holds. Apply the corollary on nonzero twelfth roots. $\square$

**Remark 1.24.6 (Formalization).** The chain for the first kind of datum `Car` is in [SplitPairOfGen.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/ColumnDataEquations/SplitPairOfGen.lean#L55), with `eqP_gen` at line 42, `eqP_all` at line 50 and the proof that the host is unramified, `splitPair_of_gen`, at line 15. The theorem on split pairs for `Car` is in [SqLTop.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/ColumnDataEquations/SqLTop.lean#L15) and calls the triangle laws directly, while for `D7` it goes through `eqP_top`. The chain for the second kind of datum `D7` starts at [FinalEq.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/SplitPairEquations/FinalEq.lean#L6). For `D7` the unramified condition is a field of the datum, and $\delta \ne 0$ comes from the nonvanishing of the discriminant in [EqPAll.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/SplitPairEquations/EqPAll.lean#L6). The name `eulerProduct_eq_of_curve_ideal` says Euler product, but the statement is the equations of the theta family. Split pairs are `SplitPair` in [SqLInput.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/ColumnDataEquations/SqLInput.lean#L14), and split pair generation is `SplitPairGen` in [SplitPairGen.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/SplitPairEquations/SplitPairGen.lean#L15). Its proof `split_pair_generation` ([SplitPairGen.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/SplitPairGen.lean#L5)) uses `square_pair_glue` and `square_pair_local`, which we have not opened. The unramified condition is defined twice with the same body, as `IsCMUnram` in CMTraceOnto.lean and in UnimodGenus.lean. The standard base `stdOK` is proved in two places, one for each kind of datum, and we have not unfolded these proofs.

## Notes and references

This chapter supplies the inputs of level four of the assembly. Sections 1 to 7 give the symmetric levels, the spectral objects over replaced stages, the gauge and the kernel conditions of true columns; they feed [the restriction of the top stage](/entry/exists-s-rest-top/), [spectral objects for extensions](/entry/has4-of-has3-of-s-ext-none/) and [the kernel entry conditions](/entry/ker-ent-c-true/). Sections 8 to 12 give the core, the Bessel periods, the theta data, the divisor data and the series ties; they feed [the closing of the membership statement](/entry/member-e-closing-alt-alt/). Sections 13 to 17 give the extension of adelic data, the coefficient fields, the fine adelic data and the row readings; they feed [the membership and bundles at large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/) and [saturated bare forms](/entry/bare-form-saturated/). Section 18 feeds [the local inputs of a member](/entry/exists-hyp-n-of-geometric-galois-compat/). Sections 19 to 22 feed [the nonempty hypotheses at unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/), and Sections 23 and 24 feed [the nonempty hypotheses](/step/nonempty-hyps/).

Several inputs are taken from the literature as hypotheses. The ray class fields and principal ideals of Section 8 are the existence theorem of class field theory and the principal ideal theorem of Furtwängler. The CM curves of Section 8 are the curves of Gross: for $p > 3$ with $p \equiv 3 \pmod 4$, the curve over $\mathbb{Q}(j)$ with CM by the integers of $\mathbb{Q}(\sqrt{-p})$, good reduction outside $p$ and minimal discriminant $-p^3$; see [Gross's curves](/learn/elliptic-curves/#grosss-curves). The Siegel mass ratio of Section 8 is the ratio of the masses of the standard hermitian lattices in two consecutive ranks; it comes from the mass formula of Siegel in the form for unitary groups of Prasad and of Gan, Hanke and Yu; see [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups). Section 12 uses global Artin reciprocity; see [global class field theory](/learn/class-field-theory/#global-class-field-theory). The hypotheses (DS), (DE), (HC) and (CW) of Sections 13 and 16 are the results of Harish-Chandra on discrete series and on Harish-Chandra modules, and the globalization theorem of Casselman and Wallach, in the form of Bernstein and Krötz; see [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees). The hypothesis (RD) is the rapid decay of cusp forms, (HF) is the finiteness theorem of Harish-Chandra for automorphic forms of fixed type and level, and (WU) is the Weil representation of a unitary dual pair.

Some statements are special cases of classical results. The equations of Sections 23 and 24 are the transformation laws of theta functions under the unitary groups and under a change of lattice, in the Weil representation; the factors $\chi(\det)^{\pm N/2}$ are the values of a splitting character of Kudla and of Harris, Kudla and Sweet. The norm condition of Section 23 says that the product of the norm forms $\alpha^2 + q\beta^2$ and $\gamma^2 + d\delta^2$ represents $-1$ modulo every $m$. The number $\delta$ is a twelfth root of the discriminant of the lattice $\Lambda(\mathfrak{c})$.

- E. Artin, "Beweis des allgemeinen Reziprozitätsgesetzes", *Abh. Math. Sem. Univ. Hamburg* 5 (1927), 353 to 363.
- Ph. Furtwängler, "Beweis des Hauptidealsatzes für die Klassenkörper algebraischer Zahlkörper", *Abh. Math. Sem. Univ. Hamburg* 7 (1930), 14 to 36.
- J. Tate, "Global class field theory", in J. W. S. Cassels and A. Fröhlich, *Algebraic Number Theory*, Chapter VII.
- J. Neukirch, *Algebraic Number Theory*, Chapter VI.
- B. H. Gross, *Arithmetic on Elliptic Curves with Complex Multiplication*, Lecture Notes in Math. 776, Springer, 1980.
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II.
- J.-P. Serre and J. Tate, "Good reduction of abelian varieties", *Ann. of Math.* 88 (1968), 492 to 517.
- C. L. Siegel, "Über die analytische Theorie der quadratischen Formen", *Ann. of Math.* 36 (1935), 527 to 606.
- G. Prasad, "Volumes of S-arithmetic quotients of semi-simple groups", *Publ. Math. IHÉS* 69 (1989), 91 to 117.
- W. T. Gan, J. P. Hanke and J.-K. Yu, "On an exact mass formula of Shimura", *Duke Math. J.* 107 (2001), 103 to 133.
- Harish-Chandra, "Representations of a semisimple Lie group on a Banach space I", *Trans. Amer. Math. Soc.* 75 (1953), 185 to 243.
- Harish-Chandra, "Discrete series for semisimple Lie groups II", *Acta Math.* 116 (1966), 1 to 111.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Chapter I.
- W. Casselman, "Canonical extensions of Harish-Chandra modules to representations of G", *Canad. J. Math.* 41 (1989), 385 to 438.
- N. R. Wallach, *Real Reductive Groups I*, Chapter 3, and *Real Reductive Groups II*, Chapter 11.
- J. Bernstein and B. Krötz, "Smooth Fréchet globalizations of Harish-Chandra modules", *Israel J. Math.* 199 (2014), 45 to 111.
- A. W. Knapp, *Representation Theory of Semisimple Groups*, Chapters VIII, IX and XII.
- C. Moeglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Chapter I.
- A. Weil, "Sur certains groupes d'opérateurs unitaires", *Acta Math.* 111 (1964), 143 to 211.
- R. Howe, "Transcending classical invariant theory", *J. Amer. Math. Soc.* 2 (1989), 535 to 552.
- S. Kudla, "Splitting metaplectic covers of dual reductive pairs", *Israel J. Math.* 87 (1994), 361 to 401.
- M. Harris, S. Kudla and W. J. Sweet, "Theta dichotomy for unitary groups", *J. Amer. Math. Soc.* 9 (1996), 941 to 1004.
