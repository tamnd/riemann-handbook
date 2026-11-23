---
id: top2
title: The Siegel-Weil identity at s0, the last step before the main argument
kind: theorem
decl: PositivityTheory.Rg.Sw.Glob.top2
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.HolomorphicContinuation.GlobalGaussLaws.VanishTop2
covers: 327
status: drafted
drafted_by: writer@claude
---
This theorem is the last step of the chain below [`top7`](/entry/top7/), called by [`top3`](/entry/top3/). It has the same conclusion as [`lit`](/entry/lit/). It adds three proved inputs and calls `top`, where the argument starts. It only passes hypotheses along.

## Statement

The conclusion of [`top7`](/entry/top7/) (the Siegel Eisenstein series is holomorphic at $s_0$ with value the theta integral) holds if `LocFact`, `AwayAct`, `LocInst`, `ThetaAuto`, `LieComm`, `DerivOne`, `GIdil` and `CoefND` hold. These are the hypotheses of [`top3`](/entry/top3/) and `ThetaAuto`, the automorphy of the theta integral.

## Proof

The proof is `top absThm hLF hAA hLi hTA hLC hDO hId eisStrong hC wtc`. The three added inputs:

- `absThm` (`AbsThm`, proved in the same file from `lv`, `cyc_of fft`, `lc_of fft` and `nullIff`): given local data (`LocData`) and global data on a group (`GlobData`), neither unfolded here, the Eisenstein series of each section $\mathrm{sec}(P)$ is holomorphic at $s_0$ with value $I(P)$.
- `eisStrong` (`EisStrong`): for each section, there are an open domain $U \ni s_0$ that contains a right half-plane, a nonzero polynomial $d$ and a function $E(z, g)$ holomorphic in $z \in U$ and left invariant under $G(F)$, with $E(z, g) = d(z)$ times the Eisenstein series where it converges, with bounds uniform on compact sets.
- `wtc`: the theta integral converges absolutely.

`top` passes these, with many proved lemmas, to `main`, a statement with 19 hypotheses.

## In the Lean code

The theorem is in [VanishTop2.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/VanishTop2.lean#L13). `top` is in [VanishTop.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/VanishTop.lean#L22), and `main` (of type `MainSt`, [ConvRight.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/ConvRight.lean#L41)) in [PhiSVal.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/PhiSVal.lean#L94). We have not opened the proof of `main`. `AbsThm` is in [GlobData.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobData.lean#L91) and `EisStrong` in [FourierZeroN.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/FourierZeroN.lean#L161). The file name `VanishTop2` does not describe its content: none of its three theorems states a vanishing.
