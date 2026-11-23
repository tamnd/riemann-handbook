---
title: Hecke operators on sections of the moduli space
decls:
  - GlobalTheory.HeckeEx.heckeTransform_of_pointLaws
  - GlobalTheory.HeckeEx.secTransform
  - GlobalTheory.HeckeEx.exists_sum
  - GlobalTheory.HeckeEx.exists_term
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke operators on sections of the moduli space

This section builds the Hecke operator at a split prime on algebraic sections of a unitary moduli space, and shows that it keeps cusp forms. Sections are defined as rules on framed points, in the style of Katz, so the operator is first defined on geometric points as a sum over isogenies. The work is to show that this sum comes from a section: it is algebraic, it commutes with base change, and it has the right weight. The result is the transform part of [the Hecke integrality, transform and reading facts](/entry/hecke-int-transform-read-tie/). The classical picture is the Hecke operator $T_p$ on modular forms, seen as a sum over the $p$-isogenies of an elliptic curve ([modular forms](/learn/automorphic-forms/#modular-forms)).

### Framed points and sections

Let $E$ be a CM field and let $X$ be a moduli space of abelian schemes $A$ with an action of $\mathcal{O}_E$, a polarization, and a level structure of level prime to an integer $M$, of signature $(p, q)$ with $p + q \ge 1$. Let $F_c$ be a coefficient field. For an $F_c$-algebra $S$, a *framed point* over $S$ is a point $x \in X(S)$ together with:

- for each embedding $\tau : E \to \mathbb{C}$, a basis $u_{\tau,1}, \dots, u_{\tau,m_\tau}$ of the $\tau$-part of the Lie algebra of $A_x$, where $m_\tau$ is the multiplicity of $\tau$ in the signature;
- a generator $s$ of the theta line of $A_x$.

A *rule* $f$ assigns to each framed point $y$ over each test ring $S$ (a reduced finitely generated $F_c$-algebra) a value $f(y) \in S$. Let $T$ be the torus of tuples $t = (t_0, (t_{\tau,j}))$ of units. The upper triangular group acts on framings: $t$ and a strictly upper triangular part change the bases $u_\tau$ by a triangular matrix with diagonal $t_{\tau,j}$, and change $s$ to $t_0 s$. For a weight $(a, n)$, with $a(\tau, j) \in \mathbb{N}$ and $n \in \mathbb{N}$, write
$$\chi_{a,n}(t) = t_0^{\,n} \prod_{\tau, j} t_{\tau,j}^{\,a(\tau,j)}.$$

**Definition 6.9.1 (Section of weight $(a, n)$).** A rule $f$ is a *section of weight* $(a, n)$ if:

1. it commutes with base change: if $\varphi : S \to S'$ is a map of $F_c$-algebras and $y'$ is the base change of $y$ along $\varphi$, then $f(y') = \varphi(f(y))$;
2. it has the weight law: if $y'$ is obtained from $y$ by the triangular change with diagonal $t$, then $f(y') = \chi_{a,n}(t)\, f(y)$.

The sections of weight $(a, n)$ form an $F_c$-vector space. This is the algebraic version of the space of automorphic forms of a given weight on the unitary group ([automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups)).

### Hecke kernels and the Hecke sum

Let $\mathfrak{P}$ be a prime of $E$ over a rational prime $p_0$. Call $(\mathfrak{P}, p_0)$ *split off* if $\mathfrak{P}$ is maximal, $\mathfrak{P}$ and its complex conjugate $\bar{\mathfrak{P}}$ are coprime, $p_0$ is prime, $p_0 \in \mathfrak{P}$, and $p_0$ does not divide $M$. Fix $i \ge 0$. For a geometric point $y$ over an algebraically closed field $\Omega$, a *Hecke kernel* of type $(\mathfrak{P}, p_0, i)$ at $y$ is a finite $\mathcal{O}_E$-stable subgroup $C$ of $A_y$ of the type fixed by $(\mathfrak{P}, i)$. A *Hecke point* of $C$ is a framed point $z$ over $\Omega$ together with an isogeny $\psi : A_y \to A_z$ with kernel $C$ that:

- lies over the same point of the base;
- multiplies the Weil pairings by the factor $u \mapsto u^{p_0^2}$ and respects the level structures up to the inverse of $p_0$ modulo $M$;
- carries each tangent vector $u_{\tau,j}(y)$ to $p_0^{-1}$ times the image of $u_{\tau,j}(z)$, under the map of Lie algebras;
- carries the theta generators by the trace map of $\psi$.

The *term* of a rule $f$ at $(y, C)$ is $f(z)$ for a Hecke point $z$ of $C$, and $0$ if there is none. The four *point laws* are the following statements, for all data and all split-off primes:

- (finite) there are finitely many Hecke kernels at each geometric point;
- (total) every Hecke kernel has a Hecke point;
- (single-valued) two Hecke points of the same kernel differ by an isomorphism of framed points;
- (detection) a section whose values at all geometric points vanish is $0$.

For a scalar $c_q \in F_c$, put $\lambda = c_q \cdot (\mathrm{N}\mathfrak{P})^{-\lfloor in/2 \rfloor}$.

**Lemma 6.9.2 (Term over a reduced ring).** Assume the total law, and let $(\mathfrak{P}, p_0)$ be split off. Let $f$ be a section of weight $(a, n)$, let $B$ be a reduced $F_c$-algebra, let $y$ be a framed point over $B$, and let $h$ be a $B$-point of the Hecke correspondence $Z \to X$ over the point of $y$. Then there is $b \in B$ such that for every algebraically closed $\Omega$, every map $\chi : B \to \Omega$, and every Hecke kernel $C$ at the base change $y_\chi$ that is carried by $h$ at $\chi$, the value $\chi(b)$ is the term of $f$ at $(y_\chi, C)$.

Lean: `GlobalTheory.HeckeEx.exists_term`.

*Proof.* The question is local on $\operatorname{Spec} B$ for the smooth topology, since a function on a reduced ring is fixed by its geometric values and smooth maps of reduced rings have reduced targets. Fix a prime $\mathfrak{q}$ of $B$. There is an étale cover $B \to T'$ over which the Hecke kernel carried by $h$ is listed by sections $\sigma_j$, and a localization $T = T'_g$ at a function $g \notin \mathfrak{q}$ over which the theta line of the target has a generator $s_0$. Over $T$, the family of Hecke isogenies with the kernel of $h$ exists, and the target with the transported tangent bases and the generator $s_0$ is a framed point. The section $f$ evaluated on this framed point is an element $b' \in T$. At each geometric point of $T$ it is the term of $f$, by the uniqueness of the base change and the single-valued choice of the target. The local elements glue to $b \in B$, by descent for functions on reduced rings along smooth covers. $\square$

**Lemma 6.9.3 (Hecke sum as a trace).** Assume the total law, let $p + q \ge 1$, and let $(\mathfrak{P}, p_0)$ be split off. Let $f$ be a section of weight $(a, n)$, let $R$ be a reduced $F_c$-algebra, and let $y$ be a framed point over $R$. Then there is $v \in R$ such that for every algebraically closed $\Omega$, every $\varphi : R \to \Omega$, and every framed point $z$ over $\Omega$ that is the base change of $y$ along $\varphi$,
$$\varphi(v) = \sum_{C} \mathrm{term}(f, z, C),$$
the sum over the Hecke kernels $C$ at $z$.

Lean: `GlobalTheory.HeckeEx.exists_sum`.

*Proof.* Since $p + q \ge 1$, there is a Hecke correspondence $Z$ over $X$ whose first projection $\pi_1 : Z \to X$ is finite and étale. Its pullback along the point of $y$ is $\operatorname{Spec} B$ for a finite étale $R$-algebra $B$, which is reduced because $R$ is reduced. Base change $y$ to $B$. The tautological point $h$ of $Z$ over $B$ carries one Hecke kernel at each geometric point, so the term lemma gives $b \in B$ with these terms as values. Let $v = \operatorname{Tr}_{B/R}(b)$. For a finite étale algebra, $\varphi(v) = \sum_\chi \chi(b)$, where $\chi$ runs over the maps $B \to \Omega$ that extend $\varphi$. These maps are in bijection with the points of $Z$ over $z$, and so with the Hecke kernels at $z$. The two sums agree term by term. $\square$

### The Hecke operator

**Theorem 6.9.4 (Hecke transform of a section).** Assume the point laws. Let $p + q \ge 1$, let $(\mathfrak{P}, p_0)$ be split off, let $i \le p + q$, let $n$ be even, and let $c_q \in F_c$. Then for every section $f$ of weight $(a, n)$ there is a section $g$ of weight $(a, n)$ such that
$$g(y) = \lambda \sum_C \mathrm{term}(f, y, C)$$
at every geometric point $y$. By detection, $g$ is unique. Write $g = T_{\mathfrak{P}, i} f$.

Lean: `GlobalTheory.HeckeEx.secTransform`.

*Proof.* A test ring is reduced, because its ideal is radical. For each test ring $S$ and framed point $y$ over $S$, the trace lemma gives an element $g_0(y) \in S$ whose geometric values are the Hecke sums. An element of a reduced finitely generated algebra is fixed by its values at geometric points. So it suffices to check the two laws of a section at geometric points. Base change: if $y'$ is the base change of $y$ along $\varphi$, then a geometric point over $y'$ is a geometric point over $y$, and both $g_0(y')$ and $\varphi(g_0(y))$ have the Hecke sum at it as value. The weight law: if $y'$ is a triangular change of $y$ with diagonal $t$, then the Hecke kernels at $y$ and $y'$ are the same, the Hecke points change by a triangular change with the same diagonal (by the single-valued law), and so each term is multiplied by $\chi_{a,n}(t)$. Hence $g_0$ is a section of weight $(a, n)$, and $g = \lambda g_0$ is too. Every geometric point is the base change of a framed point over a test ring, so $g$ has the stated values. $\square$

**Theorem 6.9.5 (Hecke operators keep cusp forms).** Assume the point laws. For each theta datum, each index $j$ in the indefinite range, each split-off prime, each $i$ and $c_q$, and each dominant weight $(a, n)$ ($a(\tau, \cdot)$ decreasing and $n$ even), the operator $T_{\mathfrak{P}, i}$ maps the cusp forms of weight $(a, n)$ to cusp forms.

Lean: `GlobalTheory.HeckeEx.heckeTransform_of_pointLaws` (the transform theorem and this theorem together).

*Proof.* A section is a cusp form if, for each complex embedding of $F_c$, its pullback to each component of the complex uniformization lies in the space of holomorphic cusp forms of the weight $(a, n)$. Let $f$ be a cusp form and $g = T_{\mathfrak{P}, i} f$. Fix a point $x$ of a component and a unit frame at it. Each Hecke point of a kernel at $x$ is a framed point on some component, reached by a rational similitude $a$ of factor $p_0$ and a triangular change $b$ whose diagonal entries have absolute value $1$. The diagonal $t$ of the triangular change that compares the Hecke point with the framed point on its component satisfies $|t_{\tau,j}| = 1$ for the tangent entries, and $|t_0| \le (\mathrm{N}\mathfrak{P})^{i}$ for the theta entry, by a bound on the generator ratio of the isogeny. So each term is at most $(\mathrm{N}\mathfrak{P})^{in}$ times the bound for $f$. The number of kernels is bounded by a constant $M_0$ that depends only on $(\mathfrak{P}, p_0)$. So $|g|$ is bounded by $|\lambda| \cdot M_0 \cdot (\mathrm{N}\mathfrak{P})^{in}$ times the bound for $f$, along all rational similitudes. A section that is dominated in this way along the rational similitudes, and whose pullbacks are holomorphic, is a cusp form. $\square$

**Remark 6.9.6 (Formalization).** The transform theorem and the cusp theorem are paired in one statement ([HeckeTransformOfPointLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTransformOfPointLaws.lean#L419)). The cusp theorem takes no hypothesis at line 404, because its statement assumes the transform, detection and finiteness itself ([SplitOffDetection.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/SplitOffDetection.lean#L50)). In the transform theorem, the intro on line 226 discards the hypotheses $i \le p + q$ and "$n$ even", so the theorem holds without them; the finite law and the detection law are not used, since reducedness does the work of detection. The intro of the cusp theorem also discards the bound on $i$. The exponent $in/2$ uses division of natural numbers ([LiftLaSpec.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/LiftLaSpec.lean#L57)), which is the floor; for $n$ even it is exact. The type of a Hecke kernel and the trace map on theta lines were not unfolded. The term is $0$ when no Hecke point exists, and the sum is a finite sum that would be $0$ on an infinite set of kernels; in the trace lemma the kernels are in bijection with the points of a finite étale algebra, so neither convention matters.
