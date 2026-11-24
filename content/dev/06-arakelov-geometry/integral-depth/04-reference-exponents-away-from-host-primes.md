---
title: Reference exponents away from the host primes
decls:
  - GlobalTheory.RefAway.refExp_le_of_oscLe
  - GlobalTheory.T.baseLocusExponent_le_oscillation_nonTypePrime
  - GlobalTheory.RefSum.GlobalPoly.exists_polyBetween
  - GlobalTheory.T.exists_harmonicPolynomial_localDepth_between
  - GlobalTheory.ColDepth.nuLocOf_eq_nuP
  - GlobalTheory.T.columnPolynomial_localDepth_eq_placeDepth
  - GlobalTheory.ColumnGerm.exists_germ_on_copies
  - GlobalTheory.T.exists_integral_germ_on_copies_same_value
  - GlobalTheory.T.exists_integral_germ_on_columns_same_value
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reference exponents away from the host primes

This section proves that at a prime $q$ that is not a host prime, the reference exponent of a theta weight at $q$ is at most the oscillation of the depth at $q$. This is the link between the oscillation sums of [the previous section](/entry/sum-at-of-sizes/) and the reference bounds that [the chapter on canonical forms near the boundary](/entry/ref-core-of-size-sum-pt/) uses. The proof goes through a harmonic polynomial whose local depth lies in the window of the oscillation. Its local depth is the depth $\nu_q$ of the previous sections, by two approximation lemmas that move integral power series between columns and copies of the formal group.

We keep the notation of the first section. Let $T$ be a complete discrete valuation ring with an embedding of $F$, $y$ an integral point of the moduli space over $T$ and $\mathrm{Ch}$ an integral chart at $y$. Fix a function $c$ from factors to $\mathbb{N}$ and $n \in \mathbb{N}$.

**Definition 3.4.1 (Local depth and column polynomials).** For a polynomial $P$ in the variables of $n$ columns over the fraction field of $T$, and $k \in \mathbb{N}$, the *local depth* $\nu_{\mathrm{loc}}(P, k)$ is the infimum, over all integral power series $g$ in the chart coordinates of the $n$ columns, of the normalized valuation $v_T(\cdot)/v_T(p)$ of $\nabla_k g$ evaluated against $P$. Here $\nabla_k$ is the invariant differential operator of order $k$ of the chart. *Isotropic column data* for $c$ over $p$ are, for each factor $f$ with $c(f) \ne 0$, a block of $2\,\mathrm{rk}(f)$ of the $n$ columns, different for different $f$, and an integral matrix $B_f$ with $\mathrm{rk}(f)$ rows and $n$ columns that is isotropic on this block. The *column polynomial* $P_B$ of such data is the product over $f$ of the $c(f)$-th power of the determinant of the $\mathrm{rk}(f) \times \mathrm{rk}(f)$ minors given by $B_f$.

We do not unfold the operator $\nabla_k$ or the isotropy condition. The *copies* for $c$ are the formal groups of the chart, one for each pair $(f, b)$ with $c(f) \ne 0$ and $b < \mathrm{rk}(f)$. For a valued extension $C$, let $\exp_H$ be the exponential along the frames $u_f$ on the copies, and let $D_H$ be the product over $f$ with $c(f) \ne 0$ of the polynomials $D_{\mathrm{rk}(f), c(f)}$ of [the first section](/entry/formal-group-types/), in the variables of the copies of $f$. Then $\partial_{D_H}(h \circ \exp_H)$, for integral $h$ on the copies, is the quantity whose infimum is a sum of factor depths. The operator $\nabla_k$ also makes sense over $C$, and we write $\nabla_k^C g$ for its value on a power series $g$ in the $n$ columns over $C$.

**Lemma 3.4.2 (Germs on columns).** Let $y$ lie over a point of the flag model at $p$, $C$ a valued extension, and $B$ isotropic column data for $c$. For all $N, k \in \mathbb{N}$ and every integral power series $g$ in the $n$ columns over $C$, there is an integral power series $h$ on the copies with
$$v\bigl(\nabla_k^C g - \partial_{D_H}(h \circ \exp_H)\bigr) \ge N.$$

Lean: `GlobalTheory.T.exists_integral_germ_on_columns_same_value`

*Proof.* This is an approximation lemma on columns, applied to the given data; we did not open its proof. $\square$

**Lemma 3.4.3 (Germs on copies).** In the same setting, for all $N, k \in \mathbb{N}$ and every integral power series $h$ on the copies, there is an integral power series $g$ in the $n$ columns over $C$ with
$$v\bigl(\nabla_k^C g - \partial_{D_H}(h \circ \exp_H)\bigr) \ge N.$$

Lean: `GlobalTheory.ColumnGerm.exists_germ_on_copies` (also `GlobalTheory.T.exists_integral_germ_on_copies_same_value`, a second name).

*Proof.* We find $g$ with $\nabla_k^C g = \partial_{D_H}(h \circ \exp_H)$ exactly. Then the difference is $0$, of valuation $\infty \ge N$. The isotropic column data give an integral substitution $\psi$ from the columns to the copies, with zero constant terms, and an integral retraction $\rho$ the other way. The frame series of the copies has an integral inverse $U'$. Put $g = (h \cdot U'^k) \circ \rho$. This $g$ is integral, since products, powers and substitutions with zero constant terms keep integrality. A formula for $\nabla_k$ on frame series, applied through $\psi$ and $\rho$, gives the equality. The inputs to this formula are lemmas on additivity of the logarithm, linearity of the action in log coordinates, integral units, continuity of coefficients and limits of integral frames, which we know by their statements. $\square$

**Theorem 3.4.4 (Local depth of a column polynomial).** Let $y$ lie over a point $x$ of the flag model at $p$, $\mathrm{Ch}$ a chart at $y$, and $B$ isotropic column data for $c$. Then for every $k$
$$\nu_{\mathrm{loc}}(P_B, k) = \nu_p(y, c).$$

Lean: `GlobalTheory.ColDepth.nuLocOf_eq_nuP` (also `GlobalTheory.T.columnPolynomial_localDepth_eq_placeDepth`, a second name).

*Proof.* Since $y$ lies over $x$, a valued extension $C$ of $T$ exists. A first lemma, an input, says that the local depth over $T$ equals the infimum of $v(\nabla_k^C g)$ over integral $g$ over $C$. A second input says that the infimum of $v(\partial_{D_H}(h \circ \exp_H))$ over integral $h$ on the copies is $\sum_f \nu_f(y, c(f)) = \nu_p(y, c)$. It remains to show that the two infima over $C$ agree. We use a fact on valuations: if $v(a) < v(a - b)$, then $v(b) = v(a)$. Let $a_g = \nabla_k^C g$ and $b_h = \partial_{D_H}(h \circ \exp_H)$. Given $g$ with $v(a_g) < \infty$, take $N > v(a_g)$ and $h$ from the lemma on columns. Then $v(b_h) = v(a_g)$, so the infimum of $v(b_h)$ is at most that of $v(a_g)$. The lemma on copies gives the other inequality in the same way. $\square$

**Definition 3.4.5 (Polynomial windows).** Let $x$ be a point of the flag model at $p$ and $P$ a polynomial over $F$ in the variables of $n$ columns. $P$ is *between $A$ and $B$ at $x$* if for every algebraic integral point $y$ over $x$, every integral chart at $y$ and every $k$, the local depth of the image of $P$ lies in $[A, B]$.

**Theorem 3.4.6 (A harmonic polynomial in the window).** Let $x$ be a point of the flag model at $p$, $a$ a weight on factors that is antitone in $j$ for each $\tau$, and $n \in \mathbb{N}$ with $\sum_f 2\,\mathrm{rk}(f) \le n$. If $\nu_p(\cdot, \mathrm{gap}(a))$ is between $A$ and $B$ at $x$, then there is a harmonic polynomial $P_1$ of weight $a$ in $n$ columns over $F$ that is between $A$ and $B$ at $x$.

Lean: `GlobalTheory.RefSum.GlobalPoly.exists_polyBetween` (also `GlobalTheory.T.exists_harmonicPolynomial_localDepth_between`, a second name).

*Proof.* Choose an integer $N$ with
$$N > B + \sum_{q \mid N_c} \tfrac12\, \mathrm{vd}_H(q)\, D_F(a),$$
where $N_c$ is the conductor of the host, $\mathrm{vd}_H$ its local numbers and $D_F(a)$ the degree of the weight. A global lemma, an input, gives a harmonic polynomial $P_1$ of weight $a$ in $n$ columns, and for every $T$ over $x$ isotropic column data $B_T$ for $\mathrm{gap}(a)$ and a polynomial $R$ with integral coefficients, such that
$$P_1 = P_{B_T} + p^N R \quad \text{over } T.$$
Let $y$ be an algebraic integral point over $x$, $\mathrm{Ch}$ a chart and $k \in \mathbb{N}$. By the theorem on column polynomials, $\nu_{\mathrm{loc}}(P_{B_T}, k) = \nu_p(y, \mathrm{gap}(a))$, which lies in $[A, B]$. A bound for the chart of the host, and a lemma that the local depth does not change under a perturbation by $p^N R$ when $N$ exceeds the depth plus the conductor correction, give $\nu_{\mathrm{loc}}(P_1, k) = \nu_{\mathrm{loc}}(P_{B_T}, k)$. For the size of $N$ we use $v_T(q)/v_T(p) \le 1$ for each prime $q$ of the conductor, which holds since $v_T(q) \le v_T(p)$ when $v_T(p) > 0$. $\square$

Now let us return to the setting of [the previous chapter](/entry/ref-core-of-size-sum-pt/): a datum of the family with core tower $T$ that satisfies the laws, an error datum, a level $j$ in range, and the uniformizations $U_j$ at level $j$. For a weight $a$ and $n$ columns, $G = G(a, n)$ is the theta weight. The *reference exponent* of $G$ at $q$ with constant $c_0$ is
$$r_q(G) = \sup_{x, y, \varphi}\Bigl(\delta_G(y) - \frac{c_0\,\varphi}{v_T(q)}\Bigr),$$
over points $x$ of the flag model at $q$, algebraic integral points $y$ over $x$ and numbers $\varphi$ attached to $y$, where $\delta_G(y)$ is the depth of $G$ at $y$ for $U_j$. The *jet condition* with constant $c_0$ holds for a degree $D_F$ if for each host prime $g_k$
$$\begin{aligned}
&4 D_F + 4 \le g_k, \qquad 2 D_F \sqrt{2 f m} < g_k, \\
&\frac{\rho_0 (2fm)^3 \bigl(\tfrac14 r\, (2fm) + 2 D_F^2\bigr)}{g_k} \le c_0,
\end{aligned}$$
where $\rho_0$ is a constant of the family.

**Theorem 3.4.7 (Reference exponent away from the host primes).** Let $a$ be a weight in the domain for $n$ columns, with positive last entries, $\sum_f 2\,\mathrm{rk}(f) \le n$ and $2r \le n$. Assume the jet condition with constant $c_0$ for $D_F(a)$. Let $q$ be a prime other than the host primes $g_k$, and assume that the oscillation at $q$ is at most $b$ for $\mathrm{gap}(a)$ on the moduli space of level $j$. Then
$$r_q(G(a, n)) \le b.$$

Lean: `GlobalTheory.RefAway.refExp_le_of_oscLe` (also `GlobalTheory.T.baseLocusExponent_le_oscillation_nonTypePrime`, a second name).

*Proof.* Let $x$ be a point of the flag model at $q$, $y$ an algebraic integral point over $x$ and $\varphi$ attached to $y$. We must show $\delta_G(y) \le b + c_0 \varphi / v_T(q)$. The oscillation bound gives $A \in \mathbb{N}$ with $\nu_q(\cdot, \mathrm{gap}(a))$ between $A$ and $A + b$ at $x$. The theorem on harmonic polynomials gives $P_1$ of weight $a$ between $A$ and $A + b$ at $x$. Then we pass to a finite extension of $T$ with a uniformized chart and a scale. On it there is a short basis of the period lattice with balanced slope. The level has a half split: elements $\pi$, $\pi'$ with $\pi \bar\pi = g$ and $\pi' \bar\pi' = g'$ for the two host primes, and an element $\alpha$ with $\alpha \bar\alpha$ a unit at $q$; here we use $q \ne g_k$. The theta series built from $P_1$ and the short basis has least valuation at most the local depth of $P_1$ plus an error, and the jet condition bounds the error by $c_0 \varphi/v_T(q)$. So the least valuation is at most $A + b + c_0\varphi/v_T(q)$. On the other side, the valuations of the theta series are bounded below by $A$. Clearing denominators away from $q$ gives a cusp form of weight $G$ and an element $s$ with $v(s) = -A\, v_T(q)$. Comparing the two bounds gives the claim. $\square$

**Remark 3.4.8 (Formalization).** The lemma on germs on columns is a wrapper of an approximation lemma that is not in this chapter and whose proof we did not open ([ExistsIntegralGermOnColumnsSameValueStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIntegralGermOnColumnsSameValueStatement.lean#L12)). The lemma on germs on copies has a precision $N$, but its proof gives an exact equality, so $N$ is not used ([ExistsIntegralGermOnCopiesSameValue.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIntegralGermOnCopiesSameValue.lean#L97)); it also passes the star condition as `fun _ => rfl`. In the theorem on column polynomials the right side does not depend on $k$ ([ColumnPolynomialLocalDepthEqPlaceDepth.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnPolynomialLocalDepthEqPlaceDepth.lean#L60)). In the theorem on harmonic polynomials the family datum enters only through the CM field, the conductor and the local numbers of its host, and the host of the moduli space is a separate argument ([ExistsHarmonicPolynomialLocalDepthBetween.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHarmonicPolynomialLocalDepthBetween.lean#L62)). In the theorem on reference exponents the error datum is an unnamed argument that the proof uses, and the condition $2r \le n$ serves only to give $n \ge 1$ ([BaseLocusExponentLeOscillationNonTypePrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BaseLocusExponentLeOscillationNonTypePrime.lean#L125)). The two inputs of the proof on column polynomials, the global harmonic lemma, the perturbation lemma, the chart bound, and the steps of the proof on reference exponents (uniformized charts, short period bases, half splits, theta series bounds, clearing of denominators) are known to us by their statements. We have not unfolded harmonic polynomials, isotropy, the operator $\nabla_k$, the theta weight or the numbers $\varphi$.
