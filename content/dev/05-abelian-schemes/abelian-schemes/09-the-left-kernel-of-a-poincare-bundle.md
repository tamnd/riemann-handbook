---
title: The left kernel of a Poincaré bundle
decls:
  - GlobalTheory.T.exists_nontrivial_additive_family_killed_by_isogeny
  - GlobalTheory.CharKer.exists_nontriv_family
  - GlobalTheory.T.dualPoincare_left_kernel_trivial_algClosed
  - GlobalTheory.DualKer.leftKer_eq_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The left kernel of a Poincaré bundle

Let $(B, P)$ be a dual of an abelian variety $A$ over an algebraically closed field. The bundle $P$ is a family of line bundles on $A$ parametrized by $B$. Read the other way, it is a family of line bundles on $B$ parametrized by $A$. Biduality says that this second family identifies $A$ with the dual of $B$. Its first part is injectivity: a point $x$ of $A$ for which $P$ is trivial on $\{x\} \times B$ is the identity (Theorem (Left kernel)). The next section uses this on geometric fibres to prove biduality over any base. The proof divides $A$ by the subgroup of such points and uses characters of a finite group scheme to produce an additive family that contradicts the universal property of $P$.

Let $K$ be an algebraically closed field. In this section all schemes are $K$-schemes, an abelian variety is an [[abelian scheme|JDDXZ89N33]] over $\mathrm{Spec}\, K$, and products are over $K$. For a $K$-scheme $T$ and $x \in A(T)$ we write $(x \times 1)^* P$ for the pullback of $P$ along $x \times 1 : T \times B \to A \times B$. We write $1$ for the constant morphism to the identity of a group. A line bundle is *trivial* if it is isomorphic to the structure sheaf. Additive families and duals are as defined in the second section of this chapter.

**Definition 1.9.1 (Character).** Let $N$ be a commutative group over $K$ and $T$ a $K$-scheme. A *character of $N$ over $T$* is a unit $\chi \in \Gamma(N \times T, \mathcal{O})^\times$ such that $\chi(n n', t) = \chi(n, t)\, \chi(n', t)$ for all points $n, n'$ of $N$ and $t$ of $T$ with values in a common scheme.

So a character over $T$ is a homomorphism $N \times T \to \mathbb{G}_{m, T}$ of groups over $T$. If $N$ is finite, the characters are the points of the Cartier dual of $N$, and the universal character lives over $T = N^D$. For $N = \mu_p$ in characteristic $p$, the Cartier dual is $\mathbb{Z}/p$, and a character over $T = \mathrm{Spec}\, K$ is the $k$-th power map for some $k \in \mathbb{Z}/p$.

We use five facts on characters and descent. Let $A$ and $A'$ be abelian varieties, $N$ a group, $i : N \to A$ and $q : A \to A'$ homomorphisms, with $q$ finite, flat and surjective, and $N$ the kernel of $q$, that is, the square formed by $i$, $N \to \mathrm{Spec}\, K$, $q$ and the identity of $A'$ is cartesian.

1. (Characters exist.) Let $N$ be a finite commutative group over $K$ whose identity morphism is not the constant morphism $1$. Then there are a $K$-scheme $T$ and a character $\chi \neq 1$ of $N$ over $T$.
2. (Descent along a character.) For each $K$-scheme $T$ and each character $\chi$ of $N$ over $T$, there are a line bundle $M$ on $A' \times T$, given by an open cover $(V_k)$ and transition units $g_{kl}$, and units $e_k$ on $(q \times 1)^{-1}(V_k)$, such that $e_k = (q \times 1)^* g_{kl} \cdot e_l$ on overlaps and $e_k(a \cdot i(n), t) = \chi(n, t)\, e_k(a, t)$.
3. (Additivity.) Each $M$ as in fact 2 is an additive family.
4. (Trivial pullback.) Let $M$ be a line bundle on $Y$, given by a cover $(V_k)$ and transition units $g_{kl}$, and $p : X \to Y$ a morphism. If there are units $e_k$ on $p^{-1}(V_k)$ with $e_k = p^* g_{kl} \cdot e_l$ on overlaps, then $p^* M$ is trivial.
5. (Faithfulness.) If $M$ as in fact 2 is trivial, then $\chi = 1$.

In fact 2, $A \times T \to A' \times T$ is an $N$-torsor, and $M$ is the descent of the trivial bundle with the action of $N$ twisted by $\chi$; the units $e_k$ are the images of the generator $1$. Fact 4 holds because the pulled back cocycle is a coboundary.

**Proposition 1.9.2 (A family killed by an isogeny).** Let $A$ and $A'$ be abelian varieties, $N$ a group, and $i : N \to A$ and $q : A \to A'$ homomorphisms. Suppose that $N$ is finite over $K$, $q$ is finite, flat and surjective, $N$ is the kernel of $q$ in the sense above, and $i \neq 1$. Then there are a $K$-scheme $T$ and an additive family $M$ on $A' \times T$ such that $(q \times 1)^* M$ is trivial and $M$ is not trivial.

Lean: `GlobalTheory.CharKer.exists_nontriv_family` (also `GlobalTheory.T.exists_nontrivial_additive_family_killed_by_isogeny`, a second name).

*Proof.* The map $i$ is a monomorphism, as the base change of the monomorphism $\mathrm{Spec}\, K \to A'$. An abelian variety is commutative, so $N$, a subgroup of $A$, is commutative. If the identity of $N$ were the constant morphism $1$, then $i = i \circ \mathrm{id}_N = i \circ 1 = 1$, which is false. So fact 1 gives $T$ and a character $\chi \neq 1$ of $N$ over $T$. Fact 2 gives $M$ and $e$. By fact 3, $M$ is additive. The units $e_k$ satisfy the condition of fact 4 for $p = q \times 1$, so $(q \times 1)^* M$ is trivial. If $M$ were trivial, fact 5 would give $\chi = 1$. So $M$ is not trivial. $\square$

In the language of duals, the proposition says that the dual isogeny $A'^\vee \to A^\vee$ has a nontrivial kernel when $N$ is nontrivial. Classically this kernel is the Cartier dual of $N$.

We use seven more facts. Let $A$ and $B$ be abelian varieties and $(B, P)$ a dual of $A$.

6. (The left kernel is a subgroup.) There are a group $N$ and a homomorphism $i : N \to A$, a closed immersion, such that $(i \times 1)^* P$ is trivial on $N \times B$, and such that every $x \in A(T)$ with $(x \times 1)^* P$ trivial factors through $i$.
7. (A finite kernel.) There are a line bundle $L$ on $A$, a finite group $H$ over $K$ and a homomorphism $j : H \to A$, a closed immersion, such that for each $T$ and $x \in A(T)$, $x$ lies in $K(L)$ if and only if $x$ factors through $j$.
8. (Left kernel and $K(L)$.) Let $L$ be a line bundle on $A$. If $(x \times 1)^* P$ is trivial, then $x$ lies in $K(L)$.
9. (Quotients.) Let $H$ be finite over $K$ and $i : H \to A$ a homomorphism and a monomorphism. Then there are an abelian variety $A'$ and a homomorphism $q : A \to A'$, finite, flat and surjective, with kernel $H$.
10. (Dimension of a quotient.) Let $q : A \to A'$ be a finite surjective morphism of abelian varieties. If $A$ is smooth of relative dimension $g$, so is $A'$.
11. (Descent of $P$.) Let $N$, $i$, $q$ and $A'$ be as in Proposition (A family killed by an isogeny), and suppose that $(i \times 1)^* P$ is trivial. Then there is an additive family $P'$ on $A' \times B$ with $(q \times 1)^* P' \cong P$.
12. (Rigidity.) Let $A'$ and $B$ be smooth of relative dimension $g$, $q : A \to A'$ a homomorphism, and $P'$ an additive family on $A' \times B$ with $(q \times 1)^* P' \cong P$. Then each additive family $M$ on $A' \times T$ with $(q \times 1)^* M$ trivial is trivial.

Fact 7 is the finiteness of $K(L)$ for an ample line bundle $L$ ([Volume 1](/learn/abelian-varieties/#the-theorem-of-the-cube)), and fact 9 is the quotient of an abelian variety by a finite subgroup scheme.

**Theorem 1.9.3 (Left kernel).** Let $A$ and $B$ be abelian varieties, both smooth of relative dimension $g$, and let $(B, P)$ be a dual of $A$. Let $T$ be a $K$-scheme and $x \in A(T)$. If $(x \times 1)^* P$ is trivial on $T \times B$, then $x = 1$.

Lean: `GlobalTheory.DualKer.leftKer_eq_one` (also `GlobalTheory.T.dualPoincare_left_kernel_trivial_algClosed`, a second name).

*Proof.* Let $i : N \to A$ be the subgroup of fact 6, and $L$, $j : H \to A$ as in fact 7. Apply fact 8 to the point $i \in A(N)$: it lies in $K(L)$, so by fact 7 it factors as $i = j \circ z$. Since $i$ and $j$ are closed immersions, so is $z$, and $N$ is finite over $K$ because $H$ is. By fact 9 there is $q : A \to A'$, finite, flat and surjective, with kernel $N$. By fact 10, $A'$ is smooth of relative dimension $g$. By fact 11 there is an additive family $P'$ on $A' \times B$ with $(q \times 1)^* P' \cong P$.

Suppose that $i \neq 1$. Proposition (A family killed by an isogeny) gives $T'$ and a nontrivial additive family $M$ on $A' \times T'$ with $(q \times 1)^* M$ trivial. This contradicts fact 12. So $i = 1$.

Now let $x \in A(T)$ with $(x \times 1)^* P$ trivial. By fact 6, $x = i \circ w$ for some $w : T \to N$. Then $x = 1 \circ w = 1$. $\square$

So the map from $A$ to the dual of $B$ given by $P$ is a monomorphism of group functors. Over a field this is the first half of biduality.

**Remark 1.9.4 (Formalization).** Facts 1 to 5 are `GlobalTheory.T.exists_nontrivial_character_finite_comm_group`, `GlobalTheory.T.exists_descended_lineBundle_equivariantGenerator`, `GlobalTheory.T.characterLineBundle_additive_of_equivariantGenerator`, `GlobalTheory.T.cechTrivial_pullback_of_isPullbackGenerator` and `GlobalTheory.T.character_eq_one_of_descended_lineBundle_trivial`. Facts 6 to 12 are `GlobalTheory.T.exists_closedSubgroupScheme_poincare_left_kernel`, `GlobalTheory.T.exists_ample_kernel_finite_subgroupScheme`, `GlobalTheory.T.mem_kernelOfLineBundle_of_dualPair_left_trivial`, `GlobalTheory.T.exists_quotient_abelianVariety_finite_subgroupScheme`, `GlobalTheory.T.smoothOfRelativeDimension_finite_surjective_abelianVariety`, `GlobalTheory.T.poincareBundle_descends_quotient_finiteSubgroup` and `GlobalTheory.T.additiveFamily_trivial_of_quotient_pullback_trivial`. They are cited by their statements; the sentences on why they hold are not read from proofs. In facts 2, 4 and 5 the line bundle $M$ is given with its cover and transition units. Fact 7 also says that $A$ is projective and that a theta bundle of $L$ has a generating section; the proof drops these outputs. Fact 8 holds for every line bundle $L$, with no ampleness. The finiteness of $N$ is `GlobalTheory.DualKer.finite_of_factor`. The theorem calls the proposition by its second name. The second names are closed by a `first` list under `set_option maxHeartbeats 1000000`.
