---
id: top5
title: The Siegel-Weil identity at s0, given the local action
kind: theorem
decl: PositivityTheory.Rg.Sw.Glob.top5
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.HolomorphicContinuation.GlobalGaussLaws.Top4
covers: 571
status: drafted
drafted_by: writer@claude
---
This theorem is the third step of the chain below [`top7`](/entry/top7/), called by [`top6`](/entry/top6/). It has the same conclusion as [`lit`](/entry/lit/). It adds one hypothesis, `LocInst`, and calls [`top3`](/entry/top3/). It only passes hypotheses along.

## Statement

The conclusion of [`top7`](/entry/top7/) (the Siegel Eisenstein series is holomorphic at $s_0$ with value the theta integral) holds if `LocFact`, `AwayAct`, `LieComm`, `DerivOne`, `GIdil` and `CoefND` hold. The first three are described in [`top6`](/entry/top6/), the last three in [`top7`](/entry/top7/).

## Proof

The proof is one line:

```
top3 hLF hAA (locInst_of_away hAA tensMem) hLC hDO hId hC
```

`locInst_of_away` proves `LocInst` from `AwayAct` and `tensMem`. `tensMem` says that a polynomial times a Gaussian at the place $\tau$, tensored with a function $\Psi$ of the away class, is in the Schwartz space and in the Fock space. `LocInst` says: for each family of local operators $L(y)$ at $\tau$ (`IsLocOp`), there is a linear map `sL` with $\mathrm{sL}(P)(y) = L(y)(f_P)(0)$, and an element $k$ of the maximal compact subgroup sends $f_P$ to $f_{\rho(k)P}$ for a linear map $\rho(k)$ on polynomials. Here $f_P$ is $P$ times the Gaussian (`fP`). It also fixes a signature $(p, q)$ with `GoodSig` and the local data `LocData`, which we have not unfolded.

## In the Lean code

The theorem is in [Top4.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Top4.lean#L6). `LocInst` and `TensMem` are in [FourierZeroN.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/FourierZeroN.lean#L114). The file is named `Top4`, but the theorem in it is `top5`; there is no `top4` in the chain.
