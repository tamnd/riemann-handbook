---
title: Biduality
decls:
  - GlobalTheory.BidualAbelian.fibre_isIso
  - GlobalTheory.T.isDualAbelianSchemePoincare_swap
  - GlobalTheory.BidualAbelian.isDual_swap
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Biduality

Let $(B, P)$ be a dual of an abelian scheme $A$ over a scheme $S$. This section proves that $(A, s^* P)$ is a dual of $B$, where $s : B \times A \to A \times B$ swaps the factors (Theorem (Biduality)). This is fact 7 of the section on the dual abelian scheme over any base, and it gives property 4 of Theorem (Dual abelian scheme) there. The proof compares $A$ with a dual $C$ of $B$ through the map $\kappa : A \to C$ that classifies $s^* P$. On each geometric fibre, $\kappa$ is a monomorphism by the theorem of the last section, and so an isomorphism. A fibrewise isomorphism of abelian schemes is an isomorphism.

Let $S$ be a scheme. All products are over $S$. For a line bundle $P$ on $A \times B$ we write $s^* P$ for its pullback to $B \times A$ along the swap of factors. For $\kappa : A \to C$ and a line bundle $Q$ on $B \times C$ we write $(1 \times \kappa)^* Q$ for its pullback to $B \times A$. The notions of a dual and of a group $B$ that keeps the dimension of $A$ are as in the second section of this chapter.

We use the following facts.

1. (Base change of duals.) If $(B, P)$ is a dual of $A$ and $S_1 \to S$ is a morphism, then $(B \times_S S_1, P_1)$ is a dual of $A \times_S S_1$, where $P_1$ is the pullback of $P$.
2. (Dimension over a field.) An abelian scheme over $\mathrm{Spec}\, \Omega$, with $\Omega$ a field, is smooth of relative dimension $g$ for some $g$.
3. (Monomorphisms of abelian schemes.) Let $S$ be locally noetherian, $B$ and $B'$ abelian schemes over $S$, smooth of relative dimensions $g$ and $g'$ with $g' \leq g$, and $x : B \to B'$ a homomorphism that is a monomorphism. Then $x$ is an isomorphism.
4. (Additivity in the second variable.) Let $B$ be an abelian scheme and $(B, P)$ a dual of $A$. Then $s^* P$ is an additive family on $B \times A$: $P(a, b b') \cong P(a, b) \otimes P(a, b')$ for all points $a$ of $A$ and $b, b'$ of $B$.
5. (Classifying maps are homomorphisms.) Let $(B', P')$ be a dual of $A$ such that $s^* P'$ is additive, and let $P$ be a line bundle on $A \times B$ such that $s^* P$ is additive. If $x : B \to B'$ satisfies $P \cong (1 \times x)^* P'$, then $x$ is a homomorphism.
6. (Fibrewise isomorphisms.) Let $B$ and $D$ be abelian schemes over $S$ and $x : B \to D$ a morphism over $S$. If the base change of $x$ along each $\mathrm{Spec}\, \Omega \to S$ with $\Omega$ algebraically closed is an isomorphism, then $x$ is an isomorphism.
7. (Transport.) Let $(B', P')$ be a dual of $A$, $P$ a line bundle on $A \times B$, and $x : B \to B'$ an isomorphism of groups with $P \cong (1 \times x)^* P'$. Then $(B, P)$ is a dual of $A$.

Fact 3 holds because a monomorphism of proper schemes is a closed immersion, and a closed subgroup of the same or larger dimension in an abelian scheme with connected fibres is everything. Fact 4 is a form of the theorem of the cube ([Volume 1](/learn/abelian-varieties/#the-theorem-of-the-cube)). In fact 5, additivity of $s^* P$ says that $b \mapsto P_b$ is a homomorphism of group functors, and the uniqueness in the universal property of $P'$ makes $x$ one too. Fact 6 is the fibrewise criterion for an isomorphism of proper flat schemes of finite presentation.

**Proposition 1.10.1 (Fibrewise isomorphism).** Let $A$, $B$ and $C$ be abelian schemes over $S$. Suppose that $B$ keeps the dimension of $A$ and $C$ keeps the dimension of $B$, that $(B, P)$ is a dual of $A$ and $(C, Q)$ is a dual of $B$, and that $\kappa : A \to C$ is a homomorphism with $s^* P \cong (1 \times \kappa)^* Q$ on $B \times A$. Then for each algebraically closed field $\Omega$ and each $t : \mathrm{Spec}\, \Omega \to S$, the base change $\kappa_\Omega : A_\Omega \to C_\Omega$ is an isomorphism.

Lean: `GlobalTheory.BidualAbelian.fibre_isIso`.

*Proof.* The base changes $A_\Omega$, $B_\Omega$ and $C_\Omega$ are abelian schemes over $\Omega$. By fact 2, $A_\Omega$ is smooth of relative dimension $g$ for some $g$. Since $B$ keeps the dimension of $A$, $B_\Omega$ is smooth of relative dimension $g$, and in the same way so is $C_\Omega$. By fact 1, $(B_\Omega, P_\Omega)$ is a dual of $A_\Omega$.

We show that $\kappa_\Omega$ is a monomorphism. Let $T$ be an $\Omega$-scheme and $x, y \in A_\Omega(T)$ with $\kappa_\Omega x = \kappa_\Omega y$. Put $z = x y^{-1}$. Since $\kappa$ is a homomorphism, $\kappa_\Omega z = 1$. For a point $b$ of $B_\Omega$,
$$P_\Omega(z, b) \cong (s^* P)(b, z) \cong Q(b, \kappa z) = Q(b, 1),$$
and $Q(b, 1)$ is trivial since $(C, Q)$ is a dual of $B$. So $(z \times 1)^* P_\Omega$ is trivial on $T \times B_\Omega$. By [Theorem 1.9.3](/entry/dual-poincare-left-kernel-trivial-alg-closed/) (Left kernel), $z = 1$, so $x = y$.

So $\kappa_\Omega$ is a homomorphism and a monomorphism between abelian schemes over $\mathrm{Spec}\, \Omega$ of the same relative dimension $g$. By fact 3 it is an isomorphism. $\square$

**Theorem 1.10.2 (Biduality).** Let $A$ and $B$ be abelian schemes over $S$ such that $B$ keeps the dimension of $A$, and let $(B, P)$ be a dual of $A$. Then $(A, s^* P)$ is a dual of $B$.

Lean: `GlobalTheory.BidualAbelian.isDual_swap` (also `GlobalTheory.T.isDualAbelianSchemePoincare_swap`, a second name).

*Proof.* By [Theorem 1.6.3](/entry/exists-dual-abelian-scheme-poincare/) (Existence), there are an abelian scheme $C$ over $S$ that keeps the dimension of $B$ and a line bundle $Q$ on $B \times C$ such that $(C, Q)$ is a dual of $B$. By fact 4, $s^* P$ is an additive family on $B \times A$. By the universal property of $(C, Q)$ there is $\kappa : A \to C$ with $s^* P \cong (1 \times \kappa)^* Q$.

The map $\kappa$ is a homomorphism by fact 5, applied to the dual $(C, Q)$ of $B$ and to the bundle $s^* P$ on $B \times A$: the swap of $Q$ is additive by fact 4, since $C$ is an abelian scheme, and the swap of $s^* P$ is $P$, which is additive. By Proposition (Fibrewise isomorphism), $\kappa$ is an isomorphism on each geometric fibre, so by fact 6 it is an isomorphism. By fact 7, applied to $(C, Q)$, $s^* P$ and $\kappa$, the pair $(A, s^* P)$ is a dual of $B$. $\square$

The theorem uses the existence of a dual of $B$, and the existence theorem of the section on the dual abelian scheme does not use biduality. So the two results do not depend on each other in a circle; only Theorem (Dual abelian scheme) uses both.

**Remark 1.10.3 (Formalization).** Facts 1 to 7 are `GlobalTheory.IsDual.baseChange`, `GlobalTheory.AbelianDim.exists_relDim`, `GlobalTheory.AbMonoIso.isIso_of_mono`, `GlobalTheory.AbDual.isDual_isAdditive_swap`, `GlobalTheory.AbDual.isMonHom_of_classifying`, `GlobalTheory.AbDual.isIso_of_isIso_pullback` and `GlobalTheory.AbDual.transport`. They are cited by their statements; the sentences on why they hold are not read from proofs. The proof of the proposition calls Theorem (Left kernel) by its second name. The swap of the swap of $P$ is additive by `GlobalTheory.BidualAbelian.isAdditive_swap_swap`. The proposition asks that $\kappa$ be a homomorphism and uses it only for $\kappa_\Omega z = 1$. The second name of the theorem is closed by a `first` list under `set_option maxHeartbeats 1000000`.
