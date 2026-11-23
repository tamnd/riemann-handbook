---
title: The congruence relation on points
decls:
  - UpperTheory.Ru.crystallineComparison.wZero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The congruence relation on points

The last part of this chapter proves a Frobenius relation of Eichler-Shimura type on crystalline periods. The classical model is the congruence relation of Eichler and Shimura for modular curves: on the special fibre at a prime $\ell$, the Hecke correspondence $T_\ell$ is the sum of the Frobenius and its transpose, so the Frobenius $F$ satisfies $F^2 - T_\ell F + \ell \langle \ell \rangle = 0$ (G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapter 7). We start from a relation of this kind on the points of the special fibre. In this section we move it to points with values in a class of perfect rings, the *test algebras*. The next section moves it to cohomology.

### The data

Let $\ell$ be a prime and let $q = \ell^f$ with $f > 0$. Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$, such that $\ell \neq 0$ in $\mathcal{O}$ and $\ell$ is not a unit. Let $Y \to \operatorname{Spec} \mathcal{O}$ be a smooth and quasi-compact map. We assume that each finite set of points of $Y$ lies in one affine open subset.

**Definition 3.8.1 (Correspondence).** A *correspondence* $T$ on $Y$ is a scheme $Z$ with two maps $p, r : Z \to Y$ and an integer $d \geq 0$, such that $p$ is finite, $p$ is étale over the open set where $\ell$ is a unit, and over each point of $Y$ with values in an algebraically closed field of characteristic not $\ell$ the map $p$ has exactly $d$ lifts. A *section* of $T$ over a point $y : X \to Y$ is a map $z : X \to Z$ with $p \circ z = y$.

We fix correspondences $T_0, \dots, T_n$ on $Y$ over $\operatorname{Spec} \mathcal{O}$, of degrees $d_0, \dots, d_n$, with $r_j$ and $p_j$ equal after composition with $Y \to \operatorname{Spec} \mathcal{O}$.

For a set $P$, a map $F : P \to P$ and finite families $v_j = (v_{j,i})_{i \in I_j}$ of elements of $P$, $0 \leq j \leq n$, we write
$$\operatorname{Alt}_q(F, v) = \sum_{j=0}^{n} (-1)^j q^{\binom{j}{2}} \sum_{i \in I_j} \bigl[F^{\,n-j}(v_{j,i})\bigr]$$
in the free abelian group on $P$. The relation $\operatorname{Alt}_q(F, v) = 0$ says that two multisets are equal: the multiset of the terms with $j$ even and the multiset of the terms with $j$ odd, each term with multiplicity $q^{\binom{j}{2}}$.

**Definition 3.8.2 (Point identity).** The correspondences satisfy the *point identity* if the following holds. Let $V$ be a valuation ring with algebraically closed fraction field and $\ell \neq 0$ in $V$, with residue field $\kappa_V$. Let $y : \operatorname{Spec} V \to Y$ send the closed point to a generic point of the special fibre $Y_{\varpi = 0}$. Let $\varphi$ be the $q$-power map of $\kappa_V$. For each $j$, let $z_{j,1}, \dots, z_{j, d_j}$ be the sections of $T_j$ over $y$. Then
$$\operatorname{Alt}_q(\varphi^*, v) = 0, \qquad v_{j,i} = r_j \circ z_{j,i} \circ \bar{y} \in Y(\kappa_V),$$
where $\bar{y}$ is the closed point of $\operatorname{Spec} V$ and $\varphi^*$ acts on $Y(\kappa_V)$ by composition with $\operatorname{Spec} \varphi$.

For $f = 1$, $n = 2$, $T_0 = \mathrm{id}$ and $T_1 = T_\ell$, this is the identity $F^2 - T_\ell F + q T_2 = 0$ on points, which is the form of the congruence relation above.

### Test algebras

We use the tilt $\mathcal{O}_C^\flat$ of the ring of integers of $C = \mathbb{C}_\ell$, and a pseudo-uniformizer $\varpi^\flat$ of it. A *perfect algebra* is a perfect ring $A$ of characteristic $\ell$ with a ring map $\mathcal{O}_C^\flat \to A$, such that $A$ is $\varpi^\flat$-adically complete and $\varpi^\flat$ is a nonzerodivisor on $A$. To $A$ we attach two rings: the quotient $U(A) = W(A)/(\xi)$ of the Witt vectors by the image of Fontaine's element $\xi = \ell - [\varpi^\flat]$, and $Q(A) = A / \varpi^\flat A$.

A perfect algebra $A$ is a *test algebra* if every monic polynomial of positive degree over $A$ has a root, and if for all $a, b \in A$ with a power of $\varpi^\flat$ in $(a, b)$ there is an idempotent $e$ with $e a \in (b)$ and $(1 - e) b \in (a)$. The second condition is a condition of valuation type. A *decomposition* of a test algebra $A$ is a finite family of maps $A \to B_s$ of test algebras such that $A \to \prod_s B_s$ is bijective.

Fix ring maps $\kappa : \mathcal{O} \to \mathcal{O}_C$ and $g : \mathcal{O} \to \mathcal{O}_C^\flat / \varpi^\flat$ with $g(\varpi) = 0$ and $g(x)^q = g(x)$ for all $x \in \mathcal{O}$. These give two functors on perfect algebras: $P_X(A)$ is the set of points $\operatorname{Spec} U(A) \to Y$ over $\kappa$, and $P_Q(A)$ is the set of points $\operatorname{Spec} Q(A) \to Y$ over $g$. We fix two natural maps:

1. a *Frobenius* $F : P_Q \to P_Q$, which acts by composition with the $q$-power map of $Q(A)$;
2. a *reduction* $\rho : P_X \to P_Q$, which acts by composition with a ring map $\psi : U(A) \to Q(A)$ that sends the image $\theta(x)$ of a Witt vector $x$ to $x_0^{\ell^m}$, for a fixed $m$.

**Definition 3.8.3 (Vanishing relation).** Let $u_1, \dots, u_k : P \to P_Q$ be natural maps and $a_1, \dots, a_k \in \mathbb{Z}$. The relation $\sum_t a_t u_t = 0$ *holds on test algebras* if for each test algebra $A$ and each $y \in P(A)$ there is a decomposition $(A \to B_s)$ such that for each $s$ either $B_s = 0$ or
$$\sum_t a_t \, [u_t(y|_{B_s})] = 0$$
in the free abelian group on $P_Q(B_s)$.

The last input is a cover that splits the correspondences. We fix a map $\pi : W \to Y$ with maps $s_{j,i} : W \to Z_j$, $i = 1, \dots, d_j$, with $p_j \circ s_{j,i} = \pi$, such that over the open set where $\ell$ is a unit the $s_{j,i}$ are all the sections of $T_j$, and which is universal with this property for rings on which $\ell$ is a nonzerodivisor.

### The theorem

**Theorem 3.8.4 (Congruence relation on test algebras).** Assume the point identity, and fix the cover $W$. Then there is $N \geq 0$ such that
$$\sum_{j=0}^{n} (-1)^j q^{\binom{j}{2}} \sum_{i=1}^{d_j} F^{\,n-j+N} \circ \rho \circ (r_j \circ s_{j,i})_* = 0$$
holds on test algebras, as a relation between maps $P_X^W \to P_Q$. Here $P_X^W$ is the functor $P_X$ for $W$ over $\mathcal{O}$.

Lean: `UpperTheory.Ru.crystallineComparison.wZero`.

We know no published source for this statement. Its role is the role of the congruence relation in the proof of the Eichler-Shimura relation on étale cohomology, and the test algebras play the role of the perfectoid algebras in the comparison theorems of $p$-adic Hodge theory (see the [Background](/learn/galois-representations/#period-rings)).

*Proof.* Let $M = \sum_j w_j d_j$, where $w_j = q^{\binom{j}{2}}$ for $j$ even and $w_j = 0$ for $j$ odd. Put $N = (M + 1)^M$. Since $q \geq 2$, we have $(M + 1)^M = N < q^N$.

Let $A$ be a test algebra and $y \in P_X^W(A)$. We find the decomposition in four steps.

*Step 1: charts.* By the assumption on finite sets, for each point of $Y$ there are affine opens $U \ni$ the point and $V$ with $p_j^{-1}(U) \subseteq r_j^{-1}(V)$ for all $j$. Finitely many such $U$ cover $Y$, and their preimages cover $\operatorname{Spec} U(A)$. For a test algebra, such a finite open cover is refined by a decomposition: there is a decomposition $(A \to B_s)$ such that on each $B_s$ the point $\pi \circ y$ lands in one such $U$. We fix $s$ and replace $A$ by $B_s$.

*Step 2: a norm identity.* Let $R = \Gamma(V, \mathcal{O}_Y)$ and $R_U = \Gamma(U, \mathcal{O}_Y)$. For a ring $B$ and a family $c = (c_k)$ of elements of $B$ indexed by a finite set, let $\Phi(c) = X - \sum_k c_k X_k$ in $B[X, X_k]$. For a multiset of families, let $\Phi$ be the product. We take as given the following consequence of the point identity, the *norm identity on charts*: for each $R_U$-algebra $B$ on which $\ell$ is a nonzerodivisor, with sections $z_{j,i}$ of $T_j$ that split $T_j$ after inverting $\ell$, each ring map $\beta : B \to B'$ that kills $\varpi$, and each finite family $(x_k)$ of elements of $R$, the two products
$$\prod_{j \text{ even}} \prod_i \Phi\bigl(\beta(z_{j,i}^* r_j^* x_k)^{q^{n-j}}\bigr)^{q^{\binom{j}{2}}}, \qquad \prod_{j \text{ odd}} \prod_i \Phi\bigl(\beta(z_{j,i}^* r_j^* x_k)^{q^{n-j}}\bigr)^{q^{\binom{j}{2}}}$$
are equal. Here $z_{j,i}^* r_j^* x_k$ is the image of $x_k$ under the ring maps of $r_j$ and $z_{j,i}$. We apply it to the ring $U(A)$, the sections $s_{j,i} \circ y$ and the map $\psi : U(A) \to Q(A)$ of the reduction. This needs $\psi(\kappa(\varpi)) = 0$, which follows from $g(\varpi) = 0$ and the compatibility of $\rho$ with $\kappa$ and $g$. So the points $r_j \circ s_{j,i} \circ y$ give ring maps $\alpha_{j,i} : R \to U(A)$, and the values of the maps $\psi \circ \alpha_{j,i}$, which give the points $\rho(r_j \circ s_{j,i} \circ y)$, satisfy the norm identity.

*Step 3: finitely many functions.* Since $Y$ is smooth over $\mathcal{O}$, there are finitely many $x_1, \dots, x_k \in R$ such that two ring maps $R \to Q(A)$ over $\mathcal{O}$ that agree on the $x_k$ are equal. If $A \neq 0$, the norm identity forces both multisets to have $M$ elements.

*Step 4: matching.* We use a matching lemma for test algebras: if two families $(c_t)$ and $(c'_t)$ of $M$ vectors in $Q(A)$ have the same norm form $\prod_t \Phi(c_t) = \prod_t \Phi(c'_t)$, and $(M + 1)^M \leq \ell^a$, then there are orthogonal idempotents $e_\sigma$ of $A$ with sum $1$, indexed by the bijections $\sigma$ of the index sets, such that $e_\sigma c_t^{\ell^a} = e_\sigma c'_{\sigma(t)}{}^{\ell^a}$ for all $t$. We apply it with $\ell^a = q^N$ to the vectors $(\psi\alpha_{j,i}(x_k)^{q^{n-j}})_k$. The idempotents give a decomposition $(A \to B_\sigma)$. On $B_\sigma$, the two multisets of vectors are equal after the $q^N$-th power. Since the $q^{n-j+N}$-th power of $\psi \circ \alpha_{j,i}$ is $F^{n-j+N}$ applied to the point, and the $x_k$ determine the points, the two multisets of points
$$\bigl\{F^{\,n-j+N} \rho (r_j s_{j,i} y)\bigr\}_{j \text{ even}}, \qquad \bigl\{F^{\,n-j+N} \rho (r_j s_{j,i} y)\bigr\}_{j \text{ odd}}$$
with multiplicities $q^{\binom{j}{2}}$ are equal over $B_\sigma$. This is the relation of the theorem over $B_\sigma$.

Finally, decompositions compose: if $A \cong \prod_s B_s$ and each $B_s \cong \prod_\sigma B_{s,\sigma}$, then $A \cong \prod_{s,\sigma} B_{s,\sigma}$. So the decompositions of Step 1 and Step 4 give one decomposition of $A$ on each part of which the relation holds. $\square$

**Remark 3.8.5 (Formalization).** The proof does not use that $Y \to \operatorname{Spec} \mathcal{O}$ is quasi-compact, nor $g(x)^q = g(x)$, which is an anonymous variable ([MapUSharp.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/MapUSharp.lean#L298)). The cover $W$ with its sections is a hypothesis, and the integer $m$ of the reduction is arbitrary. The point identity is the hypothesis `PtId` and is not proved here. The norm identity on charts is the private lemma `normOfPt'`, built from about twenty lemmas on charts, valuation points and splitting fields. It, the refinement of covers, `UpperTheory.correspondence_norm_bound_of_affine_opens` and the matching lemma `UpperTheory.exists_orthogonalIdempotents_matching_of_sameNorm` were checked from their statements.
