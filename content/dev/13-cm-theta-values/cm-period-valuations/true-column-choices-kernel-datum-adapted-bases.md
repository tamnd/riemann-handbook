---
id: true-column-choices-kernel-datum-adapted-bases
title: A kernel datum with adapted bases for the true columns (second name)
kind: theorem
decl: GlobalTheory.T.trueColumnChoices_kernelDatum_adaptedBases
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TrueColumnChoicesKernelDatumAdaptedBasesStatement
covers: 516
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`kerEntC_true`](/entry/ker-ent-c-true/). It has the same statement, and its proof only calls `kerEntC_true`. All the content is in that entry. Its user is [the lattice layer with a kernel datum](/entry/gy-lay-ker-t-ent-c/), through the lemma that makes the kernel datum for the true columns.

## Statement

Take the data of a true column choice $I$ that satisfies `I.Ok` and the pin conditions, a law $l$ with a later datum $Z$, a divisor datum $Y$, lifts $O$ of the twisted theta objects and a choice of local places $P$ (`EntPl`). Suppose that the places of $Y$ are the ones that $I$ fixes, that $O$ is the standard object, that the unfolding conditions hold for each level $i < m$, and that the jets of $I$ are integral (`ColIn.JetsIn`).

**Theorem.** There are a family of matrices $B_w$ at the places $w$ and a proof $h$ of the kernel hypotheses `KerEntHyp` for $B$, such that the kernel entry `kerEntC` built from $h$ satisfies `EntOk`.

The objects are defined in the entry for [`kerEntC_true`](/entry/ker-ent-c-true/).

## Proof

The proof is `exact @GlobalTheory.Pdv.kerEntC_true`.

## In the Lean code

The theorem is at [TrueColumnChoicesKernelDatumAdaptedBasesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnChoicesKernelDatumAdaptedBasesStatement.lean#L13). Its only use that we found is in `gyLay_kerT_entC`, at [ExistsLatticeLayerKernelDatumTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLatticeLayerKernelDatumTrueColumns.lean#L30). The proof is a `first | exact ... | apply ...` block, a form that the code uses for second names.
