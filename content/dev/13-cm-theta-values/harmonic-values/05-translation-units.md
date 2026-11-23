---
title: Translation units on formal groups
decls:
  - GlobalTheory.TransUnit.model_unit
  - GlobalTheory.TransUnit.exists_trUnit
  - GlobalTheory.T.exists_translateUnit_symmetric_formalGroup_point
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Translation units on formal groups

Let $a$ be a torsion point of odd order $k$ on an abelian scheme over a complete [[discrete valuation ring|MGM3CNJW9V]], and assume that $a$ reduces to $0$. The theta group of $L^k$ contains a symmetric lift of $a$, and this lift acts on sections of $L^k$. This section computes the action in a formal chart. Translation by the lift multiplies the germ by a unit power series $u$ after a shift of the variable by the formal point $\alpha$ of $a$. The unit $u$ satisfies three laws: a cocycle law with the cube series, an order law and a symmetry law. The next section sums germs over the kernel of a similitude and needs exactly these three laws. The background is in [formal group laws](/learn/formal-groups/#formal-group-laws) and [the cubical structure](/learn/theta-functions-cm/#the-cubical-structure).

### The cube series and the inversion series

Let $V$ be a complete discrete valuation ring with fraction field $K$ of characteristic $0$. Let $C$ be a chart of dimension $d$ over $V$, with formal group law $\mathcal{F}$, formal action of $\mathcal{O}_E$ and canonical gauge $h$. Write $x +_{\mathcal{F}} y$ for $\mathcal{F}(x, y)$ and $[c]x$ for the action of $c \in \mathcal{O}_E$. Let $\Lambda(x) = h_L(x)$ be the gauge term of the [third section](/entry/harm-nab-eq-poly-deriv/), a power series over $K$ in one point $x$.

**Definition 2.5.1 (cube series).** A power series $\Theta \in V[[x, y, z]]$ in three points is the *cube series* if, over $K$,
$$\Theta = \exp\Bigl(\Lambda(x + y + z) - \Lambda(x + y) - \Lambda(x + z) - \Lambda(y + z) + \Lambda(x) + \Lambda(y) + \Lambda(z)\Bigr),$$
where all sums are taken in $\mathcal{F}$.

**Definition 2.5.2 (inversion series).** A power series $j \in V[[x]]$ is the *inversion series* if, over $K$, $j = \exp\bigl(\Lambda([-1]x) - \Lambda(x)\bigr)$.

**Definition 2.5.3 (translation unit).** Let $\alpha \in V^d$ be a point with small coordinates, and let $\mathrm{sh}_\alpha f(x) = f(x +_{\mathcal{F}} \alpha)$. A power series $u \in V[[x]]$ is a *translation unit* for $(\Theta, j, k, \alpha)$ if:

1. *unit:* $u$ is a unit of $V[[x]]$;
2. *cocycle:* $u(x +_{\mathcal{F}} y)\, u(0) = u(x)\, u(y)\, \Theta(x, y, \alpha)^k$;
3. *order:* the map $f \mapsto u \cdot \mathrm{sh}_\alpha f$, applied $k$ times to $1$, gives $1$;
4. *symmetry:* $u(0)\, j(\alpha)^k\, u([-1]\alpha) = 1$.

The cocycle law says that $u$ is a quasi-character for the cube structure. The order law says that the operator $f \mapsto u \cdot \mathrm{sh}_\alpha f$ has order dividing $k$. The symmetry law says that it commutes with the action of $[-1]$ up to the inversion series.

### The model computation

**Theorem 2.5.4 (translation unit in a model chart).** Let $V$ be a complete discrete valuation ring, and let $t$ be an abelian scheme over $V$ with a symmetric line bundle and cubical structure. Let $C$ be a chart over $V$ with formal group law $\mathcal{F}$, frame $e$, primitive generator $w$ and canonical gauge $h$, whose frames are compatible with truncation. Assume that the global sections of $t \times t$ map onto those of the formal completion. Let $\Theta$ be the cube series and $j$ the inversion series. Let $k$ be odd. Let $\alpha$ be a small point with $k\alpha = 0$ in the formal group, and let $a_V$ be the section of $t$ that reduces to $\alpha$ modulo every power of the maximal ideal. Then there are a symmetric lift $U$ of $a_V$ in the theta group of $L^k$ and a translation unit $u$ for $(\Theta, j, k, \alpha)$ such that for every power series $f$ and all sections $s, s'$ of $L^k$ with $s' = U \cdot s$: if $s$ has germ $f$, then $s'$ has germ $u \cdot \mathrm{sh}_\alpha f$.

Lean: `GlobalTheory.TransUnit.model_unit`.

*Proof.* The chart gives a point $X$ of $t$ over $V[[x]]$ that is the limit of the jet points. The point $a_V$ has order dividing $k$, since its formal point does.

*Step 1: the lift.* Over a local ring, a point of odd order $k$ has a symmetric lift $U$ to the theta group of $L^k$, of order dividing $k$.

*Step 2: readings.* Choose a trivialization of $L$ near the zero section. In it we read four unit power series: $\rho(x)$ from the primitive generator, $\theta(x, y, z)$ from the cubical structure, $\varphi(x)$ from the lift $U$, and $\varepsilon(x, y)$ from the frame. The frame laws give partial cocycles $p_1, p_2$ with $\theta = p_1 \cdot \partial_1 \varepsilon$ and $\theta = p_2 \cdot \partial_2 \varepsilon$, where $\partial_1, \partial_2$ are the two coboundaries. The values of $\varepsilon$ at $0$ in either variable are $1$.

*Step 3: the unit.* With $w$ the action of $w_0$, put
$$u(x) = \varphi(x) \cdot \Bigl(\frac{\rho(\alpha + x)\, \varepsilon\bigl(\alpha + x, w(\alpha + x)\bigr)}{\rho(x)\, \varepsilon\bigl(x, w(x)\bigr)}\Bigr)^k.$$
A computation in an abelian group of units shows three identities. First, $u(x+y)\,u(0) = u(x)\,u(y)\,Q(x, y)^{-k}$, where $Q$ is a quadratic expression in $p_1, p_2$. Second, $\prod_{i < k} u(i\alpha + x) = 1$. Third, $u(0)\, N^k\, u([-1]\alpha) = 1$, with $N$ another expression in $p_1, p_2$. Here all sums are taken in $\mathcal{F}$. These identities need the lift laws of $U$ and $k\alpha = 0$.

*Step 4: the laws.* The unit $u$ is compatible with substitution of points. Evaluation of the cube series against the partial cocycles turns the first identity into the cocycle law. Iteration of $f \mapsto u \cdot \mathrm{sh}_\alpha f$ gives the product of translates, so the second identity gives the order law. Evaluation of the inversion series turns the third identity into the symmetry law.

*Step 5: germs.* Let $s$ have germ $f$ and $s' = U \cdot s$. Read $s$ and $s'$ in the trivialization. The reading of the action of $U$ is $\varphi$ times the shifted reading. Comparing with the germ reading through $\rho$ and $\varepsilon$ gives the germ $u \cdot \mathrm{sh}_\alpha f$ for $s'$. $\square$

### Translation units at integral points

**Theorem 2.5.5 (translation units at integral points).** Assume that the involution of $\mathcal{O}_E$ is complex conjugation. Let $V$ be a complete discrete valuation ring with an embedding of the coefficient field $F$ into its fraction field. Let $y$ be an integral framed point over $V$, and $C$ an integral chart at $y$ whose frames are compatible with truncation. Let $B$ be formal data of the chart in the canonical gauge, $\Theta$ the cube series and $j$ the inversion series. Let $k$ be odd, and let $a$ be a point of the abelian variety at $y$ with formal point $\alpha$ and $a^k = 1$ in the group law of the abelian scheme. Then there is a translation unit $u$ for $(\Theta, j, k, \alpha)$ such that, for all sections $s, s'$ of $L^k$ where $s$ is regular and $s'$ is the symmetric translate of $s$ by $a$: if $s$ has germ $f$, then $s'$ has germ $u \cdot \mathrm{sh}_\alpha f$.

Lean: `GlobalTheory.TransUnit.exists_trUnit` (also `GlobalTheory.T.exists_translateUnit_symmetric_formalGroup_point`, a second name).

*Proof.* The integral chart gives a model chart over $V$, and the formal point of $a$ is small. The canonical gauge of the formal data is the gauge of the model, by the bound on gauge eigenvalues. Since $k\alpha = 0$ in the formal group, the constant section $\alpha$ has order dividing $k$ in every truncation. The Theorem on model charts gives a lift $U$ and a unit $u$. A lemma on fibres identifies the symmetric translate by $a$ with the action of $U$ on the model. So the germ of $s'$ is $u \cdot \mathrm{sh}_\alpha f$. $\square$

**Remark 2.5.6.** Classically, Mumford's theta group $\mathcal{G}(L^k)$ acts on the sections of $L^k$, and a point of odd order has a unique symmetric lift of the same order. See Mumford, *Abelian Varieties*, §23, for the theta group over a field. In a formal chart the action of the lift is a twisted translation. The three laws of the unit are the formal forms of the group law of $\mathcal{G}(L^k)$, of the order of the lift, and of its symmetry under $[-1]$.

**Remark 2.5.7 (Formalization).** Both theorems are in [ExistsTranslateUnitSymmetricFormalGroupPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/ExistsTranslateUnitSymmetricFormalGroupPoint.lean#L479), at L479 and L618. The formula of Step 3 is at L51 and its three identities at L54. The translation unit and the cube series are in [AdaptStd.lean](lean:Development/AbelianVarietyTheory/Definitions/PlaceAdaptation/AdaptStd.lean#L75), with the cube series at L61. The second name is in [ExistsTranslateUnitSymmetricFormalGroupPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/ExistsTranslateUnitSymmetricFormalGroupPointStatement.lean#L11) and is proved by a `first` combinator.
