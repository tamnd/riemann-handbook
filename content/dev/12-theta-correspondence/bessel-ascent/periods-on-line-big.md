---
id: periods-on-line-big
title: The periods of the row test lie on one line
kind: theorem
decl: GlobalTheory.RowReal.periodsOnLine_big
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.RowTestRealPlacesDefinitePeriodsOnOneLine
covers: 413
status: drafted
drafted_by: writer@claude
---
This theorem proves `PeriodsOnLine` for all large admissible choices: as a function of the polynomial labels, every period of the row test is a multiple of one fixed function $\ell$. It joins two facts. The periods are values of an invariant linear functional on a representation of a product of compact unitary groups, and that space of invariant functionals has dimension one. Through its second name [`rowTest_realPlaces_definitePeriods_onOneLine`](/entry/row-test-real-places-definite-periods-on-one-line/) it goes to [`realLine`](/entry/real-line/) and then to [the unfolding of the iterated theta lift](/entry/twisted-theta-integral-unfolding/).

## Statement

**Theorem.** For all large admissible choices $\mathrm{ch}$ (in the sense of `Big`), there is a function $\ell$ on pairs $P$ of polynomial data such that for each admissible $(t, a, \beta, M, \tau)$, each $d$ in the support of $\tau$ and each $y$, there is $\kappa \in \mathbb{C}$ with $\mathcal{P}_M(P, d) = \kappa\, \ell(P)$ for all $P$.

The periods $\mathcal{P}_M(P, d)$ and the word "admissible" are as in [the entry for `realLine`](/entry/real-line/).

## Proof

The two inputs are these.

**The invariant functional** (`InvLine`, from `rowTest_definitePeriods_invariant_functional`). There are a finite set $\iota$, sizes $S = (k, m, s, t_S)$ (positive integers, $k$ and $m$ even, $s$ and $t_S$ odd) and entries $E_x$ for $x \in \iota$, all good, and a map $e$ from pairs $P$ to a representation $\Omega(E)$, such that for each admissible tuple, $d$ and $y$ there is a $G$-invariant functional $\lambda$ on $\Omega(E)$ with $\mathcal{P}_M(P, d) = \lambda(e(P))$ for all $P$. Here:

- $G = \prod_{j < m} \mathrm{U}(n_R(j))^\iota \times \prod_{i \le m} \mathrm{U}(n_C(i))^\iota$, with $n_R(j) = k + ms + j(t_S+1)$ and $n_C(i) = k + m - 1 + m t_S + is$;
- $\Omega(E)$ is the tensor product of $m$ Fock spaces of polynomials along the row, $m$ Fock spaces along the column, a Weyl module $V_\psi$ of $\mathrm{U}(n_R(0))^\iota$ and the dual of a Weyl module $V_{\mathrm{base}}$ of $\mathrm{U}(n_C(0))^\iota$. The highest weights and the twists of the Fock actions are read off from the entries.

The entries $E_x$ are rational numbers $a, c, v, u, b, e$. They are *good* if $a$ and $u$ are half-integers and one list made from them is strictly decreasing.

**Multiplicity one** (`OneLine`, proved as `OneFunctional.oneLine`). For every such $\iota$, $S$ and good $E$, the space $\mathrm{Hom}_G(\Omega(E), \mathbb{C})$ has dimension $1$.

Given both, let $L_0$ span the invariant functionals and put $\ell(P) = L_0(e(P))$. Each $\lambda$ from `InvLine` is $c\,L_0$ for some $c$, and $\kappa = c$. This is `periodsOnLine_of_invLine`.

## In the Lean code

The theorem is in [RowTestRealPlacesDefinitePeriodsOnOneLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowTestRealPlacesDefinitePeriodsOnOneLine.lean#L8). It is `big_mono` with `periodsOnLine_of_invLine OneFunctional.oneLine` ([PeriodsOnLineOfInvLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/PeriodsOnLineOfInvLine.lean#L22)) applied to `GlobalTheory.T.rowTest_definitePeriods_invariant_functional`.

- `OneLine`, `OM`, `omRep` and `invFun` are in [MinorOrderedEntries.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/MinorOrderedEntries.lean#L237). `OneLine` has no hypothesis on the choice; it is a statement about compact groups only.
- `oneLine` is in [FinrankInvFunBranch.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FinrankInvFunBranch.lean#L248). It calls `exists_ganGrossPrasad_row_weights`, `exists_ganGrossPrasad_column_weights` and `contracts_tensorProduct_chain`. The names point to branching laws of Gan-Gross-Prasad type, but we have not unfolded these lemmas and do not name a published result.
- `invLine_big` is in [RowTestDefinitePeriodsInvariantFunctional.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowTestDefinitePeriodsInvariantFunctional.lean#L88). It uses `gen_left`, `genPer_conv`, `coefPsi`, `coefBase` and `invLine_of_iso`, which we have not unfolded.
- We have not unfolded `weylSub`, `fock` or `hw`, so "Weyl module" and "highest weight" are readings of the names.
