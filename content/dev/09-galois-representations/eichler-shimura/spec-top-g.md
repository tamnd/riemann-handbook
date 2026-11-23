---
id: spec-top-g
title: Choice of the auxiliary prime and the type
kind: theorem
decl: UpperTheory.Gal.Spc.specTopG
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ScalarCommutation.SpecTopG
covers: 897
status: drafted
drafted_by: writer@claude
---
This theorem proves `SpecTopG` from `WtOf`. Its parent [specTop_holds](/entry/spec-top-holds/) only renames it. The proof makes two choices, an auxiliary prime $r$ and a type at $w_0$, and then gives the work to [specData](/entry/spec-data/). Below it are 897 declarations.

## Statement

`SpecTopG` is in [ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean#L139). Take a CM field $E$, arithmetic data $A$, an odd $n$, a prime $p$, a `Setup` $S$, a `Frame` $F$ and a vector datum $V$ : `Vec x U w₀ Up`. Assume `Sc S.D S.G`, `Gen A x` (so $x$ and $A.\omega$ generate the same field over $\mathbb{Q}$), `Off V p`, and that some good prime $q$ lies in $w_0$. Then for every finite set $X$ of primes there is a prime $r_0 \notin X$ with $r_0 \ne p$ such that the following holds. Let $N$ be a level with $r_0 \mid N$ such that every element of $K_N$ is `Stab`. Let $g_j$ : `Mem S.L N` be Hecke elements with numbers $\theta_j$, each pair passing `Seen F V r₀`. Then there is $f$ with `IsFnL S.L N f` and `Spec S.L V.lam K_N (g_j.fn) θ f`.

`Seen` has two cases: a deck element in $K_{r_0}$ with $\theta = 1$, or an operator $T_i$ at a free split place $w$ with $\theta$ given by the Satake parameters of $U$ at $w$. `IsFnL` asks that $f$ is in the Hecke algebra of $K_N$ and is supported on integral elements. `Spec` asks that the words in the $g_j$ applied to $f$ commute and that a weight-`V.lam` representation gives a nonzero trace for each eigencharacter. I have not unfolded the helpers of `Spec`.

## Proof

The proof is in [SpecTopG.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/SpecTopG.lean#L9).

1. `auxiliary_prime_holds` gives $r \notin X$ and a nonempty finite set $W$ of places with `SlopeTestRemainingChoices`: $r$ is prime, $r \ne p$, $A$ is good at $r$, $r$ is off `V.S`, and `Half r W` (each place above $r$ is $w$ or its conjugate for some $w \in W$, and the places of $W$ are pairwise apart). Take $r_0 = r$.
2. For a level $N$, `tyEx` gives local data $L$ and a type `Ty` at $w_0$ with `TyOK`. Thus `Ty.K₀` is $K_N$, and `Ty.K` holds the elements of level `lev V.S V.Kw` whose components at the places of $W$ are in the Iwahori subgroup.
3. `plTr` and `regTr` prove `Extra S F.j`: local components away from $p$, and regularity of `F.j g` when the characteristic polynomials at the places above $q$ are separable.
4. `specData` takes all of this and gives $f$.

## In the Lean code

The name `AuxiliaryInertOddPrime`, at line 87 of the statement file, says "inert" and "odd". The statement asks neither. The set $W$ consists of split places: it lies in `Spl E p`, the places with `IsSplitAt w` and $p \notin w$. The hypotheses `Odd n`, `Sc` and the prime $q$ only pass through to `specData`.
