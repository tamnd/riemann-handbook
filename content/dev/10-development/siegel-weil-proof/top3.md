---
id: top3
title: The Siegel-Weil identity at s0, with the theta integral automorphic
kind: theorem
decl: PositivityTheory.Rg.Sw.Glob.top3
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.HolomorphicContinuation.GlobalGaussLaws.VanishTop2
covers: 385
status: drafted
drafted_by: writer@claude
---
This theorem is the fourth step of the chain below [`top7`](/entry/top7/), called by [`top5`](/entry/top5/). It has the same conclusion as [`lit`](/entry/lit/). It proves that the theta integral is automorphic and calls [`top2`](/entry/top2/). It only passes hypotheses along.

## Statement

The conclusion of [`top7`](/entry/top7/) (the Siegel Eisenstein series is holomorphic at $s_0$ with value the theta integral) holds if `LocFact`, `AwayAct`, `LocInst`, `LieComm`, `DerivOne`, `GIdil` and `CoefND` hold. These are the hypotheses of [`top5`](/entry/top5/) and `LocInst`.

## Proof

The proof is one line:

```
top2 hLF hAA hLi (GlobalTheory.T.theta_automorphic_of_convergence wtc) hLC hDO hId hC
```

The new input is `ThetaAuto`: under `Std` and `InRange`, the theta integral $g \mapsto I(g)$ is continuous and left invariant under $G(F)$. `theta_automorphic_of_convergence` proves it from `wtc`, which says that the theta integral converges absolutely, for $n \ge 1$, when $V$ has Witt index $0$ or $n + r < m$.

## In the Lean code

The theorem is in [VanishTop2.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/VanishTop2.lean#L19). `ThetaAuto` is in [CoefDataExists.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/UnitarySchrodingerModel/CoefDataExists.lean#L70), and `theta_automorphic_of_convergence` in [ThetaAutomorphicOfConvergenceStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ThetaAutomorphicOfConvergenceStatement.lean#L14). The latter is a restatement of `ThetaAutoPf.thetaAuto`, proved by `first | exact …`; we have not opened that proof. `wtc` is in [Wtc.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Wtc.lean#L6).
