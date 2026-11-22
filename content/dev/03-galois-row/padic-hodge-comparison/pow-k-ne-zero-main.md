---
id: pow-k-ne-zero-main
title: The top power of the de Rham first Chern class is not zero, with the three inputs supplied
kind: theorem
decl: CrystallineSemistableComparison.Pb.powK_ne_zero_main
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.ConeSectionRestriction.PowTop
covers: 666
status: drafted
drafted_by: writer@claude
---
This theorem has the same statement as [its parent](/entry/pow-k-ne-zero/): for a connected smooth $X$ of dimension $d$ over a field $K$ of characteristic $0$, with a tautological line $D$ and a de Rham first Chern class $c$ of $D$, the power $c^d$ is not zero. Its proof only passes three proved lemmas to [the conditional form](/entry/pow-k-ne-zero-of/), which has the real argument. Below it are 666 declarations, and most of them are below these three lemmas.

## Statement

The statement is the same text as `powK_ne_zero`. See the parent entry.

## Proof

Apply `powK_ne_zero_of` to three lemmas, and then to `q d D hD c hc`.

1. `geo_setup` proves `GeoSetupP`. A closed $X \subseteq \mathbb{P}^N_K$ of dimension $n+1$ has homogeneous $y_0, \dots, y_{n+1}$ of one degree $e > 0$ whose charts $U_k = X \cap D_+(y_k)$ cover $X$, with affine finite intersections. On an open $V$ inside all $U_k$, the ratios $t_k = y_{k+1}/y_0$ are étale coordinates. The rings of the intersections embed in $\Gamma(V)$, and each is finitely generated and integral over a ring of monomials in the $t_k$ (`torusS`).
2. `resid_alg` proves `ResidAlgP`. This is a statement in commutative algebra only: in a domain with such coordinates, the unit $(t_0 \cdots t_n)^{-1}$ is not a sum of Jacobian terms from the intersection rings plus derivatives. Its proof takes a trace down to $K(t)$ and applies a residue. We have not followed it further.
3. `firstChern_local_exact` proves `LocExactP`. On each chart, $e$ times the local cocycle of $c$ is the coboundary of a $1$-cochain $b_k$ in the first step of the filtration. On $U_k \cap U_{k'}$, the difference $b_k - b_{k'}$ is a truncated $d\log$ of a lift of $y_k / y_{k'}$.

## In the Lean code

The theorem is in [PowTop.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/PowTop.lean#L16). The three hypotheses are defined in [ConeHyp.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/ConeHyp.lean#L19). The lemmas are in [GeometricGenericComponents.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/GeometricGenericComponents.lean#L21), [ResidStmt.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/ResidStmt.lean#L15) and [LocExact.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/ConeSectionRestriction/LocExact.lean#L63).
