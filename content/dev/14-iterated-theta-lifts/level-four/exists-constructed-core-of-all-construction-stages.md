---
id: exists-constructed-core-of-all-construction-stages
title: A built core from a level 4 object, as a statement file
kind: theorem
decl: GlobalTheory.T.exists_constructedCore_of_all_construction_stages
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsConstructedCoreOfAllConstructionStagesStatement
covers: 1474
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`stepW_core`](/entry/step-w-core/). It says that, for a slot $\mathcal{S}$ with the three existence conditions, a pinned level 4 object of the construction gives a core and a certificate that the core is built from $\mathcal{S}$. Its user is [`memberE_of_steps2`](/entry/member-e-of-steps2/), which calls it twice: once for $\mathcal{S}$ in the first pass, and once for $\mathcal{S}'$ in the second pass. All the content is in [`stepW_core`](/entry/step-w-core/). Below this theorem are 1,474 declarations, and 1,473 of them are below that theorem.

## Statement

**Theorem.** Assume `SiegelMassRatioCM`. Let $\mathcal{S}$ be a slot, and assume `AmbEx 𝒮`, `DivEx 𝒮` and `ThEx 𝒮`. Then

```
StepW (pinAnd (Has4 𝒮)) (HasC (BuiltE 𝒮))
```

holds: eventually, at all large bases, each column data $w$ that is pinned and has a level 4 object has a core $c$ and a certificate that $c$ is built from $\mathcal{S}$, with the kernel of the certificate of the form `kerEntC`. The terms are explained in the entry for [`stepW_core`](/entry/step-w-core/).

## Proof

The proof applies `stepW_core`. There is nothing else.

## In the Lean code

The theorem is in [ExistsConstructedCoreOfAllConstructionStagesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsConstructedCoreOfAllConstructionStagesStatement.lean#L12). The proof on line 13 is

```
first | exact @GlobalTheory.Mem.Top.Bl.CoreAsm.stepW_core | ...
```

The first branch succeeds, because the two statements are the same. Line 11 sets `maxHeartbeats` to 1000000 for this one term.

The hypothesis `SiegelMassRatioCM` is idle. `stepW_core` takes it as `_h2b` and its proof does not use it. So the theorem holds without it.
