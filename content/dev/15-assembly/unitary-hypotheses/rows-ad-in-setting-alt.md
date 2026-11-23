---
id: rows-ad-in-setting-alt
title: The bounds at twisted primes of the middle range
kind: theorem
decl: GlobalTheory.NLink.rowsAD_in_setting_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowsADInSetting
covers: 3409
status: drafted
drafted_by: writer@claude
---
This theorem proves the two bounds at twisted primes of the middle range that the conclusion `Concl` of a family needs: the local bound `StarAD` and the error bound `BBLe` with constant $7200$. It is called through its [statement form](/entry/star-ad-and-bb-le-of-joint-cond/), and the result goes to the fields `mid` and `bb` in [the closing theorem for ConclF](/entry/nlink-close-main-alt-alt/). That theorem feeds the field `nRest` of `HypsAlt` (see the [unitary hypotheses chapter](/proof/unitary-hypotheses/)). Below this theorem are 3,409 declarations.

## Statement

Let $D$ be a datum with size data $L$, a parameter choice $P$, a norm choice $n$, local data `HW`, `F`, `Cm`, and hub data $X$. The hub data give, at each local index $i$, homomorphisms $r_i, \rho_i$ from a Galois group $G_E$ to matrix groups, a length table, an error bound $e_X(i,\pi)$ at each point $\pi$, and a finite excluded set of primes. Let $\ell_i$ be the prime of $i$.

Call $\ell_i$ *in the middle range* (`RangeAD`) if it is not small, not $3$, not $q$ or $d$, and not both above the cutoff $\ell^*$ and outside the excluded set. Let $M$ be the set of twisted indices $i$ with $\ell_i \notin \{g_0, g_1\}$ and $\ell_i$ in the middle range.

Assume `Hypotheses₂` (seven inputs named after published results) and:

1. `SetupAlt L n HW X C₂`: norm choice facts, a canonical form of $X$ for the row `rowC C₂`, parameter bounds, a size number of $L$ at least $8$, a split bound of $D$ at least $60$, the condition `KillAt` on $\rho$, and `ShaFinOdd`;
2. $C_2 \ge 1$ and `Conclusion2 D C₂`, a local lifting corollary that we have not unfolded;
3. `JointParametersHubConditions`: at twisted inert indices and good points, a local bound or a local congruence condition, by the row of $\ell_i$.

Then for $i \in M$ and each good point $\pi$ of $i$:

- `StarAD`: $v(i,\pi) \le s(i,\rho_i,\pi) + \Sigma(i,\pi) + V(\ell_i) + v_{\ell_i}(h_E) + e_X(i,\pi) + \epsilon(\ell_i)$, where $\Sigma(i,\pi)$ is a sum over the length table and $v, s, V, \epsilon$ are named quantities that we have not unfolded;
- `BBLe`: $e_X(i,\pi) \le 7200\, f\, n\, t^2\, n_V\, \lambda^2$, with numbers $f, n, t, n_V$ of $D$ and the size $\lambda$ (`large₂`) of $L$.

## Proof

1. **Step data.** The proof builds `StepAD L X`, with three fields. At inert primes of $M$, the local conditions `admitted` come from [the inert step](/entry/inert-step-main-alt-alt/), through [its statement form](/entry/adm-at-inert-of-range/). At split primes, `unramified_places_declared'` gives a declaration of the places over $\ell_i$, all with ramification index $1$. The good points come from the canonical form of $X$.
2. **StarAD.** `starInequality_rowsAD_of_global_theorems` gives `StarAD` from the row data of $X$, the step data, `IntegralityFromMetric D` (from `integralityFromMetric_of_designConditionAll`), a split case bound (from `splitCase_bound_at_point_of_admitted_items_alt`), the condition `admG2` (from `set_pt_of_setup_not_twisted`), `KillAt` and `ShaFinOdd`.
3. **BBLe.** `invariantsBoundNonsplit_of_setup` bounds the invariants of $X$ with $c = 120$. Then `nonPlacePart_localBound_le_middleRange` gives `BBLe` with constant $60c = 7200$.

## In the Lean code

The theorem is in [RowsADInSetting.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsADInSetting.lean#L15). `StarAD`, `BBLe` and `StepAD` are in [CommutingEndomorphismCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/JointConditionsZpowers/CommutingEndomorphismCondition.lean#L132).

The data $P$, $n$, `F` and `Cm` are only passed to the lemmas. The hypotheses $C_2 \ge 1$, `Conclusion2` and the joint hub conditions are used only at inert primes, in step 1.
