---
id: siegel-weil-std-mid-k
title: The Siegel-Weil formula from the Weyl action, polynomial vectors and the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilFinMid
covers: 810
status: drafted
drafted_by: writer@claude
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd_k` from four hypotheses. Its user is [`siegelWeilStd_pre_k`](/entry/siegel-weil-std-pre-k/), which proves the first three. The fourth, `CTSplit_k`, comes from [`ctSplit_of_k`](/entry/ct-split-of-k/). The theorem is an assembly step. It proves four more inputs and passes everything to [`siegelWeilStd_of_k`](/entry/siegel-weil-std-of-k/), which has the main argument. Below it are 810 declarations.

## Statement

**Theorem.** Suppose that `TWeyl_k`, `KFinPoly_k`, `LDEx_k` and `CTSplit_k` hold. Then `SiegelWeilStd_k` holds.

The [parent entry](/entry/siegel-weil-std-pre-k/) states the first three: the action of the Weyl element on the transform $T\Phi$, the fact that $T\Phi$ lies in `R.fock` for $K$-finite $\Phi$, and the lower rank datum for $n \geq 2$. [The constant term entry](/entry/siegel-weil-std-of-ct-k/) states `CTSplit_k`.

## Proof

Put $h_T$ = `tAll_of_k hW`. This is `TAll_k`, the five properties of $T$ of Step 2 of the [Siegel-Weil chapter](/proof/siegel-weil/). Then the proof calls `siegelWeilStd_of_k` with these new inputs:

1. `LocInst_k`, from `locInst_of_k`. For each local operator $L$ at an infinite place $w$ there are a signature $(p, q)$ and a local datum `LocData`, and $L$ acts on polynomial vectors through a map $\rho$ on $K$. The lemma calls `KLI.locInst_of_k` with `auxiliaryExistence_holds`, `fockMem_k` and `liftEx_k`.
2. `GIdil_k`, from `Kdil.gIdil_full_k`. Along a path of dilations $a(t)$ at $w$, the function $t \mapsto I(\varphi(1))(g\,\iota_w(y\,a(t)))$ extends to a holomorphic function on an open set that contains the real line.
3. `PolyKFin_k`, from `KK.polyKFin_of_k`. If $T\Phi$ lies in `R.fock`, then $\Phi$ is $K$-finite. This is the converse of `KFinPoly_k`.
4. `HolLead`, from `HSt.holLeadB`. This is the holomorphy at $s_0$ of Step 6 of the chapter. It is shared with the copy without `_k`.

The hypotheses `KFinPoly_k`, `LDEx_k` and `CTSplit_k` go to `siegelWeilStd_of_k` unchanged. We have not opened the proofs of the four lemmas above.

## In the Lean code

The theorem is in [SiegelWeilFinMid.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinMid.lean#L23), and `locInst_of_k` at [L22](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinMid.lean#L22). The properties are in [SiegelWeilDatumProperties.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilDatumProperties.lean#L158). The term `locInst_of_k hT` occurs twice: once as an argument, and once inside the proof of `GIdil_k`. The theorem is a copy of [`siegelWeilStd_mid`](/entry/siegel-weil-std-mid/) with `_k` added to each name.
