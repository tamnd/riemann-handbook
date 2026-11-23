---
id: cusp-step-of-large-flip-run
title: Theta lifts along the arrows of the grid keep cusp forms
kind: theorem
decl: GlobalTheory.FlipRun.cuspStep_of_large_flipRun
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.CuspStepOfLargeFlipRun
covers: 1474
status: drafted
drafted_by: writer@claude
---
This theorem says that each theta lift along an arrow of the grid of Hermitian spaces converges on cusp forms and gives a cusp form again. It is used below [the row properties of the theta lift](/entry/theta-lift-row-properties-conj/): directly by `theta_tower_first_occurrence_exists`, and through a copy with the same statement in three files on flips and iterated lifts. The proof is a case split into right arrows and down arrows. The analytic content is in [the smooth form of the lift property](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/). Below this theorem are 1,474 declarations.

## Statement

Let $\mathcal L$ be the statement `LiftsCuspidal`: for theta kernels made from Fock vectors, the theta lift maps cusp forms on each node of a grid to cusp forms on the next node. Let $F$ be the record [ThetaLocalInputs](/step/theta-local-inputs-def/).

**Theorem.** Assume $\mathcal L$ and $F$. There is $C_{F,0}$ such that for each $\varepsilon$ and each $C_F \ge C_{F,0}$ there is $x_0$ with this property. Take a datum $D$ with size data of parameter $\varepsilon$ and $x \ge x_0$, a face in a Hida setting, and a choice $\mathrm{ch}$ that is admissible at scale $C_F$. For each index $t$, let $M$ be a measure datum (a Haar measure $\nu_X$ and a fundamental domain $\mathcal F_X$ on each node $X$) that is correct at $t$. Let $m$ be the parameter `D.R.m`, and let $a$ be a grid arrow: from node $(i,j)$ to $(i+1,j)$ with $i < m$, $j \le m$, or from $(i,j+1)$ to $(i,j)$ with $i \le m$, $j < m$. Let $K$ be the theta kernel of $a$ for a Fock vector $f_Q$ (a local vector $f$ at an idempotent sum $e$ of local places, times a polynomial $Q$). Let $\varphi$ be a smooth automorphic cusp form on the source of $a$ that is "listed". Then $g \mapsto K(g,h)\varphi(g)$ is integrable on $\mathcal F_{\mathrm{src}}$ for each $h$, and

$$h \mapsto \int_{\mathcal F_{\mathrm{src}}} K(g,h)\,\varphi(g)\,d\nu_{\mathrm{src}}(g)$$

is a smooth automorphic cusp form on the target that is listed.

We do not unfold the Hida setting, the admissible choice, the local vectors or the listed condition.

## Proof

1. [The lift property on all theta functions](/entry/cuspidal-lift-smooth-at-cusps/) turns $\mathcal L$ and $F$ into `LiftsCuspidalSmoothAt D` for every $D$.
2. `cusp_transition_rightward` proves the claim for right arrows. It builds a grid from the choice and uses the right arrow field of the smooth lift property.
3. `flipRun_descending_cusp_transition` does the same for down arrows.
4. `RowClaim.Big.and` joins the two claims, with the maximum of the constants. A grid arrow is right or down, so one claim applies.

## In the Lean code

The theorem is in [CuspStepOfLargeFlipRun.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/CuspStepOfLargeFlipRun.lean#L15). The claim is `CuspStep` in [RangeSndRel.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RangeSndRel.lean#L146). The quantifiers over scales are `RowClaim.Big` in [FormulaAt.lean](lean:Development/AbelianVarietyTheory/Statements/HeckeThetaIntegrals/FormulaAt.lean#L68). The two case lemmas are copies of `RightArrowCusp.cuspStep_rightward` and `FlipRun.cuspStep_down_of_large_flipRun`.

Three points are odd. The word "large" in the name does no work: both case lemmas take $C_{F,0} = 0$ and $x_0 = 0$, so the claim holds at every scale. The same file has `GlobalTheory.T.flipRun_cusp_transition` (line 34), with the same statement and a proof that only applies this theorem. The hypothesis $\mathcal L$ is not a new assumption of the trunk: `twisted_thetaLift_cuspidal` proves it from $F$.
