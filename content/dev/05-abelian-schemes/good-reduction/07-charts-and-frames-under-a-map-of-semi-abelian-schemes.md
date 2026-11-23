---
title: Charts and frames under a map of semi-abelian schemes
decls:
  - GlobalTheory.ChartCmp.jrel_of_sabMap
  - GlobalTheory.T.formal_biextensions_related_of_triple_map_over_id
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Charts and frames under a map of semi-abelian schemes

A semi-abelian scheme with an action of an order, a rigidified line bundle and a cubical structure gives a formal biextension once we choose two things: a chart, which is a system of formal coordinates at the origin, and a frame, which is a compatible family of generators of the line bundle $\Lambda(L)$ on the jets. If two such schemes are related by a map over the identity of the base, then the formal biextensions read off from any two choices of charts and frames differ, to each finite order, by a change of coordinates and a unit. The result is used through [the step on characters from the literature](/step/every-character-of-literature/). For the geometry behind it see [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) and [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1.

### Semi-abelian schemes with cubical data

Throughout, $E$ is a CM number field with ring of integers $O_E$, and $a \mapsto \bar a$ is complex conjugation on $O_E$. The objects below are attached to a fixed set of data on $E$: a prime $p \equiv 7 \pmod{16}$, elements $r, w_0 \in O_E$ with $r^2 = -p$ and $2w_0 = 1 + r$, and the assumption that $O_E$ is unramified over the ring of integers of the maximal real subfield. We fix a ring structure with involution on $O_E$ whose involution is $a \mapsto \bar a$. Let $V$ be a local ring and $S = \operatorname{Spec} V$.

For a line bundle $L$ on a commutative group scheme $G$ over $S$, we write $\Lambda(L)$ for the line bundle on $G \times_S G$ with fibre $L_{x+y} \otimes L_x^{-1} \otimes L_y^{-1} \otimes L_0$ at $(x, y)$, and $\Theta(L)$ for the line bundle on $G \times_S G \times_S G$ given by the analogous alternating product over the eight partial sums of $(x, y, z)$.

**Definition 3.7.1 (Semi-abelian scheme with cubical data).** A *semi-abelian scheme with cubical data* over $S$ consists of a commutative semi-abelian group scheme $G$ over $S$ (see [[abelian scheme|JDDXZ89N33]] for the proper case), an action $a \mapsto [a]$ of $O_E$ on $G$ by endomorphisms, a rigidified line bundle $L$ on $G$, and a cubical structure on $L$, that is, a generator of $\Theta(L)$. These are subject to the following conditions: the cubical structure is symmetric; for each $a \in O_E$ there is an isomorphism $\Lambda(L)_{([a]x, y)} \cong \Lambda(L)_{(x, [\bar a]y)}$; and $L$ is isomorphic to the line bundle obtained from $\Lambda(L)$ by restriction along $x \mapsto (x, [w_0]x)$.

**Definition 3.7.2 (Map over the identity).** Let $t = (G, L, \dots)$ and $t' = (G', L', \dots)$ be semi-abelian schemes with cubical data over $S$. A *map over the identity* $n : t \to t'$ is a morphism $\varphi : G \to G'$ over the identity of $S$ such that the square formed by $\varphi$ and the identity of $S$ is a pullback square of group schemes, $\varphi$ commutes with the actions of $O_E$, and the cubical structure of $L$ is the pullback of that of $L'$ along $\varphi$.

### Charts, jets and frames

Let $d \geq 0$. For $m \geq 0$ write $J_m$ for the $V$-algebra of jets of order $m$ in $d$ variables, that is, the polynomial ring in $d$ variables modulo the monomials of degree $m + 1$. A family of points $x_m : \operatorname{Spec} J_m \to G$ over $S$ is compatible if each $x_{m+1}$ restricts to $x_m$ along the truncation $J_{m+1} \to J_m$.

**Definition 3.7.3 (Universal jets).** A compatible family $(x_m)$ is *universal* if each $x_m$ sends the augmentation point to the origin, and for every $V$-algebra $A$ with an augmentation $A \to V$ whose kernel $I$ satisfies $I^{m+1} = 0$, every point $y : \operatorname{Spec} A \to G$ which sends the augmentation point to the origin factors as $y = x_m \circ \operatorname{Spec}\psi$ for a unique augmented $V$-algebra map $\psi : J_m \to A$.

Let $F$ be a formal group law of dimension $d$ over $V$ with an action $a \mapsto [a]_F$ of $O_E$, as in the [previous section](/entry/canon-gauge-exists/). For tangent vectors we use the dual numbers $V[\varepsilon]$: a tangent vector at the origin is a point $\operatorname{Spec} V[\varepsilon] \to G$ which lies over the origin modulo $\varepsilon$. The jet $x_1$ gives $d$ such vectors $\partial_1, \dots, \partial_d$, one for each variable. Given $u \in V^d$, we say that a tangent vector $v$ has *coordinates* $u$ in $x$ if $v$ is the sum, in the group of tangent vectors, of the vectors $\partial_j$ scaled by $u_j$.

**Definition 3.7.4 (Chart).** Let $(v_\ell)_{\ell \in \kappa}$ be a finite family of tangent vectors of $G$ at the origin and $(u_\ell)$ a family in $V^d$. A compatible family $(x_m)$ is a *chart* of $G$ with group law $F$, action $[a]_F$ and tangent data $(v_\ell, u_\ell)$ if the following hold for every $m$.

1. $x_m$ sends the augmentation point to the origin.
2. Substituting $F$ into $x_m$ gives the product, in $G$, of the restrictions of $x_m$ to the two copies of the jets, so that $x_m(F(X, Y)) = x_m(X) \cdot x_m(Y)$.
3. $[a] \circ x_m = x_m \circ [a]_F$ for every $a \in O_E$.
4. Each $v_\ell$ has coordinates $u_\ell$ in $x$.
5. Every $w \in V^d$ is $\sum_\ell c_\ell u_\ell$ for a unique family $(c_\ell)$ in $V$.

Let $e_m$ be a generator of the pullback of $\Lambda(L)$ along the pair of jets $(x_m(X), x_m(Y))$, for each $m$. We write $e(X, Y)$ for $e_m$, and $e(P, Q)$ for its pullback along a pair of substitutions $P$ and $Q$.

**Definition 3.7.5 (Frame).** Let $B = (F, [a]_F, \phi_1, \phi_2, s, \alpha)$ be a formal biextension over $V$ with an action of $O_E$, as in the [previous section](/entry/canon-gauge-exists/), and let $x$ be a chart of $G$ with the group law and action of $B$. A family $(e_m)$ of generators is a *frame* for $B$ if, for every $m$, the truncation to order $m$ of each of the following identities holds under the canonical identifications of line bundles.

1. The cubical structure at $(X, Y, Z)$ corresponds to $\phi_1(X, Y, Z)\, e(X + Y, Z)\, e(X, Z)^{-1}\, e(Y, Z)^{-1}$.
2. The cubical structure at $(Y, Z, X)$ corresponds to $\phi_2(X, Y, Z)\, e(X, Y + Z)\, e(X, Y)^{-1}\, e(X, Z)^{-1}$.
3. $e(X, Y)$ corresponds to $s(X, Y)^{-1}\, e(Y, X)$.
4. For each $a \in O_E$ there is a generator $\omega_a$ of the line bundle on $G \times_S G$ with fibre $\Lambda(L)_{([a]x, y)} \otimes \Lambda(L)_{(x, [\bar a]y)}^{-1}$ at $(x, y)$ such that $\omega_a(X, Y)\, e([a]_F X, Y)$ corresponds to $\alpha_a(X, Y)\, e(X, [\bar a]_F Y)$.

**Definition 3.7.6 (Relation to order $m$).** Let $B = (F, [a], \phi_1, \phi_2, s, \alpha)$ and $B' = (F', [a]', \phi_1', \phi_2', s', \alpha')$ be formal biextensions of dimension $d$ over $V$ with an action of $O_E$, and let $m \geq 0$. Let $\varphi$ and $\varphi^{-1}$ be $d$-tuples of power series in $d$ variables. We say that $B$ and $B'$ are *related to order $m$* by $\varphi$, $\varphi^{-1}$ and a series $\varepsilon \in V[[X, Y]]$ if:

1. $\varphi$ and $\varphi^{-1}$ have no constant term and are inverse to each other under composition;
2. the constant term of $\varepsilon$ is a unit;
3. $F'(X, Y) = \varphi^{-1}\bigl(F(\varphi X, \varphi Y)\bigr)$ and $[a]' = \varphi^{-1} \circ [a] \circ \varphi$ for each $a \in O_E$, exactly;
4. the following congruences hold modulo terms of total degree greater than $m$, where $+'$ is the sum for $F'$:
$$
\begin{aligned}
\phi_1'(X, Y, Z)\, \varepsilon(X +' Y, Z) &\equiv \phi_1(\varphi X, \varphi Y, \varphi Z)\, \varepsilon(X, Z)\, \varepsilon(Y, Z), \\
\phi_2'(X, Y, Z)\, \varepsilon(X, Y +' Z) &\equiv \phi_2(\varphi X, \varphi Y, \varphi Z)\, \varepsilon(X, Y)\, \varepsilon(X, Z), \\
s'(X, Y)\, \varepsilon(X, Y) &\equiv s(\varphi X, \varphi Y)\, \varepsilon(Y, X), \\
\alpha_a'(X, Y)\, \varepsilon(X, [\bar a]' Y) &\equiv \alpha_a(\varphi X, \varphi Y)\, \varepsilon([a]' X, Y).
\end{aligned}
$$

Lean: `GlobalTheory.ChartCmp.JRel`.

Thus $\varphi$ is an isomorphism from $F'$ to $F$ which respects the actions, and the biextension data of $B'$ are those of $B$ transported by $\varphi$ and changed by the coboundary of $\varepsilon$, up to order $m$. We write $d\varphi$ for the matrix of linear coefficients of $\varphi$, whose entry $(i, j)$ is the coefficient of $X_j$ in $\varphi_i$.

### Comparison of charts and frames

**Theorem 3.7.7 (Charts and frames along a map over the identity).** Let $t$ and $t'$ be semi-abelian schemes with cubical data over $S = \operatorname{Spec} V$, with groups $G$ and $G'$, and let $n : t \to t'$ be a map over the identity, with underlying morphism $\varphi_n : G \to G'$. Assume that every global function on $G' \times_S G'$ comes from $V$. Let $B$ and $B'$ be formal biextensions of dimension $d$ over $V$ with an action of $O_E$. Let $x$ be a chart of $G$ with the law and action of $B$, and $x'$ a chart of $G'$ with the law and action of $B'$, both universal, with some tangent data. Let $e$ be a frame for $B$ on $x$ and $e'$ a frame for $B'$ on $x'$. Then there are $d$-tuples $\varphi$ and $\varphi^{-1}$ of power series such that:

1. for every $m$ there is $\varepsilon$ such that $B$ and $B'$ are related to order $m$ by $\varphi$, $\varphi^{-1}$ and $\varepsilon$;
2. if a tangent vector $v$ of $G$ at the origin has coordinates $u$ in $x$, and $\varphi_n \circ v$ has coordinates $u'$ in $x'$, then $u = d\varphi \cdot u'$.

Lean: `GlobalTheory.ChartCmp.jrel_of_sabMap` (also `GlobalTheory.T.formal_biextensions_related_of_triple_map_over_id`, a second name).

*Proof.* The proof moves the chart and the frame of $t$ to $t'$ along $n$, and then compares two charts and two frames on the single scheme $t'$.

First, push the chart. Put $y_m = \varphi_n \circ x_m$. Then $y$ is universal, since $x$ is. It is a chart of $G'$ with the law and action of $B$ and with tangent data $(\varphi_n \circ v_\ell, u_\ell)$, since $\varphi_n$ is a homomorphism which commutes with the actions. If a tangent vector $v$ of $G$ has coordinates $u$ in $x$, then $\varphi_n \circ v$ has coordinates $u$ in $y$.

Second, a map over the identity is an isomorphism. There is an isomorphism of group schemes $G \cong G'$ with underlying morphism $\varphi_n$, which commutes with the actions, and an isomorphism $w : L \cong \varphi_n^* L'$ of line bundles under which the cubical structure of $L$ corresponds to the pullback of the cubical structure of $L'$.

Third, push the frame. Since each $e_m$ is a generator, the isomorphism $w$ carries $e_m$ to a generator $f_m$ of the pullback of $\Lambda(L')$ along the pair of jets of $y_m$. The four conditions of a frame for $B$ on $x$ are then transported along $w$, one at a time: the two cocycle conditions because $w$ respects the cubical structures, the symmetry condition because the canonical identifications are compatible with $w$, and the adjointness condition because $\varphi_n$ commutes with the actions, which lets us transport the generators $\omega_a$. Thus $f$ is a frame for $B$ on the chart $y$ of $t'$.

Fourth, compare on $t'$. Now $t'$ carries two universal charts, $y$ with the data of $B$ and $x'$ with the data of $B'$, and two frames, $f$ and $e'$. Since $y$ and $x'$ are universal, each is obtained from the other by a unique change of coordinates; this gives $\varphi$ and $\varphi^{-1}$, and the conditions on the group law and on the action follow from the chart conditions. Since $f$ and $e'$ are generators of the same line bundle on the jets, their ratio at order $m$ is a unit, which is the jet of a series $\varepsilon$. The result for this step takes as hypotheses that every global function on $G' \times_S G'$ comes from $V$ and that the involution of $O_E$ is complex conjugation. The frame conditions for $f$ and $e'$ then give the four congruences to order $m$. This shows that $B$ and $B'$ are related to order $m$ by $\varphi$, $\varphi^{-1}$ and $\varepsilon$. The same comparison shows that if a tangent vector $v'$ of $G'$ has coordinates $u$ in $y$ and $u'$ in $x'$, then $u = d\varphi \cdot u'$.

Finally, if $v$ has coordinates $u$ in $x$ and $\varphi_n \circ v$ has coordinates $u'$ in $x'$, then by the first step $\varphi_n \circ v$ has coordinates $u$ in $y$, so $u = d\varphi \cdot u'$ by the fourth step. $\square$

The series $\varphi$ does not depend on $m$, but the series $\varepsilon$ may: the theorem gives one $\varepsilon$ for each order, not a single series which works to all orders.

**Remark 3.7.8 (Formalization).** The statement under the second name is a wrapper of `GlobalTheory.ChartCmp.jrel_of_sabMap`, proved by a `first | exact` tactic with a raised heartbeat limit ([FormalBiextensionsRelatedOfTripleMapOverIdStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/FormalBiextensionsRelatedOfTripleMapOverIdStatement.lean#L10)). The main theorem is proved ([FormalBiextensionsRelatedOfTripleMapOverId.lean](lean:Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/FormalBiextensionsRelatedOfTripleMapOverId.lean#L22)) by assembling `GlobalTheory.T.pushChartAlt`, `GlobalTheory.T.exists_groupIso_cubicalIso_of_tripleMap_id`, `GlobalTheory.T.exists_pushFr_of_isGen`, the four transport results `firstPartialLaw_push_along_tripleMap`, `secondPartialLaw_push_along_tripleMap`, `famSy_of_pushFr_cubIso` and `adjointness_series_transport_frames`, and `GlobalTheory.T.chartsWithFrames_related_allOrders`; each is itself a wrapper of the same kind, and we have not unfolded them. Of the second step, only the isomorphism $w$ of line bundles is used: the group isomorphism and its properties are discarded at line 25. The relation `JRel` is defined in [AdditionLawSecondIdentity.lean](lean:Development/AbelianVarietyTheory/Definitions/TwoChartAtlas/AdditionLawSecondIdentity.lean#L23), and charts and frames are `IsChartG` and `IsFrameG` ([IsChartIff.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsChartIff.lean#L36)). In the definition of a frame, the generator $\omega_a$ of the adjointness condition is only required to exist: it is not tied to the adjointness isomorphism which is part of the data of $t$ ([IsChartIff.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsChartIff.lean#L107)). The fixed data on $E$, including the prime $p \equiv 7 \pmod{16}$ and $w_0$, enter only through the definition of the objects, and the theorem does not concern good reduction.

## Notes and references

The first four sections of this chapter prove the criterion of Néron, Ogg and Shafarevich and the theorem of Serre and Tate on potential good reduction of abelian varieties with complex multiplication, which enter the proof through [the step on inputs on CM abelian varieties from the literature](/step/cm-abelian-inputs-from-literature/). The last three sections prove the existence of semistable majorants of self-dual Hermitian lattices, the existence of canonical gauges of formal biextensions and the comparison of charts and frames, which enter through [the step on characters from the literature](/step/every-character-of-literature/).

- J.-P. Serre and J. Tate, *Good reduction of abelian varieties*, Ann. of Math. 88, 1968, §1, §2 and the section on complex multiplication.
- A. Grothendieck, *Modèles de Néron et monodromie*, SGA 7 I, Lecture Notes in Math. 288, Springer, 1972, Exposé IX; Exposés VII and VIII treat biextensions.
- S. Bosch, W. Lütkebohmert and M. Raynaud, *Néron Models*, Ergeb. Math. Grenzgeb. 21, Springer, 1990, §7.4 and Chapter 6.
- D. Mumford, *Abelian Varieties*, Oxford University Press, 1970, §4.
- D. Mumford, *Bi-extensions of formal groups*, Algebraic Geometry (Bombay Colloquium 1968), Oxford University Press, 1969.
- N. Bourbaki, *Commutative Algebra*, Hermann and Addison-Wesley, 1972, Chapter V, §2.
- U. Stuhler, *Eine Bemerkung zur Reduktionstheorie quadratischer Formen*, Arch. Math. 27, 1976.
- D. Grayson, *Reduction theory using semistability*, Comment. Math. Helv. 59, 1984.
