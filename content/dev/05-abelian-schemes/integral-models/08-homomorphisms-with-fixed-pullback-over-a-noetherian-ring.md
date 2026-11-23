---
title: Homomorphisms with fixed pullback over a noetherian ring
decls:
  - GlobalTheory.T.exists_locallyClosed_universal_hom_matrix_scheme
  - GlobalTheory.HomFixMat.exists_locClosed_homFix
  - GlobalTheory.T.exists_locallyClosed_represents_fixedPullback_homs
  - GlobalTheory.HomFixGlob.exists_homFixRep_of_secBases
  - GlobalTheory.T.exists_fixedPullbackHomScheme_of_sectionBases
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Homomorphisms with fixed pullback over a noetherian ring

Let $A$ and $B$ be [[abelian scheme|JDDXZ89N33]]s over a scheme $S$, with line bundles $L$ on $A$ and $M$ on $B$. This section and the next two construct a scheme $H$ over $S$ whose points with values in $T$ are the homomorphisms $\Phi : A_T \to B_T$ with $\Phi^* M_T \cong L_T$. The scheme of actions of an order in result 3 of the previous section is a closed subscheme of such an $H$, for $B = A^r$. Here we treat the case $S = \operatorname{Spec} R$ with $R$ a [[noetherian|0670T59HGE]] ring, under the extra assumption that powers of $L$ and $M$ have bases of sections that are stable under base change. Then $H$ is a locally closed subscheme of an affine space over $R$: a homomorphism is recorded by the matrix of its action on the bases. The next section removes the extra assumption and glues over a locally noetherian base. For [abelian schemes](/learn/abelian-varieties/#abelian-schemes) and [duality](/learn/abelian-varieties/#duality-and-the-poincare-bundle) see Volume 1.

### Test data and representing schemes

**Definition 8.8.1 (Test datum).** Let $A$ and $B$ be group schemes over $S$ with line bundles $L$ on $A$ and $M$ on $B$, and let $t : T \to S$. A *test datum* over $t$ is a tuple $D' = (A', B', \varphi_{A'}, \varphi_{B'}, \Phi')$, where $\varphi_{A'} : A' \to A$ and $\varphi_{B'} : B' \to B$ are group pullbacks along $t$ (Definition 8.2.5), $\Phi' : A' \to B'$ is a homomorphism of group schemes over $T$, and the line bundles $\varphi_{A'}^* L$ and $\Phi'^* \varphi_{B'}^* M$ on $A'$ are isomorphic. Let $D_1$ be a test datum over $t_1 : T_1 \to S$, $D_2$ a test datum over $t_2 : T_2 \to S$, and $h : T_2 \to T_1$. A *map* $D_2 \to D_1$ over $h$ is a pair of group pullbacks $\psi_A : A_2 \to A_1$ and $\psi_B : B_2 \to B_1$ along $h$ with
$$\varphi_{A_1} \psi_A = \varphi_{A_2}, \qquad \varphi_{B_1} \psi_B = \varphi_{B_2}, \qquad \psi_B \Phi_2 = \Phi_1 \psi_A.$$

Lean: `GlobalTheory.HomFixMat.IsTest` (also `GlobalTheory.HomFixMat.IsPullD`, the maps).

So a test datum over $t$ is a homomorphism $A_T \to B_T$ of the base changes that pulls $M_T$ back to $L_T$, given together with its identifications of $A'$ and $B'$ with $A_T$ and $B_T$.

**Definition 8.8.2 (Representing scheme).** A *representing scheme* for homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback is a map $\pi : H \to S$ with a test datum $D_H = (A_H, B_H, \varphi_A, \varphi_B, \Phi)$ over $\pi$, with this property. For every scheme $T$, every $t : T \to S$ and every test datum $D'$ over $t$, there is a unique $h : T \to H$ with $\pi h = t$ such that there is a map $D' \to D_H$ over $h$.

Lean: `GlobalTheory.EndLoc.HomFixRep`.

Thus $H$ represents the functor that sends $T$ to the set of homomorphisms $\Phi' : A_T \to B_T$ with $\Phi'^* M_T \cong L_T$. The isomorphism of line bundles is a condition, not a datum.

**Definition 8.8.3 (Rigidified and ample line bundles).** Let $A$ be an abelian scheme over $S$ with zero section $e_A$, and $L$ a line bundle on $A$.

1. $L$ is *rigidified* if $e_A^* L$ is trivial. A generator $\varepsilon_A$ of $e_A^* L$ is a *rigidification*.
2. $L$ is *very ample of degree $k$* if for every affine open $U \subseteq S$ there are sections $s_0, \dots, s_m$ of $L^{k}$ over $A_U$ with these properties: the open sets $D(s_i)$ where $s_i$ does not vanish cover $A_U$; each $D(s_i)$ is affine; and the quotients $s_j / s_i$ generate $\mathcal{O}(D(s_i))$ as an $\mathcal{O}(U)$-algebra.
3. $L$ is *relatively ample* if for every affine open $U \subseteq S$ there is $N \geq 1$ such that the condition of 2 holds over $U$ for $L^N$.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.Rigidified` (also `ReciprocityTheory.ChartRestriction.G.Out.VeryAmpleAt` and `ReciprocityTheory.ChartRestriction.G.Out.RelAmple`).

Condition 2 says that the sections $s_0, \dots, s_m$ define an immersion of $A_U$ into $\mathbb{P}^m_U$ whose pieces over the standard charts are closed.

**Definition 8.8.4 (Base-change-stable basis).** Let $S = \operatorname{Spec} R$ and $k \geq 1$. Sections $b_1, \dots, b_m$ of $L^k$ over $A$ form a *base-change-stable basis* if for every ring $R'$ and every map $\operatorname{Spec} R' \to S$ the pullbacks of $b_1, \dots, b_m$ to $A_{R'}$ are linearly independent over $R'$ and span the $R'$-module of global sections of $L^k$ on $A_{R'}$.

Lean: `GlobalTheory.HomFixMat.IsBCBasis`.

For example, if the direct image of $L^k$ to $S$ is a free $R$-module and its formation commutes with every base change $\operatorname{Spec} R' \to S$, then every basis of it is a base-change-stable basis.

### The matrix of a homomorphism

Fix $S = \operatorname{Spec} R$, an integer $k \geq 1$, rigidifications $\varepsilon_A$ of $e_A^* L$ and $\varepsilon_B$ of $e_B^* M$, and base-change-stable bases $b_{A,1}, \dots, b_{A,m_A}$ of $L^k$ and $b_{B,1}, \dots, b_{B,m_B}$ of $M^k$.

**Definition 8.8.5 (Matrix of a test datum).** Let $D' = (A', B', \varphi_{A'}, \varphi_{B'}, \Phi')$ be a test datum over $t : \operatorname{Spec} R' \to S$. An $m_A \times m_B$ matrix $c = (c_{ij})$ with entries in $R'$ is a *matrix* of $D'$ if there is a generator $\alpha$ of the line bundle
$$\Phi'^* \varphi_{B'}^* M^{k} \otimes \varphi_{A'}^* L^{-k}$$
on $A'$ with these two properties.

1. At the zero section, $\alpha(0) \cdot t^* \varepsilon_A^{k} = t^* \varepsilon_B^{k}$.
2. For every $j$, $\Phi'^* \varphi_{B'}^* b_{B,j} = \alpha \cdot \sum_i c_{ij}\, \varphi_{A'}^* b_{A,i}$.

Lean: `GlobalTheory.HomFixMat.IsMat`.

Condition 2 says that $\Phi'^*$ maps the basis of $M^k$ to combinations of the basis of $L^k$, after the isomorphism $\alpha$. Condition 1 fixes $\alpha$ among its multiples by units, so that the matrix is unique. We write $N = m_A m_B$, we let $p : \mathbb{A}^N_R \to \operatorname{Spec} R$ be the affine space with coordinates $x_{ij}$, and for a map $g : X \to \mathbb{A}^N_R$ we write $\operatorname{mat}(g)$ for the matrix $(g^* x_{ij})$ of functions on $X$.

We say that the *hypotheses of the matrix construction* hold if $R$ is noetherian, $A$ and $B$ are abelian schemes, $L$ is relatively ample, $k \geq 1$, $M$ is very ample of degree $k$, and $\varepsilon_A$, $\varepsilon_B$, $b_A$, $b_B$ are as above.

**Theorem 8.8.6 (The universal matrix).** Assume the hypotheses of the matrix construction. Then there are a [[closed immersion|WWRWYSJDET]] $c_E : X \to \mathbb{A}^N_R$, an [[open immersion|GFC5YKSN5H]] $i : H \to X$ and a test datum $D_H$ over $\pi = p\, c_E\, i$, with two properties.

1. For every ring $R'$, every $t : \operatorname{Spec} R' \to S$, every test datum $D'$ over $t$ and every matrix $c$ of $D'$, there is $h : \operatorname{Spec} R' \to H$ with $\pi h = t$ and $\operatorname{mat}(c_E i h) = c$.
2. For every ring $R'$, every $h : \operatorname{Spec} R' \to H$ and every test datum $D'$ over $\pi h$ with a map $D' \to D_H$ over $h$, the matrix $\operatorname{mat}(c_E i h)$ is a matrix of $D'$.

Lean: `GlobalTheory.T.exists_locallyClosed_universal_hom_matrix_scheme`.

*Proof.* This is the [Theorem 8.13.2](/entry/exists-universal-matrix/) on the universal matrix, proved in a later section. $\square$

We also use the following results on matrices. Results 1 to 3 assume the hypotheses of the matrix construction, and $D'$, $D_1$, $D_2$ are test data over $t : \operatorname{Spec} R' \to S$.

1. (Existence.) Every test datum $D'$ has a matrix.
2. (Uniqueness.) If $c$ and $c'$ are matrices of $D'$, then $c = c'$.
3. (The matrix determines the datum.) If $D_1$ and $D_2$ have a common matrix, there is a map $D_2 \to D_1$ over the identity of $\operatorname{Spec} R'$.
4. (Pullback.) Let $S = \operatorname{Spec} R$ for any ring $R$, let $A$ and $B$ be any group schemes over $S$ with line bundles $L$ and $M$, let $D_1$ be a test datum over $t : T \to S$, and let $h : T' \to T$. Then there is a test datum $D_2$ over $t h$ with a map $D_2 \to D_1$ over $h$.
5. (Affine tests suffice.) Let $\pi : H \to S$ be a map with a test datum $D_H$ over $\pi$. If the property in the definition of a representing scheme holds for every test datum over every affine scheme $\operatorname{Spec} R'$, then $(\pi, D_H)$ is a representing scheme.

Result 5 holds because a map $T \to H$ is determined by its restrictions to the affine open sets of $T$.

### The representing scheme

**Theorem 8.8.7 (Locally closed representing scheme).** Let $R$ be a noetherian ring and $S = \operatorname{Spec} R$. Let $A$ and $B$ be abelian schemes over $S$ with rigidified line bundles $L$ on $A$ and $M$ on $B$. Assume that $L$ is relatively ample, that $k \geq 1$, that $M$ is very ample of degree $k$, and that $L^k$ and $M^k$ have base-change-stable bases. Then there are $N \geq 0$, a closed immersion $c : X \to \mathbb{A}^N_R$, an open immersion $i : H \to X$ and a test datum $D_H$ over $\pi = p\, c\, i$, with this property. For every ring $R'$, every $t : \operatorname{Spec} R' \to S$ and every test datum $D'$ over $t$, there is a unique $h : \operatorname{Spec} R' \to H$ with $\pi h = t$ such that there is a map $D' \to D_H$ over $h$.

Lean: `GlobalTheory.HomFixMat.exists_locClosed_homFix` (also `GlobalTheory.T.exists_locallyClosed_represents_fixedPullback_homs`, a second name).

*Proof.* Choose rigidifications $\varepsilon_A$, $\varepsilon_B$ and bases $b_A$, $b_B$ with $m_A$ and $m_B$ elements. The hypotheses of the matrix construction hold. The theorem on the universal matrix gives $c = c_E$, $i$ and $D_H$, with $N = m_A m_B$.

Existence. Let $D'$ be a test datum over $t$. By result 1 it has a matrix $\gamma$. Property 1 of the universal matrix gives $h$ with $\pi h = t$ and $\operatorname{mat}(c\, i\, h) = \gamma$. Result 4, applied to $D_H$ and $h$, gives a test datum $D_2$ over $\pi h = t$ with a map $D_2 \to D_H$ over $h$. By property 2, the matrix $\operatorname{mat}(c\, i\, h) = \gamma$ is a matrix of $D_2$. So $D_2$ and $D'$ have the common matrix $\gamma$, and result 3 gives a map $D' \to D_2$ over the identity. The composite $D' \to D_2 \to D_H$ is a map over $h$.

Uniqueness. Let $h'$ satisfy $\pi h' = t$, with a map $D' \to D_H$ over $h'$. By property 2, $\operatorname{mat}(c\, i\, h')$ is a matrix of $D'$, so it equals $\gamma$ by result 2. The two maps $c\, i\, h$ and $c\, i\, h'$ from $\operatorname{Spec} R'$ to $\mathbb{A}^N_R$ have the same composite with $p$, which is $t$, and the same pullbacks $\gamma_{ij}$ of the coordinates. A map to $\mathbb{A}^N_R$ is determined by these data, so $c\, i\, h = c\, i\, h'$. Immersions are monomorphisms, so $h = h'$. $\square$

**Theorem 8.8.8 (Representing scheme from bases of sections).** Under the hypotheses of the previous theorem, there is a representing scheme $\pi : H \to S$ for homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback such that $\pi$ is [[quasi-compact|41009J4M5D]], [[separated|X30G4V7VAJ]] and [[locally of finite type|AHTE5DVX61]].

Lean: `GlobalTheory.HomFixGlob.exists_homFixRep_of_secBases` (also `GlobalTheory.T.exists_fixedPullbackHomScheme_of_sectionBases`, a second name).

*Proof.* The previous theorem gives $\pi = p\, c\, i : H \to S$ and $D_H$, universal for test data over affine schemes. By result 5, $(\pi, D_H)$ is a representing scheme. The ring $R[x_1, \dots, x_N]$ is noetherian by the Hilbert basis theorem, so $\mathbb{A}^N_R$ is a noetherian topological space. The immersion $c\, i$ identifies $H$ with a subspace, so $H$ is noetherian, hence quasi-compact. As $S$ is affine, $\pi$ is quasi-compact. The map $p$ is affine, hence separated, and the immersion $c\, i$ is separated, so $\pi$ is separated. Immersions are locally of finite type, and $p$ is of finite type, so $\pi$ is locally of finite type. $\square$

**Remark 8.8.9 (Formalization).** The hypotheses of the matrix construction are bundled in [WchartCompLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WchartCompLe.lean#L118); test data, maps and base-change-stable bases are at lines 41, 46 and 54 of the same file. The matrix condition is written on the trivializing charts of the line bundles, with the normalization at the zero section on its own line: [WchartCompLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WchartCompLe.lean#L77). The representing scheme asks for a unique $h$, but only for the existence of the map of test data over $h$: [NonemptyHomFixRepTrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyHomFixRepTrivial.lean#L31). Abelian schemes are also asked to be commutative group objects, which the definition of an abelian scheme already contains. The statement wrapper of the universal matrix theorem tries three forms of one proof term under a raised heartbeat limit: [ExistsLocallyClosedUniversalHomMatrixSchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocallyClosedUniversalHomMatrixSchemeStatement.lean#L10). The three properties of $\pi$ are proved in a local lemma: [ExistsFixedPullbackHomSchemeOfSectionBases.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFixedPullbackHomSchemeOfSectionBases.lean#L20). We read the statements of results 1 to 5, not their proofs.
