---
title: Notes and references
decls:
  - GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds the second branch of [the chapter on the unitary hypotheses](/proof/unitary-hypotheses/) through the main theorem of Section 1, which pairs [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/) of Section 10 with [the lower bound for lambda](/entry/lam-low-of-hypotheses-alt-alt/) of Section 11. The step [the hypotheses are not empty](/step/nonempty-hyps/) uses only the second half: the lower bound for $\lambda$ is its third item. The surjectivity statement rests on Sections 2 to 9: the page and geometric statements of Section 2 and the runs and comparison of Section 3 give the rank statement, the export statement of Section 4 gives the twist bound, the run models of Section 3 give the share and bad places statements, and Sections 5 to 9 give [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/). The exponent bound is the longest chain, and it is where most of the published inputs of the chapter enter. The step [on the closed properties](/step/closed-def/) has the definition of a closed property of families, and the step [on the local Langlands correspondence](/step/rect-exists-def/) builds the last input of Section 7 from the local hypotheses.

Sections 1 to 3 are internal to the development. The closed properties of Section 1 are a filter argument: a property that holds for small $\varepsilon$, for large families and eventually at the points is closed under finite conjunctions, and each proof of the chapter joins its inputs in this way. The comparison of Section 3, away from the own prime, is a comparison of a lattice of cusp forms with a lattice of theta series, in the tradition of the theorem of Siegel and Weil that theta series span a space of modular forms; the inclusion at the primes above the own prime is the harder part and is left to Sections 4 and 10.

The inputs of Section 4 are classical. Rapid decay of cusp forms on Siegel sets goes back to Gelfand and Piatetski-Shapiro, and is proved in Harish-Chandra's notes (1968, Chapter I) and in Moeglin and Waldspurger (1995, Chapter I). The global Artin map and the ray class fields are the main theorems of global class field theory (Neukirch 1999, Chapter VI). The classification of the discrete series is Harish-Chandra (1966), and the smooth globalization of Harish-Chandra modules is due to Casselman (1989) and Wallach (1992, Chapter 11).

The frames of Section 5 and the automorphic representations of Section 6 are the theory of algebraic modular forms of Gross (1999): for a definite unitary group the automorphic forms of a given weight and level are functions on a finite double coset space with values in a representation, and the Hecke operators act on them through the double cosets. The passage from Hecke eigenvalues to Satake parameters is the Satake isomorphism (Satake 1963). The conditions $N_r + 1 < \ell$ and $\ell \nmid \operatorname{disc} E$ of the smallness condition put $\ell$ in the range where the weights are small with respect to $\ell$ and the group is unramified at $\ell$.

The Galois representations of Section 7 come from the theory of polarized regular algebraic cusp forms on $\mathrm{GL}_n$ over CM fields. That regular algebraic cusp forms are cohomological is a lemma of Clozel (1990). Base change from definite unitary groups to $\mathrm{GL}_n$ is due to Labesse (2011). The Galois representations were constructed by Harris and Taylor (2001), Shin (2011) and Chenevier and Harris (2013), and their compatibility with the local Langlands correspondence of Harris and Taylor (2001) and Henniart (2000) gives the Frobenius polynomials. The $\ell$-adic characters of algebraic Hecke characters are due to Weil, in the form of Serre (1968, Chapter II).

The model statement of Section 8 is in the style of Hida theory: the block subspace is covered by the localizations of the Hecke module at the maximal ideals that meet it. Chebotarev's density theorem (Neukirch 1999, Chapter VII, §13) gives places of degree one with a given Frobenius. The comparison of crystalline lattices with $F$-crystals is the theorem of Bhatt and Scholze (2023), which identifies crystalline $\mathbb{Z}_\ell$-lattices with prismatic $F$-crystals over the ring of integers.

The cut lemma of Section 9 is a statement on the Weyl modules of $\mathrm{GL}_N$ in characteristic $\ell$; the background is in Jantzen (2003, Part II, Chapter 2). The classification of the cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_q)$ in Section 10, with their degrees $\prod_{i=1}^{d-1}(q^i - 1)$, is part of Green's determination of the characters of the finite general linear groups (1955).

The lower bound of Section 11 uses the theta correspondence. Weil (1965) proved the convergence of the theta integral and the Siegel-Weil formula in his range; Kudla and Rallis (1994) gave the regularized form for symplectic and orthogonal pairs, and Ichino (2004) for unitary groups. The doubling method and the unramified computation of the doubling integral are due to Piatetski-Shapiro and Rallis, in the book of Gelbart, Piatetski-Shapiro and Rallis (1987, Part A). The finiteness results for smooth representations of $\mathrm{GL}_n$ over a local field are in Bernstein and Zelevinsky (1977), and the formal degree of a discrete series is Harish-Chandra (1966).

- J. Bernstein and A. V. Zelevinsky, Induced representations of reductive $p$-adic groups I, Ann. Sci. École Norm. Sup. 10 (1977), 441 to 472.
- B. Bhatt and P. Scholze, Prismatic $F$-crystals and crystalline Galois representations, Camb. J. Math. 11 (2023), 507 to 562.
- W. Casselman, Canonical extensions of Harish-Chandra modules to representations of $G$, Canad. J. Math. 41 (1989), 385 to 438.
- G. Chenevier and M. Harris, Construction of automorphic Galois representations II, Camb. J. Math. 1 (2013), 53 to 73.
- L. Clozel, Motifs et formes automorphes: applications du principe de fonctorialité, in *Automorphic Forms, Shimura Varieties, and L-functions*, Vol. I, Perspect. Math. 10, Academic Press, 1990, 77 to 159.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254, Springer, 1987, Part A.
- J. A. Green, The characters of the finite general linear groups, Trans. Amer. Math. Soc. 80 (1955), 402 to 447.
- B. H. Gross, Algebraic modular forms, Israel J. Math. 113 (1999), 61 to 93.
- Harish-Chandra, Discrete series for semisimple Lie groups II, Acta Math. 116 (1966), 1 to 111.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Springer, 1968, Chapter I.
- M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Ann. of Math. Stud. 151, Princeton Univ. Press, 2001.
- G. Henniart, Une preuve simple des conjectures de Langlands pour GL(n) sur un corps $p$-adique, Invent. Math. 139 (2000), 439 to 455.
- A. Ichino, A regularized Siegel-Weil formula for unitary groups, Math. Z. 247 (2004), 241 to 277.
- J. C. Jantzen, *Representations of Algebraic Groups*, 2nd ed., Math. Surveys Monogr. 107, Amer. Math. Soc., 2003, Part II, Chapter 2.
- S. S. Kudla and S. Rallis, A regularized Siegel-Weil formula: the first term identity, Ann. of Math. 140 (1994), 1 to 80.
- J.-P. Labesse, Changement de base CM et séries discrètes, in *On the Stabilization of the Trace Formula*, International Press, 2011, 429 to 470.
- C. Moeglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Cambridge Tracts in Math. 113, Cambridge Univ. Press, 1995, Chapter I.
- J. Neukirch, *Algebraic Number Theory*, Grundlehren Math. Wiss. 322, Springer, 1999, Chapter VI, §§6 and 7, and Chapter VII, §13.
- I. Satake, Theory of spherical functions on reductive algebraic groups over $\mathfrak{p}$-adic fields, Publ. Math. IHÉS 18 (1963), 5 to 69.
- J.-P. Serre, *Abelian $\ell$-adic Representations and Elliptic Curves*, Benjamin, 1968, Chapter II.
- S. W. Shin, Galois representations arising from some compact Shimura varieties, Ann. of Math. 173 (2011), 1645 to 1741.
- N. R. Wallach, *Real Reductive Groups II*, Pure Appl. Math. 132-II, Academic Press, 1992, Chapter 11.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), 1 to 87.

**Remark 5.12.1 (Formalization).** The declaration listed for this section is the surjectivity statement of Section 10 ([OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L28)). It takes twelve of the published inputs of the chapter: Green's classification, the six Galois inputs of Sections 7 and 8, the theorem of Clozel, rapid decay, the local Langlands correspondence, the discrete series and the Casselman-Wallach theorem. The lower bound for $\lambda$ takes rapid decay and six more inputs, so the chapter has eighteen published inputs in all, and rapid decay is the only one used by both halves. Of the eighteen, the Siegel-Weil formula in the convergent range does no work: it is bound and never used in Section 11. In Lean the statements of the inputs are named after their published sources and are taken as hypotheses; we have read the Lean types of most of them only in part, and we have not checked them against the published theorems.
