---
title: Hopf structures on cochain complexes and the bound on the first cohomology
decls:
  - GlobalTheory.CompanionTheory.HopfLe.core_step
  - GlobalTheory.CompanionTheory.HopfLe.hopfLeSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hopf structures on cochain complexes and the bound on the first cohomology

Sections 12 to 14 prove two facts on the cohomology of the structure sheaf of an abelian scheme over a field $k$, in a combinatorial form. Let $A$ be an abelian variety of dimension $g$ over $k$, with $H^n(A, \mathcal{O}) = 0$ for $n > g$. Then $\dim H^1(A, \mathcal{O}) \leq g$, and if $\dim H^1(A, \mathcal{O}) = g$, the cup product gives $\Lambda^2 H^1(A, \mathcal{O}) \cong H^2(A, \mathcal{O})$. The proofs use only the group law, through the fact that the classes in $H^1$ are primitive: their pullback by the multiplication $A \times A \to A$ is the sum of the two pullbacks by the projections. This is the argument of Hopf for the cohomology of a group. This section proves the bound, which is an input of the [row step](/step/every-character-of-row/). The isomorphism of Section 13 is an input of the [list of chapters of the Hodge and de Rham proof](/entry/abelian-hodge-de-rham-prime/) for abelian schemes.

We work with cochains on a category of affine open sets. Let $R$ be a commutative ring, $C$ a category and $F$ a functor from $C$ to commutative $R$-algebras. For $n \geq 0$, an *$n$-chain* in $C$ is a functor $c : [n] \to C$, where $[n] = \{0 < 1 < \dots < n\}$, so a string of $n$ composable arrows $c(0) \to \cdots \to c(n)$.

**Definition 7.12.1 (Cochain complex of a functor).** The module of *$n$-cochains* is
$$C^n(F) = \prod_{c : [n] \to C} F(c(n)).$$
For $0 \leq i \leq n+1$, the coface $\partial_i : C^n(F) \to C^{n+1}(F)$ sends $f$ to the cochain whose value on $c$ is $f(c \circ \delta_i)$, mapped into $F(c(n+1))$ along the arrow $c(\delta_i(n)) \to c(n+1)$. Here $\delta_i : [n] \to [n+1]$ is the injection that omits $i$. The differential is $d = \sum_i (-1)^i \partial_i$. We write
$$H^n(F) = \ker(d : C^n \to C^{n+1}) / \operatorname{im}(d : C^{n-1} \to C^n)$$
for $n \geq 1$, and $H^0(F) = \ker(d : C^0 \to C^1)$.

For an affine cover of a scheme $X$ that is closed under intersection, and $F$ the functor of sections of $\mathcal{O}_X$, this is a Čech complex of the nerve of the cover. Section 14 proves that it computes $H^n(X, \mathcal{O}_X)$. The *cup product* of $x \in C^1(F)$ and $z \in C^n(F)$ is the cochain $x \cup z \in C^{n+1}(F)$ with
$$(x \cup z)(c) = x(c(0) \to c(1)) \cdot z(c(1) \to \cdots \to c(n+1)),$$
where both factors are mapped into $F(c(n+1))$. It induces $H^1(F) \times H^n(F) \to H^{n+1}(F)$.

A *coefficient map* $m : F \to F'$, from $F$ on $C$ to $F'$ on $C'$, is a functor $G : C' \to C$ with a natural family of $R$-algebra maps $\alpha_T : F(G T) \to F'(T)$. It induces the pullback $m^* : C^n(F) \to C^n(F')$, $m^*(f)(c) = \alpha_{c(n)}(f(G \circ c))$, and maps $m^*$ on cohomology. It is a *quasi-isomorphism* if $m^*$ is bijective on $H^n$ for each $n$.

**Definition 7.12.2 (Square of a functor).** The *square* $F \boxtimes F$ is the functor on $C \times C$ with $(F \boxtimes F)(T, T') = F(T) \otimes_R F(T')$. The two *projections* $p_1, p_2 : F \to F \boxtimes F$ are the coefficient maps given by the two functors $C \times C \to C$ and the inclusions $a \mapsto a \otimes 1$ and $b \mapsto 1 \otimes b$. For $T_0 \in C$ and an $R$-algebra map $\varepsilon : F(T_0) \to R$, the *unit section* $e : F \boxtimes F \to F$ is the coefficient map given by $T \mapsto (T_0, T)$ and $a \otimes b \mapsto \varepsilon(a) b$.

For a group scheme $A$, $F \boxtimes F$ is the functor of a cover of $A \times A$ by products, and $e$ comes from the map $x \mapsto (0, x)$, with $\varepsilon$ the evaluation at the unit point $0 \in T_0$.

**Definition 7.12.3 (Hopf structure).** A *Hopf structure* on $F$ is a functor $G$ on a category $D$ with coefficient maps $\pi : F \boxtimes F \to G$ and $\mu : F \to G$ with these properties.

1. $\pi$ is a quasi-isomorphism.
2. For each $c \in H^1(F)$, $\mu^* c = \pi^*(p_1^* c + p_2^* c)$.

The structure is *with unit* if, in addition, there are $T_0 \in C$ and an $R$-algebra map $\varepsilon : F(T_0) \to R$ such that, for $y \in H^2(F)$ and $w \in H^2(F \boxtimes F)$ with $\pi^* w = \mu^* y$, we have $e^* w = y$.

In the geometric case $G$ is the functor of a common refinement on $A \times A$ of the product cover and of the pullback of the cover of $A$ by the multiplication. Then $\pi$ is the refinement and $\mu$ is the multiplication. The second property says that the classes in $H^1$ are primitive.

We say that $F$ is *Stein* if the map $R \to C^0(F)$ is injective and $R \to C^0(F) \to C^1(F)$ is exact. So $H^0(F) = R$.

For a linear form $\Lambda : C^1(F) \to R$ we use a *contraction* $T_\Lambda : C^{q+1}(F \boxtimes F) \to C^q(F)$. It is an alternating sum, over the ways to split a $(q+1)$-chain of $C \times C$ into a $1$-chain in the first factor and a $q$-chain in the second, of $\Lambda$ applied to the first tensor factor. It needs finitely many $1$-chains, so that the sum over them is finite. For a cocycle $x \in C^1(F)$, a cocycle $w$, and $\Lambda$ with $\Lambda \circ d = 0$ on $C^0$, it has these properties, which we take as given.

- $T_\Lambda(dr) = -d(T_\Lambda r)$ for each $r$. So $T_\Lambda$ sends boundaries to boundaries.
- $T_\Lambda(p_2^* x \cup w) = -x \cup T_\Lambda(w)$.
- If $F$ is Stein and $R$ is a field, then $T_\Lambda(p_1^* x \cup w) = \Lambda(x) \, e^* w + (\text{a boundary})$.
- In degree $0$, $T_\Lambda(p_1^* x + p_2^* x) = \Lambda(x) \cdot 1$.
- $e^* p_1^* x = 0$ and $e^* p_2^* x = x$.

**Lemma 7.12.4 (Contraction lemma).** Let $R$ be a field, and let $F$ be a functor on $C$ such that $C$ has finitely many $0$-chains and $1$-chains and $R \to C^0(F) \to C^1(F)$ is exact. Let $\pi : F \boxtimes F \to G$ and $\mu : F \to G$ be coefficient maps with $\pi$ a quasi-isomorphism, and let $T_0 \in C$ and $\varepsilon : F(T_0) \to R$ be an $R$-algebra map. Let $x_0, \dots, x_g \in C^1(F)$ be cocycles with $\pi^*(p_1^* x_i + p_2^* x_i) - \mu^* x_i$ a boundary for each $i$. Let $\Lambda_0, \dots, \Lambda_g : C^1(F) \to R$ be linear forms with $\Lambda_i \circ d = 0$ on $C^0(F)$ and $\Lambda_i(x_j) = \delta_{ij}$. Then for each $s \leq g$ there are cocycles $z \in C^{s+1}(F)$ and $w \in C^{s+1}(F \boxtimes F)$ with these properties.

1. $\pi^* w - \mu^* z$ is a boundary.
2. $e^* w = z$.
3. $T_{\Lambda_i}(w)$ is a boundary for each $i$ with $i + s < g$. In degree $0$ this means $T_{\Lambda_i}(w) = 0$.
4. If $z$ is a boundary, then $x_g$ is a boundary.

Lean: `GlobalTheory.CompanionTheory.HopfLe.core_step`.

The cochain $z$ is $x_{g-s} \cup \cdots \cup x_{g-1} \cup x_g$, and $w$ is the corresponding product of the cochains $p_1^* x_j + p_2^* x_j$.

*Proof.* We use induction on $s$. A cocycle $x \in C^1(F)$ and a boundary $b$ give a boundary $x \cup b$, since $d(x \cup y) = -x \cup dy$ for a cocycle $x$.

For $s = 0$, let $z = x_g$ and $w = p_1^* x_g + p_2^* x_g$. Both are cocycles, since pullbacks commute with $d$. The first claim is the hypothesis on $x_g$. The second follows from $e^* p_1^* x_g = 0$ and $e^* p_2^* x_g = x_g$. For $i < g$ we have $i \neq g$, so $T_{\Lambda_i}(w) = \Lambda_i(x_g) \cdot 1 = 0$. The fourth claim is trivial.

Now let $s + 1 \leq g$, take $z$ and $w$ for $s$, and let $j = g - s - 1$. Put $z' = x_j \cup z$ and $w' = (p_1^* x_j + p_2^* x_j) \cup w$. Both are cocycles, by the rule $d(x \cup y) = -x \cup dy$. For the first claim, write $\pi^*(p_1^* x_j + p_2^* x_j) = \mu^* x_j + du$ and $\pi^* w = \mu^* z + dv$. Pullbacks respect the cup product, so
$$\pi^* w' - \mu^* z' = (\mu^* x_j + du) \cup (\mu^* z + dv) - \mu^* x_j \cup \mu^* z,$$
and each remaining term is a boundary, since $\mu^* x_j$, $\mu^* z$ and $\pi^* w$ are cocycles. For the second claim, $e^* w' = (e^* p_1^* x_j + e^* p_2^* x_j) \cup e^* w = x_j \cup z = z'$.

By the properties of the contraction, for each $i$,
$$T_{\Lambda_i}(w') = \Lambda_i(x_j) \, z - x_j \cup T_{\Lambda_i}(w) + (\text{a boundary}). \tag{$*$}$$
For the third claim let $i + s + 1 < g$. Then $i < j$, so $\Lambda_i(x_j) = 0$, and $i + s < g$, so $T_{\Lambda_i}(w)$ is a boundary. By $(*)$, $T_{\Lambda_i}(w')$ is a boundary.

For the fourth claim, let $z' = dt$. Then $\pi^* w' = \mu^* z' + dv' = d(\mu^* t + v')$ is a boundary. Since $\pi$ is a quasi-isomorphism, $\pi^*$ is injective on cohomology, so $w' = dr$ for some $r$. Hence $T_{\Lambda_j}(w') = -d(T_{\Lambda_j} r)$ is a boundary. Since $j + s = g - 1 < g$, $T_{\Lambda_j}(w)$ is a boundary, and so is $x_j \cup T_{\Lambda_j}(w)$. With $\Lambda_j(x_j) = 1$, the formula $(*)$ for $i = j$ shows that $z$ is a boundary. By the fourth claim for $s$, $x_g$ is a boundary. $\square$

**Theorem 7.12.5 (Hopf bound on the first cohomology).** Let $P$ be a finite meet semilattice and $F$ a functor from $P^{\mathrm{op}}$ to commutative algebras over a field $R$. Let $g \geq 0$. Assume that $F$ is Stein, that $H^n(F) = 0$ for each $n \geq g + 1$, and that $F$ has a Hopf structure with unit. Then each family of $g + 1$ elements of $H^1(F)$ is linearly dependent. So $\dim_R H^1(F) \leq g$.

Lean: `GlobalTheory.CompanionTheory.HopfLe.hopfLeSt`.

*Proof.* Since $P$ is finite, it has finitely many chains of each length. Let $\xi_0, \dots, \xi_g \in H^1(F)$, and assume that they are linearly independent. Choose cocycles $x_i$ that represent them. Since $R$ is a field, there are linear forms $l_i$ on $H^1(F)$ with $l_i(\xi_j) = \delta_{ij}$. The space of $1$-cocycles is a subspace of $C^1(F)$, so the forms $l_i$, composed with the map from cocycles to classes, extend to linear forms $\Lambda_i$ on $C^1(F)$. A boundary $dy$ has class $0$, so $\Lambda_i \circ d = 0$ on $C^0(F)$. Also $\Lambda_i(x_j) = l_i(\xi_j) = \delta_{ij}$.

The second property of the Hopf structure says that $\mu^* \xi_i = \pi^*(p_1^* \xi_i + p_2^* \xi_i)$, so $\pi^*(p_1^* x_i + p_2^* x_i) - \mu^* x_i$ is a boundary. Since $F$ is Stein, $R \to C^0(F) \to C^1(F)$ is exact. Take $T_0$ and $\varepsilon$ from the unit. The lemma with $s = g$ gives a cocycle $z \in C^{g+1}(F)$ such that if $z$ is a boundary, then $x_g$ is a boundary. Since $H^{g+1}(F) = 0$, $z$ is a boundary. So $x_g$ is a boundary and $\xi_g = 0$. This contradicts the linear independence. $\square$

The proof uses the unit only for $T_0$ and $\varepsilon$, which define the map $e$. The compatibility of $e$ with $\pi$ and $\mu$ on $H^2$ is not used here. It is used in Section 13.

**Remark 7.12.6 (Formalization).** Both results are in [Cup1BoundaryOfBoundary.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Cup1BoundaryOfBoundary.lean#L120), with the theorem at line 259. The cochains `Cn`, the differential `dn`, the coefficient maps and the definitions `Stein`, `AllQIso`, `box`, `boxL`, `boxR`, `boxE` and `Hopf` are in [H1CommutesBaseChange.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/HodgeWedgeFields/H1CommutesBaseChange.lean#L34); `Hopf b` adds the unit when `b` holds. The statement `HopfLeSt` is in [IsPullbackH2Structure.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/HodgeWedgeFields/IsPullbackH2Structure.lean#L19). The contraction is `T` in [BisimplicialActionSecondFactor.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BisimplicialActionSecondFactor.lean#L85). In the statement, $H^1(F)$ is `GlobalTheory.CatCoh.H1 F`, the cohomology of a low degree complex, and the proof moves between it and `Cn` with the bijections `Dict.L0`, `Dict.L1` and `Dict.L2`. The theorem is stated as `CxSt → DictSt → LowSt → HopfLeSt` and does not use its three hypotheses. It also drops the compatibility part of `Hopf F True` with `obtain ⟨T₀, ε, -⟩`. In the lemma, the boundary condition in degree $0$ is `IsB`, which means equal to $0$.
