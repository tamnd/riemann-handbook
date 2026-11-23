---
title: The exterior square of the first cohomology
decls:
  - GlobalTheory.CompanionTheory.HopfC.package
  - GlobalTheory.CompanionTheory.HopfC.hopfFieldSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The exterior square of the first cohomology

This section proves the second fact of Hopf type. If $F$ has a Hopf structure with unit over a field, $H^1(F)$ has dimension $g$, and $H^n(F) = 0$ for $n > g$, then the cup product gives an isomorphism $\Lambda^2 H^1(F) \cong H^2(F)$. The proof builds, for each linear form $l$ on $H^1(F)$, an operator $D(l)$ that lowers the degree by one and acts on cup products by a Leibniz rule. A statement of linear algebra on graded modules with such operators then gives the isomorphism. The theorem is an input of the [list of chapters of the Hodge and de Rham proof](/entry/abelian-hodge-de-rham-prime/), where $F$ comes from an affine cover of an abelian scheme over a field.

We keep the notation of Section 12. So $C^n(F)$ is the module of $n$-cochains of a functor $F$ on a category $C$, $H^n(F)$ is its cohomology, with $H^0(F) = \ker(d : C^0 \to C^1)$, the cup product is $x \cup z$ for $x \in H^1$ and $z \in H^n$, and $p_1$, $p_2$ and $e$ are the projections and the unit section of the square $F \boxtimes F$. We write $1 \in H^0(F)$ for the class of the unit cochain, the cochain with value $1$ on each object.

**Lemma 7.13.1 (Lowering operators from a Hopf structure).** Let $R$ be a field and $F$ a functor from $C$ to commutative $R$-algebras, with finitely many $n$-chains in $C$ for each $n$. Assume that $d(df) = 0$ for each $f \in C^0(F)$, and that each $f \in C^0(F)$ with $df = 0$ is a constant $r \cdot 1$ with $r \in R$. Let $\pi : F \boxtimes F \to G$ and $\mu : F \to G$ be coefficient maps such that:

1. $\pi$ is a quasi-isomorphism;
2. $\mu^* x = \pi^*(p_1^* x + p_2^* x)$ for each $x \in H^1(F)$;
3. for some $T_0 \in C$ and an $R$-algebra map $\varepsilon : F(T_0) \to R$, with unit section $e$, each $y \in H^2(F)$ and $w \in H^2(F \boxtimes F)$ with $\pi^* w = \mu^* y$ have $e^* w = y$.

Then there are linear maps $D_n(l) : H^{n+1}(F) \to H^n(F)$ for each $n \geq 0$ and each linear form $l$ on $H^1(F)$, and linear maps $\tau_n : H^n(F) \to H^n(F)$, with these properties for $x \in H^1(F)$:

- $x \cup 1 = x$;
- $D_0(l)(x) = l(x) \cdot 1$;
- $D_{n+1}(l)(x \cup z) = l(x) \, \tau_{n+1}(z) - x \cup D_n(l)(z)$ for $z \in H^{n+1}(F)$;
- $\tau_{n+2}(x \cup z) = x \cup \tau_{n+1}(z)$ for $z \in H^{n+1}(F)$;
- $\tau_1$ and $\tau_2$ are the identity maps.

Lean: `GlobalTheory.CompanionTheory.HopfC.package`.

*Proof.* Since $\pi$ is a quasi-isomorphism, $\pi^*$ is a bijection from $H^n(F \boxtimes F)$ to $H^n(G)$ for each $n$. Let $\theta = (\pi^*)^{-1} \circ \mu^* : H^n(F) \to H^n(F \boxtimes F)$. Pullbacks respect cup products, so $\theta(x \cup z) = \theta(x) \cup \theta(z)$. The second hypothesis says that $\theta(x) = p_1^* x + p_2^* x$ for $x \in H^1(F)$.

The unit cochain is a cocycle, and $x \cup 1 = x$ already on cochains. Put $\tau_n = e^* \circ \theta$. For $x \in H^1(F)$, $\tau_1(x) = e^* p_1^* x + e^* p_2^* x = 0 + x$, by the properties of $e$ in Section 12. For $y \in H^2(F)$, let $w = \theta(y)$. Then $\pi^* w = \mu^* y$, so $\tau_2(y) = e^* w = y$ by the third hypothesis. For $z \in H^{n+1}(F)$,
$$\tau_{n+2}(x \cup z) = e^* \theta(x) \cup e^* \theta(z) = \tau_1(x) \cup \tau_{n+1}(z) = x \cup \tau_{n+1}(z).$$

Now let $l$ be a linear form on $H^1(F)$. The $1$-cocycles form a subspace of $C^1(F)$. Since $R$ is a field, the form that sends a cocycle to $l$ of its class extends to a linear form $l'$ on $C^1(F)$. For $f \in C^0(F)$, $df$ is a cocycle by the first hypothesis, and its class is $0$, so $l'(df) = 0$. By the properties of the contraction in Section 12, $T_{l'}$ sends cocycles to cocycles and boundaries to boundaries, so it induces maps $T_{l'} : H^{n+1}(F \boxtimes F) \to H^n(F)$. Put
$$D_n(l) = T_{l'} \circ \theta : H^{n+1}(F) \to H^n(F).$$

We take as given three identities for the contraction. For a cocycle $x \in C^1(F)$, a cocycle $w$ on $F \boxtimes F$ of degree $n + 1$ and $l'$ as above:

- in degree $0$, $T_{l'}(p_1^* x + p_2^* x) = l'(x) \cdot 1$;
- $T_{l'}(p_2^* x \cup w) = -x \cup T_{l'}(w)$;
- $T_{l'}(p_1^* x \cup w) - l'(x) \, e^* w$ is a boundary.

The last identity uses the hypothesis on the $0$-cocycles: the contraction with a linear form $\Theta$ on $C^0(F)$ differs from $\Theta(1)$ times the contraction with the evaluation at $\varepsilon$ by a boundary, because $\Theta - \Theta(1) \varepsilon$ vanishes on the constants, which are the $0$-cocycles, and so factors through $d$.

The first identity gives $D_0(l)(x) = T_{l'}(p_1^* x + p_2^* x) = l(x) \cdot 1$. For $z \in H^{n+1}(F)$, let $w = \theta(z)$. Then
$$D_{n+1}(l)(x \cup z) = T_{l'}\big((p_1^* x + p_2^* x) \cup w\big) = l(x) \, e^* w - x \cup T_{l'}(w) = l(x) \, \tau_{n+1}(z) - x \cup D_n(l)(z). \qquad \square$$

For $n = 0$ the Leibniz rule reads $D_1(l)(x \cup y) = l(x) y - l(y) x$ for $x, y \in H^1(F)$. If $l_1, \dots, l_g$ is the dual basis of a basis $x_1, \dots, x_g$, this gives $D_1(l_j)(x_i \cup x_k) = \delta_{ji} x_k - \delta_{jk} x_i$, so the products $x_i \cup x_k$ with $i < k$ are linearly independent.

**Theorem 7.13.2 (Exterior square of the first cohomology).** Assume these two facts on cochains, for every ring $R$ and every functor $F$ from a category to commutative $R$-algebras:

1. $d \circ d = 0$ on $C^n(F)$ for each $n$, and $m^* \circ d = d \circ m^*$ for each coefficient map $m$;
2. the cochains $C^0, \dots, C^3$ of Section 12 agree with the cochains of the low degree complex, made of functions on objects, arrows, pairs and triples of composable arrows, and the identifications are compatible with $d$.

Let $P$ be a finite meet semilattice and $F$ a functor from $P^{\mathrm{op}}$ to commutative algebras over a field $R$. Let $g \geq 0$. Assume that $F$ is Stein, that $H^1(F)$ has dimension $g$, that $H^n(F) = 0$ for each $n \geq g + 1$, and that $F$ has a Hopf structure with unit. Then there is an isomorphism $\Lambda^2 H^1(F) \cong H^2(F)$ that sends $a \wedge b$ to $a \cup b$.

Lean: `GlobalTheory.CompanionTheory.HopfC.hopfFieldSt`.

Here $H^1$, $H^2$ and the cup product are those of the low degree complex. The second fact identifies them with the cohomology of Section 12.

*Proof.* We take as given four inputs.

1. *Finite chains.* A finite meet semilattice has finitely many $n$-chains for each $n$.
2. *Comparison in low degrees.* Given the second fact, there are isomorphisms between $H^1$ and $H^2$ of the low degree complex and of the complex of Section 12. They commute with pullbacks by coefficient maps, they carry the cup product of one complex to that of the other, and each low degree cocycle comes from a cocycle of Section 12.
3. *Stein functors.* Given the second fact, if $F$ is Stein, then each $f \in C^0(F)$ with $df = 0$ is $r \cdot 1$ for some $r \in R$, and $r \cdot 1 = 0$ only for $r = 0$.
4. *Linear algebra.* Let $(H^n)_{n \geq 0}$ be modules over a ring $R$, with a basis of $H^1$ of size $g$, an element $1 \in H^0$ with $r \cdot 1 = 0$ only for $r = 0$, bilinear products $H^1 \times H^n \to H^{n+1}$, and operators $D_n(l)$ and $\tau_n$ with the five properties of the lemma. If $H^{g+2} = 0$, then the product gives an isomorphism $\Lambda^2 H^1 \cong H^2$.

The first fact gives $d(df) = 0$ on $C^0(F)$. The third input gives the hypothesis of the lemma on $0$-cocycles. Transport the primitivity of the Hopf structure and the compatibility of its unit along the comparison isomorphisms of the second input, for $F$, $F \boxtimes F$ and $G$. This gives the second and third hypotheses of the lemma. The first input and the lemma give $1$, $D$ and $\tau$.

The isomorphism of the second input carries a basis of $H^1(F)$ of size $g$ to a basis of size $g$. The group $H^{g+2}(F)$ is $0$, since $d$ is exact at $C^{g+2}(F)$ by hypothesis. The third input gives $r \cdot 1 = 0$ only for $r = 0$. The fourth input gives $\Lambda^2 H^1 \cong H^2$ for the complex of Section 12, with the cup product. The comparison isomorphisms carry it to the required isomorphism for the low degree complex. $\square$

Only $H^{g+2} = 0$ is used, not $H^{g+1} = 0$.

**Remark 7.13.3 (Formalization).** Both results are in [TransferSumProjectionsDegreeZero.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TransferSumProjectionsDegreeZero.lean#L274), with the theorem at line 372. The statement `HopfFieldSt` is in [H1CommutesBaseChange.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/HodgeWedgeFields/H1CommutesBaseChange.lean#L378). The cohomology of Section 12 is `HH`, with the product `Lc`; the low degree cohomology is `GlobalTheory.CatCoh.H1` and `H2`, with `cup`. The theorem is stated as `CxSt → DictSt → LowSt → HopfFieldSt`. It uses `CxSt` and `DictSt`, which are the two facts on cochains, and it does not use `LowSt`; the third binder is `_`. The inputs are `T.finite_functor_category_of_meet_lattice`, `T.low_degree_cocycles_lift_to_nerve`, `T.low_degree_comparison_independent_of_choice`, `T.cup_product_compatible_with_comparison`, `T.stein_cocycles_degree_zero_are_constants`, `T.vector_space_has_basis_of_dimension`, `T.contraction_lowering_derivation_formula` and `T.exteriorSquare_transport_along_equiv`. The linear algebra input does not require $R$ to be a field. In `HopfFieldSt` the dimension is given by `VB R (H1 F) g`, which says that $H^1$ is finite projective of constant rank $g$.
