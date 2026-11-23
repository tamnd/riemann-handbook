---
title: The twisted unitary row
decls:
  - GlobalTheory.Svd.rowTwU
  - GlobalTheory.Proof.UnitaryWeightModels.rowTwU_of_models
  - GlobalTheory.T.local_systems_lower_bounds_second_real_place
  - GlobalTheory.TwU.SiteSys.sysTw_sites
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twisted unitary row

This section proves [the theorem on the twisted unitary row](/entry/row-tw-u/). It says that if the local model condition of Section 5 holds in a row, then every family class is closed under the twisted unitary row condition, in a row. This is part 1 of the service condition of Section 6, and [the service row](/entry/serv-h-row/) uses it. The main step is the twisted system condition at admissible sites. It sums [the lower bounds over the second real place](/entry/low-at-f/) of Section 11 and compares the sum with the low sum of the error data.

We keep the notation of Section 11: the datum $D$, size data $L$, the instances $X$ and $Y$, the constants $K$ and $c_e$, an entry $\mathrm{Ee}$, the prime $p$ of a place $w$, the orbit numbers $F_{\mathrm{orb}}$ and the orbit errors $\mathrm{err}$, the split bound, largeness, the shape, and the lower bound of a pending tuple at a place.

### The twisted system condition

Let $\mathrm{LC}$ choose, for each tuple $\mu$, word $u$ and place $w$ with its index condition, levels and a chain for the filling of $Y$. Write $Y(\mathrm{LC})$ for $Y$ with these levels and chain at $\mu$. Let $Q_p(\mu)$ be the primes of $\mu$, $X_e$ the error data and $d_\Gamma$ as in Section 5. The *low sum* $\mathrm{low}(u, w)$ is the sum over the lifts $j$ of the value $L_F(j, w)$ of the size data minus the error term at $(u, j, w)$, plus a term $v_\Gamma(u, w)$ attached to $D_\Gamma$, which is not unfolded here. The places of the gate that are images of the representatives of $X$ at $p$ are the *first orbit places*.

**Definition 5.12.1 (Twisted system condition).** The *twisted system condition* holds for $\mathrm{LC}$ if, given the error definitions, for every used tuple $\mu$, every gate tie with the lattice tie of $X$ and $Y(\mathrm{LC})$ at $\mu$, every word $u$ and every place $w$ with its index condition and $p \notin Q_p(\mu)$, the following holds. There are local data of a formal group system at the gate, with a function $d_G$, and an admitted pending tuple $Y_5$, and real numbers $F_v(j)$ for the places $v$ of the gate, such that:
1. for every place $v$ that is not a first orbit place and every $j < m$, $Y_5$ has the lower bound $F_v(j + 1)$ at $(j, v)$;
2. the low sum is bounded:
$$
\mathrm{low}(u, w) \le \sum_{j = 1}^{m} \sum_{v} F_v(j) - \sum_{j < m} d_G(j),
$$
where $v$ runs over the places that are not first orbit places.

**Theorem 5.12.2 (Twisted systems at admissible sites).** Assume the lattice tie of $X$ and $Y$, that $Y$ fills every gate, that $L$ has its defining property, the split bound $(11, 1)$, the shape of $\mathrm{Ee}$ and largeness $(11, 1)$. Assume that site admissibility holds for $\mathrm{LC}$ at every used $\mu$, word $u$ and place $w$ with $p \notin Q_p(\mu)$. Then the twisted system condition holds for $\mathrm{LC}$.

Lean: `GlobalTheory.TwU.SiteSys.sysTw_sites` (also `GlobalTheory.T.local_systems_lower_bounds_second_real_place`, a second name)

*Proof.* Fix $\mu$, $u$ and $w$. Site admissibility gives the local data, $d_G$ with $d_G(0) = 0$ and $d_G(j) \le v_p(D_\Gamma)$, and an admitted pending tuple $Y_5$. A lemma on places off the first orbits gives a map $r$ from places to $H_D$. For each place $v$ that is not a first orbit place, it gives $n'(v) = n_P(p)$ and that the positions of $v$ are $\tau(\mathrm{pos}(r(v), s))$. It also says that the sum of $f(r(v))$ over these places equals the sum of $f(t)$ over the representatives $t$ of $X$ at $p$, for every $f$ that is invariant under $t \mapsto t + h_P(p)$. Put

$$
F_v(j) = \begin{cases} F_{\mathrm{orb}}(j, p, r(v)) - \mathrm{err}(j, p, r(v)) & p \le X'',\\ 0 & p > X''. \end{cases}
$$

Condition 1. If $p \le X''$, [the theorem on the lower bound at a place over the second real place](/entry/low-at-f/) applies, since admitted tuples have the $\beta$-property. If $p > X''$, the last condition of an admitted tuple gives the lower bound $0$.

Condition 2. A lemma on the second real place bounds uses the defining property of $L$ and the bounds on $d_G$. It bounds $\mathrm{low}(u, w)$ by the same sum with $t$ over the representatives in place of $v$. The function $t \mapsto F_{\mathrm{orb}}(j, p, t) - \mathrm{err}(j, p, t)$ is invariant under $t \mapsto t + h_P(p)$: we have $\mathrm{pos}(t, 1) = t + h_P(p)$ because $p$ is not of signal class, and both numbers are invariant under the step. So the two sums agree. $\square$

### The row

Let $\mathcal{F}$ be a family with scale $\varepsilon$ and threshold $x_1$. For each $x > x_1$ and each index $i$ it has a datum $D_{x, i}$, size data, instances $X_{x, i}$ and $Y_{x, i}$, primes $Q_p$, extra data $\mathrm{ex}_{x, i}$ with comparison map $c$ and twist $\tau$, constants $K$ and error constants. Its fixed constants include $\delta_1 = 5$, $\delta_2 = 4$, $c_6 = 12$ and digit bound $3$.

**Definition 5.12.3 (Twisted unitary row condition).** The family $\mathcal{F}$ satisfies the *twisted unitary row condition* if there is $x_0$ such that for every $x \ge x_0$ with $x > x_1$ and every $i$ there is a choice $\mathrm{LC}$ with two properties. The first is the valued comparison: for every word $u$, place $w$ with its index condition, used $\mu$ with $p \notin Q_p(\mu)$, vector $y$ at level $0$ and $s \in \mathbb{R}$, if $c(y)$ has valuation at least $s$ in $Y_{x,i}(\mathrm{LC})$ at $\mu$, then the twisted column of $y$ has valuation at least $s$. The second is the twisted system condition for $\mathrm{LC}$.

A family class $\mathcal{A}$ is *closed* under a condition $P$ if there is $\varepsilon_1 > 0$ such that for every $\varepsilon \in (0, \varepsilon_1]$ there are thresholds with the following property: every family of $\mathcal{A}$ with scale $\varepsilon$ that is large for them satisfies $P$.

**Theorem 5.12.4 (Twisted unitary row from local models).** Assume the split bound $(11, 1)$. Let $\mathcal{F}$ be a family. Assume that for all large $x$ and all $i$ some entry has the shape, and that for all large $x$ and all $i$ the extra data have local models. Then $\mathcal{F}$ satisfies the twisted unitary row condition.

Lean: `GlobalTheory.Proof.UnitaryWeightModels.rowTwU_of_models`

*Proof.* The fixed constants give largeness $(11, 1)$. Take $x_0$ the larger of the two thresholds, and fix $x$ and $i$. The local models give $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ and a choice $\mathrm{LC}$ with the light comparison and site admissibility at every used $\mu$. A lemma on column weight comparison turns the equality of step maps and the light comparison into the valued comparison. The theorem on twisted systems at admissible sites gives the twisted system condition. Its hypotheses are the lattice tie, filling and the defining property of $L$, all from the family and its extra data, together with the split bound, the shape and largeness. $\square$

**Theorem 5.12.5 (Twisted unitary row).** Let $Q$ be a slot and $\mathrm{Lk}$ a linkage. Assume that the local model condition satisfies the row condition for $(Q, \mathrm{Lk})$. Then the property "$\mathcal{A}$ is closed under the twisted unitary row condition" holds in a row for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.Svd.rowTwU`

*Proof.* We take $E$ to be the local model condition. Let $\sigma$ be a selection along $E$ for $\mathcal{A}$. We prove closure with $\varepsilon_1 = 1$ and all thresholds $0$. Let $\mathcal{F}$ be a family of $\mathcal{A}$. The selection gives, at each $(x, i)$, the local model condition for the object of $\mathcal{F}$. The split bound $(11, 1)$ holds by [the split bound](/entry/split-bound-eleven-one/). A lemma on shapes says that for large $x$ every entry has the shape. We use the entry with the diagrams of $D$ and zero numbers. A lemma on the weight gives $2 r_G(\varepsilon) \le k$ for $x \ge 71/\varepsilon$. With the lattice tie of the family, the local model condition gives local models. The previous theorem applies. $\square$

**Remark 5.12.6 (Formalization).** Several facts about the Lean code:
1. The name `GlobalTheory.T.local_systems_lower_bounds_second_real_place` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000`.
2. In `GlobalTheory.TwU.SiteSys.sysTw_sites` the premise `ErrDefs` of `SysTw`, and the gate tie and lattice tie at $\mu$, are introduced as `hE`, `hT'` and `hty'` and not used (LocalSystemsLowerBoundsSecondRealPlace.lean:49). For $p > X''$ the bound is the last field `a11` of `admitted` (line 63).
3. In `GlobalTheory.Svd.rowTwU`, `Closed` is witnessed with $\varepsilon_1 = 1$ and the zero thresholds `⟨0, fun _ => 0, fun _ => 0, fun _ => 0⟩`, and the shape is used for `entStd`, an entry with four zero fields (RowTwUHolds.lean:13 and :19).
4. `SysTw` has two definitions, ModelsOK.lean:25 and Formalism/SharpRestriction/SmoothDesignExistence/SumOverPrimesHypotheses.lean:116.
5. The term `ES` of `lowS` (WeilJacquetShalikaLaw.lean:73) and the lemma `low_term_le_second_real_place_bounds` are not unfolded here.
