---
title: Sections with prescribed reduction
decls:
  - GlobalTheory.Mum.exists_secs_finExt
  - GlobalTheory.T.exists_sections_prescribed_reduction_finite_ext
  - GlobalTheory.Mum.SecsAsm.secs_exists
  - GlobalTheory.Mum.exists_secs_of_intFam
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sections with prescribed reduction

This section builds, on the abelian variety $A$ of a labelled cover, a finite family of sections of a power of the polarisation bundle whose reductions at every complete trait are known: they map the closed fibre of the group, through a fixed isomorphism, onto the closed fibre of the torus extension of $D$ embedded in a projective space. A last section $\theta$ of degree one has a known nonzero locus on the closed fibre. The [next section](/entry/emb-of-secs/) uses these sections to embed a neighbourhood of the closed fibre of the cover in a projective space, which is the input of the descent. The tools are the theta expansions of [the previous section](/entry/exists-map-exp-all-traits/) and the [completion](/learn/commutative-algebra/#completion) of $R$.

Throughout, $R$ is a base with maximal ideal $\mathfrak{m}$, residue field $\kappa(R)$ and fraction field $K$, $D = (B, L, \mathsf{X}, c, \psi)$ is degeneration data over $R$, and $C$ is a labelled cover of $D$, with modification $(S, \pi, \gamma)$, group $G$ over $S$, line bundle $P$, abelian variety $A$ with $\alpha : A \to G$, and odd prime $n$. We use the integral theta families, the traits of $C$ and the expansions of [the previous section](/entry/exists-map-exp-all-traits/), and write $P_A = \alpha^* P$.

### Normalised theta sections

**Theorem 4.5.1 (Normalised theta sections).** Let $R$ be a base, $D$ degeneration data over $R$ and $C$ a labelled cover of $D$. Then:

1. there is $j_0$ such that for every $j \geq j_0$ there is a map $\Phi_j$ from integral theta families of level $n^j$ to sections of $P_A^{n^j}$ on $A$ with the following property: at every trait $T$ of $C$ over a ring $W$ there is a unit $u \in W^\times$ such that $\Phi_j(\mathcal{F})$ has expansion $(1, u)$ along $\mathcal{F}$ at $T$ for every $\mathcal{F}$;
2. for every integral theta family $\mathcal{F}_1$ of level $1$ there is a section $\theta$ of $P_A$ on $A$ such that at every trait $T$ of $C$ over a ring $W$ there is a unit $u \in W^\times$ with $\theta$ of expansion $(1, u)$ along $\mathcal{F}_1$ at $T$.

Lean: `GlobalTheory.Mum.exists_secs_of_intFam`.

So $\Phi_j(\mathcal{F})$ extends over every trait, and there its Fourier expansion is a unit times the pullback of $\mathcal{F}$.

*Proof.* There is $k_0$ with the following property: for every $k \geq k_0$, a map $\Phi$ from integral theta families of level $k$ to sections of $P_A^k$, which has at every trait an expansion $(a, b)$ with $a, b \neq 0$ for all families, can be replaced by a map $\Phi'$ that has at every trait an expansion $(1, u)$ with $u$ a unit. This is a normalisation of the scalars at the origin. Put $j_0 = k_0$. For $j \geq j_0$ we have $n^j > j \geq k_0$, since $n > 1$. By [the theorem on theta sections at all traits](/entry/exists-map-exp-all-traits/), there is a map for level $n^j$ with nonzero expansion scalars at every trait, and the normalisation gives part 1.

For part 2, apply part 1 with $j = 2 j_0$. Then $n^j = m^2$ for $m = n^{j_0}$, and $m$ is odd. So [the theorem on a theta section normalised at all traits](/entry/exists-theta-unit-at-traits/) applies to $\Phi_{2 j_0}$ and gives $\theta$. $\square$

### The torus extension and its terms

**Definition 4.5.2 (Torus extension).** A *torus extension* for $D$ is a commutative group scheme $H$ over $R$ with a natural bijection between the points of $H$ with values in $R$-schemes and the points of the extension of $B$ by the split torus with character group $\mathsf{X}$ that is defined by $c$. We write $q : H \to B$ for the projection. For $k \geq 0$, $\chi \in \mathsf{X}$ and a section $b$ of $M_{k, \chi}$ on $B$, a section $t$ of $q^* L^k$ on $H$ is the *term* of $b$ if $t(x) = b(q(x)) \cdot x_\chi$ for every point $x$ of $H$, where $x_\chi$ is the $\chi$-component of the torus part of $x$.

Lean: `GlobalTheory.Mum.Ext` (also `GlobalTheory.Mum.IsTermOf`, the terms).

The torus extension is the Raynaud extension $\widetilde{G}$ of the data, defined over all of $\operatorname{Spec} R$. Every $D$ has a torus extension, $H$ is smooth over $R$, $q$ is affine and onto, and every $b$ has a term. The term of $b$ is the monomial $b \cdot t^\chi$ of a theta series.

### Sections with prescribed reduction

Let $h : Y \to X$ and $h' : Y' \to X$ be morphisms and let $s$, $s'$ be sections of $h^* \mathcal{L}^k$ and $h'^* \mathcal{L}^k$ for a line bundle $\mathcal{L}$ on $X$. We say that $s$ and $s'$ *agree* if their values are equal at all points $p$ of $Y$ and $p'$ of $Y'$ with $h(p) = h'(p')$.

**Definition 4.5.3 (Sections with prescribed reduction).** Let $(S, \pi, \gamma)$ be a modification of $\operatorname{Spec} R$, let $G$ be a group scheme over $S$ with a line bundle $\mathcal{L}$, and let $\alpha : A \to G$ be a morphism. A *system of sections with prescribed reduction* consists of: integers $N$ and $k$; sections $s_0, \dots, s_N$ of $\alpha^* \mathcal{L}^k$ and a section $\theta$ of $\alpha^* \mathcal{L}$; a smooth group scheme $Y$ over $\kappa(R)$ with an immersion $j : Y \to \mathbb{P}^N_R$ over $\operatorname{Spec} \kappa(R)$; and a nonempty open subset $O$ of $Y$. We require the following trait condition. Let $V$ be a complete trait, $\varphi : R \to V$ an injective local map and $\xi$ a trait of $S$ over $\varphi$. Then there are a complete trait $V'$ with a finite injective map $\iota : V \to V'$, a group scheme $G'$ over $V'$ with $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $\xi \circ \operatorname{Spec}\iota$, sections $\sigma_i$ of $\beta^* \mathcal{L}^k$ that agree with $s_i$, a section $\theta'$ of $\beta^* \mathcal{L}$ that agrees with $\theta$, a map $\kappa : \kappa(R) \to \kappa(V')$ compatible with $\iota \circ \varphi$, and an isomorphism of group schemes $e$ from the closed fibre of $G'$ to $Y \otimes_{\kappa} \kappa(V')$. For every field $\Omega$ and every point $p$ of the closed fibre of $G'$ with values in $\Omega$, with image $p'$ in $G'$ and image $y$ in $Y$ under $e$:

1. the $\sigma_i(p')$ have no common zero, and the point $[\sigma_0(p') : \dots : \sigma_N(p')]$ of $\mathbb{P}^N$ is $j(y)$;
2. if $y \in O$, then $\theta'(p') \neq 0$.

Lean: `GlobalTheory.Mum.Secs`.

So the sections $s_i$ extend over every trait, after a finite extension, and on the closed fibre they give the fixed immersion $j$ of $Y$, up to the isomorphism $e$. This is the sense in which their reduction is prescribed. The theorem below takes $Y$ to be the closed fibre of the torus extension.

**Theorem 4.5.4 (Sections with prescribed reduction).** Let $R$ be a base, $D$ degeneration data over $R$ and $C$ a labelled cover of $D$. Then $C$ has a system of sections with prescribed reduction, for the modification of $C$, its group $G$, the line bundle $P$ and the map $\alpha$.

Lean: `GlobalTheory.Mum.SecsAsm.secs_exists`.

*Proof.* *Step 1: an immersion of the torus extension.* Let $H$ be a torus extension for $D$. There are a finite set $\Sigma \subseteq \mathsf{X}$ and $k_1$ such that for every $k \geq k_1$ there are $N$, characters $\chi_0, \dots, \chi_N \in \Sigma$, sections $b_i$ of $M_{k, \chi_i}$ on $B$, and the terms $t_i$ of $b_i$ on $H$, such that the $t_i$ have no common zero and $[t_0 : \dots : t_N] : H \to \mathbb{P}^N_R$ is an immersion.

*Step 2: integral families with a given leading term.* For each $\chi \in \mathsf{X}$ there is $k_0(\chi)$ such that for $k \geq k_0(\chi)$ every section $b$ of $M_{k, \chi}$ is the leading term at $\chi$ of an integral theta family of level $k$. For $\chi = 0$ this holds for every $k \geq 1$.

*Step 3: the degree.* Let $j_0$ be as in [the theorem on normalised theta sections](/entry/exists-secs-of-int-fam/), let $j = \max(j_0, k_1 + \sum_{\chi \in \Sigma} k_0(\chi))$ and $k = n^j$. Then $k \geq j$, so $k \geq k_1$ and $k \geq k_0(\chi)$ for $\chi \in \Sigma$. Step 1 gives $N$, $\chi_i$, $b_i$ and $t_i$ for this $k$, and Step 2 gives integral families $\mathcal{F}_i$ of level $k$ that lead at $\chi_i$ with $b_i$. Put $s_i = \Phi_j(\mathcal{F}_i)$.

*Step 4: the theta section.* There are a section $b_\theta$ of $M_{1, 0}$ on $B$ with term $t_\theta$ on $H$ and a point $y_0$ of $H$ over the closed point of $\operatorname{Spec} R$ with $t_\theta(y_0) \neq 0$. By Step 2 there is an integral family $\mathcal{F}_1$ of level $1$ that leads at $0$ with $b_\theta$. Let $\theta$ be the section of part 2 of the theorem on normalised theta sections for $\mathcal{F}_1$.

*Step 5: the closed fibre.* Let $Y = H \otimes_R \kappa(R)$, a smooth group scheme over $\kappa(R)$. The map $j$ is the restriction of the immersion of Step 1 to $Y$; it is an immersion, since $Y \to H$ is a closed immersion. Let $O$ be the set of points of $Y$ where $t_\theta$ is not zero. It is open, and it is nonempty since it contains a point over $y_0$.

*Step 6: the trait condition.* Let $V$, $\varphi$ and $\xi$ be as in the definition. After a finite extension $\iota : V \to V'$ there is a trait $T$ of $C$ over $V'$, with group $G_{V'}$ and $\beta$, over $\iota \circ \varphi$ and $\xi \circ \operatorname{Spec}\iota$. By the choice of $\Phi_j$ and $\theta$ there are units $u, u_\theta$ of $V'$ and sections $\sigma_i$, $\theta'$ on $G_{V'}$ which are equal to $s_i$ and $\theta$ on $A$, and which expand as $u \mathcal{F}_i$ and $u_\theta \mathcal{F}_1$. At the trait $T$ there are a map $\kappa : \kappa(R) \to \kappa(V')$ and a group isomorphism $e$ of the closed fibre of $G_{V'}$ with $Y \otimes \kappa(V')$ such that the following holds: if a section $\sigma$ on $G_{V'}$ expands as $u\mathcal{F}$, and $\mathcal{F}$ leads at $\chi$ with $b$, then at corresponding points $p'$ of the closed fibre of $G_{V'}$ and $y$ of $Y$ the value $\sigma(p')$ is $c$ times the value at $y$ of the term of $b$, with a unit $c$ that depends on the points and on $u$ only. This is the meaning of the leading condition: modulo $\mathfrak{m}$, only the term at $\chi$ remains in the Fourier expansion.

Apply this to the $\sigma_i$: the values $\sigma_i(p')$ are $c\, t_i(y)$ for one unit $c$, so they have no common zero, and $[\sigma_i(p')] = [t_i(y)] = j(y)$. Apply it to $\theta'$: $\theta'(p') = c'\, t_\theta(y)$ with $c'$ a unit, so $\theta'(p') \neq 0$ if $y \in O$. $\square$

**Theorem 4.5.5 (Sections after a finite extension).** Let $R$ be a base, $D$ degeneration data over $R$ and $C$ a labelled cover of $D$. Then there are a finite extension $\rho : R \to R_1$, degeneration data $D_1$ over $R_1$ that are a pullback of $D$ along $\rho$, and a labelled cover $C_1$ of $D_1$ which has a system of sections with prescribed reduction.

Lean: `GlobalTheory.Mum.exists_secs_finExt` (also `GlobalTheory.T.exists_sections_prescribed_reduction_finite_ext`, a second name).

*Proof.* Take $R_1 = R$, $\rho$ the identity, $D_1 = D$ and $C_1 = C$. The identity is a finite extension, and $D$ is a pullback of itself along the identity. The previous theorem gives the sections. $\square$

**Remark 4.5.6 (Formalization).** The finite extension of the last theorem is the identity ([ExistsSectionsPrescribedReductionFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSectionsPrescribedReductionFiniteExt.lean#L120), lines 122 to 124, with `GlobalTheory.DegPullId.exists_isPullDeg_id_self`), so the statement is weaker than what is proved. The second name is a wrapper proved by a `first | exact` tactic. The theorem on normalised theta sections is a term `GlobalTheory.Mum.SecsDesc.assemble` applied to three statements: `GlobalTheory.T.exists_map_thetaExpansion_all_traits`, `GlobalTheory.T.exists_origin_normalisation_unit_at_traits` (the normalisation at the origin) and `GlobalTheory.T.exists_thetaSection_normalised_unit_at_traits`. The lemma `assemble` sits in the file `ImportsTailRest.lean`, line 13, whose name does not describe it. In the proof of the main theorem, Step 1 is `GlobalTheory.T.exists_theta_immersion_torus_extension_projective`, Step 2 is `GlobalTheory.T.exists_integralThetaFamily_prescribed_leadingTerm`, Step 4 is `GlobalTheory.Mum.exists_term_nonzero_closed`, the comparison of Step 6 is `GlobalTheory.Mum.trait_lead_value`, and the passage to projective points is `GlobalTheory.Mum.toProj_secPull_of_sval`. The smoothness of $H$ comes from `GlobalTheory.Mum.ext_smooth_affine_surj_terms`; its other four outputs are discarded (line 37). The existence of a torus extension is an `instance` in the definition file, proved from `GlobalTheory.allSixLaws`.
