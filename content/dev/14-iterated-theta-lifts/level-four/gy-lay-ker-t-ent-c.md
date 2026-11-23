---
id: gy-lay-ker-t-ent-c
title: A lattice instance and a kernel certificate with explicit entries
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.gyLay_kerT_entC
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsLatticeLayerKernelDatumTrueColumns
covers: 772
status: drafted
drafted_by: writer@claude
---
This theorem builds, for each pinned column datum, a lattice instance $G_y$, a kernel family, and a kernel certificate whose entry datum is the explicit one `kerEntC`. Through its copy [`exists_latticeLayer_kernelDatum_trueColumns`](/entry/exists-lattice-layer-kernel-datum-true-columns/), it is step 2 of [the built core](/entry/step-w-core/). The proof is assembly from five lemmas.

## Statement

We use the words of [the built core](/entry/step-w-core/). `StepW Pinned q` says: eventually in the context $K$, at all large bases where `KPx` and the forced primes hold, each pinned $w$ satisfies $q$. A pin (`ColPin`) records that $w$ is twisted, that its jets lie in the right space, and other facts.

**Theorem.** `StepW Pinned q`, where $q(w)$ says: for each stage $Z$, column data $t$ at split primes, set of places $W_t$, tied choice `nch` and divisor datum $Y$, if the character $\mu$ is given by $W_t$ (`MuIsW`) and the primes of $Y$ are those of the ideals of $w$ (`QpIs`), then there are:

- a lattice instance $G_y$ and a kernel family with `GyLay`: the ramified part of $G_y$ is spanned by the image of the ramified subspace under the comparison map, the fill weights are the given ones, and $G_y$ is tied to the canonical instances;
- a kernel certificate `KerT`: lift objects $O$, an entry datum $E$ with `EntOk`, and at each word $u$ and place $v$ a kernel that agrees with $E$, is symmetric and is positive;
- place embeddings `Pl`, place matrices `Bs` and a proof $h$ of `KerEntHyp` with $E = $ `kerEntC Pl O Bs h`.

## Proof

1. `columnChoice_cloudBound_le_cG` adds a cloud bound $c \le c_G(L)$ to the hypotheses.
2. `TC.lift_objects` gives $O$. `Pl` is chosen from `entPl_nonempty`.
3. [`trueColumnChoices_kernelDatum_adaptedBases`](/entry/true-column-choices-kernel-datum-adapted-bases/) gives `Bs`, $h$, and `EntOk` for `kerEntC`. It uses the jets field of the pin.
4. `latticeLayer_trueColumns_intrinsic` gives the vertex map, the fills and the tie to canonical instances.
5. `levels_kernelData_at_served_place` gives at each $(u, v)$ kernel data that agree with $E$.

Then $G_y$ is `withFirst` of these data: its chains come from the comparison maps of the kernel data. The kernel family is `kerAll` of the kernel data. The last equation holds by definition.

## In the Lean code

The theorem is in [ExistsLatticeLayerKernelDatumTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLatticeLayerKernelDatumTrueColumns.lean#L21). `GyLay` is in [AmbientBaseHeq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/AmbientBaseHeq.lean#L30); `KerT` and `Pinned` are in [TiedColumnData.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TiedColumnData.lean#L111); `KerEntHyp` and `kerEntC` are in [KerEntHyp.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/KerEntHyp.lean#L149) (described in [the entry for `kerEntHyp_true`](/entry/ker-ent-hyp-true/)); `withFirst` and `kerAll` are in [ComparisonZeroEmbedding.lean](lean:Formalism/LocalToGlobal/GroupLattices/ComparisonMaps/ComparisonZeroEmbedding.lean#L188).

The proof first writes $G_y$ with the zero chain and the zero ramified part. `withFirst` replaces both, so these placeholders do not reach the result. `Pl` comes from `Classical.choice`. We have not unfolded `ThAtServed` or `LatTied`.
