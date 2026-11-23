---
title: Galois descent of the line bundle
decls:
  - GlobalTheory.GaloisPackageDescent.exists_cp
  - GlobalTheory.T.uniformisation_lineBundle_descends_galois
  - GlobalTheory.Mum.unif_lb_descend_gal
  - GlobalTheory.Mum.LBGal.lemF
  - GlobalTheory.T.exists_galoisInvariant_local_frames_uniformisation
  - GlobalTheory.Mum.unif_lb_frames_gal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois descent of the line bundle

This section proves that the line bundle of a uniformisation descends along a finite Galois extension, together with its cubical and symmetric structures. The result is [the proposition on the descent of the line bundle](/entry/uniformisation-bundle-descends-along-galois-extension/) in [the section on Galois descent](/entry/has-of-galois-action/), which uses it to show that data with a Galois action on a uniformisation are realised. The proof is the classical descent of a line bundle by cocycles. We choose local frames of the line bundle upstairs, show that their ratios are fixed by the Galois group, and descend the ratios to units on the base. For Galois theory see [Galois theory](/learn/algebra/#galois-theory) in Volume 1.

### The situation

Throughout this section we fix the situation of [the section on Galois descent](/entry/has-of-galois-action/). So $R$ is a base with fraction field $K$, and $\rho : R \to R'$ is a finite extension that is Galois, with group $\operatorname{Gal}(\rho)$. Let $D$ be degeneration data over $R$ and $D'$ a pullback of $D$ along $\rho$. Let $A'$ be a polarised abelian variety over the fraction field of $R'$, $G'$ a commutative semi-abelian scheme over $R'$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $(a_\sigma)$ a Galois action on $U'$. Let $G$ be a commutative semi-abelian scheme over $R$, and let $\beta : G' \to G$ make $G'$ the group pullback of $G$ along $\rho$, with $\beta \circ a_\sigma = \beta$ for all $\sigma \in \operatorname{Gal}(\rho)$. We write $L'$ for the line bundle of $U'$ on $G'$.

We call this the *Galois situation*. In it, $G'$ is the base change of $G$ along $\operatorname{Spec} \rho$, and $a_\sigma$ is the action of $\sigma$ on this base change, up to the identification of $U'$ with its own pullback.

### Line bundles by cocycles

In this section a line bundle $L$ on a scheme $X$ is given by an open cover $(U_k)$ of $X$ and units $g_{k k'}$ on $U_k \cap U_{k'}$ with $g_{kk} = 1$ and $g_{k k'} g_{k' k''} = g_{k k''}$ on triple overlaps. An isomorphism $w : L \cong M$ of two such line bundles is a family of units on the overlaps of the two covers that is compatible with both cocycles. For a point $z$ in $U_k$ and a chart $j$ of $M$ at $z$ we write $w_{jk}(z)$ for the germ of this unit at $z$.

**Definition 4.13.1 (Frame).** Let $L = ((U_k), (g_{kk'}))$ be a line bundle on $X$ and $W \subseteq X$ an open subset. A *frame* of $L$ over $W$ is a family of units $T_k$ on $W \cap U_k$ such that $T_k = g_{k k'} T_{k'}$ on $W \cap U_k \cap U_{k'}$ for all $k, k'$.

Lean: `GlobalTheory.Mum.IsFrameOver`.

A frame over $W$ is a nowhere vanishing section of $L$ over $W$, written in the charts. So a frame over $W$ is the same as a trivialisation of $L|_W$. If $T$ and $T'$ are frames over $W$ and $W'$, the quotient $T'_k T_k^{-1}$ on $W \cap W' \cap U_k$ does not depend on $k$, since the factor $g_{kk'}$ cancels. It is a unit on $W \cap W'$, the *ratio* of the two frames.

**Definition 4.13.2 (Carried frame).** Let $L$ be a line bundle on $X$, let $f : X \to X$ be a morphism and $w : L \cong f^* L$ an isomorphism. A frame $T$ of $L$ over $W$ is *carried* by $(f, w)$ if the following holds for every point $z \in W$ with $f(z) \in W$ and all charts $k$ at $z$ and $j$ at $f(z)$: in the local ring of $X$ at $z$, the pullback along $f$ of the germ of $T_j$ at $f(z)$ is equal to $w_{jk}(z)$ times the germ of $T_k$ at $z$.

Lean: `GlobalTheory.Mum.FrameCarried`.

So a carried frame is a trivialisation of $L|_W$ that the isomorphism $w$ moves to its own pullback along $f$.

**Lemma 4.13.3 (Ratio of carried frames).** Let $L$ be a line bundle on $X$, $f : X \to X$ a morphism and $w : L \cong f^* L$ an isomorphism. Let $T$ and $T'$ be frames of $L$ over $W$ and $W'$, both carried by $(f, w)$. Let $O \subseteq W \cap W'$ be an open subset with $O \subseteq f^{-1}(O)$, and let $r$ be a unit on $O$ whose germ at every $z \in O \cap U_k$ is the germ of $T'_k T_k^{-1}$. Then $f^* r = r$ on $O$.

Lean: `GlobalTheory.Mum.FrameCarried.ratio_fixed`.

*Proof.* Two sections of the structure sheaf on $O$ are equal if their germs agree at every point of $O$. Let $z \in O$ and choose a chart $k$ at $z$ and a chart $j$ at $f(z)$. Then $f(z) \in O$, so the germ of $r$ at $f(z)$ is the germ of $T'_j T_j^{-1}$. Its pullback to $z$ is
$$
\frac{w_{jk}(z) \, T'_k}{w_{jk}(z) \, T_k} = \frac{T'_k}{T_k},
$$
which is the germ of $r$ at $z$. $\square$

The isomorphism $w$ is the same for both frames, and so it cancels in the ratio. This is the only point where the choice of $w$ enters.

### Invariant frames

**Proposition 4.13.4 (Invariant local frames).** In the Galois situation, there are, for each point $y$ of $G$, an open subset $V_y \subseteq G$ with $y \in V_y$ and a frame $T_y$ of $L'$ over $\beta^{-1}(V_y)$, with this property. Let $y, y'$ be points of $G$, and let $r$ be a unit on $\beta^{-1}(V_y \cap V_{y'})$ whose germ at every point $z$ in a chart $U_k$ of $L'$ is the germ of $T_{y', k} T_{y, k}^{-1}$. Then for every $\sigma \in \operatorname{Gal}(\rho)$ with $\beta^{-1}(V_y \cap V_{y'}) \subseteq a_\sigma^{-1} \beta^{-1}(V_y \cap V_{y'})$, we have $a_\sigma^* r = r$.

Lean: `GlobalTheory.Mum.unif_lb_frames_gal` (also `GlobalTheory.T.exists_galoisInvariant_local_frames_uniformisation` and `GlobalTheory.Mum.LBGal.lemF`, two more names).

*Proof.* *Step 1: carried frames at each point.* Let $y$ be a point of $G$. If $y$ lies over the closed point of $\operatorname{Spec} R$, an input on frames near the closed fibre applies. Otherwise an input on frames off the closed fibre applies. In both cases we get an open $V_y \ni y$ and a frame $T_y$ of $L'$ over $\beta^{-1}(V_y)$ with this property: for every $\sigma$, every way to make $D'$ a pullback of itself along $\sigma$, and every isomorphism of $G'$ with its base change along $\operatorname{Spec} \sigma$ whose composite with the projection is $a_\sigma$, if $U'$ is the pullback of $U'$ under these identifications, then $T_y$ is carried by $(a_\sigma, w_\sigma)$. Here $w_\sigma : L' \cong a_\sigma^* L'$ is the isomorphism of line bundles that comes with the pullback of $U'$.

*Step 2: invariance.* Let $y, y'$, $r$ and $\sigma$ be as in the statement. Condition 3 in the definition of a Galois action gives identifications of $D'$ and $G'$ with their pullbacks along $\sigma$ under which $U'$ is its own pullback. By Step 1, $T_y$ and $T_{y'}$ are both carried by $(a_\sigma, w_\sigma)$ for the same $w_\sigma$. The lemma on the ratio of carried frames, with $f = a_\sigma$, $W = \beta^{-1}(V_y)$, $W' = \beta^{-1}(V_{y'})$ and $O = \beta^{-1}(V_y \cap V_{y'})$, gives $a_\sigma^* r = r$. $\square$

The hypothesis on $\sigma$ holds for all $\sigma$, since $\beta \circ a_\sigma = \beta$. The statement keeps it because the pullback $a_\sigma^* r$ is formed with it.

### Descent of the line bundle

The descent uses one more input, on units. It is the statement that functions on $G$ are the invariant functions on $G'$.

**Theorem 4.13.5 (Invariant units descend).** Let $R$ be a base and $\rho : R \to R'$ a finite Galois extension. Let $G'$ be a group scheme over $R'$, $G$ a commutative semi-abelian scheme over $R$, $\beta : G' \to G$ a group pullback along $\rho$, and $(a_\sigma)$ a family of morphisms $G' \to G'$ such that each $a_\sigma$ is a group pullback along $\sigma$ and $\beta \circ a_\sigma = \beta$. Then for every open $O \subseteq G$, the pullback $\beta^* : \Gamma(O, \mathcal{O}_G) \to \Gamma(\beta^{-1} O, \mathcal{O}_{G'})$ is injective, and every unit $u$ on $\beta^{-1}(O)$ with $a_\sigma^* u = u$ for all $\sigma$ is $\beta^* g$ for a unit $g$ on $O$.

Lean: `GlobalTheory.Mum.LBGal.lemD`.

We take this theorem as given; it is proved elsewhere in the development. Over an affine open $O = \operatorname{Spec} B$ it says that $B \to B \otimes_R R'$ is injective with image the invariants of $\operatorname{Gal}(\rho)$, which follows from flatness of $B$ over $R$ and the equality $R = (R')^{\operatorname{Gal}(\rho)}$.

**Theorem 4.13.6 (Descent of the line bundle of a uniformisation).** In the Galois situation, there is a line bundle $L$ on $G$ with a generating isomorphism $L' \cong \beta^* L$.

Lean: `GlobalTheory.Mum.unif_lb_descend_gal` (also `GlobalTheory.T.uniformisation_lineBundle_descends_galois`, a second name).

*Proof.* *Step 1: frames.* The proposition on invariant local frames gives opens $V_y \ni y$ and frames $T_y$ of $L'$ over $\beta^{-1}(V_y)$. Each $T_y$ satisfies the frame relation also after pullback along any morphism $f : W \to G'$.

*Step 2: ratios.* For points $y, y'$ of $G$, let $r_{y y'}$ be the ratio of $T_y$ and $T_{y'}$: the unit on $\beta^{-1}(V_y \cap V_{y'})$ whose germ at a point of $U_k$ is the germ of $T_{y', k} T_{y, k}^{-1}$. It exists since $L'$ is a line bundle, so the local quotients glue.

*Step 3: invariance.* By the proposition, $a_\sigma^* r_{y y'} = r_{y y'}$ for every $\sigma$.

*Step 4: descent of the ratios.* By the theorem on invariant units, applied with $O = V_y \cap V_{y'}$ and the morphisms $a_\sigma$, there is a unit $g_{y y'}$ on $V_y \cap V_{y'}$ with $\beta^* g_{y y'} = r_{y y'}$.

*Step 5: the line bundle.* Let $L$ be given by the cover $(V_y)$ of $G$ and the units $g_{y y'}$. The cover covers $G$, since $y \in V_y$. Pulled back along $\beta$, the relations $g_{yy} = 1$ and $g_{y y'} g_{y' y''} = g_{y y''}$ become the relations for the ratios, which hold at every point. Since $\beta^*$ is injective on sections, they hold on $G$. So $L$ is a line bundle. The frames $T_y$ give an isomorphism $L' \cong \beta^* L$: on $\beta^{-1}(V_y) \cap U_k$ it is multiplication by $T_{y, k}$. It is a generating isomorphism, since its local units are the frames. $\square$

### The cubical symmetric line bundle

**Theorem 4.13.7 (Galois descent of the cubical symmetric line bundle).** In the Galois situation, there is a cubical symmetric line bundle $P$ on $G$ with a generating isomorphism $L' \cong \beta^* P$.

Lean: `GlobalTheory.GaloisPackageDescent.exists_cp`.

*Proof.* *Step 1: the line bundle.* The theorem on the descent of the line bundle gives a line bundle $L$ on $G$ with $L' \cong \beta^* L$.

*Step 2: rigidification.* The pullback of $L$ along the zero section of $G$ is a line bundle on $\operatorname{Spec} R$. Since $R$ is local, it has a generating section. This rigidifies $L$ along the zero section.

*Step 3: cubical structure.* The cubical structure of $L'$ descends: there is a cubical structure on the rigidified line bundle $L$. This is an input that we did not open. Its idea is that the isomorphism of the theorem of the cube for $L'$ is invariant under the Galois action, so it descends by the theorem on invariant units.

*Step 4: symmetry.* By a second input, the rigidified line bundle $L$ is symmetric.

*Step 5: the generic fibre.* By a third input, the polarised abelian variety $A'$ descends: there are a polarised abelian variety $A$ over $K$ and an isomorphism of group schemes from the generic fibre $G_K$ to $A$. The other parts of this input are not used.

*Step 6.* A rigidified symmetric line bundle on a commutative semi-abelian scheme over a noetherian domain, with a cubical structure, is a cubical symmetric line bundle, once the generic fibre is identified with an abelian variety. This result holds under the first five laws of the global theory. It gives $P$ with underlying rigidified line bundle $L$ and the cubical structure of Step 3. Then $L' \cong \beta^* L$ is the required isomorphism. $\square$

In this theorem the Galois group acts on $G'$ over the action on $\operatorname{Spec} R'$, so the descent is ordinary Galois descent for the cover $\operatorname{Spec} R' \to \operatorname{Spec} R$. The proof does not use effectivity of descent for quasi-coherent sheaves. It works with cocycles and with the descent of units only.

**Remark 4.13.8 (Formalization).** The three names for the proposition on invariant local frames are the same statement: `GlobalTheory.T.exists_galoisInvariant_local_frames_uniformisation` is a wrapper of the proof in [ExistsGaloisInvariantLocalFramesUniformisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGaloisInvariantLocalFramesUniformisation.lean#L15), and `GlobalTheory.Mum.LBGal.lemF` and `GlobalTheory.Mum.LBGal.lemD` ([UniformisationLineBundleDescendsGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisationLineBundleDescendsGalois.lean#L16)) are renamings of `GlobalTheory.T.exists_galoisInvariant_local_frames_uniformisation` and `GlobalTheory.T.galoisBaseChange_semiAbelian_invariant_units_descend`. The inputs of Step 1 of the proposition are `GlobalTheory.T.exists_carried_frame_near_closedFibre` and `GlobalTheory.T.exists_carried_frame_off_closedFibre`. In the theorem on the descent of the line bundle, Step 2 is `GlobalTheory.Mum.LBDesc.ratio` and the line bundle is `GlobalTheory.Mum.LBDesc.descLB` with isomorphism `GlobalTheory.Mum.LBDesc.descIso`. The proof repeats `GlobalTheory.Mum.LBDesc.lb_descend` ([ExistsLineBundleDescentBijectiveApp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLineBundleDescentBijectiveApp.lean#L168)) with injective in place of bijective maps on sections, and the helper lemmas `eq_of_gm_inj` and `isLB_descLB_inj` (lines 20 and 27) duplicate `eq_of_gm` and `isLB_descLB` (lines 98 and 107 of that file) in the same way. In the last theorem ([UniformisationBundleDescendsAlongGaloisExtension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisationBundleDescendsAlongGaloisExtension.lean#L20)), Steps 2 to 6 are `ReciprocityTheory.ChartRestriction.G.DVR.exists_gen_of_isLB_local`, `GlobalTheory.T.exists_cubicalStructure_descendedLineBundle`, `GlobalTheory.T.isSymmetric_of_galoisPullback_uniformisationBundle`, `GlobalTheory.T.polarised_generic_fibre_descends_galois` and `GlobalTheory.UU.exists_cp_of_isSymmetric`; outputs are discarded at lines 27, 28 and 29. We did not open the proofs of the carried frame inputs, of the theorem on invariant units, or of Steps 3 to 5, and the reasons given for them are sketches. A line bundle is the structure `LB` of cocycle data, and a generating isomorphism is `LBIso`.
