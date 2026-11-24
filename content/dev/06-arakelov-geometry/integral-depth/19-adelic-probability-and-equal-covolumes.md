---
title: Adelic probability and equal covolumes
decls:
  - GlobalTheory.LevGeo.adelicProb_mul_volFund
  - GlobalTheory.EqCovol.covol_eq_of_isUnf
  - GlobalTheory.T.complexUniformisation_components_covolume_eq
  - GlobalTheory.LevelIsometry.petE_transl
  - GlobalTheory.LevelIsometry.keeps_cusp_lattice_norm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Adelic probability and equal covolumes

The complex points of a unitary Shimura variety are a finite union of quotients $\Gamma_k \backslash \mathcal{D}_k$, one for each component, and the same space is the adelic quotient $G(\mathbb{Q}) \backslash G(\mathbb{A}) / K$. This section proves three facts that connect these two pictures. The normalized Haar measure on the adelic quotient is the normalized sum of the masses of fundamental sets of the components. All components have the same covolume. And the Petersson norm, defined on the adelic quotient, does not change when a cusp form is moved by an automorphism of the level structure. The results are used in [the covolume of the top lattice](/entry/top-covol-g-alt-alt/) and in [the equal volume of the compactification](/entry/equal-volume-of-compactification/).

We use [hermitian data](/entry/riem-haar-eq-smul/) $X$, frames, the domain $\mathcal{D}_X$, the group $B$ of upper triangular frames, the flag chart $c_x$, the mass $\mu_x$ and fundamental sets as in the previous two sections. We also use the moduli data of [the section on the Lie determinant line](/entry/exists-of-snc/): a host $H$, a datum $\mathcal{D}$ of signature $(p, q)$, a level $l$, a moduli space $X_o$ and coefficients in a field $F$. An embedding $\sigma : F \to \mathbb{C}$ is *good* if it maps the fixed root of the base field to $\varrho_0$.

**Definition 3.19.1 (Uniformization of the components).** A *uniformization* $U$ of $X_o$ at $\sigma$ in rank $r$ consists of a finite set of components $k$, hermitian data $X_k$ of rank $r$ for each $k$, and maps from $\mathcal{D}_{X_k}$ to framed complex points of $X_o$ over $\sigma$. It is *a uniformization* in the strict sense if:

1. $r = p + q$, and for each $k$ the data $X_k$ have $p_0 = q$ and CM type $\Psi = \{ \tau : \tau(\varrho) = \varrho_0 \}$;
2. every framed complex point comes, up to a change of frame by a diagonal torus, from a point of some $\mathcal{D}_{X_k}$;
3. two points of $\mathcal{D}_{X_k}$ and $\mathcal{D}_{X_{k'}}$ give the same framed point up to the torus if and only if $k = k'$ and the frames differ by $\gamma \in \Gamma_k$ on the left and $b \in B$ on the right;
4. sections of the automorphic bundles of $X_o$ read in these charts are sections of the matching weights on $\mathcal{D}_{X_k}$, and the charts come from a family of complex abelian varieties with periods given by the frames.

We do not unfold the framed points or part 4.

**Definition 3.19.2 (Covolume of hermitian data).** For hermitian data $X$ of rank $r$, fix an orthonormal frame $x_0$ and a fundamental set $F$ for $x_0$. The *covolume* is
$$\mathrm{covol}(X) = \Bigl(\prod_{i = 0}^{r - 1} \frac{i!}{\pi^{i}}\Bigr)^{|\Psi|} \mu_{x_0}(F).$$

### The adelic probability measure

Let $W$ be a hermitian space over the host field of a datum $D$, and let $G_W(\mathbb{A})$ be the adelic unitary group of $W$, with the subgroup $G_W(\mathbb{Q})$ of rational points. Fix a Haar measure on $G_W(\mathbb{A})$ and a fundamental domain for $G_W(\mathbb{Q})$ of finite, nonzero measure. The *adelic probability measure* $\mu_{\mathrm{ad}}$ on the quotient $G_W(\mathbb{Q}) \backslash G_W(\mathbb{A})$ is the image of the Haar measure on the fundamental domain, divided by its total mass. A *dictionary* is a map that sends each $g \in G_W(\mathbb{A})$ to a component $k$ and a frame of $X_k$. *Laws* for $(U, \mathrm{dict})$ are a list of compatibility conditions: the host data of $D$ and $H$ agree, the level has $l_A = 1$, $U$ is a uniformization at every good $\sigma$, the characters of the $X_k$ are trivial on the weights that occur, and the dictionary is compatible with a level subgroup and with the uniformizations, with frames of unit Gram minors. We do not unfold these conditions.

**Theorem 3.19.3 (Adelic probability and fundamental sets).** Assume laws for $(U, \mathrm{dict})$ at the space $W = W_j$. Let $\sigma$ be good. For each component $k$ let $x_{0,k}$ be an orthonormal frame and $F_k$ a fundamental set for $x_{0,k}$. Then the total mass $M = \sum_k \mu_{x_{0,k}}(F_k)$ satisfies $0 < M < \infty$, and for every family of measurable functions $\Phi_k \ge 0$ on frames of $X_k$ that are invariant under $\Gamma_k$ on the left and under $B$ on the right on $\mathcal{D}_{X_k}$,
$$M \int \Phi(\mathrm{dict}(g))\, d\mu_{\mathrm{ad}}(g) = \sum_k \int_{F_k} \Phi_k(c_{x_{0,k}}(z))\, d\mu_{x_{0,k}}(z).$$

Lean: `GlobalTheory.LevGeo.adelicProb_mul_volFund`.

Here $\Phi(\mathrm{dict}(g))$ means $\Phi_k(y)$ when $\mathrm{dict}(g) = (k, y)$. The integrand on the left is well defined on the quotient, because the laws make the dictionary change by an element of $\Gamma_k$ when $g$ changes by a rational point.

*Proof.* Input lemmas give a pair of a Haar measure and a fundamental domain for $W$ with finite nonzero volume $v$.

*Two unfoldings.* An unfolding lemma for the dictionary gives a constant $\kappa > 0$ with
$$\int_{\text{fund.\ dom.}} \Phi(\mathrm{dict}(g))\, dg = \kappa \sum_k I_k(\Phi_k),$$
where $I_k$ is the integral over the quotient $\Gamma_k \backslash \mathcal{D}_{X_k} / B$. A second input lemma gives a universal constant $\kappa_2 > 0$, which depends only on $r$, $q$ and $|\Psi|$, with
$$I_k(\Phi_k) = \kappa_2 \int_{F_k} \Phi_k(c_{x_{0,k}}(z))\, d\mu_{x_{0,k}}(z)$$
for each $k$. All $X_k$ have the same CM type, so $\kappa_2$ is the same for all $k$.

*Normalization.* So
$$\int \Phi(\mathrm{dict}(g))\, d\mu_{\mathrm{ad}} = v^{-1} \kappa \kappa_2 \sum_k \int_{F_k} \Phi_k(c_{x_{0,k}}(z))\, d\mu_{x_{0,k}}.$$
With $\Phi = 1$ the left side is $1$, so $v^{-1}\kappa\kappa_2 M = 1$. This shows $0 < M < \infty$ and gives the formula. $\square$

### Equal covolumes

**Theorem 3.19.4 (Components have equal covolumes).** Let $\sigma$ be good and $U$ a uniformization at $\sigma$ in rank $r$. Assume that the level is good at every prime, $p \ge 1$ and $q \ge 1$. Then for all components $k$ and $k'$,
$$\mathrm{covol}(X_k) = \mathrm{covol}(X_{k'}).$$

Lean: `GlobalTheory.EqCovol.covol_eq_of_isUnf` (also `GlobalTheory.T.complexUniformisation_components_covolume_eq`, a second name).

*Proof.* An input lemma gives, for each component $k$, hermitian data $Y_k$ with the same CM type and the same $p_0 = q$ as $X_k$, whose group is the full level group of a self-dual lattice, and with $\mathrm{covol}(Y_k) = \mathrm{covol}(X_k)$. The CM types of $Y_k$ and $Y_{k'}$ are both $\{\tau : \tau(\varrho) = \varrho_0\}$, so they agree, and $1 \le p_0 < r$ since $q \ge 1$ and $p \ge 1$. A second input lemma transports $Y_{k'}$ to data $Z$ on the same hermitian space as $Y_k$, again with a self-dual lattice and full level group, with the same covolume. A third input lemma says that two self-dual lattices in the same hermitian space give the same covolume. So
$$\mathrm{covol}(X_k) = \mathrm{covol}(Y_k) = \mathrm{covol}(Z) = \mathrm{covol}(Y_{k'}) = \mathrm{covol}(X_{k'}). \qquad \square$$

### Level automorphisms and the Petersson norm

The *Petersson norm* of a family $P$ of sections of weight $\lambda$ on the components is the $L^2$ norm
$$\|P\|_{\mathrm{Pet}} = \Bigl( \int \|P(\mathrm{dict}(g))\|_\lambda^2\, d\mu_{\mathrm{ad}}(g) \Bigr)^{1/2},$$
where $\|\cdot\|_\lambda$ is the pointwise norm of weight $\lambda$. For an automorphism $\gamma$ of the level structure, the translate $\gamma \cdot f$ of a section $f$ of the automorphic bundle is the section obtained by moving the level structure by $\gamma$.

**Lemma 3.19.5 (Translation keeps the Petersson norm).** Let $\sigma$ be good, $U$ a uniformization at $\sigma$, $p + q \ge 1$ and $l_A = 1$. Let $W$ be a hermitian space with the right signatures and rank $r$, and assume that each $X_k$ is modelled on $W$, that the lattice of the moduli data embeds into $W$, that the dictionary is compatible with the uniformization, the lattices and a level subgroup, and that it takes values in frames with unit Gram minors. Let $G$ be a weight with even last entry, such that the characters of the $X_k$ are trivial on the model weights of $G$. Then for every level automorphism $\gamma$ and every integral section $f$ of weight $G$ whose reading in the charts is holomorphic,
$$\|\gamma \cdot f\|_{\mathrm{Pet}} = \|f\|_{\mathrm{Pet}}.$$

Lean: `GlobalTheory.LevelIsometry.petE_transl`.

*Proof.* Since the frames in the image of the dictionary have unit Gram minors, the pointwise norm at $\mathrm{dict}(g)$ is the absolute value of the reading of the section.

*Right translation.* An input lemma on level reductions gives $\kappa \in G_W(\mathbb{A})$ that induces the automorphism $\gamma$ on the lattice. The adelic probability measure is invariant under right translation by $\kappa$, by the invariance of the Haar measure. So for every function $\Phi$ on $G_W(\mathbb{A})$ that is invariant under rational points on the left,
$$\int |\Phi(g \kappa)|^2\, d\mu_{\mathrm{ad}} = \int |\Phi(g)|^2\, d\mu_{\mathrm{ad}}.$$
The function $g \mapsto |f(\mathrm{dict}(g))|$ is invariant on the left, since the section is $\Gamma_k$-invariant up to a character that is trivial here.

*The pointwise identity.* For each $g$, the dictionary at $g\kappa$ is the image of the dictionary at $g$ under the move of components and frames that $\gamma$ carries: there are components $k$, $k'$ and $\delta \in \mathrm{GL}_r(E)$ that carry the level automorphism, with
$$|(\gamma \cdot f)(k, y)| = |f(k', \delta\, y')|,$$
where $y'$ is $y$ cast to the frames of $X_{k'}$. An input lemma on constants of carried maps proves this, using that the hermitian data of all components have the same $\xi_0$. Combining the two steps gives the claim. $\square$

**Theorem 3.19.6 (Level automorphisms keep cusp forms, the lattice and the norms).** Let $D$ be a datum and $T$ a core datum for $D$ with laws. Let $j$ be an index such that the moduli datum at $j$ has $p \ge 1$ and $q \ge 1$, with $[E : \mathbb{Q}]/2 > 2$ and $W_j$ in the range of the datum. Let $Y$ be a deep datum over $T$ at $j$ that is good for $(e, o)$, and $G$ a weight with even last entry. Then:

1. the space of cusp forms of weight $G$ is stable under pullback by every level automorphism;
2. for every level automorphism $\gamma$ and cusp forms $f$, $g$ of weight $G$ with $g = \gamma^* f$: if $f$ lies in the integral lattice, so does $g$, and the norm of $g$ at every embedding $\sigma$ equals the norm of $f$.

Lean: `GlobalTheory.LevelIsometry.keeps_cusp_lattice_norm`.

*Proof.* The level of $Y$ has $l_A = 1$, so $l_A$ is coprime to $l_M$.

*Part 1.* An input lemma says that cusp forms are kept by level automorphisms when the data are uniformizations at good embeddings, the components have the same $\xi_0$ and $p_0$, the level automorphisms lie in the group of the dictionary, and the characters are trivial on the model weights. All these are fields of the good deep datum $Y$.

*The lattice.* The integral lattice consists of the forms whose values at all integral points have nonnegative valuation. An input lemma shows that translation by a level automorphism keeps this condition: it moves an integral point to an integral point. Pullback by $\gamma$ is translation by $\gamma^{-1}$.

*The norms.* The norm of a cusp form at $\sigma$ is a fixed positive factor times its Petersson norm at the good embedding attached to $\sigma$. The previous lemma, applied to $\gamma^{-1}$, shows that this Petersson norm is the same for $f$ and $g$. $\square$

**Remark 3.19.7 (Formalization).** In the last theorem the hypotheses $q \ge 1$ and $[E : \mathbb{Q}]/2 > 2$ are not used in the proof ([KeepsCuspLatticeNorm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeepsCuspLatticeNorm.lean#L204)); only $p \ge 1$ enters, through $p + q \ge 1$. The adelic probability measure is defined with a fixed choice of a Haar measure and a fundamental domain, and it falls back to a point mass when the volume is $0$ or $\infty$; the input lemmas show that this case does not occur for $W_j$ ([IsProbabilityMeasureAutQuotientNormalized.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsProbabilityMeasureAutQuotientNormalized.lean#L24)). The covolume of hermitian data uses a fundamental set at a fixed orthonormal frame chosen once ([FirstIndexEqOfUnfolded.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/FirstIndexEqOfUnfolded.lean#L89)). We have not unfolded the laws, the dictionary, the deep datum, the framed points, the valuations or the two unfolding lemmas. The second name is a wrapper.
