---
title: Moriwaki bigness and the Hilbert-Samuel inputs
decls:
  - PositivityTheory.HtPt.Ah.deep_slim_use
  - GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use
  - GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis
  - GlobalTheory.CompanionTheory.Ar.Giv.lineOfLargeDegree_of_use
  - GlobalTheory.CompanionTheory.Ar.Link.given_of_use
  - GlobalTheory.CompanionTheory.Ar.Link.nineFree_of_use
  - GlobalTheory.CompanionTheory.Ar.Giv.grassmannian_height_bound_of_systems
  - GlobalTheory.CompanionTheory.Ar.Link.provHS_of_use
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moriwaki bigness and the Hilbert-Samuel inputs

This section derives the inputs of the volume theorem from a short list of statements of arithmetic intersection theory: the existence of an arithmetic intersection system, the Hilbert-Samuel statements, Moriwaki's bound of the self-intersection by the arithmetic volume, and resolution. From these it proves the absolute Siegel lemma, the bundle of top level inputs, the good tower and volume theorems, and the deep statement on mean slopes. The deep statement is used by the [self-intersection and volume estimate](/entry/top-covol-slim2-use-alt-alt/) of the chapter on canonical forms near the boundary, and through it in Step 4 of [the Weil bound](/proof/weil-bound/). The objects are [arithmetic varieties and intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers), [arithmetic volumes](/learn/arakelov/#arithmetic-volume-and-bigness) and [hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes).

Throughout, $X$ is an arithmetic variety of dimension $D + 1$, given by a prime ideal of a polynomial ring in coordinates $y$ that are birational onto it, and $\overline{A}$ is a hermitian line on $X$. We write $\overline{A}^{D+1}$ for its top self-intersection in an intersection system $\mathrm{II}$, $\deg_A X$ for the geometric degree, and $\widehat{\mathrm{vol}}(\overline{A})$ for the arithmetic volume of the small sections of $\overline{A}$.

**Definition 9.16.1 (Moriwaki's statement).** Moriwaki's statement says: if $\mathrm{II}$ is an intersection system and $\overline{A}$ is semipositive relative to an ambient variety, invariant under complex conjugation, nef on the fibres and nef on the generic fibre, then

$$
\overline{A}^{D+1} \le \widehat{\mathrm{vol}}(\overline{A}).
$$

**Definition 9.16.2 (The Hilbert-Samuel statement).** The Hilbert-Samuel statement is the conjunction of three statements: an arithmetic Kleiman criterion; an upper bound for the growth of the number of small sections of the powers of a well generated $\overline{A}$ by $\overline{A}^{D+1}$; and the arithmetic Hilbert-Samuel upper bound, which says that for $D \ge 1$ and a semipositive conjugation invariant $\overline{A}$ with bounded monomials,

$$
\limsup_{\tau \to \infty} \frac{N(\tau)}{\tau^{D+1}/(D+1)!} \le \overline{A}^{D+1},
$$

where $N(\tau)$ is the small section count of $\overline{A}^{\tau}$ for the normed chart lattice.

**Definition 9.16.3 (Successive minima bounds).** Let $\overline{A}$ be semipositive, nef on the fibres and conjugation invariant. The lower bound says: if $e \deg W \le \overline{A}|_W$ for every subvariety $W$ of $X$ of arithmetic dimension $1$, then

$$
(D + 1)\, e\, \deg_A X \le \overline{A}^{D+1}.
$$

The upper bound says: if a Zariski dense family of such $W$ has $\overline{A}|_W \le e' \deg W$, then

$$
\overline{A}^{D+1} \le (D + 1)\, e'\, \deg_A X.
$$

These are the two halves of Zhang's theorem of successive minima, in a form for an abstract intersection system.

A lemma of the theory of heights turns the Hilbert-Samuel statement and Moriwaki's statement into six statements: the nonnegativity of arithmetic intersections, which is proved outright; the lower successive minima bound, from the arithmetic Kleiman criterion and the finiteness of points on curves; the upper successive minima bound and the lower bound of the arithmetic volume by the self-intersection, both from Moriwaki's statement; Zhang's lower bound for components, from the lower successive minima bound; and the dimension statement, which is proved outright.

**Theorem 9.16.4 (The Hilbert-Samuel provisions).** Assume the arithmetic intersection system statement, the Hilbert-Samuel statement, Moriwaki's statement and the resolution statement. Then the following nine statements hold: the two successive minima bounds; the nonnegativity of arithmetic intersections; the lower bound of the arithmetic volume; the bound of $\overline{A}^{D+1}$ by the arithmetic volume for the normed chart lattice; the arithmetic Hilbert-Samuel upper bound; its form over a number field; the bound of a self-intersection under a bounded injection of sections; and the multiplicativity of the arithmetic volume.

Lean: `GlobalTheory.CompanionTheory.Ar.Link.provHS_of_use`

*Proof.* The first four come from the lemma above. The bound for the normed chart lattice follows from Moriwaki's statement. The Hilbert-Samuel upper bound is the third part of the Hilbert-Samuel statement. The number field form follows from the intersection system statement, the Hilbert-Samuel statement and resolution. The bound under a bounded injection follows from the Hilbert-Samuel statement and Moriwaki's statement, and the multiplicativity from all four hypotheses. $\square$

**Theorem 9.16.5 (Height bound for Grassmannians).** Under the same four hypotheses the following holds. Let $\Psi$ be a finite set, $N \ge 2$, $1 \le j \le N - 1$ and $c$ a rational number with $J > 0$, where $J$ is the degree number of the standard line $F_A$ of the Grassmannian of type $(\Psi, N, j)$ with coefficient $c$, and let $d$ be the dimension. If

$$
\tfrac{1}{2} \log \det\big(1 + Z Z^{*}\big) \le e
$$

for every $(N - j) \times j$ complex matrix $Z$ whose entries have absolute value $1$, then the flag height satisfies

$$
- h_{\mathrm{Fl}}(F_A) \le (d + 1)\, J\, |\Psi|\, e.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.grassmannian_height_bound_of_systems`

*Proof.* The inputs of the proof theory follow from the four hypotheses. With the intersection system statement and the upper successive minima bound they give the claim. $\square$

**Theorem 9.16.6 (The Zhang, dimension and push down bundle).** Under the same four hypotheses, Zhang's lower bound for components, the dimension statement, the push down statement and the height bound for Grassmannians hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Link.nineFree_of_use`

*Proof.* Zhang's lower bound and the dimension statement come from the lemma above, the push down statement from the intersection system statement, and the Grassmannian bound from the previous theorem. $\square$

Zhang's lower bound for components says: if $e$ is at most the height of every algebraic point of a component, then $(n + 1)\, e$ times the geometric degree is at most the top intersection. The push down statement expresses the limit $\mathrm{PP}_B$ of a component as a constant times its arithmetic limit, and gives a positive volume for the degree.

**Theorem 9.16.7 (Absolute Siegel lemma).** Assume the four hypotheses. Let $K$ be a number field, $F$ a hermitian lattice of rank $i \ge 1$ over $\mathcal{O}_K$ with slope $\mu(F)$, and $\varepsilon > 0$. Then there are a finite extension $K'$ of $K$ and a nonzero $v \in K'^{i}$ such that

$$
\mu(F) - \tfrac{1}{2} \log i - \varepsilon \le \deg_{K'}(v),
$$

where $\deg_{K'}(v)$ is the normalized degree of the line spanned by $v$ in $F \otimes \mathcal{O}_{K'}$.

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.lineOfLargeDegree_of_use`

*Proof.* The upper successive minima bound comes from Moriwaki's statement, the lower one from the Hilbert-Samuel statement, and the existence of intersections from the intersection system statement. The Siegel lemma follows from these three by a reduction through Grassmannians and dual lattices. The reduction uses about thirty auxiliary statements on charts, dual lattices, stacked graphs, metric energies and changes of model. Almost all of them are proved outright. The four hypotheses enter in five places: the generic degree, the coordinate projection and the degree of a system come from the intersection system statement, and the integrability and independence of points come from resolution. $\square$

The lemma says that every hermitian lattice has, after a finite extension, a line of degree at least its slope minus $\frac{1}{2} \log i$. It is a form of the absolute Siegel lemma.

**Theorem 9.16.8 (The top level inputs).** Assume the four hypotheses, the extension statement for homomorphisms of semi-abelian schemes, the Hodge-Tate comparison of Fargues, the GAGA statement for sections and the absolute Siegel lemma. Then the fourteen top level inputs of the chapter hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Link.given_of_use`

*Proof.* The model clause, the key formula, the numerical Segre statement and the analytic provisions are proved outright. The semi-abelian extension, resolution, the Fargues comparison, the GAGA statement and the Siegel lemma are given. The inputs of the proof theory, the Hilbert-Samuel provisions and the Zhang bundle are built from the four hypotheses by the theorems above. The [assembly of the top level inputs](/entry/given-of-inputs/) gives the fourteen inputs. $\square$

**Theorem 9.16.9 (Good towers and the volume theorem from ten inputs).** Assume the eight hypotheses of the previous theorem, the statement on quotients by finite flat group schemes and Zarhin's statement. Then the existence statement for good towers and the volume statement of the [section on the volume theorem](/entry/volume-theorem-x-of-inputs/) hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis`

*Proof.* The previous theorem gives the top level inputs. Eleven of the fourteen parts, with the Siegel lemma, the integrability of points from resolution, the prime avoidance statement, the uniformization of abelian varieties by theta functions, the quotient statement and Zarhin's statement, are the inputs of the [right hand final theorem](/entry/final-theorem-of-inputs-right/), which gives both statements. $\square$

**Theorem 9.16.10 (The deep statement from its uses).** Assume the four hypotheses, the semi-abelian extension, the Fargues comparison, the GAGA statement, the quotient statement, Zarhin's statement and the nef Riemann-Roch statement. Then there is $C \ge 0$ such that for every datum $D$ with $m^2 \le k$, every core tower with its laws, every $1 \le j < m$ and every good deep model whose level has at most $15$ prime factors, the mean slope bound holds with the constant $C$.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use`

*Proof.* The absolute Siegel lemma follows from the four hypotheses. With it the top level inputs hold, and so do the existence and volume statements of the previous theorem. The Hilbert-Samuel provisions are among the top level inputs, and the bound of the self-intersection by the arithmetic volume for the normed chart lattice is among them. The [deep statement from the volume theorem](/entry/deep-st-r-of-volume/) takes the nef Riemann-Roch statement, the top level inputs, the intersection system statement, that bound, and the existence and volume statements, and gives the claim. $\square$

**Theorem 9.16.11 (The deep statement from resolution and positivity).** Assume resolution of singularities and principalization in characteristic zero, the invariance statement for the Poincaré-Lelong formula, the Hilbert-Samuel statement, Moriwaki's statement, the exactness statement of Fargues, Zarhin's statement and the nef Riemann-Roch statement. Then the deep statement holds.

Lean: `PositivityTheory.HtPt.Ah.deep_slim_use`

*Proof.* Resolution and principalization give the resolution statement. With the Poincaré-Lelong invariance they give the Poincaré-Lelong formula, and with resolution the arithmetic intersection system statement. The semi-abelian extension and the GAGA statement are proved outright. The Hodge-Tate comparison follows from the exactness statement of Fargues. The quotient statement follows from the existence of free quotient schemes, which is proved. The previous theorem applies. $\square$

So the deep statement, and with it the mean slope bound of Step 4, rests on resolution in characteristic zero, the Poincaré-Lelong invariance, the Hilbert-Samuel statement, Moriwaki's bound, the exactness of Fargues, Zarhin's statement and nef Riemann-Roch. The volume theorem itself is the second statement of the theorem with ten inputs.

**Remark 9.16.12 (Formalization).** The fifth part of the Hilbert-Samuel provisions is named `BirationalPullbackPushforwardFormula`, but its statement is the inequality of the self-intersection by the arithmetic volume for the normed chart lattice ([ArithmeticHilbertSamuelLowerBound.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ArithmeticHilbertSamuelLowerBound.lean#L126)); it is filled by `GlobalTheory.T.big_line_implies_height_positivity` ([ProvHSOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/ProvHSOfUse.lean#L17)). The Hilbert-Samuel upper bound is taken as the third part of the Hilbert-Samuel statement, whose type there is `ArithmeticVolumeNef.Statement`; our reading is that the two are equal by definition. The Zhang bundle has `True` as its third part ([ZhangDimensionPushDownGrassmannianHeightBounds.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/ZhangDimensionPushDownGrassmannianHeightBounds.lean#L33)), filled by `trivial`. The theorem with ten inputs takes the top level inputs apart by position and drops three parts, `_hSAst`, `_hSlope` and `_hAnti` ([GoodTowerVolumeTheoremBis.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GoodTowerVolumeTheoremBis.lean#L16)); the word "bis" in its name has no meaning in the statement. `deepStR_of_use` builds the top level inputs with `given_of_use` and builds them again inside `good_tower_volume_theorem_bis`, then takes the Hilbert-Samuel provisions as the eleventh part and their fifth part by position ([DeepStROfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean#L19)). `deep_slim_use` has the same proof as `deep_slim` in [AhSlim.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/AhSlim.lean#L29), with the Hilbert-Samuel statement in place of Moriwaki's Hilbert-Samuel statement. Two definitions named `GrassmannianHeightZTwo.Statement` exist in different namespaces; the one used here is in [FlagIndices.lean](lean:GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/FlagIndices.lean#L95). The names of the Kleiman, push down, quotient and nef Riemann-Roch statements are our reading; we have not unfolded them, the degree number $J$, the line $F_A$, the deep models, or the thirty statements of the Siegel lemma.
