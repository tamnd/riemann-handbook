---
id: sharp-bound-stability-lattice-column-chain
title: The stability theorem for built chains
kind: theorem
decl: GlobalTheory.LvT.Built.Assemble.sharpBound_stability_latticeColumnChain
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.SharpBoundStabilityLatticeColumnChain
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem gives the sharp column bound `Conclusion5Sharp` and the stability of the forms `FormsStable` for the chain of a built datum. [The sharp bound at each tuple](/entry/true-columns-chain-last-step-sharp-bound/) calls it and keeps the first part. The proof only connects lemmas. It builds local point models at each level, then kernels between levels, and passes them to a general sharp bound.

## Statement

Let `B : Built.Dat D u` be a built datum with chain `B.ch`. Assume that each $A_i$ with $i \le m$ splits over $T$, that `B.Sees` holds, that each $i < m$ has a kernel with the five laws `KerEq`, `KerDil`, `KerUK`, `KerBar`, `KerP`, that $[E : \mathbb{Q}]\, N_m + 1 < T$, and that `WtSigns B.ch` holds. Then `Conclusion5Sharp B.ch` and `FormsStable B.ch` hold. The second says that each $U_v$ preserves $F_i$, the $U_v$ commute on $F_i$, and $K_T$ maps $F_i$ into $F_{i+1}$.

## Proof

1. For each $i \le m$, `exists_levelPrimePointModel_realisation` gives a point model `PtModel B.ch i` with a realisation. These form a level tie `Lv`.
2. For each $i \le m$, `exists_coordinates_valueLattices_eq_weylLattices` gives good coordinates whose value lattices match. This uses `Sees`. These form `Vt`.
3. For each $i < m$, `exists_pointKernel_realised_models` turns the kernel `k` into a point kernel `KerPt` between the models at $i$ and $i+1$, with `TgtEq`. These form `Kt`.
4. The structure `KerLaws Vt Kt` is filled field by field. Each of `KerDil`, `KerUK`, `KerBar` and `KerP` is moved from the coefficient kernel to the point kernel by its own lemma.
5. `formsStable_of_tgtEq` gives `FormsStable`. `levelChainUOperatorCommutation_of_pointPairLaw` gives $U_v K_T = T^{(t+1)/2} K_T U_v$.
6. `stabUnit_of_chainIn` uses the inequality to show that $T$ does not divide the order of any stabilizer (`StabUnit`). `wtBounds_of_nonneg` turns `WtSigns` into `WtBounds`.
7. `ukSharp` and `levelChainSharpColumnValuation_of_stability` give `Conclusion5Sharp`.

## In the Lean code

The theorem is at [SharpBoundStabilityLatticeColumnChain.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SharpBoundStabilityLatticeColumnChain.lean#L17). `FormsStable` is at [FormsStable.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/FormsStable.lean#L318), with `KerLaws` at line 233 and `StabUnit` at line 240. I have not unfolded `Split`, `Sees`, the five kernel laws, `PtModel` beyond its fields, or the lemmas of steps 1 to 4 and 7.

The proof makes a copy `hk` of the hypothesis `hker` at line 33 and uses only the copy. Steps 5 to 7 repeat the body of [levelChainSharpColumnValuation_of_pointKernelLiftLaws](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LevelChainSharpColumnValuationOfPointKernelLiftL.lean#L21). The file imports that lemma but does not call it. The repetition exists because that lemma returns only `Conclusion5Sharp`, and this theorem also returns `FormsStable`.
