---
id: dat-ext-rest
title: The rest of an adelic datum over an enlarged base, given its core
kind: theorem
decl: GlobalTheory.Mem.R3.Rw.datExt_rest
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsExtendedAdelicDataWithIntertwinersOverEnla
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem builds an adelic datum over an enlarged base around a core that is already given there. Its second name, [`exists_extendedAdelicData_with_intertwiners_over_enlargedCore`](/entry/exists-extended-adelic-data-with-intertwiners-over-enlarged-core/), is step 2 of [`exists_ext_build`](/entry/exists-ext-build/). That entry writes out the statement in full; this entry gives the proof. Below it are 347 declarations.

## Statement

Assume the seven published statements of the [second name](/entry/exists-extended-adelic-data-with-intertwiners-over-enlarged-core/), from `DiscreteSeriesCover` to `HarishChandraFinite`. Let $B \subset B'$ be bases with `Enl0 B B'`: the same underlying data and image of $K_s$, and the fields $L_{B,0}$ and $L_B$ inside those of $B'$. Let $w$ and $w'$ be pinned columns over them with the same frame and point, $z$ a fine adelic datum at a later stage of $w$, and $c'$ a core at a later stage $Z'$ of $w'$ that shares fourteen core parts with $z$ and meets the other conditions listed there.

**Theorem.** Eventually in the context (the form `StepW Pinned`), there is an adelic datum $z'$ at $Z'$ with core $c'$ such that `ExAt`, `InGeo`, `Std` and `ExtN z z'` hold. The last condition says that about thirty parts of $z'$ agree with those of $z$.

## Proof

The proof has three parts. `datExt_rest_of_parts` joins them.

1. **The real datum.** `exists_analyticData_enlargedBase_tupleFree`, a second name of `exists_realDat_keep_rsideW`, gives a finite set $X_g$ of characters, a trace datum, a real datum $R_0$ over the coefficient field of $c'$, and a group isomorphism $c_G$. They satisfy twelve conditions. The last is `RSideW z R_0`: $R_0$ agrees with the real datum of $z$.
2. **The pins.** `exists_characterisedData_weil_enlargedBase`, a second name of `WeilExt.exists_pins_rSide`, changes the trace and real data so that the pins, `ExAt` and the full agreement `RSide` hold.
3. **The geometric half.** `geometricHalf_to_analyticData_enlargedBase` gives a geometric half with `InGeo`. Its $v_0$, $j$, $\kappa$ and forms agree with those of $z$. It needs one more input: for each $\iota \colon L_B \to L_{B'}$ that commutes with the embeddings into $\mathbb{C}$, each vector of the space $W_K$ of the new real datum is the image under $\iota$ of a vector of $z$ at the same index. The lemma `RSideW.wk_image` proves this from the field `rI` of `RSideW`.

`datExt_rest_of_parts` then puts the parts into one datum $z'$ and checks `ExtN z z'` field by field. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean#L53). The assembly lemma is in [DatExtRestOfParts.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DatExtRestOfParts.lean#L28).

- `RSideW.wk_image` ([line 29](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean#L29)) has a vacuous branch. If no compatible $\iota$ exists, it takes $x = 0$, and the claim holds over an empty set of maps. Under `Enl0` such a map exists: `geometricHalf_to_analyticData_enlargedBase` builds it with `enlEmb`.
- [GeometricHalfToAnalyticDataEnlargedBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/GeometricHalfToAnalyticDataEnlargedBase.lean#L56) uses only `CuspRapidDecay` of the seven hypotheses. We did not check which hypotheses the other two parts use.
