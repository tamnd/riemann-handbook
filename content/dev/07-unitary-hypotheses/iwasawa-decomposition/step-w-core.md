---
id: step-w-core
title: A built core from a pinned level 4 object
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.CoreAsm.stepW_core
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsConstructedCoreOfAllConstructionStages
covers: 1473
status: drafted
drafted_by: writer@claude
---
This theorem is the last stage of the construction of a core. From a pinned level 4 object and the three existence conditions of a slot $\mathcal{S}$, it builds a core $c$ and a certificate that $c$ is built from $\mathcal{S}$. Its copy [`exists_constructedCore_of_all_construction_stages`](/entry/exists-constructed-core-of-all-construction-stages/) is called twice by [`memberE_of_steps2`](/entry/member-e-of-steps2/), once in each pass. Below this theorem are 1,473 declarations. The proof is assembly from the lemmas that it calls.

## Statement

Fix a context $K$, a base $B$ with frame $f$, a twist datum $T$ and column data $w$. A *stage choice* $Z$ of $w$ gives a datum $D = w.D(Z)$. A *level 4 object* $l$ at $Z$ collects the column data at split primes, a set $W_t$ of places, the rows with their character $\mu$, a choice of $n$, and the realness and volume identities. A *core* is a record `V4.Core` with 21 fields, and `Built` is a certificate with nineteen fields that ties the core to $l$ and to the slot $\mathcal{S}$. `BuiltE` asks in addition that the kernel datum of the certificate has the form `kerEntC`.

**Theorem.** Assume `SiegelMassRatioCM`. Let $\mathcal{S}$ be a slot with:

- `AmbEx 𝒮`: each level 4 object has ambient data $a, a_0$;
- `DivEx 𝒮`: each level 4 object has a divisor datum $Y$ with the condition `MjAre`, with $\kappa_R(\sigma) = \kappa^\sharp$ for all $\sigma$, and with a position object for each object over $Y$;
- `ThEx 𝒮`: each level 4 object has a theta datum.

Then eventually, at all large bases where `KPx` and the forced primes hold, each pinned $w$ with a level 4 object has a stage $Z$, a core $c$ and a certificate $b$ with `BuiltE`.

## Proof

Fix $w$ with a pin and a level 4 object $l$ at $Z$.

1. The three hypotheses give $a, a_0$, $Y$ with its divisor certificate, and a theta datum $\theta$.
2. `exists_latticeLayer_kernelDatum_trueColumns` gives a lattice instance $G_y$, a kernel family, the lattice layer condition, and a kernel certificate whose entries are `kerEntC`.
3. `GaugeEx.exists_isGauge` gives a gauge family for the CM extension of $D$.
4. These data form the object $O$. `DivEx` then gives a position object for $O$.
5. The core takes its fields from $l$, $O$ and the lemmas. Three fields need a short proof. `fval_off` says that the forced values vanish at places outside $W_t$. It uses `forcedContent_eq_scale_at_residueChar` and the identity that defines $W_t$ in $l$. `rowLay_of` builds the row layer. Its untwisted clause uses `not_mem_of_untw`: a place where the character is the untwisted one is not in $W_t$, by `TwFin.tw_fin`. The column field comes from `columnLayerConditions_trueColumns_laterStages`.
6. The certificate takes its fields from the pin, from $l$, and from the data of steps 1 and 2. The kernel entries of step 2 give `BuiltE`.

## In the Lean code

The theorem is in [ExistsConstructedCoreOfAllConstructionStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsConstructedCoreOfAllConstructionStages.lean#L67). The lemmas it calls:

- `fval_off`, `not_mem_of_untw` and `rowLay_of`, in the same file, lines 27, 43 and 55.
- `exists_latticeLayer_kernelDatum_trueColumns` in [ExistsLatticeLayerKernelDatumTrueColumnsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLatticeLayerKernelDatumTrueColumnsStatement.lean#L12).
- `GaugeEx.exists_isGauge` in [ExistsIsGaugeOfIsCMExt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L205).
- `columnLayerConditions_trueColumns_laterStages` in [ColumnLayerConditionsTrueColumnsLaterStagesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ColumnLayerConditionsTrueColumnsLaterStagesStatement.lean#L8).

The structures `Lv4` and `Built` are in [NonzeroPlacesOverPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L140), and `BuiltE` is in [ThetaChr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ThetaChr.lean#L85). We have not unfolded the fields of `V4.Core`, `Obj2` or the kernel certificate beyond their names.

The hypothesis `SiegelMassRatioCM` is named `_h2b` and is not used. The theorem holds without it. The field `forced` of the core is the forced primes hypothesis of the step itself, so the core records a condition of the base and not a new fact.
