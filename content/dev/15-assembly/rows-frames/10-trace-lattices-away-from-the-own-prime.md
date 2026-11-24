---
title: Trace lattices away from the own prime
decls:
  - GlobalTheory.OrbitAdapt.shortRule_change_mat
  - GlobalTheory.T.exists_orbit_family_adapted_lattice_split_support
  - GlobalTheory.OrbitAdapt.exists_adapted
  - GlobalTheory.T.shortSeries_trace_term_at_evaluationVector
  - GlobalTheory.OneTermEval.series_term_at_eval
  - GlobalTheory.OneMapExact.one_term
  - GlobalTheory.T.trace_shortSeries_eq_mul_adelicSeries
  - GlobalTheory.OneMapExact.trace_short_eq
  - GlobalTheory.T.traceLattice_le_span_thetaSeries_awayFromOwnPrime
  - GlobalTheory.CompareOff.compareOffOwn_run
  - GlobalTheory.T.exists_cuspForm_independent_translates
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Trace lattices away from the own prime

This section proves that the trace lattice of a run at a twisted place $v$ lies in the lattice spanned by theta series, after localization at every prime $\lambda$ of the coefficient field that does not lie over the own prime $p$ of $v$. It is used by [the comparison away from the own prime](/entry/compare-off-own-at-runs-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The proof writes each trace of a cusp form as a multiple of one theta series of a translated kernel, and controls the denominators of the multiple. At the end we record the existence of a cusp form with independent translates, used by [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/).

We use [theta series of lattices](/learn/theta-functions-cm/#theta-series-of-lattices) and [unitary groups](/learn/groups/#unitary-groups) of Volume 1.

Fix a point of the construction, a full run $T$ with its laws, an index $i$ and a twisted place $v$ with own prime $p$. Let $L$ be the coefficient field, $U$ a subgroup of the level group with $\det e_G(u) = 1$ at each place of the level, and $\psi : U \to L^\times$ a character. The run gives a map $f \mapsto \mathrm{cusp}(f)$ from cusp forms of the run to vectors in $L^{n}$. A family $f = (f_u)_{u \in U}$ of cusp forms is an *orbit family* if $f_u$ is obtained from $f_1$ by the level action of $u$, inside the forms of the run with the bad number $\mathrm{badN}$ and the given weight and $\delta$ datum. Its *trace* is
$$S(f) = \sum_{u \in U} \psi(u)\, \mathrm{cusp}(f_u).$$
The *trace lattice* $T_{\mathrm{tr}}$ is the $\mathcal{O}_L$-span of the traces of all orbit families. The *theta lattice* $\Theta$ is the $\mathcal{O}_L$-span of the vectors $x$ such that, for a base kernel $(\omega, \varphi)$ at the places over $p$ above $v$, the form of $x$ against coefficient vectors is the $\psi$-average over $U$ of the single theta series of $(\omega, \varphi)$.

### Adapted families

A lattice $\Lambda$ with a short rule is a lattice in the hermitian space with a set of short vectors that the theta series reads. A matrix $g$ acts on lattices and on harmonic polynomials by the push $P \mapsto g P$.

**Lemma 7.10.1 (Change of matrix).** Let $g$ be unitary with $g \equiv 1$ modulo an ideal $\mathfrak{b}$, let the level $M$ divide $\mathfrak{b}$, let the lattices be unimodular with trivial level, and let $P$ be harmonic. Then the pushed polynomial $P' = g P$ is harmonic, and there is a root of unity $\zeta \neq 0$ such that whenever $\Lambda$ has the short rule for $f$, the lattice $g \Lambda$ has the short rule for $\zeta f$.

Lean: `GlobalTheory.OrbitAdapt.shortRule_change_mat`.

*Proof.* Since $g$ is unitary, it preserves the hermitian form, so it maps short vectors of $\Lambda$ to short vectors of $g \Lambda$ and keeps $P$ harmonic. The congruence $g \equiv 1$ modulo $\mathfrak{b}$ with $M \mid \mathfrak{b}$ means that $g$ acts on the level characters through a root of unity $\zeta$. So the short rule moves from $f$ to $\zeta f$. $\square$

**Theorem 7.10.2 (Adapted orbit families).** Let $f$ be an orbit family and $\lambda$ a prime of $\mathcal{O}_L$. Then there are $s \in \mathcal{O}_L$ with $s \notin \lambda$, an integral $a$, an orbit family $f'$ with $s f = a f'$, a lattice $\Lambda$ with a short rule for $f'$ that is integral at $\lambda$, unimodular and of trivial level, a level $N$, a base point $x_0$ and a harmonic polynomial $P$ with support split off the bad primes.

Lean: `GlobalTheory.T.exists_orbit_family_adapted_lattice_split_support` (also `GlobalTheory.OrbitAdapt.exists_adapted`).

*Proof.* If the bad number is $0$, a direct choice works. Otherwise, an integral step gives a lattice for $f$, and a step that splits off the bad primes gives a matrix $g$ that moves the support away from them. The bad part divides the level, so the lemma applies, and it gives the short rule for $\zeta f$. Take $s = 1$, $f' = \zeta f$ and $a = \zeta^{m-1}$, where $m$ is the order of $\zeta$. Then $a f' = \zeta^m f = f$. $\square$

### One term and the trace

**Lemma 7.10.3 (One term at an evaluation vector).** For a base kernel $(\omega, \varphi)$, an adapted family $f'$, a coefficient vector $y$ and each $u \in U$, there are a vector $y_0$ with $\mathrm{rank}(y_0 P) = \mathrm{rank}\, W$ and a constant $c$ that is $\lambda$-integral up to some $s \notin \lambda$, such that the adelic form of $\mathrm{cusp}(f'_u)$ at $w$ equals $c$ times the action of $e_G(u^{-1})$ on the single theta series of the kernel at $y_0$.

Lean: `GlobalTheory.T.shortSeries_trace_term_at_evaluationVector` (also `GlobalTheory.OneTermEval.series_term_at_eval`).

*Proof.* The short series of the base datum is a multiple of the adelic form, by the theta correspondence for the run. Translating by $u$ moves the series by $e_G(u^{-1})$. The character of $W$ at $u^{-1}$ is $1$, since $\det e_G(u) = 1$. $\square$

**Lemma 7.10.4 (One term).** Under the hypotheses of the last lemma, each term of the trace is $c$ times the $u$-translate of one series, with the same $c$ for all $u$.

Lean: `GlobalTheory.OneMapExact.one_term`.

*Proof.* The lowest type of the evaluation vector is the same for all $u$, and the support of $P$ splits off the bad primes. So the constant of the last lemma does not depend on $u$. $\square$

**Theorem 7.10.5 (Trace and adelic series).** Let the run have its pins, phase tie, class sums and pins at $v$, as in the comparison. Then for each adapted family $f'$ with base kernel $(\omega, \varphi)$ there are $y_0$ and $c$ as above such that, for all coefficient vectors $w$,
$$\big\langle S(f'), w \big\rangle = c \cdot \Big\langle \sum_{u \in U} \psi(u)\, e_G(u^{-1}) \vartheta_{\omega, \varphi}(y_0), w \Big\rangle.$$

Lean: `GlobalTheory.T.trace_shortSeries_eq_mul_adelicSeries` (also `GlobalTheory.OneMapExact.trace_short_eq`).

*Proof.* Sum the one term lemma over $u \in U$ with the weights $\psi(u)$. The form is additive in the first variable. $\square$

### The comparison

**Theorem 7.10.6 (Trace lattice away from the own prime).** Under the hypotheses of the comparison at the run, for each prime $\lambda$ of $\mathcal{O}_L$ that does not lie over $p$,
$$(T_{\mathrm{tr}})_\lambda \subseteq \Theta_\lambda.$$

Lean: `GlobalTheory.T.traceLattice_le_span_thetaSeries_awayFromOwnPrime` (also `GlobalTheory.CompareOff.compareOffOwn_run`).

*Proof.* It is enough to show $S(f) \in \Theta_\lambda$ for each orbit family $f$.

1. The theorem on adapted families gives $s \notin \lambda$, $a$ and $f'$ with $s f = a f'$, so $s S(f) = a\, g'$ with $g' = S(f')$.
2. A coefficient vector $y$ with $s' y$ in the coefficient lattice for some $s' \notin \lambda$ exists by the harmonic coefficients.
3. Take a base kernel $(\omega, \varphi)$ at $v$ with its kernel data.
4. The theorem on the trace gives $\langle g', w \rangle = c \langle \vartheta, w \rangle$ for all $w$, with $s'' c$ integral for some $s'' \notin \lambda$.
5. The kernel $\varphi'$ of $y_0$ is the translate of $\varphi$ by some $k$, up to a constant $c'$ with $p^m c'$ integral.
6. The form is nondegenerate in the first variable.
7. If $c = 0$, then $g' = 0$ by step 6, so $S(f) = 0$ after multiplying by $s$. Otherwise put $e = p^m s' (c c')^{-1} g'$. Then $e \in \Theta$, with the kernel $(\omega, \varphi)$ translated by $k$ and the vector $p^m s' y$, and
$$p^{2m} s' s'' s \cdot S(f) = \big(a\, s'' c \cdot p^m c'\big)\, e.$$
The factor on the right is integral. Since $p$ is prime and $\lambda$ does not lie over $p$, $p \notin \lambda$. With $s, s', s'' \notin \lambda$ this gives $S(f) \in \Theta_\lambda$. $\square$

### Independent translates

Let $E$ be a CM field. A *two level datum* of rank $r$ over $E$ is a finite group $U$ acting on a finite set $C$, with a domain, a set of short sums $SS(\cdot)$ of cusp forms, and a determinant $\det[\ldots](u_0, c, x)$ of the translates of $u_0$ at the point $x$ for each $c \in C$. It satisfies the *level hypothesis* if there is a prime $g$ that splits completely in $E$ with $3r < g$, such that the datum is unipotent over $g$.

**Theorem 7.10.7 (Cusp forms with independent translates).** Let $E$ be CM, let a two level datum of rank $r$ satisfy the level hypothesis, and let $s$ be even with
$$s \geq 2r + 50 r^2 \dim X + 1.$$
Then there is a cusp form $u_0$ among the short sums of weight $s$ such that for each $c \in C$ some point $x$ of the domain has a nonzero determinant of translates.

Lean: `GlobalTheory.T.exists_cuspForm_independent_translates`.

*Proof.* This is [the independent translates theorem](/entry/independent-translates/), proved in the second part of this chapter. $\square$

**Remark 7.10.8 (Formalization).** The trace lattice and the comparison are `traceLat` and `CompareOffOwn` in TraceLatticeLeThetaLatticeAtPlace.lean, and the theta lattice is `thetaBase` in [ThetaSeriesTies.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ThetaSeriesTies.lean#L89). The comparison is at line 81 of [TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean#L81), under `maxHeartbeats 1000000`, with helpers at lines 33 to 68; step 2 is `HarmInCoef.harm_mem_coefLat`, step 5 is `T.freeLowerBlockVector_eq_translate_kernelDatum` and step 6 uses `TraceIncl.eq_of_low`. We read their statements, not their proofs, and the sketches of the lemma on matrices and of the one term lemmas follow their statements. The primality of $p$ comes from the field condition at the own prime. The theorem on adapted families is at line 130 of [ExistsOrbitFamilyAdaptedLatticeSplitSupport.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsOrbitFamilyAdaptedLatticeSplitSupport.lean#L130), with the steps at lines 25, 81 and 117. It always returns $s = 1$, so the freedom $s \notin \lambda$ is not used, and one of its hypotheses is not used. The lemma on matrices is at line 16 of [ShortRuleChangeMat.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShortRuleChangeMat.lean#L16). The one term lemma is at line 83 and the trace theorem at line 92 of TraceShortSeriesEqMulAdelicSeries.lean. The last theorem is a wrapper of `TranslatesDet.independentTranslates` at line 187 of ExistsCuspFormIndependentTranslates.lean, proved by `first | exact ...`, with `maxHeartbeats 1000000`; the property `IndependentTranslates` is at line 99 of [TwoLevelLogarithm.lean](lean:Development/AbelianVarietyTheory/BlockTheory/PoincareCuspForms/TwoLevelLogarithm.lean#L99).
