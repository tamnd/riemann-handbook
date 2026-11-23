---
title: The archimedean arc condition
decls:
  - GlobalTheory.arcClause_closed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The archimedean arc condition

This section proves the archimedean arc condition for unitary moduli schemes. A formal arc through the boundary of a model of a unitary moduli scheme carries a semi-abelian scheme over $\mathbb{C}[[q]]$, and the condition says that this formal family is analytic: after the substitution $q = e^{2\pi i w}$ it agrees, for $\operatorname{Im} w$ large, with the complex uniformisation of the abelian varieties at the points of the moduli scheme. The result is used in [the step on characters from the literature](/step/every-character-of-literature/). The section has one theorem, and its proof applies a theorem of the chapter on sup norms of theta sections. For the complex side see [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization) and [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications) in Volume 1.

### The classical statement

Let $\mathrm{Sh}$ be a Shimura variety of PEL type with a smooth toroidal compactification. Lan proves that the algebraic toroidal compactification, built from Mumford's construction over complete rings, is isomorphic to the analytic one of Ash, Mumford, Rapoport and Tai. Near a cusp, the degenerating family given by Mumford's construction over the formal completion is the analytic family of complex tori, with the formal variable replaced by $e^{2\pi i w}$ (Lan, *Comparison between analytic and algebraic constructions of toroidal compactifications of PEL-type Shimura varieties*, J. reine angew. Math. 664 (2012)). The condition of this section is a statement of this kind for one formal arc at a time, for unitary data, and it also compares derivatives and theta functions.

### The setting

The condition is about the following data.

1. A CM field $E$ with an element $\rho$ of $\mathcal{O}_E$ such that $\rho^2 = -d$ for a prime $d \equiv 7 \pmod{16}$, an element $w_0$ with $2w_0 = 1 + \rho$, the complex conjugation on $\mathcal{O}_E$, and a complex number $\rho_0$ with $\rho_0^2 = -d$. The extension of $E$ over its maximal totally real subfield is unramified.
2. A Hermitian lattice: a finite projective $\mathcal{O}_E$-module $\Lambda$ with a unimodular alternating form $E_\Lambda$ that is Hermitian for the conjugation, of signature $(p, q)$.
3. A level: an odd integer $M \geq 3$, an ideal $\mathfrak{M}$ of $\mathcal{O}_E$ with $\mathfrak{M}\bar{\mathfrak{M}} = (M)$ and $\mathfrak{M} + \bar{\mathfrak{M}} = \mathcal{O}_E$, and an integer $A \geq 1$. Put $M' = \operatorname{lcm}(M, A)$ and $K_A = \mathbb{Q}(\rho_0, e^{2\pi i/A})$.
4. A moduli scheme $X^\circ$ over $K_A$: smooth and quasi-projective, with a universal object of unitary PEL type that represents the objects over reduced schemes.
5. A number field $F \subset \mathbb{C}$ that contains $K_A$, $e^{2\pi i/M'}$ and all images of $E$, a ring $O$ with a homomorphism $\beta : O \to F$, and an embedding $b_F : F \to \mathbb{C}$.
6. A model $Y$ of $X^\circ_F$ over $O$: a normal, projective and flat scheme over $O$ with a dense open immersion of $X^\circ_F$ into $Y \otimes_O F$, and a semi-abelian scheme over $Y$ that extends the universal object and is abelian exactly over $X^\circ_F$.
7. Arc data at the boundary: degeneration data $D_0$ over $\mathbb{C}$ with a nontrivial character group $\mathsf{X}$, an action of $\mathcal{O}_E$, $\psi$ even, $\tau$ bimultiplicative, and a positive definite symmetric form $b$ on $\mathsf{X}$ with values in $2M'\mathbb{Z}$, Hermitian for the conjugation.
8. A formal arc $\chi : \operatorname{Spec} \mathbb{C}[[q]] \to Y$ and a witness for it: a semi-abelian scheme over $\mathbb{C}[[q]]$ with a map to the semi-abelian scheme over $Y$ above $\chi$, and a uniformisation of PEL type whose abelian part is the pullback of that of $D_0$.
9. Embeddings $\tau_1, \dots, \tau_g : E \to \mathbb{C}$ and a family of complex uniformisations of $X^\circ$: for finitely many lattices $\Lambda_i$ of signature $(p, q)$, period maps from periods of $\Lambda_i$ to points of $X^\circ(\mathbb{C})$, with exponential maps from $\mathbb{C}^g$ onto the fibres.

**Definition 4.23.1 (Archimedean arc condition).** The *archimedean arc condition* says the following. For all data 1 to 9 such that $b_F$ maps the element $\rho_0$ of $K_A \subset F$ to $\rho_0$, each embedding $\sigma$ of $E$ occurs $p$ times among the $\tau_j$ if $\sigma(\rho) = \rho_0$ and $q$ times otherwise, $O$ has elements that map to $\rho_0$ and $e^{2\pi i/A}$, the composite of $\chi$ with $Y \to \operatorname{Spec} O$ is induced by $b_F \circ \beta$ followed by the constants $\mathbb{C} \to \mathbb{C}[[q]]$, and every point of $\operatorname{Spec} \mathbb{C}[[q]]$ outside $q = 0$ maps into the image of $X^\circ_F$, there is a *holomorphic arc*. This consists of:

1. an index $i$, a real number $T$, and homomorphisms $P_0, N : \Lambda_i \to \mathbb{C}^g$ such that $P(w) = P_0 + wN$ is a period of $\Lambda_i$ of type $(\tau_j)$ for $\operatorname{Im} w > T$;
2. a surjective $\mathcal{O}_E$-linear map $y : \Lambda_i \to \mathsf{X}$;
3. a surjective additive map $\varepsilon$ from $\mathbb{C}^g$ onto the points of the Raynaud extension of $D_0$ over $\mathbb{C}$. It is $\mathcal{O}_E$-linear for the types $\tau_j$ and holomorphic, its kernel is $P_0(\ker y)$, and $\varepsilon(wN v)$ is the torus point with character values $e^{2\pi i w\, b(y(v), x)}$;
4. compatibility with the level structures and a relation between $E_\Lambda$ and the torus points;
5. convergence: for every function $f$ on an open set of $Y$ that contains the arc, the power series $\chi^* f$ converges at $q = e^{2\pi i w}$ to the value of $f$ at the point $P(w)$, for $\operatorname{Im} w$ large;
6. the same convergence for first derivatives along the fibres, and for the expansions of theta sections, which become classical theta functions with characteristics in $\{0, \tfrac12\}$ up to a nonzero constant.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.ToroidalArchimedeanCondition` (also `ReciprocityTheory.ChartRestriction.G.Geo.Tor.HolArc`, the holomorphic arc).

### The theorem

The complex uniformisation of polarised abelian varieties is used in the following form. Every polarised complex abelian variety with a rigidified line bundle is a quotient $\mathbb{C}^g/\Lambda$, holomorphically, with a positive Hermitian form whose imaginary part is the Riemann form on $\Lambda$, a character of $\Lambda$, and an identification of sections with theta functions, together with a formula for the Weil pairing (Mumford, *Abelian Varieties*, Oxford University Press 1970, §1 and §2).

**Theorem 4.23.2 (Archimedean arc condition).** The archimedean arc condition holds.

Lean: `GlobalTheory.arcClause_closed`.

*Proof.* This is [the theorem on holomorphic degeneration arcs](/entry/holomorphic-degeneration-arc-of-uniformisation/) applied to the laws of abelian schemes, which hold without hypotheses, and to the complex uniformisation of polarised abelian varieties. $\square$

The theorem on holomorphic degeneration arcs takes the laws of abelian schemes and the complex uniformisation as hypotheses, and its conclusion is the arc condition. So the only work in this section is to supply the hypotheses. The laws are the same statements that [the theorem on degeneration data](/entry/exists-degeneration-data-uniformisation-of-torsion-count/) assumes.

**Remark 4.23.3 (Formalization).** The theorem is a composition of three results ([ArcClauseClosed.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ArcClauseClosed.lean#L10)): the wrapper `GlobalTheory.T.holomorphic_degenerationArc_of_uniformisation`, the two components of `GlobalTheory.T.abelianScheme_laws_unconditional`, and `GlobalTheory.T.thetaUniformisation_complexAbelianVariety`, a proof of the structure `ReciprocityTheory.ChartRestriction.G.Geo.Tor.ThetaUnifAV`. The wrapper is proved by a `first | exact` tactic over `GlobalTheory.HolomorphicArc.main` ([HolomorphicDegenerationArcOfUniformisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/HolomorphicDegenerationArcOfUniformisationStatement.lean#L7)). The condition is a definition in [HasArcDataIff.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/HasArcDataIff.lean#L208), and the holomorphic arc is the structure at line 109 of the same file, with twenty-four fields. Our list in the definition groups these fields; fields 4 to 6 are much longer in the code. The convergence uses the predicate `ReciprocityTheory.ChartRestriction.G.Geo.Tor.SumsAt`, which sums $\sum_n a_n e^{2\pi i w n}$. The data 1 to 9 are the structures `Host`, `Datum`, `Level`, `Moduli`, `Coeff`, `Model`, `ArcIn`, `ArcWit` and `FamilyUnif`, and our descriptions of items 4, 7 and 8 leave out some fields. In the code, $d \equiv 7 \pmod{16}$ and the other host conditions are fields of `Host`. The reference to Lan is ours.

## Notes and references

The chapter proves [Mumford's construction over a complete normal base](/entry/has-of-base/): degeneration data over a noetherian, integrally closed, complete local domain of characteristic $0$ come from a semi-abelian scheme. Sections 2 to 16 reduce the theorem to data of unitary PEL type and build the semi-abelian scheme from labelled covers, Galois descent and the idempotent factor. Sections 17 to 21 give the tools for the extension of abelian schemes from [complete regular charts](/entry/has-ext-away-map-of-charts/) and the algebraicity of formal endomorphisms. Section 22 proves the converse direction over a complete discrete valuation ring, and this section proves the comparison with the complex uniformisation. The results feed into the steps [on every character](/step/every-character/) and [on characters from the literature](/step/every-character-of-literature/). For the background see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) and [abelian schemes](/learn/abelian-varieties/#abelian-schemes).

The proof follows Faltings and Chai in outline, but it reduces to unitary data with a level structure and constructs the semi-abelian scheme over a modification of the base, then descends it. The degeneration data of Section 22 are obtained in two steps, with a second choice of the trivialisations $\psi$ from one theta section.

Sources:

- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter I, Proposition 2.7, and Chapter II.
- D. Mumford, *An analytic construction of degenerating abelian varieties over complete rings*, Compositio Math. 24 (1972).
- D. Mumford, *Abelian Varieties*, Oxford University Press 1970, §1, §2 and §4, Application 2.
- A. Grothendieck, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS 11 (1961), Théorème 5.4.1.
- R. Hartshorne, *Algebraic Geometry*, Springer 1977, Chapter III, Exercise 5.7(d).
- M. Auslander and D. A. Buchsbaum, *Unique factorization in regular local rings*, Proc. Nat. Acad. Sci. USA 45 (1959).
- K.-W. Lan, *Comparison between analytic and algebraic constructions of toroidal compactifications of PEL-type Shimura varieties*, J. reine angew. Math. 664 (2012).
