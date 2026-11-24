---
title: The Kodaira-Spencer identification off the boundary
decls:
  - GlobalTheory.CompHS.exists_local
  - GlobalTheory.CompHS.exists_regular_ksRel
  - GlobalTheory.T.exists_regular_kodairaSpencerCoordinate_affine_off_boundary
  - GlobalTheory.CompHS.canId_nonempty
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kodaira-Spencer identification off the boundary

On a smooth modification $M$ of a component of a flag cover, the canonical bundle $K_M$ and the pullback of the automorphic line bundle $L_0(\kappa_{\mathrm{can}})$ of the canonical weight agree off the boundary. This section constructs the identification. It is a nowhere vanishing section $\omega$ of $K_M \otimes L_0(\kappa_{\mathrm{can}})^{-1}$ over the part of $M$ that lies over the interior, normalized by the Kodaira-Spencer map at every point. The construction is local: in each chart the normalization determines the value of $\omega$ at every field point, and the local values glue. The result is used in [the covolume of the top lattice](/entry/top-covol-g-alt-alt/) ([Shimura varieties and toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)).

We use the moduli data of the previous section: a CM field $E$ with host data $H$, a datum $\mathcal{D}$, a level, a moduli space with coefficients in $F$, a model $Y$ over $F$, a flag cover $X$ of $Y$ and a component $Z$. Write $n$ for the dimension of the flag variety of $\mathcal{D}$.

**Definition 3.15.1 (Modification of a component).** A *modification* $M$ of the component of the flag cover at $Z$ is a scheme $M$ with a morphism $\pi$ to this component such that $M$ is smooth over $F$ of relative dimension $n$ and projective, $\pi$ is an isomorphism over the open interior $U_0$, and $\pi^{-1}(U_0)$ is dense. Write $M^\circ = \pi^{-1}(U_0)$ and $K_M$ for the canonical bundle of $M$.

**Definition 3.15.2 (Kodaira-Spencer normalization).** For a field $K$ over $F$, a *frame point* over $K$ is a point of the moduli space over $K$ with a frame of its de Rham cohomology adapted to the Hodge filtration. Let $P$ and $Q$ be frame points over $K$ and $t = (t_i)$ a family of units of $K$ such that $P$ is obtained from $Q$ by a Borel change with diagonal $t$. A *tangent frame* of $P$ is a family $v = (v_b)$ of frame points over the dual numbers $K[\varepsilon]$ that reduce to $P$ and whose Kodaira-Spencer classes form a basis of the tangent space, indexed by the tangent indices $b$ of the flag variety. A section $\omega$ of $K_M \otimes \pi^* L_0(\kappa_{\mathrm{can}})^{-1}$ over $M^\circ$ is *normalized* if for all such data, every $K$-point $z$ of $M^\circ$, every lift $z_v = (z_{v_b})$ of $v$ to $K[\varepsilon]$-points of $M$ through $z$, every chart of the flag cover at $z$ in which $Q$ is the chart frame, every chart of $K_M$ with frame $\omega_i$, and all functions $g_1, \dots, g_n$ on an open set of this chart that contains $z$,
$$\omega(z) \cdot \det\bigl[\partial_{z_{v_b}} g_a\bigr]_{a, b} = \prod_{i} t_i^{\kappa_{\mathrm{can}}(i)} \cdot J(g)(z).$$
Here $\partial_{z_{v_b}} g_a \in K$ is the $\varepsilon$-coefficient of $g_a$ at the point $z_{v_b}$, $J(g)$ is the Jacobian of $g$ with respect to $\omega_i$, so $dg_1 \wedge \dots \wedge dg_n = J(g)\,\omega_i$, and $\kappa_{\mathrm{can}}(i)$ is the exponent of the canonical weight at the diagonal index $i$.

**Definition 3.15.3 (Canonical identification).** A *canonical identification* on $M$ is a section $\omega$ of $K_M \otimes \pi^* L_0(\kappa_{\mathrm{can}})^{-1}$ over $M^\circ$ that is nowhere zero and normalized.

The normalization says that $\omega$ sends the top form $dg_1 \wedge \dots \wedge dg_n$ to the determinant of its values on a Kodaira-Spencer tangent frame, up to the character $t^{\kappa_{\mathrm{can}}}$ of the Borel change. If $\det[\partial g_a] \ne 0$, the relation determines $\omega(z)$. So a canonical identification is unique if it exists.

The construction uses two inputs. The first is a published result on abelian schemes.

**Definition 3.15.4 (de Rham theory of abelian schemes).** We assume the following properties of the de Rham cohomology of an abelian scheme over a base: it is locally free, the Hodge filtration is a filtration by locally free subsheaves with locally free quotients, it commutes with base change, it is rigid, and it satisfies duality. We do not unfold these statements.

The second input is the Kodaira-Spencer isomorphism at frame points: for every field $K$ over $F$ and every frame point $y$ over $K$, the first order deformations of $y$ correspond one to one, through the Kodaira-Spencer map, to the matrices of the tangent space of the flag variety. We take it as a hypothesis.

Fix a chart $i$ of $K_M$ and a chart $k$ of the flag cover. Let $O_{i k}$ be the intersection of $M^\circ$, the chart $i$ and the preimage of the chart $k$. The *Kodaira-Spencer relation* at a field point $z$ of $O_{ik}$ and $x \in K$ is the normalization relation with $x$ in place of $\omega(z)$, for all data as above.

**Lemma 3.15.5 (Local Kodaira-Spencer coordinate).** Assume the de Rham theory of abelian schemes and the Kodaira-Spencer isomorphism at frame points. Let $W \subset O_{ik}$ be open and $p \in W$. Then there are an open $W' \subset W$ with $p \in W'$ and a function $a$ on $W'$ such that $a(z)$ satisfies the Kodaira-Spencer relation at every field point $z$ of $W'$, and such that at every field point of $W'$ at most one value satisfies it.

Lean: `GlobalTheory.CompHS.exists_local`.

*Proof.* Since $M$ is smooth of dimension $n$, there are an open $V \ni p$ and functions $g_1, \dots, g_n$ on $V$ whose differentials form a frame of the cotangent bundle on $V$. Choose an affine open $W_1 \ni p$ inside $W \cap V$.

An input lemma on the Hodge-de Rham theory of the modification, which uses the de Rham theory of abelian schemes and the Kodaira-Spencer isomorphism, gives an open $W' \subset W_1$ with $p \in W'$ and derivations $e_H$ on $W'$ in the horizontal directions, which lift the Kodaira-Spencer tangent frame. A second input lemma, on lifts of vertical deformations of ring maps over affine sets, gives derivations $e_V$ in the vertical directions. Together $e = (e_H, e_V)$ is a family of $n$ derivations on $W'$.

Let $A = [e_b(g_a)]$. An input lemma on tangent lifts shows that $\det A$ is nonzero at every field point of $W'$. By the next lemma, $\det A$ is a unit on $W'$. Put
$$a = J(g) \cdot (\det A)^{-1}.$$
At a field point $z$, two input lemmas, one on the change of Borel frames and the canonical weight and one on the independence of the ratio of a determinant of derivatives and the Jacobian, show that $a(z)$ satisfies the Kodaira-Spencer relation for all data. If two values $x$ and $y$ satisfy it, then $x \det A(z) = y \det A(z)$ for the functions $g$, and $\det A(z) \ne 0$ gives $x = y$. $\square$

**Lemma 3.15.6 (Units from field points).** Let $Z$ be a scheme, $V \subset Z$ open, $a$ a function on $V$ and $y \in V$. If $a(z) \ne 0$ for every field point $z$ of $V$, then the germ of $a$ at $y$ is a unit.

*Proof.* Take an affine open $W \subset V$ that contains $y$, with $y$ given by the prime $\mathfrak{p}$. The residue field of $\mathfrak{p}$ gives a field point, at which the value of $a$ is the image of $a$ in the residue field. It is nonzero, so $a \notin \mathfrak{p}$, and $a$ is a unit in the localization at $\mathfrak{p}$, which is the stalk at $y$. $\square$

**Lemma 3.15.7 (Gluing by values at field points).** Let $Z$ be a reduced scheme, $V \subset Z$ open, and $R$ a relation between field points of $Z$ and elements of their fields. Assume that every $p \in V$ has an open neighbourhood $W \subset V$ with a function $a$ on $W$ such that $a(z)$ satisfies $R$ at every field point $z$ of $W$, and such that at every field point of $W$ at most one value satisfies $R$. Then there is a function $a$ on $V$ such that $a(z)$ satisfies $R$ at every field point $z$ of $V$.

*Proof.* On the intersection of two neighbourhoods the two local functions have the same value at every field point, by uniqueness. On a reduced scheme a function is determined by its values at field points, so they agree on the intersection. The sheaf property glues them to a function on $V$. A field point of $V$ lies in some neighbourhood $W$, and there the value is that of the local function. $\square$

**Theorem 3.15.8 (Regular Kodaira-Spencer coordinate).** Assume the de Rham theory of abelian schemes and the Kodaira-Spencer isomorphism at frame points. Let $W \subset O_{ik}$ be open. Then there is a function $a$ on $W$ such that $a(z)$ satisfies the Kodaira-Spencer relation at every field point $z$ of $W$.

Lean: `GlobalTheory.CompHS.exists_regular_ksRel` (also `GlobalTheory.T.exists_regular_kodairaSpencerCoordinate_affine_off_boundary`, a second name).

*Proof.* The scheme $M$ is smooth, hence reduced. Apply the gluing lemma on $W$ to the Kodaira-Spencer relation. The local functions and the uniqueness come from [the local Kodaira-Spencer coordinate](/entry/exists-local/). $\square$

**Theorem 3.15.9 (Kodaira-Spencer identification off the boundary).** Assume the de Rham theory of abelian schemes. Let $M$ be a modification of the component of the flag cover at $Z$. Assume the Kodaira-Spencer isomorphism at every frame point over every field $K$ over $F$. Then a canonical identification on $M$ exists.

Lean: `GlobalTheory.CompHS.canId_nonempty`.

*Proof.* The scheme $M$ is smooth over $F$, hence reduced.

*Local sections.* For each pair $(i, k)$ of charts, a uniqueness input says that on $O_{ik}$ the Kodaira-Spencer relation has at most one solution at each field point, and that this solution is nonzero. The gluing lemma, with the local functions of [the regular Kodaira-Spencer coordinate](/entry/exists-regular-ks-rel/) on affine opens of $O_{ik}$, gives a function $a_{ik}$ on $O_{ik}$ that satisfies the relation at every field point.

*Cover.* Every point of $M^\circ$ lies in a chart $i$ of $K_M$ and in the preimage of a chart $k$ of the flag cover, so the sets $O_{ik}$ cover $M^\circ$.

*Gluing.* On an overlap $O_{ik} \cap O_{i'k'}$ a transition input for Kodaira-Spencer coordinates in two charts shows that $a_{ik}$ and $a_{i'k'}$ are related by the transition functions of $K_M \otimes \pi^* L_0(\kappa_{\mathrm{can}})^{-1}$. It compares the values at field points, and the reducedness of $M$ turns this into an equality of germs. So the $a_{ik}$ are the local coordinates of a section $\omega$ over $M^\circ$.

*Nowhere zero.* At every field point the value of $a_{ik}$ is the solution of the relation, which is nonzero. By the lemma on units from field points, each germ of $a_{ik}$ is a unit, so $\omega$ is nowhere zero.

*Normalized.* A section is normalized exactly when its local coordinates satisfy the Kodaira-Spencer relation on each $O_{ik}$. This holds by construction. $\square$

**Remark 3.15.10 (Formalization).** The theorem on the regular coordinate assumes that $W$ is an affine open set, and its second name says "affine", but the proof does not use this hypothesis: the gluing lemma works on every open set ([ExistsRegularKodairaSpencerCoordinateAffineOffBo.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRegularKodairaSpencerCoordinateAffineOffBo.lean#L187)). We stated it without the hypothesis. The de Rham theory is a conjunction of five published properties; we have not unfolded them, nor the frame points, the Borel change, the tangent frames, the Kodaira-Spencer isomorphism or the inputs on Hodge-de Rham theory, vertical deformations, tangent lifts and transitions ([NonemptyKodairaSpencerIdentificationOffBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NonemptyKodairaSpencerIdentificationOffBoundary.lean#L41)). The lemma on units and the gluing lemma are auxiliary results of the development, `GlobalTheory.CompHS.isUnit_ger_of_ev` and `GlobalTheory.CompHS.glue_field_cover`. The second name is a wrapper.
