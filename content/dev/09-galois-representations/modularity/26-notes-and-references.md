---
title: Notes and references
decls:
  - UpperTheory.ConvolutionTheory.R2.quadBC2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds the [window bound](/proof/vwin/), the last step that the [Galois row](/proof/galois-row/) feeds. Section 1 reduces the window bound to Lemma K and four case counts, under the extended hypotheses and the [base change for unitary groups](/step/base-change-n/). The later sections prove the counts, and the last section proves that the extended hypotheses follow from the [published inputs](/proof/literature/) and the weak descent for unitary groups, through the [Theorem 8.25.5](/entry/published-hypotheses-from-patching-alt/) on extended hypotheses. The CM inputs enter through [the CM inputs](/step/cm-abelian-inputs-from-literature/) of the proof.

The method of the chapter is the method of Ribet for the converse of Herbrand's theorem, with Galois representations of higher rank in place of those of $\mathrm{GL}_2$. A congruence between an Eisenstein series and a cusp form gives a Galois representation whose reduction is reducible and whose extension class is in a Selmer group. The upper bound for the length of the Selmer group then comes from a comparison of a deformation ring with a Hecke algebra. Ribet built unramified extensions of $\mathbb{Q}(\mu_p)$ in this way, and Mazur and Wiles proved the main conjecture of Iwasawa theory over $\mathbb{Q}$ with the same idea in Hida families. The counts here bound the lengths, not only the nonvanishing, and they bound them for all $l$ at once with a polynomial in $l N e$.

Sections 2 to 6 follow Kato's construction of an Euler system of zeta elements in the cohomology of modular curves. The vanishing of two Bloch-Kato Selmer groups for two twists is the form of Kato's main theorem that the chapter needs, and the Hodge-Tate law of smoothed zeta classes is the explicit reciprocity law of Kato in the form for the smoothed classes. The Selmer groups are those of Bloch and Kato. The Euler system argument itself, which turns the norm relations at tame primes into a bound for a Selmer group, is due to Kolyvagin and to Rubin and Kato. Here the argument is proved for the case at hand, and the result is a vanishing, not a bound with an index.

The Eisenstein congruences for Hilbert modular forms in section 7 and the seeds of sections 14 and 16 follow the method of Ribet over totally real fields. The ordinary theory is Hida's theory of ordinary families for $\mathrm{GL}_2$ over totally real fields, and section 19 uses the analogue for definite unitary groups. The modularity theorems of sections 10, 11, 13 and 17 are of Taylor-Wiles type. The patching method is due to Taylor and Wiles; the form for unitary groups in any rank is that of Clozel, Harris and Taylor, and potential automorphy with a change of weight is due to Barnet-Lamb, Gee, Geraghty and Taylor. The proofs here use a deformation ring of the reducible point and a model of it, and the main count of section 17 bounds the length of the model by the valuations of the trace differences at a finite set of points; this is the form of the [Theorem 8.17.7](/entry/main-big/) in rank four.

Automorphic induction from $\mathrm{GL}_2$ over a CM field to $\mathrm{GL}_4$ in sections 8 and 9 is a case of the induction of Arthur and Clozel for cyclic extensions. The proof here goes through a trace identity with an Eisenstein term, in place of the full comparison of trace formulas. The adjoint lifting theorem of section 13 is the analogue for $\mathrm{U}_2$ and $\mathrm{U}_3$ of the theorem of Gelbart and Jacquet on the adjoint lift from $\mathrm{GL}_2$ to $\mathrm{GL}_3$. The base change for unitary groups is due to Labesse, after the work of Rogawski in rank three; the descent to definite unitary groups and the multiplicity one statement of section 18 are in the line of the stable trace formula and of the endoscopic classification of Mok. The factorization of forms in section 18 is the tensor product theorem of Flath.

The linked characters of section 20 are the condition that two characters of the inertia at a place above $l$ are not congruent after a twist by a power of the cyclotomic character. The [Theorem 8.20.7](/entry/linked-unl-e-alt/) of section 20 proves that the points of case V are unlinked, and the end statements of section 21 use it. The two counts I and V are of the same form as the count of section 17, with a deformation ring of rank three.

The Weil representation of section 23 is that of Weil, and the Fock model is the model of Bargmann and Segal. The theta correspondence for dual pairs is due to Howe, and the global theta lift with its nonvanishing is in the work of Rallis. The base change for $\mathrm{GL}_2$ along a quadratic extension is due to Langlands, by a comparison of trace formulas; the [Theorem 8.23.11](/entry/quad-bc2/) of section 23 proves the form of the extended hypotheses from the Weil representation of a two-dimensional quadratic space, so the result is in the line of the theta lifts of Shimura, Shintani and Kudla, not of Langlands' proof.

The Asai $L$-function of section 24 is the twisted tensor $L$-function of Asai, and its analytic properties are due to Flicker. The characterization of the image of base change from $\mathrm{GL}_2$ over $\mathbb{Q}$ to $\mathrm{GL}_2$ over an imaginary quadratic field by the pole of the Asai $L$-function is due to Harder, Langlands and Rapoport, and to Flicker. The [Theorem 8.24.4](/entry/asai-nv/) on Asai nonvanishing uses the theorem of Landau on Dirichlet series with nonnegative coefficients. The [Theorem 8.24.7](/entry/desc-s/) on descent is the form that the extended hypotheses need.

The conjugation theorem of section 25 is Clozel's theorem on the rationality of regular algebraic cuspidal representations. Its proof uses the injectivity of cuspidal cohomology into the full cohomology, which goes back to Borel. The cyclic base change of section 25 is the base change of Arthur and Clozel. The strong multiplicity one theorem is due to Jacquet and Shalika, after Piatetski-Shapiro for $\mathrm{GL}_2$; the uniqueness of Whittaker models is due to Gelfand and Kazhdan. The Galois representations of regular algebraic cuspidal representations over CM fields are due to Harris and Taylor, Shin, and Chenevier and Harris, and the local-global compatibility at places that do not divide $l$ is due to Caraiani. The CM inputs include the theorem of Serre and Tate on good reduction, the main theorem of complex multiplication, the theorem of Siegel and Klingen with that of Deligne and Ribet on the values of partial zeta functions, and Tate's thesis for the functional equation of Hecke $L$-functions.

- K. A. Ribet, *A modular construction of unramified p-extensions of Q(μ_p)*, Invent. Math. 34 (1976), 151 to 162.
- B. Mazur and A. Wiles, *Class fields of abelian extensions of Q*, Invent. Math. 76 (1984), 179 to 330.
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117 to 290.
- S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in The Grothendieck Festschrift, Vol. I, Progr. Math. 86, Birkhäuser, 1990, 333 to 400.
- J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, 2nd ed., Grundlehren Math. Wiss. 323, Springer, 2008, Chapter VII (local duality and the local Euler characteristic) and Chapter VIII (Poitou-Tate duality).
- H. Hida, *On p-adic Hecke algebras for GL_2 over totally real fields*, Ann. of Math. 128 (1988), 295 to 384.
- A. Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Ann. of Math. 141 (1995), 443 to 551.
- R. Taylor and A. Wiles, *Ring-theoretic properties of certain Hecke algebras*, Ann. of Math. 141 (1995), 553 to 572.
- L. Clozel, M. Harris and R. Taylor, *Automorphy for some l-adic lifts of automorphic mod l Galois representations*, Publ. Math. IHÉS 108 (2008), 1 to 181.
- R. Taylor, *Automorphy for some l-adic lifts of automorphic mod l Galois representations II*, Publ. Math. IHÉS 108 (2008), 183 to 239.
- T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor, *Potential automorphy and change of weight*, Ann. of Math. 179 (2014), 501 to 609.
- J. Arthur and L. Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Ann. of Math. Stud. 120, Princeton Univ. Press, 1989, Chapter 3 (global base change and automorphic induction).
- S. Gelbart and H. Jacquet, *A relation between automorphic representations of GL(2) and GL(3)*, Ann. Sci. École Norm. Sup. 11 (1978), 471 to 542.
- D. Flath, *Decomposition of representations into tensor products*, in Automorphic Forms, Representations and L-functions, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 179 to 183.
- H. Jacquet and J. A. Shalika, *On Euler products and the classification of automorphic representations I*, Amer. J. Math. 103 (1981), 499 to 558, and *II*, Amer. J. Math. 103 (1981), 777 to 815.
- I. I. Piatetski-Shapiro, *Multiplicity one theorems*, in Automorphic Forms, Representations and L-functions, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 209 to 212.
- L. Clozel, *Motifs et formes automorphes: applications du principe de fonctorialité*, in Automorphic Forms, Shimura Varieties, and L-functions, Vol. I, Perspect. Math. 10, Academic Press, 1990, 77 to 159, Théorème 3.13.
- A. Borel, *Stable real cohomology of arithmetic groups*, Ann. Sci. École Norm. Sup. 7 (1974), 235 to 272.
- R. Kottwitz, *Base change for unit elements of Hecke algebras*, Compositio Math. 60 (1986), 237 to 250.
- A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), 143 to 211.
- R. Howe, *θ-series and invariant theory*, in Automorphic Forms, Representations and L-functions, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 275 to 285.
- S. Rallis, *Langlands' functoriality and the Weil representation*, Amer. J. Math. 104 (1982), 469 to 515.
- T. Asai, *On certain Dirichlet series associated with Hilbert modular forms and Rankin's method*, Math. Ann. 226 (1977), 81 to 94.
- Y. Z. Flicker, *Twisted tensors and Euler products*, Bull. Soc. Math. France 116 (1988), 295 to 313.
- G. Harder, R. P. Langlands and M. Rapoport, *Algebraische Zyklen auf Hilbert-Blumenthal-Flächen*, J. Reine Angew. Math. 366 (1986), 53 to 120.
- G. Chenevier and M. Harris, *Construction of automorphic Galois representations II*, Camb. J. Math. 1 (2013), 53 to 73.
- S. W. Shin, *Galois representations arising from some compact Shimura varieties*, Ann. of Math. 173 (2011), 1645 to 1741.
- A. Caraiani, *Local-global compatibility and the action of monodromy on nearby cycles*, Duke Math. J. 161 (2012), 2311 to 2413.
- G. Henniart, *Une preuve simple des conjectures de Langlands pour GL(n) sur un corps p-adique*, Invent. Math. 139 (2000), 439 to 455.
- J.-P. Serre and J. Tate, *Good reduction of abelian varieties*, Ann. of Math. 88 (1968), 492 to 517.
- P. Deligne and K. A. Ribet, *Values of abelian L-functions at negative integers over totally real fields*, Invent. Math. 59 (1980), 227 to 286.
- J. Tate, *Fourier analysis in number fields and Hecke's zeta-functions*, in Algebraic Number Theory (J. W. S. Cassels and A. Fröhlich, eds.), Academic Press, 1967, Chapter XV, 305 to 347.
- B. Ferrero and L. C. Washington, *The Iwasawa invariant μ_p vanishes for abelian number fields*, Ann. of Math. 109 (1979), 377 to 395.
