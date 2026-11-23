---
id: chain-twist-places-integral-peel-of-doubling
title: Peeling the twist places off the doubling integral, the statement form
kind: theorem
decl: GlobalTheory.T.chainTwistPlacesIntegralPeel_of_doubling
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ChainTwistPlacesIntegralPeelOfDoublingStatement
covers: 401
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`qPeel_holds`](/entry/q-peel-holds/) and proves it by calling that theorem. Its only user is [`scalars_of_given_all`](/entry/scalars-of-given-all/), which feeds it into `thetaLiftChainStep_exact_innerProduct`.

## Statement

**Theorem.** Assume `UnramifiedDoublingGL` and `CuspRapidDecay`. Then `QPeel D` holds for every datum $D$.

`QPeel D` says: at each step of a twisted theta chain, if the doubling integrand is integrable on the level set, then it is integrable on the set of elements that are integral off $S$. At the point $z = t/2$, its integral over that larger set is the product over the twist places $\mathfrak P$ of `blockL c k 𝔓 * zinv 𝔓 t ((k+1)t)` times its integral over the level set.

`UnramifiedDoublingGL` is a hypothesis that computes the unramified doubling integral of a zonal spherical function of $\mathrm{GL}_n$ over a $p$-adic field, for a representation with Satake parameters $\alpha$, as a product of two local $L$-factors and a normalising factor. `CuspRapidDecay` says that smooth cusp forms of moderate growth decay rapidly.

## Proof

The proof is `first | exact @GlobalTheory.ChainTw.Peel.qPeel_holds | ...`. It applies that theorem. The statements are identical.

## In the Lean code

The theorem is in [ChainTwistPlacesIntegralPeelOfDoublingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainTwistPlacesIntegralPeelOfDoublingStatement.lean#L21). `QPeel` is in [IsLevMeas.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsLevMeas.lean#L159). `UnramifiedDoublingGL` is in [PairwiseDisjointCell.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/PairwiseDisjointCell.lean#L314) and `CuspRapidDecay` in [ExistsNormLeHeightPow.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsNormLeHeightPow.lean#L28).
