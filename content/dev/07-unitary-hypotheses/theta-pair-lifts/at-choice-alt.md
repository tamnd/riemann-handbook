---
id: at-choice-alt
title: Three bounds for every selection, from Siegel-Weil
kind: theorem
decl: GlobalTheory.LocalRows.at_choice_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AtChoice
covers: 13599
status: drafted
drafted_by: writer@claude
---
This theorem proves three properties of an arbitrary selection of bundles from one hypothesis, `SiegelWeilUnitaryConvergent`. The wrappers [`sLp_sO_hTF_of_siegelWeil`](/entry/s-lp-s-o-h-tf-of-siegel-weil/) and [`lg1_sLp_sO_hTF`](/entry/lg1-s-lp-s-o-h-tf/) turn them into the fields `sLp`, `sO` and `hTF` of the record built by [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/). Most of the work is in [`offDiag`](/entry/carrier-gap-off-diag/), which dominates 12,991 of the 13,599 declarations below this theorem.

## Statement

The hypothesis `SiegelWeilUnitaryConvergent` says the following. Let $E/F$ be a CM extension with conjugation $\sigma$, and $J$ a nondegenerate $M \times M$ hermitian matrix over $E$. Then each fundamental domain of the kind `IsFDH` has finite Haar volume. For $2n < M$, for each nondegenerate hermitian $T$ of size $n$ and each factorizable test function $\Phi$ with the stated decay and smoothness, the mean of the theta series of $\Phi$ over the vectors with Gram matrix $T$ equals $g_\infty(T) \prod_v g_v(T)$. Here $g_\infty$ and $g_v$ are densities of the push forward of local measures under the Gram map. This has the shape of the Siegel-Weil formula in Weil's convergent range (A. Weil, Acta Math. 113, 1965). We have not checked each normalization.

Let $\mathcal A$ be a family class and $\sigma$ a selection of bundles for $\mathcal A$ (`RawSel`): a bundle $\sigma(F, x, i)$ for each family $F$ of $\mathcal A$, each $x > x_1$ and each index $i$. Write $\mathcal D = $ `D3 3 𝒜` for the subclass that also appears in [`HypsAlt`](/step/hyps-alt-def/), and $s_\sigma$ for the selection of spectral ties that $\sigma$ gives (a threshold, and the ties of each selected bundle).

**Theorem.** Under this hypothesis:

1. (`SelectionLpBound`) `LoopRowS 3 𝒟 s_σ` holds. For each function $a_F$, this is a [closed](/step/closed-def/) statement on $\mathcal D$ that bounds the loop rows of the ties, eventually in $x$. We have not unfolded it further.
2. (`SelectionOrderBound`) On $\mathcal D$ it is closed that, eventually, under a size hypothesis, for each $x$ above the threshold and distinct words $u \neq u'$,
$$\|K_0(u,u')\|^2 \le (1 + b^{-6}) \frac{d(u)\, d(u')}{D^*},$$
where $K_0(u, u')$ is an off-diagonal entry of the ties, $b$ is a scale of the size data, and $d$ and $D^*$ are fields of the datum (`duS`, `Dstar`).
3. (`H_hTF`) On $\mathcal D$ it is closed that, eventually, under a size hypothesis, $1 \le \operatorname{Tr}(w)\, \kappa^{2 r_S}$ for each $w$ (`TFrame`). This does not depend on $\sigma$.

## Proof

Let $T$ be the twist selection on $\mathcal D$ that $\sigma$ gives.

1. `bothRowsFromSiegelWeil_alt` gives two closed statements on $\mathcal D$: a rank bound `RanksF` and the frame bound, which is part 3.
2. `volumeRatio` gives `MassRatioUnderVolume D` for each datum $D$. `rowsFinDim_link` gives `RowsFinDim` with no hypothesis. With these, `loopRows_of_rowsFinDim_alt` gives part 1. The size condition `TuSize` that it needs is part of membership in $\mathcal D$.
3. `offDiag` gives part 2. Its inputs are `SWXS` (from `swxs_of_siegelWeil`), `RowNGP` (from `rowNGP_of_siegelWeil`), `RowsFinDim`, the condition `LocTied` on each selected datum (a field of the selected bundle), the rank bound of step 1 and part 1.

## In the Lean code

The theorem is at [AtChoice.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean#L16). The three properties are in [CountsIrreducibilityConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CountsIrreducibilityConstants.lean#L95) and, for `H_hTF`, [CountsIrreducibilityConstants.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/CountsIrreducibilityConstants.lean#L224). `LoopRowS` and `TheoremSSelected` are in [ThmSOwn.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean#L669), `TFrame` in [PExtra.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/PExtra.lean#L247). The hypothesis is in [SiegelWeilUnitaryConvergent.lean](lean:Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean#L46).

The lemmas: `bothRowsFromSiegelWeil_alt`, `loopRows_of_rowsFinDim_alt`, `CarrierGap.offDiag`, `volumeRatio`, `swxs_of_siegelWeil`, `rowNGP_of_siegelWeil`, `rowsFinDim_link`.

The names do not match the definitions. "Lp bound" is a statement on loop rows, "order bound" is the off-diagonal bound of part 2, and "torsion free" is the lower bound `TFrame`. The name `at_choice_alt` says only that the statement holds at each choice $\sigma$.
