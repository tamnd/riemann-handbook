---
id: ind-cs-of-gm
title: Automorphic induction from the comparison of geometric sides
kind: theorem
decl: UpperTheory.V.Z.InvariantSubmoduleMonicPolynomial.E.indCs_of_gm
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.IwahoriHeckeInjectivity.IndCsOfBcfl
covers: 2022
status: drafted
drafted_by: writer@claude
---
This theorem proves the automorphic induction statement $\mathrm{IndCs}$ of [`indCs`](/entry/ind-cs/) from $\mathrm{GM}$, a comparison of the geometric sides of the twisted and the untwisted trace formula. The proof follows the plan of Arthur and Clozel (Ann. of Math. Stud. 120, 1989): first base change for cyclic extensions of prime degree, then automorphic induction for quadratic extensions. [`indCs_of_bcfl`](/entry/ind-cs-of-bcfl/) supplies $\mathrm{GM}$.

## Statement

Let $\mathrm{GM}$ be the following statement. Let $E/F$ be a cyclic extension of prime degree of totally complex fields, and $n \ge 1$. Fix a Galois twist $\theta$, a split place $q$ of $F$, and matching archimedean test functions (`ArchPair`). Then there is $\kappa > 0$ such that for all matching local data (`Loc`, with constants $c_v$ on a finite set $S$) and each $\nu$ with `Good ν`, the two geometric sides satisfy `GeoPair` with constant $\kappa \prod_{v \in S} c_v$. We have not unfolded `GeoPair`. Its name and its use in `CI` say that it is the equality of the geometric sides up to this constant.

**Theorem.** If $\mathrm{GM}$ holds, then $\mathrm{IndCs}$ holds.

## Proof

The proof is one line:

```
indCs (indNorm (coreInd cix hG (T.liftAll (T.liftStep (T.coreLift ci hG)))))
```

Read from the inside out, it has five steps.

1. **Spectral comparison.** `ci` proves `CI`: if the geometric sides agree up to $c$, then at parameters that satisfy `OffFam` (not unfolded) the twisted spectral trace over $E$ is $c$ times the spectral trace over $F$. `cix` proves `CIx`, a form for $\mathrm{GL}_4$ with one extra term. We have not unfolded the proofs of `ci` and `cix`.
2. **Base change of one summand.** `T.coreLift : CI → GM → CoreLift`. A summand of the spectrum over $F$ whose base-changed parameters satisfy `OffAll` has a $\theta$-stable summand over $E$ with those parameters.
3. **Base change for all $n$.** `T.liftStep : CoreLift → LiftStep`. If `LiftPlus` holds for all $m < n$, then each cuspidal $\pi$ on $\mathrm{GL}_n(F)$ either has a weak base change to an isobaric sum of at least two pieces, or lifts to a cuspidal $P$ on $\mathrm{GL}_n(E)$ that is stable under the Galois group. Then `T.liftAll` proves `LiftAll` by strong induction on $n$: each cuspidal $\pi$ has a weak base change to an isobaric sum over $E$.
4. **Induction of a swapped pair.** `coreInd : CIx → GM → LiftAll → CoreInd`. Let $E/F$ be quadratic and let $\tau_1, \tau_2$ be cuspidal on $\mathrm{GL}_2(E)$, exchanged by the Galois twist. Then there is a summand of the spectrum of $\mathrm{GL}_4$ over $F$ with infinitesimal characters $m_1 + m_2$ and Satake parameters $B_1 + B_2$ at almost all places.
5. **From pairs to one representation.** `indNorm : CoreInd → IndNorm`. `IndNorm` is $\mathrm{IndCs}$ for $\pi$ normalized (`IsNormalised`) and not isomorphic to its Galois conjugate. Then `indCs : IndNorm → IndCs` removes these two conditions. It twists $\pi$ by a Hecke character $\chi$ with `IsPow χ s` (not unfolded) so that $\pi \otimes \chi$ is normalized. The twist is not isomorphic to its conjugate (`not_conjIso`), since `MixWtC` makes the weights distinct. It applies `IndNorm` and twists the result back by $\chi_0^{-1}$, a character of $K$ with `IsPow χ₀ s`.

## In the Lean code

The theorem is in [IndCsOfBcfl.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IndCsOfBcfl.lean#L11). It calls:

- `E.indCs` in [NotConjIso.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/NotConjIso.lean#L186), `E.indNorm` in [IndNorm.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/IndNorm.lean#L92), `E.coreInd` in [CoreInd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/IwahoriHeckeInjectivity/IdempotentTraces/CoreInd.lean#L84).
- `T.coreLift`, `T.liftStep` and `T.liftAll`, with statements in [NormCharSplit.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/TraceSplitting/NormCharSplit.lean#L102).
- `ci` in [Ci.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/BlockEvaluation/Ci.lean#L23) and `cix` in [Cix.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/InductionEstimates/SpectralOperatorNorms/Cix.lean#L5).

The hypothesis $\mathrm{GM}$ is used twice, in `coreLift` and in `coreInd`. The theorem `E.indCs` has the same short name as [`Bc.indCs`](/entry/ind-cs/) but a different statement.
