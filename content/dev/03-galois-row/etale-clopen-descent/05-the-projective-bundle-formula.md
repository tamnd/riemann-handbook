---
title: The projective bundle formula
decls:
  - UpperTheory.Pbf.pbf_all
  - UpperTheory.Cb.etaleCohomology_projectiveBundle_formula
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The projective bundle formula

Let $V$ be a vector bundle of rank $N$ on a scheme $U$, let $\pi : \mathbb{P}(V) \to U$ be its projective bundle, and let $L$ be the tautological line bundle on $\mathbb{P}(V)$. The projective bundle formula says that the étale cohomology of $\mathbb{P}(V)$ is free over the cohomology of $U$, with basis $1, c_1(L), \dots, c_1(L)^{N-1}$. This section proves the formula in the model of étale cohomology of the code. The proof is an induction on $N$ that joins four lemmas, one for each case. In this model each bundle on a scheme is trivial, so the formula is really about $U \times \mathbb{P}^{N-1}$.

We use the model of [the projective bundle formula on discrete spaces](/entry/pbf-disc/). A *space* is a simplicial presheaf on schemes. A scheme $U$ gives the discrete space $\mathrm{sch}(U)$. The space $B\mathrm{GL}_N$ is the nerve of the group $\mathrm{GL}_N$ seen as a category with one object, and a map $V : E \to B\mathrm{GL}_N$ is a vector bundle of rank $N$ on the space $E$. The projective bundle $\mathbb{P}(V)$ is the pullback along $V$ of a universal projective bundle $P_N \to B\mathrm{GL}_N$, and $L$ is the pullback of the universal line bundle on $P_N$. The groups $H^n(E, \mathbb{Z}/q(i))$, the pullback, the cup product and the first Chern class $c_1$ are the ones of the code.

**Definition 3.5.1 (Invertible on a space).** Let $q \geq 1$ and let $E$ be a space. We say that $q$ is *invertible on* $E$ if $q$ is a unit in $\Gamma(T, \mathcal{O}_T)$ for each scheme $T$ over which $E$ has a $0$-simplex. For $E = \mathrm{sch}(U)$ this says that $q$ is a unit on $U$.

**Definition 3.5.2 (Projective bundle formula in rank N).** Let $E$ be a space, $N \geq 0$, and let $\mathrm{triv}_N : E \to B\mathrm{GL}_N$ be the trivial bundle, with projective bundle $\pi : P \to E$ and line bundle $L$. The *projective bundle formula in rank* $N$ holds for $E$ if for all $n, i \in \mathbb{Z}$ the map
$$
\begin{aligned}
\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) &\to H^n(P, \mathbb{Z}/q(i)), \\
(a_j) &\mapsto \sum_{j} \pi^* a_j \cup c_1(L)^j
\end{aligned}
$$
is bijective.

This is the Leray and Hirsch condition for $\pi$ and the classes $c_1(L)^j$. In [algebraic topology](/learn/geometry/#complex-manifolds) the same statement for the complex projective bundle of a complex vector bundle is the Leray and Hirsch theorem.

**Lemma 3.5.3 (Trivial bundles).** Let $q \geq 1$ and $N \geq 0$. The projective bundle formula in rank $N$ holds for each space $E$ on which $q$ is invertible.

Lean: `UpperTheory.Pbf.pbf_all`.

*Proof.* We use induction on $N$, with the space $E$ arbitrary in the induction hypothesis. There are four cases.

For $N = 0$, the source is an empty sum, so it is zero. A lemma of the code shows that the target has at most one element in this case, so the map is bijective. This case does not need $q$ to be invertible.

For $N = 1$, the class $c_1(L)^0$ is $1$, so the map is $\pi^*$. A lemma of the code shows that $\pi : P \to E$ gives a quasi-isomorphism of the cochain complexes, so $\pi^*$ is bijective.

For $N = 2$, the [rank two lemma](/entry/projective-bundle-formula-rank-two/) covers $P$ by two charts, uses the Mayer and Vietoris sequence, and computes the cohomology of $\mathbb{G}_m \times E$ by a Künneth formula with the Kummer class.

For $N + 1$ with $N \geq 2$, the [step lemma](/entry/projective-bundle-formula-succ-of-forall/) takes the formula in rank $N$ for all spaces on which $q$ is invertible and gives it in rank $N + 1$. Its proof uses a second form of the formula in terms of $P\mathrm{GL}$, and Mayer and Vietoris covers. We read it as a statement.

The induction hypothesis is used only in the last case. $\square$

**Theorem 3.5.4 (Projective bundle formula).** Let $q \geq 1$, let $U$ be a scheme on which $q$ is a unit, let $N \geq 0$, and let $V : \mathrm{sch}(U) \to B\mathrm{GL}_N$ be a vector bundle of rank $N$, with projective bundle $\pi : \mathbb{P}(V) \to \mathrm{sch}(U)$ and line bundle $L$. Then for all $n, i \in \mathbb{Z}$ the map
$$
\begin{aligned}
\bigoplus_{j=0}^{N-1} H^{n-2j}(U, \mathbb{Z}/q(i-j)) &\to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \\
(a_j) &\mapsto \sum_{j} \pi^* a_j \cup c_1(L)^j
\end{aligned}
$$
is bijective.

Lean: `UpperTheory.Cb.etaleCohomology_projectiveBundle_formula`.

*Proof.* First, $V$ is the trivial bundle. A $k$-simplex of the discrete space $\mathrm{sch}(U)$ is the image of a $0$-simplex under the map $[k] \to [0]$. The value of $V$ on a $0$-simplex is a functor from the category with one object and one map to $B\mathrm{GL}_N$, and its composite with $[k] \to [0]$ is constant at the base object. So naturality of $V$ along $[k] \to [0]$ shows that $V$ is the constant map $\mathrm{triv}_N$. Second, this is the lemma on trivial bundles applied to $E = \mathrm{sch}(U)$. $\square$

**Remark 3.5.5.** The classical theorem is the following. Let $X$ be a scheme, $V$ a locally free sheaf of rank $N$ on $X$, and $n$ an integer invertible on $X$. Then $H^*(\mathbb{P}(V), \mathbb{Z}/n)$ is a free module over $H^*(X, \mathbb{Z}/n)$ with basis $1, \xi, \dots, \xi^{N-1}$, where $\xi$ is the Chern class of $\mathcal{O}(1)$ (SGA 5, Exposé VII; J. S. Milne, *Étale Cohomology*, Chapter VI, §10). The Lean theorem has this form, but a map from a discrete space to $B\mathrm{GL}_N$ is always the trivial bundle. A bundle that is only locally trivial is not a map $\mathrm{sch}(U) \to B\mathrm{GL}_N$ in this model. So the theorem is the formula for $U \times \mathbb{P}^{N-1}$ only, and the general bundle in the statement is a misleading generality.

**Remark 3.5.6.** The name of the rank one lemma says "of homotopy invariant", but its statement has no hypothesis of homotopy invariance: it asks only that $q$ be invertible on $E$. The theorem is used, under the name [of its parent statement](/entry/t-etale-cohomology-projective-bundle-formula/), in the step of [the formula on discrete spaces](/entry/pbf-disc/) that handles a scheme. We have not unfolded the model of spaces, the simplices in the definition of invertibility, or the definition of $c_1$.
