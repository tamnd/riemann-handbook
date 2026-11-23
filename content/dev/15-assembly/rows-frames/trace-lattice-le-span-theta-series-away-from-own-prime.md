---
id: trace-lattice-le-span-theta-series-away-from-own-prime
title: The trace lattice lies in the theta lattice away from the own prime (second name)
kind: theorem
decl: GlobalTheory.T.traceLattice_le_span_thetaSeries_awayFromOwnPrime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TraceLatticeLeSpanThetaSeriesAwayFromOwnPrimeStatement
covers: 387
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is word for word the statement of [the comparison at one run](/entry/compare-off-own-run/), and its proof only calls that theorem. It is used in step 5 of the proof of [the comparison along a family](/entry/compare-off-own-at-runs-alt/), which gives it the hypotheses that it needs from the links, the pins and the runs at a point.

## Statement

Fix a point, a twisted place $v$ with own prime $\ell_v$, a subgroup $U$ of the face group with $\det e_G(u) = 1$ on $U$, and a character $\psi$ of $U$. Assume the hypotheses of [the comparison at one run](/entry/compare-off-own-run/). Then for each prime $\lambda$ of $\mathcal{O}_L$ not above $\ell_v$, the localization at $\lambda$ of the trace lattice $T$ (the $\mathcal{O}_L$-span of the sums $\sum_{u \in U} \psi(u)\, c(f(u))$) lies in the localization at $\lambda$ of the theta base lattice at $v$, with phase 1. In Lean this is `CompareOffOwn ... 1 v (ownAt D v)`.

## Proof

The proof is one tactic line:

```
first | exact @GlobalTheory.CompareOff.compareOffOwn_run | ...
```

The first branch closes the goal. All the work is in [`compareOffOwn_run`](/entry/compare-off-own-run/).

## In the Lean code

The theorem is in [TraceLatticeLeSpanThetaSeriesAwayFromOwnPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceLatticeLeSpanThetaSeriesAwayFromOwnPrimeStatement.lean#L18). The theorem that it renames is in [TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceLatticeLeSpanThetaSeriesAwayFromOwnPrime.lean#L81).