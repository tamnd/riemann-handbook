---
id: top6
title: The Siegel-Weil identity at s0, from six inputs
kind: theorem
decl: PositivityTheory.Rg.Sw.Glob.top6
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.HolomorphicContinuation.GlobalGaussLaws.Top6
covers: 594
status: drafted
drafted_by: writer@claude
---
This theorem is the second step of the chain below [`top7`](/entry/top7/). It has the same conclusion: the Siegel Eisenstein series is holomorphic at $s_0$ with value the theta integral, as in [`lit`](/entry/lit/). It turns three of its hypotheses into three others and calls [`top5`](/entry/top5/). It only passes hypotheses along.

## Statement

The conclusion of [`top7`](/entry/top7/) holds if `FTfact`, `GenA`, `SchDeriv`, `DerivOne`, `GIdil` and `CoefND` hold. These are the three hypotheses of `top7` and the three facts that `top7` proves.

## Proof

The proof builds three statements about the action $\omega$ of $G$ on pure tensors $f \otimes \Psi$, where $f$ is the component at one archimedean place $\tau$:

- `AwayAct`, from `GenA`, `FTfact` and `decompAway`: an element that is trivial at $\tau$ acts only on $\Psi$;
- `LocFact`, from `decomp` and `opGen_of hF`: there is a family of operators $L(y)$ on Schwartz functions with $\omega(\iota(y))(f \otimes \Psi) = L(y)f \otimes \Psi$ for $y$ in the group at $\tau$;
- `LieComm`, from `awayIn`, `lNe`, `schFP`, `opCLM_of' hF`, `awayFact_of` and `SchDeriv`: $\omega(g)$ of the function with polynomial part $X \cdot P$ (`vfX`) is the derivative along $\exp(tX) \in \mathrm{U}(V)$ at $\tau$ of $\omega(g)$ of the function with polynomial part $P$.

Then it calls `top5` with these three, `DerivOne`, `GIdil` and `CoefND`.

## In the Lean code

The theorem is in [Top6.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Top6.lean#L12). `AwayAct` and `LocFact` are in [GaussLaw.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/GaussLaw.lean#L49), `LieComm` in [DerivOne.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/DerivOne.lean#L21). We have not unfolded `tens`, `AwayCls` or the bundle `Cx`, so the description of the pure tensors is read from the statements, not from their definitions. `GenA` and `FTfact` are used only to build `AwayAct`, and `FTfact` again in `opGen_of` and `opCLM_of'`.
