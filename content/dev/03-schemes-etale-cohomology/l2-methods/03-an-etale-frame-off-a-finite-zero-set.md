---
title: An étale frame off a finite zero set
decls:
  - GlobalTheory.exists_etale_frame_of_finite_zeroSet
  - GlobalTheory.T.exists_etale_frame_off_finite_zeroSet
status: drafted
drafted_by: writer@claude-opus-5-5
---
## An étale frame off a finite zero set

Let $s_1, \dots, s_n$ be sections of a line bundle $L$ on a compact complex manifold $Y$ of dimension $n \ge 1$, with a finite set $S$ of common zeros. This section builds one more section $\tau$ of a semipositive bundle $\Lambda$, a map $z : Y \to \mathbb{C}^n$ and a frame $\beta$ of $K_Y + E$, such that off the zeros of $\tau$ the map $z$ is étale and $\beta$ has no zero. The zero set of $\tau$ contains $S$ and is controlled by $|\tau|^2 \le C|s|^2$. The open set $\{\tau \neq 0\}$ is then an étale Stein space in the sense of Section 1, so Hörmander's estimate applies on it. This is how the twisted estimate of Section 4 and the $L^2$ extension theorem of Section 5 use the result.

We keep the notation of Section 2. For a section $\tau$ we write $N(\tau) = \{y \in Y : \tau(y) \neq 0\}$. We say that a bundle $\lambda$ is *semipositive* if $\mathcal{L}_i \varphi^\lambda_i(y)(\xi) \ge 0$ for all $i$, $y \in U_i$ and $\xi \in \mathbb{C}^n$.

**Definition 10.3.1 (Étale map on an open set).** Let $U \subseteq Y$ be open and $z : Y \to \mathbb{C}^n$ a map. We say $z$ is *étale on* $U$ if $z \circ \phi_i^{-1}$ is holomorphic on $\phi_i(U_i \cap U)$ for each chart $i$, and its Jacobian determinant $\det d(z \circ \phi_i^{-1})$ is nonzero at $\phi_i(y)$ for each $y \in U \cap U_i$.

By the inverse function theorem, a map that is étale on $U$ is a local homeomorphism of $U$ to $\mathbb{C}^n$.

**Theorem 10.3.2 (Étale frame off a finite zero set).** Let $Y$ be compact with a weighted atlas of dimension $n \ge 1$, and suppose that some $H \in \mathrm{La}$ is positive. Let $E, L \in \mathrm{La}$ and let $s = (s_1, \dots, s_n)$ be global sections of $L$ whose common zero set $S$ is finite. Then there are $\Lambda \in \mathrm{La}$, a global section $\tau$ of $\Lambda$, a map $z : Y \to \mathbb{C}^n$ and a family $\beta$ with:

1. $\Lambda$ is semipositive;
2. $z$ is étale on $N(\tau)$;
3. $\beta$ is a frame of $\kappa + E$ on $N(\tau)$;
4. $N(\tau)$ is dense in $Y$;
5. there is $C > 0$ with $|\tau|^2_\Lambda(y) \le C\, |s|^2(y)$ for all $y \in Y$.

Lean: `GlobalTheory.exists_etale_frame_of_finite_zeroSet` (also `GlobalTheory.T.exists_etale_frame_off_finite_zeroSet`, a second name).

Item 5 gives $\tau = 0$ on $S$, so $N(\tau) \cap S = \emptyset$. The open set $N(\tau)$ is not the complement of $S$ in general. It is the complement of a hypersurface that contains $S$.

*Proof.* We use five facts, each of which we read as a statement.

- (a) *Points on each component.* Since $n \ge 1$ and $S$ is finite, there is a finite set $T \subseteq Y$, disjoint from $S$, that meets each connected component of $Y$. Each component is an open manifold of positive dimension, so it is not contained in the finite set $S$.
- (b) *Positivity of large twists.* For each $B \in \mathrm{La}$ there is $k_2$ such that $B + kH$ is semipositive for $k \ge k_2$. This holds because $Y$ is compact and the Levi form of $\varphi^H$ is positive definite, so $k\varphi^H$ dominates the bounded Levi form of $\varphi^B$ on a finite cover by compact sets in charts.
- (c) *The Jacobian section.* For sections $t_0, t_1, \dots, t_n$ of a bundle $B$ there is a global section $J$ of $\kappa + 2nB$ with $J = t_0^{2n} \det d(t/t_0)$ in each chart at each point where $t_0 \neq 0$. Here $d(t/t_0)$ is the derivative of the quotient map of Section 2. In terms of forms, $J = t_0^{2n}\, d(t_1/t_0) \wedge \dots \wedge d(t_n/t_0)$, and the factor $t_0^{2n}$ clears the denominators.
- (d) *A combination that does not vanish on $T$.* For sections $s_1, \dots, s_N$ of $L$ and a finite set $T$ with no common zero of the $s_k$, there is a section $s'$ of $L$ with $s'(P) \neq 0$ for $P \in T$ and $C > 0$ with $|s'|^2_L \le C |s|^2$. A general linear combination of the $s_k$ works, and the Cauchy-Schwarz inequality gives the bound.
- (e) *Density.* A global section of a bundle that is nonzero at a point of each connected component has a dense set of nonzeros. This is the identity theorem in charts.

Now let $T$ be as in (a). Apply the theorem on coordinates and a nonvanishing section ([Theorem 10.2.4](/entry/sections-coords-and-nonvanishing-at-finset/)) to $H$, $T$ and the bundle $G = \kappa + E$. It gives $k_1$. Apply (b) to $B = (2n+4)\kappa + E + L$. It gives $k_2$. Put $k = \max(k_1, k_2)$. The theorem of Section 2 gives sections $t_0, t_1, \dots, t_n$ of $B_0 = \kappa + kH$ and a section $a$ of $\kappa + (\kappa + E) + kH$ with $t_0(P) \neq 0$, $(t_0; t)$ coordinates at $P$, and $a(P) \neq 0$ for each $P \in T$. Let $J$ be the section of (c) for $t_0, t$ and $B_0$, and let $s'$ be the section of (d) for $s$ and $T$. This applies because $T \cap S = \emptyset$.

Define
$$\tau = t_0 \cdot J \cdot a \cdot s', \qquad z(y) = \Bigl(\frac{t_j(y)}{t_0(y)}\Bigr)_{j=1}^n, \qquad \beta = \frac{a}{t_0},$$
with $z$ computed in the chart $i(y)$. The bundle of $\tau$ is
$$\Lambda = B_0 + (\kappa + 2nB_0) + (B_0 + \kappa + E) + L = (2n+4)\kappa + E + L + (2n+2)kH.$$
The products and quotients of sections are sections of the sums and differences of bundles, and the quotient is holomorphic where the denominator is nonzero.

Item 1. Since $(2n+2)k \ge k \ge k_2$, (b) shows that $\Lambda$ is semipositive.

Item 2. Let $y \in N(\tau)$. Then $t_0(y) \neq 0$, $J(y) \neq 0$ and $a(y) \neq 0$. By (c), $J(y) = t_0(y)^{2n} \det d(t/t_0)$ at $y$, so the determinant is nonzero, and $(t_0; t)$ are coordinates at $y$. On the open set $N(\tau)$ the function $t_0$ has no zero, so the quotients $t_j/t_0$ are holomorphic there. Their Jacobian in each chart differs from the one in the chart $i(y)$ by the Jacobian of a chart change, which is nonzero. So $z$ is étale on $N(\tau)$.

Item 3. On $N(\tau)$ both $a$ and $t_0$ have no zero, so $\beta = a/t_0$ is a section of $(2\kappa + E + kH) - (\kappa + kH) = \kappa + E$ on $N(\tau)$ with no zero.

Item 4. At $P \in T$ the four factors of $\tau$ are nonzero: $t_0(P) \neq 0$ and $a(P) \neq 0$ by Section 2, $s'(P) \neq 0$ by (d), and $J(P) = t_0(P)^{2n} \det d(t/t_0)(P) \neq 0$ since $(t_0; t)$ are coordinates at $P$. So $\tau$ is nonzero at a point of each component, and $N(\tau)$ is dense by (e).

Item 5. The function $|t_0 J a|^2$ (the pointwise norm of the product of the first three factors) is continuous on the compact space $Y$, so it has an upper bound $M$. Then
$$|\tau|^2_\Lambda = |t_0 J a|^2 \cdot |s'|^2_L \le \max(M, 1) \cdot C\, |s|^2.$$
So item 5 holds with the constant $\max(M,1)\,C > 0$. $\square$

The construction is the standard one of the proofs of $L^2$ extension from a zero set: coordinates from sections of a high multiple of an ample bundle, a section that cuts out the bad set, and a frame of the canonical bundle off it. The point of the semipositivity of $\Lambda$ is that $-\log|\tau|^2_\Lambda$ is then plurisubharmonic on $N(\tau)$ and tends to $+\infty$ at the boundary. This is the exhaustion that makes $N(\tau)$ an étale Stein space.

**Remark 10.3.3 (Formalization).** The étale condition is the structure `Etale` and $N(\tau)$ is `nz A τ`, both in Definitions/Divisors/EtaleEmpty.lean. Semipositivity is `A.Pos Λ (fun _ => 0)`. The facts (a) to (e) are `exists_finite_disjoint_meeting_every_component`, `exists_pos_add_nsmul_of_levi_pos`, `exists_jacobian_section_canonical_weight`, `exists_linComb_sections_ne_zero_on_finset` and `dense_nonvanishingSet_of_ne_zero_on_components`, with the rules for products and quotients in `atlasSections_mul_div_nonvanishing_isOpen` and item 2 in `isEtaleCoordinates_section_quotients`. We read their statements, not their proofs. The reasons given for (a), (b), (d) and (e) are the standard ones. The positive bundle $H$ is only assumed to exist. It is not part of the conclusion, and $\Lambda$ depends on the choice of $H$ and of $k$.
