---
title: Normal Hecke correspondences and good models
decls:
  - UpperTheory.Gal.crystallineComparison.Mod.esNorm_of
  - UpperTheory.Gal.crystallineComparison.Mod.esNorm_link
  - UpperTheory.Gal.crystallineComparison.Mod.quotObj_link
  - UpperTheory.Gal.G3.kSEx_holds
  - UpperTheory.Gal.FiniteEtaleModels.ksGood_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normal Hecke correspondences and good models

Sections 10 and 11 used Hecke correspondences of type $j$ on the integral models $M$, and Section 12 listed six facts on the Kuga-Sato tower. This section proves three of the inputs behind them. First, a Hecke correspondence that is given only where $p$ is invertible extends to a finite normal correspondence over the whole model. Second, the Kuga-Sato tower of each power exists over every field of characteristic $0$. Third, at a place $w$ where the eigensystem satisfies the group conditions for good reduction, the Hecke tower of a Kuga-Sato tower has a good model over the valuation ring of $w$. Items 2 and 4 of Theorem 3.12.7 are the last two results.

We keep the notation of Sections 08 to 11. So $p$ is a prime, $F$ the field of the moduli data with ring of integers $\mathcal{O}_F$, $\mathfrak{u}_r = (p, \omega - r)$, and a model $M$ of level $N$ over a ring $R$ carries a universal object. For a scheme $M$ over $R$, write $M[1/p]$ for the open subscheme where $p$ is invertible. An *isogeny datum of type $j$ and factor $c$* over a scheme $Y$ is a pair of objects $o, o'$ over $Y$ with a map $\psi : A_o \to A_{o'}$ that satisfies conditions 2, 3 and 4 of Definition 3.10.5: $\psi$ is a $p$-isogeny of factor $c$, its kernel has the type $j$ at $w$, and it is universal over schemes on which $p$ is invertible.

### Normal models of Hecke correspondences

Fix the following data, which we call *admissible data for a Hecke correspondence*: $R$ a discrete valuation ring of characteristic $0$ with $p \in \mathfrak{m}_R$, a base over $R$, $N \geq 3$ prime to $p$, $m = 1$, an integer $r$, a maximal ideal $w$ of $\mathcal{O}_F$ with $\mathfrak{u}_r \subseteq w$, an integer $0 \le j \le n$, and $c = p^e$ with $e > 0$ when $j > 0$.

**Definition 3.13.1 (generic and normal Hecke correspondences).** Let $M$ be a model of level $N$ over $R$, with admissible data as above.

1. A *generic Hecke correspondence* of type $j$ and factor $c$ on $M$ is a scheme $Y_0$ with maps $s_0, t_0 : Y_0 \to M$ that factor through $M[1/p]$ by finite étale maps, together with an isogeny datum $(o_0, o_0', \psi_0)$ of type $j$ and factor $c$ over $Y_0$, with $o_0$ and $o_0'$ the pullbacks of the universal object along $s_0$ and $t_0$.
2. A *normal Hecke correspondence* of type $j$ and factor $c$ on $M$ is a scheme $Y$, flat over $R$, whose local rings are integrally closed domains, with finite maps $s, t : Y \to M$ over $R$ and an isogeny datum $(o, o', \psi)$ of type $j$ and factor $c$ over $Y$, with $o$ and $o'$ the pullbacks of the universal object along $s$ and $t$.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.EsGen`, `UpperTheory.Gal.crystallineComparison.Mod.EsNorm`.

The normal version is what Section 11 and the good models below need: a finite correspondence over the integral model whose legs agree over $R$. We take the generic version as given, from [the theorem on Hecke correspondences on integral models](/entry/exists-hecke-correspondence-on-integral-shimura-model/).

**Theorem 3.13.2 (normal models of Hecke correspondences).** Suppose that for all admissible data every model $M$ of level $N$ over $R$ has a generic Hecke correspondence of type $j$ and factor $c$. Then for the same data every such $M$ has a normal Hecke correspondence of type $j$ and factor $c$.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.esNorm_of`.

*Proof.* Let $(Y_0, s_0, t_0, o_0, o_0', \psi_0)$ be a generic correspondence on $M$. The model $M$ is of finite type over the Noetherian ring $R$, and $s_0$ is finite over $M[1/p]$. Let $Y$ be the normalization of $M$ in $Y_0$, that is, the relative spectrum over $M$ of the integral closure of $\mathcal{O}_M$ in $s_{0*}\mathcal{O}_{Y_0}$. Since $M$ is excellent, $s : Y \to M$ is finite, $Y$ is Noetherian and normal, and there is an open immersion $i : Y_0 \to Y$ with $s \circ i = s_0$. The scheme $Y$ has no component in the special fibre, because each generic point of $Y$ lies in $Y_0$, so $Y$ is flat over the discrete valuation ring $R$.

The map $t_0$ extends to $t : Y \to M$ with $t \circ i = t_0$. To see this, note that $Y_0$ is dense in $Y$ and $t_0$ is finite over $M[1/p]$, so the closure of the graph of $t_0$ in $Y \times_R M$ is finite over $Y$; it maps isomorphically to $Y$ because $Y$ is normal and the map is birational. The scheme $Y$ is reduced, since it is normal and its generic fibre $Y_0$ is reduced, and its local rings are domains.

Put $o = s^* \mathcal{U}$ and $o' = t^* \mathcal{U}$, with $\mathcal{U}$ the universal object; then $i^* o = o_0$ and $i^* o' = o_0'$. The isogeny $\psi_0$ is a map of abelian schemes over the dense open $Y_0$ of the normal scheme $Y$, so it extends uniquely to $\psi : A_o \to A_{o'}$, and so does its quasi-inverse $\psi_0'$ with $\psi_0 \psi_0' = c$ and $\psi_0' \psi_0 = c$. Linearity, the level structure and the polarization condition are equalities of maps that hold on $Y_0$, so they hold on $Y$. This gives condition 2 of Definition 3.10.5.

Condition 3 concerns geometric points of characteristic $0$. Each such point of $Y$ lies over $R[1/p]$ and so in $Y_0$, and the condition holds there for $\psi_0$. Condition 4 concerns schemes $T$ on which $p$ is invertible. A map $T \to Y$ from such a scheme factors uniquely through the open immersion $i$, so universality for $(Y_0, \psi_0)$ gives universality for $(Y, \psi)$. $\square$

**Corollary 3.13.3 (normal Hecke correspondences exist).** For all admissible data, every model $M$ of level $N$ over $R$ has a normal Hecke correspondence of type $j$ and factor $c$.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.esNorm_link`.

*Proof.* This is [Theorem 3.13.2](/entry/es-norm-of/) applied to [the theorem on Hecke correspondences on integral models](/entry/exists-hecke-correspondence-on-integral-shimura-model/). $\square$

With universality, the next theorem says that the points of a Hecke correspondence over a scheme where $p$ is invertible are the subgroups of the right type.

**Theorem 3.13.4 (quotients by subgroup schemes).** Let $R$ be a ring with a base, $N \geq 3$ prime to $p$, $m = 1$, $r$ an integer, $w$ a maximal ideal of $\mathcal{O}_F$ with $\mathfrak{u}_r \subseteq w$, $0 \le j \le n$, and $c = p^e$ with $e > 0$ when $j > 0$. Let $S$ be a locally Noetherian scheme over $R$ on which $p$ is a unit, $o$ an object of level $N$ over $S$, and $K \subseteq A_o$ a finite étale subgroup scheme, stable under $\mathcal{O}$, killed by $w$, of degree $N(w)^j$. Then there are an object $o'$ over $S$ and a $p$-isogeny $\psi : A_o \to A_{o'}$ of factor $c$ with kernel of type $j$ at $w$, such that the part of $\ker \psi$ killed by a power of $\mathfrak{u}_r$ is $K$.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.quotObj_link`.

*Proof.* This is [the theorem on quotients by subgroup schemes](/entry/exists-p-isogeny-kernel-eq-subgroup-scheme/). $\square$

### The Kuga-Sato tower over a field of characteristic zero

Recall the Kuga-Sato tower of power $k$ from Section 09 and the standard range from Section 12.

For an integral element $h$ of the finite adelic group and levels $N', N$, a *witness* for $h$ from level $N'$ to level $N$ is a map $\pi : M_{N'} \to M_N$ of generic models over $R$ with a map $\Phi$ of the universal abelian schemes over $\pi$, such that $\Phi$ is an isogeny followed by a pullback square, and the isogeny moves the level structure of level $N'$ to that of level $N$ by the action of $h$ on the lattice. A witness for $h = 1$ is a change of level.

**Theorem 3.13.5 (existence of Kuga-Sato towers).** Suppose the data are in the standard range. Then for every field $R$ of characteristic $0$, every base over $R$ and every $k \ge 0$, there is a Kuga-Sato tower of power $k$ over $R$.

Lean: `UpperTheory.Gal.G3.kSEx_holds`.

*Proof.* Fix a generic model $M_N$ over $R$ for each level $N$ (Section 08), and a witness $(\pi_h, \Phi_h)$ for each $h$ admitted from $N'$ to $N$; witnesses exist for all such $h$. Put $Z_N = A_N^{\times k}$, the $k$-th fibre power of the universal abelian scheme over $M_N$, and let $\operatorname{tr}_h$ be the $k$-th fibre power of $\Phi_h$ over $\pi_h$. The axioms of a tower follow from these facts on witnesses.

1. *Uniqueness.* Two witnesses for the same admitted $h$ are equal. So $\operatorname{tr}_h$ does not depend on choices.
2. *Composition.* The identity is a witness for each $u \in K_{N'}$, and composites of witnesses for $h$ and $h'$ are witnesses for $h'h$. So $\operatorname{tr}_{h'h} = \operatorname{tr}_{h'} \circ \operatorname{tr}_h$ and $\operatorname{tr}_u = \mathrm{id}$.
3. *Cartesian squares.* For $u \in K_1$, $\Phi$ is a pullback of $A_N$ along $\pi$, so the fibre power map is a pullback of $Z_N \to M_N$.
4. *Change of level.* A witness for $1$ has $\pi$ finite, étale and surjective. With the last item, the transition $Z_{N'} \to Z_N$ is finite étale of degree $[K_N : K_{N'}]$.
5. *Fibres.* If two geometric points $x, y$ of $M_{N'}$ have the same image under a change of level to $N$, then $y = \pi'(x)$ for the witness $\pi'$ of some $u \in K_N$, and $\Phi'$ commutes with $\Phi$ on the fibre at $x$. If a witness for $u \in K_N$ fixes a geometric point and $K_{N'} \subseteq K_N$, then $u \in K_{N'}$.

So $K_N / K_{N'}$ acts simply transitively on the geometric fibres of a change of level. The group axioms hold since each element of $K_1$ is admitted at every level, every $g$ is admitted from $Nc$ to $N$ for some $c$ prime to $p$, and the indices $[K_M : K_N]$ are finite and nonzero. $\square$

### Good models at good places

Let $E$ be a number field with an isomorphism $e : F \cong E$, and let the base be the standard base for $e$ (Section 12). A finite place $w$ of $E$ *lies over* the prime $\mathfrak{w}$ of $F$ if $e$ matches $\mathcal{O}_F$-elements in $\mathfrak{w}$ with $\mathcal{O}_E$-elements in $w$. Let $O_w$ be the valuation ring of $w$ in $E$. Let $H$ be the Hecke tower of a Kuga-Sato tower $T$ at a level $N$ for members $g_j$ of the Hecke algebra, with eigenvalues $\theta_j$, as in Section 05.

**Definition 3.13.6 (good model).** A *good model* of $(H, \theta)$ at $w$ is a smooth projective scheme $Y$ over $O_w$ with a map $\pi : Z_N \to Y$ over $\operatorname{Spec} E \to \operatorname{Spec} O_w$ such that the induced map $Z_N \to Y_E$ is finite étale, together with a finite group $\Delta$ acting on $Z_N$ that splits this map, such that for each $j$ the correspondence of $g_j$ lies over a finite étale correspondence $(s, t)$ on $Y$ over $O_w$, with $s$ of some degree $d$ and with $s$ and $t$ agreeing on $O_w$. The model is *onto* if $Z_N \to Y_E$ is also surjective.

Lean: `UpperTheory.Gal.Int.Geo.GoodAtW`.

Onto good models are the good models of Section 05.

**Definition 3.13.7 (group conditions for good reduction).** The eigensystem $(g, \theta)$ satisfies the *group conditions for good reduction at* $\mathfrak{w}$ if there are a prime $q$ and an integer $r$ with $\mathfrak{w}$ the prime of $F$ above $q$ cut out by $r$, a level $N_0 \mathfrak{a}$ adapted to $(q, r, \mathfrak{w})$ with level group $K_0 \supseteq K_N$ and $N \in N_0 \mathfrak{a}$, such that:

1. every $k \in K_0$ is the element of some $g_j$ at level $N$ with $\theta_j = 1$;
2. for each $j$, the element of $g_j$ is a product $h_1 h_2$ of integral elements, where the image of the lattice under $h_2$ contains $c$ times the lattice for an integer $c$, and $h_1$ is either $1$ or an element of type $i$ at a maximal ideal $\mathfrak{w}'$ with $\mathfrak{u}_r \subseteq \mathfrak{w}'$ and $N(\mathfrak{w}')^i$ dividing an intermediate level $N_1$;
3. the conjugations by $h_2 k$ and by $h_1$ carry the level groups at the levels of $g_j$ into those of $N_1$ and of $N$, and the intermediate levels lie in a level $N_0 c\, \mathfrak{a}'$ with $\mathfrak{a}' \subseteq \mathfrak{a}$.

Lean: `UpperTheory.Gal.Int.Geo.GoodGrp`.

Condition 2 makes each Hecke operator a scalar followed by a Hecke correspondence of type $i$, which the normal correspondences above model.

**Theorem 3.13.8 (good models at good places).** Suppose the data are in the standard range. Let $E$ be a number field, $e : F \cong E$ with the standard base, $T$ a Kuga-Sato tower of power $k$ over $E$, $N$ a level, and $(g_j, \theta_j)$ an eigensystem. Let $w$ be a place of $E$ over the prime $\mathfrak{w}$ of $F$, and suppose that $(g, \theta)$ satisfies the group conditions for good reduction at $\mathfrak{w}$. Then the Hecke tower of $(T, N, g)$ with $\theta$ has a good model at $w$.

Lean: `UpperTheory.Gal.FiniteEtaleModels.ksGood_holds`.

*Proof.* Take $q$, $r$, $N_0$, $\mathfrak{a}$ and $K_0$ from the group conditions. Over $O_w$ there is an étale level model of level $N_0 \mathfrak{a}$ by Theorem 3.11.5, items 4 and 5. The Kuga-Sato variety $Y$ over it is smooth and projective, and since $K_N \subseteq K_0$ and $N \in N_0 \mathfrak{a}$ it receives a finite étale map $\pi$ from $Z_N$, split by a finite group $\Delta$.

Fix $j$ with $g_j = h_1 h_2$ as in condition 2, and take an étale level model $X_1$ of level $N_0 c\, \mathfrak{a}'$ over $O_w$. The element $h_2$ gives a finite étale correspondence from $X_1$ to an intermediate model. If $h_1 \neq 1$, the [normal Hecke correspondence](/entry/es-norm-link/) of type $i$ at $\mathfrak{w}'$, pulled back to the étale level models, gives a finite correspondence for $h_1$. It is étale, since it has $\#\mathrm{Gr}_i((\mathcal{O}_F/\mathfrak{w}')^n)$ points on each geometric fibre by Theorem 3.11.5, item 7, which is its degree. The composite is a finite étale correspondence of $Y$ for $h_1 h_2$, and condition 3 makes it compatible with the changes of level to the levels of $g_j$. So the correspondence of $g_j$ on $Z_N$ lies over it, and its two legs agree over $O_w$. $\square$

**Remark 3.13.9 (Formalization).** `esNorm_link` is `esNorm_of esGen_link`, and `esGen_link` and `quotObj_link` are the theorems `Cb.exists_heckeCorrespondence_on_integral_shimuraModel` and `Cb.exists_pIsogeny_kernel_eq_subgroupScheme`. The proof of `esNorm_of` cites `NormCover.exists_finite_normal_model`, `ExtT.exists_finite_extension`, `PIsogExt.exists_isPIsog_extend` and two more lemmas that we did not open; the arguments for finiteness and the extension of $\psi$ above are the standard ones, not read from them. `kSEx_holds` is `pKSEx` applied to the eight facts `kNBasic_holds`, `witUniq_holds`, `witComp_holds`, `witCart_holds`, `witEx_holds`, `witOne_holds`, `witTrans_holds` and `witFree_holds`, the facts on witnesses above. `ksGood_holds` is `ksGood_of` applied to fourteen inputs, five of them derived from `mIn`; the step for $h_1$ is `stepB`, built from `esNorm_link` and `esGen_link`, and the étaleness comes from `degGen_holds` and `fEtExt_holds`, which we did not open. The conclusion `KSGood` gives `GoodAtW`, a good model without the condition `Onto`, while `GoodAt` asks for `Onto`. The namespace `crystallineComparison.Mod` has no crystalline content.
