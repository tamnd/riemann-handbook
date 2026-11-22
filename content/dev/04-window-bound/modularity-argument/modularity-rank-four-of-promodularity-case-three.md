---
id: modularity-rank-four-of-promodularity-case-three
title: Symplectic four-dimensional automorphy from promodularity in case III
kind: theorem
decl: UpperTheory.V.Cu.modularity_rank_four_of_promodularity_case_three
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ModularityRankFourOfPromodularity
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem is the second step of [`main4_alt`](/entry/main4-alt/). It proves `AutomorphyRankFourDense` from `PromodularityCaseThreeDense`, which `main4_alt` gets from a chain reduction. The proof does the promodularity in case II itself. Then it goes from promodularity to finiteness, purity and automorphy.

## Statement

**Theorem.** `PromodularityCaseThreeDense` implies `AutomorphyRankFourDense`.

Both statements are given in [`main4_alt`](/entry/main4-alt/). We recall the objects. Let $D$ be good raw data in case II or III, and $\mathfrak{a}$ an ambient datum: a field $K$ with a valuation ring $V$. A pair $(r, u)$ with `KPair D 𝔞 r u` is a lift $r \colon G_{\mathbb{Q}} \to \mathrm{GSp}_4(V)$ of the residual representation of $D$, with the multiplier and ramification of $D$. It comes from a complete discrete valuation ring with finite residue field, and a symplectic $u$ makes it upper triangular on the decomposition group at $\ell$, with the diagonal characters of $D$. `Star` says that $r$ over $K$ is irreducible or a block extension that does not split. `ProModAlt D ι 𝔞 r` says that $r$ is conjugate over $K$ to the specialization at a point $y$ of the universal representation of a potential modularity tower $(T, X, J)$, with $y(J) = 0$.

## Proof

1. With `D.Good`, the case hypothesis gives case II or case III. The lemma `ambZero` gives $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$.
2. **Promodularity.** Each `KPair` with `Star` is promodular. In case II this is `proMod_of_pmEx_of_ctx2_of_kPair_of_star`, from `CohomologyHyp`, `FerreroWashington`, `SeedIIAlt` and `PMExAlt`. In case III it is the hypothesis.
3. **Characteristic $\ell$.** By `contradiction_star_promodular`, a promodular `KPair` over a field of characteristic $\ell$ is not `Star`. With step 2 this gives `Con D`.
4. **Purity.** `pureW_of_proModular_of_isZero` gives `PurityAtPoints D ι`: each promodular point over $\overline{\mathbb{Q}}_\ell$ is pure (`PureW`).
5. **Automorphy.** `aut_n_alt` gives `AutmAlt D ι`: each irreducible promodular point over $\overline{\mathbb{Q}}_\ell$ is `IsAut4Alt`. Irreducible implies `Star`, so step 2 applies.
6. `fin0_no_end_all_irr_of_good_con_purity_aut` turns these three facts into `Fin0`, `NoEnd` and `AllIrr (IsAut4Alt ι)`.

We have not unfolded `PureW`, nor the proofs of the lemmas in steps 3 to 6.

## In the Lean code

The theorem is in [ModularityRankFourOfPromodularity.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ModularityRankFourOfPromodularity.lean#L20). `KPair` and `Con` are in [NearSplit.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/NearSplit.lean#L63), `ProModAlt` in [PotentialModularityTower.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean#L67). The lemmas:

- `proMod_of_pmEx_of_ctx2_of_kPair_of_star` in [Gsp4PromodularityCaseTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Gsp4PromodularityCaseTwo.lean#L101);
- `contradiction_star_promodular` in [ContradictionStarPromodular.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ContradictionStarPromodular.lean#L183);
- `pureW_of_proModular_of_isZero` in [CharpolyConj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CharpolyConj.lean#L32);
- `aut_n_alt` in [MapRepComp.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MapRepComp.lean#L201);
- `fin0_no_end_all_irr_of_good_con_purity_aut` in [VWinPm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VWinPm.lean#L75).

`IsAut4Alt` is `IsAutQA`: if $r$ is continuous, then for each quadratic CM field $K$ on which $r$ stays irreducible, $r|_{G_K}$ is attached to a regular algebraic cuspidal representation of $\mathrm{GL}_4(\mathbb{A}_K)$, with a condition `WitA` that we have not unfolded. The $\iota$ of the conclusion does not depend on $D$. The hypothesis `HFit` is used only in case III, where it is passed to `PromodularityCaseThreeDense`.
