---
id: see-saw-twist-place-laws-of-root-of-unity-rescaling
title: The twist place laws survive a rescaling by roots of unity (restatement)
kind: theorem
decl: GlobalTheory.T.seeSawTwistPlaceLaws_of_rootOfUnityRescaling
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawTwistPlaceLawsOfRootOfUnityRescalingStatement
covers: 1076
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the laws for rescaled pinned tuples](/entry/laws-of-pin-resc/). It adds no mathematics. Its user is [`laws_resc_alt`](/entry/laws-resc-alt/), which applies it to a tuple $\mathrm{resc}(w_0, s)$ in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in the entry [laws-of-pin-resc](/entry/laws-of-pin-resc/).

## Statement

Let $D$ be a datum, $c$ a common datum (`Comm D`), $v$ a choice of level data (`VCom c`), $t$ a tuple (`Tup c`) and $w$ a decorated tuple over $t$ (`VTup t`). Assume that $c$, $t$ and $v$ satisfy their conditions `Is`, that the Weil data of $v$ are compatible with $t$ (`WeilOK`), and that $w$ is obtained from a pinned tuple $w_0$ by a rescaling with roots of unity (`QPinU v w`). Then the three laws at the twist places hold for $w$: the iterated integral law `QLaw`, the law at the last steps `QLast`, and the finiteness of cells `QFin`.

The objects are defined in the entry [laws-of-pin-resc](/entry/laws-of-pin-resc/).

## Proof

The proof is the term `laws_of_pin_resc`, tried in three forms by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic. The statements are the same, so the first form works.

## In the Lean code

The theorem is at [SeeSawTwistPlaceLawsOfRootOfUnityRescalingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawTwistPlaceLawsOfRootOfUnityRescalingStatement.lean#L10). It only passes its hypotheses along to `GlobalTheory.QTw.laws_of_pin_resc`. A second caller, `GlobalTheory.QColLaws.laws_resc` in [TrueGeometryFamilyFinal.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyFinal.lean#L24), uses it in the same way.
