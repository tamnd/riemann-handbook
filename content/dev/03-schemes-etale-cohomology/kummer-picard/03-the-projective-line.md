---
title: The projective line
decls:
  - UpperTheory.projectiveBundleFormula_rank_two
  - UpperTheory.P2.kun
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The projective line

This section proves the projective bundle formula for the projective line over a space $E$: the cohomology of $\mathbb{P}^1_E$ is the cohomology of $E$ plus a copy of it shifted by $2$ and multiplied by the first Chern class $\xi$ of the tautological line bundle. The proof covers $\mathbb{P}^1_E$ by two affine lines, uses the homotopy invariance of the affine line on each, the [Künneth formula for $\mathbb{G}_m$](/entry/bijective-cohomology-gm-product-kummer-cup/) on their intersection, and the fact that the Mayer-Vietoris boundary of the Kummer class is $\pm \xi$. It is the case $N = 2$ of [the induction on the rank](/entry/pbf-all/), and the base of the induction step of the next section. We keep the notation of the previous section: spaces, their cohomology with coefficients $\mathbb{Z}/q(i)$, and the Kummer class $\kappa$.

### The projective bundle formula

**Definition 6.3.1 (Leray-Hirsch property).** Let $\pi : X \to E$ be a map of spaces and let $c_0, \dots, c_{m-1}$ be classes with $c_j \in H^{d_j}(X, \mathbb{Z}/q(e_j))$. The pair $(\pi, c)$ has the *Leray-Hirsch property* if for all $n, i \in \mathbb{Z}$ the map
$$\bigoplus_{j=0}^{m-1} H^{n - d_j}(E, \mathbb{Z}/q(i - e_j)) \to H^n(X, \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup c_j,$$
is bijective.

Lean: `UpperTheory.Pbf.LH`.

In topology, the Leray-Hirsch theorem says that a fibre bundle whose fibre cohomology is free on classes that extend to the total space has this property ([complex manifolds](/learn/geometry/#complex-manifolds)).

Let $N \ge 1$. For a ring $A$, a vector $v \in A^N$ is *unimodular* if its entries generate the unit ideal. The space $\mathbb{P}^{N-1}$ is the nerve of the groupoid whose objects over $A$ are the unimodular vectors in $A^N$ and whose arrows $v \to w$ are the units $\lambda \in A^\times$ with $v = \lambda w$. The arrow $\lambda$ gives a line bundle $\mathcal{L}$ on $\mathbb{P}^{N-1}$: its transition function on a $1$-simplex is $\lambda$. The space $\mathbb{P}^{N-1}_E$ is the trivial $\mathbb{P}^{N-1}$-bundle over $E$, with projection $\pi : \mathbb{P}^{N-1}_E \to E$, and $\mathcal{L}$ pulls back to it. Let $\xi = c_1(\mathcal{L}) \in H^2(\mathbb{P}^{N-1}_E, \mathbb{Z}/q(1))$ be its first Chern class ([line bundles](/learn/geometry/#line-bundles-and-divisors)).

**Definition 6.3.2 (Projective bundle formula).** The *projective bundle formula in rank $N$ for $E$*, written $\mathrm{PBF}_N(E)$, is the Leray-Hirsch property of $\pi : \mathbb{P}^{N-1}_E \to E$ with the classes $1, \xi, \dots, \xi^{N-1}$, where $\xi^j$ lies in degree $2j$ and twist $j$. So for all $n$ and $i$
$$\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) \xrightarrow{\ \sim\ } H^n(\mathbb{P}^{N-1}_E, \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup \xi^j.$$

Lean: `UpperTheory.Pbf.PBF`.

For a vector bundle $V$ of rank $N$ on a scheme $X$ and $q$ invertible on $X$, the classical theorem says that $H^*(\mathbb{P}(V), \mathbb{Z}/q)$ is free over $H^*(X, \mathbb{Z}/q)$ with basis $1, \xi, \dots, \xi^{N-1}$ (SGA 5, Exposé VII; Milne, *Étale Cohomology*, Chapter VI, §10). Here we treat the case of the trivial bundle, for spaces.

### Two charts

The proof of the rank $2$ case rests on a general lemma about a space covered by two pieces. A pair of maps $f_1 : W_1 \to X$, $f_2 : W_2 \to X$ is a *cover* if both are monomorphisms and, in each simplicial degree, the free sheaves on $W_1$ and $W_2$ map onto the free sheaf on $X$. A cover gives a Mayer-Vietoris sequence
$$\cdots \to H^n(X) \to H^n(W_1) \oplus H^n(W_2) \to H^n(W_{12}) \xrightarrow{\ \delta\ } H^{n+1}(X) \to \cdots,$$
where $W_{12} = W_1 \times_X W_2$. The boundary $\delta$ is compatible with cup products by classes pulled back from $X$.

**Lemma 6.3.3 (Two charts).** Let $\pi : X \to E$ be a map of spaces and $f_1, f_2$ a cover of $X$ with intersection $W_{12}$. Let $\xi \in H^2(X, \mathbb{Z}/q(1))$ and $k \in H^1(W_{12}, \mathbb{Z}/q(1))$. Write $\pi_{12} : W_{12} \to E$ for the composite map. Assume:

1. $\pi \circ f_1$ and $\pi \circ f_2$ are cohomological equivalences for each $\mathbb{Z}/q(i)$;
2. for all $m, j$ the map $(a, b) \mapsto \pi_{12}^* a + \pi_{12}^* b \cup k$ from $H^{m+1}(E, \mathbb{Z}/q(j+1)) \oplus H^m(E, \mathbb{Z}/q(j))$ to $H^{m+1}(W_{12}, \mathbb{Z}/q(j+1))$ is bijective;
3. $\delta(k) = \xi$ or $\delta(k) = -\xi$.

Then for all $m, j \in \mathbb{Z}$ the map
$$H^{m+2}(E, \mathbb{Z}/q(j+1)) \oplus H^m(E, \mathbb{Z}/q(j)) \to H^{m+2}(X, \mathbb{Z}/q(j+1)), \qquad (a, b) \mapsto \pi^* a + \pi^* b \cup \xi,$$
is bijective. If also $q$ is invertible on $X$, then $(\pi; 1, \xi)$ has the Leray-Hirsch property.

Lean: `UpperTheory.P2.core` (also `UpperTheory.P2.lh2`, the last sentence).

*Proof.* By hypothesis 1, $H^n(W_1) \oplus H^n(W_2)$ is $H^n(E)^2$, and the restriction from $H^n(X)$ composed with these isomorphisms becomes the diagonal on the image of $\pi^*$. By hypothesis 2 and the compatibility of $\delta$ with cup products, the boundary sends $\pi_{12}^* b \cup k$ to $\pm \pi^* b \cup \xi$, and it kills the classes $\pi_{12}^* a$, which come from $W_1$. So the Mayer-Vietoris sequence splits into short exact sequences
$$0 \to H^{n-1}(E) \xrightarrow{\ b \mapsto \pm \pi^* b \cup \xi\ } H^n(X) \to H^n(E) \to 0,$$
and $\pi^*$ splits the second map. A diagram chase gives the bijectivity of $(a, b) \mapsto \pi^* a + \pi^* b \cup \xi$. The sign in hypothesis 3 does no harm: it changes $b$ into $-b$. For the last sentence, write $n = m + 2$ and $i = j + 1$. The Leray-Hirsch map for the classes $\xi^0 = 1$ and $\xi^1 = \xi$ is the map above, since $\pi^* a \cup 1 = \pi^* a$. We use the invertibility of $q$ on $X$ for this identity and for $\xi^1 = \xi$. $\square$

**Lemma 6.3.4.** Let $E$ be a space on which $q$ is invertible. For all $m, j \in \mathbb{Z}$ the map
$$\begin{aligned} H^{m+1}(E, \mathbb{Z}/q(j+1)) \oplus H^m(E, \mathbb{Z}/q(j)) &\to H^{m+1}(\mathbb{G}_m \times E, \mathbb{Z}/q(j+1)), \\ (a, b) &\mapsto \mathrm{pr}_2^* a + \mathrm{pr}_2^* b \cup \mathrm{pr}_1^* \kappa \end{aligned}$$
is bijective.

Lean: `UpperTheory.P2.kun`.

*Proof.* This is [Theorem 6.2.7](/entry/bijective-cohomology-gm-product-kummer-cup/) (Künneth formula for $\mathbb{G}_m$) with $n = m + 1$ and $i = j + 1$. $\square$

### The rank two case

**Theorem 6.3.5 (Projective line).** Let $E$ be a space on which $q$ is invertible. Then $\mathrm{PBF}_2(E)$ holds: for all $n, i$ the map
$$H^n(E, \mathbb{Z}/q(i)) \oplus H^{n-2}(E, \mathbb{Z}/q(i-1)) \to H^n(\mathbb{P}^1_E, \mathbb{Z}/q(i)), \qquad (a, b) \mapsto \pi^* a + \pi^* b \cup \xi,$$
is bijective.

Lean: `UpperTheory.projectiveBundleFormula_rank_two`.

*Proof.* We check the hypotheses of the Lemma on two charts.

1. *Charts.* The space $\mathbb{P}^1_E$ is isomorphic to $E \times \mathbb{P}^1$. Let $\mathbb{P}^0$ be the space of the same construction with $N = 1$: its objects over $A$ are the units of $A$, and any two of them are joined by exactly one arrow. For $b = 0, 1$ there is a chart $f_b : \mathbb{A}^1 \times E \times \mathbb{P}^0 \to \mathbb{P}^1_E$. On a simplex with coordinate $x$ and unit $c$ it gives the vector $c\,(1, x)$ for $b = 0$ and $c\,(x, 1)$ for $b = 1$. Each chart composed with $\pi$ is the projection to $E$. The two charts form a cover. The invertibility of $q$ passes from $E$ to $\mathbb{P}^1_E$ and to the charts, since a map of spaces sends $0$-simplices over $T$ to $0$-simplices over $T$.

2. *Homotopy invariance.* We use two facts. First, the projection $Y \times \mathbb{P}^0 \to Y$ is a cohomological equivalence when $q$ is invertible on $Y$. This is $\mathrm{PBF}_1(Y)$, the rank one case of the projective bundle formula. Second, the projection $\mathbb{A}^1 \times E \to E$ is a cohomological equivalence for each $\mathbb{Z}/q(i)$ when $q$ is invertible on $E$. This is the homotopy invariance of étale cohomology with coefficients prime to the residue characteristics (Milne, *Étale Cohomology*, Chapter VI, §4). The composite of the two is $\pi \circ f_b$, so hypothesis 1 holds.

3. *The intersection.* The intersection $W_{12}$ of the two charts is isomorphic to $\mathbb{G}_m \times E \times \mathbb{P}^0$: it is the locus where the coordinate $x$ is a unit. So it has a map $u : W_{12} \to \mathbb{G}_m$, the coordinate, and a map $\rho : W_{12} \to \mathbb{G}_m \times E$, which forgets the factor $\mathbb{P}^0$. By step 2, $\rho$ is a cohomological equivalence. Put $k = u^* \kappa$. The bijection of hypothesis 2 is the bijection of the Lemma above composed with $\rho^*$, since pullback is compatible with cup products. So hypothesis 2 holds.

4. *The boundary.* On chart $b$ the line bundle $\mathcal{L}$ has a trivializing unit $w_b$. On $W_{12}$ the coordinate is the ratio: $u^* t = w_1 w_2^{-1}$. We use the following fact on the Mayer-Vietoris boundary of Kummer classes: if a line bundle is trivialized on the two pieces of a cover by units $w_1$ and $w_2$, then the boundary of the Kummer class of $w_1 w_2^{-1}$ is $c_1$ of the line bundle, up to sign. It gives $\delta(u^* \kappa) = \pm c_1(\mathcal{L}) = \pm \xi$. This is hypothesis 3.

The Lemma on two charts now gives the Leray-Hirsch property for $1, \xi$, since $q$ is invertible on $\mathbb{P}^1_E$. This is $\mathrm{PBF}_2(E)$. $\square$

For $E$ a point over $\mathbb{C}$ this is the computation $H^*(\mathbb{P}^1) = \mathbb{Z} \oplus \mathbb{Z} \xi$, obtained from the cover of the sphere by two discs that meet in an annulus.

**Remark 6.3.6 (Formalization).** The boundary of the Kummer class is known only up to sign, so the Lemma on two charts accepts either sign. The first part of that Lemma has no hypothesis on $q$; the invertibility of $q$ on $X$ is used only in the identities $\pi^* a \cup \xi^0 = \pi^* a$ and $\xi^1 = \xi$, since the unit class and the powers of a class are fixed by a choice of cocycles. The Lemma that restates the Künneth formula only changes its indices. The rank one formula, the homotopy invariance of $\mathbb{A}^1$ and the boundary of Kummer classes are separate results of the formal proof that we cite and do not prove here. The charts are built in [TwoChart.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/TwoChart.lean#L136), and the Lemma on two charts is at [TwoCore.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/TwoCore.lean#L193).
