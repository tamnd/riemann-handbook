---
id: injective-decomposition-action-holds
title: The injectivity, decomposition and action package for the nilradical
kind: theorem
decl: PositivityTheory.RgBcC.RealD.injective_decomposition_action_holds
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.RealDescent.RealLeviDescent.InjectiveDecompositionActionHolds
covers: 545
status: drafted
drafted_by: writer@claude
---
This theorem only assembles six proved statements into a conjunction. The real content is in those statements, and the place where the conjunction is used is [the multiplicity formula](/entry/multiplicity-formula-holds/), which also fixes the notation: letters, $\mathfrak{u}_\ell$, the chain space $C(V)$ and its boundary $\partial$.

## Statement

`InjectiveDecompositionAction` is `InjUU ∧ HCdecL ∧ ActUU`:

- `InjUU`: for $u \in V_{\mu_\ell}$, if $u \otimes \omega_U$ is the boundary of a chain of degree $|\omega_U| + 1$ on letters in $\mathfrak{u}_\ell$, then $u = 0$.
- `HCdecL`: each word that commutes with all $K_{cd}$ is congruent, modulo $\mathfrak{u}_\ell$, to a word in the Levi letters that commutes with the Levi $K_{cd}$.
- `ActUU`: steps 2 and 3 of [the multiplicity formula](/entry/multiplicity-formula-holds/).

## Proof

`injective_decomposition_action_of` takes `BdSqL` ($\partial^2 = 0$), `VanKL` (exactness of the $K$-part of $\partial$ in one weight), a map from these two to `InjRL`, a map from `InjRL` to `InjUU`, `HCdecL` and `ActUU`, and returns the triple. `HCdecL` comes from `HCdecLv` by `hcdecL_of`. All six inputs are `GlobalTheory.T` statements whose proofs we have not unfolded.

## In the Lean code

The theorem is at [InjectiveDecompositionActionHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/InjectiveDecompositionActionHolds.lean#L11), and the definitions at [InjectiveDecompositionAction.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/RealLeviDescent/InjectiveDecompositionAction.lean#L77). The same file declares `hc_decomposition_levi_holds`, which is `HCdecLv`.

The middle part `HCdecL` is never read: the users take parts 1 and 3, and `multFor_of` uses `hc_decomposition_levi_holds` instead.
