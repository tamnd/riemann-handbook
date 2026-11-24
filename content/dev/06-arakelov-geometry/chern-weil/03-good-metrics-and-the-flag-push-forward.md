---
title: Good metrics and the flag push forward
decls:
  - GlobalTheory.GoodTop.goodTopChernForm
  - GlobalTheory.T.goodMetric_topChernForm_integral_eq_smooth
  - GlobalTheory.FlagPush.interPoly_swap_adjacent
  - GlobalTheory.T.flagSpace_intersectionNumber_adjacent_swap_neg
  - GlobalTheory.FlagPushProof.flagPushForward
  - GlobalTheory.T.fullFlagBundle_pushForward_formula
  - GlobalTheory.GoodMetric.goodChernWeil
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good metrics and the flag push forward

This section proves the theorem of Mumford on good metrics in the form that the development uses. A metric on a family of vector bundles that is smooth on an open set $O$ and good along the complement of $O$ has Chern integrals over $O$, and they are the Chern numbers of the bundles. We first prove this for the top Chern form of one bundle, by a transgression argument with a partition of unity. A reduction to representations then gives every Chern polynomial. The value is the intersection number on the flag bundle of [the previous section](/entry/chern-weil-numbers-holds/), and a second theorem computes it by an antisymmetrization over the Weyl group. Both theorems together form the hypothesis `GoodChernWeil`, a field of the step [published results in arithmetic geometry](/step/published-results-arithmetic/). For the classical statement see the [good metrics of Volume 1](/learn/positivity-resolution/#chern-weil-forms).

### Good metrics

We keep the notation of the previous section: $X$ is a projective variety over $F$, $\sigma : F \to \mathbb{C}$, $E$ is a family of frames of type $0$ on $X$ with ranks $m$, and $O$ is an open set of $X$. For a point $v$ of a polydisc and a set $S$ of coordinates, put
$$w_a(v) = |v_a| \, \big|\log |v_a|\big| \ (a \in S), \qquad w_a(v) = 1 \ (a \notin S),$$
and $\ell(v) = \sum_{a \in S} |\log |v_a||$.

**Definition 5.3.1 (Good metric).** A metric $H$ on $E$ over $O$ is good if each complex point $y$ of $X$ outside $O$ has a holomorphic chart $e$ with $e(y)$ in the coordinate hyperplanes $\{v_a = 0\}$, $a \in S$, such that in the chart the complement of $O$ is the union of these hyperplanes, and such that for one frame $A$ at $y$ there are $c$ and $N$ with these bounds near $y$ on $O$, for each $\tau$, where $G = H(A, \cdot)_\tau$:

1. the entries of $G$ and $|\det G|^{-1}$ are at most $c\,\ell^N$;
2. the entries of the connection matrix in the direction $a$ are at most $c / w_a$;
3. the entries of the curvature matrix and of the antisymmetric $\partial$-derivative of the connection in the directions $a, b$ are at most $c / (w_a w_b)$.

Lean: `GlobalTheory.GoodMetric.IsGood` (also `GlobalTheory.GoodMetric.GoodBound`, the bounds).

The weights $1/w_a$ are the lengths of the coordinate vectors for the Poincaré metric on the punctured disc. So the definition is Mumford's: the Gram matrix has logarithmic growth, and the connection and curvature forms have Poincaré growth.

### The top Chern form

**Theorem 5.3.2 (Top Chern form of a good metric).** Let $E$ be a single vector bundle of rank $m$ on $X$, given by frames of type $0$. Let $H$ be a good metric on $E$ over $O$, and let $H_0$ be a metric on $E$ over all of $X$. If
$$\int_X c_{\dim X}(E, H_0) = t,$$
then also $\int_O c_{\dim X}(E, H) = t$.

Lean: `GlobalTheory.GoodTop.goodTopChernForm` (also `GlobalTheory.T.goodMetric_topChernForm_integral_eq_smooth`, a second name).

*Proof.* Put $n = \dim X$. We write both Chern integrals as integrals of top degree densities over the charts. Each complex point $y$ has a patch $W_y$ of one of two kinds. If $y$ lies in $O$, the patch is a chart in $O$ with a frame. If $y$ lies outside $O$, the patch is a chart of the kind in the definition of a good metric, with its Poincaré bounds. The complex points form a compact second countable space, so there is a smooth partition of unity $(\rho_i)$, finite and subordinate to the patches.

For each $i$, a transgression argument on the patch gives real numbers $a_i$ and $b_i$ with
$$a_i = \int_O \rho_i \, c_n(E, H), \qquad b_i = \int_X \rho_i \, c_n(E, H_0),$$
and it writes $a_i - b_i$ as the integral over $O$ of a correction density of top degree. On a patch outside $O$ the bounds of the good metric make these integrals finite. Since $\sum_i \rho_i = 1$, the sum of the $a_i$ is $\int_O c_n(E, H)$, and the sum of the $b_i$ is $\int_X c_n(E, H_0) = t$. The correction densities for the different $i$ sum to $0$ at each point of $O$, again because $\sum_i \rho_i = 1$. So $\sum_i (a_i - b_i) = 0$, and $\int_O c_n(E, H) = \sum_i a_i = t$. $\square$

The transgression on one patch, the existence of the two kinds of patch and the vanishing of the summed corrections are separate results of the development that the proof cites. The finiteness of the integrals of $\rho_i c_n(E, H)$ near the boundary is the place where the bounds of a good metric enter.

### The push forward from the flag bundle

Let $(Y, E')$ refine $(X, E)$ along $f$ and $\phi$, and let $\operatorname{gr}$ grade $E'$. The Weyl group $W = \prod_\tau S_{m_\tau}$ acts on the roots by $w(\tau, i) = (\tau, w_\tau(i))$, and so on $\mathbb{R}[x_{\tau, i}]$.

**Definition 5.3.3 (Antisymmetrization).** For $Q \in \mathbb{R}[x_{\tau, i}]$ put
$$\mathcal{A}(Q) = \sum_{w \in W} \operatorname{sign}(w) \, w(Q), \qquad \delta = \prod_\tau \prod_{i < j} (x_{\tau, j} - x_{\tau, i}).$$

Lean: `GlobalTheory.GoodMetric.antisymm` (also `GlobalTheory.GoodMetric.rootDiscr`, the product $\delta$).

**Lemma 5.3.4 (Adjacent swap).** Let $\tau \in \iota$ and let $a, b < m_\tau$ with $b = a + 1$. Let $s$ be the transposition of the roots $(\tau, a)$ and $(\tau, b)$. Then for every $Q \in \mathbb{R}[x_{\tau, i}]$,
$$\langle s(Q) \rangle_{\operatorname{gr}} = -\langle Q \rangle_{\operatorname{gr}}.$$

Lean: `GlobalTheory.FlagPush.interPoly_swap_adjacent` (also `GlobalTheory.T.flagSpace_intersectionNumber_adjacent_swap_neg`, a second name).

*Proof.* Let $B$ be the generic frame of the grading. There is a second embedding $\psi_2 : K(Y) \to K(Y)(t)$ that agrees with the standard embedding on $\phi(K(X))$ and moves the flag of $B$ only in the step $a$: the two frames differ by a shear in the positions $a$ and $b$. From this pair of embeddings we get a variety $W$ with two maps $\alpha_1, \alpha_2 : K(Y) \to K(W)$ and an embedding $j : K(W) \to K(Y)(t)$ with $j \circ \alpha_1$ the standard embedding and $j \circ \alpha_2 = \psi_2$. Geometrically, $W$ is the space of pairs of full flags that differ only in the step $a$. The maps $\alpha_1$ and $\alpha_2$ agree on $\phi(K(X))$, and the frames $\alpha_1(B)$ and $\alpha_2(B)$ differ by an almost lower triangular matrix. This gives divisors $D_1$, $D_2$ and $\Theta$ on $W$ that compare the gradings pulled back by the two maps. A theorem of the development on such double spaces then gives the sign. We do not open the proofs of these steps. $\square$

The classical picture is this. Forgetting the step $a$ of the flag makes $Y$ a $\mathbb{P}^1$-bundle over a partial flag bundle. The transposition $s$ exchanges the two roots of this $\mathbb{P}^1$-bundle, and the push forward of a polynomial in the roots to the partial flag bundle changes sign under $s$.

**Theorem 5.3.5 (Push forward from the flag bundle).** Assume that $F$ has characteristic $0$. Let $Q \in \mathbb{R}[x_{\tau, i}]$ and $R \in \mathbb{R}[X_{\tau, k}]$, and assume that $\mathcal{A}(Q) = \operatorname{cr}(R) \cdot \delta$. Then
$$\langle Q \rangle_{\operatorname{gr}} = \big\langle \operatorname{cr}(R) \cdot \varpi \big\rangle_{\operatorname{gr}}.$$

Lean: `GlobalTheory.FlagPushProof.flagPushForward` (also `GlobalTheory.T.fullFlagBundle_pushForward_formula`, a second name).

*Proof.* Let $\lambda(Q) = \langle Q \rangle_{\operatorname{gr}}$. By the lemma, $\lambda(s(Q)) = -\lambda(Q)$ for each adjacent transposition $s$. These transpositions generate $W$, so $\lambda(w(Q)) = \operatorname{sign}(w) \lambda(Q)$ for all $w \in W$. So $\lambda(\mathcal{A}(Q)) = |W| \, \lambda(Q)$, and two polynomials with the same antisymmetrization have the same value under $\lambda$. The polynomial $\operatorname{cr}(R)$ is symmetric, so $\mathcal{A}(\operatorname{cr}(R) \cdot \varpi) = \operatorname{cr}(R) \cdot \mathcal{A}(\varpi)$. The antisymmetrization of the monomial $\varpi$ is the product of the Vandermonde determinants, $\mathcal{A}(\varpi) = \delta$. So $\mathcal{A}(Q) = \mathcal{A}(\operatorname{cr}(R) \cdot \varpi)$, and the claim follows. $\square$

So the intersection number of a polynomial in the roots depends only on its antisymmetrization. If $Q$ is the product of $\operatorname{cr}(R)$ and a polynomial with antisymmetrization $\delta$, the theorem gives the usual formula for the Gysin map of a flag bundle.

### Chern numbers for good metrics

**Theorem 5.3.6 (Chern numbers for good metrics).** Let $X$, $Y$, $E$, $E'$, $\phi$, $f$ and $\operatorname{gr}$ be as in the previous section, with $(Y, E')$ refining $(X, E)$ and $\operatorname{gr}$ grading $E'$. Then these hold.

1. Let $H$ be a metric on $E$ over an open set $O$ that is good. Then for every $R \in \mathbb{R}[X_{\tau, k}]$,
$$\int_O R(c(E, H)) = \big\langle \operatorname{cr}(R) \cdot \varpi \big\rangle_{\operatorname{gr}}.$$
2. If $F$ has characteristic $0$, then the push forward formula above holds.

Lean: `GlobalTheory.GoodMetric.goodChernWeil`.

*Proof.* Part 2 is the theorem on the push forward from the flag bundle. For part 1, fix $R$. There is a finite family of polynomial representations $\rho_j$ of $\prod_\tau \mathrm{GL}_{m_\tau}$, with ranks $M_j$, and real numbers $a_j$, with this property: for every curvature matrix whose entries are homogeneous linear forms, the top coefficient of $R(c)$ is $\sum_j a_j$ times the top coefficient of $c_{n}$ of the image of the curvature under the Lie algebra map of $\rho_j$. Here $n = \dim X$.

Choose a metric $H_0$ on $E$ over all of $X$; it exists since $X$ is projective. Each $\rho_j$ gives a vector bundle $E_j$ of rank $M_j$ with frames $\rho_j(A)$, and metrics $\rho_j(H)$ over $O$ and $\rho_j(H_0)$ over $X$. The metric $\rho_j(H)$ is again good. By [the theorem on smooth metrics](/entry/chern-weil-numbers-holds/), applied to $E_j$ and $\rho_j(H_0)$, there is $t_j$ with $\int_X c_n(E_j, \rho_j(H_0)) = t_j$. By the theorem on the top Chern form, $\int_O c_n(E_j, \rho_j(H)) = t_j$.

The curvature of $\rho_j(H)$ is the image of the curvature of $H$ under the Lie algebra map of $\rho_j$. So at each point of $O$ the density of $R(c(E, H))$ is $\sum_j a_j$ times the density of $c_n(E_j, \rho_j(H))$. By linearity of the Chern integral, $\int_O R(c(E, H)) = \sum_j a_j t_j$. The same argument over $X$ gives $\int_X R(c(E, H_0)) = \sum_j a_j t_j$. By the theorem on smooth metrics the last integral is $\langle \operatorname{cr}(R) \cdot \varpi \rangle_{\operatorname{gr}}$. $\square$

The statement of this theorem is the hypothesis `GoodChernWeil`. Combined, the two parts give $\int_O R(c(E, H)) = \langle Q \rangle_{\operatorname{gr}}$ for each $Q$ with $\mathcal{A}(Q) = \operatorname{cr}(R) \cdot \delta$. The development uses it in this form for flag bundles over toroidal compactifications, in [the proportionality theorem for toroidal flag bundles](/entry/toroidal-flag-proportionality-of-good-chern-weil/). Its parent in the literature chapter is [the theorem of Mumford from the literature](/entry/good-chern-weil-of-literature/), which it replaces.

**Remark 5.3.7 (Formalization).** The theorem on the top Chern form covers only one bundle and only $c_{\dim X}$; the passage to every $R$ is the reduction to representations in the last proof. That reduction is a separate lemma of the development, in the folder of the Iwasawa decomposition, which the proof of `goodChernWeil` cites with the three theorems. The decomposition of $R$ into top Chern forms of representations, the induced bundles and metrics, the goodness of $\rho_j(H)$ and the transformation of the curvature are results of the development that the proofs cite. The hypothesis of characteristic $0$ in the push forward formula is introduced in its proof but not passed to the swap lemma or to the lemma on antisymmetrization. The intersection form takes real coefficients, so $|W|$ is invertible in any case.
