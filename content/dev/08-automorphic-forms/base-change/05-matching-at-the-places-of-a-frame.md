---
title: Matching at the places of a frame
decls:
  - PositivityTheory.Rg.BcB.F.MatchAll.matchLMB2
  - PositivityTheory.Rg.BcB.F.MatchAll.matchLMB2₀
  - PositivityTheory.Rg.BcB.F.B3.locMatch
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Matching at the places of a frame

The global argument compares a unitary trace formula with a twisted trace formula for $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$, for test functions that are high convolution powers of a fixed function at a finite set of places. This section shows that all the local functions match. At the inert places of a set $T$ we use the Iwahori matching of [the previous section](/entry/m4/), at a set $S_0$ of split places a constant term, and at a set of bad places the matching of congruence subgroups. The local functions on the general linear side are written as matrices of functions, so that powers can be taken entrywise in a basis adapted to the Iwahori matching. The result is used by [the frame bound](/entry/frame-word-identity-frame-bound/), which leads to the step [BaseChangeN](/step/base-change-n/).

We keep the notation of [the fundamental lemma at an inert place](/entry/archimedean-base-change-fourth/): $E$ is a CM field in which every finite place is unramified over $F$, matching of $f$ on $U_w$ and $\varphi$ on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_{n-a}(E_w)$ with a character $\mu$ of $E_w^\times$ is the identity of stable twisted orbital integrals with $\Delta_\mu$ times $\kappa$-orbital integrals, and at an inert place $\mu$ plays no role. At a split place $U_w = \mathrm{GL}_n(E_w)$. Convolution of functions on a group with a compact open subgroup $K$ is normalized so that $\mathbf{1}_K/\mathrm{vol}$ is the unit, and $f^{*m}$ is the $m$-th convolution power. For a function $\phi$ on a group, write $\phi^{*m}$ for the same.

**Definition 7.5.1 (Local datum).** A local datum for $E$ and $n$ consists of:

1. three disjoint finite sets $T$, $S_0$ and $\mathrm{Bad}$ of finite places, with union $B$;
2. for each finite place $w$, a character $\mu_w$ of $E_w^\times$ and a uniformizer $\varpi_w$;
3. for $w \in T$: a Witt basis $b_w$ as in the Iwahori matching, and a finitely supported function $c_w$ on $\mathbb{Z}^n$ whose support consists of strictly decreasing $x$ with $l(x)$ a cone point;
4. for $w \in S_0$: an open subgroup $K'_w \subset K_n$ normalized by $K_n$, a set $X_w \subset K_n$ of representatives of $K_n/K'_w$, and a function $e_w$ bi-invariant under $K'_w$;
5. for $w \in S_0 \cup \mathrm{Bad}$ and $a \le n$: a $\theta$-stable level $L_{a,w} = L_1 \times L_2$ in $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$;
6. for $w \in \mathrm{Bad}$: an open subgroup $K^B_w$ of $K_{U,w}$ and, for each $a$, a function $\mathrm{fix}_{a,w}$ bi-invariant under $L_{a,w}$.

It is compatible with the places if every $w \in T$ is inert, every $w \in S_0$ is split, the level $K'_w$ is a level for $U_w$ at $w \in S_0$, the elements of $L_{a,w}$ at $w \in S_0$ lie in the Levi part of $K'_w$ and are killed by $\mu_w(\det{}^{n-a} \times \det{}^a)$, and at a split $w \in \mathrm{Bad}$ the function $\mathrm{fix}_{a,w}$ is the twisted constant term along $\mu_w$ of the normalized unit of $K^B_w$.

The datum defines a function at each $w \in B$ on the unitary side:
$$g_{0,w} = \begin{cases}\sum_x c_w(x)\,[K_U : I_U]\,f_U(l(x)) & w \in T,\\ e_w & w \in S_0,\\ \text{the normalized unit of } K^B_w & w \in \mathrm{Bad},\end{cases}$$
and $g_U(m)_w = g_{0,w}^{*m}$. On the general linear side, at $w \in T$, it defines for each admissible $s$ (as in the definition of $\varphi_x$) the function
$$\beta_{s,w} = \sum_x c_w(x)\,(-q)^{-v(s)}\,[K_a \times K_{n-a} : I_a \times I_{n-a}]\;\mathbf{1}_{I_a t(x|_S) I_a} \otimes \mathbf{1}_{I_{n-a} t(x|_{S'}) I_{n-a}},$$
which is the part of $\sum_x c_w(x)\varphi_x$ indexed by $s$. The functions $\beta_{s,w}$ form a diagonal matrix $\beta_w$ indexed by $s$. At $w \in S_0$ the matrix $\beta_w$ is indexed by $X_w$, with entries built from $e_w$ and $\mu_w$ by a twisted constant term. A matrix $\mathrm{fix}_a$ of idempotents (the normalized units of $I_a \times I_{n-a}$ at $T$ and of $L_{a,w}$ at $S_0$, and $\mathrm{fix}_{a,w}$ at $\mathrm{Bad}$) is the starting term. Products of matrices use convolution of the entries, and $\mathrm{tr}$ is the sum of the diagonal entries.

The point of the matrix form is that the Iwahori double cosets of strictly dominant elements multiply without mixing: the convolution of the characteristic functions of $It(x)I$ and $It(x')I$ is a multiple of the characteristic function of $It(x + x')I$ when both are dominant. So the $(m+1)$-st power of $\beta_w$ is again diagonal, with entries the analogous functions for the sums of the cone points.

**Theorem 7.5.2 (Congruence matching and split matching).** We use two further local matchings, proved in the companion development.

1. Let $w$ be inert, $a + b = n$, and $k \ge 1$. Let $K(k) \subset K_n$ be the principal congruence subgroup of level $\varpi^k$. Then $\mathbf{1}_{U \cap K(k)}$ matches the function equal to $(-q)^{-kab}$ at the $(y_1, y_2)$ with $y_i \in K$ and $N(y_i) \in K(k)$, and $0$ elsewhere.
2. Let $w$ be split, $a \le n$, $\mu$ a character of $E_w^\times$, $K'$ a level for $U_w$, and $f$ bi-invariant under $K'$. Then $f$ matches its twisted constant term along $\mu$ with the character $\mu$.

Part 1 is the analogue for congruence subgroups of the fundamental lemma for the unit. Part 2 is the matching at a split place, where the stable twisted orbital integrals of a function on $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ are orbital integrals of its pullback, and the matching function is the constant term along the parabolic of type $(a, n-a)$.

**Proposition 7.5.3 (Matching for a local datum, conditional form).** Assume part 1 and part 2 of the previous theorem and the [Iwahori matching](/entry/m4/). Let $d$ be a local datum that is compatible with the places. Then for every $a \le n$, every $m \ge 0$ and every $w \in B$, the functions $g_U(m+1)_w$ and $\mathrm{tr}(\mathrm{fix}_a\,\beta^{m+1})_w$ match with the character $\mu_w$ if $w \in S_0$ or $w$ is a split place of $\mathrm{Bad}$, and with the trivial character otherwise.

Lean: `PositivityTheory.Rg.BcB.F.MatchAll.matchLMB2`.

*Proof.* We treat the three kinds of places. At $w \in T$, the convolution powers of the Iwahori double coset functions on both sides are computed by the multiplicativity of dominant double cosets, which is taken as an input from the companion development. So $g_U(m+1)_w$ is a linear combination of functions $f_U(l)$ with $l$ a cone point, and $\mathrm{tr}(\mathrm{fix}_a\beta^{m+1})_w$ is the same combination of the functions $\varphi_x$, entry by entry in $s$. Each pair matches by the Iwahori matching, and matching is linear. At $w \in S_0$, the entries of $\beta^{m+1}$ are twisted constant terms of the powers of $e_w$, by the compatibility of $L_{a,w}$ with the Levi part of $K'_w$, and part 2 gives the matching. At a split $w \in \mathrm{Bad}$, the function $\mathrm{fix}_{a,w}$ is the constant term of the unit of $K^B_w$, which matches by part 2, and the powers of the unit are the unit. At an inert $w \in \mathrm{Bad}$ we use part 1. Two algebraic facts close the argument: $\mathrm{fix}_a$ is idempotent for the matrix product, and the idempotents act as units on the algebra generated by $\beta$. $\square$

**Theorem 7.5.4 (Matching for a local datum).** Let $d$ be a local datum that is compatible with the places. Then for every $a \le n$, $m \ge 0$ and $w \in B$, the functions $g_U(m+1)_w$ and $\mathrm{tr}(\mathrm{fix}_a\,\beta^{m+1})_w$ match, with the characters of the Proposition.

Lean: `PositivityTheory.Rg.BcB.F.MatchAll.matchLMB2₀`.

*Proof.* This is the Proposition applied to the two matchings of the previous theorem and to the [Iwahori matching](/entry/m4/). $\square$

The frame bound uses products of many local operators, not only powers of $\beta$. These are words in letters, each letter a matrix of the kind above or a Hecke operator at a good split place, and the frame bound needs that the global test function built from a word matches at every place. Let $S$ be a finite set of places that contains $B$ and every archimedean place. A place $w \notin B$ is good if it is split and $\mu_w$ is unramified. A word $\ell$ in the letters has, at each good place $w$, a local word $\ell_w$ in the spherical Hecke algebra of $\mathrm{GL}_n(E_w)$ and its image in $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$; at the places of $B$ it gives a product $\Pi(\ell)$ of matrices.

**Theorem 7.5.5 (Local matching for words).** Let $d$ be a local datum compatible with the places, with $T$ nonempty and every $\mu_w$ unitary. Let $S$ be as above, with the level of $d$ off $S$ hyperspecial, and assume that every split place of $S$ outside $B$ is good. Let $m, k \ge 1$, let $\ell$ be a word with exactly $mk$ letters of the first kind, and let $\ell_U$ be a word in the unitary Hecke generators whose spherical part at each $w \notin B$ is the unitary word attached to $\ell_w$. Then:

1. $g_U(m)_w$ is bi-invariant under $K_{U,w}$ for every $w \in B$;
2. at some $w \in S$, the unitary test function $\Phi_w$ built from $g_U(m)$, $k$ and $\ell_U$ is supported on elements with separable characteristic polynomial;
3. for every $a \le n$, the general linear test function built from $\mathrm{tr}\,\Pi(\ell)$ and its second component is a test function, and at every $w \in S$ it matches $\Phi_w$ with the character $\mu_w$;
4. at some inert $w \in S$, the function $\mathrm{tr}\,\Pi(\ell)_w$ is supported on pairs whose norms have separable product of characteristic polynomials.

Lean: `PositivityTheory.Rg.BcB.F.B3.locMatch`.

*Proof.* Write $mk = N + 1$. We use four inputs: the Theorem above; the identity of words, which says that at each $w \in B$ the trace of $\Pi(\ell)$ equals $\mathrm{tr}(\mathrm{fix}_a\beta^{N+1})_w$ and that the unitary side at $w \in B$ is the $k$-th power of $g_U(m)_w$; the matching at good places, which says that a word in spherical Hecke operators and their adjoints at a good place matches its image with the character $\mu_w$; and the matching of the units at the places outside $B$, with the character $\mu_w$ at split places and the trivial character at inert places. These are proved in the companion development. For part 1, $g_{0,w}$ is bi-invariant under $K_{U,w}$ at each $w \in B$ by the compatibility conditions, and convolution powers of a bi-invariant function are bi-invariant. For part 3, at $w \in B$ the unitary function is $g_U(m)_w^{*k} = g_U(N+1)_w$, and by the identity of words the general linear function is $\mathrm{tr}(\mathrm{fix}_a\beta^{N+1})_w$; these match by the Theorem above. At a good place outside $B$ we use the matching at good places, and at the other places outside $B$ we use the matching of the units. The test function property follows from the same property for each letter, because convolution keeps compact support and local constancy. For parts 2 and 4 pick $w_0 \in T$. There the support of $g_U(N+1)_{w_0}$ consists of elements with separable characteristic polynomial, and $\mathrm{tr}(\mathrm{fix}_a\beta^{N+1})_{w_0}$ is supported on regular pairs. Both facts come from the regularity part of the Iwahori matching, applied to the cone points in the support of $c_{w_0}$, and are proved in the companion development. $\square$

**Remark 7.5.6 (Formalization).** The local datum is `LocData` (FrameL.lean:22); its compatibility conditions are `Ok` (FrameL.lean) and `MOk` (MatchLM.lean:57), and the statement of the Proposition and the Theorem is `MatchLMB2` (MatchLM.lean:67). The matrices are the structure `LM` (AdelRep.lean:25), with a matrix part at the places of $T \cup S_0$ and two scalar components elsewhere; the power `pw L m` is $L^{m+1}$. The functions at $S_0$ (`mac`, built from `phiMu`) and the twisted constant term `ctMu` were not unfolded. `matchLMB2` (MatchAll.lean:52) passes its three inputs to `matchLMB3Of_pf`, which we have not unfolded; so the proof of the Proposition above follows the six inputs of that lemma (`MatchT`, `MatchSplitPlace`, `MatchBadS`, `MatchBadI`, `FixIdem`, `IdemAlg`), not an unfolded argument. `matchLMB2₀` (HM2.lean) applies it to `hM2 = match_principal_congruence_inert`, `hM3 = match_ctMu_of_isSplitAt` and `hM4`. The statements `M2` and `M3` are defined by `type_of%` (SymIdx.lean:20 to 22). MatchLM.lean:71 states `MatchLMB2Of` with a hypothesis `MatchLin` that the route actually used drops. `locMatch` (PLocMatch.lean:143) takes `LocWord`, `MatchLMB2`, `MatchLMWordS` and `MatchLMUnit` as inputs, which are the four inputs of its proof above; parts 2 and 4 come from `sepPowT` and `regPowT` (GeneratorPowSplitPlacesOfIdempotent.lean:22 to 23), which are wrappers for `GlobalTheory.T.separable_power_torus` and `GlobalTheory.T.regular_power_torus`. In FrameL.lean:84 and in `IsGen`, a Boolean argument that chooses which of the two scalar components is updated is named `intersection_update_fsHerm_neg_one`, a name with no relation to its role.
