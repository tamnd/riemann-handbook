---
title: Theta families with smooth generic fibre
decls:
  - GlobalTheory.ZM.ThetaFamily.nonempty_thetaFam
  - GlobalTheory.T.nonempty_thetaObject_family_open_closure
  - GlobalTheory.ZM.exists_thetaFam_isPEL_smooth
  - GlobalTheory.T.exists_thetaFamily_pel_smooth_generic_fibre
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta families with smooth generic fibre

This section constructs the first moduli scheme of the chapter. We fix a class $\mathcal{C}$ of complex theta level objects and cut out, over an arithmetic base $o$, the scheme of theta values of the members of $\mathcal{C}$. Under a reduction criterion for theta values over complete discrete valuation rings, this scheme carries a universal theta level object, represents the objects whose points come from $\mathcal{C}$, and is infinitesimally rigid. For the class of PEL objects of a unitary datum it carries a PEL structure, and its generic fibre is smooth of relative dimension $\tfrac{[E:\mathbb{Q}]}{2} pq$, by [the tangent bound](/entry/finrank-derivation-le/). The family is the starting point of [the projective model of full level](/entry/top-amp-exists/).

Fix $g \ge 0$, a set $J$, an integer $N' \ge 1$ and a ring $o$ with a base $\zeta$ of level $N'^2$. Let $I = (\mathbb{Z}/N'^2)^{2g}$ be the set of labels of the $N'^2$-torsion.

**Definition 5.3.1 (Theta values).** Let $t$ be a theta level object of level $N'^2$ over $S$ and $x : \operatorname{Spec} R \to S$ a point. A family $v = (v_a)_{a \in I}$ in $R$ is a family of *theta values* of $t$ at $x$ if the values of the theta structure of level $N'$ of the polarization at the labelled points $P_a$, over $x$, are the $v_a$.

Lean: `GlobalTheory.ZM.TObj.HasTh`.

Over $\mathbb{C}$ the theta values play the part of the theta constants of the polarization at the points of the level structure, the classical projective coordinates of a point of the moduli space.

**Definition 5.3.2 (Coset condition and the theta ideal).** Let $n$ divide $N'$. A family $v \in R^I$ satisfies the *coset condition* at an ideal $\mathfrak{q} \subseteq R$ if each coset $a + \tfrac{N'}{n} I$ contains a label $b$ with $v_b \notin \mathfrak{q}$. Let $em : o \to \mathbb{C}$ be a ring map and $\mathcal{C}$ a class of theta level objects over $\operatorname{Spec} \mathbb{C}$, seen over $o$ through $em$. The *theta ideal* of $\mathcal{C}$ is the ideal of polynomials $F \in o[X_a : a \in I]$ with $F^{em}(v) = 0$ for every family $v$ of theta values of every member of $\mathcal{C}$. A family $v \in R^I$, over a ring map $\beta : o \to R$, is a *point of the theta scheme* if $F^\beta(v) = 0$ for all $F$ in the theta ideal and $v$ satisfies the coset condition at every prime ideal of $R$.

Lean: `GlobalTheory.ZM.Coset`, `GlobalTheory.ZM.thIdeal`, `GlobalTheory.ZM.InMM`.

The coset condition is an open condition: at a prime $\mathfrak{q}$, it says that $v$ is not zero modulo $\mathfrak{q}$ on any coset. It removes the boundary of the closure of the theta values, where the object degenerates.

**Definition 5.3.3 (Points from the class).** Let $t$ be a theta level object over $s : S \to \operatorname{Spec} o$. A point $x : \operatorname{Spec} K \to S$ with values in a field *comes from* $\mathcal{C}$ if there are a field $K_0$ with a map $\beta : o \to K_0$ and embeddings $K_0 \to K$ and $j : K_0 \to \mathbb{C}$ with $j \circ \beta = em$, a theta level object $t_0$ over $K_0$ with $x$ lying over $\operatorname{Spec} K_0$, such that the fibre of $t$ at $x$ and the base change of $t_0$ to $K$ are both pullbacks of one object, and the base change of $t_0$ to $\mathbb{C}$ is a member of $\mathcal{C}$. We write $S_\mathcal{C}$ for the set of points of $S$ that come from $\mathcal{C}$.

Lean: `GlobalTheory.ZM.FromC`, `GlobalTheory.ZM.fromSet`.

**Definition 5.3.4 (Shape and the unitary relations).** Let $w, w' \in J$. A theta level object satisfies the *unitary relations* for $(w, w')$ if $\alpha_w + \alpha_{w'} = 1$, the cubical line bundles of $(\alpha_w, 1)$ and $(1, \alpha_{w'})$ agree, and $L$ is isomorphic to the cubical line bundle of $(1, \alpha_w)$. Let $M_j$ ($j \in J$) be integer $2g \times 2g$ matrices and $\kappa \ge 1$. The object has *shape* $(M, \kappa)$ if, for each $j$, $\alpha_j(P_i)$ is the labelled point of the $i$-th column of $M_j$ modulo $N'^2$, and $L^{\kappa} \otimes \alpha_j^* L^{-1}$ is relatively ample.

Lean: `GlobalTheory.ZM.TObj.Prim`, `GlobalTheory.ZM.TObj.Shape`.

The unitary relations are those of $w_0$ and $\bar w_0 = 1 - w_0$ in a semi-abelian scheme with $\mathcal{O}_E$-action, from [the previous section](/entry/finrank-derivation-le/). The shape fixes the action of the endomorphisms on the level structure.

**Definition 5.3.5 (Good class).** A class $\mathcal{C}$ as above is *good of dimension* $d$ for $(M, \kappa, w, w')$ if:

1. it is closed under isomorphism;
2. each member has shape $(M, \kappa)$ and satisfies the unitary relations for $(w, w')$;
3. there are finitely many open preconnected sets $B_1, \dots, B_r \subseteq \mathbb{C}^d$ and holomorphic maps $\theta_i : B_i \to \mathbb{C}^I$ such that each $\theta_i(z)$ is a family of theta values of a member of $\mathcal{C}$, the set of $z' \in B_i$ with $\theta_i(z') \in \mathbb{C}\, \theta_i(z)$ is countable for each $z$, and every member of $\mathcal{C}$ has theta values $\theta_i(z)$ for some $i$ and $z$.

Lean: `GlobalTheory.ZM.GoodClass`.

Condition 3 says that $\mathcal{C}$ is parametrized by finitely many $d$-dimensional holomorphic families whose theta values are finite to one up to scaling. For the unitary class the $B_i$ are charts of the symmetric domain of the previous section.

**Definition 5.3.6 (Arithmetic base).** A ring map $em : o \to \mathbb{C}$ is an *arithmetic base* if $o$ is a [[Dedekind domain|7NPY2CN5KB]] of finite type over $\mathbb{Z}$ and $em$ is injective.

Lean: `GlobalTheory.ZM.ArBase`.

**Definition 5.3.7 (Theta family).** Let $n$ be a prime dividing $N'$ and $\mathcal{C}$ a class of complex theta level objects over $em$. A *theta family* for $\mathcal{C}$ is a scheme $s : \mathcal{M} \to \operatorname{Spec} o$ with a theta level object $t^{u}$ over $\mathcal{M}$ (the *universal object*) such that:

1. $s$ is quasi-projective and [[Flat|5M6KS8F47R]] and $\mathcal{M}$ is reduced;
2. the points of $\mathcal{M}$ that come from $\mathcal{C}$ are dense;
3. for every local ring $R$ and point $x \in \mathcal{M}(R)$ over $\beta : o \to R$, the object $t^u$ has theta values $v$ at $x$, and $v$ is a point of the theta scheme;
4. for every ring $R$ over $\beta$ and every point $v$ of the theta scheme with values in $R$, there is exactly one $x \in \mathcal{M}(R)$ over $\beta$ at which $t^u$ has theta values $v$;
5. for every reduced scheme $S$ over $o$ and every theta level object $t$ over $S$ whose points from $\mathcal{C}$ are dense, there is exactly one map $f : S \to \mathcal{M}$ over $o$ with a map $t \to t^u$ over $f$;
6. for every field $K$, every $x : \operatorname{Spec} K[\varepsilon] \to \mathcal{M}$ with the same image in $\operatorname{Spec} o$ as $\bar x$, and every object $t$ with maps $t \to t^u$ over $x$ and over $\bar x$, we have $x = \bar x$.

Lean: `GlobalTheory.ZM.ThetaFam`.

Conditions 3 and 4 say that $\mathcal{M}$ is the scheme of points of the theta scheme, through the theta values of $t^u$; condition 5 says that $\mathcal{M}$ is a fine moduli space for the reduced families whose points come from $\mathcal{C}$; condition 6 is infinitesimal rigidity over every field.

We use the following input on reduction. We call it the *reduction criterion*. For all $g$, $J$, $w, w' \in J$ and every odd prime $n$, there is $j_0$ such that for all $j \ge j_0$ the following holds, with $N' = n^j$. Let $o$ carry a base of level $N'^2$. Let $V$ be a complete [[discrete valuation ring|MGM3CNJW9V]] with finite residue field and fraction field $K$ of characteristic $0$, with a map $o \to V$. Let $t$ be a theta level object over $K$ that satisfies the unitary relations for $(w, w')$, with theta values $v \in V^I$ that satisfy the coset condition at the maximal ideal of $V$. Then there are a local map $V \to V'$ of discrete valuation rings, a compatible map $K \to K'$ of fraction fields, a theta level object $t'$ over $V'$ with theta values the images of $v$, and an object over $K'$ that is a pullback of both $t$ and $t'$. In words: after a finite extension, a theta level object with integral theta values that do not vanish on a coset has good reduction.

**Theorem 5.3.8 (Theta families exist).** Assume the laws, the second laws and the reduction criterion. Let $g \ge 0$, let $J$ be a finite set, let $M_j$ ($j \in J$) be integer matrices, $\kappa \ge 0$, $w, w' \in J$, and let $n$ be an odd prime. Then there is $j_0$ such that for all $j \ge j_0$, every ring $o$ with a base of level $(n^j)^2$, every arithmetic base $em : o \to \mathbb{C}$ and every class $\mathcal{C}$ of complex theta level objects of level $(n^j)^2$ that is good of some dimension $d$ for $(M, \kappa, w, w')$, there is a theta family for $\mathcal{C}$.

Lean: `GlobalTheory.ZM.ThetaFamily.nonempty_thetaFam` (also `GlobalTheory.T.nonempty_thetaObject_family_open_closure`, a second name).

*Proof.* Take $j$ larger than the bounds of the two lemmas below. Let $\mathcal{M}$ be the scheme of points of the theta scheme: the closed subscheme of the affine space $\mathbb{A}^I_o$ cut out by the theta ideal, intersected with the open set where the coset condition holds. The theta ideal is radical and homogeneous, since it is the ideal of a set of complex points stable under scaling by the theta values, so the scheme it defines is reduced. The first lemma uses the reduction criterion: for $j$ large it gives a scheme over $o$, quasi-projective, flat and reduced, with a theta level object $t^u$ whose theta values are the coordinates, whose points from $\mathcal{C}$ are dense, and which represents the points of the theta scheme. This gives conditions 1 to 4. The second lemma is the universal property of the theta ideal: a reduced family whose points from $\mathcal{C}$ are dense has theta values that satisfy every equation of the theta ideal, and their coordinates give the unique map to $\mathcal{M}$. This is condition 5. Condition 6 holds because a first-order deformation along which $t^u$ is constant has constant theta values, so its tangent vector in the coordinates is zero. $\square$

**Theorem 5.3.9 (PEL theta families with smooth generic fibre).** Assume the laws, the second laws, the reduction criterion, the theorem of the cube and the uniformization theorem. Let $E$ be a CM field with a host, $D$ a PEL datum with $p + q \ge 1$, $J$ a finite set with $a : J \to \mathcal{O}_E$, $w, w' \in J$ with $a(w) = w_0$ and $a(w') = \bar w_0$, the image of $a$ generating $\mathcal{O}_E$, and $\mathrm{bas}$ a symplectic basis of $\Lambda$ of size $2g$. Let $n$ be an odd prime. Then there is $j_0$ such that for all $j \ge j_0$, every ring $o$ with a base of level $(n^j)^2$, every arithmetic base $em : o \to \mathbb{C}$ and every $\rho \in o$ with $em(\rho) = \rho_0$, there are a theta family $\mathcal{M}$ for the class of complex theta level objects with a PEL structure for $(D, a, \mathrm{bas}, \rho)$, and a semi-abelian scheme $G$ with $\mathcal{O}_E$-action over $\mathcal{M}$ that is a PEL structure on the universal object, such that the generic fibre $\mathcal{M} \times_o \operatorname{Frac}(o)$ is smooth over $\operatorname{Frac}(o)$ of relative dimension $\tfrac{[E:\mathbb{Q}]}{2} pq$.

Lean: `GlobalTheory.ZM.exists_thetaFam_isPEL_smooth` (also `GlobalTheory.T.exists_thetaFamily_pel_smooth_generic_fibre`, a second name).

*Proof.* There are matrices $M$ and an integer $\kappa$ such that, for $j$ large, the class $\mathcal{C}$ of complex PEL objects is good of dimension $\tfrac{[E:\mathbb{Q}]}{2} pq$ for $(M, \kappa, w, w')$: the matrices record the action of the generators $a(j)$ on the symplectic basis, and the holomorphic families are the theta values over charts of the symmetric domain. [The existence theorem](/entry/nonempty-theta-fam/) gives a theta family $\mathcal{M}$ for $\mathcal{C}$. The universal object carries a PEL structure $G$: the action of $\mathcal{O}_E$ is generated by the $\alpha_j$, and the signature and Tate conditions hold at the dense set of points from $\mathcal{C}$ and spread to all points of characteristic $0$.

It remains to prove smoothness. Since the class is good of dimension $d = \tfrac{[E:\mathbb{Q}]}{2} pq$, every component of the generic fibre has dimension at least $d$, and the generic fibre is smooth of relative dimension $d$ as soon as every complex tangent space has dimension at most $d$. Let $\operatorname{Spec} R \to \mathcal{M}$ be an [[IsOpenImmersion|GFC5YKSN5H]] onto an affine open, with a complex point compatible with $em$. The universal object and $G$ pull back to $\operatorname{Spec} R$, and $G$ stays a PEL structure. Since $em$ is injective and $em(\rho)^2 = \rho_0^2 = -d$, we get $\rho^2 = -d$ in $o$. Since $\mathcal{M}$ is quasi-projective over $o$, $R$ is of finite type over $o$. The pulled back object is infinitesimally rigid: a deformation along which it is constant maps to a deformation of $\mathcal{M}$ along which $t^u$ is constant, which is zero by condition 6, and the chart is a monomorphism. So [the tangent bound](/entry/finrank-derivation-le/) gives $\dim_\mathbb{C} \operatorname{Der}_o(R, \mathbb{C}) \le d$. $\square$

**Remark 5.3.10 (Formalization).** The reduction criterion is a hypothesis of both theorems; in the proof of the chapter it is filled by `T.goodReduction_of_thetaPoint_units` (see [the section on the full level model](/entry/top-amp-exists-of-semistable-reduction/)). The theta values are the predicate `Out.IsThetaPt` and the cubical line bundles are `cubeLB`; neither was unfolded. In the unitary relations, $\alpha_w + \alpha_{w'} = 1$ is written `t.act w * t.act w' = 𝟙 t.A`, where `*` is the group law of the endomorphisms, that is the sum ([GoodClass.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/GoodClass.lean#L77)). The rigidity condition of a theta family is required over every field and needs the extra hypothesis that $x$ and $\bar x$ have the same image in $\operatorname{Spec} o$ ([GoodClass.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/GoodClass.lean#L108)). The proof of the first theorem runs through `T.exists_thetaFamily_over_thetaPointScheme`, `T.thetaIdealFamily_universal_property`, `T.thetaPointsVanishingIdeal_radical_homogeneous`, `ZM.nonempty_MMPre` and `T.tangentVector_zero_of_object_constant_along`; the second through `T.isGoodThetaComplexClass_unitaryFullLevel`, `thetaFam_isPEL`, `ThetaFam.smooth_genericFibre` and the helper `ThetaFam.unram_of_mono` ([ExistsThetaFamilyPelSmoothGenericFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaFamilyPelSmoothGenericFibre.lean#L24)). We followed the statements of these lemmas; the proofs above give their mathematical content as far as the statements show it. The line `have := hb.1` in [NonemptyThetaObjectFamilyOpenClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/NonemptyThetaObjectFamilyOpenClosure.lean#L28) only records that $o$ is a Dedekind domain.
