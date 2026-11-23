---
title: The congruence relation on Kuga-Sato models
decls:
  - UpperTheory.Gal.crystallineComparison.Mod.ordEmb_holds
  - UpperTheory.Gal.crystallineComparison.Mod.ordKSE_holds
  - UpperTheory.Gal.crystallineComparison.Mod.congKS_holds
  - UpperTheory.Gal.crystallineComparison.Mod.congKS_link
  - UpperTheory.Gal.Int.Geo.CovMain.mIn
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The congruence relation on Kuga-Sato models

Section 10 described the Hecke correspondences $T_j$ at the ordinary points of the special fibre through the subspaces of a vector space $H$ over $\mathcal{O}_F/w$ with a marked line $C$. This section counts these subspaces with the signs $c_q(j) = (-1)^j q^{\binom j2}$, carries the description from the models $M$ to flat covers and to the Kuga-Sato varieties over the étale level models, and obtains the congruence relation there. It ends with the list of facts on integral models that Section 07 takes as input. We keep the notation of Section 10: $\mathfrak{u}_r = (p, \omega - r)$, standard rings $O$, and Hecke correspondences of type $j$ and factor $p^{fj}$.

**Lemma 3.11.1 (alternating count).** Let $k$ be a field with $q$ elements, $H$ a $k$-space of dimension $n$ and $C \subset H$ a line. Let $P$ be a set with a map $F : P \to P$ and let $A$ map the subspaces of $H/C$ to $P$. For each $j$ let $I_j$ be a finite set with a bijection $i \mapsto D_i$ onto the $j$-dimensional subspaces of $H$, and let $v_j(i) = F(A(\bar D_i))$ if $C \subseteq D_i$ and $v_j(i) = A(\bar D_i)$ otherwise. Then, in the free abelian group on $P$,
$$\sum_{j=0}^{n} c_q(j) \sum_{i \in I_j} [F^{n-j}(v_j(i))] = 0.$$

*Proof.* Group the terms by $U = \bar D$, a subspace of $H/C$ of dimension $u$. The one subspace $D \supseteq C$ with $\bar D = U$ is the preimage of $U$, of dimension $u + 1$; it contributes $c_q(u+1) [F^{n-u}(A(U))]$. The subspaces $D \not\supseteq C$ with $\bar D = U$ have dimension $u$; after a choice of complement they are the graphs of the linear maps $U \to C$, so there are $q^u$ of them, each contributing $c_q(u) [F^{n-u}(A(U))]$. Since $\binom{u+1}{2} = \binom{u}{2} + u$, we get $q^u c_q(u) + c_q(u+1) = 0$. $\square$

We say that a family $(C_j)_{0 \le j \le n}$ of finite correspondences on a scheme $Y$ over $O$ has the *ordinary reading* if, for each valuation ring $V$ with algebraically closed fraction field and $p \ne 0$ in $V$, each $V$-point $y$ of $Y$ whose closed point is generic in the special fibre, and $\varphi$ the $q$-power map, the residue points of the targets of the lifts of $y$ to $C_j$ are given by values $v_j(i)$ as in Lemma 3.11.1, with $F = \varphi^*$. The family *satisfies the congruence relation* if, for the same data, the residue points of the targets satisfy the identity of Lemma 3.11.1.

**Proposition 3.11.2 (ordinary reading on flat covers).** Let $O$ be standard for $(f, N, r, w)$ with $w$ maximal, $M$ a model of level $N$, $\varpi$ a uniformizer of $O$, and $T_j$ Hecke correspondences of type $j$ and factor $p^{fj}$. Let $h : Y \to M$ be flat, and let $(a_i)$ be sections of $A$ over $h$ such that two maps $u, v$ to $Y$ with $h u = h v$ and $a_i u = a_i v$ for all $i$ are equal. Let $C_j$ be finite correspondences on $Y$ with maps $g_j : C_j \to T_j$ such that the source of $C_j$ is the pullback of $s$ along $h$, $h \circ r = t \circ g_j$, and $a_i \circ r$ is the image of $a_i$ under $g_j$. Then $(C_j)$ has the ordinary reading.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.ordEmb_holds`.

*Proof.* A flat map sends generic points of the special fibre to generic points, so the image in $M$ of the closed point of $y$ is generic, and its geometric points are $w$-ordinary by Theorem 3.10.4. Theorem 3.10.6 gives $H$, $C$ and the bijections, and its two cases are the two cases of $v$. The points of $Y$ are separated by $h$ and the $a_i$, so the equalities of targets and of images in $M$ and in $A$ give the equalities of targets in $Y$. $\square$

**Proposition 3.11.3 (ordinary reading on Kuga-Sato varieties).** Keep $O$, $M$, $\varpi$ and $T_j$ as in the proposition. Let $\mathfrak{a}$ be an ideal of $\mathcal{O}_F$, $E$ an étale level model of level $\mathfrak{a}$ with $\pi : E \to M$ flat over $O$ and a map of universal objects over $\pi$, let $L_j$ be lifts of the $T_j$ to $E$ compatible with the isogenies and the level structures, and let $k \geq 0$. Then there are $d_j \in \mathbb{N}$ and correspondences on the $k$-th fibre power $Z$ of the universal abelian scheme over $E$ built from the $L_j$, finite, étale where $p$ is invertible and of degree $d_j$ on each geometric fibre where $p \ne 0$, whose two legs agree over $O$, and which have the ordinary reading.

Lean: `UpperTheory.Gal.crystallineComparison.Mod.ordKSE_holds`.

*Proof.* The pullbacks of the $T_j$ along any map are finite, étale away from $p$, with $\#\mathrm{Gr}_j((\mathcal{O}_F/w)^n)$ points on each geometric fibre; take $d_j$ to be this number. Apply the previous proposition to $Z \to E \to M$, which is flat, with the $k$ coordinate sections of the $k$-th power, which separate points of $Z$ over $M$ because $E \to M$ is injective on the points that matter. $\square$

**Theorem 3.11.4 (congruence relation on Kuga-Sato models).** Let $O$ be standard for $(f, N, r, w)$ with $w$ maximal, $M$ a model of level $N$ and $\varpi$ a uniformizer of $O$. Let $\mathfrak{a}$ be an ideal with $\mathfrak{a} + w = \mathcal{O}_F$ and $\mathfrak{u}_r^e \subseteq \mathfrak{a}$ for some $e$, and let $E$, $\pi$ be as in the proposition, with $\pi$ flat, and $k \geq 0$. Then there are Hecke correspondences $T_j$ of type $j$ and factor $p^{fj}$ on $M$, lifts $L_j$ to $E$, numbers $d_j$, and correspondences of degree $d_j$ on $Z$ as in the proposition, whose two legs agree over $O$, and which satisfy the congruence relation
$$\sum_{j=0}^{n} c_q(j)\, (\varphi^*)^{n-j} \circ T_j = 0, \qquad q = p^f.$$

Lean: `UpperTheory.Gal.crystallineComparison.Mod.congKS_holds` (also `UpperTheory.Gal.crystallineComparison.Mod.congKS_link`).

This is the congruence relation for unitary Shimura varieties at a split prime, the analogue of the relation of Faltings and Chai, loc. cit., for Siegel modular varieties (see also O. Bültel and T. Wedhorn, Congruence relations for Shimura varieties associated to some unitary groups, J. Inst. Math. Jussieu 5 (2006)).

*Proof.* Correspondences $T_j$ with $T_j \to O$ flat exist on $M$ by [the theorem on Hecke correspondences on integral models](/entry/exists-hecke-correspondence-on-integral-shimura-model/), and they lift to $E$ because $\mathfrak{a} + w = \mathcal{O}_F$ and $\mathfrak{u}_r^e \subseteq \mathfrak{a}$. The last proposition gives the correspondences on $Z$ with the ordinary reading, and the alternating count lemma turns the ordinary reading into the congruence relation. $\square$

The integral models that Section 07 needs are now collected.

**Theorem 3.11.5 (integral models of the Kuga-Sato tower).** The following hold.

1. For every Noetherian ring $R$ with a base and $N \geq 3$ prime to $p$, a model of level $N$ over $R$ exists.
2. If $R$ is also a domain of characteristic $0$ and the data are compact, every model of level $N$ over $R$ is projective.
3. For a map $R \to R'$ of rings with $R'$ a $\mathbb{Q}$-algebra and a generic model over $R'$ with matching base, the generic model embeds in the base change of the model over $R$ by an open and closed immersion compatible with the universal objects.
4. If every maximal ideal containing the nonzero ideal $\mathfrak{a}$ is an étale place of the base, then over each model $M$ there are an étale level model $E$ of level $\mathfrak{a}$ and $\pi : E \to M$ over the base with a map of universal objects, and $\pi$ is a Galois cover with group the level group of $\mathfrak{a}$.
5. If $O$ is a discrete valuation ring of characteristic $0$ with $p \in \mathfrak{m}_O$, $a = 1$, $w$ is maximal with $\mathfrak{u}_r \subseteq w$ and $t_i(w) \subseteq \mathfrak{m}_O$ for all $i$, then an ideal $\mathfrak{a}$ with $\mathfrak{a} + w = \mathcal{O}_F$ has the property of item 4 if and only if $\mathfrak{u}_r^e \subseteq \mathfrak{a}$ for some $e$.
6. The congruence relation on Kuga-Sato models holds as in Theorem 3.11.4.
7. In the standard situation, the pullback of a Hecke correspondence of type $j$ along any map $Y \to M$ is finite, étale where $p$ is invertible, with $\#\mathrm{Gr}_j((\mathcal{O}_F/w)^n)$ points on each geometric fibre where $p \neq 0$.

Lean: `UpperTheory.Gal.Int.Geo.CovMain.mIn`.

*Proof.* Item 1 is [the existence of integral models](/entry/model-nonempty/), item 2 is the projectivity of the moduli model over a compact base, and item 3 is the immersion of the generic fibre used in Section 08. Items 4 and 5 are proved in their own entries of this chapter. Item 6 is the theorem above. Item 7 follows from the universality of $T_j$ and [the theorem on quotients by subgroup schemes](/entry/exists-p-isogeny-kernel-eq-subgroup-scheme/). $\square$

From items 1, 4, 5 and 6 one gets, for each good place $w$ and each power $k$, the congruence models of the Kuga-Sato tower that Section 07 takes as given.

**Remark 3.11.6 (Formalization).** The identity of Lemma 3.11.1 is `AltId`, an equality of two multisets (even $j$ with multiplicity $q^{\binom j2}$ against odd $j$), proved as `ordCount_holds`; the ordinary reading is `OrdPt` and the congruence relation `PtId`. `congKS_link` is `congKS_holds` applied to `esNorm_link`, `esGen_link`, `ordGen_link` and `quotObj_link`. Proposition 3.11.3 does not need $\mathfrak{a} + w = \mathcal{O}_F$; only the existence of the lifts in Theorem 3.11.4 does. The namespace `crystallineComparison.Mod` has no crystalline content. In `mIn`, items 1 and 3 are the hypotheses `ModelEx` and `GenCmp` of `gUnif_of` (Section 08), proved by the same theorems, and `stdEx_holds`, `ksCong_holds` and `ksCover_holds` are projections of `mIn`.
