---
title: Integrality of Hecke operators
decls:
  - GlobalTheory.HkIntegral.heckeInt
  - GlobalTheory.HkIntegral.heckeFrameInt
  - GlobalTheory.HkIntegral.exists_frBor_unit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integrality of Hecke operators

This section proves that Hecke operators keep integrality at the places of the coefficient field that do not lie over the Hecke prime. Let $y$ be an integral framed point over a complete discrete valuation ring and let $z$ be a Hecke point of $y$ over an algebraically closed field. We show that $z$, after a finite extension of the ring, is an integral framed point changed by a diagonal of units. A section with integral values at all integral points then has an integral value at $z$. The main input is [the lemma that the theta entry is a unit](/entry/theta-unit/). The result is the integrality part of [the Hecke integrality, transform and reading facts](/entry/hecke-int-transform-read-tie/). The classical model is the fact that for primes $l \ne p$ the operator $T_p$ keeps the modular forms whose values at elliptic curves with good reduction at $l$ are $l$-integral ([modular forms](/learn/automorphic-forms/#modular-forms)).

### Integrality up to units

We keep the notation of the section before: $T$ is a complete discrete valuation ring with fraction field $K$ and normalized valuation $v_T$, $\iota : F_c \to K$ is a field map, integral framed points have integral data, and $z = t \cdot y$ means that $z$ comes from $y$ by the triangular change with diagonal $t$. For a map $k : K \to \Omega$ to a field, $y_\Omega$ is the base change of $y$ along $k$.

**Definition 6.12.1 (Integral up to units).** Let $k : K \to \Omega$ be a field map and let $z$ be a framed point over $\Omega$. Then $z$ is *integral up to units* for a class $\mathcal{C}$ if there are:

1. a complete discrete valuation ring $T'$ with fraction field $K'$ and a field map $i : K \to K'$, with $K'$ finite over $i(K)$ and $v_{T'}(i(a)) = r\, v_T(a)$ for a fixed integer $r > 0$;
2. a map $j : K' \to \Omega$ over $F_c$ with $j \circ i = k$;
3. an algebraic integral framed point $y'$ over $(T', i \circ \iota)$ in the class $\mathcal{C}$;
4. a tuple $u$ of units of $T'$,

such that $z = j(u) \cdot y'_\Omega$, where $y'_\Omega$ is the base change of $y'$ along $j$.

**Lemma 6.12.2 (Hecke points are integral up to units).** Let $p_0$ be prime and a unit in $T$, and let the residue field of $T$ be finite. Let $y$ and $y_0$ be integral framed points over $(T, \iota)$, and let $z$ be a Hecke point of $y$ over $K$ that lies over the same point of $X$ as $y_0$. Then there are an integral framed point $y'$ over $(T, \iota)$ and a tuple $u$ of units of $T$ with $z = u \cdot y'$. If $y$ is good, then $y'$ is good.

Lean: `GlobalTheory.HkIntegral.exists_frBor_unit`.

*Proof.* The isogeny $\psi$ extends to a map of the integral data of $y$ and $y_0$. The tangent law says that $\psi$ carries $u_{\tau,j}(y)$ to $p_0^{-1}$ times the image of $u_{\tau,j}(z)$. Since $p_0$ is a unit, the map of Lie lattices of the models is onto after the factor $p_0^2$, and so the tangent bases of $z$ are $T$-bases of the Lie lattice of the model of $y_0$. We change the frame of $y_0$ to these bases. This gives an integral framed point $y'$ on the same point of $X$, whose tangent bases are those of $z$. Then $z = t \cdot y'$ for a tuple $t$ with $t_{\tau,j} = 1$ for all $(\tau, j)$. By the lemma on the theta entry, $v_T(t_0) = 0$, so $t_0$ is a unit $u_0$ of $T$. Take $u = (u_0, (1))$.

If $y$ is good, its integral datum is an abelian scheme $\mathcal{G}$. The isogeny $\psi$ extends to an isogeny of models from $\mathcal{G}$ to the model $\mathcal{G}'$ of $y'$, and the target of an isogeny from a proper model is proper. So $y'$ is good. $\square$

### Frame and value integrality

Let $\lambda$ be a finite place of $F_c$. Say that $(T, \iota)$ lies over $\lambda$ with index $e > 0$ if $v_T(\iota(a)) = e\, v_\lambda(a)$ for all $a \in F_c$. For a section $f$ and an algebraic integral framed point $y$ over $(T, \iota)$ over $\lambda$ with index $e$, the normalized valuation of $f$ at $y$ is $v_T(f(y))/e$. The *integral valuations* at $\lambda$ are these maps $f \mapsto v_T(f(y))/e$, over all such $y$.

**Theorem 6.12.3 (Frame integrality).** Let $\mathcal{C}$ be a class of integral points with this property: if $y$ is in $\mathcal{C}$, and $y'$ is good whenever $y$ is good, then $y'$ is in $\mathcal{C}$. Let $\lambda$ be a finite place of $F_c$ with $p_0 \notin \lambda$, let $(T, \iota)$ lie over $\lambda$, and let $y$ be an algebraic integral framed point over $(T, \iota)$ in $\mathcal{C}$. Let $\Omega$ be an algebraically closed field, algebraic over $K$ by a map $k$, let $C$ be a Hecke kernel at $y_\Omega$, and let $z$ be a Hecke point of $C$. Then $z$ is integral up to units for $\mathcal{C}$.

Lean: `GlobalTheory.HkIntegral.heckeFrameInt`.

*Proof.* Since $p_0 \notin \lambda$ and $T$ lies over $\lambda$, $p_0$ is a unit in $T$. The Hecke isogeny over $\Omega$ has an inverse up to $p_0^2$ which is linear, so the Hecke point $z$ and its isogeny are defined over a finite extension $L$ of $K$ in $\Omega$: there is a Hecke point $z_1$ of $y_L$ over $L$ whose base change to $\Omega$ is $z$. Let $T_1$ be the complete discrete valuation ring of $L$ over $T$. Its residue field is finite, since that of $T$ is finite and $L$ is finite over $K$. After a second finite extension $T_2$ of $T_1$, the point of $X$ under $z_1$ carries an integral frame $y_0$. Let $y_2$ be the base change of $y$ to $T_2$, which is again integral, and good if $y$ is good. By the last lemma, applied over $T_2$ to $y_2$, $y_0$ and the base change of $z_1$, there are an integral $y'$ over $T_2$ and units $u$ of $T_2$ with $z_1 = u \cdot y'$ over $T_2$, and $y'$ is good if $y_2$ is good. The map $L \to \Omega$ extends to a map $j$ from the fraction field of $T_2$ to $\Omega$ with $j \circ i = k$, where $i : K \to K_2$ is the composite. Then $z = j(u) \cdot y'_\Omega$. The valuations scale by the product of the two indices, and $T_2$ has finite residue field, so $y'$ is algebraic. The property of $\mathcal{C}$ puts $y'$ in $\mathcal{C}$. $\square$

**Theorem 6.12.4 (Integrality of Hecke values).** For the good class and for the full class, both of the following hold, under the hypotheses of frame integrality:

1. $z$ is integral up to units for the class;
2. $z$ comes from a test ring, and for every section $f$ of weight $(a, n)$ that has $w(f) \ge 0$ for every integral valuation $w$ at $\lambda$, the value $f(z)$ is integral over $T$ under $k$.

Lean: `GlobalTheory.HkIntegral.heckeInt`.

*Proof.* Both classes have the property of frame integrality: the good class by its definition, and the full class because it holds for every point. So part 1 is frame integrality. For part 2, the point $z$ is over the field $\Omega$, which is a local ring, so $z$ comes from a test ring. Take $T'$, $i$, $j$, $y'$ and $u$ as in part 1. By the weight law and base change,
$$f(z) = \chi_{a,n}(j(u))\, f(y'_\Omega) = j\big(\chi_{a,n}(u)\, f(y')\big).$$
The point $y'$ is algebraic and lies over $\lambda$ with index $r e$, so $v_{T'}(f(y'))/(re) \ge 0$ by hypothesis. Thus $f(y') \in T'$, and $\chi_{a,n}(u) f(y') \in T'$ since $u$ is a tuple of units. The ring $T'$ is finite over $T$, so every element of $T'$ is integral over $T$. Applying $j$ gives a monic polynomial over $T$ that $f(z)$ satisfies under $k$. $\square$

The full class gives the stronger statement for values, since its hypothesis on $y$ is weaker. The good class is kept because its frame statement gives a good $y'$, which the full class does not.

**Remark 6.12.5 (Formalization).** The three results are in [IsUnitNatCastUp.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsUnitNatCastUp.lean#L403), at lines 286, 327 and 403; value integrality for one class is `heckeValueInt` (line 376). The classes and the two integrality properties are in [HeckeValueIntegrality.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/HeckeValueIntegrality.lean#L11), whose namespace is `GlobalTheory.IndefiniteRowSideFullHecke.UnusedSlot39` (line 11), a placeholder name. The full class is `trivialClassCondition`, the condition `fun _ _ _ => True` (line 36). A class with a similar name, `trivCls` in [RegularityR2Quotient.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/RegularityR2Quotient.lean#L12), is not trivial: it asks that each nonzero element of $F_c$ go to a unit of $T$. The example at line 83 shows that value integrality for the full class gives it for the good class, so the good part of `HeckeInt` (line 79) repeats the value statement. The theorems are stated for every CM field, moduli space and coefficient datum at once, and the proof of frame integrality uses `intFrExt` (line 324 of IsUnitNatCastUp.lean), which splits on whether the signature has rank zero.

## Notes and references

The results of this chapter feed the later volumes and the final steps. Newforms and strong multiplicity one go into [the newform attached to a twist](/entry/exists-newform-attached-twist-of-kills-mu/) and [the window of automorphy](/entry/v-window-of-automorphy-csd-ss-mono-odd/), and the cohomology bounds into [the window of hypotheses](/entry/vwin-of-hypotheses-h-e-alt/). Hilbert Eisenstein series of weight one go into [the seed](/entry/seed-iis-alt/), and the weight congruences of the trace formula into [the mixed seed](/entry/mix-seed-of-alt/). The harmonic representatives go into [the conjugate representations theorem](/entry/clozel-conj-c/), and the row placement into [the placement of a realisation](/entry/placement-of-realisation-alt/). The definite good vectors and the scalar identity go into [large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/) and [twisted scalar conjugation](/entry/twisted-scalar-conjugation/). Sections 9 to 12 are collected in [the Hecke integrality, transform and reading facts](/entry/hecke-int-transform-read-tie/). Strong multiplicity one and the existence of local parameters are used in the step [EveryCharacter](/step/every-character/), the count of primes of norm form in [the step from theta integrals and local matching](/step/theta-local-matching/), and the parameters of cuspidal representations in [the local Langlands existence step](/step/rect-exists/). The background is in Volume 1: [modular forms](/learn/automorphic-forms/#modular-forms), [Hecke characters](/learn/class-field-theory/#hecke-characters), [the local Langlands correspondence](/learn/galois-representations/#the-local-langlands-correspondence) and [the global theta lift](/learn/theta/#the-global-theta-lift).

- A. O. L. Atkin and J. Lehner, Hecke operators on $\Gamma_0(m)$, Math. Ann. 185 (1970), 134 to 160.
- A. Borel and J.-P. Serre, Corners and arithmetic groups, Comment. Math. Helv. 48 (1973), 436 to 491.
- A. Borel and N. Wallach, *Continuous Cohomology, Discrete Subgroups, and Representations of Reductive Groups*, 2nd ed., Math. Surveys Monogr. 67, Amer. Math. Soc., 2000, Chapters I, II and VII.
- D. Bump, *Automorphic Forms and Representations*, Cambridge Stud. Adv. Math. 55, Cambridge University Press, 1997, Section 3.7.
- W. Casselman, On some results of Atkin and Lehner, Math. Ann. 201 (1973), 301 to 314.
- L. Clozel, Motifs et formes automorphes: applications du principe de fonctorialité, in *Automorphic Forms, Shimura Varieties, and L-functions*, Vol. I, Perspect. Math. 10, Academic Press, 1990, 77 to 159.
- P. Deligne and J.-P. Serre, Formes modulaires de poids 1, Ann. Sci. École Norm. Sup. 7 (1974), 507 to 530.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergeb. Math. Grenzgeb. 22, Springer, 1990, Chapters III and VII.
- J. A. Green, The characters of the finite general linear groups, Trans. Amer. Math. Soc. 80 (1955), 402 to 447.
- B. H. Gross, Algebraic modular forms, Israel J. Math. 113 (1999), 61 to 93.
- M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Ann. of Math. Stud. 151, Princeton University Press, 2001, Chapter VII.
- G. Henniart, Une preuve simple des conjectures de Langlands pour GL(n) sur un corps p-adique, Invent. Math. 139 (2000), 439 to 455.
- H. Hida, Galois representations into $\mathrm{GL}_2(\mathbb{Z}_p[[X]])$ attached to ordinary cusp forms, Invent. Math. 85 (1986), 545 to 613.
- R. Howe, $\theta$-series and invariant theory, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 275 to 285.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Amer. Math. Soc. Colloq. Publ. 53, 2004, Chapter 5.
- H. Jacquet and J. A. Shalika, On Euler products and the classification of automorphic representations I, Amer. J. Math. 103 (1981), 499 to 558; II, 777 to 815.
- N. M. Katz, p-adic properties of modular schemes and modular forms, in *Modular Functions of One Variable III*, Lecture Notes in Math. 350, Springer, 1973, 69 to 190.
- D. Mumford, On the equations defining abelian varieties I, Invent. Math. 1 (1966), 287 to 354.
- D. Mumford, An analytic construction of degenerating abelian varieties over complete rings, Compositio Math. 24 (1972), 239 to 288.
- D. Mumford, *Abelian Varieties*, Tata Inst. Fund. Res. Stud. Math. 5, Oxford University Press, 1970, Section 23.
- I. I. Piatetski-Shapiro, Multiplicity one theorems, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 209 to 212.
- S. Rallis, Langlands' functoriality and the Weil representation, Amer. J. Math. 104 (1982), 469 to 515.
- P. Scholze, The local Langlands correspondence for $\mathrm{GL}_n$ over p-adic fields, Invent. Math. 192 (2013), 663 to 715.
- J. A. Shalika, The multiplicity one theorem for $\mathrm{GL}_n$, Ann. of Math. 100 (1974), 171 to 193.
- G. Shimura, The special values of the zeta functions associated with Hilbert modular forms, Duke Math. J. 45 (1978), 637 to 679.
- A. Wiles, On ordinary $\lambda$-adic representations associated to modular forms, Invent. Math. 94 (1988), 529 to 573.
