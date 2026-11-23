---
id: twisted-pairing-identity
title: The period of one basis element is a fixed multiple of a class sum
kind: theorem
decl: GlobalTheory.T.twisted_pairing_identity
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.PairingOfPointsExpansion
covers: 998
status: drafted
drafted_by: writer@claude
---
This theorem is the content of [`twisted_jet_one_of_all`](/entry/twisted-jet-one-of-all/), which is its second name, and so of the one-element case in [the jet step of the row test](/entry/twisted-jet-succ-eq-assembly/). It turns a combination of integrals over definite unitary groups into a finite sum over classes. The constant comes from one average over a compact real group at the last node.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/) and `SumOKK`. Then for all large admissible choices $\mathrm{ch}$ (in the sense of `Big`) and each polynomial datum $P$ on the column and the row, there is $\kappa \in \mathbb{C}$ such that, for all $t$, $a$, $\beta \in \operatorname{supp}_t(\Phi_a)$, volumes $M$ with `IsTermVol`, expansions $\tau$ with `IsExpansion`, and all $y$,
$$P_M(\delta_P, \tau; \varphi_a, F_y) = \kappa \sum_{c} \gamma(c)^{-1}\, \langle \tau, c\rangle\bigl(\tilde\Psi_a(p_c), F'_y(q_c)\bigr).$$

Here $\delta_P$ is the combination with the single element $P$. The notation is that of [the parent entry](/entry/twisted-jet-succ-eq-assembly/). The statement is `JetsOne ch` with the definition written out.

## Proof

1. `Big.and` joins `SumOKK` with `first_row_invariant_under_twist`. The second fact says that the pairing of points does not change when the first point $y_0$ moves by an element of the first row level and $F'_y$ moves with it.
2. `col_real` and `form_real` give linear functionals $\Lambda_0$, $\Lambda'_0$ at the first nodes. `col_chain` and `row_chain` extend them along the column and the row to chains $\Lambda_j$, $\Lambda'_j$, one for each node up to $m$.
3. The private lemma `last_functional_compatible` gives $c \in \mathbb{C}$ and a group map $s$ from the group of node $(m,m)$ to the group of the top node $m$. It is the stabilizer embedding, and the record `LastOK` holds for $c$ times the pairing `brPair`. Its main field says this. For each Haar probability measure $\kappa$ on the real group of node $(m,m)$,
$$\int \Lambda_m\bigl(\rho(s(k))^{-1}u\bigr)\, \Lambda'_m\bigl(\rho'(k)^{-1}u'\bigr)\, d\kappa(k) = c\, B(u, u').$$
The real group is compact because node $(m,m)$ is definite. The proof takes one Haar probability measure with `exists_haar` and uses `TopIntegral.real_average`. Then it uses the uniqueness `isHaarMeasure_eq_of_isProbabilityMeasure`.
4. Put $\kappa = c$. It does not depend on $t$, $a$, $\beta$, $M$, $\tau$ or $y$.
5. `isMeasDef_of_isTermVol` gives that the levels of $M$ are open compact and fit the measures. `normalisedKernelExpansionSum_levelInvariant` gives four invariances of the pairing of points under these levels.
6. `JetsOne.glue` does the main work. All nodes on the column and the row are positive definite (`posDef_top`, `posDef_grid`). So each integral over a fundamental domain becomes a finite sum over classes, weighted by the inverse orders $\gamma(c)^{-1}$ of the stabilizers. The functionals of step 2 and the record of step 3 evaluate the integrand at the points of each class.
7. The private lemma `pairing_of_points_expansion` rewrites $c$ times the pairing of points as the sum over $\tau$ of the pairing `pairP`. Rewrites with `defTot`, `defPer_eq`, `classSum` and `mul_finsum` then close the goal.

We have not unfolded `glue` past its statement, nor the functionals of step 2.

## In the Lean code

The theorem is in [PairingOfPointsExpansion.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/PairingOfPointsExpansion.lean#L55), with the two private lemmas at lines 12 and 35. `LastOK` and `glue` are in [JetsGlue.lean](lean:Development/AutomorphicArithmetic/LocalEmbeddings/JetsGlue.lean#L23).

- The theorem is a near copy of `term_volume_class_sum` in [TermVolumeClassSum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/TermVolumeClassSum.lean#L64). That one assumes `Hypotheses₂` and calls `first_level_invariance` in place of `first_row_invariant_under_twist`. The two private lemmas copy `last_ok` and `pair_eq` of the same file.
- `ThetaLocalInputs` enters only through `first_row_invariant_under_twist`. In that proof it goes to `twist_first_coefficient_law`, which we have not opened.
