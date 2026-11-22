---
id: prop-eg-w-of-printed-hida
title: Eisenstein-congruent representations with unlinked adjoint
kind: theorem
decl: UpperTheory.V.Z.Sym.W.prop_eg_w_of_printed_hida
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.TPropEGW
covers: 757
status: drafted
drafted_by: writer@claude
---
This theorem proves `PropEGW` from the published hypotheses `HypothesesH'`. Its result goes to [`unitary_three_automorphy_dense_of_prints_and_row`](/entry/unitary-three-automorphy-dense-of-prints-and-row/), which takes adjoints of the representations that it gives as seeds. The proof only passes hypotheses along. The real content is in [`prop_eg_complex_of_printed_hida`](/entry/prop-eg-complex-of-printed-hida/).

## Statement

**Theorem.** `HypothesesH'` implies `PropEGW`.

`PropEGW` has the hypotheses and the first two conclusions of `PropEGc`, stated in [`prop_eg_complex_of_printed_hida`](/entry/prop-eg-complex-of-printed-hida/): for all large $k$ with $\varphi(c) = (-1)^k$ there is $\rho \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ with `EisRep ι φ θ k ρ` and `PR`. In place of the conditions `RW` and `NoHalf` of `PropEGc`, it asks that $\mathrm{ad}^0\rho$ is unlinked. A representation $r$ is *unlinked* if at each finite place $w \nmid \ell$ where $r$ has finite image of inertia, there are $j \ge 1$ and a Frobenius $s$ for $N(w)^j$ such that no two eigenvalues $\alpha, \beta$ of $r(s)$ satisfy $\alpha^k = (N(w)^j \beta)^k$ for some $k \ge 1$.

## Proof

Take $\rho$ from `PropEGc`. Keep `EisRep` and `PR`. The lemma `adUnl` says that `RW` and `NoHalf` for a 2-dimensional $\rho$ imply that $\mathrm{ad}^0\rho$ is unlinked.

## In the Lean code

The theorem is in [TPropEGW.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TPropEGW.lean#L9). `PropEGW` is in [UnitaryTwoForm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/UnitaryTwoForm.lean#L176). `adUnl` is in [SplitTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnlinkedHeckeRoots/SplitTwo.lean#L40), and its statement `AdUnl` in [UnitFormC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnitFormC.lean#L103). `Unlinked` is in [IsAutomorphicOverImagQuad.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AdmissibleResidues/IsAutomorphicOverImagQuad.lean#L19). We have not read the proof of `adUnl` beyond its first step.
