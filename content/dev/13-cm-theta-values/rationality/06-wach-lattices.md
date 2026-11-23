---
title: Wach lattices from prismatic F-crystals
decls:
  - GlobalTheory.HWL.exists_hw_fon_cmp_ties
  - GlobalTheory.T.exists_hwOf_fonOf_cmpOf'
  - GlobalTheory.HWL.exists_hwOf_fonOf_cmpOf
  - GlobalTheory.T.exists_local_wach_functor
  - GlobalTheory.HWL.Assembly.exists_wach
  - GlobalTheory.T.wachLatticesExistAllLayers_of_bhattScholze
  - GlobalTheory.WachLattice.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Wach lattices from prismatic F-crystals

The integrality of Sections 1 to 3 is a statement about forms. To use it at a prime $l$ on the Galois side, the development needs the local objects that turn crystalline lattices into modules over power series rings: Wach modules, étale $(\varphi, \Gamma)$-modules, and a comparison between them and the period rings. This section builds them, at every prime and over every good tower of fields, from one published input: the theorem of Bhatt and Scholze that crystalline lattices are realized by prismatic F-crystals. See [lattices, Wach modules and prismatic F-crystals](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals), [period rings](/learn/galois-representations/#period-rings) and [crystalline representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations) in Volume 1.

### The local data

Fix a prime $l$. A *local datum* $P$ at $l$ consists of abstract period rings $B$ and $B_{\mathrm{dR}}$ with their Galois actions, Frobenius and filtration, for each finite extension $K$ of $\mathbb{Q}_l$. An *$A_{\mathrm{inf}}$ datum* over $P$ is a ring with the structure of $A_{\mathrm{inf}}$ and its maps to the period rings. The datum is *tied* if there are ring isomorphisms from $B$ to $B_{\mathrm{cris}}$ and from $B_{\mathrm{dR}}$ to the standard $B_{\mathrm{dR}}$, compatible with all this structure. A *local theory* is a choice of local datum at every prime.

A triple $(K, s, L')$ is *good* if $s \ge 1$, $s \ge 2$ when $l = 2$, $K$ lies in $K_0(\mu_{l^s})$, and $L'$ contains every conjugate of that field. Over a good triple, the construction has seven layers.

1. A group $\Gamma$ with its cyclotomic character $\chi$, and a generator $\gamma$ with $v(\chi(\gamma) - 1) = s$.
2. The ring $O[[X]]$ with Frobenius $\varphi(X) = (1 + X)^{l} - 1$ and an action of $\gamma$, and a ring $\mathcal{E}$ over it in which $\pi = X$ is a unit.
3. Maps of these rings into two rings $R_A$ and $R_W$; the first sends $\pi$ to $1 \otimes ([\varepsilon] - 1)$, and the map on $\mathcal{E}$ commutes with $\varphi$ and $\Gamma$.
4. The étale module functor $T \mapsto D(T)$: $D(T)$ is free of the rank of $T$, with an injective map $D(T) \to R_W \otimes T$ that respects $\varphi$ and the Galois action.
5. The *Wach lattice* $N(T) \subseteq D(T)$ of a crystalline lattice $T$.
6. Class maps from Herr cocycles of $D(T)$ to the cohomology of $T$.
7. The comparison of $N(T)$ with $V \otimes B$.

**Definition 3.6.1 (Wach lattice).** Let $E$ be an étale layer over a good triple. A *Wach lattice* for $E$ is a family of submodules $N(T) \subseteq D(T)$, one for each lattice $T$, with these properties. For crystalline $T$, the base change of $N(T)$ to $\mathcal{E}$ is $D(T)$. Each $N(T)$ is finitely generated and projective over $O[[X]]$. It is stable under $\Gamma$, and $\gamma x - x \in \pi N(T)$ for $x \in N(T)$. A power of $q = \varphi(\pi)/\pi$ (after $s - 1$ applications of $\varphi$) moves $\varphi(N(T))$ into $N(T)$, and moves $N(T)$ into the span of $\varphi(N(T))$. Morphisms of crystalline lattices map $N(T)$ into $N(T')$. For the trivial lattice, $N$ is spanned by the vector $1 \otimes e_0$. For $T$ not crystalline, $N(T) = 0$.

The datum *has Wach lattices* if every étale layer over every good triple, whose ring maps satisfy the fixed condition on Teichmüller lifts, has a Wach lattice.

These are the conditions of Wach and Berger on the lattice $N(T)$ of a crystalline representation with nonnegative Hodge-Tate weights.

### The Bhatt-Scholze input

**Theorem 3.6.2 (Bhatt-Scholze).** Let $K$ be a finite extension of $\mathbb{Q}_l$ with ring of integers $O_K$. For every crystalline $\mathbb{Z}_l$-lattice $T$ of $G_K$ there is a prismatic F-crystal on $O_K$ whose étale realization is $T$. Every morphism of lattices lifts uniquely to the F-crystals.

The development states this for every $A_{\mathrm{inf}}$ prism of $O_K$, and as the realization of the value at the prism inside $W(\mathcal{O}_{\mathbb{C}_l^\flat}) \otimes T$. It is used as a published input.

**Theorem 3.6.3 (Wach lattices from F-crystals).** Assume the theorem of Bhatt and Scholze. Then every tied $A_{\mathrm{inf}}$ datum at every prime has Wach lattices.

Lean: `GlobalTheory.WachLattice.main` (also `GlobalTheory.T.wachLatticesExistAllLayers_of_bhattScholze`, a second name).

*Proof.* Fix a good triple and an étale layer $E$. The development builds a prism $P_S$ over $\mathbb{Z}_l[[X]]$: a local ring $A_S$ with a principal ideal $(Q)$, an injective map $a$ of $A_S$ into the power series ring of the layer with $a(\pi_S) = \pi$ and $a(Q) = q$, a map of prisms from $P_S$ to the $A_{\mathrm{inf}}$ prism, and an action of the Galois group that $a$ carries to the action of $\gamma$. The map from the layer into $R_W$ is injective, and it reflects units.

Let $T$ be a crystalline lattice. Bhatt and Scholze give an F-crystal $C$ and a realization $j$ of $C$ at the $A_{\mathrm{inf}}$ prism. Move $C$ to $P_S$ and compose with $j$ and with the identification $\kappa$ of $W(\mathcal{O}_{\mathbb{C}_l^\flat}) \otimes T$ with $R_W \otimes T$. This gives a map $\nu$ from the value $C(P_S)$ into $R_W \otimes T$, semilinear over $A_S$. The value of an F-crystal at a prism is free, with a basis $b$, and the development gives three facts on it. A power of $Q$ times the Frobenius of an element is in the image. A power of $Q$ times an element is in the span of the Frobenius images of the basis. The Galois action is compatible with $\nu$.

So the images $\nu(b_i)$ form a basis of $R_W \otimes T$ over $R_W$, whose Frobenius matrix $A$ is invertible over $\mathcal{E}$. The images are fixed by the kernel of the cyclotomic character. A vector system with these two properties lies in the image of $D(T)$; this is a property of the étale layer. So the $\nu(b_i)$ are the images of vectors $x_i \in D(T)$. Put $N(T) = \sum_i O[[X]]\,x_i$ for crystalline $T$, and $N(T) = 0$ otherwise. The three facts give the conditions on $\varphi$ and on $\Gamma$. The functor property follows from the uniqueness of the lifts of morphisms. For the trivial lattice, the image is spanned by $1 \otimes e_0$, by the realization of the trivial F-crystal. $\square$

### Assembly at one prime and at all primes

**Theorem 3.6.4 (Local Wach construction).** Let $P$ be a local datum at $l$ and $A$ an $A_{\mathrm{inf}}$ datum over it. Assume that $A$ is tied, that $A$ is faithful on the tilt (an element of $G_{\mathbb{Q}_l}$ in the cyclotomic kernel that fixes the right elements of the tilt lies in $G_K$), and that $A$ has Wach lattices. Then there are Wach modules $H$ over every good triple, étale modules $F$ over the same triples, and a comparison between them.

Lean: `GlobalTheory.HWL.Assembly.exists_wach` (also `GlobalTheory.T.exists_local_wach_functor`, a second name).

*Proof.* Tied data give two facts in $B_{\mathrm{dR}}$: the element $\mu - t$ lies in $\mathrm{Fil}^2$, and $\pi_1$ has an inverse in $\mathrm{Fil}^0$. With these facts, the construction reduces to one record of seven layers for each good triple. Fill the record in order. The layers $\Gamma$, the power series ring and the maps into $R_A$ and $R_W$ exist for every good triple. The étale functor needs a basis of $R_W \otimes T$ that is fixed by the cyclotomic kernel; faithfulness on the tilt gives it. The Wach lattice is the hypothesis. The class maps exist for every étale layer. The comparison uses the tied datum and the Wach lattice. $\square$

**Theorem 3.6.5 (Wach construction at all primes).** Let $L$ be a local theory and $A$ an $A_{\mathrm{inf}}$ datum at each prime. If $A$ is tied and has Wach lattices at every prime, then there are, as functions of $l$, Wach modules $H$, étale modules $F$ and a comparison between them.

Lean: `GlobalTheory.HWL.exists_hwOf_fonOf_cmpOf` (also `GlobalTheory.T.exists_hwOf_fonOf_cmpOf'`, a second name).

*Proof.* Every $A_{\mathrm{inf}}$ datum is faithful on the tilt. Apply [the local construction](/entry/exists-wach/) at each prime, and choose the objects as functions of $l$. $\square$

**Theorem 3.6.6 (Wach construction from Bhatt-Scholze).** Assume the theorem of Bhatt and Scholze. Let $L$ be a local theory and $A$ a tied $A_{\mathrm{inf}}$ datum at each prime. Then there are Wach modules $H$, étale modules $F$, a comparison between them, and at each prime a map $\theta : B_{\mathrm{dR}} \to \mathbb{C}_l$ that is a ring map on $\mathrm{Fil}^0$, onto, Galois equivariant, with kernel $\mathrm{Fil}^1$.

Lean: `GlobalTheory.HWL.exists_hw_fon_cmp_ties`

*Proof.* By [the theorem on Wach lattices](/entry/wach-lattice-main/), each $A_l$ has Wach lattices. [The construction at all primes](/entry/exists-hw-of-fon-of-cmp-of/) gives $H$, $F$ and the comparison. The map $\theta$ exists at each tied prime. $\square$

**Remark 3.6.7 (Formalization).** The construction of $N(T)$ is `build_prism` in [WachLatticesExistAllLayersOfBhattScholze.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticesExistAllLayersOfBhattScholze.lean#L26). It takes about thirty hypotheses, which `WachLattice.main` (line 175) supplies from `T.exists_wach_prism_over_integers`, `T.wachInclusion_injective_saturated_inter` and `T.witt_twist_invariant_basis_change`; both theorems set `maxHeartbeats` to 2000000. The published input is `BhattScholzeCrystallineLattices` ([BhattScholzeCrystallineLattices.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeCrystallineLattices.lean#L12)). The hypothesis `WachEx` is in [ConvZero.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ConvZero.lean#L29). The Wach layer `WN` has a field `N_junk` ([ExistsOfLayers.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsOfLayers.lean#L176)): $N(T) = 0$ for $T$ not crystalline, so $N$ is a total function with a junk value. The local assembly is [ExistsLocalWachFunctor.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLocalWachFunctor.lean#L16); its Wach layer is the hypothesis `WachEx`, passed through at line 25. The family over all primes is [ExistsHwOfFonOfCmpOf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwOfFonOfCmpOf.lean#L10), where `FaithH` comes from `cyclotomicKernel_tilt_invariants_faithful`. The last theorem is [ExistsHwFonCmpTies.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwFonCmpTies.lean#L13). Its last conjunct is `Ties` ([LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L525)), whose one field is the map $\theta$ at each prime; it does not involve $H$ or $F$, so this part of the conclusion says nothing about the objects that the theorem builds. The proof picks it with `Classical.choice` from `T.nonempty_theta_deRhamFil_zero_concretePeriod`. We have not unfolded `WCl`, `WCmp`, `LocCmpT` or the record `Layers`.
