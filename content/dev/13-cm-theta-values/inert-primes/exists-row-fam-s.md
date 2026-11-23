---
id: exists-row-fam-s
title: A row family from the Frobenius orbits at an inert prime
kind: theorem
decl: UpperTheory.OrbitFamilyRestriction.exists_rowFamS
module: Development.AutomorphicArithmetic.OrbitLabellings.ExistsPkgCsOfDegreeBoundAtInertPrimes
covers: 1998
status: drafted
drafted_by: writer@claude
---
This private lemma labels the embeddings of a CM field $E$ by Frobenius orbits at an inert prime $l$ of odd order. It then gets a family of row data with a lower bound on $\nu$ by blocks. Its one user is [`exists_pkgCs_of_degree_bound_at_inert_primes`](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/), which turns the result into packages. Most of the real content is below it, in [`labelSetGeo_of_even_of_rankOK_of_not_dvd_discr`](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/). The work done here is the labelling and its arithmetic.

## Statement

Use the setting and the predicate `AllPts` of [the entry above](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/). Let $P$ = `parOf N j l`. It has the places $\mathrm{Bool} \times A$ of $N$, the order $h$ = `ordP l`, and the shift `pos`. For an embedding $\tau$ let $g_\tau = \mathrm{gap}(\mathrm{mult}\,\tau, a(\tau,\cdot))$, where $\mathrm{gap}(r,a)(k) = a(k-1) - a(k)$ for $1 \le k \le r$, with $a(r) = 0$ in that formula, and $0$ for other $k$.

**Theorem.** Assume `UpFSt p` for all primes $p$. In the setting of `AllPts`, let $l$ be inert with $h$ odd. Then there are a set $Z$ of places, a map $\tau \colon Z \times \mathbb{Z}/2h \to (E \to \mathbb{C})$ and a row family $R$ (`RowFamS`) with these properties:

1. $Z$ is a set of representatives for the shift (`IsReps`);
2. $\tau$ is a bijection onto the embeddings;
3. $\tau(o,s)$ is in $\Psi$ (that is, $\tau(\mathrm{rt}) = \mathrm{rt}_0$, where the host fixes $\mathrm{rt} \in O_E$ and $\mathrm{rt}_0 \in \mathbb{C}$ with square $-d$) if and only if $s$ is even;
4. for even $s$, $\tau(o,s) = p_l(\mathrm{pos}(o, s \bmod h))$;
5. the rank `rkF 0 s` of the row data at $o$ is the multiplicity of $D$ at $\tau(o,s)$;
6. `ValBlocksS` holds for the shift $h$ in $\mathbb{Z}/2h$, the rows of $R$, $n_W$, the weights $g_{\tau(o,s)}$ and $\nu$.

## Proof

1. `exists_closed_field_over_place` gives an algebraically closed field $C$ with a valuation over the prime, and turns the bound on $\nu$ into a bound by `nuLocC` over $C$. As $l$ is not small, $l \ne 2$.
2. `exists_baseChange` gives a chart $Y$ over $C$ at level $M$.
3. `exists_reps` gives $Z$. `exists_orbit_labelling_at_inert_prime_of_odd_order` gives a labelling with shift $h$ in $\mathbb{Z}/2h$, ranks $n = k-1$, $j$ and $m-j$, and $l \nmid \mathrm{disc}(E)$. Its $\tau(o,s)$ is $p_l(\mathrm{pos}(o,s))$ for even $s$ and its complex conjugate for odd $s$.
4. Then the proof checks: point 3; the multiplicity is $p$ at even $s$ and $q$ at odd $s$; `RankOK` from the signature $\sigma_j = (k+j-1, m-j)$; $m - j < k - 1$; and `WtTieS` from `gap_sums`.
5. It calls `labelSetGeo_of_even_of_rankOK_of_not_dvd_discr` with the even number $2h$. This gives the rows, the flags and `ValBlocksS`.
6. Injectivity of $\tau$ comes from the injectivity of $p_l$ and of complex conjugation. If $s \equiv s' \bmod h$ and $s, s'$ have the same parity in $[0, 2h)$, then $s = s'$, because $h$ is odd.

## In the Lean code

The lemma is in [ExistsPkgCsOfDegreeBoundAtInertPrimes.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/ExistsPkgCsOfDegreeBoundAtInertPrimes.lean#L45). `RowFamS`, `ValBlocksS` and `WtTieS` are in [RowDefs.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/RowDefs.lean#L24). The labelling is in [ExistsOrbitLabellingAtInertPrimeOfOddOrder.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/ExistsOrbitLabellingAtInertPrimeOfOddOrder.lean#L12). We have not unfolded `RowData` beyond its fields, `nuLocC` or the chart types.

`UpFSt` is used only to pass to the lemma below. The hypotheses $l \ne q_N$, $l \ne d_N$ and ($l$ `Inert` $\Rightarrow 5 \le l$) from `AllPts` are introduced on line 55 and not used.
