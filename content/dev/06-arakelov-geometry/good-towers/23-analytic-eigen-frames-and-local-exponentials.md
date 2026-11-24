---
title: Analytic eigen frames and local exponentials
decls:
  - GlobalTheory.T.eigen_frames_analytic
  - GlobalTheory.CompanionTheory.Ar.Flat.exists_gen_of_unitAn
  - GlobalTheory.T.gaga_line_generator_embedding
  - GlobalTheory.CompanionTheory.Ar.Flat.gaga_rat
  - GlobalTheory.T.eigen_frame_function_compare
  - GlobalTheory.CompanionTheory.Ar.Flat.extendsUnitAt_resolution
  - GlobalTheory.T.exists_family_exponential_locally
  - GlobalTheory.CompanionTheory.Ar.Flat.exists_famExp_near
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Analytic eigen frames and local exponentials

The flat frame functions of the last sections are defined analytically: their norms are constant at the archimedean places, they change by determinants under a change of frames, and they are holomorphic in families. To use them in the arithmetic of the model we need an algebraic generator. This section proves that an analytic frame function is, up to a nonzero constant, the value of an algebraic generator of the line bundle of top wedges of the two eigen lattices on the generic fibre. The proof resolves the singularities of the model, uses GAGA on the resolution, and needs holomorphic exponentials in families of commutative group schemes. The result is used in the [covolume statement](/entry/top-covol-slim2-use-alt-alt/), where the frame function of the flat degree must be algebraic.

We keep the setting of the last section: $E$, $H$, $D$ with $N = p + q \ge 1$, a moduli space $X_o$, a coefficient datum with number field $F$, a Noetherian discrete valuation ring $O$ with an injective map $\beta: O \to F$ such that $F$ is its fraction field, a model $Y$, an unfolding $U$ and a geometric component $Z$ with generic point $\xi_0$ and field $\Omega$. Let $\tau$ be an embedding of $E$ with $\tau(\sqrt{-d}) = r_0$, and let $\sigma: F \to \mathbb{C}$ with $\sigma(\tau(\sqrt{-d})) = r_0$.

### Analytic frame functions

**Definition 8.23.1 (Analytic unit frame function).** A frame function $\Phi$ is an analytic unit for $\tau$ and $\sigma$ if:

1. $\Phi(y, v, w) \ne 0$ at all framed complex points;
2. under a change of frames $v' = v A$ and $w' = w B$, $\Phi(y, v', w') \det A = \Phi(y, v, w) \det B$;
3. at Hodge frames with Gram matrices $\Gamma$ and $\Delta$, $|\Phi|^2 \, |\det \Gamma| = |\det \Delta|$;
4. $\Phi$ is holomorphic along holomorphic families of framed points.

**Definition 8.23.2 (Extension as a unit).** Let $F$ be a function on complex points, and let $t$ be a local generator of a line lattice at a complex point $x$. $F$ extends as a unit at $x$ for $t$ if for every holomorphic family $y_b$ of points through $x$ there are $\varepsilon > 0$ and a holomorphic function $h$ on the ball of radius $\varepsilon$ with $h(b_0) \ne 0$ and
$$
F(y_b) = h(b) \, r_b ,
$$
where $r_b$ is the value of $t$ at $y_b$.

### Inputs

We use two named inputs of the top level inputs. The first is resolution of singularities with coordinates: a variety over a field of characteristic $0$ has a proper birational map from a smooth variety, which is an isomorphism over the smooth locus, with simple normal crossings coordinates on the complement of an open set. See the [learning page on resolution](/learn/geometry/#resolution-of-singularities). The second is GAGA for sections: on a proper smooth complex variety $X$ with a line bundle $L$, a family of holomorphic local functions that is compatible with the transition functions of $L$ comes from an algebraic section.

### Holomorphic exponentials in families

**Definition 8.23.3 (Family exponential).** Let $G$ be a smooth commutative group scheme over a ring $R$, with a Lie model $M$ of dimension $g$, and let $\psi_b$ be a family of points of $\mathrm{Sp}\,R$ over $\mathbb{C}$ that is holomorphic in $b \in B$. A family exponential over $B$ is a family of maps $\exp_b: \mathbb{C}^g \to G(\psi_b)$ with:

1. $\exp_b(z + w) = \exp_b(z) \exp_b(w)$;
2. $\exp_b(z)$ is holomorphic in $(b, z)$;
3. the derivative of $\exp_b$ at $0$ is given by the vectors of the Lie model;
4. there is an analytic local logarithm that inverts $\exp$ near $(b_0, 0)$.

**Lemma 8.23.4 (Local family exponentials).** Let $G$ be smooth and commutative over $R$ with a Lie model, and let $\psi$ be holomorphic on an open set $B$. For every $b_0 \in B$ there is $\varepsilon > 0$ with $\mathrm{ball}(b_0, \varepsilon) \subseteq B$ and a family exponential over this ball.

Lean: `GlobalTheory.T.exists_family_exponential_locally` (also `GlobalTheory.CompanionTheory.Ar.Flat.exists_famExp_near`, a second name).

*Proof.* Since $G$ is smooth, there is a holomorphic chart $\Psi$ of the family of complex groups near the unit section, and in this chart the group law is a holomorphic function $\mu_b(z, w)$. The group is commutative, so the holomorphic germ of the group law has a formal logarithm $L_b$ with $L_b(\mu_b(z, w)) = L_b(z) + L_b(w)$, and it converges near $(b_0, 0)$. Its inverse gives $\exp_b$ on a small ball of $\mathbb{C}^g$, holomorphic in $(b, z)$, and the slices in $b$ are inverses for each $b$. A local homomorphism from a ball of $\mathbb{C}^g$ extends in a unique way to a homomorphism on $\mathbb{C}^g$, by $\exp_b(z) = \exp_b(z/n)^n$ for large $n$. The extension is still holomorphic, and the derivative at $0$ is the derivative of the inverse of $L_b$, which is given by the Lie model. $\square$

The family exponential is used to write the frames of the Lie algebra at nearby points as values of holomorphic functions, which is how the holomorphy of $\Phi$ is used on the resolution.

### Comparison on the resolution

**Lemma 8.23.5 (Frame function on the resolution).** Let $\pi: X' \to Y_F$ be a resolution, smooth of relative dimension $d$ over $F$, with simple normal crossings coordinates on the complement of an open set $W'$, and let $\xi'$ be a generic point over $\xi_0$. Let $W \subseteq W'$ be open, and let $F'$ be a function on complex points of $X'$ with $F'(y') = \Phi(y, v, w)$ at framed points. Assume that the pull back of the line lattice of $\wedge b_1 / \wedge b_2$ is generated by $1$ on $W$, where $b_1$ and $b_2$ are bases of the two eigenspaces. Then for every complex point $x$ of $X'$ over $\sigma$ there is a local generator $t$ of the line lattice at $x$ such that $F'$ extends as a unit at $x$ for $t$.

Lean: `GlobalTheory.T.eigen_frame_function_compare` (also `GlobalTheory.CompanionTheory.Ar.Flat.extendsUnitAt_resolution`, a second name).

*Proof.* The eigen lattices are vector bundles on $X'$, so near $x$ there is an affine chart with bundle sections that give frames $v_b$ and $w_b$ at every point $y_b$ of a holomorphic family through $x$. At the complex point $x$ these are vectors of the eigen lattices, and they pair to frames on an open set. Let $t$ be the wedge of these frames. By the change of frames property, $F'(y_b)$ is $\Phi$ at the chart frames times the ratio of determinants, and the ratio is the value $r_b$ of $t$. By the holomorphy and the nonvanishing of $\Phi$, the first factor is a holomorphic function $h$ with $h(b_0) \ne 0$. The pull back of frames to the complex point gives the claim. $\square$

### GAGA for line generators

**Theorem 8.23.6 (Algebraic generators by GAGA).** Let $K$ be a field with $\sigma: K \to \mathbb{C}$, let $X$ be proper and smooth over $K$, and let $\xi: \mathrm{Sp}\,\Omega \to X$ be a component generic point with $K$ closed in $\Omega$. Let $L$ be a line lattice on $X$ that is a vector bundle of rank $1$, and let $W$ be an open set that contains the generic point, such that $L$ is generated by $1$ at the components in $W$. Let $F$ be a function on complex points such that for every complex point $x$ over $\sigma$ there is a local generator $t$ with which $F$ extends as a unit at $x$. Then there are $f$ and $\kappa \ne 0$ such that $f$ generates $L$ at all components, and the value of $f$ at every complex point $y$ in $W$ is $\kappa F(y)$.

Lean: `GlobalTheory.T.gaga_line_generator_embedding` (also `GlobalTheory.CompanionTheory.Ar.Flat.gaga_rat`, a second name).

*Proof.* Base change to $\mathbb{C}$ along $\sigma$. The local functions $h_x$ that come from the extension as a unit are compatible with the transition functions of $L$, and they do not vanish. So by GAGA for sections over $\mathbb{C}$ they are the values of an algebraic section $f_{\mathbb{C}}$ of $L_{\mathbb{C}}$ that generates $L_{\mathbb{C}}$ everywhere. The space of such generators is a torsor under the units of the proper variety, which are constants. Since $K$ is closed in $\Omega$, the proper model and its generic fibre compare, and a lattice basis pulls back along the dominant map from the component. So $f_{\mathbb{C}}$ is a constant multiple of a section $f$ defined over $K$; the constant is $\kappa^{-1}$. $\square$

### The analytic frame theorem

**Theorem 8.23.7 (Analytic eigen frames).** Assume resolution of singularities with coordinates and GAGA for sections. Let $\Phi$ be an analytic unit frame function for $\tau$ and $\sigma$, and let $b_1$ and $b_2$ be bases of the $\tau$ and $\bar\tau$ eigenspaces at the generic point of $Z$. Then there are $f \in \Omega$, $\kappa \ne 0$ and an open set $W$ that contains the generic point, such that $f \wedge b_1$ and $\wedge b_2$ give a line generator on the generic fibre over $W$, and for every complex point $y$ over $\sigma$ in $W$ and $U$ there are framed $v$ and $w$, the values of $b_1$ and $b_2$ at $y$, with
$$
f(y) = \kappa \, \Phi(y, v, w) .
$$

Lean: `GlobalTheory.T.eigen_frames_analytic` (also `GlobalTheory.CompanionTheory.Ar.Flat.exists_gen_of_unitAn`, a second name).

*Proof.* Resolve the generic fibre of the component: $\pi: X' \to Y_F$, smooth over $F$, with simple normal crossings coordinates on the complement of an open set $W'$ over which $\pi$ is an isomorphism. The eigen lattices are vector bundles near the generic point, and the frames $b_1$ and $b_2$ give a frame near it, so the wedge of the eigen lattices is a line lattice on an open set $W \subseteq W'$ that is generated by $1$ there. Since the component is geometric, the generic point of $X'$ is the image of a smooth surjective map, and lattice bases pull back along the dominant map.

Put $F'(y') = \Phi(\pi y', v, w)$ at framed points. The lemma on the resolution says that $F'$ extends as a unit at every complex point of $X'$ for a local generator of the line lattice. The resolution is proper and smooth, so the GAGA theorem applies to the pull back of the line lattice and gives $f'$ and $\kappa \ne 0$. The stalk maps of the open immersion are surjective and the values along a surjective stalk map agree, so $f'$ descends to $f$ on $W$. The wedge of the line lattice is generated by $f \wedge b_1 / \wedge b_2$, and the values at complex points give $f(y) = \kappa \Phi(y, v, w)$. $\square$

So an analytic frame function is algebraic up to a constant. With the last two sections, its archimedean and finite norms are constant on components, and its log norms have the degree of the section on the flat degree.

**Remark 8.23.8 (Formalization).** In the family exponential (ExistsFamilyExponentialLocally.lean, 598 lines, main result at line 507), the map $\exp_b$ is defined as the constant `fun _ => 1` for $b$ outside the ball (line 399); this value is never used, since the result is stated on the ball. The two named inputs `ResKStatement` (BlowupProjStatement.lean:66) and `GagaSections` (GagaSections.lean:10) are hypotheses of `eigen_frames_analytic`, and both are parts of `Top.Given`; the statement file EigenFramesAnalyticStatement.lean imports `Mathlib` twice (lines 1 and 3). The analytic unit has four fields `ne`, `chg`, `norm` and `hol` (IsFlatAnIffIsConstMul.lean:33), and the extension as a unit is `ExtendsUnitAt` (line 54). The GAGA theorem is at GagaLineGeneratorEmbedding.lean:595, in a file of 671 lines with helpers in the namespace `GagaRat`, such as `cpt_base_change` (line 573) and `constClosed_complex` (line 583). The family exponential is `FamExp` (ExponentialFamilyPeriods.lean:15), and its extension from a ball is `famExp_of_inverse` (line 373) with `pow_of_add` (line 311). The `T.*` names are renamings proved by `first | exact @...`. We do not unfold the resolution, the line lattices or the holomorphic charts.
