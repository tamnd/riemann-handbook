---
id: row-test-real-places-definite-periods-on-one-line
title: The periods of the row test lie on one line, second name
kind: theorem
decl: GlobalTheory.T.rowTest_realPlaces_definitePeriods_onOneLine
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.RowTestRealPlacesDefinitePeriodsOnOneLineStatement
covers: 414
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`periodsOnLine_big`](/entry/periods-on-line-big/). Its one user is [`realLine`](/entry/real-line/), which turns it into the fact `RealLine` for [the unfolding of the iterated theta lift](/entry/twisted-theta-integral-unfolding/).

## Statement

**Theorem.** For all large admissible choices $\mathrm{ch}$ (in the sense of `Big`), $\mathrm{PeriodsOnLine}(\mathrm{ch})$ holds.

$\mathrm{PeriodsOnLine}(\mathrm{ch})$ says that there is one function $\ell$ on pairs $P$ of polynomial data such that, for each admissible $(t, a, \beta, M, \tau)$, each pure datum $d$ in the support of $\tau$ and each $y$, the periods satisfy $\mathcal{P}_M(P, d) = \kappa\, \ell(P)$ for all $P$, with a constant $\kappa$ that depends on the tuple, on $d$ and on $y$. The notation is that of [the entry for `realLine`](/entry/real-line/).

## Proof

The proof applies `GlobalTheory.RowReal.periodsOnLine_big`. The statement is the same.

## In the Lean code

The theorem is in [RowTestRealPlacesDefinitePeriodsOnOneLineStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowTestRealPlacesDefinitePeriodsOnOneLineStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.RowReal.periodsOnLine_big | ...`, with a raised heartbeat limit.

The name speaks of real places and definite periods. Neither appears in the statement. The proof of [`periodsOnLine_big`](/entry/periods-on-line-big/) uses invariant functionals for a product of compact unitary groups $\mathrm{U}(n)$, one copy for each element of a finite index set. We guess that the name refers to this, but the Lean code does not say so.
