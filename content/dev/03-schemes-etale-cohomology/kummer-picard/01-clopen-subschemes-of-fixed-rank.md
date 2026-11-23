---
title: Clopen subschemes of fixed rank
decls:
  - UpperTheory.exists_clopRepOfRank_of_locallyNoetherian
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Clopen subschemes of fixed rank

Let $G \to S$ be a finite étale morphism. For an $S$-scheme $T$, an open and closed subscheme of $G_T = T \times_S G$ is again finite étale over $T$. This section proves that the clopen subschemes of a fixed rank $r$ have a moduli space: an $S$-scheme $Y_r$ with a universal clopen subscheme $U_r$ of $G_{Y_r}$. The construction takes the Hilbert scheme of finite flat subschemes of rank $r$ of $G$ and shows that its universal family is already open. The finite étale scheme that represents all clopen subschemes of $G$ is built from these pieces in [Theorem 5.1.4](/entry/exists-finite-etale-representing-clopen-subschemes/), which uses this result for each rank $r$.

Recall that a morphism is [finite étale](/learn/geometry/#schemes-and-varieties) if it is finite and étale, and that a subset of a topological space is *clopen* if it is open and closed ([[clopen set|DQ4E55T3BW]]). For a morphism $y : T \to Y$ of $S$-schemes we write $y \times 1 : G_T \to G_Y$ for its base change.

**Definition 6.1.1 (Rank).** Let $f : V \to T$ be finite and locally free. For $t \in T$ the stalk $(f_*\mathcal{O}_V)_t$ is a free $\mathcal{O}_{T,t}$-module of finite rank. This rank is the *rank of $f$ at $t$*. The morphism $f$ has *constant rank $r$* if its rank at each point of $T$ is $r$.

**Lemma 6.1.2.** Let $G \to S$ be finite étale, let $T$ be an $S$-scheme and let $V \subseteq G_T$ be an open subscheme whose underlying set is closed. Then the projection $V \to T$ is finite étale.

Lean: `UpperTheory.clopProj_finite_etale_of_isClosed`.

*Proof.* The projection $G_T \to T$ is the base change of $G \to S$, so it is finite étale. The inclusion $V \to G_T$ is an open immersion, so it is étale. Its image is closed, so it is also a closed immersion, and a closed immersion is finite. A composite of finite étale morphisms is finite étale. $\square$

**Definition 6.1.3 (Clopen subscheme of rank $r$).** Let $G \to S$ be finite étale and $T$ an $S$-scheme. A *clopen subscheme of $G_T$* is an open subscheme $V \subseteq G_T$ whose underlying set is closed. By the Lemma, $V \to T$ is finite étale. The subscheme $V$ has *rank $r$* if $V \to T$ has constant rank $r$.

**Definition 6.1.4 (Classifying pair).** Fix $r \ge 0$. A pair $(Y, U)$, with $Y$ an $S$-scheme and $U$ a clopen subscheme of $G_Y$ of rank $r$, *classifies the clopen subschemes of rank $r$* if the following holds. For each $S$-scheme $T$ and each clopen subscheme $V$ of $G_T$ of rank $r$, there is exactly one $S$-morphism $y : T \to Y$ with $(y \times 1)^{-1}(U) = V$.

So $Y$ represents the functor that sends $T$ to the set of clopen subschemes of $G_T$ of rank $r$, and $U$ is the universal object.

**Example 6.1.5.** Let $S = \operatorname{Spec} k$ with $k$ a field, and let $G$ be the disjoint union of $n$ copies of $S$. For a connected $S$-scheme $T$, the scheme $G_T$ is the disjoint union of $n$ copies of $T$, and a clopen subscheme of rank $r$ is the union of $r$ of these copies. So we can take for $Y_r$ the disjoint union of $\binom{n}{r}$ copies of $S$, one for each subset of size $r$ of the $n$ points, and for $U_r$ the obvious subscheme. For a general $T$, a clopen subscheme of rank $r$ picks a subset of size $r$ of the $n$ points at each point of $T$, and this choice is locally constant on $T$. Such a choice is the same as a morphism $T \to Y_r$.

The proof uses one fact about immersions.

**Lemma 6.1.6 (Flat closed immersions are open).** Let $p : X \to T$ be étale and let $v : V \to X$ be a closed immersion. If $p \circ v$ is flat and locally of finite presentation, then $v$ is an open immersion.

Lean: `UpperTheory.isOpenImmersion_of_closedImmersion_flat_etale`.

*Proof.* A closed immersion is unramified, so $v$ is unramified. The map $p$ is étale, so it is unramified, and the composite $p \circ v$ is unramified. It is flat and locally of finite presentation by assumption, so $p \circ v$ is étale. Now $v$ is the composite of its graph $\Gamma_v : V \to V \times_T X$ and the second projection $V \times_T X \to X$. The graph is a section of the first projection $V \times_T X \to V$, which is unramified as a base change of $p$, and a section of an unramified morphism is an open immersion, since it is a base change of the diagonal and the diagonal of an unramified morphism is an open immersion. The second projection is étale as a base change of $p \circ v$. So $v$ is étale. A closed immersion is a monomorphism. An étale monomorphism is an open immersion (EGA IV, Théorème 17.9.1). So $v$ is an open immersion. $\square$

**Theorem 6.1.7.** Let $S$ be a locally noetherian scheme, let $G \to S$ be finite étale and let $r \ge 0$. Then there is a pair $(Y, U)$ that classifies the clopen subschemes of $G$ of rank $r$.

Lean: `UpperTheory.exists_clopRepOfRank_of_locallyNoetherian`.

*Proof.* The proof has three steps.

1. *The Hilbert scheme.* The morphism $G \to S$ is finite, flat and of finite presentation, since it is finite étale. So the Hilbert scheme of finite flat subschemes, [Theorem 2.16.6](/entry/hilbert-scheme-finite-locally-free-representable-proper/), gives a proper $S$-scheme $h : H \to S$ and a closed subscheme $u : U_0 \to G_H$ that is finite and flat of constant rank $r$ over $H$. The pair is universal: for each $S$-scheme $T$ and each closed subscheme $V$ of $G_T$ that is finite and flat of constant rank $r$ over $T$, there is exactly one $S$-morphism $f : T \to H$ such that $V$ is the fibre product of $U_0$ and $G_T$ over $G_H$.

2. *The universal family is open.* The scheme $H$ is of finite type over the locally noetherian $S$, so it is locally noetherian. The projection $G_H \to H$ is étale, as a base change of $G \to S$. The composite $U_0 \to G_H \to H$ is finite and flat, and of finite presentation since $H$ is locally noetherian. By the Lemma on flat closed immersions, $u$ is an open immersion. Its image is closed, since $u$ is a closed immersion. So $U_0$ is a clopen subscheme of $G_H$ of rank $r$. Put $Y = H$ and $U = U_0$.

3. *Universality.* Let $V$ be a clopen subscheme of $G_T$ of rank $r$. By the first Lemma, $V \to T$ is finite étale, so it is finite and flat of constant rank $r$. The inclusion $V \to G_T$ is a closed immersion, since its image is closed. So step 1 gives exactly one $f : T \to H$ such that $V$ is the fibre product of $U_0$ along $f \times 1$. For an open subscheme of $G_H$, the fibre product along $f \times 1$ is the open subscheme $(f \times 1)^{-1}(U_0)$. So the condition on $f$ is $(f \times 1)^{-1}(U) = V$, and $f$ is the unique such morphism. $\square$

**Remark 6.1.8 (Formalization).** The hypothesis that $S$ is locally noetherian is used once: it makes $H$ locally noetherian, so that $U_0 \to H$ is of finite presentation. The Hilbert scheme theorem itself has no noetherian hypothesis. The rank is defined through the rank of the free module $(f_*\mathcal{O}_V)_t$, and we did not unfold this definition further. The classifying pair is stated for the product $Y \times_S G$, while the Hilbert scheme uses $G \times_S H$; the two are identified by the symmetry isomorphism.
