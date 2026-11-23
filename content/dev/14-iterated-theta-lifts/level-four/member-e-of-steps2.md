---
id: member-e-of-steps2
title: The four parts of membership from two passes of the construction
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.memberE_of_steps2
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsMemberOfConstructionStepsSecondPass
covers: 1731
status: drafted
drafted_by: writer@claude
---
This theorem proves the membership statement `MemberE` for a slot $\mathcal{S}$. It assembles the four parts of `MemberE` from four literature hypotheses and the construction steps for $\mathcal{S}$ and a second slot $\mathcal{S}'$. Its copy [`exists_member_of_construction_steps_secondPass`](/entry/exists-member-of-construction-steps-second-pass/) carries it to [the membership statement from the construction steps](/entry/member-e-closing-alt-alt/). Below this theorem are 1,731 declarations. Of these, 1,474 are below the core construction [`exists_constructedCore_of_all_construction_stages`](/entry/exists-constructed-core-of-all-construction-stages/).

## Statement

A *slot* $\mathcal{S}$ is a record of four position predicates. See [the member bundles entry](/entry/member-bundles-large-unramified-exponents-alt/) for slots and parameters. A *step* from $p$ to $q$ says: eventually in the context $K$, at all large bases $B$ with frame $f$ and twist datum $T$, if the base condition `KPx` holds and $T$ contains the forced primes, then $p$ implies $q$. `StepW p q` is the same for predicates on column data $w$, for all $w$. The levels `Has3` and `Has4` say that the construction from $w$ reaches stage 3 or stage 4.

**Theorem.** Assume the literature hypotheses `RayField`, `PrincipalIdealSt`, `CMCurveGoodOutsidePrimeSt` and `SiegelMassRatioCM`. Let $\mathcal{S}, \mathcal{S}'$ be slots. Assume:

1. `StepW Start (Has3 𝒮)` and `StepW (pinAnd (Has3 𝒮)) (Has4 𝒮)`: the construction for $\mathcal{S}$ goes from a start to level 3, and from a pinned level 3 to level 4;
2. `AmbEx`, `DivEx` and `ThEx` for $\mathcal{S}$: from a level 4 object there are ambient data, a divisor datum and a theta datum;
3. `ExportF` for the built cores of $\mathcal{S}$;
4. `Pass`: each built core of $\mathcal{S}$ that exports has an enlarged base where some column data start and reach level 3 for $\mathcal{S}'$;
5. the level 4 step and `AmbEx`, `DivEx`, `ThEx` for $\mathcal{S}'$;
6. each core built from $\mathcal{S}'$ is a good core of $\mathcal{S}$, and `DQ.TwAllAt` holds for its object.

Then `MemberE 𝒮` holds. By its definition in [ThetaChr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ThetaChr.lean#L102), this is the conjunction of `BaseCond KPx`, `FirstG`, `ExportF` and `SecondG`, for the slot of built cores `IsBuiltE 𝒮` and the slot of good cores `IsGoodE 𝒮`. We do not unfold `ExportAt`, `DQ.TwAllAt` or `GoodO`.

## Proof

The proof gives the four parts in order.

1. **Base condition.** `KPxCond.baseCond_KPx` gives `BaseCond KPx` from the four literature hypotheses.
2. **First pass.** `MemberEx2.step_start` is a step from untwisted $T$ to the existence of column data $w$ with `Start`. It uses `PinW.step_pinned`, `supp_of_untw` and `coh_of_untw`. `MemberEx2.stepW_builtE` chains the hypotheses for $\mathcal{S}$ from start to level 3, then level 4, then a built core. The last link is [`exists_constructedCore_of_all_construction_stages`](/entry/exists-constructed-core-of-all-construction-stages/). Then `step_hasCore` turns this into `FirstG`.
3. **Export.** `ExportF` is hypothesis 3, unchanged.
4. **Second pass.** The same chain for $\mathcal{S}'$ starts from `Start` and level 3 for $\mathcal{S}'$, and gives a core built from $\mathcal{S}'$. Hypothesis 6 makes it a good core of $\mathcal{S}$ with `TwAllAt`. `step_hasCore` gives a step to a core in this slot. `pass_step` composes hypothesis 4 with this step. The lemma `positionOf_ind` turns the slot into the three conditions of `SecondG`: built for $\mathcal{S}$, `TwAllAt`, and good for $\mathcal{S}$.

## In the Lean code

The theorem is in [ExistsMemberOfConstructionStepsSecondPass.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsMemberOfConstructionStepsSecondPass.lean#L38). The lemmas it calls:

- `MemberEx2.step_start` and `MemberEx2.stepW_builtE`, in the same file, lines 20 and 28.
- `KPxCond.baseCond_KPx` in [ExistsPrePin.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsPrePin.lean#L30).
- `step_hasCore` and `positionOf_ind` in [PositionOfIntro.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/PositionOfIntro.lean#L123).
- `pass_step` in [PassStepCongr.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PassStepCongr.lean#L16).

The third part of `MemberE`, `ExportF`, is a hypothesis that the proof returns unchanged (line 61). So export is a duty of the caller. "Second pass" is the second run of the construction, through $\mathcal{S}'$. The folder name, Iwasawa decomposition, matches nothing in this statement.
