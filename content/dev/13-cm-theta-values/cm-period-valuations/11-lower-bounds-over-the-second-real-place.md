---
title: Lower bounds over the second real place
decls:
  - GlobalTheory.T.local_model_bound_place_over_second_embedding
  - GlobalTheory.TwU.LowF.lowAt_F
  - GlobalTheory.TwU.LowF.kval_general
  - GlobalTheory.TwU.LowF.kval_orbit
  - GlobalTheory.T.exists_letterCoordinates_series_onePlace_alt
  - GlobalTheory.OnePlace.exists_letterCoordinates_series_onePlace
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lower bounds over the second real place

This section proves a lower bound for the pending tuple of a formal group system at each place of a gate that lies over the second real place. We first write the theta series of a pending tuple at one place in letter coordinates. This gives an orbit theta expansion in the sense of Section 9, and the orbit bound then gives the lower bound. The result is used in [the theorem on twisted systems at admissible sites](/entry/sys-tw-sites/), which is the main step of the twisted unitary row in Section 12.

### Letter coordinates

Let $p$ be a prime and $\mathbb{C}_p$ the completion of an algebraic closure of $\mathbb{Q}_p$. Let $K_0$ be the coefficient field of the formal group systems at $p$, with its map $\iota : K_0 \to \mathbb{C}_p$. Let $n' \ge 1$ and $r_0, r_1 \ge 0$, and let $\mathcal{E} = \mathcal{E}(n', r_0, r_1)$ be the index set of the variables of a place of degree $n'$ between ranks $r_0$ and $r_1$. A series $U$ over $K_0$ in two copies $X_e, Y_e$ ($e \in \mathcal{E}$) of these variables is *integral* if its parameter form is integral.

**Definition 5.11.1 (One place theta series).** Let $B$ be an $\omega$-basis for $(p, n')$ and $\beta \in K_0[[x, y]]$ a series with the $\beta$-property. For an integral $U$ put

$$
\theta_1(B, \beta, U) = \Theta_B\Big(\exp\Big(-\sum_{e \in \mathcal{E}} \beta(X_e, Y_e)\Big)\, U\Big),
$$

where $\Theta_B$ is the theta series of $B$ at the parameter $1$. We read $\theta_1$ as a series in variables indexed by $\mathbb{Z}/n' \times \{1, \dots, r_0\} \times \{1, \dots, r_1\}$, the *letters*.

The $\beta$-property gives in particular that the constant term of $\beta$ is $0$, so the exponential makes sense. The $\omega$-basis and the $\beta$-property are not unfolded here.

**Theorem 5.11.2 (Letter coordinates at one place).** Let $p \ge 5$ be a prime and $n' \ge 1$ even. Let $B$ be an $\omega$-basis for $(p, n')$ and $\beta$ a series with the $\beta$-property. Then there is a series $b$ over $\mathbb{C}_p$ in variables indexed by $\mathbb{Z}/n'$, with the four letter conditions B1 to B4, such that the following holds. For all $r_0, r_1$ and every integral $U$ there is a series $U'$ in the letters, with all coefficients of norm at most $1$, such that

$$
\begin{aligned}
&\iota\, \theta_1(B, \beta, U) \circ (1 \cdot \lambda_G)\\
&\quad = U' \cdot \Big(\exp\Big(-\sum_{a = 1}^{r_0} \sum_{b' = 1}^{r_1} b(z_{\cdot, a, b'})\Big) \circ \lambda_G\Big).
\end{aligned}
$$

Here $\lambda_G$ is the jet logarithm, $\circ\, \lambda_G$ means that $\lambda_G$ is substituted for each letter, and $z_{\cdot, a, b'}$ is the family $(z_{s, a, b'})_{s \in \mathbb{Z}/n'}$ of letters.

Lean: `GlobalTheory.OnePlace.exists_letterCoordinates_series_onePlace` (also `GlobalTheory.T.exists_letterCoordinates_series_onePlace_alt`, a second name)

*Proof.* Choose a Frobenius automorphism $\sigma$ with its Witt compatibility. The map $\iota$ carries $\beta$ to a series that satisfies the axioms of a $\beta_0$ series for $\sigma$, and in particular its constant term is $0$. The $\omega$-basis gives a dual basis for $\sigma$, since $n'$ is even. A lemma on unramified coordinates, which uses $p \ge 5$, then gives the series $b$ with B1 to B4, together with coordinates $t$ and $x$ and a similarity relation. A lemma on bivariate pairs writes $\exp(-\sum \iota\beta)$, read in the coordinates, as an integral series $V$ times the exponential of the pair sum of $b$. A second lemma on pairs carries this to every pair of ranks $(r_0, r_1)$, with an integral factor $U_2$. The substitution $\xi_x$ of the coordinates is integral, so $U_2 \cdot \xi_x(\iota U)$ has coefficients of norm at most $1$. We take $U'$ to be this product. Finally, a reading lemma for $\theta_1$ identifies the substituted theta series with the coordinate form, and the identity follows from the identity for $U_2$. $\square$

The left side is $\theta_1$ with the jet logarithm put in for the letters. So the theorem says that $\theta_1$ has an orbit theta expansion in the sense of Section 9, with $\varepsilon = 1$, $s_g = -1$ and exponent $b$.

### Orbit numbers and the bound at one place

Let $D$ be a datum with size data $L$, an instance $X$, constants $K$ and error constants $c_e$. Let $p$ be a prime that is not of signal class, and let $H_D$ and $h_P(p) \in H_D$ be as in Section 9. A *point* over the second real place is an element $t \in H_D$. Its orbit is the sequence $\mathrm{pos}(t, s)$ for $s \ge 0$, with $\mathrm{pos}(t, 1) = t + h_P(p)$. For $j \ge 1$ the *orbit number* $F_{\mathrm{orb}}(j, p, t)$ and the *orbit error* $\mathrm{err}(j, p, t)$ are real numbers. The error is built from the sum of the place weights $w(j, \cdot)$ along the orbit and from the number of tops of the orbit. Both are invariant under the step of the orbit:

$$
F_{\mathrm{orb}}(j, p, \mathrm{pos}(t, e)) = F_{\mathrm{orb}}(j, p, t), \qquad \mathrm{err}(j, p, \mathrm{pos}(t, e)) = \mathrm{err}(j, p, t).
$$

For the error this holds because a shift of $\mathbb{Z}/n_P(p)$ permutes the orbit. Apart from this, the two numbers are not unfolded here.

We use three hypotheses on the constants. The *split bound* $(11, 1)$ is [the split bound](/entry/split-bound-eleven-one/) of the sharp restriction chapter. *Largeness* $(11, 1)$ of $(K, c_e)$ asks that the constants are nonnegative, that $C_6 \le c_6$ and $3 C_d \le 1 + \delta_1$, that $\delta_1, \delta_2 \ge 0$, and that $3 C_d \le$ the digit bound. The *shape* of an entry $\mathrm{Ee}$ is the condition of Section 9.

**Theorem 5.11.3 (Orbit bound at one place).** Assume the split bound $(11, 1)$, the shape of $\mathrm{Ee}$ and largeness $(11, 1)$ of $(K, c_e)$. Let $p$ be a prime of inert class that satisfies the orbit condition, with $h_P(p) \ne 0$ and $p \le X''$. Let $u$ be a word, $i < m$ and $t \in H_D$. Put $n = n_P(p)$, $r_0 = N(i)$ and $r_1 = N(i + 1)$. Let $B$ be an $\omega$-basis for $(p, n)$, $\beta$ a series with the $\beta$-property, and $U$ integral. Then

$$
\mathrm{Kv}\big(\iota\, \theta_1(B, \beta, U)\big) \ge F_{\mathrm{orb}}(i + 1, p, t) - \mathrm{err}(i + 1, p, t),
$$

where $\mathrm{Kv}$ is taken along the diagrams $s \mapsto \nu_{u, i}(\mathrm{pos}(t, s))$ of $\mathrm{Ee}$ for $s \in \mathbb{Z}/n$.

Lean: `GlobalTheory.TwU.LowF.kval_orbit` (also `GlobalTheory.TwU.LowF.kval_general`, the same statement for any $n, r_0, r_1$ equal to $n_P(p), N(i), N(i+1)$)

*Proof.* The orbit condition gives $p \ge 5$ and that $n$ is even. By the theorem on letter coordinates, $\theta_1(B, \beta, U)$ has an orbit theta expansion with $\varepsilon = 1$, $s_g = -1$ and an exponent $b$ with B1 to B4. A theorem on the orbit bound over the second embedding at any base point, not unfolded here, takes these data, the split bound, the shape, largeness, the orbit condition, the inert class, $h_P(p) \ne 0$ and $p \le X''$. It gives the bound. $\square$

### The lower bound at a place of the gate

Let $u$ be a word and $w$ a place with its index condition, of residue characteristic $p$. Let $Y$ be a lattice instance whose lattice tie to $X$ holds and which fills every gate. A formal group system at the gate of $(u, w)$ has places $v$, each with a degree $n'(v)$, and a pending tuple $Y_5$ with a series $\beta = \beta(Y_5)$.

**Definition 5.11.4 (Place cofactor bound).** Let $g \in \mathbb{R}$, $j \ge 0$ and $v$ a place of the system. The series $\beta$ has the *place cofactor bound* $g$ at $(j, v)$ if for every integral $U$, every column choice $I$ at level $j$ and every monomial $n$, the coefficient of $n$ in the jet operator of $(j, I, v)$ applied to the theta series of $\exp(-\varphi_v)\, U$ is $p^{\lceil g \rceil} a$ for some Witt vector $a$. Here $\varphi_v = \sum_e \beta(X_{v, e}, Y_{v, e})$ is the sum over the variables of $v$.

A lemma on pending tuples says: if the constant term of $\beta$ is $0$ and $\beta$ has the place cofactor bound $g$ at $(j, v)$, then $Y_5$ has the *lower bound* $g$ at $(j, v)$. The lower bound itself is not unfolded here.

**Theorem 5.11.5 (Lower bound at a place over the second real place).** Assume the lattice tie of $X$ and $Y$, that $Y$ fills every gate, the split bound $(11, 1)$, the shape of $\mathrm{Ee}$, largeness $(11, 1)$, and $p \le X''$. Let $Y_5$ be a pending tuple of a formal group system at the gate of $(u, w)$, with levels, a chain and its local data, and assume that $\beta(Y_5)$ has the $\beta$-property. Let $v$ be a place with $n'(v) = n_P(p)$ and $t \in H_D$, and assume that the $s$-th position of $v$ in the gate is $\tau(\mathrm{pos}(t, s))$ for every $s$. Then for every $i < m$, $Y_5$ has the lower bound $F_{\mathrm{orb}}(i + 1, p, t) - \mathrm{err}(i + 1, p, t)$ at $(i, v)$.

Lean: `GlobalTheory.TwU.LowF.lowAt_F` (also `GlobalTheory.T.local_model_bound_place_over_second_embedding`, a second name)

*Proof.* The index condition says that $p$ is of inert class, and a lemma on served primes gives $h_P(p) \ne 0$. The index condition and the standard data at $v$, which give that $n'(v)$ is even and at least $2$, show that $p$ satisfies the orbit condition. The $\beta$-property gives that the constant term of $\beta$ is $0$. The lattice tie gives that the filling adds $t_D$ vectors at each step, so the ranks of the system are $N(j)$. By the lemma on pending tuples it is enough to prove the place cofactor bound. A restriction lemma writes the theta series at $v$ for an integral $U$ as $\theta_1$ of the $\omega$-basis of $v$, $\beta$ and an integral restriction of $U$. A lemma on agreement of valuations reduces the place cofactor bound to the bound on $\mathrm{Kv}$, provided the diagrams agree. They agree: the row lengths of the diagram of the system at $(i + 1, s)$ are those of $\nu_{u, i}(\mathrm{pos}(t, s))$, by a lemma on the diagrams of the formal group, the row property of $\mathrm{Ee}$ and the hypothesis on positions. The orbit bound at one place now gives the bound. $\square$

**Remark 5.11.6 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.exists_letterCoordinates_series_onePlace_alt` and `GlobalTheory.T.local_model_bound_place_over_second_embedding` are second names, each proved by `first | exact @… | …` under `maxHeartbeats 1000000`. `GlobalTheory.TwU.LowF.kval_general` only substitutes $n$, $r_0$, $r_1$ into `kval_orbit` (LocalModelBoundPlaceOverSecondEmbedding.lean:48).
2. The left side of the letter identity has the factor `MvPowerSeries.C (1 : ℂ_[p]) * jetLogG`, a product with $1$ (ExistsLetterCoordinatesSeriesOnePlace.lean:27).
3. `FOrb` has two definitions, Formalism/LocalRingCardinality/DataForced.lean:99 and Numbers.lean:165, and `OrbitPlaces.errF` (Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean:239) has a second copy at SumConsecutiveRanks.lean:15.
4. The field `K0` and the predicates `BeProp`, `OmBasis`, `IntS`, `Pend.LowAt` and `B1` to `B4` are not unfolded here, and neither is the lemma `orbitBound_overSecondEmbedding_anyBasePoint`.
