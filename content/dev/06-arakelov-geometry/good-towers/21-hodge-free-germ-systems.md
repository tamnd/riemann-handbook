---
title: Hodge free germ systems
decls:
  - GlobalTheory.T.germ_system_height_free
  - GlobalTheory.CompanionTheory.Ar.Flat.hfree_at_component_stalks
  - GlobalTheory.T.height_char_free_geometric
  - GlobalTheory.CompanionTheory.Ar.Flat.hfree_geom
  - GlobalTheory.T.abelian_quotient_bilinear
  - GlobalTheory.CompanionTheory.Ar.Flat.FrGauge.frame_gauge
  - GlobalTheory.T.proper_multiplication_kernel
  - GlobalTheory.CompanionTheory.Ar.Flat.lemF_ker_order_dvd
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Hodge free germ systems

To compute the finite norms of a frame function on the whole model, and not only at CM points, we need that the de Rham module of the semi-abelian scheme is free over $k \otimes \mathcal{O}_E$ at every point of a component, also at points of positive residue characteristic. This section proves it. The condition at the generic point is that the characteristic polynomial of $\mathcal{O}_E$ has the right form; the result says that this condition spreads to all specializations. In characteristic $p$ the proof counts the order of the kernel of multiplication by $a \in \mathcal{O}_E$ in two ways. The result is the input that the [covolume statement](/entry/top-covol-slim2-use-alt-alt/) uses through the [Hodge freeness at every stalk](/entry/hodge-free-every-stalk/).

Let $E$ be a CM field with host $H$, and give $\mathcal{O}_E$ the involution of complex conjugation. Let $X$ be a scheme and $t$ a semi-abelian scheme over $X$ with an action of $\mathcal{O}_E$ and with power functions, so that $t$ is a quotient of a power of a torus by a lattice near each boundary point. Let $\Omega$ be a field of characteristic $0$ and $\xi: \mathrm{Sp}\,\Omega \to X$ a component generic point.

### Germs and the two conditions

A germ of $t$ at a point $x$ is a formal group law of dimension $d$ at $x$, with the action of $\mathcal{O}_E$ by matrices $\rho(a)$ on the Lie algebra, and with the bilinear term $A(a)$ of the action in degree two. On $k^d \times k^d$ the Hodge action of $a$ is
$$
\rho_H(a)(y_1, y_2) = \bigl( \rho(a) y_1, \ \rho(\bar a)^{T} y_2 - A(a)^{T} y_1 \bigr) .
$$
This is the action of $a$ on the first de Rham module, written in the coordinates of the germ: the Lie algebra and the dual of the Lie algebra of the dual, with the extension class $A$.

**Definition 8.21.1 (Hodge character and Hodge freeness).** Let $B$ be the de Rham module of a germ, with the Hodge action. For $r \ge 1$ the germ has Hodge character $r$ if for every $a \in \mathcal{O}_E$
$$
\det \bigl( T - \rho_H(a) \bigr) = P_a(T)^r ,
$$
where $P_a$ is the characteristic polynomial of $a$ on $E$ over $\mathbb{Q}$. The germ is Hodge free of rank $r$ if $B$ is free of rank $r$ over $k \otimes \mathcal{O}_E$.

A free module of rank $r$ has the Hodge character $r$. The converse is false in general in characteristic $p$, and it is what we prove under a condition on the fibres.

A germ system for $\xi$ is a germ $g_0$ at the generic point and a germ $g_q$ at every specialization $q$ of $\xi$, compatible with the specialization maps.

### The result on germ systems

**Theorem 8.21.2 (Hodge freeness on germ systems).** Let $S$ be a germ system for $\xi$. Assume that $g_0$ has Hodge character $r$, and that $t$ has a principal fibre at every specialization of positive residue characteristic. Then $g_q$ is Hodge free of rank $r$ at every specialization $q$ of $\xi$.

Lean: `GlobalTheory.T.germ_system_height_free` (also `GlobalTheory.CompanionTheory.Ar.Flat.hfree_at_component_stalks`, a second name).

*Proof.* The Hodge character is invariant under isomorphism and under base change of the germ, so $g_q$ has Hodge character $r$ for every $q$. Then we use the [result at a point](/entry/at-point/). If the residue characteristic of $q$ is $0$, the Hodge character gives freeness, since $k \otimes \mathcal{O}_E$ is a product of fields and the multiplicity of each eigenvalue is read from the characteristic polynomial. If the residue characteristic is $p > 0$, we base change the formal germ to an algebraic closure of the residue field, apply the theorem below, and descend the freeness along the base change. $\square$

### The geometric case

**Theorem 8.21.3 (Hodge freeness at a geometric point).** Let $k$ be an algebraically closed field of characteristic $p$, let $x: \mathrm{Sp}\,k \to X$ be a point at which $t$ has a principal fibre, and let $g$ be a germ of $t$ at $x$ of dimension $d$. If $g$ has Hodge character $r$, then $g$ is Hodge free of rank $r$.

Lean: `GlobalTheory.T.height_char_free_geometric` (also `GlobalTheory.CompanionTheory.Ar.Flat.hfree_geom`, a second name).

The proof is at the end of the section. It uses two lemmas.

**Lemma 8.21.4 (Gauge of an abelian quotient).** Let $Q$ be an abelian quotient of $t$ at $x$, so that there is an exact sequence $0 \to T \to t_x \to B \to 0$ with a torus $T$ and an abelian variety $B$. Let $g$ be a germ of $t$ and $g_B$ a germ of $B$, and let $P$ be the differential of the quotient map in these coordinates. Then there is a matrix $Z$ with
$$
A(a) + \rho(a)^{T} Z - Z \rho(\bar a) = P^{T} A_B(a) P
$$
for every $a \in \mathcal{O}_E$, where $A$ and $A_B$ are the bilinear terms of $g$ and $g_B$.

Lean: `GlobalTheory.T.abelian_quotient_bilinear` (also `GlobalTheory.CompanionTheory.Ar.Flat.FrGauge.frame_gauge`, a second name).

*Proof.* Write the quotient map as a power series in the coordinates of the two germs. Its linear term is $P$. The quotient map is a homomorphism, so it commutes with the action of $a$ and with the group laws. The theta line bundle on $B$ pulls back to a line bundle on $t_x$ whose germ differs from the germ of the polarization of $t$ by a gauge transformation, given by a unit power series. This unit is trivial on both axes, and its quadratic term is $Z$. Compare the bilinear terms of the two sides of the relation in degree two; the substitution rule for bilinear forms and the product rule for the bilinear terms give the identity. $\square$

**Lemma 8.21.5 (Order of a multiplication kernel).** Let $t$ be a proper group scheme over $k$ with trivial outer part, let $g$ be a germ at the origin, let $a \in \mathcal{O}_E$, and let $A$ be a finite $k$-algebra with a map $\mathrm{Sp}\,A \to t$ that is the kernel of multiplication by $a$. Then
$$
p^{\dim \ker \rho_H(a)} \ \text{divides} \ \dim_k A .
$$

Lean: `GlobalTheory.T.proper_multiplication_kernel` (also `GlobalTheory.CompanionTheory.Ar.Flat.lemF_ker_order_dvd`, a second name).

*Proof.* The kernel of $a$ on a proper group germ is a finite subscheme, and its connected part is a finite infinitesimal group scheme whose order is a power of $p$. The tangent space of the kernel contains the kernel of $\rho(a)$ on the Lie algebra. The primitive derivations of the kernel pair with the kernel of $\rho_H(a)$ on the de Rham module, and the pairing is perfect on its image. So the order of the connected part is at least $p^{\dim \ker \rho_H(a)}$. The bound on the kernel gives
$$
\dim \ker \rho_H(a) \le \dim \ker \rho(\bar a) + \dim W ,
$$
where $W$ is the space of the extension class, and both summands are realized in the kernel. The order of a finite group scheme is the product of the orders of its connected and étale parts, so the power of $p$ divides $\dim_k A$. $\square$

### Proof of the geometric case

By the power functions, $t_x$ has an abelian quotient: an exact sequence $0 \to T \to t_x \to B \to 0$. Take a formal germ of $t$ at $x$, the lattice of the quotient, and the gauge $Z$ of the first lemma. Then $\rho_H(a)$ is conjugate to a block matrix whose blocks are the action on the torus part, its dual, and the Hodge action of $B$. The rank of the kernel of the gauge is computed from the blocks.

Fix $a \in \mathcal{O}_E$ with $a \ne 0$. The kernel $B[a]$ of multiplication by $a$ on $B$ is finite of order $m$, with
$$
m^{[E:\mathbb{Q}]} = |N a|^{2 d'} ,
$$
where $d'$ is the dimension of $B$ and $N$ is the norm from $E$ to $\mathbb{Q}$. The second lemma, applied to $B$, says that $p^{\dim \ker \rho_H^B(a)}$ divides $m$. Together with the blocks for the torus part, this gives
$$
\dim \ker \rho_H(a) \le r \, v_p(N a) .
$$
This is the bound that a free module of rank $r$ over $k \otimes \mathcal{O}_E$ would have, with equality.

Now $k \otimes \mathcal{O}_E$ is a product of local Artinian rings $R_\mathfrak{p}$, one for each prime $\mathfrak{p}$ over $p$, and $B = \prod_\mathfrak{p} B_\mathfrak{p}$. The Hodge character fixes the length of each $B_\mathfrak{p}$ to be $r$ times the length of $R_\mathfrak{p}$. A module of this length over $R_\mathfrak{p}$ is free of rank $r$ if and only if the kernel of a uniformizer has dimension at most $r$ times the residue degree. Choose $a$ that is a uniformizer at $\mathfrak{p}$ and a unit at the other primes over $p$; the bound gives exactly this. So each $B_\mathfrak{p}$ is free of rank $r$, and a free basis can be chosen compatible with the hermitian pairing of the formal action. $\square$

So the Hodge character, which is a condition on characteristic polynomials and can be checked at the generic point, gives freeness at every point of the component, once the fibres in positive characteristic are principal.

**Remark 8.21.6 (Formalization).** The two names with `height` (`germ_system_height_free`, `height_char_free_geometric`) speak of a height, but no height appears; the properties are `HChar` and `HFree` (GermSys.lean:19 and 47), the Hodge character and Hodge freeness. The result on germ systems `hfree_at_component_stalks` (GermSystemHeightFree.lean:19) is a one-term second name of `PositivityTheory.Xgn.hodge_free_every_stalk` (HodgeFreeEveryStalk.lean:178), and its file imports statement forms that the proof does not use. In HeightCharFreeGeometric.lean the rank of the kernel of the gauge is `finrank_ker_gauge` (line 76), the bound on kernels is `ker_bound` (line 95), and the numerical step $\dim \ker \rho_H(a) \le r v_p(N a)$ is `numeric` (line 199). The bound $\dim \ker \rho_H(a) \le \dim \ker \rho(\bar a) + \dim W$ is `finrank_ker_rhoH_le` (ProperMultiplicationKernel.lean:46) with the space `KerBd.Wd` (line 17). The `T.*` names are renamings proved by `first | exact @...`. We do not unfold the power functions, the formal group laws or the gauge transformations.
