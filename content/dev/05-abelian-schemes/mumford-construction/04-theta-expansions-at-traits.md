---
title: Theta expansions at traits
decls:
  - GlobalTheory.Mum.exists_map_exp_all_traits
  - GlobalTheory.T.exists_map_thetaExpansion_all_traits
  - GlobalTheory.Mum.exists_theta_unit_at_traits
  - GlobalTheory.T.exists_thetaSection_normalised_unit_at_traits
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta expansions at traits

A labelled cover of degeneration data $D$ has a polarised abelian variety $A$ over $K$, and at every complete trait it is uniformised by a pullback of $D$. This section turns integral theta families of $D$ into sections of powers of the polarisation bundle of $A$, so that at every trait the section has the given family as its Fourier expansion, up to nonzero scalars. In degree one it then normalises one section so that the scalar is a unit at every trait. The next section uses both results to build [sections with prescribed reduction](/entry/exists-secs-of-int-fam/), and from these the projective embedding of the cover near its closed fibre. The section uses the [algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions) and [Galois theory](/learn/algebra/#galois-theory) from Volume 1.

Throughout, $R$ is a base with maximal ideal $\mathfrak{m}$ and fraction field $K$, and $D = (B, L, \mathsf{X}, c, \psi)$ is degeneration data over $R$, with $\tau$ as in [the first section](/entry/has-of-base/). Let $C$ be a [labelled cover](/entry/has-fin-of-lab-cover/) of $D$ with modification $(S, \pi, \gamma)$, semi-abelian scheme $G$ over $S$, line bundle $P$, abelian variety $A$ with $\alpha : A \to G$, and odd prime $n$. We write $P_A = \alpha^* P$; it is isomorphic to the polarisation bundle of $A$.

### Theta families

For $k \geq 1$ and $\chi \in \mathsf{X}$ let $M_{k, \chi}$ be the line bundle on $B$ with fibre
$$L_x^{k-1} \otimes L_{x + c(\chi)} \otimes L_{c(\chi)}^{-1} \otimes L_0$$
at $x$, a rigidified twist of $L^k$ by the translate along $c(\chi)$. A *theta family of level $k$* over a field $F$ over $K$ is a family $(s_\chi)_{\chi \in \mathsf{X}}$ of sections $s_\chi$ of $M_{k, \chi}$ on $B_F$ that satisfies the functional equation
$$s_{\chi + k\mu} = \psi(\mu)^k \, \tau(\mu, \chi) \, T_{c(\mu)}^* s_\chi \qquad (\chi, \mu \in \mathsf{X}),$$
where $T_{c(\mu)}$ is the translation by $c(\mu)$ and the products are read through the canonical generators. In Mumford's theory these are the Fourier coefficients of the sections of $L^k$ on the generic fibre of the uniformised group.

**Definition 4.4.1 (Integral theta family).** An *integral theta family of level $k$* for $D$ is a theta family $(s_\chi)$ of level $k$ over $K$ together with sections $f_\chi$ of $M_{k, \chi}$ on $B$ over $R$ such that $f_\chi$ restricts to $s_\chi$ on the generic fibre, and such that for every $e \geq 0$ the section $f_\chi$ vanishes modulo $\mathfrak{m}^{e+1}$ for all but finitely many $\chi$. The family *leads at $\chi_0$ with $b$* if $f_{\chi_0} = b$ and $f_\chi$ vanishes modulo $\mathfrak{m}$ for $\chi \neq \chi_0$.

Lean: `GlobalTheory.Mum.IntFam` (also `GlobalTheory.Mum.IntFam.Lead`, the leading condition).

The finiteness condition makes the formal sum $\sum_\chi f_\chi$ finite modulo every power of $\mathfrak{m}$. This is the integral form of the convergence of a theta series.

### Traits of a labelled cover

**Definition 4.4.2 (Trait of a labelled cover).** A *trait* of $C$ over a ring $W$ consists of: a structure of complete trait on $W$; an injective local map $\varphi : R \to W$; a trait $\xi : \operatorname{Spec} W \to S$ over $\varphi$; a commutative group scheme $G_W$ over $W$ with $\beta : G_W \to G$ that makes $G_W$ the group pullback of $G$ along $\xi$; degeneration data $D_W$ over $W$ that are a pullback of $D$ along $\varphi$; a polarised abelian variety $A_W$ over $\operatorname{Frac} W$ and a uniformisation $U$ of $G_W$ by $D_W$ with generic fibre $A_W$; a generating isomorphism $\ell$ from the line bundle $L_U$ of $U$ to $\beta^* P$; and the compatibility of $U$ with the labels of $C$, as in the trait condition of a labelled cover.

Let $T$ be a trait of $C$ over $W$, let $k \geq 1$, let $\mathcal{F} = (s_\chi, f_\chi)$ be an integral theta family of level $k$, and let $a, b \in W$.

1. A section $\sigma$ of $\beta^* P^k$ on $G_W$ *expands as $b \mathcal{F}$* if $\sigma = b\, \ell^k(\sigma')$ for a section $\sigma'$ of $L_U^k$ on $G_W$ whose Fourier coefficients, through $U$ at every thickening $\operatorname{Spec} W/\mathfrak{m}_W^{e+1}$, are the pullbacks to $D_W$ of the $f_\chi$.
2. A section $s$ of $P_A^k$ on $A$ *has expansion $(a, b)$ along $\mathcal{F}$ at $T$* if there is a section $\sigma$ of $\beta^* P^k$ on $G_W$ that expands as $b \mathcal{F}$ and is equal to $a s$ at all points of $G_W$ and $A$ with the same image in $G$.

Lean: `GlobalTheory.Mum.Trait` (also `GlobalTheory.Mum.Trait.Exp`, the expansion).

In condition 1, "the Fourier coefficients are the $f_\chi$" means: modulo $\mathfrak{m}_W^{e+1}$, the uniformisation identifies $G_W$ with the Raynaud extension of the abelian part, and there $\sigma'$ is the finite sum of the pulled back $f_\chi$ times the sections of the torus parts for the characters $\chi$. So a section has expansion $(a, b)$ along $\mathcal{F}$ when, up to the ratio $b / a$, its theta series at the trait is the pullback of $\mathcal{F}$. We call $b/a$ the *expansion scalar*. Every trait of the trait condition of $C$ gives a trait of $C$ after a finite extension of the ring.

### Sections with a given expansion

**Theorem 4.4.3 (Theta sections at all traits).** Let $R$ be a base, $D$ degeneration data over $R$, $C$ a labelled cover of $D$ with prime $n$, and $j \geq 0$. Then there is a map $\Phi$ from integral theta families of level $n^j$ to sections of $P_A^{n^j}$ on $A$ such that the following holds. For every trait $T$ of $C$ over a ring $W$ there are $a, b \in W$, both nonzero, such that $\Phi(\mathcal{F})$ has expansion $(a, b)$ along $\mathcal{F}$ at $T$ for every integral theta family $\mathcal{F}$ of level $n^j$.

Lean: `GlobalTheory.Mum.exists_map_exp_all_traits` (also `GlobalTheory.T.exists_map_thetaExpansion_all_traits`, a second name).

The point is that the scalars $a$ and $b$ depend on the trait only, and not on the family.

*Proof.* Put $N = n^j$. Then $N$ is odd and $N \geq 1$. If $C$ has no trait over any ring, every map $\Phi$ has the property; take $\Phi = 0$. So assume that $C$ has a trait $T_0$ over a ring $W_0$.

*Step 1: labels and an equivariant map at one trait.* Let $\bar K$ be an algebraic closure of $K$. Since $\varphi_0 : R \to W_0$ is injective, there is an algebraically closed field $F_0$ over $\operatorname{Frac} W_0$ with a $K$-embedding of $\bar K$ that agrees with $\varphi_0$ on $R$. The trait $T_0$ gives labels from the torsion classes $Q_N(D)(F_0)$ to $A(F_0)$ that extend the labels $\ell_j$ of $C$. It also gives a map $E$ from theta families of level $N$ over $F_0$ to sections of $P_A^N$ on $A_{F_0}$ that is *equivariant* for these labels: $E$ is bijective and $F_0$-linear, the labels map onto the $N$-torsion of $A$, and $E$ carries the action of the torsion classes on theta families to the action of the theta group of $P_A^N$ through the labels. The inverse of $E$ reads the theta series at $T_0$: if a section $\sigma$ on $G_{W_0}$ expands as $\mathcal{F}$, then $\sigma$ agrees with $E$ of the generic family of $\mathcal{F}$, up to the given isomorphism of $P_A$ with the polarisation bundle.

*Step 2: descent to $K$.* Since $N$ is odd, an equivariant map for labels over $F_0$ that extend the labels $\ell_j$ gives an equivariant map $E'$ over $\bar K$ for the labels $\ell_j$. Since $C$ has a trait, the labels $\ell_j$ commute with every $K$-automorphism of $\bar K$. So an equivariant map over $\bar K$ can be chosen with a rational form: there are a map $\Phi_0$ from integral theta families of level $N$ to sections of the polarisation bundle of $A$ to the power $N$ over $K$, and an equivariant map $E_0$ over $\bar K$, such that $E_0$ of the generic family of $\mathcal{F}$ agrees with $\Phi_0(\mathcal{F})$. Let $\Phi(\mathcal{F})$ be the section of $P_A^N$ that corresponds to $\Phi_0(\mathcal{F})$ under the isomorphism of $P_A$ with the polarisation bundle.

*Step 3: one constant at each trait.* Let $T$ be a trait of $C$ over $W$, and let $F$ be an algebraically closed field over $\operatorname{Frac} W$ with a $K$-embedding of $\bar K$ that agrees with $\varphi$ on $R$. The map $E_0$ and the map that $T$ gives as in Step 1 are compared over $F$. There is $c \in F$, $c \neq 0$, such that for every integral theta family $\mathcal{F}$ and every section $\sigma$ on $G_W$ that expands as $\mathcal{F}$, the values of $\sigma$ are $c$ times the values of $\Phi(\mathcal{F})$ at the geometric points over $F$ with the same image in $G$.

*Step 4: integral sections and descent from $F$.* Since $N \geq 1$, for each $\mathcal{F}$ there is a section $\sigma$ on $G_W$ that expands as $\mathcal{F}$. With Step 3, the constant $c$ descends from $F$ to $\operatorname{Frac} W$, and there are $a, b \in W$, both nonzero, with $c = b/a$, such that $\Phi(\mathcal{F})$ has expansion $(a, b)$ along $\mathcal{F}$ at $T$ for all $\mathcal{F}$. $\square$

**Theorem 4.4.4 (A theta section normalised at all traits).** Let $R$ be a base, $D$ degeneration data over $R$, $C$ a labelled cover of $D$, and $m$ an odd number. Let $\Phi$ be a map from integral theta families of level $m^2$ to sections of $P_A^{m^2}$ on $A$, and assume that at every trait $T$ of $C$ over a ring $W$ there is a unit $u \in W^\times$ such that $\Phi(\mathcal{F})$ has expansion $(1, u)$ along $\mathcal{F}$ at $T$ for every $\mathcal{F}$. Then for every integral theta family $\mathcal{F}_1$ of level $1$ there is a section $\theta$ of $P_A$ on $A$ such that at every trait $T$ of $C$ over a ring $W$ there is a unit $u \in W^\times$ with $\theta$ of expansion $(1, u)$ along $\mathcal{F}_1$ at $T$.

Lean: `GlobalTheory.Mum.exists_theta_unit_at_traits` (also `GlobalTheory.T.exists_thetaSection_normalised_unit_at_traits`, a second name).

So in level $m^2$ the hypothesis asks for the normalisation, and the theorem gives it in level $1$. The section $\theta$ extends over every trait, and its reduction there is not zero.

*Proof.* There is a section $\theta_0$ of $P_A$ such that at every trait $T$ there are nonzero $a, b \in W$ with $\theta_0$ of expansion $(a, b)$ along $\mathcal{F}_1$. Compare $\theta_0$ with the normalised sections of level $m^2$. Since $m$ is odd, the expansion scalars $b/a$ of $\theta_0$ have a common ratio from $R$: there are $r, t \in R$, both nonzero, such that at every trait $T$ there are an expansion $(a, b)$ of $\theta_0$ and a unit $v \in W^\times$ with
$$b\, \varphi(t) = a\, \varphi(r)\, v.$$
Put $\theta = (t / r)\, \theta_0$, a section of $P_A$ on $A$ since $r \neq 0$ in $K$. At a trait $T$ with $a, b, v$ as above, take the section $\sigma$ on $G_W$ for $\theta_0$; it is equal to $a \theta_0$ on $A$ and expands as $b \mathcal{F}_1$. Then $\varphi(t)\sigma / (a \varphi(r))$ is equal to $\theta$ on $A$, and it expands as $b \varphi(t) / (a \varphi(r))\, \mathcal{F}_1 = v \mathcal{F}_1$. So $\theta$ has expansion $(1, v)$ along $\mathcal{F}_1$ at $T$. $\square$

In the next section the second theorem is applied with $m$ a power of $n$, and its hypothesis comes from the first theorem after a normalisation of the scalars at the origin.

**Remark 4.4.5 (Formalization).** Both second names are wrappers, proved by a `first | exact` tactic. In [ExistsMapThetaExpansionAllTraits.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMapThetaExpansionAllTraits.lean#L32), the case without traits is the last line (line 51): it returns the zero map, so the theorem has no content when $C$ has no trait. The line bundle property of $P$ is found by a `first | exact C.P.L.isLB | exact C.P.L.hL | exact C.P.L.lb` fallback (line 37). Step 1 is `GlobalTheory.T.trait_inverse_expansion_equivariant_labels`, whose last output is discarded with `-`; Step 2 is `GlobalTheory.Mum.Desc.eqv_down`, `GlobalTheory.Mum.labExt_of_trait` and `GlobalTheory.Mum.exists_eqv_rational`, with the transport `GlobalTheory.T.exists_lineBundlePowSection_transport_pullbackIso`; Step 3 is `GlobalTheory.T.integral_family_expansion_eq_const_mul_algClosure`; Step 4 is `GlobalTheory.T.exists_integralSection_expanding_thetaFamily` and `GlobalTheory.T.traitExpansion_descends_from_algClosed_field`. The word "equivariant" describes the predicate `Eqv`. The constant of Step 3 is the conclusion of one lemma; the Lean statements give no separate lemma on uniqueness of equivariant maps. In the second theorem, $\theta_0$ is `GlobalTheory.T.exists_polarisationSection_ratio_integralThetaFamily`, the ratio is `GlobalTheory.T.thetaExpansionScalars_ratio_odd_mul`, and the rescaling is `GlobalTheory.T.trait_expansionScalar_rescale_degreeOne`. A theta family is `Fam`, with functional equation `DegPre.FamFE`; the bundle $M_{k,\chi}$ is the linear combination of pullbacks along `DegPre.famφB` with exponents `DegPre.famε k`, that is $(k - 1, 1, -1, 1)$; the Fourier expansion at a thickening is `UnifPre.ExpandsAt`.
