---
id: exists-lattice-layer-kernel-datum-true-columns
title: A lattice instance and a kernel certificate, stated for the built core
kind: theorem
decl: GlobalTheory.T.exists_latticeLayer_kernelDatum_trueColumns
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsLatticeLayerKernelDatumTrueColumnsStatement
covers: 773
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`gyLay_kerT_entC`](/entry/gy-lay-ker-t-ent-c/). It has the same statement and its proof only applies that theorem. [The built core](/entry/step-w-core/) calls it in step 2, to get a lattice instance $G_y$, a kernel family and a kernel certificate for each pinned column datum. The mathematics is in [the entry for `gyLay_kerT_entC`](/entry/gy-lay-ker-t-ent-c/).

## Statement

`StepW Pinned q`: eventually, at all large bases where `KPx` and the forced primes hold, each pinned column datum $w$ satisfies $q$. Here $q(w)$ says: for each stage $Z$, column data $t$ at split primes, set of places $W_t$, tied choice and divisor datum $Y$ with `MuIsW` and `QpIs`, there are a lattice instance $G_y$ and a kernel family with `GyLay`, a kernel certificate `KerT`, and place data `Pl`, `Bs` with a proof $h$ of `KerEntHyp`, such that the entry datum of the certificate is `kerEntC Pl O Bs h`.

## Proof

The proof applies `GlobalTheory.Mem.Top.Bl.gyLay_kerT_entC`.

## In the Lean code

The theorem is in [ExistsLatticeLayerKernelDatumTrueColumnsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLatticeLayerKernelDatumTrueColumnsStatement.lean#L12). The proof is the tactic `first | exact @gyLay_kerT_entC | ...`, which tries three ways to apply the same theorem. The two statements are the same text. The file adds only a second name, in the namespace `GlobalTheory.T`.
