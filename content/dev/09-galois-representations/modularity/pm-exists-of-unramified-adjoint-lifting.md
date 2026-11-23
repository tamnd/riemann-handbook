---
id: pm-exists-of-unramified-adjoint-lifting
title: Potential modularity towers from the unramified inputs and adjoint vanishing
kind: theorem
decl: UpperTheory.Gal.projectedFormsSystemPart.pm_exists_of_unramified_adjoint_lifting
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.PmExTh
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem proves `PMExAlt`: each deformation space of a suitable tower carries an ideal that makes it a potential modularity tower. [`pmEx_of_printsH`](/entry/pm-ex-of-prints-h/) supplies its two inputs from the published hypotheses. The result is used for promodularity in [`main4_alt`](/entry/main4-alt/).

## Statement

**Theorem.** `UnramifiedInputs` and `AdjointLiftingTheorem` imply `PMExAlt`.

`UnramifiedInputs` bundles `CohomologyHyp`, `HypothesesH'` and four existence statements (`ModUAlt`, `LevEx`, `LamEx`, `ProModularRingExists`) that we have not unfolded. `AdjointLiftingTheorem` says: in a Hida setting over a CM field $L$ with no primitive $\ell$-th root of unity, for $2 \le n \le 4$, at each locally generic automorphic point of the universal ordinary determinant ring, each Bloch-Kato class of the adjoint is a coboundary (`AdZero`).

`PMExAlt` says: let $D$ be raw data and $T$ a tower of $D$ with `Fit` and `Deep`, and let $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$. Then there is a coefficient ring $\mathcal{O}_1$ such that for each $\mathcal{O}' \supseteq \mathcal{O}_1$ and each space $X$ of deformations over $\mathcal{O}'$, with rings $B \to A$ and universal representation $P$, there is an ideal $J$ of $B$ with these properties.

- **Finiteness.** A power of the maximal ideal of $B$ lies in $J + \mathfrak{m}_{\mathcal{O}'}B + (\psi_{v,i}(s) - 1)$, where $s$ runs over inertia at the places of $T$.
- **Points in characteristic $\ell$.** For a finite field $k$, each irreducible local point $y \colon A \to k[[t]]$ with $y(J) = 0$ and distinct inertia characters is locally zero.
- **Seeds.** Each point $y$ over $\overline{\mathbb{Q}}_\ell$ where $P$ is a seed (`IsSeedAlt`) is locally zero.
- **Purity.** Let $y$ be a point over $\overline{\mathbb{Q}}_\ell$ with $y(J) = 0$ and weights $2\,\mathrm{wts}_4(D)$. Each $r$ of $G_{\mathbb{Q}}$ that restricts to $y_*P$ is pure (`PureW`).
- **Automorphy.** If, in addition, $r$ is continuous, has the multiplier of $D$ and is irreducible on $G_L$, then $r$ is automorphic (`IsAut4Alt`).

Here $y$ is *locally zero* (`LocZero`) if each prime $\mathfrak{q}$ of $B$ that $y$ kills contains $J$.

## Proof

The proof is `promodular_existence_of_local_zero U (local_zero_of_modular_p U hA)`.

1. `local_zero_of_modular_p` proves the seed property for one link. A link $K$ is a Hida setting over the field $L$ of $T$ with a level, a character $\kappa$ and more data. Let $B_K$ be its universal ordinary determinant ring, $J_0$ a modular ideal of $B_K$ (`ModularAlt`) and $\varphi \colon B_K \to B$ a map with `IsPhi`. Then each seed point is locally zero for $J_0 B$. This is the one place where $hA$ is used, through `eigenbasis_rank_four`.
2. `promodular_existence_of_local_zero` builds $J$. `exists_two_links_same_kappa_not_dvd_of_fit_deep` gives $\mathcal{O}_1$ and two links $K, K'$ with the same $\kappa$ and with $p_{K'} \nmid p_K$. For each link it takes $B_K$, $\varphi$, $\Lambda$ and $J_0$ from the inputs. It sets $J = J_0 B + J_0' B$. Then:
   - finiteness comes from `exists_pow_maximalIdeal_le_of_modular_phi` for $K$;
   - the points in characteristic $\ell$ come from `modular_deformation_quotient_regular_at_point_alt` for both links;
   - the seeds come from step 1 for both links;
   - purity comes from `pmPur_w_alt` for $K$;
   - for automorphy, `pmAutO_alt` gives automorphy of the twist of $r|_{G_L}$ by $\kappa$ with a condition at the place $v_0$ of each link. `glueN` joins the two, with $v_0 \ne v_0'$. `pmDown_alt` brings the result down to $r$.

## In the Lean code

The theorem is in [PmExTh.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PmExTh.lean#L15). The lemmas:

- `local_zero_of_modular_p` in [BirthPm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthPm.lean#L28);
- `promodular_existence_of_local_zero` in [PmTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PmTwo.lean#L21);
- `exists_two_links_same_kappa_not_dvd_of_fit_deep` in [LinkTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkTwo.lean#L13);
- `pmAutO_alt` in [PmAutO.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PmAutO.lean#L23), `pmDown_alt` in [DnPmDown.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/DnPmDown.lean#L32) and `glueN` in [IrrArithPointsAutomorphicAway.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PlainTorsionPairs/IrrArithPointsAutomorphicAway.lean#L47).

The structures `PotentialModularityTower` and `PMExAlt` are in [PotentialModularityTower.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean#L38), `UnramifiedInputs` in [WsLink.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WsLink.lean#L18) and `Link` in [IsAlgClosureField.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/IsAlgClosureField.lean#L19). The second link is needed only for automorphy. Finiteness and purity use the first link alone.
