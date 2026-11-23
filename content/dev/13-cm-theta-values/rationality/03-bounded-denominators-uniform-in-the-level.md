---
title: Bounded denominators uniform in the level
decls:
  - GlobalTheory.T.exists_forms_theta_short_series_identity
  - GlobalTheory.LevelSeries.SerId.exists_forms_of_transSum
  - GlobalTheory.LevelSeries.series_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bounded denominators uniform in the level

This section proves the main estimate of the chapter. A theta series of a vacuum pair with $\dim W$ odd, made from a level function with values in a local ring at a place above $l$ and from a harmonic polynomial with coefficients in that ring, is $l^{-c}$ times an integral combination of sections of the Shimura variety. The exponent $c$ does not depend on the auxiliary level of the cover. The proof has two parts. The first part is an exact identity at a half-level idempotent: a theta series of a mean of translates equals a combination of sections whose denominators are bounded by an explicit number. The second part reduces the general series to this case, with [the flip to a half-level idempotent](/entry/exists-flip-theta/) of Section 2 and three more bounds. [The theorem on integrality](/entry/ser-int-outright/) of Section 1 uses the result.

### Shimura varieties and their sections

Fix a Hermitian space $W$ of odd rank $r = p + q$. A *level* is an integer $M$ with an ideal of $\mathcal{O}_E$, and a *moduli space* $X$ of that level is a finite union of Shimura varieties for $\mathrm{U}(p, q)$ with a coefficient field $k$ and an embedding $\sigma : k \to \mathbb{C}$. An *unfolding* $U$ of $X$ is a uniformization of its components by symmetric domains, with frames of rank $r$. A *dictionary* sends an element $g$ of the adelic group of $\mathrm{U}(W)$ to a component of $X$ and a frame. Through the dictionary, each section $f$ of the automorphic bundle of weight $a$ on $X$ gives a function $\mathrm{rd}_U(f)$ on the frames. The dictionary comes with a scalar $\mu(g)$ and with constants $c(k)$ on the components; they compare the theta kernel with the reading of a section. Let $\kappa_a > 0$ be the real factor that compares the derivatives in the Lie algebra with the reading of a section of weight $a$. It depends only on $a$.

Let $\lambda$ be a place of $k$ above a prime, and let $O \subseteq \mathbb{C}$ be a subring that contains $\sigma(x)$ for every $x \in k$ that is integral at $\lambda$. A section $f$ has *denominators bounded by $b$ at $\lambda$* if, at every point of $X$ over the integers of a finite extension and above $\lambda$, the value of $b f$ is integral. In this case we say that $f$ is *$b$-bounded at $\lambda$*.

For a level $l$ of a cover, an embedding $\iota$ of the lattice of the datum into $E^{\dim W}$, and a function $u$ on the $l$-torsion points $q$ of $(\mathcal{O}_E / M)^{\dim V}$, the *translate mean* is
$$\mathrm{tm}(u) = \frac{1}{\# Q}\sum_{q \in Q} u(q)\,\rho\big(y(q)\big) f_0 ,$$
where $Q$ is the set of these torsion points and $y(q)$ is the point $e\,\iota(q)/M$, supported at a half-level idempotent $e$.

**Theorem 3.3.1 (Theta series of a translate mean).** Let $(\omega, \Lambda_V, \Lambda_W, f_0)$ be a vacuum pair, and let $X$, $U$ and the dictionary be as above, with the dictionary compatible with the frames and the constants of the vacuum identity, the level with trivial auxiliary part, and $r$ odd. Let $e$ be a half-level idempotent. Let $h$ be an element of the finite adelic group of $V$ that is supported at an idempotent sum $e'$ over a set $P_s$ of places prime to a multiple $b$ of the level, with determinant $y$ at $e'$. Let $\Lambda$ be the lattice attached to $h$; assume that $\Lambda$ is unimodular, trivial at the level, and of level $N$. Let $\lambda$ be a place of $k$ above a prime $p$ at which the level is good, and $O$ as above. Let $u$ have values in $O$, and let $Q$ be a harmonic polynomial of weight $a$ with coefficients in $O$. Then there are $\beta_1, \dots, \beta_m \in O$ and sections $f_1, \dots, f_m$ of weight $a$, each with holomorphic reading that vanishes to the right order at the boundary and with denominators bounded at $\lambda$ by
$$B = i_N(\Lambda) \cdot \#Q \cdot (2\,d_E\,N)^{\deg a},$$
such that for all $g$:
$$\theta\big(h, g; \mathrm{tm}(u), Q\big) = (-1)^{\deg a}\,\gamma(y, \Lambda)\sum_{k} \beta_k\,\kappa_a\,c(k_g)\,\mu(g)\,\mathrm{rd}_U(f_k)(g) .$$
Here $d_E$ is the discriminant of $E$, $i_N(\Lambda)$ is an index attached to $\Lambda$, $N$ and the signature, and $\gamma(y, \Lambda) = \chi_W(y)^{-1}\,[\Lambda : \Lambda \cap \Lambda_0]^{-r/2}$, with $\Lambda_0$ the standard lattice.

Lean: `GlobalTheory.LevelSeries.SerId.exists_forms_of_transSum` (also `GlobalTheory.T.exists_forms_theta_short_series_identity`, a second name).

*Proof.* Extend the unfolding $U$ to a family of unfoldings, one for each good embedding of $k$; the development constructs one for each good embedding, and the given $U$ is kept at $\sigma$. Choose a level datum one step higher than the level, with the same auxiliary part, as the development provides.

Write $u(q)\,Q = \sum_k \beta_k\,\sigma(P_{k,q})$, with $\beta_k \in O$ and harmonic polynomials $P_{k,q}$ over $k$ whose coefficients are integral at $\lambda$. Such an expansion exists because $O$ contains the image of the $\lambda$-integral elements: choose a basis of $k$ with integral coordinates at $\lambda$, and expand each product $u(q)\cdot(\text{coefficient of } Q)$ in that basis. Harmonicity is preserved, because the harmonic polynomials are cut out by linear conditions over $k$.

For each $k$, the theta sum of the family $P_{k,q}$ is invariant under the automorphisms of the level, and the development gives a cusp section $f_k$ of weight $a$ whose reading is the theta sum. The bound for theta sums on covers gives the bound $B$ for the denominators of $f_k$ at $\lambda$. The value identity for theta sums gives
$$\sum_q \theta\big(h, g; \rho(y(q)) f_0, \sigma(P_{k,q})\big) = (-1)^{\deg a}\,\gamma(y,\Lambda)\,\kappa_a\,c(k_g)\,\mu(g)\,\mathrm{rd}_U(f_k)(g)$$
after the factor $1/\#Q$ is put in. Sum over $k$ with the weights $\beta_k$. The theta series is linear in the Schwartz function and in the polynomial, so the sum is the theta series of $\mathrm{tm}(u)$ with $Q$. $\square$

### The bound

**Theorem 3.3.2 (Bounded denominators).** Let $(\omega, \Lambda_V, \Lambda_W, f_0)$ be a vacuum pair with $\dim W = r$ odd, and let $(\chi, M_0)$ be tied to $\chi_W$ with $M_0 \ne 0$. Fix the signature $(p, q)$ with $p + q = r$, orthonormal archimedean frames, the letters of the harmonic polynomials and a dominant weight $a$. Let $l$ be a prime and $s$ an element of the finite adelic group of $V$. Then there is $c \in \mathbb{N}$ with the following property. Let $l_2$ be a level with $M = M_0\,p_d$, $p_d$ prime to $M_0$ and to $l$, $M$ prime to the bad number, trivial auxiliary part, and good at $l$. Let $X$ be a moduli space of level $l_2$ with coefficient field $k$ and embedding $\sigma$, $U$ an unfolding and a dictionary as above, and assume that $\chi$ takes values in $\sigma(k)$ up to weight $-1/2$. Let $\lambda$ be a place of $k$ above $l$ and $O$ as above. Let $\Phi$ be a level function for an idempotent sum $\bar{e}$ over places that divide $M$, with values in $O$, and let $\varphi$ be the Schwartz function that $\Phi$ defines. Let $Q$ be a harmonic polynomial of weight $a$ with coefficients in $O$. Then there are $\beta_1, \dots, \beta_m \in O$ and sections $f_1, \dots, f_m$ of weight $a$, holomorphic in the above sense and $1$-bounded at $\lambda$, with
$$l^{c}\,\theta(s, g; \varphi, Q) = \sum_k \beta_k\,\kappa_a\,c(k_g)\,\mu(g)\,\mathrm{rd}_U(f_k)(g) \quad \text{for all } g .$$

Lean: `GlobalTheory.LevelSeries.series_bound`

*Proof.* The exponent is a sum $c = vK + c_f + c_a + c_3$ of four terms. Each term comes from one result, and all four are chosen before the level $l_2$.

1. The development proves a uniform level bound for vacuum pairs: there is $K$ such that $M^K \varphi$ lies in the $O$-span of the Heisenberg translates of $f_0$ by $M$-torsion points, for every level function $\varphi$ of level $M$ with values in $O$. Write $M_0 = l^v M_1$ with $l \nmid M_1$. Then $M_1 p_d$ is prime to $l$, so it is a unit in $O$, and $l^{vK}\varphi$ lies in a translate span.
2. [The flip to a half-level idempotent](/entry/exists-flip-theta/) gives a finite set $Z$ and $c_f$, and moves the support of the translates to a half-level idempotent at the cost of $l^{c_f}$ and of the translate $s z_2 z_1$.
3. For each $z \in Z$, the development proves that the series at $s z$ is a series at a point $h$ of $\omega(a, 1)$ applied to the Schwartz function, with $a$ a rational point of bounded $l$-denominator. There are finitely many $z$, so one bound serves all of them. The action of a rational point on the harmonic polynomial is a substitution; it gives $c_a$ with $l^{c_a}$ times the substituted polynomial integral.
4. [The theta series of a translate mean](/entry/exists-forms-of-trans-sum/) applies at $h$. Its factor $B$ divides $l^{c_3}$ times a number prime to $l$, and $c_3$ is chosen before the level. The number prime to $l$ is a unit in $O$, so one can divide by it. The development proves that the scalar $\gamma(y, \Lambda)$ lies in $O$.

The translate mean is the form that the half-level translates take after step 3. Combine the four steps: $l^{vK + c_f + c_a + c_3}\,\theta(s, g; \varphi, Q)$ is an $O$-combination of the readings of sections that are $1$-bounded at $\lambda$. $\square$

The theorem is local at $\lambda$: the ring $O$ is a local ring of $k$ at one place. The integrality at a set $S$ of places in Section 1 is the intersection over $\lambda \in S$.

**Remark 3.3.3 (Formalization).** The bound is at [SerIntAtOfSeriesRat.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SerIntAtOfSeriesRat.lean#L137). Its four inputs are `T.vacuum_pair_uniform_level_bound`, `T.exists_centralFlip_thetaTranslate_halfLevel`, `T.exists_levelSeries_translate_boundedDenominator` with `T.real_rational_point_acts_harmonic_substitution`, and `T.exists_forms_theta_short_series_identity` with `const_dvd` ([IsTorsionFreeIntOf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsTorsionFreeIntOf.lean#L99)). The identity at a half-level idempotent is at [ExistsFormsThetaShortSeriesIdentity.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsFormsThetaShortSeriesIdentity.lean#L231). Its helpers are `thetaSum_value_emb` (line 34), `exists_expansion` (line 173) and `exists_family` (line 210). The last one fills the family of unfoldings at a bad embedding with an empty unfolding, which is never used. The translate mean is `transSum`, the scalar $\gamma$ is `clsScal`, and the index factor of $B$ is `Λ.mIdx N (p + q)` ([IsInertTop.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsInertTop.lean#L33)). The bound on denominators is `GoodPts.BddAll`, and the ring condition is `ValRing`. The factor $\kappa_a$ is `lieFac`. The file sets `maxHeartbeats` to 4000000 for `thetaSum_value_emb` and 2000000 for the main identity. We have not unfolded `Unf`, `IsDict`, `CcIs`, `stdF`, `rdU` or `holSub0`; the text describes them by their role.
