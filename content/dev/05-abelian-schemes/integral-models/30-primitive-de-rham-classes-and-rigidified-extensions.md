---
title: Primitive de Rham classes and rigidified extensions
decls:
  - GlobalTheory.deRhamVectorExtension
  - GlobalTheory.T.deRhamVectorExtensionIso_of_hodgeDeRham
  - GlobalTheory.deRhamVectorExtension_of_abelianHodgeDeRham
  - GlobalTheory.T.exists_canonical_deRham_rigidExtension_family
  - GlobalTheory.DeRhamExt.exists_canonical_family
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Primitive de Rham classes and rigidified extensions

Let $R$ be a ring in which $p$ is nilpotent, $A$ an abelian scheme over $R$, and $G$ a $p$-divisible group with a torsion tower for $A$. This section constructs an isomorphism between the primitive classes in the first de Rham cohomology of $A$ and the rigidified extensions of $G$. The isomorphism is natural, carries the Hodge part to the invariant differentials, and is compatible with tangent vectors. It is the comparison between de Rham cohomology and the universal vector extension, and it is how the chapter moves between de Rham homology and Dieudonné theory: [the theorem on characteristic polynomials in characteristic $p$](/entry/charpoly-push/) uses it, and so does [the Kodaira-Spencer map of weight one](/entry/kodaira-spencer-of-weight-one/). The proof assumes [the Hodge and de Rham structure of abelian schemes](/entry/ab-coh-abelian-hodge-de-rham/) and builds the isomorphism from canonical rigidified extensions.

### Notation

We use the $p$-divisible groups, semilinear maps and rigidified extensions $\operatorname{RigExt}(G)$ of Section 8.25, and the torsion towers of Section 8.26, now over a ring $R$. A torsion tower $t$ for $A$ with group $G$ is a family of homomorphisms $y_n : \operatorname{Spec} A_n(G) \to A$, compatible with the maps $A_{n+1}(G) \to A_n(G)$, injective on points, with image the points of $A$ killed by $p^n$.

For a $p$-divisible group $G$ over $R$, $\omega(G)$ is the module of compatible invariant differentials of the $A_n(G)$. The map $\omega(G) \to \operatorname{RigExt}(G)$ sends $w$ to the class of the pair $(0, w)$; we write $\omega(G)$ also for its image. We put
$$\operatorname{Lie}(G) = \omega(G)^\vee, \qquad \operatorname{Lie}^{\natural}(G) = \operatorname{RigExt}(G)^\vee,$$
the duals over $R$, and write $\operatorname{Lie}^{\natural}(G) \to \operatorname{Lie}(G)$ for the dual of the inclusion of $\omega(G)$.

For an abelian scheme $A$ over $R$, let $H^1_{\mathrm{dR}}(A)$ be the first [[algebraic de Rham cohomology|13F5JZPDD0]] of $A$, and $P(A) \subseteq H^1_{\mathrm{dR}}(A)$ the primitive classes, those $c$ with $m^* c = \mathrm{pr}_1^* c + \mathrm{pr}_2^* c$. Let $H_{\mathrm{dR}}(A) = P(A)^\vee$, as in Section 8.26. The *Hodge part* $F^1 P(A)$ is the set of primitive classes that map to $0$ in $H^1(A, \mathcal{O}_A)$, and $\operatorname{Fil} H_{\mathrm{dR}}(A)$ is its annihilator in $H_{\mathrm{dR}}(A)$.

### Canonical rigidified extensions

A primitive class gives a rigidified extension of $G$ through the tower: we represent the class by a Čech cocycle, evaluate it on the points $y_n$, and correct by elements of $A_n(G)$ to obtain a 2-cocycle and an invariant differential on each $A_n(G)$.

**Definition 8.30.1 (Canonical rigidified extension).** Let $A$ be an abelian scheme over $R$, $t$ a torsion tower for $A$ with group $G$, and $c \in P(A)$. A *datum* for $(t, c)$ consists of a Čech 1-cocycle $f$ of $\mathcal{O}_A$ whose class is $c$, an additivity datum $g$ for the values of $f$ on pairs of points, and elements $h_n \in A_n(G)$ such that the value of $f$ at $y_{n+1}$, restricted to $A_n(G)$, equals $h_n - \operatorname{res}(h_{n+1})$ for every $n$. A datum gives elements $z_n \in A_n(G) \otimes A_n(G)$ and $w_n$ in the cotangent module of $A_n(G)$: $z_n$ is the value of $g$ at the two universal points of $\operatorname{Spec}(A_n(G) \otimes A_n(G))$, minus the coboundary of the value of $f$ at $y_n$, minus the coboundary of $h_n$; and $w_n$ is the cotangent value of $f$ at $y_n$ minus $d h_n$. An element $x \in \operatorname{RigExt}(G)$ is *canonical for $c$* if for some datum the $z_n$ form a cocycle $z$ of $G$, the $w_n$ form an element $w$ of $\omega(G)$, and $x$ is the class of $(z, w)$.

Lean: `GlobalTheory.PtExt.Dat` (also `GlobalTheory.PtExt.IsCan`).

### Inputs

We use the following results. The first one is [the Hodge and de Rham structure](/entry/ab-coh-abelian-hodge-de-rham/) of Chapter 1; the others are statements about canonical extensions.

1. (Hodge and de Rham structure.) Let $A$ be an abelian scheme over a ring $R$, smooth of relative dimension $g$. Then $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$, its exterior square is $H^2_{\mathrm{dR}}(A)$ by the cup product, $\Omega(A)$ and $H^1(A, \mathcal{O}_A)$ are finite projective of rank $g$, every global 1-form is closed, $\Omega(A) \to H^1_{\mathrm{dR}}(A)$ is injective, $H^1_{\mathrm{dR}}(A) \to H^1(A, \mathcal{O}_A)$ is surjective, and these modules commute with base change. (`GlobalTheory.T.abelianScheme_deRham_locallyFree_hodgeDegenerates`, `GlobalTheory.AbCoh.abelianHodgeDeRham`)
2. (Canonical map.) For every ring $R$, abelian scheme $A$ over $R$, prime $p$ and torsion tower $t$ for $A$ with group $G$, there is an $R$-linear map $L : P(A) \to \operatorname{RigExt}(G)$ such that $x$ is canonical for $c$ if and only if $x = L(c)$. (`GlobalTheory.T.exists_linear_canonical_map_primitiveDeRham_rigExt`)
3. (Relative dimension.) Assume result 1. If $p$ is prime and nilpotent in $R$ and $A$ has a torsion tower, then $A$ is smooth of some relative dimension $g$. (`GlobalTheory.T.exists_relativeDimension_abelian_torsionTower`)
4. (Bijectivity.) Assume result 1. If $p$ is prime and nilpotent in $R$, $A$ is smooth of relative dimension $g$ and $L$ is a map such that $L(c)$ is canonical for $c$ for all $c$, then $L$ is bijective. (`GlobalTheory.T.deRham_to_rigidified_extension_bijective_p_nilpotent`)
5. (Naturality.) Let $\sigma : R \to R'$ be a ring map, $A$ over $R$ and $A'$ over $R'$ abelian schemes with towers $t$ and $t'$, and $\varphi : A' \to A$ a homomorphism over $\operatorname{Spec} \sigma$. Let $s$ be the semilinear map of $p$-divisible groups that $\varphi$ induces through the towers. If $x$ is canonical for $c$, then $s_{\mathrm{rig}}(x)$ is canonical for $\varphi^* c$. (`GlobalTheory.T.canonicalRigidifiedExtension_pullback_naturality`)
6. (Hodge part.) If $p^N = 0$ in $R$ and $L$ is surjective with $L(c)$ canonical for $c$ for all $c$, then $L(F^1 P(A)) = \omega(G)$. (`GlobalTheory.T.canonical_iso_hodge_filtration_eq_range_invariant_forms`)
7. (Tangent vectors.) Assume result 1. If $p$ is prime and nilpotent in $R$, $A$ is smooth of relative dimension $g$ and $E : P(A) \to \operatorname{RigExt}(G)$ is an isomorphism with $E(c)$ canonical for $c$, then $E$ is compatible with tangent vectors in the sense of the theorem below. (`GlobalTheory.T.lie_image_iff_lie_correspondence_deRham_extension`)

### The theorem

We now state the compatibility with tangent vectors. Let $R[\varepsilon]$ be the ring of dual numbers. A map $v : \operatorname{Spec} R[\varepsilon] \to A$ is a *tangent vector* if it reduces to the origin at $\varepsilon = 0$. For $h \in H_{\mathrm{dR}}(A)$, $v$ is a *Lie image* of $h$ if $v$ is a tangent vector and $h(\mathrm{cl} f) = f(v)$ for every 1-form $f$ on $A$ whose class $\mathrm{cl} f$ is primitive, where $f(v)$ is the value of $f$ on $v$. For $x \in \operatorname{Lie}(G)$, $v$ *corresponds to $x$ under $t$* if $v$ is a tangent vector and for every $n$ there is an $R$-algebra map $\psi : A_n(G) \to (R/p^n)[\varepsilon]$ such that $y_n \circ \operatorname{Spec} \psi$ is $v$ reduced modulo $p^n$, and such that $x(w)$ modulo $p^n$ is the $\varepsilon$-coefficient of $\psi(a)$ whenever $w \in \omega(G)$ and $d a = w_n$.

**Theorem 8.30.2 (Canonical family).** Assume the Hodge and de Rham structure (result 1), and let $p$ be a prime. Then there is a family of $R$-linear isomorphisms
$$e_t : P(A) \xrightarrow{\ \sim\ } \operatorname{RigExt}(G),$$
one for each ring $R$ in which $p$ is nilpotent, each abelian scheme $A$ over $R$ and each torsion tower $t$ for $A$ with group $G$, such that:

1. (Natural) for $\sigma$, $\varphi$, $t$, $t'$ and $s$ as in result 5 and $c \in P(A)$, $e_{t'}(\varphi^* c) = s_{\mathrm{rig}}(e_t(c))$;
2. (Filtered) $e_t(F^1 P(A)) = \omega(G)$;
3. (Tangent) for $h \in H_{\mathrm{dR}}(A)$ and $v : \operatorname{Spec} R[\varepsilon] \to A$, $v$ is a Lie image of $h$ if and only if $v$ corresponds under $t$ to the image of $h \circ e_t^{-1} \in \operatorname{Lie}^{\natural}(G)$ in $\operatorname{Lie}(G)$;
4. (Canonical) $e_t(c)$ is canonical for $c$, for every $c \in P(A)$.

Lean: `GlobalTheory.DeRhamExt.exists_canonical_family` (also `GlobalTheory.T.exists_canonical_deRham_rigidExtension_family`, a second name).

*Proof.* For each $(R, A, t)$ let $L_t$ be the map of result 2, so that $L_t(c)$ is the unique canonical element for $c$. By result 3, $A$ has a relative dimension $g$, and by result 4, $L_t$ is bijective; let $e_t$ be the inverse pair of isomorphisms it defines. Property 4 holds by the choice of $L_t$. For property 1, $e_t(c)$ is canonical for $c$, so by result 5, $s_{\mathrm{rig}}(e_t(c))$ is canonical for $\varphi^* c$; by the uniqueness in result 2 it equals $e_{t'}(\varphi^* c)$. Property 2 is result 6, since $p$ is nilpotent and $e_t$ is surjective. Property 3 is result 7, with $g$ from result 3. $\square$

**Theorem 8.30.3 (De Rham classes and rigidified extensions).** For every prime $p$ there is a family of isomorphisms $e_t : P(A) \to \operatorname{RigExt}(G)$, indexed as in the previous theorem, with the properties Natural, Filtered and Tangent.

Lean: `GlobalTheory.deRhamVectorExtension` (also `GlobalTheory.deRhamVectorExtension_of_abelianHodgeDeRham` and `GlobalTheory.T.deRhamVectorExtensionIso_of_hodgeDeRham`, which prove it from the Hodge and de Rham structure).

*Proof.* The previous theorem gives the family under the Hodge and de Rham structure; we forget property 4. The Hodge and de Rham structure holds by [Theorem 1.15.1](/entry/ab-coh-abelian-hodge-de-rham/). $\square$

Two consequences are used later. By property 2, an element $h \in H_{\mathrm{dR}}(A)$ lies in $\operatorname{Fil}$ if and only if the image of $h \circ e_t^{-1}$ in $\operatorname{Lie}(G)$ is $0$: $h$ kills $F^1 P(A)$ exactly when $h \circ e_t^{-1}$ kills $\omega(G)$. By property 1 applied to $\sigma = \mathrm{id}_R$, a homomorphism $f : A \to B$ of abelian schemes over $R$ with towers $t$ and $u$ satisfies $e_t(f^* c) = t(f)_{\mathrm{rig}}(e_u(c))$, where $t(f) : G \to H$ is the morphism of Section 8.26. So $e$ carries $f^*$ on $P$ to the map that $t(f)$ induces on rigidified extensions, and dually $f_*$ on $H_{\mathrm{dR}}$ to the map on $\operatorname{Lie}^{\natural}$. This is the form used for characteristic polynomials in Section 8.26.

**Remark 8.30.4 (Formalization).** The family and its three properties are defined in [DeRhamVectorExtension.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/DeRhamVectorExtension.lean#L20), lines 20 to 48; the two consequences are at lines 64 and 77 of the same file. The theorem without hypothesis is [DeRhamVectorExtension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DeRhamVectorExtension.lean#L8). Both wrappers of a second name, [ExistsCanonicalDeRhamRigidExtensionFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCanonicalDeRhamRigidExtensionFamilyStatement.lean#L13) and [DeRhamVectorExtensionIsoOfHodgeDeRhamStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DeRhamVectorExtensionIsoOfHodgeDeRhamStatement.lean#L13), raise the heartbeat limit at line 13 and try three tactics at line 15 to apply one lemma. The map $L_t$ is chosen by the axiom of choice from result 2 ([ExistsCanonicalDeRhamRigidExtensionFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCanonicalDeRhamRigidExtensionFamily.lean#L24), lines 24 to 26). Property 4 is dropped at [line 19](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DeRhamVectorExtensionIsoOfHodgeDeRham.lean#L19) of the second proof. Results 2 to 7 are cited by their statements; we do not unfold the additivity datum, the cotangent value or the value $f(v)$ of a form on a tangent vector. Result 2 asks for no hypothesis on $p$, while the family is indexed only by rings in which $p$ is nilpotent.
