---
id: compare-off-own-run
title: The trace lattice lies in the theta lattice away from the own prime, at one run
kind: theorem
decl: GlobalTheory.CompareOff.compareOffOwn_run
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime
covers: 386
status: drafted
drafted_by: writer@claude
---
This theorem proves the inclusion of [the second name](/entry/trace-lattice-le-span-theta-series-away-from-own-prime/), which [the comparison along a family](/entry/compare-off-own-at-runs-alt/) uses at each point. It shows that each generator of the trace lattice is, up to a factor prime to $\lambda$, an integral multiple of one theta series in the theta base lattice.

## Statement

The statement is that of [the second name](/entry/trace-lattice-le-span-theta-series-away-from-own-prime/). Write $p = \ell_v$ for the own prime of the twisted place $v$, $L$ for the coefficient field, $T$ for the trace lattice and $\Theta$ for the theta base lattice `thetaBase` at $v$ with phase 1. Recall that $\Theta$ is the $\mathcal{O}_L$-span of the vectors $x$ such that, for a base kernel $(\omega, \varphi)$ at the place of $v$, some $h$ in the group `GfC` and some coefficient vector $w$ in the coefficient lattice, the form $\langle x, \cdot \rangle$ (`adForm`) equals the $\psi$-average over $U$ of the single theta series of $(\omega, \varphi)$ at $h$ and $w$. Then $T_\lambda \subseteq \Theta_\lambda$ for each prime $\lambda$ of $\mathcal{O}_L$ with $\lambda \nmid p$.

## Proof

Fix $\lambda \nmid p$. It is enough to show that each generator $S(f) = \sum_{u \in U} \psi(u)\, c(f(u))$ of $T$ lies in $\Theta_\lambda$.

1. `T.exists_orbit_family_adapted_lattice_split_support` gives an integer $s \notin \lambda$, an integral $a$ and a second family $f'$ with $s f = a f'$, and a lattice $\Lambda$ and $h$ adapted to $f'$. So $s\, S(f) = a\, g'$ with $g' = S(f')$.
2. `HarmInCoef.harm_mem_coefLat` gives a coefficient vector $y$ and an integer $s' \notin \lambda$ with $s' y$ in the coefficient lattice.
3. `OnCmp.exists_baseKernel` and `OnBaseKer.kerDat_of_isBaseKernel` give a base kernel $(\omega, \varphi)$ with its kernel data.
4. `T.trace_shortSeries_eq_mul_adelicSeries` gives the main identity: $\langle g', w \rangle = c \cdot (\text{a theta series of } \varphi')$ for all $w$, with a constant $c$ and $s'' c$ integral at $\lambda$ for some $s'' \notin \lambda$. This step uses almost all the hypotheses.
5. `T.freeLowerBlockVector_eq_translate_kernelDatum` writes $\varphi'$ as the translate of $\varphi$ by some $k$ in `GfC`, with a constant $c'$ and $p^m c'$ integral.
6. The form $\langle \cdot, \cdot \rangle$ is nondegenerate in the first variable. This comes from `TraceIncl.eq_of_low` and the uniformity of the places.
7. If $c = 0$, then $g' = 0$ by step 6, so $s\, S(f) = 0$. Otherwise put $e = p^m s' (c c')^{-1} g'$. Then $e \in \Theta$, with witnesses $(\omega, \varphi)$, $hk$ and $p^m s'$ times the vector of $y$. A short computation gives $p^{2m} s' s'' s \cdot S(f) = (a\, s'' c \cdot p^m c')\, e$, and the right-hand factor is integral. Since $p \notin \lambda$ (`natCast_not_mem`, which needs $p$ prime) and $s, s', s'' \notin \lambda$, we get $S(f) \in \Theta_\lambda$.

## In the Lean code

The theorem is in [TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean#L81). The helpers `mem_localization_iff`, `localization_le_of_le_localization'`, `natCast_not_mem`, `splitOffBad_of_mul` and `singleSeries_transl` are at lines 33 to 68 of the same file. `thetaBase` is in [ThetaSeriesTies.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ThetaSeriesTies.lean#L89), and `CompareOffOwn` in [TraceLatticeLeThetaLatticeAtPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/TraceLatticeLeThetaLatticeAtPlace.lean#L38).

We have not unfolded the statements of the lemmas in steps 1 to 5. The hypotheses on the runs, the pins, the determinant of $U$ and $\psi$ go only to `T.trace_shortSeries_eq_mul_adelicSeries`. The primality of $p$ comes from the field condition `FieldOK0`, which makes $p$ one of the two primes of the host.
