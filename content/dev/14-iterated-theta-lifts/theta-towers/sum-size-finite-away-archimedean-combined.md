---
id: sum-size-finite-away-archimedean-combined
title: Size bounds for the sums at the finite, away and archimedean places
kind: theorem
decl: GlobalTheory.SumSize.Join.sum_size_finite_away_archimedean_combined
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.SumSizeFiniteAwayArchimedeanCombined
covers: 1150
status: drafted
drafted_by: writer@claude
---
This theorem bounds, for all large data, the denominators and the archimedean heights of certain test vectors, and it proves a condition on ramified primes. It is restated as [`sum_size_bound_all_places`](/entry/sum-size-bound-all-places/), and [the bound on the maximal slope at fitted points](/entry/fitted-function-at-zero-close-alt/) uses its three conclusions. Below it are 1,150 declarations of the proof.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/). Then `FinK`, `AwayK` and `InfK` hold.

Each of the three has the form `BigC Q`: there is $C_{F,0}$ such that for each $C_F \ge C_{F,0}$ there is $C_0$, and for each $\varepsilon$ and $C \ge C_0$ there is $x_0$ with this property. For each datum $D$ with size data at this $\varepsilon$ and $x \ge x_0$, each family $A$ over a finite group, real datum $R$ and face $F$ in a Hida setting, and each valid choice $ch$ at scale $(C_F, b)$ with a good field, $Q(F, ch, C, b)$ holds.

Let $L$ be the coefficient field of $D$, $v_w$ the valuation at a finite place $w$ of $L$ and $\ell_w = \log N(w)/[L:\mathbb{Q}]$. A *loss* $d$ with bound $B$ is a function $d \ge 0$ on the finite places of $L$, with finite support and $\sum_w \ell_w d(w) \le B$. Let $\sigma = \sum_{v \in S_0} \mathrm{depth}(v) \log N(v)$, and let

$$b_1 = C f m N^2 (\log b + \sigma)\, b, \qquad a_1 = C f N b \log b + C m N^2 \sigma.$$

A place $w$ is *away* for $t$ if each prime of $E$ in the set $Q(t)$ of the level datum lies over $S_0$ or contains no rational prime that lies in $w$.

- `FinAt`: there is a loss $d$ with bound $m b_1/2$ such that, for each test lattice $M$, each $t$, each $w$ away for $t$, and each lift $y$ of a test vector $v_K$, there is $s \ne 0$ in $L$ with $v_w(s) \le d(w)$ and $s y \in M$.
- `AwayAt`: each $w$ is away for $\mu(w)$.
- `InfAt`: for each test lattice, each metric $X$ and each matrix $V$ over $L$ that gives $v_K$, the height of $V$ (the mean over the infinite places of the log of the operator norm) is at most $m a_1$.

## Proof

1. `sumOKK_of_theta_local_inputs` and `depthK_of_sumOKK` give the row claim `SumOKK` and a depth bound `DepthK`. `sum_size_dictionary` gives `DictK`.
2. Factor lemmas give nine bounds at the finite places: for the scalar, the coefficients, the data, the gamma factors, the top and row steps, the last pairing, the test vector and the form. They give nine bounds at the infinite places, with the tensor, the count and the class count in place of the coefficients, the data and the gamma factors.
3. `finiteSumDenominatorBound_of_factor_claims` combines `SumOKK`, `DepthK` and the nine finite bounds into `FinK`. `archimedeanSumSizeBound_largeData_from_factors` combines `SumOKK`, `DepthK` and the nine infinite bounds into `InfK`.
4. `twisted_local_factor_away_from_level` gives `AwayK`.

## In the Lean code

The theorem is in [SumSizeFiniteAwayArchimedeanCombined.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SumSizeFiniteAwayArchimedeanCombined.lean#L26). The claims are in [InfClassAt.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/InfClassAt.lean#L203). The finite assembly lemma is in [FiniteSumDenominatorBoundOfFactorClaims.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteSumDenominatorBoundOfFactorClaims.lean#L587). We have not unfolded the two assembly lemmas.

The factor lemmas that we opened are `first | exact …` wrappers of inner lemmas.

`AwayK` does not use the hypothesis. Its proof, `twist_trivial_away_from_level` in [TwistedLocalFactorAwayFromLevel.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedLocalFactorAwayFromLevel.lean#L16), starts with `intro _`. It argues from the Hida setting alone, by cases on whether $w$ is a twisted place. At the other places $\mu(w) = \mu_0$ and the character is trivial.
