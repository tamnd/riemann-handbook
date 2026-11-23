---
title: The universal matrix
decls:
  - GlobalTheory.HomFixUniv.exists_universal_matrix
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The universal matrix

This section proves [Theorem 8.8.6](/entry/exists-locally-closed-universal-hom-matrix-scheme/) on the universal matrix, which Section 8.8 stated and used to build the scheme of homomorphisms with fixed pullback over a noetherian ring. The idea is classical. A homomorphism $\Phi : A_T \to B_T$ with $\Phi^* M_T \cong L_T$ is recorded by the matrix $c$ that expresses $\Phi^*$ of the basis of $M^k$ in the basis of $L^k$. Each condition on $c$ that we need (the combinations generate, they satisfy the equations of $B$, they are normalized at the zero section, and the line bundles match) cuts out an open or a closed subscheme of the affine space of matrices. The universal matrix lives on the intersection.

### The data and the conditions on a matrix

We keep the notation of Section 8.8. So $R$ is a [[noetherian|0670T59HGE]] ring, $S = \operatorname{Spec} R$, $A$ and $B$ are [[abelian scheme|JDDXZ89N33]]s over $S$, $L$ and $M$ are line bundles on $A$ and $B$ with rigidifications $\varepsilon_A$ and $\varepsilon_B$, $L$ is relatively ample, $k \geq 1$, $M$ is very ample of degree $k$, and $b_{A,1}, \dots, b_{A,m_A}$ and $b_{B,1}, \dots, b_{B,m_B}$ are base-change-stable bases of $L^k$ and $M^k$ (Definition 8.8.4). We write $N = m_A m_B$ and $p : \mathbb{A}^N_R \to S$ for the affine space with coordinates $x_{ij}$.

Let $T$ be a scheme, $c = (c_{ij})$ an $m_A \times m_B$ matrix of functions on $T$, $t : T \to S$, and $\varphi : A' \to A$ a map that identifies $A'$ with $A \times_S T$, with projection $q : A' \to T$. Put
$$s_j = \sum_i q^* c_{ij}\, \varphi^* b_{A,i}, \qquad j = 1, \dots, m_B,$$
a section of $\varphi^* L^k$ on $A'$.

**Definition 8.13.1 (Conditions on a matrix).** In this situation we say the following.

1. The matrix $c$ *generates* if at every point $z$ of $A'$ some $s_j$ does not vanish at $z$.
2. The matrix $c$ *satisfies the forms of $B$* if every homogeneous polynomial $F \in R[y_1, \dots, y_{m_B}]$ with $F(b_{B,1}, \dots, b_{B,m_B}) = 0$ on $B$ satisfies $F(s_1, \dots, s_{m_B}) = 0$ on $A'$.
3. A map $\Psi : A' \to B$ over $S$ is *proportional* to $c$ if $\Psi^* b_{B,j} \cdot s_{j'} = \Psi^* b_{B,j'} \cdot s_j$ for all $j$ and $j'$, in local trivializations of $L$ and $M$.
4. Write $e_A^* b_{A,i} = \alpha_i\, \varepsilon_A^k$ and $e_B^* b_{B,j} = \beta_j\, \varepsilon_B^k$ with $\alpha_i, \beta_j \in R$. The matrix $c$ is *normalized* if $t^* \beta_j = \sum_i c_{ij}\, t^* \alpha_i$ for every $j$.

Lean: `GlobalTheory.HomFixUniv.Generates` (also `GlobalTheory.HomFixUniv.FormsOK`, `GlobalTheory.HomFixUniv.Proport` and `GlobalTheory.HomFixUniv.Normal`).

The values $\alpha_i$ and $\beta_j$ exist because $e_A^* L$ is trivialized by $\varepsilon_A$ and $e_B^* M$ by $\varepsilon_B$. If $\Psi$ is proportional to a generating matrix $c$, then $\Psi^*$ of the basis of $M^k$ is $c$ applied to the basis of $L^k$, up to one common factor. Condition 4 is that factor equal to $1$ at the zero section. Condition 2 is a necessary condition for such a $\Psi$: the $s_j$ must satisfy every relation of the $b_{B,j}$.

We use the following results. Let $T$, $c$, $\varphi$ and $q$ be as above.

1. (Flat and projective.) $A \to S$ is [[flat|5M6KS8F47R]] and universally closed, and some line bundle on $A$ has sections $s_0, \dots, s_m$ that make $A$ very ample over $S$ in the sense of Definition 8.8.3.
2. (Embedding by the basis.) The open sets $D(b_{B,j})$ cover $B$, each is affine, and on $D(b_{B,i})$ the ratios $b_{B,j}/b_{B,i}$ generate the ring of functions over $R$.
3. (The generating locus.) There is an open set $U \subseteq \mathbb{A}^N_R$ such that, for every $g : T \to \mathbb{A}^N_R$, the matrix $\operatorname{mat}(g)$ generates if and only if $g$ maps $T$ into $U$. This needs only that $A \to S$ is universally closed.
4. (The forms locus.) There is a closed immersion $Z_F \to \mathbb{A}^N_R$ such that $\operatorname{mat}(g)$ satisfies the forms of $B$ if and only if $g$ factors through $Z_F$. This needs $R$ noetherian and result 1.
5. (The normalization locus.) There is a closed immersion $Z_N \to \mathbb{A}^N_R$ such that $\operatorname{mat}(g)$ is normalized if and only if $g$ factors through $Z_N$.
6. (Intersection.) Let $Y$ be a noetherian scheme, $Z_1, Z_2 \to Y$ closed immersions and $U \subseteq Y$ open. There is a quasi-compact immersion $W \to Y$ with $W$ locally noetherian such that $g : T \to Y$ factors through $W$ if and only if it factors through $Z_1$ and through $Z_2$ and maps $T$ into $U$.
7. (Forms and proportional maps.) If $c$ generates, then $c$ satisfies the forms of $B$ if and only if there is a map $\Psi : A' \to B$ over $S$ proportional to $c$. Two maps $\Psi_1, \Psi_2 : A' \to B$ over $S$ that are both proportional to $c$ are equal.
8. (A homomorphism.) Let $\varphi_A : A' \to A$ and $\varphi_B : B' \to B$ be group pullbacks along $t$ (Definition 8.2.5). If $c$ generates, $\Psi : A' \to B$ is proportional to $c$ and $c$ is normalized, then there is a homomorphism of group schemes $\Phi : A' \to B'$ with $\varphi_B \Phi = \Psi$.
9. (The isomorphism locus.) Let $W$ be locally noetherian, $t_1 : W \to S$, and $\varphi_{A_1} : A_1 \to A$, $\varphi_{B_1} : B_1 \to B$ group pullbacks along $t_1$ with a homomorphism $\Phi_1 : A_1 \to B_1$. There is a closed immersion $Z \to W$ with this property. For $u : T \to W$ and group pullbacks $\psi_A : A' \to A_1$, $\psi_B : B' \to B_1$ along $u$ with a homomorphism $\Phi'$ such that $\psi_B \Phi' = \Phi_1 \psi_A$, the map $u$ factors through $Z$ if and only if $(\varphi_{A_1}\psi_A)^* L \cong \Phi'^* (\varphi_{B_1}\psi_B)^* M$.
10. (Matrices of test data.) Every matrix $c$ of a test datum $(A', B', \varphi_{A'}, \varphi_{B'}, \Phi')$ over $t : \operatorname{Spec} R' \to S$ (Definition 8.8.5) generates and is normalized, and $\varphi_{B'} \Phi'$ is proportional to $c$.
11. (A matrix from the conditions.) Let $(A', B', \varphi_{A'}, \varphi_{B'}, \Phi')$ be a test datum over $t : \operatorname{Spec} R' \to S$. If $c$ generates and is normalized and $\varphi_{B'} \Phi'$ is proportional to $c$, then $c$ is a matrix of the test datum.

**Theorem 8.13.2 (The universal matrix).** Assume the hypotheses of the matrix construction of Section 8.8. Then there are a [[closed immersion|WWRWYSJDET]] $c_E : X \to \mathbb{A}^N_R$, an [[open immersion|GFC5YKSN5H]] $i : H \to X$ and a test datum $D_H$ over $\pi = p\, c_E\, i$, with two properties.

1. For every ring $R'$, every $t : \operatorname{Spec} R' \to S$, every test datum $D'$ over $t$ and every matrix $c$ of $D'$, there is $h : \operatorname{Spec} R' \to H$ with $\pi h = t$ and $\operatorname{mat}(c_E i h) = c$.
2. For every ring $R'$, every $h : \operatorname{Spec} R' \to H$ and every test datum $D'$ over $\pi h$ with a map $D' \to D_H$ over $h$, the matrix $\operatorname{mat}(c_E i h)$ is a matrix of $D'$.

Lean: `GlobalTheory.HomFixUniv.exists_universal_matrix`.

*Proof.* The ring $R[x_{ij}]$ is noetherian by the Hilbert basis theorem, so $\mathbb{A}^N_R$ is a noetherian scheme. Let $U$, $Z_F$ and $Z_N$ be the loci of results 3, 4 and 5. Result 6 gives a quasi-compact immersion $j : W \to \mathbb{A}^N_R$ with $W$ locally noetherian, and $g : T \to \mathbb{A}^N_R$ factors through $W$ if and only if $\operatorname{mat}(g)$ generates, satisfies the forms of $B$ and is normalized.

Step 1: a homomorphism over $W$. Let $g : T \to \mathbb{A}^N_R$ factor through $W$, and let $A_T$ and $B_T$ be the pullbacks of $A$ and $B$ along $p g$. Result 7 gives $\Psi : A_T \to B$ proportional to $\operatorname{mat}(g)$, and result 8 gives a homomorphism $\Phi_T : A_T \to B_T$ with $\varphi_{B_T} \Phi_T = \Psi$. We apply this to $g = j$ and get $A_1$, $B_1$ and $\Phi_1$ over $W$.

Step 2: comparison. Let $u : T \to W$, let $\varphi_{A'} : A' \to A$ and $\varphi_{B'} : B' \to B$ be group pullbacks along $p j u$, and let $\Phi' : A' \to B'$ be a map over $T$ such that $\operatorname{mat}(j u)$ generates and $\varphi_{B'} \Phi'$ is proportional to it. As $A_1$ and $B_1$ are pullbacks, there are group pullbacks $\psi_A : A' \to A_1$ and $\psi_B : B' \to B_1$ along $u$ with $\varphi_{A_1} \psi_A = \varphi_{A'}$ and $\varphi_{B_1} \psi_B = \varphi_{B'}$. The two maps $\varphi_{B'} \Phi'$ and $\varphi_{B_1} \Phi_1 \psi_A$ from $A'$ to $B$ are both proportional to $\operatorname{mat}(j u)$, since proportionality pulls back along $u$. By the uniqueness in result 7 they are equal. Both $\psi_B \Phi'$ and $\Phi_1 \psi_A$ lie over the same map to $T$, so the pullback property of $B_1$ gives $\psi_B \Phi' = \Phi_1 \psi_A$.

Step 3: the scheme $H$. Result 9, for $W$ and $(A_1, B_1, \Phi_1)$, gives a closed immersion $i_Z : Z \to W$. Step 1 for $g = j i_Z$ gives $A_H$, $B_H$ and $\Phi_H$ over $Z$, and step 2 compares them with $(A_1, B_1, \Phi_1)$ over $i_Z$. Result 9 for $u = i_Z$ then shows $\varphi_{A_H}^* L \cong \Phi_H^* \varphi_{B_H}^* M$, so $D_H = (A_H, B_H, \varphi_{A_H}, \varphi_{B_H}, \Phi_H)$ is a test datum. The composite $j i_Z : Z \to \mathbb{A}^N_R$ is a quasi-compact immersion. So it factors as an open immersion $i : Z \to X$ onto an open subscheme of its scheme-theoretic image $X$, followed by the closed immersion $c_E : X \to \mathbb{A}^N_R$. We put $H = Z$.

Property 1. Let $c$ be a matrix of $D'$ over $t : \operatorname{Spec} R' \to S$. A map to $\mathbb{A}^N_R$ is given by its composite with $p$ and the pullbacks of the coordinates, so there is $g : \operatorname{Spec} R' \to \mathbb{A}^N_R$ with $p g = t$ and $\operatorname{mat}(g) = c$. By result 10, $c$ generates and is normalized and $\varphi_{B'} \Phi'$ is proportional to $c$. By result 7, $c$ satisfies the forms of $B$. So $g = j u$ for some $u$. Step 2 gives $\psi_A$, $\psi_B$ with $\psi_B \Phi' = \Phi_1 \psi_A$. As $D'$ is a test datum, $\varphi_{A'}^* L \cong \Phi'^* \varphi_{B'}^* M$, and result 9 shows that $u = i_Z h$ for some $h$. Then $c_E i h = j i_Z h = g$, so $\pi h = t$ and $\operatorname{mat}(c_E i h) = c$.

Property 2. Let $h : \operatorname{Spec} R' \to H$ and let $D' \to D_H$ be a map over $h$. The matrix $\operatorname{mat}(j i_Z)$ generates and is proportional to $\varphi_{B_H} \Phi_H$, by step 1. Both conditions pull back along $h$, and the map $D' \to D_H$ carries $\varphi_{B_H} \Phi_H$ to $\varphi_{B'} \Phi'$. So $\operatorname{mat}(j i_Z h)$ generates and $\varphi_{B'} \Phi'$ is proportional to it. It is normalized since $j i_Z h$ factors through $W$. Result 11 shows that it is a matrix of $D'$. $\square$

The scheme $H$ is cut out in four steps: an open condition, two closed conditions on the affine space, and a closed condition on the locally noetherian scheme $W$. Only the last step uses the homomorphism $\Phi_1$, which exists only over $W$.

**Remark 8.13.3 (Formalization).** The four conditions on a matrix are written on the stalks of $A'$, in the trivializing charts of the line bundles: [CoordComp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CoordComp.lean#L20). Result 1 is stated for the map $S \times_S A \to S$, which is isomorphic to $A \to S$, and its "very ample" is a list of sections as in Definition 8.8.3: [FirstCohomologyVanishesSpecOfIsLocalRing.lean](lean:Development/AbelianVarietyTheory/Definitions/AbelianSchemeLaws/FirstCohomologyVanishesSpecOfIsLocalRing.lean#L30). The comparison of step 2 is a local claim in the proof: [ExistsLocallyClosedUniversalHomMatrixScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocallyClosedUniversalHomMatrixScheme.lean#L119). The open immersion $i$ is the map of $Z$ to its scheme-theoretic image: [ExistsLocallyClosedUniversalHomMatrixScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLocallyClosedUniversalHomMatrixScheme.lean#L149). We read the statements of results 1 to 11, not their proofs.
