---
title: Hodge cohomology by Čech complexes
decls:
  - CrystallineSemistableComparison.Om.L2.hodge_affine_iso_sign
  - CrystallineSemistableComparison.Om.L2.hdg_aff_iso_onto
  - CrystallineSemistableComparison.Om.Nt2.TermAff.term_aff
  - GlobalTheory.CompanionTheory.OmGlobTerm.AssemblyHe1.term
  - CrystallineSemistableComparison.Om.GlobPf2.glob_iso
  - CrystallineSemistableComparison.Om.Nt2F.glob_iso_c
  - CrystallineSemistableComparison.Om.Nt2F.hodge_iso_natural_cech
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge cohomology by Čech complexes

The Hodge-Tate comparison of this chapter compares étale cohomology with a cohomology $\mathrm{Hdg}(a, n)$ that is defined on a site of divided-power thickenings. The classical statement uses the coherent cohomology $H^{n-a}(X, \Omega^a)$. This section proves that the two agree for a smooth proper scheme over a field of characteristic $0$, naturally in the scheme. The proof goes from affine schemes, where both sides are differential forms, to a Čech complex of forms on a coordinate cover, and then to sheaf cohomology. The result is used in the next sections, where the top power of a Chern class and the Hodge-Tate pairing are computed in $\mathrm{Hdg}$ and read off in $H^j(X, \Omega^a)$.

**Definition 2.1.1 (Hodge cohomology on the thickening site).** Let $K$ be a field and $q : X \to \operatorname{Spec} K$ a scheme over $K$. On the site of divided-power thickenings of opens of $X$, the structure sheaf has a divided-power ideal $J$ and its divided-power filtration $J^{[a]}$. For $a, n \geq 0$ put
$$\mathrm{Hdg}(a, n) = H^n\big(J^{[a]} / J^{[a+1]}\big),$$
a $K$-vector space. It has a cup product $\mathrm{Hdg}(a, i) \times \mathrm{Hdg}(a', j) \to \mathrm{Hdg}(a + a', i + j)$, a unit $1 \in \mathrm{Hdg}(0, 0)$, and a pullback $u^* : \mathrm{Hdg}_Y(a, n) \to \mathrm{Hdg}_X(a, n)$ for each map $u : X \to Y$ over $K$.

This is the right object because the graded pieces of the divided-power filtration are the place where the Hodge-Tate decomposition lives: the comparison maps of the later sections land in them, and the cup product and pullback are the structures that the comparison must respect.

**Definition 2.1.2 (Differential forms and Hodge cohomology).** For $q : X \to \operatorname{Spec} K$ let $\Omega^a$ be the sheaf of $a$-forms of $X$ over $K$, the sheafification of $U \mapsto \Omega^a_{\mathcal{O}(U)/K}$. It has the wedge product $\Omega^a \times \Omega^b \to \Omega^{a+b}$, the unit $1 \in \Omega^0$, restriction to smaller opens, and pullback along maps over $K$. The *Hodge cohomology* of $X$ is the sheaf cohomology $H^j(X, \Omega^a)$.

**Definition 2.1.3 (Coordinate cover).** Let $q : X \to \operatorname{Spec} K$ be smooth. A *coordinate cover* $\mathcal{U}$ of $X$ is a finite family of opens $(U_\alpha)_{\alpha \in I}$ that covers $X$, such that each $U_\alpha$ has étale coordinates (functions $t_1, \dots, t_d$ on $U_\alpha$ with $K[t_1, \dots, t_d] \to \mathcal{O}(U_\alpha)$ étale), and such that each nonempty finite intersection $U_{\alpha_0 \cdots \alpha_j} = U_{\alpha_0} \cap \dots \cap U_{\alpha_j}$ is an affine open. The *Čech complex of $a$-forms* $C^\bullet(\mathcal{U}, \Omega^a)$ has in degree $j$ the families $(\omega_{\alpha_0 \cdots \alpha_j})$, indexed by all ordered tuples $(\alpha_0, \dots, \alpha_j) \in I^{j+1}$, with $\omega_{\alpha_0 \cdots \alpha_j} \in \Omega^a(U_{\alpha_0 \cdots \alpha_j})$, and the usual alternating sum of restrictions as differential.

A coordinate cover is the right tool because both sides of the comparison are computable on it: on each intersection the thickening cohomology is a space of forms, and the forms on the intersections assemble into a complex.

We first treat affine schemes. Here $\mathrm{Hdg}(a, a)$ is the space of global $a$-forms, and the product becomes the wedge product up to a sign.

**Theorem 2.1.4 (Hodge cohomology of a smooth affine scheme).** Let $K$ be a field of characteristic $0$. There are $K$-linear isomorphisms
$$e_X : \mathrm{Hdg}(a, a) \xrightarrow{\ \sim\ } \Omega^a(X),$$
one for each smooth affine $X$ over $K$ and each $a \geq 0$, and a function $\varepsilon : \mathbb{N} \times \mathbb{N} \to \mathbb{Z}$ with $\varepsilon(a, b) \in \{1, -1\}$ for all $a, b$, with these properties.

1. For smooth affine $X$ and $Y$ over $K$, a map $u : X \to Y$ over $K$ and $x \in \mathrm{Hdg}_Y(a, a)$, $e_X(u^* x) = u^*(e_Y(x))$.
2. For $a + b = c$, $x \in \mathrm{Hdg}(a, a)$ and $y \in \mathrm{Hdg}(b, b)$, $e_X(x \cup y) = \varepsilon(a, b)\, e_X(x) \wedge e_X(y)$ in $\Omega^c(X)$.
3. $e_X(1) = 1$.

Lean: `CrystallineSemistableComparison.Om.L2.hodge_affine_iso_sign`.

*Proof.* We take as given the two hypotheses of the next theorem. The first comes from a uniqueness statement for maps out of forms: a $K$-linear map from $\Omega^a(V)$ that is compatible with sums, scalars, wedge products and the unit is fixed by its values on functions and their differentials. The second is the naturality of these maps under restriction along maps over $K$. The next theorem then gives the conclusion. $\square$

**Theorem 2.1.5 (Affine case from two hypotheses).** Assume the following two statements.

1. For every field $K$ of characteristic $0$, every scheme $Z$ over $K$, every open $V \subseteq Z$ with étale coordinates and every $a$: the group $H^j(J^{[a]}/J^{[a+1]})$ on the thickenings of $V$ is zero for $j \neq a$, and there is a bijective $K$-linear map $\Omega^a(V) \to H^a(J^{[a]}/J^{[a+1]})$ that is compatible with the sum, the scalar action, the wedge and cup products and the unit.
2. For every field $K$, every map $u : Y \to Z$ over $K$ and opens $V \subseteq Z$, $V' \subseteq Y$ with $V' \subseteq u^{-1}(V)$ such that $u$ sends the thickenings of $V'$ to thickenings of $V$: the restriction $\mathcal{O}(V) \to \mathcal{O}(V')$ along $u$ is a $K$-algebra map, and any two compatible maps as in statement 1, for $V$ and for $V'$, commute with the pullbacks along $u$ on forms and on cohomology.

Then the conclusion of the [Theorem 2.1.4](/entry/hodge-affine-iso-sign/) holds.

Lean: `CrystallineSemistableComparison.Om.L2.hdg_aff_iso_onto`.

*Proof.* Let $X$ be smooth and affine. Then $X$ has étale coordinates on $V = X$, so statement 1 gives a bijective compatible map $\Omega^a(X) \to \mathrm{Hdg}(a, a)$, and we let $e_X$ be its inverse. Property 1 is statement 2 for $V = \top$ in $Y$ and $V' = \top$ in $X$. Property 2 holds with $\varepsilon(a, b) = 1$, since the map of statement 1 sends wedge products to cup products. Property 3 holds since it sends $1$ to $1$. $\square$

The next lemma passes from an affine scheme to an affine open of a smooth scheme. The site that computes the degree $a$ term is the site of thickenings of $V$ on which $J^{[a+1]} = 0$; on it the graded piece $J^{[a]}/J^{[a+1]}$ is $J^{[a]}$.

**Lemma 2.1.6 (Affine opens).** Let $K$ be a field of characteristic $0$. There are $K$-linear isomorphisms
$$t_V : H^a\big(J^{[a]}/J^{[a+1]}\big)_{V,\, a+1} \xrightarrow{\ \sim\ } \Omega^a(V),$$
one for each smooth $q : X \to \operatorname{Spec} K$, each affine open $V \subseteq X$ and each $a$, where the source is cohomology on the thickenings of $V$ with $J^{[a+1]} = 0$. They are natural in this sense: for smooth $X$ and $Y$ over $K$, a map $u : X \to Y$ over $K$, affine opens $V \subseteq X$ and $W \subseteq Y$ with $V \subseteq u^{-1}(W)$, and $x$ in the source for $W$, $t_V(u^* x) = (u^* t_W(x))|_V$.

Lean: `CrystallineSemistableComparison.Om.Nt2.TermAff.term_aff`.

*Proof.* The thickenings of $V$ in $X$ are the thickenings of the affine scheme $V$. We take as given that restriction to the thickenings with $J^{[a+1]} = 0$ is bijective on $H^a$ of the graded piece and commutes with pullback. Composing it with the inverse of $e_V$ from the [Theorem 2.1.4](/entry/hodge-affine-iso-sign/) defines $t_V$. For the naturality, write $x$ as the restriction of a class $z$ on $W$. Then $u^* x$ is the restriction of $u|_V^* z$, and property 1 of the theorem for the map $u|_V : V \to W$ gives $e_V(u|_V^* z) = u|_V^*(e_W z)$. The right side is $(u^* e_W z)|_V$. $\square$

**Lemma 2.1.7 (The terms of the Čech complex).** Let $K$ be a field of characteristic $0$. There are $K$-linear isomorphisms
$$t_{\alpha_0 \cdots \alpha_n} : H^a\big(J^{[a]}/J^{[a+1]}\big)_{U_{\alpha_0 \cdots \alpha_n}} \xrightarrow{\ \sim\ } \Omega^a(U_{\alpha_0 \cdots \alpha_n}),$$
one for each smooth $X$ over $K$, coordinate cover $\mathcal{U}$, $a$, $n$ and tuple $(\alpha_0, \dots, \alpha_n)$, where the source is cohomology on the thickenings with $J^{[a+1]} = 0$ that lie over $U_{\alpha_0 \cdots \alpha_n}$. They have two properties.

1. For a map $\theta : \{0, \dots, m\} \to \{0, \dots, n\}$, $t_{\alpha_0 \cdots \alpha_n}$ of the restriction of $x$ equals the restriction of $t_{\alpha_{\theta 0} \cdots \alpha_{\theta m}}(x)$ from $U_{\alpha_{\theta 0} \cdots \alpha_{\theta m}}$ to $U_{\alpha_0 \cdots \alpha_n}$.
2. Let $u : X \to Y$ be a map over $K$ with $Y$ smooth, $\mathcal{W}$ a coordinate cover of $Y$ and $\tau : I_{\mathcal{U}} \to I_{\mathcal{W}}$ a map with $U_{\alpha_0 \cdots \alpha_n} \subseteq u^{-1}(W_{\tau\alpha_0 \cdots \tau\alpha_n})$ for all tuples. If $u$ sends the thickenings of the two sites over $\mathcal{U}$ into those over $\mathcal{W}$, then $t_{\alpha_0 \cdots \alpha_n}(u^* x) = (u^* t_{\tau\alpha_0 \cdots \tau\alpha_n}(x))|_{U_{\alpha_0 \cdots \alpha_n}}$.

Lean: `GlobalTheory.CompanionTheory.OmGlobTerm.AssemblyHe1.term`.

*Proof.* Each intersection $U_{\alpha_0 \cdots \alpha_n}$ is an affine open by the definition of a coordinate cover, and the thickenings over it with $J^{[a+1]} = 0$ are the site of the [Lemma 2.1.6](/entry/term-aff/) for $V = U_{\alpha_0 \cdots \alpha_n}$. Compose the identification of the two sites with $t_V$. Property 1 is the naturality of the lemma for $u = \mathrm{id}_X$ and the inclusion $U_{\alpha_0 \cdots \alpha_n} \subseteq U_{\alpha_{\theta 0} \cdots \alpha_{\theta m}}$. Property 2 is the naturality for $u$, $V = U_{\alpha_0 \cdots \alpha_n}$ and $W = W_{\tau\alpha_0 \cdots \tau\alpha_n}$. $\square$

**Theorem 2.1.8 (Hodge cohomology by a Čech complex).** Let $K$ be a field of characteristic $0$. There are $K$-linear isomorphisms
$$e_{\mathcal{U}} : \mathrm{Hdg}(a, a + j) \xrightarrow{\ \sim\ } H^j\big(C^\bullet(\mathcal{U}, \Omega^a)\big),$$
one for each smooth $X$ over $K$, coordinate cover $\mathcal{U}$ of $X$ and $a, j \geq 0$, with this property. Let $u : X \to Y$ be a map over $K$ with $Y$ smooth, $\mathcal{W}$ a coordinate cover of $Y$ and $\tau : I_{\mathcal{U}} \to I_{\mathcal{W}}$ a map with $U_{\alpha_0 \cdots \alpha_n} \subseteq u^{-1}(W_{\tau\alpha_0 \cdots \tau\alpha_n})$ for all tuples. Let $c$ be a $j$-cocycle of $C^\bullet(\mathcal{W}, \Omega^a)$ such that the family $c'_{\alpha_0 \cdots \alpha_j} = (u^* c_{\tau\alpha_0 \cdots \tau\alpha_j})|_{U_{\alpha_0 \cdots \alpha_j}}$ is a $j$-cocycle of $C^\bullet(\mathcal{U}, \Omega^a)$. Then
$$u^*\big(e_{\mathcal{W}}^{-1}[c]\big) = e_{\mathcal{U}}^{-1}[c'].$$

Lean: `CrystallineSemistableComparison.Om.GlobPf2.glob_iso` (a second name for it is `CrystallineSemistableComparison.Om.Nt2F.glob_iso_c`).

*Proof.* We take as given the Čech degeneration on the thickening site: a natural isomorphism of $\mathrm{Hdg}(a, a + j)$ with $H^j$ of the Čech complex whose degree $n$ term is the product over tuples of the groups $H^a(J^{[a]}/J^{[a+1]})_{U_{\alpha_0 \cdots \alpha_n}}$. It holds because on each intersection the graded piece has cohomology only in degree $a$. The maps $t_{\alpha_0 \cdots \alpha_n}$ of the [Lemma 2.1.7](/entry/term/) are bijective on each term, and property 1 says that they commute with the restrictions that make up the Čech differentials. So they form an isomorphism of complexes, and it induces an isomorphism on $H^j$. Composing gives $e_{\mathcal{U}}$. For the naturality, put $c_0 = (t^{-1}_{\beta_0 \cdots \beta_j}(c_{\beta_0 \cdots \beta_j}))$, a cocycle of the first complex with image $c$. By property 2, the pullback of $c_0$ along $u$ and $\tau$ maps to $c'$. The naturality of the degeneration then gives $u^*(e_{\mathcal{W}}^{-1}[c]) = e_{\mathcal{U}}^{-1}[c']$. $\square$

The theorem asks only that $X$ is smooth. It does not ask that $X$ is proper or separated, because a coordinate cover has affine finite intersections. The last step replaces the Čech complex by sheaf cohomology. For a quasi-coherent sheaf on a noetherian separated scheme, Čech cohomology of an open affine cover computes sheaf cohomology (R. Hartshorne, *Algebraic Geometry*, Theorem III.4.5).

**Theorem 2.1.9 (Hodge cohomology on the thickening site).** Let $K$ be a field of characteristic $0$. There are $K$-linear isomorphisms
$$e_X : \mathrm{Hdg}(a, a + j) \xrightarrow{\ \sim\ } H^j(X, \Omega^a),$$
one for each smooth proper $X$ over $K$ and all $a, j \geq 0$, such that $e_X(u^* x) = u^*(e_Y(x))$ for smooth proper $X$ and $Y$ over $K$, each map $u : X \to Y$ over $K$ and each $x \in \mathrm{Hdg}_Y(a, a + j)$.

Lean: `CrystallineSemistableComparison.Om.Nt2F.hodge_iso_natural_cech`.

*Proof.* Let $X$ be smooth and proper, and fix a coordinate cover $\mathcal{U}$ of $X$. The isomorphism $e_X$ is a composite of three isomorphisms.

1. The [Theorem 2.1.8](/entry/glob-iso/) gives $\mathrm{Hdg}(a, a + j) \cong H^j(C^\bullet(\mathcal{U}, \Omega^a))$.
2. We take as given that the map from $C^\bullet(\mathcal{U}, \Omega^a)$ to the Čech complex of the sheaf $\Omega^a$ on $\mathcal{U}$ is $K$-linear and bijective on $H^j$. It holds because all finite intersections are affine, so the sections of the sheaf $\Omega^a$ over them are the Kähler forms.
3. We take as given, from Hartshorne, Theorem III.4.5, that Čech cohomology of $\Omega^a$ on $\mathcal{U}$ is $H^j(X, \Omega^a)$, compatibly with pullback.

For the naturality, let $u : X \to Y$ and let $\mathcal{W}$ be the fixed coordinate cover of $Y$. We take as given that every open cover of a smooth, separated, quasi-compact scheme is refined by a coordinate cover. Apply it to the cover of $X$ by the opens $U_\alpha \cap u^{-1}(W_\beta)$. This gives a coordinate cover $\mathcal{U}'$ of $X$, a map $\tau$ to the index set of $\mathcal{W}$ as in the [Theorem 2.1.8](/entry/glob-iso/), and a map $\sigma$ to the index set of $\mathcal{U}$ for the identity of $X$. A class of $H^j(X, \Omega^a)$ is represented by a cocycle $c$ on $\mathcal{W}$. Its pullback along $(u, \tau)$ and the restriction along $(\mathrm{id}, \sigma)$ of $e_{\mathcal{U}}$ of the same class are cocycles on $\mathcal{U}'$, and the naturality of the three isomorphisms identifies both sides of $e_X(u^* x) = u^* e_Y(x)$ with the class of the pullback of $c$ on $\mathcal{U}'$. The case $u = \mathrm{id}$ uses that $\mathrm{id}^*$ is the identity on $\mathrm{Hdg}$ and on $H^j(X, \Omega^a)$. $\square$

**Remark 2.1.10 (Formalization).** The site of thickenings is used only through the operations of the first definition. In the affine theorem the sign is $\varepsilon(a, b) = 1$ ([AsmOnto.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/AffineHodgeIsomorphisms/AsmOnto.lean#L38)). The last theorem is the type of the hypothesis of `CrystallineSemistableComparison.Om.hdg_iso` ([HdgAffIso.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/DifferentialFormsCech/HdgAffIso.lean#L13)), which returns that hypothesis; the file name does not match its content, which is about proper schemes. The inputs taken as given (the degeneration, the comparison of Čech complexes, the Leray comparison, the refinement of covers and the restriction to the truncated site) enter as statements whose proofs we did not open.
