---
id: theta-lift-row-properties-conj
title: Five properties of the twisted theta lifts of the row test
kind: theorem
decl: GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ThetaLiftRowPropertiesConj
covers: 5130
status: drafted
drafted_by: writer@claude
---
This theorem proves five properties of the theta lifts of the row test. It is below the last node of the trunk, [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), through two users. `test_vector_at_datum_of_join` uses it for the rational row (item 2 of that step). `local_sum_estimates_joined` gives it to [`fittedFunction_at_zero_close_alt`](/entry/fitted-function-at-zero-close-alt/), which is below the fit of constant functions (item 3). Below this theorem are 5,130 declarations.

## Statement

Each conclusion has the form $\mathrm{Big}(Q)$. This says: there is $C_{F,0}$ such that for all $\varepsilon$ and all $C_F \ge C_{F,0}$ there is $x_0$ with this property. For each datum $D$ with size data of parameter $\varepsilon$ and size $x \ge x_0$, each finite group $\Gamma$, family $A$, number field $K_s$, real datum $R$ and face $F$ in the setting `HidaSetting`, and each admissible choice $\mathrm{ch}$ at scale $C_F$, the property $Q(\mathrm{ch})$ holds. A [choice](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/ExistsMatchOver.lean#L115) holds grid data, a Weil representation, a sum choice, test indices $a$ with data $\Phi_a$, and constants $c_{ij}(t)$.

The hypotheses are [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/), [`LocalMatching`](/step/local-matching-def/), and three statements of the namespace `SquareSt`. The first of these, `WeilConvergence`, says that for a Weil representation of a pair $(M, X)$, where $M$ has signature $(r - p, p)$ at some real place and $\dim X < 2(r - p)$, each theta function satisfies the integrability condition `ModInt`. The other two are forms of the theta matching.

The conclusion is the conjunction of five statements $\mathrm{Big}(Q)$:

1. `SumOKK`: for each $t$ and $a$, the sum choice is meaningful at $\Phi_a$ (`SumOK`). For example, the support of cosets $\beta$ is finite and each $\beta$ has an expansion.
2. `ConstK`: for all $i, j, t$, the square condition `SquareNonzero` holds and $c_{ij}(t) \neq 0$.
3. `LinK`: for each $a$ and $u$, the theta integral of $u$ at $\Phi_a$ and its pairing $B^+$ with the column vector of $a$ converge (`FConv`).
4. `Formula2K`: if the numbers of the choice are in the field $L$ with embedding $\iota$ (`FieldOK`), there are $\kappa \in \mathbb{C}$ and roots of unity $\zeta_t \in L$ with $\iota(\zeta_t)\, c(t)\, \psi_a(\Theta_t x) = \kappa\, v(t, x, a)$ for all good $x$ and all $a$. Here $c(t) = \prod_{i,j} c_{ij}(t)$, $\psi_a(u)$ is the pairing of the column vector of $a$ with the theta lift of $u$, and $v(t, x, a)$ is a finite sum `vSum`.
5. `SumRatK`: if `FieldOK` holds, each $v(t, x, a)$ is in $\iota(L)$.

We have not unfolded `SquareNonzero`, `vSum`, `ModInt` or the fields of `HidaSetting`.

## Proof

1. `constK_alt` gives `ConstK` from all six hypotheses.
2. `twisted_thetaLift_cuspidal` gives `LiftsCuspidal` from `ThetaLocalInputs`: along each arrow of the grid, the theta kernel lifts cusp forms to cusp forms.
3. `sumOKK_of_theta_local_inputs` gives `SumOKK` from `ThetaLocalInputs`.
4. `twisted_characters_linearly_independent` gives `LinK` from `ThetaLocalInputs` and `LiftsCuspidal`.
5. `rowTestLiftFormula_principalLevel` gives `Formula2K` from `ConstK`, `SumOKK` and four step statements: `StepProj` from `twisted_period_identity`; `StepFlip` from `twisted_lift_flip_invariant`, which also uses `WeilConvergence` and `ThetaIntegralsAgree`; `StepUnfold` from [`twisted_theta_integral_unfolds`](/entry/twisted-theta-integral-unfolds/); and `StepJets` from [`twisted_jets_assemble`](/entry/twisted-jets-assemble/). We have not opened the proof of `rowTestLiftFormula_principalLevel`.
6. `rowTestRationalSums_of_finiteSumsMeaningful` gives `SumRatK` from `SumOKK`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ThetaLiftRowPropertiesConj.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftRowPropertiesConj.lean#L16). The theorem `GlobalTheory.T.thetaLift_row_properties` at line 30 of the same file is a renaming of it.

- `LinK` is a convergence statement, but the lemma that proves it is named `twisted_characters_linearly_independent`.
- `LocalMatching`, `SquareSt.LocalMatching` and `SquareSt.ThetaIntegralsAgree` go only to `constK_alt`. `SumOKK` and `SumRatK` need only `ThetaLocalInputs`.
- The two callers prove the three `SquareSt` hypotheses from the other inputs, with different lemmas: `twisted_weil_representation_convergence`, `twisted_square_local_matching` and `twisted_theta_integrals_agree` in [TestVectorAtDatumOfJoin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TestVectorAtDatumOfJoin.lean#L22), and `twisted_theta_integral_converges`, `twisted_local_factors_match` and `twisted_square_theta_integrals_eq` in [JoinedLocalSumEstimates.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/JoinedLocalSumEstimates.lean#L15).
