---
title: Change of representative
decls:
  - GlobalTheory.Phase.ChangePt.change_at_point
  - GlobalTheory.changeRoot_complex
  - GlobalTheory.changeRoot_of_chartIndep
  - GlobalTheory.T.thetaChangeOfRepRootOfUnity_of_chartIndependence
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Change of representative

A short theta value is a number attached to a point of a unitary moduli space, a Hermitian lattice $\Lambda$ with level structure, and a harmonic polynomial $P$. If we move $\Lambda$ by a unitary matrix $h$ and move $P$ with it, the value changes. This section proves that it changes by a root of unity $\zeta$ in the coefficient field, and that $\zeta$ is the same for all points over all rings. The proof first works at one complex point, where the short theta value is a classical theta value and [the multiplier theorem](/entry/is-mu-multiplier-sq-mul-det/) applies, and then spreads the result to all points and all rings. The result feeds the [change of representative rule](/entry/short-rule-change-mat/), which lets the proof define short theta values on classes of lattices.

### The setting

We fix the following data and do not unfold them here; they are the objects of the moduli chapters of this volume.

- A CM field $E$ with complex conjugation $a \mapsto \bar a$, and a unitary Shimura datum over $E$ of signature $(p, q)$. To each embedding $\tau \colon E \to \mathbb{C}$ it attaches a multiplicity $m_\tau \ge 0$.
- A level with an integer $M \ge 3$, the moduli space $X$ of this datum at this level, and a number field $F$ of coefficients with an embedding into $\mathbb{C}$. For each embedding $\tau$ of $E$ we also write $\tau$ for an embedding $E \to F$ through which $\tau$ factors.
- For each commutative $F$-algebra $S$, the set $X^{\mathrm{fr}}(S)$ of *framed points* of $X$ with values in $S$. A map $S \to T$ of $F$-algebras moves framed points over $S$ to framed points over $T$.
- A *lattice datum* $\Lambda$ of rank $n$. It has two $\mathcal{O}_E$-lattices $\Lambda^a$ and $\Lambda^n$ in $E^n$, and we write $A(\Lambda) = [\Lambda^a : \Lambda^a \cap \Lambda^n]^{p+q}$. It can be *unimodular*, *trivial at* an integer $k$, and of *level* $N$. A matrix $h \in M_n(E)$ moves it to a lattice datum $h\Lambda$.
- For a weight $a$, a space of *harmonic polynomials* $P$ with coefficients in $F$ in the letters of the datum, and the push-forward $h_* P$ by $h$.
- A *normalizing constant* for $\Lambda$: an element $\beta \in F^\times$ such that $(\beta) \prod_\tau I_\tau(\Lambda^a)^{m_\tau} = \prod_\tau I_\tau(\Lambda^n)^{m_\tau}$ as $\mathcal{O}_F$-modules, where $I_\tau(\Lambda')$ is spanned by the images under $\tau$ of the determinants of $n$-tuples of vectors of $\Lambda'$, and $|\sigma(\beta)|^2 = A(\Lambda)$ for every embedding $\sigma \colon F \to \mathbb{C}$. We call it *admissible for* $\Lambda$.
- An auxiliary datum $\nabla$ on the moduli space, with a condition that makes it *admissible*.
- For a function $w$ on the level structures, a lattice datum $\Lambda$ with constant $\beta$ and level $N$, a harmonic polynomial $P$, a framed point $y \in X^{\mathrm{fr}}(S)$ and $v \in S$, the relation "$v$ is the *short theta value* of $(w, \Lambda, \beta, N, P)$ at $y$". For unimodular $\Lambda$, trivial at $M$, there is exactly one such $v$ for each $y$, and it is natural in $S$.

A matrix $h$ *fixes* $w$ if $w(q') = w(q)$ whenever $h$ moves the level structure $q$ to $q'$. A matrix $h \in M_n(E)$ is *unitary* if $\bar h^T h = 1$.

The proof assumes one statement about charts on $X$. A *chart* at a framed point $y$ is a formal coordinate system at $y$. In a chart, a section of a power $\mathcal{L}^k$ of the automorphic line bundle has a *germ*, a power series. A harmonic polynomial $P$ in $n$ letters turns $n$ germs into a *chart value* by applying $P$ to their Taylor coefficients.

**Theorem 3.2.1 (Chart independence of theta expressions).** Let $S$ be a commutative ring that is an $F$-algebra and a $\mathbb{Q}$-algebra, and let $y \in X^{\mathrm{fr}}(S)$. Let $C$ and $C'$ be two charts at $y$, let $k, n \ge 0$, and let $F_1, \dots, F_n$ be sections of $\mathcal{L}^k$ at $y$ with germs $f_b$ in $C$ and $f'_b$ in $C'$. Then for every harmonic polynomial $P$ of any weight, the chart value of $(f_b)$ under $P$ in $C$ equals the chart value of $(f'_b)$ under $P$ in $C'$.

We do not prove this statement here. All results of this section take it as a hypothesis. It says that harmonic theta expressions do not depend on the chart.

### At one complex point

The first step is local. At a complex point $y$ that comes from a frame $x$ of the period domain $\mathcal{D}$ of the previous section and a self-dual lattice $L$ (we say that $y$ is the *analytic fibre* of $(x, L)$), a short theta value is a classical theta value of a vacuum vector, up to an explicit constant. The column change $z \mapsto h \cdot z$ is then a change of theta series.

**Theorem 3.2.2 (Change at a complex point).** Assume chart independence. Let a unitary period datum of rank $r = p + q$ with a symplectic basis be given, whose embeddings and columns match the letters of the Shimura datum, and let $n$ be even. Let $\nabla$ be admissible, let $\Lambda$ be a unimodular lattice datum of rank $n$, and let $h \in M_n(E)$ be unitary, with $\Lambda$ and $h\Lambda$ trivial at $M$. Then there is $t \in \mathbb{C}$ with $|t| = 1$ such that, for every frame $x \in \mathcal{D}$, every self-dual $L$ and every complex framed point $y$ that is the analytic fibre of $(x, L)$:

1. $t^2 \prod_{\tau \colon E \to \mathbb{C}} \tau(\det h)^{m_\tau}$ is a root of unity;
2. for every $w$ fixed by $h$, levels $N$ of $\Lambda$ and $N'$ of $h\Lambda$, a harmonic polynomial $P$ of weight $a$, constants $\beta, \beta' \in F^\times$, and short theta values $v$ of $(w, \Lambda, \beta, N, P)$ and $v'$ of $(w, h\Lambda, \beta', N', h_*P)$ at $y$,
$$v' \beta' \sqrt{A(\Lambda)} = t\, \beta \sqrt{A(h\Lambda)}\, v.$$

Lean: `GlobalTheory.Phase.ChangePt.change_at_point`

*Proof.* Since $\Lambda$ is unimodular and trivial at $M \ge 3$, the lattice $\Lambda^a$ lies in the set $V_n$ of self-dual lattices commensurable with $\mathcal{O}_E^n$, and the same holds for $h\Lambda$, since $h$ is unitary. The CM datum gives an integral $w_0 \in E$ with $w_0 + \bar w_0 = 1$. A result of the sources gives $t$ with $|t| = 1$ such that, for every self-dual $L$, every vacuum $v_0$ for $\mathcal{O}_E^n \otimes L$ and every $x \in \mathcal{D}$, the theta series of the normalized projections to $(h\Lambda)^a \otimes L$ and $\Lambda^a \otimes L$ satisfy the column relation $\Theta_{\varphi_2}(x, h \cdot z) = t\, \Theta_{\varphi_1}(x, z)$. A vacuum $v_0$ exists for each self-dual $L$.

For part 1, [the multiplier theorem](/entry/is-mu-multiplier-sq-mul-det/) shows that $t^2 \prod_{i=1}^g \sigma_i(\det h)$ is a root of unity. The columns $i$ match the letters of the Shimura datum, and these are the pairs $(\tau, j)$ with $j < m_\tau$. The embedding $\sigma_i$ is the embedding $\tau$ of the letter of $i$. So the product over $i$ is $\prod_\tau \tau(\det h)^{m_\tau}$.

For part 2, the frame $x$ gives a theta function on the abelian variety at $y$, and a choice of level marks. With these, a result of the sources expresses each short theta value at $y$ as a classical theta value: $v \beta \sqrt{A(\Lambda)}$ is, up to a factor that depends only on $x$, $L$ and the marks, the value of $\Theta_{\varphi_1}$ at the point given by $P$ and $w$, and the same holds for $v'$ with $h\Lambda$ and $h_*P$. The push-forward $h_* P$ is again harmonic. The column relation now gives the identity. $\square$

### Over the complex numbers

**Theorem 3.2.3 (Change over the complex numbers).** Assume chart independence, and fix an embedding $F \to \mathbb{C}$. Let $\nabla$ be admissible and let $n$ be even. Assume that there is a unitary period datum as in the previous theorem such that every complex framed point $y$ is the image, under an element of the Borel subgroup, of a complex framed point $y_0$ that is the analytic fibre of some $(x, L)$ with $x \in \mathcal{D}$ and $L$ self-dual. Let $\Lambda$ be unimodular, let $h$ be unitary, let $\Lambda$ and $h\Lambda$ be trivial at $M$, and let $\beta$ and $\beta'$ be admissible for $\Lambda$ and $h\Lambda$. Then there is a root of unity $z \in \mathbb{C}$ such that, for every $w$ fixed by $h$, levels $N$ and $N'$, harmonic $P$ of any weight, and complex framed point $y$, the short theta values satisfy $v' = z v$.

Lean: `GlobalTheory.changeRoot_complex`

*Proof.* If there is no complex framed point, take $z = 1$. Otherwise pick one, write it as the image of some $y_0$, and let $t$ be given by the previous theorem. Put $D = \prod_\tau \tau(\det h)^{m_\tau}$, $A = A(\Lambda)$ and $A' = A(h\Lambda)$. A result of the sources on admissible constants gives $m > 0$ with
$$(\beta^2 A')^m = (\beta'^2 A D)^m.$$
The admissibility of $\beta$ gives $A \ne 0$. Put $z = t \beta \sqrt{A'} / (\beta' \sqrt{A})$. Then $z^2 = t^2 \beta^2 A' / (\beta'^2 A)$, so $z^{2m} = (t^2 D)^m$. Since $t^2 D$ is a root of unity by part 1 of the previous theorem, so is $z$.

Now let $y$ be any complex framed point, the image of $y_0$ under a Borel element $b$. The short theta values at $y_0$ exist and are unique. A result of the sources says that a Borel element multiplies short theta values by a factor that depends only on $b$ and the weight, and not on $\Lambda$, $\beta$ or $P$. So $v$ and $v'$ at $y$ are the values $u$ and $u'$ at $y_0$ times the same factor. Part 2 of the previous theorem gives $u' = z u$, and so $v' = z v$. $\square$

### Over all rings

The last step removes the embedding into $\mathbb{C}$. A *bad integer* for the level is an integer $\mathrm{bad} > 0$ that is even, is divisible by $M$, and is divisible by each prime that divides the discriminant of $E$.

**Theorem 3.2.4 (Change of representative).** Assume chart independence. Let $\nabla$ be as above and $n \ge 0$. Assume that $E$ is Galois over $\mathbb{Q}$, that $p + q$ is odd, that $n$ is even and that $\nabla$ is admissible. Let $\mathrm{bad}$ be a bad integer, let $\Lambda$ be a unimodular lattice datum of rank $n$, let $h \in M_n(E)$ be unitary, let $\Lambda$ and $h\Lambda$ be trivial at $\mathrm{bad}$, and let $\beta$ and $\beta'$ be admissible for $\Lambda$ and $h\Lambda$. Then there is $\zeta \in F$ with $\zeta^k = 1$ for some $k > 0$ such that: for every $w$ fixed by $h$, levels $N$ of $\Lambda$ and $N'$ of $h\Lambda$, weight $a$ and harmonic $P$ of weight $a$, commutative $F$-algebra $S$, framed point $y \in X^{\mathrm{fr}}(S)$, and short theta values $v$ of $(w, \Lambda, \beta, N, P)$ and $v'$ of $(w, h\Lambda, \beta', N', h_* P)$ at $y$, we have $v' = \zeta v$.

Lean: `GlobalTheory.changeRoot_of_chartIndep` (also `GlobalTheory.T.thetaChangeOfRepRootOfUnity_of_chartIndependence`, a second name)

*Proof.* Since $M$ divides $\mathrm{bad}$, a lattice datum that is trivial at $\mathrm{bad}$ is trivial at $M$. Since $p + q$ is odd, it is positive, and a result of the sources gives an embedding $F \to \mathbb{C}$ and a unitary period datum with the property of the previous theorem: every complex framed point comes from the analytic fibre of a frame by a Borel element. The [previous theorem](/entry/change-root-complex/) gives a root of unity $z \in \mathbb{C}$ with $v' = z v$ at all complex points.

Index by $j$ the data $(w, N, N', a, P)$ of the statement. For each $j$, the short theta values define two functions $u_j$ and $u'_j$ that give an element of $S$ for each $F$-algebra $S$ and each $y \in X^{\mathrm{fr}}(S)$, and they are natural in $S$. Over $\mathbb{C}$ we have $u'_j = z u_j$. A result of the sources on such natural functions now gives $\zeta \in F$ with $\zeta^k = 1$ for some $k > 0$ and $u'_j(S, y) = \zeta u_j(S, y)$ for all $j$, $S$ and $y$. Uniqueness of short theta values gives $v = u_j(S, y)$ and $v' = u'_j(S, y)$. $\square$

**Remark 3.2.5 (Formalization).** The three theorems take the chart independence statement `ChartIndepSt2` ([ThExprUniqOfChartIndep2.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/ThExprUniqOfChartIndep2.lean#L12)) as a hypothesis; it is not proved. We have not unfolded the moduli objects: lattice data `GenLat`, unimodularity, triviality at a level, admissible constants `IsBeta`, the level condition `LevOK`, `ShortValAt`, the harmonic spaces `HHa` and `harmL`, the push-forward `pushLet`, `AnFib`, `FrPt` and the connection `IsNab`. The Galois hypothesis on $E$ is dropped at line 106 of [ThetaChangeOfRepRootOfUnityOfChartIndependence.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/ThetaChangeOfRepRootOfUnityOfChartIndependence.lean#L106) and is not used. Of the four conditions on the bad integer, only $M \mid \mathrm{bad}$ is used. The empty case at lines 59 to 61 takes $z = 1$. The point theorem `change_at_point` lives in CmHostIdempotentTraceEqOne.lean, whose name is that of a small lemma at line 44.
