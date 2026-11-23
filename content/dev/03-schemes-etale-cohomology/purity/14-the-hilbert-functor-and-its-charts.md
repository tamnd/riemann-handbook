---
title: The Hilbert functor and its charts
decls:
  - GlobalTheory.HilbAff.functor
  - GlobalTheory.HilbertSch.IsHilbRep
  - GlobalTheory.hilbChart_representable
  - GlobalTheory.T.affineHilbertChart_representable
  - GlobalTheory.T.exists_open_affineHilbertChartBasic_locus
  - GlobalTheory.T.exists_affineHilbertChartBasic_neighbourhood
  - GlobalTheory.T.affineHilbertSchemeFunctor_isSheaf_zariski
  - GlobalTheory.GeneratorFunctor.isRepresentable_of_charts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hilbert functor and its charts

This section starts the last part of the chapter, sections 14 to 16. This part does not use étale cohomology. It constructs the Hilbert scheme of points of a finite flat morphism: a proper scheme $H$ that classifies the closed subschemes that are finite and flat of a fixed rank $r$. The chapter on clopen subschemes uses it in [Theorem 6.1.7](/entry/exists-clop-rep-of-rank-of-locally-noetherian/) to classify the clopen subschemes of rank $r$ of a finite étale cover. This section defines the Hilbert functor of $\operatorname{Spec} B \to \operatorname{Spec} A$, for $B$ free of finite rank over $A$, and covers it by affine charts, one for each choice of $r$ basis vectors of $B$. Section 15 deduces that the functor is represented by a proper scheme, and section 16 glues the affine case.

All rings are commutative. We use the language of [schemes](/learn/geometry/#schemes-and-varieties) and of [flat algebras](/learn/commutative-algebra/#flat-and-tale-algebras). For a morphism $g : T \to \operatorname{Spec} A$ we write $Z_T = \operatorname{Spec} B \times_{\operatorname{Spec} A} T$ and $p_T : Z_T \to T$ for the projection. For $a : T' \to T$ we write $a_Z : Z_{T'} \to Z_T$ for the base change of $a$.

**Definition 2.14.1 (Rank of a finite flat morphism).** Let $f : V \to T$ be a [[finite|N9C4X7XKE4]] and [[flat|5M6KS8F47R]] morphism and let $t \in T$. Choose an affine open $\operatorname{Spec} R \subseteq T$ that contains $t$, let $\mathfrak{p} \subseteq R$ be the prime of $t$, and write $f^{-1}(\operatorname{Spec} R) = \operatorname{Spec} M$. Then $M_{\mathfrak{p}}$ is a finite flat module over the local ring $R_{\mathfrak{p}}$, so it is free (H. Matsumura, *Commutative Ring Theory*, Theorem 7.10). Its rank is the *rank of $f$ at $t$*, written $\operatorname{rk}_t(f)$. The morphism $f$ has *rank $r$* if $\operatorname{rk}_t(f) = r$ for all $t \in T$.

The rank does not change under base change: if $a : T' \to T$ and $f' : V \times_T T' \to T'$ is the base change, then $\operatorname{rk}_{t'}(f') = \operatorname{rk}_{a(t')}(f)$. For a finite flat morphism of finite presentation, this is the rank of the locally free sheaf $f_*\mathcal{O}_V$.

**Definition 2.14.2 (Hilbert functor).** Let $A \to B$ be a ring map and $r \geq 0$. For a scheme $T$ let $\operatorname{Hilb}^r(T)$ be the set of pairs $(g, V)$ where $g : T \to \operatorname{Spec} A$ is a morphism and $V \subseteq Z_T$ is a [[closed subscheme|N3PGYJJQ7W]] such that $p_T|_V : V \to T$ is finite, flat and of rank $r$. For $a : T' \to T$ put $a^*(g, V) = (g \circ a, a_Z^{-1}(V))$, where $a_Z^{-1}(V) = V \times_{Z_T} Z_{T'}$ is the inverse image. This makes $\operatorname{Hilb}^r$ a contravariant functor from schemes to sets.

Lean: `GlobalTheory.HilbAff.functor`, `GlobalTheory.HilbAff.Good`.

The inverse image $a_Z^{-1}(V)$ is the base change of $V \to T$ along $a$, so it is again finite and flat of rank $r$. A pair $(g, V)$ is a family of closed subschemes of the fibres of $\operatorname{Spec} B$, of length $r$, parametrised by $T$. So $\operatorname{Hilb}^r$ is the functor of points of the Hilbert scheme of $r$ points, written over the base $\operatorname{Spec} A$.

**Definition 2.14.3 (Hilbert scheme).** Let $z : Z \to S$ be a morphism of schemes and $r \geq 0$. A *Hilbert scheme of rank $r$* for $z$ is a triple $(H, h, u)$ of a scheme $H$, a [[proper|9537RKBZPP]] morphism $h : H \to S$, and a [[closed immersion|WWRWYSJDET]] $u : U \to Z \times_S H$, such that $U \to H$ is finite, flat and of rank $r$, with the following property. Let $T$ be a scheme, $g : T \to S$ a morphism and $v : V \to Z \times_S T$ a closed immersion such that $V \to T$ is finite, flat and of rank $r$. Then there is exactly one $f : T \to H$ with $h \circ f = g$ such that $V$ is the inverse image of $U$: there is $w : V \to U$ for which the square
$$
\begin{array}{ccc}
V & \xrightarrow{\;w\;} & U \\
{\scriptstyle v}\downarrow & & \downarrow{\scriptstyle u} \\
Z \times_S T & \xrightarrow{\;1 \times f\;} & Z \times_S H
\end{array}
$$
is cartesian. We say that $z$ *has a Hilbert scheme of rank $r$*.

Lean: `GlobalTheory.HilbertSch.IsHilbRep`.

**Example 2.14.4.** Let $B = A[x]/(x^2)$ and $r = 1$. Over an affine $T = \operatorname{Spec} A'$, a closed subscheme of $\operatorname{Spec} A'[x]/(x^2)$ that is finite flat of rank $1$ over $A'$ is the kernel of a surjection $A'[x]/(x^2) \to A'$ of $A'$-algebras. Such a map sends $x$ to an element $c$ with $c^2 = 0$. So $\operatorname{Hilb}^1(\operatorname{Spec} A') = \{ c \in A' : c^2 = 0 \}$, and the Hilbert scheme is $\operatorname{Spec} A[c]/(c^2)$. It is finite over $A$ but not reduced.

### Charts

From now on $B$ is free of rank $N$ as an $A$-module, with basis $e_1, \dots, e_N$. Write $\bar e_j$ for the image of $1 \otimes e_j$ in the ring of functions of a closed subscheme of $Z_T$.

**Definition 2.14.5 (Basic pairs).** Let $\sigma : \{1, \dots, r\} \to \{1, \dots, N\}$ be injective. A pair $(g, V) \in \operatorname{Hilb}^r(T)$ is *$\sigma$-basic* if for every affine open $U \subseteq T$ the map
$$
\Gamma(U, \mathcal{O}_T)^r \longrightarrow \Gamma(p_T^{-1}(U) \cap V, \mathcal{O}_V), \qquad c \longmapsto \sum_{k=1}^r c_k \, \bar e_{\sigma(k)},
$$
is bijective. So the sections $\bar e_{\sigma(1)}, \dots, \bar e_{\sigma(r)}$ form a basis of $(p_T|_V)_* \mathcal{O}_V$ over each affine open.

Lean: `GlobalTheory.HilbAff.Basic`.

**Lemma 2.14.6 (The chart ring).** Let $\sigma$ be as above. There are a finitely presented $A$-algebra $C$ and an ideal $J \subseteq C \otimes_A B$ such that the images of $1 \otimes e_{\sigma(k)}$, $k = 1, \dots, r$, form a basis of $(C \otimes_A B)/J$ over $C$, with the following property. For each $A$-algebra $A'$ and each ideal $J' \subseteq A' \otimes_A B$ such that the images of $1 \otimes e_{\sigma(k)}$ form a basis of $(A' \otimes_A B)/J'$ over $A'$, there is exactly one $A$-algebra map $\varphi : C \to A'$ such that $J'$ is the ideal generated by the image of $J$ under $\varphi \otimes 1$.

Lean: `GlobalTheory.hilbChart_representable`.

*Proof.* Write $e_a e_m = \sum_b s_{a m b} e_b$ with $s_{a m b} \in A$. Let $C$ be the quotient of $A[c_{m k} : 1 \leq m \leq N, 1 \leq k \leq r]$ by the relations
$$
\begin{aligned}
c_{\sigma(k) k'} &= \delta_{k k'}, \\
\sum_b s_{a m b} \, c_{b k} &= \sum_{k'} c_{m k'} \sum_b s_{a \sigma(k') b} \, c_{b k} \quad \text{for all } a, m, k,
\end{aligned}
$$
and let $J$ be generated by the elements $\ell_m = 1 \otimes e_m - \sum_k c_{m k} (1 \otimes e_{\sigma(k)})$. The idea is that $c_{m k}$ is the $k$-th coordinate of $\bar e_m$ in the basis $\bar e_{\sigma(1)}, \dots, \bar e_{\sigma(r)}$. The first relations say that $\bar e_{\sigma(k)}$ has the $k$-th unit vector as coordinates. The second relations say that the coordinates of $\bar e_a \bar e_m$ are the same whether we expand $e_a e_m$ in $B$ first or replace $\bar e_m$ by its expansion first. Let $\kappa : C \otimes_A B \to C^r$ be the $C$-linear map with $\kappa(1 \otimes e_m) = (c_{m k})_k$. Every $y$ is a combination of the $\ell_m$ plus $\sum_k \kappa(y)_k (1 \otimes e_{\sigma(k)})$, and $\kappa(\ell_m) = 0$ by the first relations. The second relations say $\kappa((1 \otimes e_a) \ell_m) = 0$, so $\ker \kappa$ is an ideal, and it equals $J$. Hence $\kappa$ induces an isomorphism $(C \otimes_A B)/J \cong C^r$ that sends the image of $1 \otimes e_{\sigma(k)}$ to the $k$-th unit vector. The ring $C$ is finitely presented, with finitely many variables and relations. For $J'$ as in the statement, the coordinates of the images of $1 \otimes e_m$ in the basis satisfy the two relations, so they define $\varphi$, and the ideal generated by the image of $J$ is contained in $J'$. Both quotients have the same basis, so the two ideals are equal. Conversely, any $\varphi$ with this property sends $c_{m k}$ to the coordinates of the image of $1 \otimes e_m$, because $\varphi(\ell_m) \in J'$. So $\varphi$ is unique. $\square$

**Lemma 2.14.7 (Charts).** For each injective $\sigma$ there are an affine scheme $X_\sigma$ and a $\sigma$-basic pair $\xi_\sigma = (g_\sigma, V_\sigma) \in \operatorname{Hilb}^r(X_\sigma)$ with $g_\sigma$ locally of finite type, such that for every scheme $T$ and every $\sigma$-basic $y \in \operatorname{Hilb}^r(T)$ there is exactly one $f : T \to X_\sigma$ with $f^* \xi_\sigma = y$.

Lean: `GlobalTheory.T.affineHilbertChart_representable` (also `GlobalTheory.HilbAff.chart_represents`).

*Proof.* Take $X_\sigma = \operatorname{Spec} C$ and $V_\sigma$ the closed subscheme defined by $J$, with $C$ and $J$ from the Lemma on the chart ring. Then $V_\sigma \to X_\sigma$ is finite and free of rank $r$, and $\xi_\sigma$ is $\sigma$-basic. For $T$ affine, a $\sigma$-basic pair over $T$ is an ideal $J'$ as in that Lemma, so the Lemma gives exactly one $f$. For a general $T$, the maps on the affine opens of $T$ agree on overlaps by uniqueness, so they glue to one map $f$. $\square$

**Lemma 2.14.8 (The basic locus).** Let $y \in \operatorname{Hilb}^r(T)$ and let $\sigma$ be injective. There is an open $W \subseteq T$ such that a morphism $a : T' \to T$ has image in $W$ if and only if $a^* y$ is $\sigma$-basic. If $T$ is quasi-compact, then $W$ is quasi-compact.

Lean: `GlobalTheory.T.exists_open_affineHilbertChartBasic_locus` (also `GlobalTheory.HilbAff.Locus.exists_basic_locus`).

*Proof.* Let $U = \operatorname{Spec} R$ be an affine open of $T$ and $M = \Gamma(p_T^{-1}(U) \cap V, \mathcal{O}_V)$, a finite flat $R$-module of rank $r$ at every prime. Let $Q$ be the cokernel of $\lambda : R^r \to M$, $c \mapsto \sum_k c_k \bar e_{\sigma(k)}$. Its support is closed, since $Q$ is finite. Outside the support, $\lambda$ is a surjection onto a free module of rank $r$, so it is bijective. Hence $\lambda$ is bijective if and only if $Q = 0$, and $W \cap U$ is the complement of the support of $Q$. The cokernel commutes with base change, and by Nakayama's lemma a point of $T'$ lies outside the support of the pulled back cokernel exactly when its image lies outside the support of $Q$. This gives the property of $W$. $\square$

**Lemma 2.14.9 (Basic neighbourhoods).** Let $y \in \operatorname{Hilb}^r(T)$ and $t \in T$. There are an injective $\sigma$ and an open $U \ni t$ such that $y|_U$ is $\sigma$-basic.

Lean: `GlobalTheory.T.exists_affineHilbertChartBasic_neighbourhood` (also `GlobalTheory.HilbAff.exists_basic_nhd`).

*Proof.* Take an affine open $\operatorname{Spec} R \ni t$ with prime $\mathfrak{p}$, and $M$ as in the last proof. Since $V$ is a closed subscheme of $Z_T$, the elements $\bar e_1, \dots, \bar e_N$ generate $M$ over $R$. The module $M_{\mathfrak{p}}$ is free of rank $r$, so $r$ of the $\bar e_j$ form a basis of $M_{\mathfrak{p}} / \mathfrak{p} M_{\mathfrak{p}}$. Let $\sigma$ list them. By Nakayama's lemma they generate $M_{\mathfrak{p}}$, so the cokernel of the last proof vanishes at $\mathfrak{p}$. It then vanishes on a basic open $D(f) \ni t$, and $D(f)$ lies in the basic locus. $\square$

**Lemma 2.14.10 (Sheaf property).** The functor $\operatorname{Hilb}^r$ is a sheaf for the Zariski topology.

Lean: `GlobalTheory.T.affineHilbertSchemeFunctor_isSheaf_zariski` (also `GlobalTheory.HilbAff.isSheaf_functor`).

*Proof.* Morphisms to $\operatorname{Spec} A$ glue along an open cover, and so do closed subschemes. The conditions finite, flat and of rank $r$ are local on the base. $\square$

**Lemma 2.14.11 (Representability by open charts).** Let $F$ be a Zariski sheaf on schemes. Let $(X_j, x_j)_{j \in I}$ be a family of schemes with $x_j \in F(X_j)$. For each scheme $T$, each $y \in F(T)$ and each $j$, let $W_j(y) \subseteq T$ be an open. Assume:

1. a morphism $a : T' \to T$ has image in $W_j(y)$ if and only if $a^* y = g^* x_j$ for some $g : T' \to X_j$;
2. for $g, g' : T \to X_j$, $g^* x_j = g'^* x_j$ implies $g = g'$;
3. for each $T$ and $y$, the opens $W_j(y)$ cover $T$.

Then $F$ is [[representable|KCCHH87H6E]].

Lean: `GlobalTheory.GeneratorFunctor.isRepresentable_of_charts`.

*Proof.* Conditions 1 and 2 say that the map from the functor of points of $X_j$ to $F$ given by $x_j$ is injective and an open immersion: its pullback along any $y : T \to F$ is the open $W_j(y)$. Condition 3 says that these open subfunctors cover $F$. A Zariski sheaf covered by open subfunctors that are representable is represented by the scheme obtained by gluing the $X_j$ along the opens $W_l(x_j) \subseteq X_j$. $\square$

**Remark 2.14.12 (Formalization).** The rank is `AlgebraicGeometry.Scheme.Hom.finrank` from Mathlib, which is defined through the rank of the localization at a prime on an affine open. A closed subscheme is a sheaf of ideals (`Scheme.IdealSheafData`). The Hilbert functor is defined in [ComapBcComp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComapBcComp.lean#L77), whose name does not describe it; it is a functor on all schemes, and a point carries its map to $\operatorname{Spec} A$. The Lemma on representability by open charts is in [InverseBundleGeneratorPointOfChartUnitsSections.lean](lean:Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/InverseBundleGeneratorPointOfChartUnitsSections.lean#L21), a module on abelian schemes whose name says nothing about it. The charts are indexed by injective maps $\sigma$, not by subsets of $\{1, \dots, N\}$, so each subset of size $r$ gives $r!$ isomorphic charts. This does no harm.
