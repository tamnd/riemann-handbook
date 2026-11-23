---
id: kernel-entry-hyp-of-true-column-choices
title: The kernel entry conditions, stated for true column choices
kind: theorem
decl: GlobalTheory.T.kernelEntryHyp_of_trueColumnChoices
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.KernelEntryHypOfTrueColumnChoicesStatement
covers: 403
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`kerEntHyp_true`](/entry/ker-ent-hyp-true/). It has the same statement and its proof only applies that theorem. The mathematics is in [the entry for `kerEntHyp_true`](/entry/ker-ent-hyp-true/).

## Statement

For true column choices $I$ with `I.Ok` and the pins, a divisor datum $Y$, lift objects $O$, place embeddings `Pl` and place matrices `Bs`: if the primes of $Y$ are those of $I$, $O$ is standard and unfolded, `BasOk` holds, the entries of `Bs` at level free places come from the coefficient field, and the jets of $I$ lie in the right space, then `KerEntHyp Pl O Bs Y (I.tw l l0 Z)` holds.

## Proof

The proof applies `GlobalTheory.Mem.Col2.TC.kerEntHyp_true`.

## How the parent uses it

[`kerEntC_true`](/entry/ker-ent-c-true/) first builds adapted bases with `AdaptedBases.exists_sys`. It calls this theorem for the matrices of those bases, with entries mapped by `tauEmb`, and gets `KerEntHyp` for them. Then it rescales the matrices by the units `adUnit` with `KerScale.scB`, and moves the conditions to the new matrices with `KerScale.kerEntHyp_scB`.

## In the Lean code

The theorem is in [KernelEntryHypOfTrueColumnChoicesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/KernelEntryHypOfTrueColumnChoicesStatement.lean#L11). The proof is the tactic `first | exact @kerEntHyp_true | ...`. The call is at [TrueColumnChoicesKernelDatumAdaptedBases.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnChoicesKernelDatumAdaptedBases.lean#L227).

The hypothesis on the entries of `Bs` covers levels $i \le m$, which are the levels $i$ and $i + 1$, $i < m$, that `KerEntHyp` uses.
