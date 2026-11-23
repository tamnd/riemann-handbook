---
title: The bundles of published results
decls:
  - UpperTheory.LiteratureTheorems.literature_nonexistence
  - UpperTheory.LiteratureTheorems.published_results_first
  - UpperTheory.LiteratureTheorems.published_results_eigen
  - UpperTheory.LiteratureTheorems.published_results_arithmetic
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The bundles of published results

The proof does not pass each published theorem separately to the step that uses it. It collects them in four bundles, one for each part of the argument, and passes the bundles. This section says what the bundles contain and how they meet in the step [EveryCharacter from the literature](/step/every-character-of-literature/). Each bundle is a conjunction of statements from the earlier sections of this chapter and from other chapters. The bundles have no mathematical content of their own. Their value is that they make the list of inputs from the literature explicit.

### The record of open statements

**Definition 1.7.1 (Open literature statements).** The *open literature statements* are the conjunction of three statements:

1. the existence of the local Langlands correspondence for $\mathrm{GL}_n$ over a $p$-adic field, in the form of [the existence of rec](/step/rect-exists-def/);
2. a statement on Galois representations attached to polarised automorphic representations of unitary groups, in the form of [a row](/step/row-def/), from Caraiani's local-global compatibility;
3. a second statement of the same form, for polarised pairs.

See [the open literature statements](/step/open-literature-statements-def/). These are the inputs that the proof does not derive from a statement with a complete proof in the development. Every theorem of this chapter takes them as a hypothesis.

Only a few theorems use the hypothesis. The local Langlands correspondence goes into the non-endoscopic bundle below and into the main step. The two statements on Galois representations go into the non-endoscopic bundle, and the first also into one further theorem on local-global compatibility. All the theorems of Sections 1 to 6 ignore the hypothesis.

### The four bundles

**Theorem 1.7.2 (Non-endoscopic inputs).** Assume the open literature statements. Then the following five statements hold:

1. a bundle of results on smooth representations of $p$-adic $\mathrm{GL}_n$, which contains the local Langlands correspondence;
2. a bundle of results on automorphic representations of $\mathrm{GL}_n$ and unitary groups and their Galois representations, which contains local-global compatibility;
3. a bundle of results on Galois cohomology: Poitou-Tate duality, local and global finiteness, local Tate duality, the local and global Euler characteristic formulas, the Greenberg-Wiles formula and the local Bloch-Kato conditions;
4. the statements on periods and zeta denominators of the previous section;
5. the functional equation of Hecke L-functions in Tate's form.

Lean: `UpperTheory.LiteratureTheorems.literature_nonexistence`.

*Proof.* Each part is a theorem from the literature applied to the open literature statements. Part 4 is the Proposition on periods and zeta denominators. $\square$

**Theorem 1.7.3 (Local theta inputs).** Assume the open literature statements. Then the 53 statements of [the local theta inputs](/step/theta-local-inputs-def/) hold. Among them are:

1. Kudla's splitting, archimedean Howe duality, the metaplectic representation, the Stone-von Neumann theorem and the existence of the Weil representation for unitary dual pairs;
2. the Harish-Chandra theorems on Harish-Chandra modules, the Casselman-Wallach theorem, the formal degree of the discrete series, and the existence and lowest $K$-types of discrete series of $U(p, q)$;
3. Gelfand's theorem on cuspidal representations over a finite field, Green's series, Bernstein-Zelevinsky finiteness, Bernstein's irreducibility theorem and Zelevinsky's theorem;
4. strong approximation for $SU$, Flath's theorem, the Hasse principle for Hermitian forms, the doubling method and the Rallis inner product formula;
5. growth and decay estimates for cusp forms.

Lean: `UpperTheory.LiteratureTheorems.published_results_first`.

*Proof.* Each statement is a theorem from the literature applied to the open literature statements. $\square$

**Theorem 1.7.4 (Unitary group hypotheses).** Assume the open literature statements. Then the 60 statements of [the unitary group hypotheses](/step/unitary-group-third-place-hypotheses-def/) hold. Among them are:

1. the non-endoscopic inputs above;
2. a bundle of twelve analytic results, including Harish-Chandra's analyticity theorem and Flath's theorem;
3. a bundle of seven $p$-adic results, including Fontaine's period ring, global Artin reciprocity, local Tate duality and the Bhatt-Scholze theorem;
4. the formal degree, the Casselman-Wallach theorem, strong approximation for $SU$, Flath's theorem and Gross's curves;
5. one statement that is trivially true and carries no content.

Lean: `UpperTheory.LiteratureTheorems.published_results_eigen`.

*Proof.* Each statement is a theorem from the literature applied to the open literature statements. The trivial statement is proved by its proof of truth. $\square$

**Theorem 1.7.5 (Hodge bundle inputs).** Assume the open literature statements. Then the 28 statements of [the published Hodge bundle theorems](/step/published-results-arithmetic/) hold. Among them are:

1. the existence of toroidal compactifications, the volume bound and the calculus of arithmetic intersection numbers;
2. Mumford's theorem on good metrics, the $L^2$ extension theorem, Grothendieck's existence theorem and the arithmetic Hilbert-Samuel theorem;
3. Kawamata-Viehweg and Nadel vanishing, principalisation, Chow forms and heights of cycles;
4. Grothendieck-Messing theory, prismatic Dieudonné theory, semistable reduction, the extension of homomorphisms of semi-abelian schemes and principal polarisations;
5. class field theory: ray class fields, the Hasse norm theorem and Landherr's theorem.

Lean: `UpperTheory.LiteratureTheorems.published_results_arithmetic`.

*Proof.* Each statement is a theorem from the literature applied to the open literature statements. $\square$

### How the bundles are used

The step [EveryCharacter from the literature](/step/every-character-of-literature/) proves [EveryCharacter](/step/every-character/) under the open literature statements and the hypothesis [VWin](/step/vwin-def/). It applies the theorem on [local matching of theta integrals](/step/theta-local-matching/) to four inputs: the unitary group hypotheses, the local theta inputs, the agreement of theta integrals with their local matching, and a volume bound for the Hodge bundle. The volume bound is [Theorem](/entry/top-covol-slim2-use-alt-alt/). It takes the Hodge bundle inputs together with resolution of singularities, the Poincaré-Lelong formula, Zarhin's trick, the toroidal compactifications of Section 5, the seminegativity of Lie algebras of semi-abelian schemes, the arithmetic degree statement, and a few further inputs. The local Langlands correspondence enters once more through [the step on rec](/step/local-langlands-gl-rect-exists-of-literature/).

**Remark 1.7.6 (Formalization).** The four theorems are at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L639), lines 639, 727, 666 and 781, and the main step is at line 810. Each is a structure instance whose fields are theorems of the same file applied to the hypothesis `O`. The hypothesis is the structure `OpenLiteratureStatements` at line 215, with fields `caraianiLocalGlobalDual`, `localLanglandsExists` and `galoisRepOfPolarizedPairLit`; the first and third have the same type `Row`, and the structure is declared with `genInjectivity false` and `genSizeOfSpec false`. The fields of `O` are read directly only at lines 284, 286, 460 and 618; the other theorems of the file pass `O` on or ignore it. The non-endoscopic bundle has type `NonEndoscopicHypothesesAlt`; its name says "nonexistence", and no field says that something does not exist. A second structure `LitNE` with the same five field names is at [HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L30). The unitary group bundle has a field `siegelEisensteinSimplePole` of type `UnusedSlot72`, which is `True` ([DiscreteSpectrumResidualClassification.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/DiscreteSpectrumResidualClassification.lean#L7)); it is filled at line 505 by `trivial`, so the name promises a simple pole of a Siegel Eisenstein series that is not stated. The Hodge bundle has fields `p1` to `p26` and `q1` to `q18` with gaps: `p6`, `p7`, `p9` to `p11`, `p15`, `p17`, `p18`, `p21`, `p24`, `q2`, `q3`, `q5`, `q12`, `q14` and `q17` do not exist. Several statements occur in two bundles, for example Flath's theorem, the formal degree and strong approximation. The local Langlands correspondence at line 313 is obtained from `O.localLanglandsExists` by `llOf_alt`, whose conclusion is its first hypothesis.

## Notes and references

This chapter is the list of results that the proof takes from the literature, with the few short derivations that the development adds on top. The bundles feed the step [EveryCharacter from the literature](/step/every-character-of-literature/), and through it the final assembly of the proof in [the proof chapter](/proof/literature/). The record of open statements is the place where the proof meets results that the development does not prove. The other inputs of this chapter are proved in the development from smaller statements, or are themselves published theorems used as stated.

- Harish-Chandra, *Representations of a semisimple Lie group on a Banach space I*, Trans. Amer. Math. Soc. 75 (1953).
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966).
- W. Casselman, *Canonical extensions of Harish-Chandra modules to representations of G*, Canad. J. Math. 41 (1989).
- N. R. Wallach, *Real Reductive Groups I*, Chapter 3, and *Real Reductive Groups II*, Chapter 11.
- A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964).
- G. B. Folland, *Harmonic Analysis in Phase Space*, Chapter 4.
- S. S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994).
- R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989).
- S. I. Gelfand, *Representations of the full linear group over a finite field*, Mat. Sb. 83 (1970).
- A. Mínguez, *Correspondance de Howe explicite: paires duales de type II*, Ann. Sci. ÉNS (4) 41 (2008).
- J. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N)*, LNM 1041 (1984).
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II*, Ann. Sci. ÉNS 13 (1980).
- D. Flath, *Decomposition of representations into tensor products*, Proc. Sympos. Pure Math. 33, part 1 (1979).
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, §7.4.
- H. Gillet and C. Soulé, *Arithmetic intersection theory*, Publ. Math. IHÉS 72 (1990).
- H. Gillet and C. Soulé, *An arithmetic Riemann-Roch theorem*, Invent. Math. 110 (1992).
- A. Abbes and T. Bouche, *Théorème de Hilbert-Samuel arithmétique*, Ann. Inst. Fourier 45 (1995).
- X. Yuan, *Big line bundles over arithmetic varieties*, Invent. Math. 173 (2008).
- P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Chapter 1.
- Yu. G. Zarhin, *A finiteness theorem for unpolarized abelian varieties over number fields with prescribed places of bad reduction*, Invent. Math. 79 (1985).
- L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129 (1985).
- D. Mumford, *Hirzebruch's proportionality theorem in the non-compact case*, Invent. Math. 42 (1977), §1.
- T. Ohsawa and K. Takegoshi, *On the extension of L2 holomorphic functions*, Math. Z. 195 (1987).
- A. Grothendieck, *Éléments de géométrie algébrique III*, Théorèmes 5.4.1 and 5.4.5.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapters IV and V.
- G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Theorem 5.4.
- D. A. Cox, *Primes of the Form $x^2 + ny^2$*, Theorem 11.1.
- P. Deligne and K. Ribet, *Values of abelian L-functions at negative integers over totally real fields*, Invent. Math. 59 (1980).
- B. H. Gross, *Arithmetic on Elliptic Curves with Complex Multiplication*, LNM 776 (1980).
- B. Bhatt and P. Scholze, *Prismatic F-crystals and crystalline Galois representations*, Camb. J. Math. 11 (2023).
