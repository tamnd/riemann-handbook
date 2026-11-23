---
title: Roots of the Mumford bundle
decls:
  - GlobalTheory.T.mumfordBundle_root_lifts_from_residue_complete_local
  - GlobalTheory.PolRootComplete.root_of_residue
  - GlobalTheory.PolRootComplete.root_of_closedFibre
  - GlobalTheory.T.exists_rigidified_cubical_root_polarisation_etale
  - GlobalTheory.PolBundleLocEt.exists_rigLB_sFam_etale
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Roots of the Mumford bundle

A principal Siegel datum carries a bundle $P$ on $A \times A$, not a line bundle on $A$. Mumford's construction of degenerations needs an ample line bundle $L$ on the abelian part, and $P$ should be the Mumford bundle $\Lambda(L)$ of $L$. Such an $L$ need not exist over the base. This section proves that it exists after a finite étale extension of a complete local base. The proof finds $L$ over the algebraic closure of the residue field, descends it to a finite separable extension, and lifts it to the complete ring by formal algebraization. The result is used in the next section, to build the lower base of a chart.

**Definition 9.3.1 (Mumford bundle).** Let $B \to T$ be a commutative group scheme with multiplication $m$, projections $p_1, p_2 : B \times_T B \to B$ and unit section $0$, and let $L$ be a line bundle on $B$. The *Mumford bundle* of $L$ is the line bundle
$$\Lambda(L) = m^* L \otimes p_1^* L^{-1} \otimes p_2^* L^{-1} \otimes 0^* L$$
on $B \times_T B$, where $0^*L$ is pulled back along the structure map. More generally, for points $x_1, \dots, x_k$ of $B$ we write $\bigotimes_{I \subseteq \{1, \dots, k\}} (\sum_{i \in I} x_i)^* L^{(-1)^{k - |I|}}$ for the cube bundle; for $k = 2$ and the two projections it is $\Lambda(L)$, and for $k = 3$ it is $\Theta(L)$ on $B^3$.

Lean: `ReciprocityTheory.ChartRestriction.G.Semi.abelian₂` (also `ReciprocityTheory.ChartRestriction.G.Semi.cubeLB`).

The theorem of the cube says that $\Theta(L)$ is trivial on an abelian scheme ([theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube)). So $\Lambda(L)$ is a biextension, and it is the pullback of the Poincaré bundle along $1 \times \varphi_L$.

**Definition 9.3.2 (Rigidified cubical bundle).** Let $B \to T$ be a commutative group scheme. A *rigidified* line bundle on $B$ is a line bundle $L$ with a generator of $0^* L$. A *cubical structure* on it is a generator of $\Theta(L)$ that is $1$ on the faces $x_i = 0$, symmetric under permutations of the factors, and satisfies the cocycle condition in the first two variables. We say that $L$ has *trivial $K$-group* if each point $x \in B(T')$, over an affine $T'$, such that $t_x^* L \otimes L^{-1}$ is locally trivial on $T' \times_T B$, is zero.

Lean: `ReciprocityTheory.ChartRestriction.G.Semi.RigLB`, `ReciprocityTheory.ChartRestriction.G.Semi.CubicalStr`, `ReciprocityTheory.ChartRestriction.G.Out.KTriv`.

So a relatively ample rigidified bundle with trivial $K$-group defines a principal polarization ([polarizations](/learn/abelian-varieties/#polarizations-and-zarhins-trick)).

**Definition 9.3.3 (Root).** Let $A \to S$ be a commutative group scheme, let $P$ be a line bundle on $A \times_S A$ and let $t : T \to S$. We say that $P$ *has a root along $t$* if there are a commutative group scheme $B \to T$, a map $\beta : B \to A$ that makes $B$ the pullback of $A$ along $t$ as a group, and a line bundle $L$ on $B$ with
$$\Lambda(L) \cong (\beta \times \beta)^* P.$$

Lean: `GlobalTheory.PolRoot.Root`.

If $P$ has a root along $t$, it has a root along $t \circ \sigma$ for each $\sigma : T' \to T$, by pulling back $L$; this uses that $A$ is an abelian scheme. And the root can be taken on any group pullback $B'$ of $A$ along $t$, because two pullbacks are isomorphic by a unique group isomorphism over $T$.

Throughout the section, $R$ is a local ring with maximal ideal $\mathfrak{m}$ and residue field $k$, and $B_e = B \times_R R/\mathfrak{m}^{e+1}$ is the $e$-th thickening of a scheme $B$ over $R$. The conditions on $P$ are those of a principal Siegel datum: $P$ is trivial on $\{0\} \times B$ and on $B \times \{0\}$, and $P_\Delta = \Delta^* P$ is relatively ample.

**Lemma 9.3.4 (Root from the closed fibre).** Let $R$ be a noetherian local ring that is $\mathfrak{m}$-adically complete, and let $B$ be an abelian scheme over $R$. Let $P$ be a line bundle on $B \times_R B$, trivial on $\{0\} \times B$ and on $B \times \{0\}$, such that $P_\Delta$ is relatively ample. Assume that there is a line bundle $L_0$ on the closed fibre $B_0$ with $\Lambda(L_0) \cong P|_{B_0 \times B_0}$. Then there is a line bundle $L$ on $B$ with $\Lambda(L) \cong P$.

Lean: `GlobalTheory.PolRootComplete.root_of_closedFibre`.

*Proof.* We use one step on thickenings: for each $e$ and each line bundle $L_e$ on $B_e$ with $\Lambda(L_e) \cong P|_{B_e \times B_e}$, there is a line bundle $L_{e+1}$ on $B_{e+1}$ with $\Lambda(L_{e+1}) \cong P|_{B_{e+1} \times B_{e+1}}$ and $L_{e+1}|_{B_e} \cong L_e$. This step needs only that $R$ is local and that $P$ is trivial on the two axes. By recursion on $e$, starting from $L_0$, we get a line bundle $(L_e)$ on the tower $(B_e)$ of thickenings, with $L_e \cong L_{e+1}|_{B_e}$.

Since $P_\Delta$ is relatively ample, $B$ is projective over $R$ with an ample family of sections. A lemma on line bundles over complete local bases, applied with the [theorem on formal algebraization](/entry/global-theory-formal-algebraisation/), turns the compatible family $(L_e)$ into a line bundle on $B$ itself. This gives a line bundle $L$ on $B$ with $L|_{B_e} \cong L_e$ for each $e$. Then $\Lambda(L)$ and $P$ are two line bundles on $B \times_R B$, both trivial on $\{0\} \times B$, with isomorphic restrictions to the closed fibre. A comparison over the local base $R$ shows that $\Lambda(L) \cong P$. $\square$

**Theorem 9.3.5 (Root from the residue field).** Let $A \to S$ be an abelian scheme and $P$ a line bundle on $A \times_S A$, trivial on $\{0\} \times A$ and on $A \times \{0\}$, with $P_\Delta$ relatively ample. Let $R$ be a noetherian, $\mathfrak{m}$-adically complete local ring, and let $t : \operatorname{Spec} R \to S$. If $P$ has a root along the closed point $\operatorname{Spec} k \to \operatorname{Spec} R \to S$, then $P$ has a root along $t$.

Lean: `GlobalTheory.PolRootComplete.root_of_residue` (also `GlobalTheory.T.mumfordBundle_root_lifts_from_residue_complete_local`, a wrapper).

*Proof.* Let $\beta : B \to A$ be the group pullback of $A$ along $t$. Then $B$ is an abelian scheme over $R$. The bundle $(\beta \times \beta)^* P$ is trivial on the two axes, and its restriction to the diagonal is relatively ample, since relative ampleness is stable under base change. The first thickening $\operatorname{Spec} R/\mathfrak{m} \to \operatorname{Spec} R$ is the closed point, so the root along the closed point gives a root on the closed fibre $B_0$ of $B$, by the remarks after the definition of a root. The lemma on the root from the closed fibre, applied to $B$ and $(\beta \times \beta)^* P$, gives $L$ on $B$ with $\Lambda(L) \cong (\beta \times \beta)^* P$. $\square$

**Theorem 9.3.6 (Étale local root).** Let $F$ be a Siegel family over $(o, \zeta)$ with universal datum $(A, P, \ell)$ on $X$. Let $R$ be a noetherian, $\mathfrak{m}$-adically complete local ring and let $y : \operatorname{Spec} R \to X$. Then there are a local ring $R'$ and a map $\rho : R \to R'$ such that $R'$ is $\mathfrak{m}'$-adically complete and $\rho$ is local, injective, finite and étale, and there are a commutative group scheme $B$ over $R'$, a map $\beta : B \to A$ that makes $B$ the group pullback of $A$ along $y \circ \operatorname{Spec}\rho$, and a rigidified line bundle $M$ on $B$ with a cubical structure, such that $M$ is relatively ample, has trivial $K$-group, and
$$\Lambda(M) \cong (\beta \times \beta)^* P.$$

Lean: `GlobalTheory.PolBundleLocEt.exists_rigLB_sFam_etale` (also `GlobalTheory.T.exists_rigidified_cubical_root_polarisation_etale`, a wrapper).

*Proof.* The ring $R$ is complete, so it is Henselian ([Henselian rings](/learn/commutative-algebra/#henselian-and-strictly-henselian-rings)). Let $t_0 : \operatorname{Spec} k \to X$ be the closed point of $y$.

1. Over the algebraic closure $\bar k$, the principal Siegel datum has a root: $P$ has a root along $\operatorname{Spec} \bar k \to X$.
2. The root over $\bar k$ is defined over a finitely generated, hence finite, $k$-subalgebra $C_0 \subseteq \bar k$.
3. There is a complete local $k$-algebra $C$ with a $k$-algebra map $C_0 \to C/\mathfrak{m}_C$, such that $K \otimes_k C$ is a domain for each finite purely inseparable extension $K$ of $k$. So $P$ has a root along the closed point of $\operatorname{Spec} C$. The theorem on the root from the residue field, applied to $C$, gives a root over $C$.
4. This root is again defined over a finitely generated $k$-subalgebra $C_1 \subseteq C$. Its base change to each finite purely inseparable extension of $k$ is a domain, being a subring of the corresponding base change of $C$, since a field is flat over $k$. A geometrically integral finite type algebra of this kind has a point in a finite separable extension $k''$ of $k$. So $P$ has a root along $\operatorname{Spec} k'' \to X$.
5. Since $R$ is Henselian, there is a finite étale local $R$-algebra $R'$ with residue field $k''$. It is Henselian, noetherian and complete, and $\mathfrak{m} R' = \mathfrak{m}'$ because $R \to R'$ is unramified. Let $\rho : R \to R'$ be the structure map.
6. The root along $\operatorname{Spec} k'' \to X$ is a root along the closed point of $R'$. The theorem on the root from the residue field gives $B$, $\beta$ and $L$ on $B$ with $\Lambda(L) \cong (\beta \times \beta)^* P$.

It remains to improve $L$. The bundle $(\beta \times\beta)^* P$ is nondegenerate, since $P$ is. A line bundle on an abelian scheme over a local base can be rigidified and given a cubical structure; this gives $M$. Since $\Lambda(M) \cong (\beta\times\beta)^*P$ is nondegenerate, $M$ has trivial $K$-group. Since $(\beta \times \beta)^* P$ restricted to the diagonal is relatively ample and $\Lambda(M)|_\Delta \cong M^2$ up to a bundle from the base, $M$ is relatively ample. Finally $\rho$ is injective, because an étale local map of local rings is faithfully flat. $\square$

**Remark 9.3.7 (Formalization).** The thickening step in the proof of the lemma on the root from the closed fibre assumes only that $R$ is local; it does not need $R$ noetherian or complete ([LineBundleThickeningSquareTheoremStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LineBundleThickeningSquareTheoremStatement.lean#L15)). The algebraization step, the comparison of $\Lambda(L)$ with $P$, the existence of a root over $\bar k$, the choice of $C$, the separable point and the improvement of $L$ to $M$ are lemmas that have no entries in this chapter; we have described only what their statements give. In particular the remark "$\Lambda(M)|_\Delta \cong M^2$" is our explanation of why that lemma holds, not a reading of its proof. The theorem on the étale local root holds for a Siegel family over any $(o, \zeta)$, not only over $\Lambda_n$.
