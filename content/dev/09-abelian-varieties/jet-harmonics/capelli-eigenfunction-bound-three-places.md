---
id: capelli-eigenfunction-bound-three-places
title: The pointwise bound for Capelli eigenfunctions from three places (restatement)
kind: theorem
decl: GlobalTheory.T.capelli_eigenfunction_bound_three_places
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.CapelliEigenfunctionBoundThreePlacesStatement
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. It gives [`EigenThreePlaces.main`](/entry/eigen-three-places-main/) a name in the namespace `GlobalTheory.T`. The real content is in that entry. The theorem [`BpEigen.pointwise_bound_eigenfunction`](/entry/pointwise-bound-eigenfunction/) uses it through its two case theorems, one for different types and one for equal types.

## Statement

We use the notation of [the parent entry](/entry/pointwise-bound-eigenfunction/) for $E_f$, $G_p$ and $\|f\|^2$.

**Theorem.** Assume `BesselXiIntegrable`, `ThmPActualCpt` and `NFTopDomAll`. For all $C_b$ and all $C_3, C_\Lambda, C_0 \ge 0$ there are $C_4$ and $C_c$ with this property. Let $p$ be a place datum, and let $p_+$ and $p_-$ be two more place data with shifted types and the same base points $z, z'$ as $p$. Let $f$ be a decaying Capelli eigenfunction, and let $A_\pm$ be polynomial operators that link $f$ at $p$ to $f$ at $p_\pm$. If the hypotheses listed in the [entry of the proof](/entry/eigen-three-places-main/) hold, then for each $\gamma$ with $G_p(\gamma) > 0$,

$$E_f(\gamma) \le b^{C_4(2r+2)^4}\, G_p(\gamma)^{-(2p_0+n_0)}\, \|f\|^2.$$

## Proof

The statement is the same text as the statement of `EigenThreePlaces.main`. The proof is that theorem. There is no other step.

## In the Lean code

The theorem is in [CapelliEigenfunctionBoundThreePlacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/CapelliEigenfunctionBoundThreePlacesStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `EigenThreePlaces.main` in each branch. The file sets `maxHeartbeats` to 1000000. The conclusion is `TBB.ThmBpAt p f b C₄ n₀ p₀`.
