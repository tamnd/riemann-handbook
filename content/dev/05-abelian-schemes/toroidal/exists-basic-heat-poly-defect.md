---
id: exists-basic-heat-poly-defect
title: Building a torus-invariant heat operator and computing its defect
kind: theorem
decl: GlobalTheory.HeatEx.exists_basic_heat_polyDefect
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTorusInvariantHeatOperatorPolynomialDefect
covers: 471
status: drafted
drafted_by: writer@claude
---
This theorem constructs a basic (torus-invariant) heat operator on the Raynaud extension and shows that its defect against the periods is a polynomial in the level. It proves [the statement form](/entry/exists-torus-invariant-heat-operator-polynomial-defect/), which is step 1 of [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/).

## Statement

The statement is that of [the statement form](/entry/exists-torus-invariant-heat-operator-polynomial-defect/). In the setting of [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/), with monomial periods in $t_1, \dots, t_m$ and a derivation $D$ with $D(t_i) \in (t_i)$, there are a basic heat operator $h$ for $D$ and maps $w, \pi, \pi'$, with $w(\mu)$ additive, such that the defect of $h$ is $2k\, w(\mu)(\alpha) + 2k^2 \pi(\mu) + 2k\, \pi'(\mu)$.

## Proof

The proof has two parts: build $h$, then compute its defect.

1. `exists_connection_matrix_invariant_basis` gives a symmetric $\Theta \in M_n(R)$, an open cover $(V_i)$ of $B$ with each $V_i$ inside a trivializing open of $L$, with transition functions $g_{ii'}$, and lifts $d_i$ of $D$ to $q^{-1}V_i$ that keep each weight, such that $d_i f - d_{i'} f = \sum_{a,b} \Theta_{ab}\, (\partial_b \log g_{ii'})\, \partial_a f$ on overlaps. This is a torus-invariant form of the Kodaira-Spencer relation of [`hasLogKS`](/entry/has-log-ks/), with $\partial_b \log g$ written as `dlg`.
2. `exists_weightZeroCocycle_eq_logDerivative_comb_add_coboundary`: on such a cover, each Čech 1-cocycle $z$ of weight-zero functions is $\sum_b c_b\, \partial_b \log g_{ii'}$ plus the coboundary of weight-zero functions $y_i$. This lemma does not involve $D$.
3. `exists_torus_invariant_heat_operator_of_symmetric_relation` takes the data of step 1, with the lemma of step 2 as a hypothesis, and gives a basic heat operator $h$ for $D$. We have not opened its proof (it is `HeatGlue.exists_basic_heat`), so we do not know how it chooses $u$, $p_i$ and $p'_i$.
4. `exists_polynomial_defect_heatOperator_monomial`: for any basic $h$, under monomial periods and $D(t_i) \in (t_i)$, the defect has the polynomial form above.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsTorusInvariantHeatOperatorPolynomialDefect.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorPolynomialDefect.lean#L25). The four lemmas are called through their statement files; the first is proved by `HeatInvLift.exists_invLift_symmKS` and the second by `PullbackWeightZero.exists_comb_dlg_add_cob`.

Steps 1 to 3 do not use the monomial periods or the condition on $D(t_i)$; only step 4 does. Step 3 returns only some basic $h$: the conclusion does not record that the symbol of $h$ is the matrix $\Theta$ of step 1. So the Kodaira-Spencer meaning of the symbol is lost here, and [`isKS_of_heat`](/entry/is-ks-of-heat/) recovers it by a uniqueness argument.
