---
title: The unit lemma
decls:
  - GlobalTheory.UnitLemma.Desc.linearDescent
  - GlobalTheory.T.linearLatticeCountDescent_proof
  - GlobalTheory.UnitLemma.unitLemma_lie_and_group
  - GlobalTheory.T.unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unit lemma

The unit lemma is an identity between counts of self-dual lattices. On one side we count lattices in a product $A_1 \times A_2$ of two algebras with involution, weighted by a sign. On the other side we take the product of the counts for $A_1$ and $A_2$. The two sides differ by a power of $-q$ given by the resultant of the two characteristic polynomials. There are two versions: the Lie algebra version, where $g_i$ is fixed by $\sigma$, and the group version, where $g_i$ is unitary. This section proves both from the [fundamental lemma](/entry/unit-match-all/), with the two facts of [the previous section](/entry/count-identity-of-unit-match/) and a descent for the linear counts. The unit lemma is used in the step [EveryCharacter](/step/every-character/), and its Lie algebra version enters [the matching of principal congruence functions](/entry/match-principal-congruence-inert/). For the orbital integrals behind the counts, see [orbital integrals and the relative trace formula](/learn/periods/#orbit-integrals-and-the-relative-trace-formula).

We keep the notation of [the previous section](/entry/count-identity-of-unit-match/): $K$ is an unramified quadratic datum with fields $F \subset E$, $A$ is an algebra with involution $(A, \sigma, g)$ of dimension $n$ over $E$, $P$ is the characteristic polynomial of $g$, and $N(x)$ is the weighted number of $T$-orbits of $g$-stable lattices that are self-dual for $h_x$.

**Definition 4.7.1 (Classes and sums).** Let $A$ be an algebra with involution.

1. $\mathrm{Cl}(A)$ is the set of $y \in A^\times$ with $\sigma(y) = y$, modulo the relation $y \sim y\, u\sigma(u)$ for $u \in A^\times$. For each class $k$ fix a representative $y_k$.
2. Fix an $E$-basis $b_1, \dots, b_n$ of $A$. For $x \in A$ let $\delta(x) = \det(h_x(b_i, b_j))_{i,j}$.
3. $S(A) = \sum_{k \in \mathrm{Cl}(A)} N(y_k)$.
4. For two algebras $A_1$, $A_2$, let $\kappa(A_1, A_2) = \sum_{k \in \mathrm{Cl}(A_1 \times A_2)} \eta(\delta_1(y_{k,1}))\, N(y_k)$, where $y_{k,1}$ is the first component of $y_k$, $\delta_1$ is $\delta$ for $A_1$, and $N$ is the count for $A_1 \times A_2$.
5. The pair $(A_1, A_2)$ satisfies the *unit identity* if
$$(-q)^{-\mathrm{val}(\mathrm{Res}(P_1, P_2))}\, \kappa(A_1, A_2) = S(A_1)\, S(A_2).$$

The terms do not depend on the choices. Since $h_{x u \sigma(u)}(y, z) = h_x(uy, uz)$, the map $L \mapsto uL$ is a bijection from $X(x u\sigma(u))$ to $X(x)$ that commutes with $T$, so $N$ is constant on classes. Also $\delta(x u \sigma(u)) = N_{A/E}(u)\, c(N_{A/E}(u))\, \delta(x)$, and $c$ preserves the valuation, so $\eta(\delta(x))$ is constant on classes. A change of basis multiplies $\delta(x)$ by $\det(Q)\, c(\det Q)$ for an invertible matrix $Q$, which again does not change $\eta(\delta(x))$.

**Definition 4.7.2 (The unit lemma).** The *unit lemma for the Lie algebra* is the statement: for every $K$ and all algebras with involution $A_1$, $A_2$ with $\sigma(g_1) = g_1$, $\sigma(g_2) = g_2$ and $P_1 P_2$ separable, the pair $(A_1, A_2)$ satisfies the unit identity. The *unit lemma for the group* is the statement: for every odd $K$ and all $A_1$, $A_2$ with $g_1\sigma(g_1) = 1$, $g_2\sigma(g_2) = 1$ and $P_1P_2$ separable, the pair satisfies the unit identity.

The separability of $P_1 P_2$ says that $g = (g_1, g_2)$ is regular semisimple and that $P_1$ and $P_2$ have no common root, so the resultant is not $0$.

For a small $a$, a positive $x$ and a real number $\ell$, say that $\ell$ is a *linear limit* at $x$ if $G(x a^{2k})/\rho(a^k) \to \ell$ as $k \to \infty$.

**Theorem 4.7.3 (Linear descent).** Let $K$ be an unramified quadratic datum and $A_1$, $A_2$ algebras with involution with $\sigma(g_i) = g_i$ and $P_1P_2$ separable. Let $a$ be small. Let $\ell$, $\ell_1$, $\ell_2$ be real functions on $A_1 \times A_2$, $A_1$, $A_2$ such that $\ell(x)$, $\ell_1(x)$, $\ell_2(x)$ are linear limits at every positive $x$ of the respective algebra. Then
$$\begin{aligned}
\sum_{k \in \mathrm{Cl}(A_1 \times A_2)} \eta\big(N_{A_1/E}(y_{k,1})\big)\, \ell(y_k) &= (-q)^{\mathrm{val}(\mathrm{Res}(P_1, P_2))} \\
&\quad \cdot \Big(\sum_{k \in \mathrm{Cl}(A_1)} \eta\big(N_{A_1/E}(y_k)\big)\, \ell_1(y_k)\Big) \Big(\sum_{k \in \mathrm{Cl}(A_2)} \ell_2(y_k)\Big).
\end{aligned}$$

Lean: `GlobalTheory.UnitLemma.Desc.linearDescent` (also `GlobalTheory.T.linearLatticeCountDescent_proof`, a second name).

*Proof.* We give the structure of the proof; the lemmas it uses are proved in other files.

Step 1: frames. Since $P$ is separable, $A$ is a product of fields. Group the factors into orbits of $\sigma$. This gives complete orthogonal idempotents $e_i$, $i \in \iota$, and a subset $S \subseteq \iota$: for $i \in S$, $e_i$ is fixed by $\sigma$ and $e_iA$ is a field; for $i \notin S$, $e_i = f + \sigma(f)$ with $f\sigma(f) = 0$. For each $i \in S$ choose a positive $\pi_i$ with $\pi_i(1 - e_i) = 1 - e_i$ and $\eta(N_{A/E}(\pi_i)) = -1$. Such a choice is a *frame*. For $I \subseteq S$ put $e_I = \sum_{i \in I} e_i$ and $\chi_I(y) = \eta\big(N_{A/E}(y e_I + 1 - e_I)\big)$, and for $J \subseteq S$ put $\pi_J = \prod_{j \in J} \pi_j$.

Step 2: the sum formula. Let $A$ be Lie regular with a frame, and let $\ell$ be a function with linear limits at every positive $x$. For $I \subseteq S$ let
$$h(I) = \sum_{J \subseteq S} (-1)^{|J \cap I|}\, \ell(\pi_J).$$
A lemma of the linear descent gives, at each positive $x$, $\sum_{J} (-1)^{|J \cap I|} \ell(\pi_J x) = \chi_I(x)\, h(I)$. The set $\mathrm{Cl}(A)$ is finite, and orthogonality of the characters $\chi_J$ on it gives
$$\sum_{k \in \mathrm{Cl}(A)} \chi_I(y_k)\, \ell(y_k) = \frac{|\mathrm{Cl}(A)|}{2^{|S|}}\, h(I).$$

Step 3: the product. Frames for $A_1$ and $A_2$ give a frame for $A_1 \times A_2$, indexed by $\iota_1 \sqcup \iota_2$ with $S = S_1 \sqcup S_2$. Take $I = S_1$ in $A_1$, $I = \emptyset$ in $A_2$, and $I = S_1$ in the product. Then $\chi_{S_1}(y) = \eta(N_{A_1/E}(y))$ on $A_1$ and on the product, and $\chi_\emptyset = 1$. A comparison of the signed counts of the product with those of the factors, with $\rho$ for the product equal to the product of the $\rho$ for the factors, gives
$$h(S_1) = (-q)^{\mathrm{val}(\mathrm{Res}(P_1, P_2))}\, h_1(S_1)\, h_2(\emptyset).$$

Step 4. Insert Step 3 in the sum formula for the three algebras, and use $|\mathrm{Cl}(A_1 \times A_2)| = |\mathrm{Cl}(A_1)|\,|\mathrm{Cl}(A_2)|$ and $2^{|S_1 \sqcup S_2|} = 2^{|S_1|}2^{|S_2|}$. $\square$

**Theorem 4.7.4 (Lie algebra case).** Assume the count identity, the unitary limit and linear descent, as statements for all data. Then the unit lemma for the Lie algebra holds.

Lean: `GlobalTheory.T.unitLemmaSelfAdjointLie_of_count_limit_descent` (also `GlobalTheory.UnitLemma.LieEnd.unitLemmaLie_of`, a second name).

*Proof.* Let $A_1$, $A_2$ be as in the unit lemma. Then $A_1$, $A_2$ and $A_1 \times A_2$ are Lie regular. Let $p$ be a uniformizer of $\mathcal{O}$; then $a = p\, c(p)$ is small.

Step 1: linear limits. Let $A$ be Lie regular and $x$ positive. Since $\sigma(a) = a$, we have $x a^{2k} = x\, a^k \sigma(a^k)$, and $a^k$ is a unit of $A$. By the count identity, $G(x a^{2k}) = U(x, a^k)$. By the unitary limit, $G(xa^{2k})/\rho(a^k) \to N(x)$. So $N$ gives linear limits, and linear descent gives
$$\sum_{\mathrm{Cl}(A_1 \times A_2)} \eta(N_{A_1/E}(y_{k,1}))\, N(y_k) = (-q)^{v} \Big(\sum_{\mathrm{Cl}(A_1)} \eta(N_{A_1/E}(y_k))\, N(y_k)\Big)\, S(A_2),$$
with $v = \mathrm{val}(\mathrm{Res}(P_1, P_2))$.

Step 2: a degenerate trace form. Suppose $\delta_1(1) = 0$. Then there is $y \neq 0$ in $A_1$ with $\mathrm{Tr}_{A_1/E}(yz) = 0$ for all $z$. If $L \in X(x)$, then self-duality puts $yA_1$ in $L$, and the image of $L$ under a linear form that is $1$ at $y$ is all of $E$. But $L$ is finitely generated over $\mathcal{O}$ and $E$ is not. So $X(x)$ is empty for every $x$, in $A_1$ and in the product (use $(y, 0)$). Then $N = 0$ everywhere, and both sides of the unit identity are $0$.

Step 3: the general case. Suppose $\delta_1(1) \neq 0$. For a unit $x$, $\delta_1(x) = N_{A_1/E}(x)\, \delta_1(1)$, so $\eta(N_{A_1/E}(x)) = \eta(\delta_1(1))\, \eta(\delta_1(x))$. If $X(x)$ is not empty, a self-dual lattice gives $\eta(\delta_1(x)) = 1$. So the left side of Step 1 is $\eta(\delta_1(1))\, \kappa(A_1, A_2)$, and the sum over $\mathrm{Cl}(A_1)$ is $\eta(\delta_1(1))\, S(A_1)$. Multiply by $\eta(\delta_1(1))$, which squares to $1$, and by $(-q)^{-v}$. $\square$

**Theorem 4.7.5 (Group case).** The unit lemma for the Lie algebra implies the unit lemma for the group.

Lean: `GlobalTheory.T.unitLemma_unitary_group_odd_residue_of_lie` (also `GlobalTheory.UnitLemma.Orbit.unitLemmaGroup_of_lie`, a second name).

*Proof.* Let $K$ be odd and $A_1$, $A_2$ as in the unit lemma for the group. If $g_1$ or $g_2$ is not integral over $\mathcal{O}$, then $\kappa(A_1, A_2) = 0$ and $S(A_1)S(A_2) = 0$, so the identity holds. Suppose both are integral. We use strong induction on $\dim A_1 + \dim A_2$. Let $R = \mathcal{O}[g] \subseteq A_1 \times A_2$.

Case 1: $R$ has an idempotent $e \neq 0, 1$ with $\sigma(e) = e$. Then $e$ is a polynomial in $g$, and cutting by $e$ and $1 - e$ splits $A_1$ and $A_2$ into smaller algebras with unitary, integral elements. The unit identity is invariant under isomorphism of algebras with involution. By induction, the identity holds for the two pieces. Since $e$ is a polynomial in $g$ over $\mathcal{O}$, the resultants between pieces cut by $e$ and by $1 - e$ are units, and a product lemma gives the identity for $(A_1, A_2)$.

Case 2: every $\sigma$-fixed idempotent of $R$ is $0$ or $1$. Then either $R$ has an idempotent $e$ with $e + \sigma(e) = 1$, and a direct lemma gives the identity; or $R$ is a local ring, and a lemma reduces the identity to the unit lemma for the Lie algebra. This last step is the one that uses that $2$ is a unit. $\square$

**Theorem 4.7.6 (Unit lemma).** Assume that the fundamental lemma holds in every rank. Then the unit lemma for the Lie algebra and the unit lemma for the group hold.

Lean: `GlobalTheory.UnitLemma.unitLemma_lie_and_group` (also `GlobalTheory.T.unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis`, a second name).

*Proof.* The [count identity](/entry/count-identity-of-unit-match/) follows from the fundamental lemma. With the [unitary limit](/entry/unitary-limit/) and [linear descent](/entry/linear-descent/), the Lie algebra case gives the unit lemma for the Lie algebra. The group case then gives the unit lemma for the group. $\square$

With the [fundamental lemma in every rank](/entry/unit-match-all/), the hypothesis holds, so both unit lemmas hold outright.

**Remark 4.7.7 (Formalization).** The sums over $\mathrm{Cl}(A)$ are `finsum`, which is $0$ when the support is infinite ([UnitLemmaGroup.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnitLemmaGroup.lean#L43)); finiteness of $\mathrm{Cl}(A)$ for separable $P$ is a lemma used inside the descent. The representatives $y_k$ are chosen with `Quot.out`, and the basis in $\delta$ is `Module.finBasis`, so the independence of the choices shown above is a fact about the definitions, not part of them. The exponent of $-q$ is $-\mathrm{val}$ in the unit identity and $+\mathrm{val}$ in linear descent, since they are on opposite sides. The two users of this theorem take only the Lie algebra part ([UnitLemmaUnramifiedProductUnitaryGroups.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitLemmaUnramifiedProductUnitaryGroups.lean#L13), [CongruenceSubgroupIndicatorWeight.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeight.lean#L49)). The first one derives the group case for every residue characteristic from the Lie part, in a file that repeats most of the group case proof without the oddness hypothesis ([UnitLemmaUnitaryGroupEveryResidueOfLie.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitLemmaUnitaryGroupEveryResidueOfLie.lean#L20)). So the oddness hypothesis of the group case here is never needed downstream.
