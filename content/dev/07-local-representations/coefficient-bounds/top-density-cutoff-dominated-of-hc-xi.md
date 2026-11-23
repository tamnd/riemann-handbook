---
id: top-density-cutoff-dominated-of-hc-xi
title: Domination of cut-off top densities, restated
kind: theorem
decl: GlobalTheory.T.topDensity_cutoff_dominated_of_HC_xi
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.TopDensityCutoffDominatedOfHCXiStatement
covers: 624
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`HatNF.topDensity_cut_dominated_all`](/entry/top-density-cut-dominated-all/). It has the same statement and its proof only calls that theorem. [The pointwise bound for Capelli eigenfunctions](/entry/pointwise-bound-eigenfunction/) uses it to turn `BesselXiIntegrable` into `NFTopDomAll`, which it then passes to its two case theorems.

## Statement

**Theorem.** `BesselXiIntegrable` implies `NFTopDomAll`.

`BesselXiIntegrable` asserts the existence of a function $\Xi$ with a coefficient bound and an integrability condition; it is proved as `xiExists` (see [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/)). `NFTopDomAll` says: for each $C_b$ there is $C_c$ such that, for a smooth decaying $f$ with enough decay, a cutoff $\chi$ and an admissible word $w$, the top densities of the cut-off functions $\chi(G/\varepsilon)\,G^{p_0} f$ are dominated by one integrable function on $\mathbb{C}^{r+1}$ as $\varepsilon \to 0^+$. The full statement is in [the entry for `topDensity_cut_dominated_all`](/entry/top-density-cut-dominated-all/).

## Proof

The proof is the term `GlobalTheory.HatNF.topDensity_cut_dominated_all`. There is nothing else. The mathematics is in [`HatNF.top_density_dominated`](/entry/top-density-dominated/).

## In the Lean code

The theorem is at [TopDensityCutoffDominatedOfHCXiStatement.lean line 8](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/TopDensityCutoffDominatedOfHCXiStatement.lean#L8). The proof is the usual `first | exact ... | ...` wrapper of the `T.` restatement files. `NFTopDomAll` is in [CutLimENF.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutLimENF.lean#L70), and `BesselXiIntegrable` is in [BesselXiIntegrable.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/BesselIntegrals/BesselXiIntegrable.lean#L6), where it is defined as `Formalism.FourierDecayAlt.B.XiExists`: for each $A \ge 2(k+r)(r+1)+1$ there is $\Xi \ge 0$ on the matrices with `CoefBound D Ξ A` and `XiInt D Ξ 2`. We have not unfolded these two conditions.
