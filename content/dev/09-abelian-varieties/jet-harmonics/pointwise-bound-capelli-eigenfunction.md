---
id: pointwise-bound-capelli-eigenfunction
title: The pointwise bound for Capelli eigenfunctions (restatement)
kind: theorem
decl: GlobalTheory.T.pointwiseBound_capelli_eigenfunction
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PointwiseBoundCapelliEigenfunctionStatement
covers: 1069
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. It gives the pointwise bound for decaying Capelli eigenfunctions a name in the namespace `GlobalTheory.T`. Its caller [`BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries`](/entry/pointwise-bound-discrete-series/) uses it once, as the last step of the bound for discrete series coefficients. The real content is in [`BpEigen.pointwise_bound_eigenfunction`](/entry/pointwise-bound-eigenfunction/).

## Statement

**Theorem.** Assume `BesselXiIntegrable` and `ThmPActualCpt`. For all $C, C_3, C_0 \ge 0$ there are $C_4$ and $C_c$ such that the following holds. Let $f$ be a function on $U(H_{k,r})$ with values in $\mathrm{Hom}(W_q, W_p)$ that is smooth, decays to order $A_0$ with all its derivatives, and is an eigenfunction of the Capelli operator with eigenvalue polynomial $\prod_s (y + \lambda'_s)$. Assume the grid conditions `StdNum C b c P λ`, one of the two cases of `Cases P n₀`, the bounds $3(r+1) \le 2p_0 \le 2C_0(r+1)^2$, a decay margin, a bound on $\lambda' - \lambda$, and the regularity bound `RegularityBoundBigCell p f b C₃ (2p₀+n₀)`. Then `ThmBpAt p f b C₄ n₀ p₀`.

The [entry of the proof](/entry/pointwise-bound-eigenfunction/) states each hypothesis in full.

## Proof

The statement is the same text as the statement of `BpEigen.pointwise_bound_eigenfunction`. The proof is that theorem. There is no other step.

## In the Lean code

The theorem is in [PointwiseBoundCapelliEigenfunctionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundCapelliEigenfunctionStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `BpEigen.pointwise_bound_eigenfunction` in each branch.

The file opens both `BpJoin` and `Formalism.FourierDecayAlt.P.CutBP2`, and each namespace has a definition `EigDec`. Only `BpJoin.EigDec` (in [SupWOfSup.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/SupWOfSup.lean#L39)) takes the arguments `f A₀ λ'`; `CutBP2.EigDec` takes a place datum first. So the statement means `BpJoin.EigDec`, although a reader of the file cannot see this at once.
