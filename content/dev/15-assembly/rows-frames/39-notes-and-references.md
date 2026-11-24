---
title: Notes and references
decls:
  - Formalism.BasicNotions.Examples₂.H0
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter collects the inputs of the assembly that are proved by rows of explicit data and frames of lattices. They fall into four groups. The first group feeds the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/), the second the nonemptiness of the hypotheses, the third shows that the data are not empty, and the fourth feeds the branch of [the characters of the literature](/step/every-character-of-literature/).

### Summary by sections

Sections 1 to 3 treat finite groups and families. Section 1 shows that a character of a product of groups $\mathrm{GL}_r(\mathbb{F}_g)$ in the good idempotent is a product of characters of cuspidal parabolic inductions, as [the nonempty set of hypotheses](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) needs. Section 2 proves the pass condition of the third place series from the rows of a real datum, and Section 3 proves the eight inputs of the second complement bound along a family, for [the second complement at the constructed points](/entry/division-second-complement-constructed-points/). Section 4 bounds the volume of the height shells in a frame quotient of an adelic unitary group.

Sections 5 to 10 are about leaves and lattices. Section 5 proves the depth bounds and the lattice properties of a leaf. Section 6 turns a crystalline block into a lattice link through Wach lattices over a power series ring, and Section 7 proves the weight inputs with lattice links in the Hida setting of a frame, both for [the model statement for a small frame](/entry/model-st-of-small-frame-gal/). Section 8 proves the exponent bound at the twisted places by the seventh recursion. Section 9 proves [the readings at small places](/entry/reads-of-small-alt/), the pinned runs and the bound at the twisted places. Section 10 shows that the trace lattices lie in the span of theta series away from the own prime, for [the comparison away from the own prime](/entry/compare-off-own-at-runs-alt/).

Sections 11 to 21 complete the surjectivity branch. Sections 11 and 12 build [cusp forms with independent translates](/entry/exists-cusp-form-independent-translates/) by orbit interpolation at a free ball. Section 13 bounds the sum of the seventh recursion over the exceptional set, for [the exponent bound at a point](/entry/has-exp-bound-at/). Section 14 compares the ranks of cusp forms at shifted weights, for [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/). Sections 15 and 16 prove the row statement from kernel chains, for [the rows from the column pins](/entry/rows-u-of-col-pins-alt/), and the norms of normalized theta families that it uses. Section 17 proves the index bound at a run, and Sections 18 and 19 prove [the inputs at a record](/entry/inputs-net-rec-plus/): the shares, the local point data, the run hypotheses and [the shares at all indices](/entry/shares-at-all/) by division at the points of a flat datum. Section 20 builds the base potentials of [the archimedean datum at a run](/entry/arch-at-of-run/) from theta sums, and Section 21 bounds the bad share at two primes, for [the definite good share](/entry/definite-good-share/).

Sections 22 and 23 serve the unitary hypotheses in two other places: Section 22 builds a class and a selection for [the record from all rows](/entry/nonempty-hyps-of-all-rows-alt/), and Section 23 compares Satake parameters at the inert places for [the unitary reading](/entry/unitary-read-true-alt/).

Sections 24, 25 and 34 show that [the record is nonempty](/entry/record-nonempty/). Section 24 builds [the example host](/entry/h0/) $H_0$, Section 25 gives the record built from it, and the first part of Section 34 constructs the local period data at every prime.

Sections 26 to 33 and 35 to 37 prove inputs of [the nonemptiness of the hypotheses](/step/nonempty-hyps/). Section 26 shows that the cut cocycles at large primes are Bloch-Kato classes, for [the main linking theorem](/entry/nlink-e-main-alt-alt/), and Section 27 builds the pending objects at depth zero. Sections 28 to 32 prove the generation statements of the downward theta lift: [the reduction to finite type](/entry/gen-fin/) at the finite places, the local steps at the twist and type places, the vanishing at the real places, and [the irreducibility of compact Howe duality](/entry/howe-irr/) through harmonics and the lowest $K$-type. Section 33 shows that representations with parahoric vectors have toral cuspidal support and that good lifts exist. The second part of Section 34 proves the bottom readings. Section 35 bounds the leaf slopes for [the tie of the multiplicity bounds](/entry/mm-tie-alt/) and computes the spectral trace. Section 36 proves the cut inequality for exact exponents of Weyl lattices, the existence of grid choices, the extension of a real datum by new tuples and the pure tensor form of the small route. Section 37 proves the doubled Schrödinger model, the evaluation of toric sums and the reach of square flips.

Section 38 proves that a rule with the four properties of Rule 4 is determined by analytic deformations, through a comparison of key values on the two fibres of a family over a local domain.

### Sources

The finite group theory of Sections 1, 21 and 27 is the theory of Harish-Chandra induction for finite general linear groups. The characters are those of Green, and the irreducibility of induction from cuspidal representations with distinct labels follows from the theorem of Howlett and Lehrer on the endomorphism algebras of induced cuspidal representations. The depth zero objects of Section 27 are the depth zero types of Moy and Prasad, read through the reduction of a parahoric subgroup to a finite reductive group.

The $p$-adic Hodge theory of Sections 6, 26 and 34 uses the period rings of Fontaine, the crystalline lattices of Wach modules in the form of Wach and Berger, and the existence of crystalline lattices from prismatic $F$-crystals of Bhatt and Scholze. The comparison with Fontaine-Laffaille theory in Section 26 and the Bloch-Kato conditions are classical. The Lean proofs take most of these as hypotheses or as fields of local period data, as the remarks of those sections say.

The Hida setting of Sections 7 and 8 follows Hida's control theorems for nearly ordinary cohomology, and the dual Weyl modules and Weyl modules of Sections 7 and 36 are those of Jantzen. The cut inequality of Section 36 compares the Weyl lattice and the dual Weyl lattice through the Levi decomposition of two blocks, and the bound on the denominators is the classical bound for the $\ell$-adic valuation of binomial coefficients.

The local representation theory of Section 33 uses the theorem of Borel and Casselman: an irreducible admissible representation with a nonzero Iwahori fixed vector is a subquotient of an unramified principal series. The classification of the cuspidal support is that of Bernstein and Zelevinsky and of Zelevinsky, and the Satake parameters of Section 23 are those of Satake.

The theta correspondence of Sections 28 to 32 and 36 to 37 is built on the Weil representation of Weil, with the lattice models and the Schrödinger models of Mœglin, Vignéras and Waldspurger, the cocycle of Ranga Rao, and the splittings of Kudla for unitary dual pairs. The unitary case with characters $\chi$ restricting to powers of the quadratic character is that of Harris, Kudla and Sweet. Compact Howe duality in Sections 31 and 32 is Howe's theorem, and the harmonic polynomials and the multiplicity one of the lowest $K$-type are due to Kashiwara and Vergne. The doubling construction and the Siegel rule of Section 37 are the starting point of the doubling method of Piatetski-Shapiro and Rallis.

The spectral side of the trace formula in Section 35 is Arthur's, with pseudo-coefficients of discrete series from Harish-Chandra's theory. The extension of real data in Section 36 uses the globalization theorem of Casselman and Wallach for Harish-Chandra modules.

The toric sums of Section 37 are lattice sums of Hecke type. Their continuation and the Euler products come from Hecke's theory of $L$-functions of Grössencharacters in the adelic form of Tate. The local factors at the primes of $Q$ come from the zeta functions of orders of conductor $q$.

The theta constants and first jets of Section 38 are those of Mumford's theory of the equations defining abelian varieties. The step that joins two key data by a family over a local domain is the statement that theta constants of high level embed the moduli of polarized abelian varieties with level structure.

### References

- J. Arthur, *The invariant trace formula II. Global theory*, J. Amer. Math. Soc. 1 (1988), 501 to 554.
- L. Berger, *Limites de représentations cristallines*, Compos. Math. 140 (2004), 1473 to 1498.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive $p$-adic groups I*, Ann. Sci. École Norm. Sup. (4) 10 (1977), 441 to 472.
- B. Bhatt and P. Scholze, *Prismatic $F$-crystals and crystalline Galois representations*, Camb. J. Math. 11 (2023), 507 to 562.
- S. Bloch and K. Kato, *$L$-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift, Vol. I*, Progr. Math. 86, Birkhäuser, 1990, 333 to 400.
- A. Borel, *Admissible representations of a semi-simple group over a local field with vectors fixed under an Iwahori subgroup*, Invent. Math. 35 (1976), 233 to 259.
- W. Casselman, *The unramified principal series of $p$-adic groups I. The spherical function*, Compos. Math. 40 (1980), 387 to 406.
- W. Casselman, *Canonical extensions of Harish-Chandra modules to representations of $G$*, Canad. J. Math. 41 (1989), 385 to 438.
- J.-M. Fontaine, *Le corps des périodes $p$-adiques*, Astérisque 223 (1994), 59 to 111.
- J.-M. Fontaine and G. Laffaille, *Construction de représentations $p$-adiques*, Ann. Sci. École Norm. Sup. (4) 15 (1982), 547 to 608.
- J. A. Green, *The characters of the finite general linear groups*, Trans. Amer. Math. Soc. 80 (1955), 402 to 447.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), 1 to 111.
- M. Harris, S. Kudla and W. J. Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), 941 to 1004.
- E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen I*, Math. Z. 1 (1918), 357 to 376.
- H. Hida, *Control theorems of $p$-nearly ordinary cohomology groups for $\mathrm{SL}(n)$*, Bull. Soc. Math. France 123 (1995), 425 to 475.
- R. Howe, *Remarks on classical invariant theory*, Trans. Amer. Math. Soc. 313 (1989), 539 to 570.
- R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989), 535 to 552.
- R. B. Howlett and G. I. Lehrer, *Induced cuspidal representations and generalised Hecke rings*, Invent. Math. 58 (1980), 37 to 64.
- J. C. Jantzen, *Representations of Algebraic Groups*, 2nd ed., Math. Surveys Monogr. 107, Amer. Math. Soc., 2003, Part II, Chapter 2.
- M. Kashiwara and M. Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978), 1 to 47.
- S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), 361 to 401.
- C. Mœglin, M.-F. Vignéras and J.-L. Waldspurger, *Correspondances de Howe sur un corps $p$-adique*, Lecture Notes in Math. 1291, Springer, 1987, Chapter 2.
- A. Moy and G. Prasad, *Jacquet functors and unrefined minimal $K$-types*, Comment. Math. Helv. 71 (1996), 98 to 121.
- D. Mumford, *On the equations defining abelian varieties I*, Invent. Math. 1 (1966), 287 to 354.
- I. I. Piatetski-Shapiro and S. Rallis, *$\varepsilon$ factor of representations of classical groups*, Proc. Nat. Acad. Sci. U.S.A. 83 (1986), 4589 to 4593.
- R. Ranga Rao, *On some explicit formulas in the theory of Weil representation*, Pacific J. Math. 157 (1993), 335 to 371.
- I. Satake, *Theory of spherical functions on reductive algebraic groups over $\mathfrak{p}$-adic fields*, Publ. Math. IHÉS 18 (1963), 5 to 69.
- J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions*, in *Algebraic Number Theory* (J. W. S. Cassels and A. Fröhlich, eds.), Academic Press, 1967, 305 to 347.
- N. Wach, *Représentations $p$-adiques potentiellement cristallines*, Bull. Soc. Math. France 124 (1996), 375 to 400.
- N. R. Wallach, *Real Reductive Groups II*, Pure Appl. Math. 132-II, Academic Press, 1992, Chapter 11.
- A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), 143 to 211.
- A. V. Zelevinsky, *Induced representations of reductive $p$-adic groups II. On irreducible representations of $\mathrm{GL}(n)$*, Ann. Sci. École Norm. Sup. (4) 13 (1980), 165 to 210.

**Remark 7.39.1 (Formalization).** The declaration of this section is the example host `H0`, at line 207 of [ExampleLayerExistsGenerators.lean](lean:Formalism/LocalRingCardinality/SpanPowerMembership/ExampleLayerExistsGenerators.lean#L207). It is a structure value of type `Host R0` whose host axioms are `hostAx0` (line 201) and whose remaining fields are filled by the lemmas of `Formalism.HC.D7` applied to the example ranks, the host hypotheses `hostHyp0` and the layer `layer0`, with the two numerical checks `QS_le` and `o_pow` closed by `norm_num`. Section 24 states and discusses it. It is listed here because it is the one object that all three uses of the example in this chapter share: the record of Section 25, the local period data of Section 34, and the statement that the record is nonempty. The theorem numbers of the sources above were not checked against the Lean statements; where a chapter is given, it is the chapter where the cited topic is treated.
