---
title: Orbit labellings and row data
decls:
  - UpperTheory.labelSet_ev_of_geo_of_not_dvd_discr
  - UpperTheory.labelSetGeo_of_even_of_rankOK_of_not_dvd_discr
  - UpperTheory.lattice_pairs_odd_degree_isometric
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbit labellings and row data

This section turns a labelling of the Frobenius orbits of embeddings into the row data that the degree bounds of Section 7 need. The first theorem proves the characteristic condition for each self-conjugate chart of the labelling. The second theorem assembles row data for all orbits, with the ranks that the multiplicities of the CM type give, and proves the block bound for their valuations. The third theorem is of a different kind: it shows that at an inert prime of odd period, the theta series of a pair of lattices in standard coordinates has the theta product form. The row data feed [the theorem on packages at inert primes](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/), and the theta product form feeds [the Frobenius conjugation conditions for the adapted kernel datum](/entry/frobenius-conjugation-conditions-adapted-kernel-datum-alt/).

### Labellings

We keep the notation of Section 5. Let $E$ be a CM field whose ring of integers has an involution equal to complex conjugation. Let $T$ be a complete discrete valuation ring, let $y$ be an integral frame over $T$ with an integral chart, and let $\iota$ be an embedding of the fraction field of $T$ into $C$ that respects the valuations. Let $Y$ be the base change of the integral chart along $\iota$, with an integer $k$. A label set with orbits $O_b$ and $d$ positions is *arithmetic* and *geometric* as in Section 5, and then each orbit $o$ gives self-conjugate data $P_o$ on $Y$. The label set has rank numbers $n$, $j$ and $j'$ and a relation *big* on triples $(o, g, a)$. It satisfies the *rank condition* if for each orbit $o$, the pair $(1 - g, a)$ is big if and only if $(g, a)$ is not, and the multiplicity of $\tau_{o,a}$ in the CM type is $n + j$ when $(0, a)$ is big and $j'$ otherwise, with the same rule at $g = 1$ for $\tau_{o, a - h_d}$. The *big rule* says that $(0, s)$ is big at $o$ if and only if $s$ is even, where $s$ runs through $\{0, \ldots, d - 1\}$.

**Definition 6.6.1 (Characteristic condition).** Let $X$ be a raw chart with a family of Cartier hypotheses. The *characteristic condition* holds if for every big $(g, a)$ and every saturated family $w_1, \ldots, w_n$ of integral vectors that are supported on the indices of type $a$, there are integral vectors $y_1, \ldots, y_n$ with these properties:
- for every system of typical curves, each germ $\exp(\sum_x y_{\rho, x} X_x)$ lies in the integral germs;
- if the alternation condition holds, then $v\bigl(\det(\langle y_\rho, w_c\rangle)\bigr) \le n\gamma_l + (j + j')/(l - 1)$;
- if every $(g, b)$ is big, then $v\bigl(\det(\langle y_\rho, w_c\rangle)\bigr) \le (j + j')/(l - 1)$.

Here $n$, $j$ and $j'$ are the rank numbers of the raw chart and $\gamma_l$ is a fixed constant.

**Theorem 6.6.2 (Characteristic condition at an inert labelling).** Assume the upper bound law for formal groups at every prime. Let $E$, $T$, $y$, $\iota$ and $Y$ be as above, with $y$ algebraic. Let the label set be arithmetic and geometric, with the rank condition and the big rule, with $d$ even, and assume that $l$ does not divide the discriminant of $E$. Then for every orbit $o$ and every family of Cartier hypotheses on $Y_{P_o}$, the characteristic condition holds.

Lean: `UpperTheory.labelSet_ev_of_geo_of_not_dvd_discr`

*Proof.* Since $l$ does not divide the discriminant of $E$, it does not divide the discriminant of any $\mathbb{Z}$-basis of $O_E$. The integral chart has a cover: a finite injective integral map $T \to T'$ of complete discrete valuation rings and a chart over $T'$ with geometric data. The prime $l$ is not a unit in $T$, because $\iota$ respects the valuations and $v(l) = 1$. So $l$ is not a unit in $T'$, since $T'$ is integral over $T$. The upper bound law at $l$ and the geometric data give the upper bound law over $T'$, and the law descends to $T$. Now [the upper bound for characters](/entry/up-char-s-chart-l/) gives characters of $Y$ with the cokernel bounds, and these bounds give the characteristic condition, by the rank hypothesis of the label set. $\square$

The proof uses neither the algebraicity of $y$, nor the parity of $d$, nor the big rule.

### Row data

*Row data* over $C$ with $d$ types and index sets $I$ and $J$ consist of two Cartier charts $G_0$, $G_1$ and integers $n, j, j', r_h, r$ with $r = n + j + j'$. A complementary rule says which $(g, a)$ are big: $(1 - g, a)$ is big if and only if $(g, a)$ is not. For big $(g, a)$ there are $n + j$ indices of type $a$, and $j'$ for the others. The data also include integral pairings between $J_g$ and $I_{1-g}$ that vanish between different types. Row data are *alternating* if $d$ is even and the big rule holds. A *flag* on row data and the *valuation block bound* $\mathrm{VB}(h_d, X, F, n_W, g_a, \nu)$ are defined in the setting of the row families. The bound says that for all lists of block monomials that attain their values along the flags, have one type each, have total size at most $n_W$ and have weight sums $g_a$, the sum of the values is at least $\nu$.

For an assignment $a(\tau, i)$ of integers to the embeddings $\tau$ of $E$ and to the indices $i$, the *weight tie* with $g_a$ says that $a(\tau_{o,s}, i) = \sum_{k = i + 1}^{r} g_a(o, s, k)$ for $i < r = \mathrm{mult}(\tau_{o,s})$, and that $a(\sigma, i) = 0$ for the embeddings $\sigma$ that are not labels. The *local value* $\nu_{\mathrm{loc}}(a, n_W)$ of the integral chart is the infimum of the valuations of a fixed differential expression over the integral series and the polynomials of the class that $a$ defines.

**Theorem 6.6.3 (Row data from a geometric labelling).** Assume the upper bound law at every prime. Let $E$, $T$, $y$, $\iota$ and $Y$ be as above, with $y$ algebraic, and let the label set be arithmetic, with a finite set of orbits. Assume that $l$ does not divide the discriminant of $E$, that $d$ is even, that the rank condition and the big rule hold, and that $j' < n$. Let $a$ and $g_a$ be given with the weight tie, such that $g_a(o, s, k) \ne 0$ only for $1 \le k \le \mathrm{mult}(\tau_{o,s})$. Then for every $n_W$ and every real $\nu \le \nu_{\mathrm{loc}}(a, n_W)$ there are row data $X_o$ and flags $F_o$ for every orbit $o$ such that:
- $X_o$ has rank numbers $n$ and $j + j'$ of the label set, is alternating, and has $\mathrm{rk}_0(s) = \mathrm{mult}(\tau_{o,s})$ for every $s$;
- the valuation block bound $\mathrm{VB}(h_d, X, F, n_W, g_a, \nu)$ holds.

Lean: `UpperTheory.labelSetGeo_of_even_of_rankOK_of_not_dvd_discr`

*Proof.* An arithmetic label set is also geometric for the base change of an integral chart. For each orbit we must check the hypotheses of the raw chart $Y_{P_o}$:
- characteristic $0$, algebraic closure, $l$ odd and $v(k) = 0$ come from $Y$;
- the Cartier hypotheses follow from [the typical curves through a point](/entry/pt-self-holds/) and the stability condition;
- the rank hypothesis comes from the rank condition of the label set;
- the axes, the germ at zero and the equality of the two charts at the axes are theorems for self-conjugate data;
- the rank maximal condition follows from [the rank maximal condition for self-conjugate charts](/entry/rank-maximal-self-unconditional/) and [the nondegeneracy of the biextension](/entry/biextension-nondegenerate-mod-maximal-ideal-integral-chart/);
- the independence bound follows from the rank maximal condition;
- the characteristic condition is [the last theorem](/entry/label-set-ev-of-geo-of-not-dvd-discr/).

These hypotheses give row data $X_o$. The type of an index $x$ of $I$ is the position of $x$ at $g = 0$ and the position plus $h_d$ at $g = 1$. So the rank at $(0, s)$ is $\mathrm{mult}(\tau_{o,s})$ and the rank at $(1, s + h_d)$ equals the rank at $(0, s)$. Take $F_o$ to be the standard flag for these ranks. Every list of block monomials lies in the family of the self-conjugate places, by the weight tie. The value of the self-conjugate row data at the letter system of the chart is at least $\nu_{\mathrm{loc}}(a, n_W) \ge \nu$, by descent, by the separation of the labels and by the unit germ. These facts give the valuation block bound. $\square$

### The theta product form at an odd inert prime

Fix a prime $l$, an integer $i \ge 1$ and a map $\mathrm{pos}$ on a finite set of positions with $\mathrm{pos}(z, 0) = z$, $\mathrm{pos}(\mathrm{pos}(z, a), b) = \mathrm{pos}(z, a + b)$ and $\mathrm{pos}(z, i) = z$. For a position $z$ and an index $b$, the *logarithm* at $(z, b)$ is
$$\log_S(X)_{(z, b)} = \sum_{e \ge 0} l^{-e} X_{\pi^e(z, b)}^{\,l^{2e}},\qquad \pi(z, b) = (\mathrm{pos}(z, 2(i - 1)), b).$$

**Definition 6.6.4 (Theta product form).** A series $\Theta$ in the variables $X_{(z, b)}$ over a normed field $K$ has the *theta product form* with $l$, $i$ and $\mathrm{pos}$ if there are a subfield $K_0$ whose nonzero elements have norms that are powers of $|l|$, a primitive $(l^{2i} - 1)$-th root of unity $\zeta$, a finite set $R$ of positions, an element $\varepsilon$ with $|\varepsilon| = 1$, signs $s_r = \pm 1$, and series $\beta_r$ in $2i$ variables with the pairing hypotheses over $K_0$ and $\zeta$, such that for some integral $U$,
$$\Theta\bigl(\varepsilon \log_S(X)\bigr) = U\cdot \exp\Bigl(\sum_{r \in R}\frac{s_r}{2}\sum_b \beta_r\bigl(X_{(\mathrm{pos}(r, s), b)}\bigr)_{s \in \mathbb{Z}/2i}\Bigr)\bigl(\log_S(X)\bigr).$$

The pairing hypotheses say that $\beta_r$ has coefficients in $K_0$, is invariant under the torus action of $\zeta$, has no terms of low bidegree, and that two exponentials built from its derivatives are integral with constant term $1$ in letter logarithms.

Let $D$ be the global datum, with a curve ideal, a twelfth root, a base $B$ and a character $\chi$. Let $p$ be a prime and $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$. The *host condition* at $p$ says: there are $c \in \mathbb{C}_p$ with $|c| = 1$ and curve data $(g_2, g_3, s_2, \varepsilon, \sigma, F)$ over the maximal unramified extension, and for every admitted pair $(L, L')$ a local basis $b$ of $Y(L, L')$ that is orthonormal, such that for every combination $G$ of torsion translates, the series obtained from $G$ by the substitution $c\,\lambda(b)$ has the host logarithm form for these curve data. The positions at $p$ are the pairs $(\epsilon, t)$ of a sign and an element of the host group. The map $\mathrm{pos}((\epsilon, t), e)$ moves $t$ by $e\,h_p$ for a fixed element $h_p$, and changes the sign, when $e$ is odd, only at primes of the signal class. At an inert prime its period $n_p$ is the order of $h_p$.

**Theorem 6.6.5 (Theta product form at an odd inert prime).** Assume the host condition at $p$, that $p \ge 5$, that $p$ is inert, and that the period $n_p$ is odd. Let $(L, L')$ be an admitted pair with standard bases $P$ and $P'$. Then for every combination $G$ of torsion translates, the series of $G$ in the standard coordinates of $P$ and $P'$, with all scalars equal to $1$, has the theta product form with $p$, $n_p$ and the positions at $p$.

Lean: `UpperTheory.lattice_pairs_odd_degree_isometric`

*Proof.* The host condition gives $c$, the curve data and, for $(L, L')$, the local basis $b$. The positions satisfy the three laws above with period $n_p$. Since $\sigma$ is an unramified Frobenius and $n_p$ is odd, there is a unit $\omega$ that is a quotient for the norm-one condition. Choose a set $R$ of representatives of the orbits of $\mathrm{pos}$. A coordinate change $\gamma$ for odd inert orbits takes the standard coordinates to the coordinates of $b$, with the substitution of the logarithm on the orbits. The substitution of unitary logarithmic coordinates keeps the integrality of the host form. The integral exponential of a sum of logarithms over an odd period then gives the theta product form, after the linear substitutions are composed. $\square$

**Remark 6.6.6 (Formalization).** In the theorem on the characteristic condition, the hypotheses `y.IsAlg`, `Even d` and the big rule are bound by the intro pattern as `_` and never used ([LabelSetEvOfGeoOfNotDvdDiscr.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/LabelSetEvOfGeoOfNotDvdDiscr.lean#L24)). The predicate `IntFr.IsAlg` itself does not depend on its argument (VAtVNeBot.lean, line 83). The name `labelSetGeo_of_even_of_rankOK_of_not_dvd_discr` suggests a conclusion `LabSGeo`, but the theorem proves the existence of row data with `ValBlocksS`; it derives `LabSGeo` inside the proof ([LabelSetGeoOfEvenOfRankOKOfNotDvdDiscr.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/LabelSetGeoOfEvenOfRankOKOfNotDvdDiscr.lean#L16), line 28 for the inner step). The name `lattice_pairs_odd_degree_isometric` does not describe the conclusion `HasThetaProductForm`. The text does not unfold `RF.Flag`, the block monomials `RF.GlobalTheory`, `nuLocC`, `IsComb`, `HostLog`, `BHyp`, `UpFSt` or the constant `gam`.
