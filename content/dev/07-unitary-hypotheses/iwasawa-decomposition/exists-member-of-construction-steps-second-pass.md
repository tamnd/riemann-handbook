---
id: exists-member-of-construction-steps-second-pass
title: The membership statement from the construction steps, as a statement file
kind: theorem
decl: GlobalTheory.T.exists_member_of_construction_steps_secondPass
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsMemberOfConstructionStepsSecondPassStatement
covers: 1732
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`memberE_of_steps2`](/entry/member-e-of-steps2/). It proves the membership statement `MemberE` for a slot $\mathcal{S}$ from four literature hypotheses and from construction steps for $\mathcal{S}$ and a second slot $\mathcal{S}'$. Its only user is [the membership statement from the construction steps](/entry/member-e-closing-alt-alt/), which calls it with $\mathcal{S}$ the slot of a parameter $p(N)$ and $\mathcal{S}'$ the slot of the refinement $p(N_g)$. All the content is in [`memberE_of_steps2`](/entry/member-e-of-steps2/). Below this theorem are 1,732 declarations, and 1,731 of them are below that theorem.

## Statement

The statement is word for word the statement of [`memberE_of_steps2`](/entry/member-e-of-steps2/). See that entry for the hypotheses and for the meaning of `MemberE`, `StepW`, `Pass` and the slot conditions. In short: if the four literature hypotheses hold, if the construction for $\mathcal{S}$ reaches level 3 and level 4, if the three existence conditions hold for $\mathcal{S}$ and for $\mathcal{S}'$, if the export and pass conditions hold, and if each object built from $\mathcal{S}'$ is a good object of $\mathcal{S}$ with all twists allowed, then `MemberE` $\mathcal{S}$ holds.

## Proof

The proof applies `memberE_of_steps2`. There is nothing else.

## In the Lean code

The theorem is in [ExistsMemberOfConstructionStepsSecondPassStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsMemberOfConstructionStepsSecondPassStatement.lean#L12). The proof on line 13 is

```
first | exact @GlobalTheory.Mem.Top.Bl.memberE_of_steps2 | ...
```

The first branch succeeds, because the two statements are the same. The other two branches are never needed. Line 11 sets `maxHeartbeats` to 1000000 for this one term.

The hypothesis `SiegelMassRatioCM` reaches [`stepW_core`](/entry/step-w-core/), which does not use it. `memberE_of_steps2` also uses it through `KPxCond.baseCond_KPx` and `PinW.step_pinned`, so it is not idle here.
