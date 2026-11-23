---
id: twist-core-surjective-of-local-components
title: Lifts down the core column reach every core form
kind: theorem
decl: GlobalTheory.Twist.CoreOntoAssembly.twist_core_surjective_of_local_components
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistCoreSurjectiveOfLocalComponents
covers: 331
status: drafted
drafted_by: writer@claude
---
This theorem proves `CoreOnto`. Its second name [`twist_core_surjective`](/entry/twist-core-surjective/) is the form that [the separation of rows by real functionals](/proof/bessel-seesaw/) calls. The proof gives five facts to `coreChain_lifts_surjective_of_evenRank`.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/) and the eleven named literature statements listed in [the parent entry](/entry/twist-core-surjective/). Then `CoreOnto` holds.

`CoreOnto` is a statement of the form `Gap Q`. It says that $Q$ holds for each datum $D$ whose numbers `pde` and `pde'` are coprime to a fixed multiple of $q$ (`OffQ`) and that has the size data `Sizes`, and for each grid $G$ at gap constant 1 with Weil datum $W$ and row datum. The core column of $G$ has nodes $0, \ldots, m$, and a theta lift $\mathrm{dn}$ goes from node $i+1$ down to node $i$. $Q$ says this. Let $v$ be a volume datum on the core column. Let $\mathcal M$ be a discrete series model at core node 0 whose real datum `cart` is that of $W$. Then for each form $y$ in the multiplicity space `CoreForms` of $\mathcal M$ at the level of $G$, and each $x$ in the span `KF` of $K$-finite pure tensors, $y(x)$ is in the span of `Reach W v`.

A function $F$ on core node 0 is in `Reach W v` if there is a chain $\Psi_0, \ldots, \Psi_m$ of rapidly decreasing functions with $\Psi_0 = F$, $\Psi_i = \mathrm{dn}_i(f_i)(\Psi_{i+1})$ for Schwartz data $f_i$ that meet `Dep`, and $\Psi_m$ the pairing of a functional $\xi$ with a column value $c$ (`pairVec`). We have not unfolded `Dep`, the models or the multiplicity spaces.

## Proof

`coreChain_lifts_surjective_of_evenRank` gives `CoreOnto` from five facts.

1. `OntoAll D` for all $D$, from `twist_even_surjective_of_representatives` and all eleven named statements. It says that each composite of $k \le m$ lift steps between core stages is surjective.
2. `ComOK`, from `testGridCommonData_properties_hold`.
3. `StageOK`, from `testGridStageLatticesProperties_proof`: each core node has a lattice datum with valid stages.
4. `ChainEx`, from `core_chain_composites_exist_lift_combinations`. It uses `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay`, `CasselmanWallach`, the fact `dependence_fixed`, and `CoreModels` from `exists_separating_models`. It says that for each $k \le m$ there is a composite $\Theta$ of $k$ lift steps whose values on $K$-finite vectors lie in the span of the functions below level $k$ of the chain.
5. `TopCols`, from `definiteTopSpace_columnValues`: each form on the top core node $m$ is a pairing of a functional with a column value.

Facts 2, 3 and 5 have no hypothesis. `ThetaLocalInputs` enters only in fact 4, through `exists_separating_models`.

## In the Lean code

The theorem is in [TwistCoreSurjectiveOfLocalComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistCoreSurjectiveOfLocalComponents.lean#L15). `CoreOnto` is in [OffQOfSizeRows.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/OffQOfSizeRows.lean#L123), and the four other facts are in [IsCoreLat.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/IsCoreLat.lean#L114).

- Nine of the eleven named statements are also fields of `ThetaLocalInputs`, which is a hypothesis too. So they are redundant. Only `HoweUnram` and `SiegelWeilUnitaryConvergent` add something.
- The words "local components" do not match any part of the statement or the proof.
