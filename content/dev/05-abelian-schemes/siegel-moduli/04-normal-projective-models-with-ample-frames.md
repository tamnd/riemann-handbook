---
title: Normal projective models with ample frames
decls:
  - GlobalTheory.Models.nonempty_zOn_of_components
  - GlobalTheory.T.generic_points_open_integral_cover
  - GlobalTheory.FamilyModel.nonempty_zOn_of_components
  - GlobalTheory.nonempty_zOn_thetaFam
  - GlobalTheory.T.nonempty_ampleFramedModel_PELThetaFamily
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normal projective models with ample frames

The theta family of [the previous section](/entry/exists-theta-fam-is-pel-smooth/) is quasi-projective, and its semi-abelian scheme is an abelian scheme. This section compactifies it: it gives a normal projective flat scheme $Z$ over the base, with a semi-abelian scheme with $\mathcal{O}_E$-action that extends the family on a dense open set, and with *ample frames*: an ample line bundle on $Z$ built from theta sections and frames of sections of a power of the theta bundle. The construction is local on the generic points: we first show that models over open neighbourhoods of the generic points glue, and then reduce the theta family to the case of one integral component. The result is used in [the projective model of full level](/entry/top-amp-exists/). The background is [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

Let $G \to Z$ be a semi-abelian scheme with a line bundle $L$ on $G$, and let $N \ge 1$. For a scheme $T$ over $Z$, sections of $L^N$ over $G_T$ are compared along maps $T' \to T$: a family $b_1, \dots, b_n$ is a *basis along* $T' \to T$ if every section of $L^N$ over $G_{T'}$ is $\sum_i c_i b_i$ for unique functions $c_i$ on $T'$.

**Definition 5.4.1 (Ample frames).** *Ample frames* of level $N$ for $(G, L)$ consist of:

1. a line bundle $\mathcal{A}$ on $Z$ such that every point of $Z$ lies in an affine set $Z_\sigma$, the nonvanishing locus of a section $\sigma$ of some $\mathcal{A}^d$ with $d \ge 1$;
2. an integer $n$ and, on each open set $U_i$ of a trivializing cover of $\mathcal{A}$, a section $\theta_i$ of $L$ over $G_{U_i}$ and sections $b_{i,1}, \dots, b_{i,n}$ of $L^N$ over $G_{U_i}$;
3. integers $r$ and $s$ such that on $U_i \cap U_j$ we have $\theta_i = c\, \theta_j$ for a unit $c$ and $b_i = M b_j$ for an invertible matrix $M$, and the transition function of $\mathcal{A}$ is $c^r \det(M)^s$;
4. for every complete discrete valuation ring $W$ and every map $\operatorname{Spec} W \to U_i$ whose generic point lands in the abelian locus of $G$, $\theta_i$ is a basis of the sections of $L$ and $b_i$ a basis of the sections of $L^N$ along $\operatorname{Spec} W$.

Lean: `GlobalTheory.LN.AmpFrames`, `GlobalTheory.LN.Lin`, `GlobalTheory.LN.BasisAlong`.

So $\mathcal{A} = \theta^{\otimes r} \otimes (\det b)^{\otimes s}$, glued from local theta sections and frames: it is the line bundle of modular forms of weight given by $(r, s)$ on the model, and condition 1 says it is ample. Condition 4 says that the frames do not degenerate over traits into the abelian locus.

**Definition 5.4.2 (Good semi-abelian scheme).** A semi-abelian scheme $G \to Z$ with line bundle $L$ is *good* if its abelian locus is open and $G$ is [[IsProper|9537RKBZPP]] over it; if at every point $z \in Z$, after a finite separable extension of the residue field, the fibre $G_z$ is a split extension of an abelian variety by a split torus; and if every point of $Z$ has a neighbourhood $V$ with sections of $L$ over $G_V$ that do not vanish simultaneously at any point of the fibres.

Lean: `GlobalTheory.Models.Good`, `GlobalTheory.Models.AbOpen`, `GlobalTheory.Models.SplitFib`, `GlobalTheory.Models.HasTheta`.

**Definition 5.4.3 (Framed model).** Let $O$ be a ring, $s_\mathcal{M} : \mathcal{M} \to \operatorname{Spec} O$ a scheme with a semi-abelian scheme $G_\mathcal{M}$ with $\mathcal{O}_E$-action, and $m \ge 1$. A *framed model* of level $m$ of $(\mathcal{M}, G_\mathcal{M})$ consists of a normal scheme $Z$, projective and flat over $O$, a good semi-abelian scheme $G$ with $\mathcal{O}_E$-action over $Z$ that is quasi-projective over $O$, a dense open $W \subseteq \mathcal{M}$ with a dominant open immersion $j : W \to Z$ over $O$, a semi-abelian scheme with $\mathcal{O}_E$-action over $W$ with maps to $G_\mathcal{M}$ (over the inclusion) and to $G$ (over $j$), and ample frames of level $m^2$ for $G$.

Lean: `GlobalTheory.Models.ZOn`.

**Theorem 5.4.4 (Gluing over generic points).** Assume the laws and the second laws. Let $O$ be a noetherian ring, $\mathcal{M}$ a reduced scheme, locally of finite type and quasi-compact over $O$, with a semi-abelian scheme $G_\mathcal{M}$ with $\mathcal{O}_E$-action that is smooth of some relative dimension and proper over $\mathcal{M}$, with relatively ample $L$ and trivial $K(L)$. Let $m \ge 1$. Assume that for every generic point $\xi$ of $\mathcal{M}$ there are an integral open neighbourhood $V$ of $\xi$, a semi-abelian scheme with $\mathcal{O}_E$-action over $V$ mapping to $G_\mathcal{M}$, and a framed model of level $m$ of $V$ with integral $Z$, with $s = 1$ in its frames, and such that for every $r$ at least the exponent $r$ of its frames there are ample frames of level $m^2$ with exponents $(r, 1)$. Then $(\mathcal{M}, G_\mathcal{M})$ has a framed model of level $m$.

Lean: `GlobalTheory.Models.nonempty_zOn_of_components` (also `GlobalTheory.T.generic_points_open_integral_cover`, a second name).

*Proof.* Since $\mathcal{M}$ is quasi-compact and locally of finite type over a noetherian ring, it is a noetherian space, so it has finitely many generic points $\xi_1, \dots, \xi_c$. Take the open immersions $V_i \to \mathcal{M}$ and the models $Z_i$ of the hypothesis, and let $r$ be an upper bound for the exponents $r_i$ of their frames. Every point $x$ of $V_i$ is a specialization of $\xi_i$, since $V_i$ is integral and its generic point maps to $\xi_i$. The images of the $V_i$ are pairwise disjoint: if $x$ lies in the images of $V_i$ and $V_j$, then $\xi_i$ specializes to $x$, which lies in the open image of $V_j$, so $\xi_i$ lies there too; then $\xi_i$ is a specialization of the generic point $\xi_j$, and two generic points with one specializing to the other are equal.

On each image, the hypothesis gives frames with exponents $(r, 1)$. The number of frame sections is the same for all $i$: since $G_\mathcal{M}$ is proper and smooth of relative dimension $g$, with $L$ relatively ample and $K(L)$ trivial, a basis of the sections of $L^{m^2}$ on its fibres has $\max(1, m^{2g})$ elements, by the laws and the second laws. Models on disjoint opens with the same rank and exponents glue, by taking the disjoint union of the $Z_i$ with the data that are the given ones on each piece. This gives a framed model of the union $U$ of the images, with $G_\mathcal{M}$ pulled back to $U$. Finally $U$ contains all generic points of $\mathcal{M}$, so it is dense, and a framed model of a dense open part of $\mathcal{M}$ is a framed model of $\mathcal{M}$, since the definition only asks for a dense open $W$. $\square$

To build the model of one component we use the following inputs. Let $V$ be a complete discrete valuation ring of characteristic $0$ with fraction field $K$.

1. *The uniformization of degenerations.* Let $A$ be a polarized abelian variety over $K$ and $G$ a commutative semi-abelian scheme over $V$ with an isomorphism $G_K \cong A$, whose special fibre becomes a split extension of an abelian variety by a split torus over the residue field. Then, under a condition on $(A, L)$ that we do not unfold, there are degeneration data and a uniformization of $A$ by them that induces the given isomorphism. This is Mumford's construction in the direction of [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).
2. *The torsion of degenerations.* For uniformized $A$, an algebraically closed field $F$ over $K$ and $k \ge 1$, the $k$-torsion of $A(F)$ is the set of classes of $k$-division points of the degeneration data, with the group law and the Weil pairing of the data.
3. *The geometric statement on theta systems.* A statement on theta systems over rational models of an arithmetic base, which produces models from lattices of theta functions. We do not unfold it here; it follows from the semistable reduction theorem by [the theorem in part two of this chapter](/entry/zarhin-geometric-of-semistable-reduction/).

**Theorem 5.4.5 (Semistable reduction).** Let $p$ be a prime, $K$ a finite extension of $\mathbb{Q}_p$ in an algebraic closure, and $A$ a polarized abelian variety over $K$. Then there are a finite extension $K' \supseteq K$ and a semi-abelian group scheme $G$ over the ring of integers $\mathcal{O}_{K'}$ whose generic fibre is $A \times_K K'$ as a group scheme (A. Grothendieck, SGA 7 I, Exposé IX, Théorème 3.6).

Lean: `GlobalTheory.Published.SemistableReductionSt`.

The theorem is proved in [another chapter](/entry/semistable-reduction-st/). Here it is an assumption.

Let $R_{N}$ be the subring $\mathbb{Z}[\tfrac{1 + \rho_0}{2}, \tfrac1n, \zeta_{N}]$ of $\mathbb{C}$, for an odd prime $n$ and $N$ a power of $n$; it contains $\rho_0 = 2 \cdot \tfrac{1 + \rho_0}{2} - 1$ and $\zeta_N = e^{2\pi i/N}$.

**Theorem 5.4.6 (Framed models from integral components).** Assume the laws, the second laws, the semistable reduction theorem and the three inputs above. Assume also the following statement on components. For every CM field $E$ with a host, every $g$ and every odd prime $n$, there are $k$ and $j_0$ such that for $j \ge j_0$: let $o \subseteq \Omega$ be an arithmetic base in a field of characteristic $0$, $R \subseteq \Omega$ a finitely generated $o$-algebra with fraction field $\Omega$, $u$ a theta level object of level $(n^j)^2$ over $R$ with theta values $v$, and $G_0$ a semi-abelian scheme with $\mathcal{O}_E$-action over $R$ with an isomorphism $G_0 \cong A_u$ that carries $L_{G_0}$ to $L_u$; if $\Omega$ is finite over the subfield generated by $o$ and the ratios $v_a / v_b$, then $(\operatorname{Spec} R, G_0)$ has a framed model of level $n^k$ with $Z$ integral, frames with $s = 1$, and frames with exponents $(r, 1)$ for every larger $r$.

Then, for every CM field $E$ with a host, every PEL datum $D$ with $p + q \ge 1$ and every odd prime $n$, there are $k$ and $j_0$ with the following property. Let $j \ge j_0$, $N' = n^j$, let $J$ be finite with $a : J \to \mathcal{O}_E$ whose image generates $\mathcal{O}_E$ and which takes the values $w_0$ and $\bar w_0$, let $\mathrm{bas}$ be a symplectic basis, and let $\zeta_{N'^2}$ be the base of level $N'^2$ on $R_{N'^2}$. Let $\mathcal{M}$ be a theta family over $R_{N'^2}$ for the class of PEL objects with $\rho = \rho_0$, with a PEL structure $G$ on its universal object, and with generic fibre smooth of relative dimension $\dim D$. Then $(\mathcal{M}, G)$ has a framed model of level $n^k$.

Lean: `GlobalTheory.FamilyModel.nonempty_zOn_of_components`.

*Proof.* Take $k$ and $j_0$ from the statement on components with $g = \tfrac12 \operatorname{rank}_\mathbb{Z} \Lambda$; this is the genus of the theta family, since the symplectic basis has $2g$ elements. The ring $R_{N'^2}$ is a Dedekind domain, of finite type over $\mathbb{Z}$, and noetherian, and $\mathcal{M}$ is reduced and quasi-projective over it, so locally of finite type and quasi-compact. Through the isomorphism of the PEL structure, $G$ is an abelian scheme, smooth of relative dimension $g$, proper, with relatively ample $L$ and trivial $K(L)$. So [the gluing theorem](/entry/models-nonempty-z-on-of-components/) applies, and we must produce a model near each generic point $\xi$.

The universal object has theta values $v$ on an affine neighbourhood of $\xi$, by condition 3 of a theta family. Inside this neighbourhood there is an integral affine chart $\operatorname{Spec} R \ni \xi$, with $R$ a finitely generated domain and $\Omega$ its fraction field. The map $R_{N'^2} \to \Omega$ is injective, and $\Omega$ has characteristic $0$, so $R_{N'^2} \subseteq \Omega$ is an arithmetic base. The theta values, the universal object and $G$ pull back to $R$. The field generated by $R_{N'^2}$ and the ratios $v_a / v_b$ is all of $\Omega$; this follows from the properties of a theta family, since by condition 4 the points of $\mathcal{M}$ are determined by their theta values. In particular $\Omega$ is finite over that field. So the statement on components applies and gives the model over $\operatorname{Spec} R$. $\square$

**Corollary 5.4.7 (Framed models of PEL theta families).** Assume the laws, the second laws, the semistable reduction theorem and the three inputs above. Then the conclusion of the previous theorem holds.

Lean: `GlobalTheory.nonempty_zOn_thetaFam` (also `GlobalTheory.T.nonempty_ampleFramedModel_PELThetaFamily`, a second name).

*Proof.* This is [the theorem on integral components](/entry/family-model-nonempty-z-on-of-components/) applied to the statement on components, which is proved from the same assumptions. $\square$

**Remark 5.4.8 (Formalization).** The inputs are `ThmUSt`, `UTorsSt` and `ZHGeoSt`; the condition `HypS`, the split extensions `SplitExt.IsGt`, the degeneration data `DegData` and the theta systems of `ZHGeoSt` were not unfolded. The statement on components is the first argument of `FamilyModel.nonempty_zOn_of_components`, and it is filled by `T.exists_model_triple_ampleFrames_component`, which we did not open. The proof of the theorem on integral components drops several hypotheses with `-`: the symplectic basis, the generation of $\mathcal{O}_E$, the elements $w, w'$, the base $\zeta = \zeta_{N'^2}$, the Tate part of the PEL structure and the smoothness of the generic fibre; the hypothesis $p + q \ge 1$ is also unused ([NonemptyZOnOfComponents.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/NonemptyZOnOfComponents.lean#L227)). The gluing theorem is in [GenericPointsOpenIntegralCover.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/GenericPointsOpenIntegralCover.lean#L449); its steps are `hasModel_rank`, `hasModel_sup`, `HasModel.sum` and `HasModel.grow`. The semistable reduction theorem in this form does not use the polarization of $A$ in its conclusion ([SemistableReductionSt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SemistableReduction₂/SemistableReductionSt.lean#L15)).
