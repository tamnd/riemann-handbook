---
id: global-theory-t-has-proper-smooth-dual-representative-noetherian-induction-2
title: The inductive step for the dual abelian scheme (second name)
kind: theorem
decl: GlobalTheory.T.hasProperSmoothDualRepresentative_noetherian_induction
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasProperSmoothDualRepresentativeNoetherianInducTer
covers: 662
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`DualCon.Step.step`](/entry/step-step/), with the same statement. It is the inductive step of the noetherian induction in [`DualConFT.hasRep_of_finiteType`](/entry/has-rep-of-finite-type/). Two lemmas use it, both in that file: `hasRep_quot`, which runs the induction, and `hasRep_of_finiteType`, which applies the step once more to the ring itself.

## Statement

**Theorem.** Let $R$ be a commutative ring of finite type over $\mathbb{Z}$, let $A \to \operatorname{Spec} R$ be an abelian scheme, smooth of relative dimension $g$. Suppose that for each ideal $J \neq 0$ of $R$, $A$ has a dual of dimension $g$ over $\operatorname{Spec} R/J$. Then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$ over $S'$" is `HasRep A g S'`, defined in [`hasRep_affineOpen`](/entry/has-rep-affine-open/). Over $\operatorname{Spec} R/J$ it asks for a dual of the restriction of $A$ to $\operatorname{Spec} R/J$, proper, smooth and geometrically connected.

## Proof

The proof is the single tactic

```
first | exact @GlobalTheory.DualCon.Step.step | ...
```

so the theorem is `DualCon.Step.step` under another name.

## In the Lean code

The theorem is at [HasProperSmoothDualRepresentativeNoetherianInducTer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeNoetherianInducTer.lean#L10). It has the option `maxHeartbeats 1000000`, which a one-line proof does not need.

The names are confusing:

- The name says "noetherian induction", but the statement is only the inductive step. The induction is `hasRep_quot` in [`hasRep_of_finiteType`](/entry/has-rep-of-finite-type/).
- A different theorem, `GlobalTheory.T.hasProperSmoothDualRepresentative_noetherianInduction` (camel case, in `HasProperSmoothDualRepresentativeNoetherianInducStatement.lean`), has a stronger hypothesis: $R$ is reduced and an affine open of $A$ meets every fibre. It is a second name of `GlobalTheory.DualConStep.step`, which differs from `GlobalTheory.DualCon.Step.step` by one dot. The proof of [`step`](/entry/step-step/) calls the camel-case theorem.
