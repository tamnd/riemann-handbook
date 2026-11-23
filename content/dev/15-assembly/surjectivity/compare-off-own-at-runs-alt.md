---
id: compare-off-own-at-runs-alt
title: The trace lattice lies in the theta lattice away from the own prime, along a family
kind: theorem
decl: GlobalTheory.BigOn.compareOffOwn_atRuns_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CompareOffOwnAtRuns
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem says that, at the points of a family and at each twisted place, a trace lattice of cusp forms lies in the theta base lattice after localization at each prime that is not above the own prime of the place. It is an input of the rank statement at twisted places. [The surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/) uses it directly, and [the last step of that proof](/entry/onto-x-of-twist-shares-exp-alt/) uses it through the second name `bigOn_comparison_at_twisted_places`. The pointwise work is in [`traceLattice_le_span_thetaSeries_awayFromOwnPrime`](/entry/trace-lattice-le-span-theta-series-away-from-own-prime/).

## Statement

The theorem has no hypothesis. For each closed family hypothesis and each family $F_m$ in it, eventually at points $p$ of $F_m$ with `More p`, the following holds for each pair of runs $r$ at $p$ that is good (`RunsOk`) and pinned at the own primes (`OwnPin`). Let $v$ be a twisted place of $p$, $j$ a level, $\ell_v$ = `ownAt v` the own prime of $v$, $U = P_0$ and $\psi = \psi_0^{-1}$ the group and character of the face of $p$. Let

$$T_j = \operatorname{span}_{\mathcal{O}_L} \Bigl\{ \sum_{u \in U} \psi(u)\, c(f(u)) \Bigr\},$$

where $f$ runs over the orbit families of cusp forms of index $j + 1$ and weight $\kappa_j$ and $c$ is the map `cuspTo` into $L^{n_W(j)}$. Then for each prime $\lambda$ of $\mathcal{O}_L$ that does not lie over $\ell_v$, the localization of $T_j$ at $\lambda$ lies in the localization at $\lambda$ of the theta base lattice at $v$ (`thetaBase`, phase 1). We have not unfolded `thetaBase`, the runs or the orbit families.

## Proof

1. `runNumericalConditions_hold_along_family 0` gives, eventually along the family, five numerical bounds on the point. The proof uses only the last one, $8 f r + 4 \le n_V$.
2. `links2_of_single_index_twisted` gives the links at $p$: the core data, the uniformity `LUnif`, the pins and the phases.
3. `classSumsSpan_core` shows that the class sums span, from the bound of step 1 and the core of step 2.
4. The values of $\delta$ at the place of $v$ lie in the image of $L$ (from `FO_le`).
5. `traceLattice_le_span_thetaSeries_awayFromOwnPrime` gives the inclusion from all of the above and from the fields of the runs: run, level and action pins. The determinant condition on $U$ comes from `det_eq_one_of_mem_base`.

## In the Lean code

The theorem is in [CompareOffOwnAtRuns.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CompareOffOwnAtRuns.lean#L14). `CompareOffOwn`, `CompareAt` and `traceLat` are in [TraceLatticeLeThetaLatticeAtPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/TraceLatticeLeThetaLatticeAtPlace.lean#L28). The second name is in [CompareOffOwnAtRunsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CompareOffOwnAtRunsStatement.lean#L13).

The condition "not above $\ell_v$" is `plc λ ≠ p` in Lean, where `plc λ` is the characteristic of the residue field $\mathcal{O}_L/\lambda$ ([StatementT.lean](lean:Formalism/MirabolicMackeyTheory/StatementT.lean#L16)). A parallel copy, `GlobalTheory.BigOn.compareOffOwn_atRuns`, is in [ComparisonOffTypePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComparisonOffTypePlaces.lean#L14).
