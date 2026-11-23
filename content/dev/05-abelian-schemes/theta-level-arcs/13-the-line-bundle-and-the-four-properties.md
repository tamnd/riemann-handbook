---
title: The line bundle and the four properties
decls:
  - GlobalTheory.T.exists_lineBundle_extension_thetaSection_semiAbelian
  - GlobalTheory.ZJ.exists_extension_with_section
  - GlobalTheory.T.nonempty_of_fourProperties_groupScheme
  - GlobalTheory.ZH.ZHPre.nonempty_out
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The line bundle and the four properties

In this section we prove two inputs of the extension of a theta-level abelian scheme. The first one extends the line bundle $\mathcal{L}$ of theta data from $A$ to the semi-abelian scheme $G$ of a core, with a section near each point of the base that does not vanish identically on the fibres. It is used in [the semi-abelian cubical extension](/entry/exists-law-split-all-cubical/). The second one shows that a pre-extension with four properties gives an extension of $\rho$. It is the last step of [the extension of a theta-level abelian scheme](/entry/zh-geo/). We keep the notation of the three previous sections. As there, $\overline{\mathbb{Q}}_p$ is the algebraic closure of $\mathbb{Q}_p$ with its absolute value, and $\mathcal{O}_p$ is its valuation ring.

### Norms on a line bundle

A line bundle $\mathcal{L}$ on a scheme $X$ comes with charts $U_j$ that trivialise it and transition functions $g_{ij}$. For a point $x : \operatorname{Spec} \overline{\mathbb{Q}}_p \to X$ inside $U_i$ and a function $f$ on $U_i$, we write $|f(x)|$ for the absolute value of $f$ at $x$.

**Definition 6.13.1 (Norm system).** A *norm system* $\nu$ on $\mathcal{L}$ assigns a real number $\nu_p(x, j)$ to each prime $p$, each point $x : \operatorname{Spec} \overline{\mathbb{Q}}_p \to X$ and each chart $j$. It is *adapted* if all values are positive, if $|g_{ij}(x)| \, \nu_p(x, i) = \nu_p(x, j)$ whenever the image of $x$ lies in $U_i \cap U_j$, and if $\nu_p(x, j) = 1$ whenever $x$ extends to an $\mathcal{O}_p$-point whose closed point lies in $U_j$.

Lean: `GlobalTheory.ZJ.Nrm` (also `GlobalTheory.ZJ.IsNrm`, adapted).

Let $a : X \to Y$ and $W \subset Y$. A point $x : \operatorname{Spec} \overline{\mathbb{Q}}_p \to X$ is *integral into $W$* if $a \circ x$ extends to an $\mathcal{O}_p$-point of $Y$ whose closed point lies in $W$. For maps $\varphi_k : Y \to X$ and integers $\varepsilon_k$, a generator $t$ of $\bigotimes_k \varphi_k^* \mathcal{L}^{\varepsilon_k}$ has *norm one* at a point $x$ of $Y$ if $|t(x)| \prod_k \nu_p(\varphi_k \circ x, j_k)^{\varepsilon_k} = 1$ for every choice of charts $j_k$ that contain the points $\varphi_k \circ x$.

Lean: `GlobalTheory.ZJ.IntAt` (also `GlobalTheory.ZJ.NormOne`, norm one).

### Norms adapted to theta data

Let $C$ be a core with a group law, and let $T = (\mathcal{L}, \theta, m, \mathcal{O}_1, s)$ be theta data on $C$. Write $\Omega_m \subset G$ for the image under $[m]$ of the set where $s$ does not vanish.

**Definition 6.13.2 (Base change test).** The data $T$ satisfy the *base change test* if, for every test $(V, H)$ of $C$, every extension $\theta_H$ of $T$ to it and every point $x$ of the special fibre of $H$, the image of $x$ in $G$ lies in $\Omega_m$ if and only if $\theta_H(x) \neq 0$.

Lean: `GlobalTheory.ZJ.Core.Theta.BTest` (also `GlobalTheory.ZJ.Core.Theta.Om`, the set $\Omega_m$).

**Definition 6.13.3 (Norms for theta data).** Let $\Omega \subset G$. A norm system $\nu$ on $\mathcal{L}$ is a *norm for $T$ with respect to $\Omega$* if it is adapted, if the rigidification has norm one at every $\overline{\mathbb{Q}}_p$-point of $U$ that extends to an $\mathcal{O}_p$-point of $Z$, if the cube generator has norm one at every triple of points of $A$ that are integral into $G$, and if this holds: for each $\overline{\mathbb{Q}}_p$-point $y$ of $U$ there is $\delta > 0$ such that $|\theta(x)| \, \nu_p(x, j) \leq \delta$ for all points $x$ of $A$ over $y$ that are integral into $G$, with equality if and only if $x$ is integral into $\Omega$.

Lean: `GlobalTheory.ZJ.Core.Theta.Norms`.

**Definition 6.13.4 (Companion property).** A set $\Omega \subset G$ has the *companion property* if for each closed point $w$ of $G$ there are an open set $N \subset Z$, sections $b$ and $c$ of $G$ over $N$, a field point $t$ of $N$ and a point $x$ of $G$ over $t$ with image $\{w\}$ such that, with $b' = b \circ t$ and $c' = c \circ t$, the six points $b'$, $c'$, $b' c'$, $x b'$, $x c'$ and $x b' c'$ all lie in $\Omega$.

Lean: `GlobalTheory.ZJ.Core.Law.CompanionTheory`.

### Inputs

The extension statement for semi-abelian schemes says: over a discrete valuation ring with fraction field $K$, let $G$ be commutative, smooth, separated, quasi-compact and geometrically connected, and let $e_A$ be a $K$-point of the generic fibre over the unit. Then every line bundle on the generic fibre with a generator of its fibre at $e_A$ extends to a rigidified line bundle on $G$. The statement on multiplication by $n$ was given in [the previous sections](/entry/exists-law-split-all-cubical/). We use the following results.

**Theorem 6.13.5 (Base change tests hold).** If $[n]$ is surjective on abelian varieties over algebraically closed fields $K$ with $n \neq 0$ in $K$, then all theta data on a core with a group law satisfy the base change test.

Lean: `GlobalTheory.T.baseChangeTest_of_surjective_mul_abelianVariety`.

**Theorem 6.13.6 (Étale multiplication).** If $G$ is semi-abelian and the statement on multiplication by $n$ holds, then $[m]$ is étale on $G$ and $\Omega_m$ is open.

Lean: `GlobalTheory.ZJ.etale_mulN_and_isOpen_om_of_isSemiAbelian`.

**Theorem 6.13.7 (Norms exist).** Under the extension statement, if $C$ has tests and $T$ satisfies the base change test, then $T$ has a norm with respect to $\Omega_m$.

Lean: `GlobalTheory.T.exists_norms_of_tests`.

**Theorem 6.13.8 (Companions).** Under the extension statement, if $C$ has tests and torsion sections of order $n$, and $T$ satisfies the base change test and has few zeros of order $n$, then $\Omega_m$ has the companion property.

Lean: `GlobalTheory.T.companionTheory_om_of_tests_torsionSections`.

**Theorem 6.13.9 (Generators of norm one).** Let $\Omega$ be open, let $\nu$ be a norm for $T$ with respect to $\Omega$, and let $\Omega$ have the companion property. Then each closed point $w$ of $G$ has an open neighbourhood $W$, and there are a nonempty open set $W_0 \subset A$ and a generator of $\mathcal{L}$ on $W_0$ with norm one at every point of $W_0$ that is integral into $W$.

Lean: `GlobalTheory.ZJ.Core.exists_gen_normOne`.

**Theorem 6.13.10 (Line bundles from generators).** Let $X$ be an integral normal scheme, flat and locally of finite type over $\mathbb{Z}$, let $a : A_0 \to X$ be an open immersion, and let $\nu$ be an adapted norm system on a line bundle $\mathcal{L}$ on $A_0$. If every closed point of $X$ has generators of norm one as in the last theorem, then there are a line bundle $\mathcal{M}$ on $X$, an isomorphism $a^* \mathcal{M} \cong \mathcal{L}$, and for each chart $i$ of $\mathcal{M}$ a nonempty open set $D_i \subset A_0$ such that the isomorphism has norm one at every point of $D_i$ that is integral into the chart $i$.

Lean: `GlobalTheory.exists_lineBundle_of_normOne_generators`.

**Theorem 6.13.11 (Local sections).** Under the hypotheses of the theorem on generators of norm one, let $\mathcal{M}$ be a line bundle on $G$ as in the conclusion of the last theorem, with $X = G$ and $A_0 = A$. Then the conclusion of the next theorem holds.

Lean: `GlobalTheory.T.exists_local_section_ne_zero_on_fibres'`.

### The line bundle

**Theorem 6.13.12 (Extension of the line bundle).** Assume the extension statement for semi-abelian schemes, the statement on multiplication by $n$, and that $[n]$ is surjective on abelian varieties over algebraically closed fields in which $n \neq 0$. Let $C$ be a core with a group law for which $G$ is semi-abelian, with tests and torsion sections of order $n$, and let $T$ be theta data on $C$ with few zeros of order $n$. Then there is a line bundle $\mathcal{M}$ on $G$ with $a^* \mathcal{M} \cong \mathcal{L}$ such that each $z \in Z$ has an open neighbourhood $N$ and a section $\sigma$ of $\mathcal{M}$ over $G_N$ with this property: each $z' \in N$ is the image of a point of $G_N$ where $\sigma$ does not vanish.

Lean: `GlobalTheory.T.exists_lineBundle_extension_thetaSection_semiAbelian` (also `GlobalTheory.ZJ.exists_extension_with_section`, a second name).

*Proof.* By the surjectivity of $[n]$, the data $T$ satisfy the base change test. Since $G$ is semi-abelian, $\Omega_m$ is open. The extension statement and the tests give a norm $\nu$ for $T$ with respect to $\Omega_m$. The torsion sections and the few zeros give the companion property of $\Omega_m$. So each closed point of $G$ has generators of norm one.

The basic properties of a core say that $G$ is integral, flat and locally of finite type over $\mathbb{Z}$, and that $a$ is an open immersion. The base $Z$ is normal and $G$ is smooth over $Z$, so all local rings of $G$ are integrally closed domains, and $G$ is normal. The theorem on line bundles from generators, with $X = G$ and $A_0 = A$, gives $\mathcal{M}$ with an isomorphism $a^* \mathcal{M} \cong \mathcal{L}$ of norm one on the sets $D_i$. The theorem on local sections gives the sections $\sigma$. $\square$

### The four properties

**Theorem 6.13.13 (Four properties).** Assume that homomorphisms of semi-abelian schemes over a discrete valuation ring extend uniquely from the generic fibre, the uniformisation over complete local domains, the semistable reduction statement, the uniformisation statement, the first two bundles of laws and the torsion statement for uniformisations. Let $S$ be a big theta system over an arithmetic base $o \subset \Omega$ with a realisation $\rho$, let $M$ be a model of $\Omega$ with an admissible open set $U_0$, and let $E$ be a lattice system fixed by tests. Let $Q$ be a closure of $\rho$ over $(M, U_0, E)$ with an extension. Let $(u_0, G, \mathcal{L}')$ be a pre-extension of $\rho$ with an isomorphism $G \cong G_Q$ that respects the maps to $Z$, the map $u_0$ and the map from $u_0^* A$. If the pre-extension has extended torsion sections, local theta sections, theta model sections and the right abelian locus, then $\rho$ has an extension.

Lean: `GlobalTheory.T.nonempty_of_fourProperties_groupScheme` (also `GlobalTheory.ZH.ZHPre.nonempty_out`, a second name).

*Proof.* We take the same $u_0$, $G$, $\mathcal{L}'$ and splitting, and we prove the six properties of an extension.

*Property 1.* The unique extension of homomorphisms gives the symmetry hypothesis for $\mathcal{L}'$, the extension of endomorphisms, and the extension of isomorphisms between linear combinations of pullbacks.

*Property 2.* The right abelian locus gives that the abelian locus is $\{z : T(z) = 0\}$. The first bundle of laws and the theta model sections make $\mathcal{L}'$ relatively ample with trivial $K(\mathcal{L}')$ over each open set in the abelian locus.

*Property 3.* This is the property of extended torsion sections.

*Property 4.* The set $\{z : T(z) = 0\}$ is open, so the abelian locus is open. For a complete noetherian normal local domain $R'$ and a map $\xi : \operatorname{Spec} R' \to Z$ that meets it, the pullback $\xi^* G$ satisfies the hypotheses of the uniformisation over complete local domains: it is semi-abelian, the line bundle $\xi^* \mathcal{L}'$ is symmetric with the symmetry hypothesis, the closed fibre is split, the local theta sections give a section that does not vanish at a point of the closed fibre, and the abelian locus, the properness and the ampleness pull back. So $\xi^* G$ has a uniformisation with the required line bundle.

*Property 5.* The torsion sections of the closure, the local theta sections, the semistable reduction statement, the laws and the torsion statement give the section that extends $\theta_1 / \vartheta(x_0)$. The theta model sections give, for each $v \in E(z)$, the section of $\mathcal{L}'^N$ that extends $\sum_l v_l s_l / \vartheta(x_0)$.

*Property 6.* The theta model sections give, for a matrix $b$ whose rows span $E$ on $W$, sections $\sigma'_i$ with no common zero and independent on fibres. Let $(\sigma_i)$ be any family with these properties. Two sections of $\mathcal{L}'^N$ that agree at the generic points are equal, so $\sigma_i = \sigma'_i$. The closure immerses $G_Q$ into projective space by its theta sections, and the isomorphism $G \cong G_Q$ carries this to $G_W$. At each point of $G_W$ some $\sigma_i$ is nonzero, since its value at a geometric point over the point is nonzero. So $(\sigma_i)$ immerses $G_W$. $\square$

**Remark 6.13.14 (Formalization).** The extension of the line bundle is proved in [ExistsLineBundleExtensionThetaSectionSemiAbelian.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsLineBundleExtensionThetaSectionSemiAbelian.lean#L23), and the four properties in [NonemptyOfFourPropertiesGroupScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/NonemptyOfFourPropertiesGroupScheme.lean#L204). The first names are `first | exact ...` wrappers in the files with the suffix `Statement`. The definitions of norms are in [CompanionTheory.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/CompanionTheory.lean#L12). The base change test is derived for all theta data from the surjectivity of $[n]$ alone; the theorem takes no hypothesis on the core. In the four properties, the closure $Q$, its extension and the isomorphism with $G_Q$ are used only for property 6. Sixteen fields of the extension, from $u_0$ to the splitting, are copied from the pre-extension. We did not unfold `Semi.extend_existsSt`, `Out.MulNSt`, `abLocus`, `ImmersedBy` or the inputs listed above.
