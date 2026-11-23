---
title: The arithmetic intersection calculus from Poincaré-Lelong and resolution
decls:
  - GlobalTheory.ArithmeticHeightTower.ArakelovDirectHeights.arCalc_direct
  - GlobalTheory.ArithmeticHeightTower.Read1.bridge3
  - GlobalTheory.CompanionTheory.MPDict.projQ_direct
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The arithmetic intersection calculus from Poincaré-Lelong and resolution

This section proves the seven rules of arithmetic intersection theory for hermitian line bundles on arithmetic varieties: existence of heights and intersection forms, the change of metric formula, the shift formula, the mixed formula through a rational section, the projection formula, invariance under isometries, and the formula for a raised metric. The hypotheses are the Poincaré-Lelong formula of [the section on that formula](/entry/poincare-lelong-of-leaves/) and a form of resolution of singularities with projective coordinates. The proof builds an intersection system from the two hypotheses, proves three statements on closed subvarieties of multiprojective spaces over $\mathbb{Z}$, and transfers them to all arithmetic varieties. The rules are used in [the step on the published results](/step/every-character-of-literature/), which supplies both hypotheses. It is a second route to [the calculus from principalisation](/entry/ar-calc-of-principalisation/).

### Heights and intersection forms

Let $k$ be a commutative ring and let $p : X \to \operatorname{Spec} k$ be an arithmetic variety of relative dimension $D$, with $X$ integral. A hermitian line bundle $\bar L$ on $X$ is a line bundle, given by a cover and a cocycle, with a smooth weight at each embedding $\sigma : k \to \mathbb{C}$, compatible with complex conjugation. For a family $(\bar L_j)_{j \in \iota}$ and $n \in \mathbb{Z}^\iota$ we write $\bar L^n = \bigotimes_j \bar L_j^{n_j}$, and $\ell_n = \sum_j n_j x_j$ for the linear form in the variables $x_j$.

**Definition 4.15.1 (Height function).** A height function for $\bar L$ is a function $h$ on the points of $X$ with three properties.
- Vertical points. If $Z \subseteq X$ is an integral closed subscheme of dimension $d$ over a finite field $\kappa$, then $h(Z) = (L|_Z)^d \log \#\kappa$, where $(L|_Z)^d$ is the algebraic self intersection number.
- Curves. If $Z$ is an integral closed subscheme of dimension $1$ in characteristic $0$, then $h(Z)$ is the arithmetic degree of $\bar L|_Z$, computed from any rational section.
- Recursion. If $Z$ has dimension $e + 1 \ge 2$ in characteristic $0$ and $r$ is a rational section of $\bar L|_Z^{\,m}$, then
$$m\, h(Z) = \sum_{z} \operatorname{mult}_z(\operatorname{div} r)\, h(z) - \int_{Z(\mathbb{C})} \log\|r\|\, c_1(\bar L)^{e},$$
and the integral exists.

A real number $a$ is a self intersection of $\bar L$ if some height function $h$ has $h(X) = a$ at the generic point.

**Definition 4.15.2 (Intersection form).** Let $(\bar L_j)_{j \in \iota}$ be a finite family. An arithmetic intersection form is a real linear map $\Phi$ on the polynomials in $(x_j)$ that vanishes on homogeneous polynomials of degree other than $D + 1$, such that $\Phi(\ell_n^{D+1})$ is a self intersection of $\bar L^n$ for every $n$. A geometric form $\Psi$ is defined in the same way with degree $D$ and $\Psi(\ell_n^D) = \int c_1(\bar L^n)^D$.

So $\Phi$ is the polarization of the self intersection number.

**Definition 4.15.3 (The calculus).** The arithmetic intersection calculus is the conjunction of seven rules, each for all arithmetic varieties $X$ of relative dimension $D$.
1. Existence: every $\bar L$ has a height function, and every finite family has an arithmetic and a geometric intersection form.
2. Change: for the trivial bundle $\mathcal{O}(u)$ with weight $u$, and an arithmetic form $\Phi$ of the family $(\mathcal{O}(u), \bar L_j)$, $\Phi(x_0\, \ell_n^D) = \frac12 \int u\, c_1(\bar L^n)^D$.
3. Shift: if $a$ is a self intersection of $\bar L$, then $a + (D + 1)\, t \deg \bar L$ is a self intersection of $\bar L$ with its weight shifted by $t$, where $\deg \bar L = \int c_1(\bar L)^D$.
4. Mixed formula: for an arithmetic form $\Phi$ of $(\bar M, \bar L_j)$, a height function $h$ of $\bar L^n$ and a rational section $r$ of $\bar M$,
$$\Phi(x_0\, \ell_n^D) = \sum_z \operatorname{mult}_z(\operatorname{div} r)\, h(z) - \int \log\|r\|\, c_1(\bar L^n)^D.$$
5. Projection: for a morphism $\pi : Y \to X$ of arithmetic varieties of the same dimension that maps the generic point to the generic point with nonzero residue degree $\delta$, self intersections and intersection forms are multiplied by $\delta$ under pull back.
6. Isometry: isometric bundles have the same height functions and forms, a form gives self intersections of the bundles in the family, and a form changes by substitution under a change of the family to integer combinations.
7. Metric: if the weight of $\bar M$ is raised by $u$, the value $\Phi(x_0\, \ell_n^D)$ increases by $\frac12 \int u\, c_1(\bar L^n)^D$.

### Multiprojective spaces over the integers

Let $\mathbb{P}_{m,n} = \mathbb{P}^{n_0}_{\mathbb{Z}} \times \dots \times \mathbb{P}^{n_m}_{\mathbb{Z}}$. A twisted bundle on $\mathbb{P}_{m,n}$ is a hermitian line bundle whose line bundle is isomorphic to a twist, with an integer exponent $t$, built from the pull backs of $\mathcal{O}(1)$ from the factor $c + 1$ and from the factor $0$. For $n' \ge 0$, let $Q = \mathbb{P}^{n'}_{\mathbb{Z}} \times \mathbb{P}_{m,n}$ with the second projection $q : Q \to \mathbb{P}_{m,n}$.

**Definition 4.15.4 (Three ambient statements).**
- FormZ: for every integral closed subscheme $X \subseteq \mathbb{P}_{m,n}$ that is an arithmetic variety of relative dimension $D$, and every finite family of twisted bundles, the restrictions to $X$ have an arithmetic intersection form.
- MixZ: for the same $X$ and twisted bundles $\bar M$ and $(\bar L_j)$, the mixed formula of rule 4 holds for the restrictions.
- ProjQ: let $Y \subseteq Q$ be an integral closed subscheme that is an arithmetic variety of relative dimension $e$, such that the closure of $q(Y)$ has dimension $e + 1$ and $q$ has nonzero residue degree $\delta$ at the generic point of $Y$. Let $\bar M$ be twisted, let $h$ be a height function of $\bar M$ and let $h'$ be a height function of $q^*\bar M$. Then $h'(Y) = \delta\, h(q(Y))$.

**Lemma 4.15.5 (Bridge).** FormZ, MixZ and ProjQ imply three rules for all arithmetic varieties: every finite family has an arithmetic intersection form, the mixed formula holds, and the height projection formula holds: for a morphism $\pi : Y \to X$ over $k$ with $Y$ of relative dimension $e$, the closure of $\pi(Y)$ of dimension $e + 1$ and nonzero residue degree $\delta$ at the generic point of $Y$, if $h$ is a height function of $\bar L$, then $\delta\, h(\pi(Y))$ is a self intersection of $\pi^* \bar L$.

Lean: `GlobalTheory.ArithmeticHeightTower.Read1.bridge3`

*Proof.* The first step reduces to base $\mathbb{Z}$: an arithmetic variety over $k$ is also one over $\mathbb{Z}$, with the same heights and forms. Over $\mathbb{Z}$, every arithmetic variety $X$ with a finite family $(\bar L_j)$ has a closed immersion $i : X \to \mathbb{P}_{m,n}$ and twisted bundles $\bar M_j$ with $i^*\bar M_j$ isometric to $\bar L_j$. The metrics are extended from $X$ to $\mathbb{P}_{m,n}$.

For forms, FormZ gives a form $\Phi$ for $(i^*\bar M_j)$. Since $\bar L^n$ is isometric to $i^* \bar M^n$, the values $\Phi(\ell_n^{D+1})$ are also self intersections of $\bar L^n$, so $\Phi$ is a form for $(\bar L_j)$. The mixed formula follows in the same way from MixZ and the invariance of the mixed formula under isometries.

For projection, FormZ and MixZ first give height functions for every twisted bundle on $\mathbb{P}_{m,n}$ and on $Q$: the recursion with the mixed formula produces them. Let $\pi : Y \to X$ be as in the lemma. Embed $X$ by $i$ into $\mathbb{P}_{m,n}$ with $\bar L \cong i^*\bar M$, and embed $Y$ into some $\mathbb{P}^{n'}_{\mathbb{Z}}$. The pair gives a closed immersion $j : Y \to Q$ with $q \circ j = i \circ \pi$. A height function of $\bar L$ is unique, so $h$ is the restriction of the height function $h_M$ of $\bar M$. ProjQ, applied to $j(Y)$ and the height function $h'$ of $q^*\bar M$, gives $h'(Y) = \delta\, h_M(i(\pi(Y))) = \delta\, h(\pi(Y))$, and $h'$ restricts to a height function of $\pi^*\bar L$. $\square$

### The projection statement

An intersection system $I$ is a function that assigns a real number $I(P; \bar A_1, \dots, \bar A_d)$ to an arithmetic variety $P$ of dimension $d$ in a multiprojective space over $\mathbb{Z}$ and a family of $d$ hermitian line bundles. It is full if it satisfies the recursion of the previous sections, is multilinear, satisfies the projection formula for coordinate maps, and is compatible with contraction of mixed families.

**Lemma 4.15.6 (ProjQ from an intersection system).** Assume that a full intersection system exists and that resolution of singularities with projective coordinates holds. Then ProjQ holds.

Lean: `GlobalTheory.CompanionTheory.MPDict.projQ_direct`

*Proof.* Let $I$ be a full intersection system. Every twisted bundle $\bar M$ is represented by a hermitian line $A$ on the multigraded ring of $\mathbb{P}_{m,n}$, and $q^*\bar M$ by the pull back line of $A$ on the ring of $Q$; both are smooth. The first fact is that heights are intersection numbers: if $h$ is a height function of $\bar M$ and $x$ is a point whose closure is an arithmetic variety of dimension $d$, then
$$h(x) = I(\overline{\{x\}}; A, \dots, A).$$
This uses the resolution hypothesis, which gives the rationality of a resolution and the integrability of the archimedean terms.

Let $y$ be the generic point of $Y$. Its closure is an arithmetic variety of dimension $e + 1$, and so is the closure of $q(y)$, by the dimension hypothesis. By the first fact,
$$h'(y) = I(\overline{\{y\}}; q^*A, \dots), \qquad h(q(y)) = I(\overline{\{q(y)\}}; A, \dots).$$
The ideal of $\overline{\{q(y)\}}$ is the image of the ideal of $\overline{\{y\}}$ under the coordinate map of $q$. The projection formula of the full system, for this coordinate map, says that $I(\overline{\{y\}}; q^*A, \dots)$ is the degree of the extension of function fields times $I(\overline{\{q(y)\}}; A, \dots)$. That degree equals the residue degree $\delta$ of $q$ at $y$. So $h'(y) = \delta\, h(q(y))$. $\square$

### The theorem

**Theorem 4.15.7 (Arithmetic intersection calculus).** Assume the arithmetic Poincaré-Lelong formula and resolution of singularities with projective coordinates. Then the seven rules of the arithmetic intersection calculus hold.

Lean: `GlobalTheory.ArithmeticHeightTower.ArakelovDirectHeights.arCalc_direct`

*Proof.* First, the Poincaré-Lelong formula and resolution give a full intersection system $I$. The intersection family comes from [the existence theorem for intersection families](/entry/intersection-exists-of-poincare-lelong/), whose recursion starts with [the product formula in dimension one](/entry/inter-r1-indep/). Resolution also gives the projection formula.

Second, $I$ and resolution give the three ambient statements. For FormZ, the polarization of $n \mapsto I(X; \bar M^n, \dots, \bar M^n)$ is an arithmetic intersection form, because $I$ is multilinear and heights are intersection numbers. For MixZ, the mixed formula is the recursion of $I$, read through the same dictionary between heights and intersection numbers. ProjQ is the lemma above.

Third, the bridge lemma turns FormZ, MixZ and ProjQ into the existence of forms, the mixed formula and the height projection formula on all arithmetic varieties.

Fourth, these three rules imply the seven rules. Height functions and geometric forms exist by an induction on the dimension with the forms and the mixed formula, which gives rule 1. Rule 2 follows from rules 1 and 4, since the trivial bundle has the rational section $1$ with no divisor. Rule 3 follows from rules 1 and 2, for a constant weight. Rule 5 follows from the height projection formula. Rule 6 holds without hypotheses. Rule 7 follows from rules 1 and 4. $\square$

**Example 4.15.8.** Take $X = \operatorname{Spec} \mathbb{Z}$, of relative dimension $0$, and the trivial bundle with $\|1\| = e^{-t}$ at the complex point. The height of the generic point is the arithmetic degree $-\log\|1\| = t$. The geometric degree is $\int c_1^0 = 1$. So rule 3 says that the shift by $t$ changes the self intersection $0$ of the trivial bundle to $0 + 1 \cdot t \cdot 1 = t$, as the direct computation gives.

**Remark 4.15.9 (Formalization).** The theorem ([CycleHeightsDirect.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/CycleHeightFormulas/CycleHeightsDirect.lean#L138)) is not closed: it takes `PoincareLelong` and `ResKStatement` as hypotheses, and its callers supply them. The three ambient statements are in [QpSndStr.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/QpSndStr.lean#L37), the bridge in [HeightsOfFormMix.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/HeightsOfFormMix.lean#L25), and the seven rules in [EqOfIsometricTrivShift.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/EqOfIsometricTrivShift.lean#L161). The last step goes through `arithIntersectionCalculus_of_form_mixed_projection`, a wrapper of the form `first | exact @... | ...` around the published proof. The lemma `projQ_direct` reads the projection formula from the third field of the full system and identifies the field degree with the residue degree.

## Notes and references

The intersection numbers of Sections 12, 13 and 15 follow the arithmetic intersection theory of H. Gillet and C. Soulé, *Arithmetic intersection theory*, Publ. Math. IHÉS 72 (1990), and the heights of cycles of J.-B. Bost, H. Gillet and C. Soulé, *Heights of projective varieties and positive Green forms*, J. Amer. Math. Soc. 7 (1994). The recursive definition through a section, with the Green function $\log\|s\|$ and the integral against Chern forms, is the one of Bost, Gillet and Soulé; for subvarieties of projective space a definition of this kind is in G. Faltings, *Diophantine approximation on abelian varieties*, Ann. of Math. 133 (1991). The product formula of Section 13 and the arithmetic degree in dimension one are classical; see E. Bombieri and W. Gubler, *Heights in Diophantine Geometry*, Cambridge University Press (2006).

The Poincaré-Lelong formula of Section 12 is due to P. Lelong; for the form used here see J.-P. Demailly, *Complex Analytic and Differential Geometry*, and P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley (1978). The Chern integral of Section 10 is the comparison of Chern forms with intersection numbers in Griffiths and Harris; the algebraic intersection numbers are defined by the Euler characteristic polynomials of E. Snapper, as in S. Kleiman, *Toward a numerical theory of ampleness*, Ann. of Math. 84 (1966). Resolution of singularities is due to H. Hironaka, Ann. of Math. 79 (1964).

The successive minima bounds of Section 14 are due to S. Zhang, *Positive line bundles on arithmetic varieties*, J. Amer. Math. Soc. 8 (1995). Absolute Siegel lemmas, with a field extension as in Section 14, are due to Zhang and to D. Roy and J. L. Thunder, *An absolute Siegel's lemma*, J. reine angew. Math. 476 (1996). The proof of Section 14 follows the route through the successive minima. Heights through Chow forms, as in Section 9, are treated in the paper of Bost, Gillet and Soulé.

Grothendieck's existence theorem of Section 7 is EGA III₁, §5.4. The Čech cohomology of Section 6 follows the methods of R. Hartshorne, *Algebraic Geometry*, Chapters II and III, and of Serre's finiteness theorems. The numerical Segre formula of Section 8 is the computation of the Segre classes of a projective bundle in W. Fulton, *Intersection Theory*, Chapter 3; the complete symmetric functions are those of I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I.

The theta functions of Section 5 are those of D. Mumford, *Tata Lectures on Theta I*, Birkhäuser (1983), and the reduction of the period matrix in Section 4 is Siegel's reduction theory, C. L. Siegel, *Einführung in die Theorie der Modulfunktionen n-ten Grades*, Math. Ann. 116 (1939). The bound $\theta(x) \le x \log 4$ used in Section 3 is Chebyshev's bound; see G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, §22.2. The quotients by the Vandermonde product in Section 1 are the alternants of Macdonald, Chapter I.
