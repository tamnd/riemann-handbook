---
title: Coefficient bounds and Galois conjugation
decls:
  - GlobalTheory.T.thetaSeries_rationality_and_coefficientBound
  - GlobalTheory.Unframe.rat_and_xiBdd
  - GlobalTheory.T.universalSeriesCoeff_boundedInSup_of_twistSeriesSideData
  - GlobalTheory.XiBound.main
  - GlobalTheory.XiIntComb.xi_int_comb
  - GlobalTheory.T.conjugate_thetaSeries_flatDatum_rootOfUnity
  - GlobalTheory.ConjTwist.FlatSeries.conj_flat_series
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coefficient bounds and Galois conjugation

Sections 1 to 3 give rationality and integrality of single theta series. This section turns them into statements about the forms that the theta series define in a module of Hecke eigenforms with a fixed lattice. There are two results. The first says that the rows of theta series are rational after a normalizing scalar, and that the universal coefficients of the twisted series lie in the integral lattice after a power of $l$ that does not depend on the twist. The second says how an automorphism $\tau$ of $\mathbb{C}$ acts on a theta series of a flat datum: it sends the series to the series of the conjugate datum, up to a root of unity that does not depend on the datum. The first result gives the rational rows of the local series in the theta pair lifts of Volume 7. The second result is used to write the series of a flat vector as a sum of conjugate series.

### Readings, rows and the integral lattice

Fix a datum, a real side $X$ for it (the Weil representations, the models of the Shimura varieties and the frames) and a series side $Y$ over $X$. The series side fixes, for each twist index $i$, a discrete valuation ring $O_i$ with fraction field $K_i$ and a prime element $l_i$ above a prime number. For each $i$, each index $j$ and each sign $b$, it fixes a $K_i$-vector space $\mathcal{F}_{ij b}$ of forms, an $O_i$-lattice $B_{ijb} \subset \mathcal{F}_{ijb}$ (the *integral lattice*), and a $\mathbb{C}$-semilinear map $\mathrm{rd}_{ijb}$ from $\mathcal{F}_{ijb}$ to functions on the adelic group of $\mathrm{U}(W_j)$ (the *reading*). The reading is *faithful*: it is injective, and if a nonzero reading $\mathrm{rd}(x)$ and the reading $\mathrm{rd}(x')$ satisfy $\mathrm{rd}(x') = \nu\,\mathrm{rd}(x)$, then $\nu$ comes from $K_i$.

A *datum* for $(i, j, b)$ is a triple $(s, h, P)$: an element $s$ of the finite adelic group of $V$, a point $h$, and a harmonic polynomial $P$, with conditions of splitting, support and finiteness. For a finite set $Q$ of places of $E$, an integer $M$ and a value $a$, the series side defines the *universal coefficient* $\xi_{ijb}(Q, M, h, P, a)$, the twisted theta series of the datum, read as a function.

**Definition 3.4.1 (Rational row).** The row $(i, j, b)$ is *rational* if there is a normalizing scalar $\nu$ for the row such that the reading of the row scaled by $\nu$ is rational: it is the reading of a vector of $\mathcal{F}_{ijb}$ for each theta series of the row.

**Definition 3.4.2 (Bounded coefficients).** The series side has *bounded coefficients* if for every $i$ at a nonzero index place, every $(j, b)$ and every datum $(s, h, P)$, there is $c \in \mathbb{N}$ such that for every $Q$ in the range of $i$ whose places are prime to the norm of $s$, every $M$, every $a$ and every $x \in \mathcal{F}_{ijb}$ with $\mathrm{rd}(x) = \xi(Q, M, h, P, a)$, we have $l_i^{c}\,x \in B_{ijb}$.

The order of the quantifiers is the point: $c$ is chosen before $Q$, $M$ and $a$. These are the parameters of the twist.

### Rationality and bounded coefficients

**Proposition 3.4.3 (Integral combinations).** Assume global Artin reciprocity, the rationality of twisted theta series in the form of Section 1, and integral theta series. Let the real side satisfy the field condition and be pinned at the frames. Let $i$ be at a nonzero index place, and let $(s, h, P)$ be a datum for $(i, j, b)$. Then there are $u \in \mathbb{C}$ with $u \neq 0$ and $c \in \mathbb{N}$ such that for every admissible $Q$, every $M$ and every $a$ there are $o_1, \dots, o_n \in O_i$ and vectors $m_1, \dots, m_n$ of the integral model lattice with
$$l_i^{c}\,u\;\xi_{ijb}(Q, M, h, P, a) = \sum_{k} e(o_k)\,\mathrm{ev}(m_k) .$$
Here $e : O_i \to \mathbb{C}$ is the embedding of the series side and $\mathrm{ev}$ is the evaluation of model vectors at the base vacuum.

Lean: `GlobalTheory.XiIntComb.xi_int_comb`

*Proof.* The development proves, from the three hypotheses, that there are $u \neq 0$ and, for each harmonic polynomial $P'$ in the value space of the row, a constant $c$ that gives the conclusion for $P'$; call such a $P'$ *good*. The set of good polynomials contains $0$ and is closed under sums and under multiplication by $e(o)$ for $o \in O_i$. Every function in the coefficient span of the lattice of $h$ is the harmonic function of a good polynomial in the value space: this follows by induction on the span, since the generators are reached by harmonic polynomials with coefficients in the small field. The polynomial $P$ of the datum lies in the value space, and its harmonic function lies in the coefficient span. A harmonic polynomial whose function is zero is zero, because the weight is dominant and the signature fits into $W_j$. So $P$ equals the good polynomial with the same function, and its constant $c$ gives the claim. $\square$

**Theorem 3.4.4 (Bounded coefficients).** Under the hypotheses of the proposition on integral combinations, the series side has bounded coefficients.

Lean: `GlobalTheory.XiBound.main` (also `GlobalTheory.T.universalSeriesCoeff_boundedInSup_of_twistSeriesSideData`, a second name).

*Proof.* Fix $i$, $(j, b)$ and the datum, and take $u$ and $c$ from [the integral combinations](/entry/xi-int-comb/). Let $\nu \neq 0$ be the normalizing scalar of the row, and put $\lambda = \nu^{-1}\,l_i^{c}\,u$. For $Q$, $M$, $a$ and $x$ with $\mathrm{rd}(x) = \xi(Q, M, h, P, a)$, the vector $y = \sum_k o_k \otimes m_k$ lies in $B_{ijb}$, and its reading is $\lambda\,\mathrm{rd}(x)$.

If $\lambda = e(\mu)$ for some $\mu \in K_i$, then $\mu \neq 0$, and by injectivity $y = \mu x$. Choose $N$ and $o \in O_i$ with $l_i^{N} = o\,\mu$; this is possible since $O_i$ is a discrete valuation ring with prime $l_i$. Then $l_i^{N} x = o\,y \in B_{ijb}$, so $c' = N$ works.

If $\lambda$ does not come from $K_i$, then $\mathrm{rd}(x) = 0$ for every such $x$: otherwise $\mathrm{rd}(y) = \lambda\,\mathrm{rd}(x)$ and faithfulness would put $\lambda$ in the image of $K_i$. So $x = 0$, and $c' = 0$ works. $\square$

**Theorem 3.4.5 (Rationality and coefficient bound).** Assume that cusp forms decay rapidly, global Artin reciprocity, rationality of twisted theta series and integral theta series. Let the real side $X$ satisfy the field condition. Then every row at a nonzero index place is rational, and the series side has bounded coefficients.

Lean: `GlobalTheory.Unframe.rat_and_xiBdd` (also `GlobalTheory.T.thetaSeries_rationality_and_coefficientBound`, a second name).

*Proof.* The rapid decay of cusp forms lets the development replace $X$ and $Y$ by a real side $X'$ and a series side $Y'$ that are pinned at the frames, with the same field condition. Rationality of a row of $Y'$ implies rationality of the same row of $Y$, and bounded coefficients for $Y'$ imply bounded coefficients for $Y$. On $X'$, the development proves the rationality of the rows from Artin reciprocity and rationality of twisted series, and [the bounded coefficients theorem](/entry/xi-bound-main/) gives the bound. $\square$

### Conjugation of theta series

Let $\tau$ be a field automorphism of $\mathbb{C}$. For a family of characters $t$, write $\xi_t$ for its Hecke character and $Q_t$ for its set of places. Two families $t$ and $t'$ are *$\tau$-conjugate* if $Q_{t'} = Q_t$ and $\xi_{t'} = \tau \circ \xi_t$. The automorphism $\tau$ *fixes the base* if it fixes the coefficient field, the host embeddings, the curve of the datum, the split values $\mu_0\,\eta^{-1}\sqrt{N\mathfrak{P}}$, and the character $\chi$ of the datum. A Schwartz function is *flat* if it is a theta function at the finite places for the flat lattice.

**Definition 3.4.6 (Conjugate functions).** Let $O$ be a coefficient ring with a reading $\mathrm{rd}$, $\tau$ an automorphism of $\mathbb{C}$ and $\zeta \in \mathbb{C}$. Two functions $\Phi$ and $\Phi'$ are *$\zeta$-conjugate under $\tau$* if $\Phi$ has an expansion $\sum_k a_k\,\mathrm{rd}(f_k)$, and for every such expansion of $\Phi$, the function $\Phi'$ equals $\sum_k \zeta\,\tau(a_k)\,\mathrm{rd}(f_k)$.

**Theorem 3.4.7 (Conjugation of flat theta series).** Assume the chart independence law of the datum in its second form. Let the datum satisfy $8 f r + 4 \le \dim V$, the Hecke laws, the finiteness of the set of twist places, the tie between the Fock model and the Weil representation, and the extension and guard conditions at all indices; let $u$ be the lowest weight vectors equal to the vacuum, and let $\tau$ fix the base. Then there is a root of unity $\zeta_0$ with the following property. For all $\tau$-conjugate families $t$ and $t'$ and all flat functions $f$ and $f'$, there is a unit $s$ of the finite adeles of $E$ such that for every $h$ in the finite adelic group with trivial archimedean part and all conjugate vectors $x$ and $x'$, the functions
$$\varphi\,\theta(t, f, u, h, x) \quad \text{and} \quad \varphi\,\theta(t', f', u, h, x')$$
are $\zeta_0\,\xi_{t'}(s)$-conjugate under $\tau$. Here $\varphi$ is the phase of the datum.

Lean: `GlobalTheory.ConjTwist.FlatSeries.conj_flat_series` (also `GlobalTheory.T.conjugate_thetaSeries_flatDatum_rootOfUnity`, a second name).

*Proof.* The development proves the same statement for the twisted theta series of conjugate families, with a root of unity $\zeta_0$ and a unit $s_1$. A flat function is a scalar multiple of the twisted datum at a translated point: the development gives $z$ and scalars $C$ and $C'$ with $C' = \eta\,\tau(C)$, where $\eta$ is a value of $\xi_{t'}$, such that the flat series at $h$ is $C$ times the twisted series at $h z$, and the same for $t'$ with $C'$. Scaling preserves conjugacy: if $\Phi$ and $\Phi'$ are $\zeta$-conjugate, then $C\Phi$ and $\eta\,\tau(C)\,\Phi'$ are $\zeta\eta$-conjugate. The case $C = 0$ is treated apart; there both sides are $0$. Combine the two steps and put $s = s_1 s_2$, where $\xi_{t'}(s_2) = \eta$. $\square$

The root of unity $\zeta_0$ is chosen before the families and the flat functions. Only the unit $s$ depends on them.

**Remark 3.4.8 (Formalization).** The integral combination is at [XiIntComb.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/XiIntComb.lean#L78); it rests on `T.thetaSeries_integral_core_supLattice_combination`, which we did not open. The bound is `XiBound.main` ([UniversalSeriesCoeffBoundedInSupOfTwistSeriesSid.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UniversalSeriesCoeffBoundedInSupOfTwistSeriesSid.lean#L40)); it uses `exists_pow_mul_mem`, and its second branch returns $c = 0$ after it shows that $x = 0$. The property of bounded coefficients is `XiBdd` and the field condition is `FieldOk` ([UnivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnivChar.lean#L126)); a rational row is `RatRow` ([ExistsIsScalar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsIsScalar.lean#L139)). The pinned replacement is `Unframe.exists_framed` ([ThetaSeriesRationalityAndCoefficientBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaSeriesRationalityAndCoefficientBound.lean#L36)), the only place where `CuspRapidDecay` enters; the bound itself takes the pinning as a hypothesis. The conjugation theorem is at [ConjugateThetaSeriesFlatDatumRootOfUnity.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ConjugateThetaSeriesFlatDatumRootOfUnity.lean#L83), with `maxHeartbeats` 2000000. Its conjugacy predicate is `ConjFun` in [ConjTupRefl.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ConjTupRefl.lean#L96), with `ConjTup` and `FixBase` (line 80) in the same file. A second, different `ConjFun` is defined in [CentralInvolutionRing.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/CentralInvolutionRing.lean#L95), next to `IsFlatVec` (line 47). The inputs `T.conjugate_tuples_twisted_thetaSeries_conjugate` and `T.heckeChoice_flatScalar_conj_twist` were not opened. We have not unfolded `ChartIndepSt2`, `Hk3.Core`, `IoExt`, `QGuard`, `OMPins` or `PhaseTie`.
