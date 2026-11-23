---
title: Characteristic polynomials on de Rham homology
decls:
  - GlobalTheory.Dieu.AbsDet.norm_det_eq_norm_deg
  - GlobalTheory.Dieu.CharpolyAV.charpoly_map_eq
  - GlobalTheory.DeRhamCharpolyP.charpoly_push
  - GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charP
  - GlobalTheory.DeRham.charpoly_push_eq_map_charpoly
  - GlobalTheory.DeRham.charpoly_push_eq
  - GlobalTheory.T.charpoly_deRhamHomology_endomorphism_eq_map_ladic
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Characteristic polynomials on de Rham homology

Let $f$ be an endomorphism of an abelian variety $A$ over a field $k$. This section shows that the characteristic polynomial of $f$ acting on the de Rham homology of $A$ is the image in $k[x]$ of the integer characteristic polynomial of $f$, when $k$ is perfect of characteristic $p$ or algebraically closed. In characteristic $p$ we compare de Rham homology with the Dieudonné module of [the previous section](/entry/theory/), and we compute the characteristic polynomial on the Dieudonné module through determinants and degrees. The case of characteristic $0$ is quoted. We end with a form in which the integer polynomial is read off from an $\ell$-adic lattice; this form is used in [the Kodaira-Spencer map of weight one](/entry/kodaira-spencer-of-weight-one/).

### Degrees and torsion towers

An *abelian variety* over $k$ is an [abelian scheme|JDDXZ89N33] $A$ over $\operatorname{Spec} k$ with an integer $g$ such that $A$ is [smooth|EXKGG9X6J0] of relative dimension $g$. A homomorphism $f : A \to B$ is an *isogeny* if it is [finite|N9C4X7XKE4] and surjective. The *degree* $\deg f$ is the rank of $f$ at the origin of $B$ if $f$ is an isogeny, and $0$ otherwise.

**Definition 8.26.1 (Characteristic polynomial).** Let $f$ be an endomorphism of $A$. A polynomial $P \in \mathbb{Z}[x]$ is a *characteristic polynomial* of $f$ if it is monic of degree $2g$ and $P(n) = \deg(n - f)$ for every integer $n$. The polynomial $\operatorname{charpoly}(f)$ is a chosen such $P$ if one exists, and $0$ otherwise.

Lean: `GlobalTheory.AV.AbVar.IsCharpoly`, `GlobalTheory.AV.AbVar.charpoly`.

**Definition 8.26.2 (Torsion tower).** Let $G$ be a $p$-divisible group over $k$, with Hopf algebras $A_n(G)$ as in the previous section. A *torsion tower* $t$ for $A$ with group $G$ is a family of homomorphisms $y_n : \operatorname{Spec} A_n(G) \to A$, compatible with the maps $A_{n+1}(G) \to A_n(G)$, such that for every $k$-algebra $C$ the map $y_n$ is injective on $C$-points and its image is the set of $C$-points of $A$ killed by $p^n$. A homomorphism $f : A \to B$ and towers $t$ for $A$ and $t'$ for $B$ give a morphism $t(f) : G \to H$ of $p$-divisible groups.

Lean: `GlobalTheory.PDivGroup.TorsionTower`, `GlobalTheory.PDivGroup.TorsionTower.map`.

Fix a Dieudonné theory $T$ with modules $M(G)$ over $W = W(k)$. For an endomorphism $f$ of $A$ and a tower $t$ we write
$$f_D = t(f)^* : M(G) \to M(G)$$
for the $W$-linear map that the theory gives. Let $\psi : \mathbb{Z}_p \to W$ be a ring map, and write $\lVert \cdot \rVert$ for the $p$-adic norm on $\mathbb{Z}_p$.

### Determinants and degrees

**Theorem 8.26.3 (Determinant and degree).** Let $A$ be an abelian variety over $k$, $t$ a torsion tower for $A$ with group $G$, $f$ an endomorphism of $A$ and $d \in \mathbb{Z}_p$ with $\det f_D = \psi(d)$. Then $\lVert d \rVert = \lVert \deg f \rVert$.

Lean: `GlobalTheory.Dieu.AbsDet.norm_det_eq_norm_deg`.

We use the following results.

### Inputs

1. Let $N$ be a free $W$-module of finite rank and $u$ an endomorphism with $\det u = \psi(d)$. If $N / u(N)$ has length $e$, then $\lVert d \rVert = p^{-e}$; if $u$ is not injective, then $d = 0$. (`GlobalTheory.T.wittVector_colength_range_eq_det_valuation`)
2. If $f$ is an isogeny, then $M(G) / f_D(M(G))$ has length $v_p(\deg f)$. (`GlobalTheory.T.abelianVariety_dieudonne_integrality_factorisation`)
3. If $f$ is an isogeny, then $\deg f > 0$. (`GlobalTheory.AV.AbVar.isogeny_flat_finrank`)
4. If $t(g) = 0$ then $g = 0$, and if $h^* = 0$ for a morphism $h$ of $p$-divisible groups then $h = 0$. (`GlobalTheory.T.eq_pow_smul_of_pDivGroup_torsionTower_map`, `GlobalTheory.T.dieudonne_integrality_and_faithful`)
5. The maps $h^*$ satisfy $(h \circ h')^* = h'^* \circ h^*$ and $0^* = 0$, and $t$ respects composition. (`GlobalTheory.T.dieudonneFunctorBase_functor_properties`, `GlobalTheory.PDivGroup.TorsionTower.map_comp`)

*Proof.* If $f$ is an isogeny, results 1 and 2 give $\lVert d \rVert = p^{-v_p(\deg f)}$, which is $\lVert \deg f \rVert$ since $\deg f > 0$ by result 3. If $f$ is not an isogeny, then $\deg f = 0$, and we show that $f_D$ is not injective, so that $d = 0$ by result 1. The element of $\operatorname{End}(A) \otimes \mathbb{Q}$ given by $f$ is not a unit, since a unit would make some $g \circ f$ equal to $n \cdot \mathrm{id}$ with $n \neq 0$, and then $f$ would be an isogeny. In a finite dimensional $\mathbb{Q}$-algebra a nonunit is a zero divisor, so there is $g \neq 0$ with $g \circ f = 0$. By result 5, $f_D \circ g_D = (g \circ f)_D = 0$, and $g_D \neq 0$ by result 4. A vector $m$ with $g_D(m) \neq 0$ shows that $f_D$ is not injective. $\square$

### Characteristic polynomials on the Dieudonné module

**Theorem 8.26.4 (Characteristic polynomial on the Dieudonné module).** Let $A$ be an abelian variety over $k$, $t$ a torsion tower for $A$ with group $G$, and suppose that $M(G)$ is free and finite. Then for every endomorphism $f$ of $A$,
$$\operatorname{charpoly}(f_D) = \operatorname{charpoly}(f) \text{ mapped to } W[x].$$

Lean: `GlobalTheory.Dieu.CharpolyAV.charpoly_map_eq`.

We use the following results, together with the theorem on determinants and degrees.

### Inputs

1. The Frobenius $F$ of $M(G)$ is injective, $f_D$ commutes with $F$, and $M(G)$ has rank equal to the height of $G$, which is $2g$. (`GlobalTheory.T.dieudonneTheory_V_eq_verschiebung_injective`, `GlobalTheory.T.dieudonneFunctorBase_functor_properties`, `GlobalTheory.T.exists_torsionTower_and_height_eq_two_dim`)
2. If an endomorphism $u$ of a free $W$-module of finite rank commutes with an injective Frobenius-semilinear map, there is a monic $P \in \mathbb{Z}_p[x]$ with $\psi(P) = \operatorname{charpoly}(u)$. (`GlobalTheory.T.exists_padicInt_charpoly_commute_frobeniusSemilinear`)
3. $\operatorname{charpoly}(f)$ is a characteristic polynomial of $f$, and it is the only one. (`GlobalTheory.T.abelianVarietyEndCharpoly_spec`)
4. Two monic polynomials $P$ and $Q$ over $\mathbb{Q}_p$ of the same degree are equal if, for every $R \in \mathbb{Z}[x]$, the products of $R(\alpha)$ over the roots $\alpha$ of $P$ and of $Q$ in an algebraic closure have the same norm. (`GlobalTheory.T.eq_of_norm_prod_aeval_eq'`)
5. If $\psi$ is injective, $\psi(P) = \operatorname{charpoly}(u)$ and $\det R(u) = \psi(d)$, then the product of $R(\alpha)$ over the roots of $P$ is $d$. (`GlobalTheory.T.prod_aeval_padicRoots_charpoly_eq_det`)
6. For $R \in \mathbb{Z}[x]$, $\deg R(f)$ is the product of $R(\alpha)$ over the roots $\alpha$ of $\operatorname{charpoly}(f)$ in an algebraically closed field of characteristic $0$. (`GlobalTheory.T.deg_aeval_end_eq_prod_aroots`)

*Proof.* Let $\psi$ be the map $\mathbb{Z}_p = W(\mathbb{F}_p) \to W(k)$; it is injective, since $\psi(p^v u) = p^v \psi(u)$ with $\psi(u)$ a unit and $p$ not a zero divisor in $W$. By results 1 and 2 there is a monic $P$ over $\mathbb{Z}_p$ with $\psi(P) = \operatorname{charpoly}(f_D)$, of degree $2g$; by result 3, $\operatorname{charpoly}(f)$ is monic of degree $2g$ too. Let $R \in \mathbb{Z}[x]$. Result 2 for $R(f)$ gives $d$ with $\det R(f)_D = \psi(d)$, and $R(f)_D = R(f_D)$ since $f \mapsto f_D$ respects sums and products. By result 5 the product of $R(\alpha)$ over the roots of $P$ is $d$, whose norm is $\lVert \deg R(f) \rVert$ by the theorem on determinants and degrees. By result 6 this is the norm of the product of $R(\alpha)$ over the roots of $\operatorname{charpoly}(f)$. Result 4 gives $P = \operatorname{charpoly}(f)$ over $\mathbb{Q}_p$, hence over $\mathbb{Z}_p$, and applying $\psi$ gives the claim. $\square$

### De Rham homology in characteristic $p$

For an abelian variety $A$ over $k$, let $P(A)$ be the space of primitive classes in the first [algebraic de Rham cohomology|13F5JZPDD0] of $A$, and let the *de Rham homology* $H_{\mathrm{dR}}(A)$ be its $k$-dual. An endomorphism $f$ acts on $P(A)$ by pullback $f^*$, and on $H_{\mathrm{dR}}(A)$ by the dual map $f_*$.

Lean: `GlobalTheory.DeRham.primDR`, `GlobalTheory.DeRham.HdR`, `GlobalTheory.DeRham.push`.

**Theorem 8.26.5 (Characteristic polynomial in characteristic $p$).** Let $k$ be a perfect field of characteristic $p$, $A$ an abelian variety over $k$ with $H_{\mathrm{dR}}(A)$ finite dimensional, and $f$ an endomorphism of $A$. Then
$$\operatorname{charpoly}(f_*) = \operatorname{charpoly}(f) \text{ mapped to } k[x].$$

Lean: `GlobalTheory.DeRhamCharpolyP.charpoly_push` (also `GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charP`, a second name).

We use the following results, the theorem on the Dieudonné module and the chosen Dieudonné theory of the previous section.

### Inputs

1. $A$ has a torsion tower with some group $G$. (`GlobalTheory.AVTower.exists_tower`)
2. For $p$ nilpotent in a ring $R$, an abelian scheme $A$ over $R$ and a torsion tower with group $G$, there is an isomorphism $P(A) \cong \operatorname{RigExt}(G)$, natural in $A$: it carries $f^*$ to the map that $t(f)$ induces on rigidified extensions. (`GlobalTheory.deRhamVectorExtension`)

*Proof.* Take $G$ and $t$ from result 1, and let $T$ be the chosen theory, so that $M(G)$ is free and finite. Its reduction map $M(G) \to \operatorname{RigExt}(G)$ is surjective, semilinear over $W \to k$, has kernel $pM(G)$, and carries $f_D$ to the map $\rho_f$ that $t(f)$ induces on $\operatorname{RigExt}(G)$. The reduction is onto $k$ since every $x \in k$ is the reduction of its Teichmüller lift. We now use a lemma of linear algebra: if $\pi : R \to K$ is a surjective map to a field with $\pi(c) = 0$, $M$ is free of finite rank over $R$, and $r : M \to V$ is $\pi$-semilinear, surjective, with kernel $cM$, then the images of a basis of $M$ form a basis of $V$. So if $r \circ \varphi = \psi \circ r$, then $\psi$ has the matrix of $\varphi$ reduced by $\pi$, and its characteristic polynomial is that of $\varphi$ mapped by $\pi$. Hence $\operatorname{charpoly}(\rho_f)$ is the image of $\operatorname{charpoly}(f_D)$, which by the theorem on the Dieudonné module is the image of $\operatorname{charpoly}(f)$. By result 2, $f^*$ on $P(A)$ is conjugate to $\rho_f$, and $f_*$ is the dual of $f^*$, which has the same characteristic polynomial since the matrix of a dual map is the transpose. $\square$

### Algebraically closed fields and $\ell$-adic lattices

**Theorem 8.26.6 (Characteristic polynomial over an algebraically closed field).** Let $k$ be algebraically closed, $A$ an abelian variety over $k$ with $H_{\mathrm{dR}}(A)$ finite dimensional, and $f$ an endomorphism of $A$. Then $\operatorname{charpoly}(f_*) = \operatorname{charpoly}(f)$ mapped to $k[x]$.

Lean: `GlobalTheory.DeRham.charpoly_push_eq_map_charpoly`.

*Proof.* If $k$ has characteristic $p > 0$, it is perfect and the previous theorem applies. If $k$ has characteristic $0$, we quote the same statement in characteristic $0$ (`GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charZero`). $\square$

**Theorem 8.26.7 (Characteristic polynomial from an $\ell$-adic lattice).** Let $k$ be algebraically closed, $A$ a commutative group scheme over $k$ that is an abelian scheme, $f$ an endomorphism of $A$, $L$ a free $\mathbb{Z}$-module of finite rank with an endomorphism $\varphi$, and $\ell$ a prime with $\ell \neq 0$ in $k$. Suppose that for each $j$ there is a homomorphism $e_j$ from $L$ to $A(k)$ with
$$e_j(\varphi x) = f(e_j x), \qquad \ker e_j = \ell^j L, \qquad \operatorname{im} e_j = A[\ell^j](k),$$
and that $H_{\mathrm{dR}}(A)$ is finite dimensional. Then
$$\operatorname{charpoly}(f_*) = \operatorname{charpoly}(\varphi) \text{ mapped to } k[x].$$

Lean: `GlobalTheory.DeRham.charpoly_push_eq` (also `GlobalTheory.T.charpoly_deRhamHomology_endomorphism_eq_map_ladic`, a second name).

We use the following results.

### Inputs

1. An abelian scheme over a field is smooth of some relative dimension $g$, so $A$ with this $g$ is an abelian variety. (`GlobalTheory.AV.exists_smoothOfRelativeDimension_of_isAbelianScheme`)
2. For an abelian variety over an algebraically closed field and $L$, $\varphi$, $\ell$ and $e_j$ as in the theorem, $\operatorname{charpoly}(\varphi) = \operatorname{charpoly}(f)$. (`GlobalTheory.T.l_power_torsion_endomorphism_evaluation`)

*Proof.* By result 1, $A$ is an abelian variety. By result 2 we may replace $\operatorname{charpoly}(\varphi)$ by $\operatorname{charpoly}(f)$, and the previous theorem applies. $\square$

**Remark 8.26.8 (Formalization).** The theorem on determinants and degrees is in [ExistsCompEqZeroOfNotIsIsogeny.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCompEqZeroOfNotIsIsogeny.lean#L83), with the zero divisor step as lemmas at [line 25](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCompEqZeroOfNotIsIsogeny.lean#L25) and [line 56](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCompEqZeroOfNotIsIsogeny.lean#L56); we read the second as using that $\operatorname{End}(A) \otimes \mathbb{Q}$ is finite dimensional. The theorem on the Dieudonné module is in [CharpolyMapEq.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyMapEq.lean#L71); it is stated for any Dieudonné theory, and the hypotheses that $M(G)$ is free and finite always hold by the axioms of a base. The characteristic $p$ theorem is in [CharpolyDeRhamHomologyAbelianVarietyCharP.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharP.lean#L81), with the linear algebra lemma at line 18 and the dual map lemma at line 68. Its second name is a wrapper under a raised heartbeat limit that tries three tactics, in a file that imports Mathlib twice: [CharpolyDeRhamHomologyAbelianVarietyCharPStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharPStatement.lean#L10). The last two theorems are in [CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyEndomorphismEqMapLadic.lean#L18), and the second name of the $\ell$-adic theorem is a wrapper of the same kind: [CharpolyDeRhamHomologyEndomorphismEqMapLadicStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyEndomorphismEqMapLadicStatement.lean#L8). The finiteness of $H_{\mathrm{dR}}(A)$ is a hypothesis of each theorem, but it always holds: it is proved as a lemma in [CharpolyDeRhamHomologyAbelianVarietyCharZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CharpolyDeRhamHomologyAbelianVarietyCharZero.lean#L57). The polynomial $\operatorname{charpoly}(f)$ is defined by choice, with value $0$ when no characteristic polynomial exists. In the $\ell$-adic theorem the maps $e_j$ are not required to be compatible as $j$ varies. We read the statements of the results quoted in this section, not their proofs.
