---
title: An effective boundary with simple normal crossings
decls:
  - GlobalTheory.Div.SncBoundary.vanishing_ample_snc_cartier
  - GlobalTheory.T.snc_boundary_ample_decomposition
status: drafted
drafted_by: writer@claude-opus-5-5
---
## An effective boundary with simple normal crossings

Section 4 proved Kawamata-Viehweg vanishing for a boundary given as a relative snc family of line bundles with sections. In applications the boundary is an effective Cartier divisor $\Gamma$ whose support lies in a reduced divisor $B$ with simple normal crossings, as on a log resolution. This section proves vanishing in that form ([Theorem 9.5.2](/entry/vanishing-ample-snc-cartier/)). It is the Corollary after the $\mathbb{Q}$-divisor form of [Kawamata-Viehweg vanishing](/learn/positivity-resolution/#kodaira-and-kawamata-viehweg-vanishing) in Volume 1. Section 6 applies it on a log resolution to prove Nadel vanishing.

Let $Y$ be an integral scheme with function field $K$. A [Cartier divisor](/learn/geometry/#line-bundles-and-divisors) ([[Cartier divisor|FHV05ZK99F]]) $\Gamma$ on $Y$ has a local equation $g_y \in K^\times$ at each point $y$, unique up to a unit of $\mathcal{O}_{Y,y}$. For a point $z$ of codimension one with $\mathcal{O}_{Y,z}$ a [discrete valuation ring](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings), the *multiplicity* $\operatorname{mult}_z \Gamma$ is the valuation of $g_z$. For any point $z$ we also write $\operatorname{mult}_z \Gamma$ for the order of $g_z$ at $z$. The divisor is *effective* if each $g_y$ lies in $\mathcal{O}_{Y,y}$, and its support is the closed set of points where $g_y$ is not a unit. On a normal scheme, a Cartier divisor is determined by its multiplicities at the points of codimension one.

**Definition 9.5.1 (Simple normal crossings).** Let $Y$ be a scheme and $B \subseteq Y$ a closed set with ideal $I_B$, the ideal of functions that vanish on $B$. Then $B$ is a *divisor with simple normal crossings* if for each $y \in Y$ the local ring $\mathcal{O}_{Y,y}$ is regular and there are an affine open $U \ni y$, functions $f_1, \dots, f_n$ on $U$ and a subset $J \subseteq \{1, \dots, n\}$ such that

1. the germs of $f_1, \dots, f_n$ at $y$ are a regular system of parameters of $\mathcal{O}_{Y,y}$, that is, they generate the maximal ideal and $n = \dim \mathcal{O}_{Y,y}$;
2. $I_B(U) = \big(\prod_{i \in J} f_i\big)$.

So near $y$, $B$ is the union of the coordinate hyperplanes $f_i = 0$ for $i \in J$, each with multiplicity one. For instance, on $Y = \mathbb{A}^2$ over $k$, the union of the two axes $xy = 0$ has simple normal crossings, and the cusp $y^2 = x^3$ and the union of three lines through the origin do not.

On a smooth projective variety over a field of characteristic $0$, such a $B$ splits into its components: there are points $w_1, \dots, w_s$ of codimension one, distinct, and Cartier divisors $D_1, \dots, D_s$ with sections $\sigma_j$ of $\mathcal{O}_Y(D_j)$, such that $\operatorname{mult}_{w_j} D_j = 1$, $\operatorname{mult}_v D_j = 0$ for $v \neq w_j$, each point of codimension one in $B$ is some $w_j$, and $(\mathcal{O}_Y(D_j), \sigma_j)$ is a relative snc family of dimension $n$ in the sense of Section 2. So the $D_j$ are the prime components of $B$, and they meet transversally.

**Theorem 9.5.2 (Kawamata-Viehweg vanishing for an effective snc boundary).** Let $k$ be a field of characteristic $0$ and $Y$ an integral scheme, smooth of relative dimension $n$ and projective over $k$, with canonical bundle $K$. Let $Q$ be a line bundle and $A$ an ample line bundle on $Y$. Let $B \subseteq Y$ be a closed set that is a divisor with simple normal crossings, $\Gamma$ an effective Cartier divisor with support in $B$, and $e$ an integer with $\operatorname{mult}_z \Gamma < e$ for all $z$, such that
$$e[Q] = e[K] + [\mathcal{O}_Y(\Gamma)] + [A] \quad \text{in } \operatorname{Pic} Y.$$
Then $H^i(Y, Q) = 0$ for all $i > 0$.

Lean: `GlobalTheory.Div.SncBoundary.vanishing_ample_snc_cartier` (also `GlobalTheory.T.snc_boundary_ample_decomposition`, a second name).

In rational terms, $Q \equiv K + \frac1e \Gamma + \frac1e A$, and the boundary $\frac1e \Gamma$ has simple normal crossings with coefficients in $[0, 1)$. With $\Gamma = 0$ and $e = 1$ this is Kodaira vanishing $H^i(Y, K \otimes A) = 0$.

*Proof.* Since $Y$ is smooth over a field, it is normal. Let $w_j$, $D_j$, $\sigma_j$ be the components of $B$ given by the lemma above, and put $b_j = \operatorname{mult}_{w_j} \Gamma$. Since $\Gamma$ is effective, all its multiplicities are $\geq 0$, so $b_j \geq 0$.

Step 1 ($\Gamma = \sum_j b_j D_j$). Compare multiplicities at a point $z$ of codimension one. If $z = w_j$, both sides have multiplicity $b_j$, since $D_l$ has multiplicity $0$ at $w_j$ for $l \neq j$. If $z$ is no $w_j$, the right side has multiplicity $0$. If $\operatorname{mult}_z \Gamma \neq 0$, then $z$ lies in the support of $\Gamma$, so in $B$, and then $z$ is some $w_j$, a contradiction. So the two divisors have the same multiplicities, and they are equal, since $Y$ is normal.

Step 2 (the integers). Since $\Gamma$ is effective, its multiplicities are $\geq 0$ at every point, and the bound at the generic point of $Y$ gives $0 < e$. Also $b_j = \operatorname{mult}_{w_j} \Gamma < e$.

Step 3. By Step 1, $[\mathcal{O}_Y(\Gamma)] = \sum_j b_j [\mathcal{O}_Y(D_j)]$, so
$$e[Q] = e[K] + \sum_j b_j [\mathcal{O}_Y(D_j)] + [A].$$
The family $(\mathcal{O}_Y(D_j), \sigma_j)$ is a relative snc family of dimension $n$, and $0 \leq b_j < e$. So [Theorem 9.4.2](/entry/vanishing-ample-snc-char-zero/) gives $H^i(Y, Q) = 0$ for $i > 0$. $\square$

**Remark 9.5.3 (Formalization).** In [SncBoundaryAmpleDecomposition.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SncBoundaryAmpleDecomposition.lean#L110) the hypothesis `IsLocallyNoetherian Y` is redundant: the proof gets local noetherianity again from smoothness over $k$, and discards it. The bound `∀ z, Γ.mult z < e` is over all points; the proof uses it at the generic point to get $e > 0$ and at the points $w_j$. The conclusion is stated for `twist (structureModule Y) Q`, while [Theorem 9.4.2](/entry/vanishing-ample-snc-char-zero/) states it for `LB.toMod Q`; the last line of the proof closes the goal by `exact`, so the two are the same module. The components come from `SncComp.relSnc_components` in [ExistsPrimeDivisorsSncBoundary.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/ExistsPrimeDivisorsSncBoundary.lean#L154); we read its statement only. The multiplicity `CartierDiv.mult` is the order of a chosen local equation at the point. The second name `GlobalTheory.T.snc_boundary_ample_decomposition` is proved by `first | exact @… | …`.
