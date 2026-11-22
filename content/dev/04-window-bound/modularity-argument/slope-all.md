---
id: slope-all
title: Slopes of Satake parameters at all places, from two literature hypotheses
kind: theorem
decl: UpperTheory.V.Z.Int.slopeAll
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.IntegralDeterminants.SlopeAll
covers: 2414
status: drafted
drafted_by: writer@claude
---
This theorem bounds the slopes of the Satake parameters of a polarized cuspidal representation of $\mathrm{GL}_n$ over a CM field, at every finite place where they are defined. It is used by `intP` and `intK` in the same file, below [the window from hypotheses H](/entry/vwin-of-hypotheses-h-e-alt/). The proof chains three lemmas. Most of the work is in [the extension from good representations to all of them](/entry/slope-all-of/).

## Statement

Let $E$ be a CM field, $n \ge 1$, and $m_1 > m_2 > \dots > m_n$ integers. Let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_E)$ with infinitesimal character given by $m$ at each embedding $E \to \mathbb{C}$, and polarized: there is a character $\chi$ with `PolarizedPair` $\pi$ $\chi$. Let $w$ be a finite place with norm $q$ at which $\pi$ has the Satake parameters $\alpha_1, \dots, \alpha_n$. Put $b_i = q^{(n-1)/2} \alpha_i$. `SlopeAll` says that for each $i$:

- $q^a b_i$ is an algebraic integer for each integer $a \ge \max_j m_j$;
- $q^a b_i^{-1}$ is an algebraic integer for each integer $a \ge -\min_j m_j$.

**Theorem.** Assume `QuadLift` and `DescOffT`. Then `SlopeAll` holds.

The two hypotheses are named statements from the literature. `QuadLift` says: for a quadratic extension $M/K$ of totally complex fields, a cuspidal $\pi$ on $\mathrm{GL}_a(\mathbb{A}_K)$ has a cuspidal lift to $\mathrm{GL}_a(\mathbb{A}_M)$, provided some place of $M$ that ramifies over $K$ lies over a place where $\pi$ has Satake parameters. `DescOffT` says: a conjugate self-dual $\pi$ with $\chi$ a power of the quadratic character matches an automorphic representation of a unitary group in $a$ variables, outside a finite set $T$ of non-split places that avoids any given finite set.

## Proof

The proof is one line:
```
slopeAllOf hL (slopeGood (slopeCsd hD))
```
Let `SlopeOn s` be the slope bound at the split places, for regular algebraic polarized $\pi$ in the class $s$. `slopeCsd` proves it for the class `csd` (conjugate self-dual with $\chi$ a power of the quadratic character) from `DescOffT`. `slopeGood` extends it to the class `good`: it twists $\pi$ by a character from `exists_good_conjSelfDual_twist_split_unramified` and moves the Satake parameters with `hasSatGL_twist`. [`slopeAllOf`](/entry/slope-all-of/) then removes the conditions on $\pi$ and on $w$. It uses `QuadLift` and calls `jacquetShalikaRigidity_holds` and `gelfandKazhdanDual_of_jacquetShalika`. We read only the first lines of its proof.

## In the Lean code

- The theorem is in [SlopeAll.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/SlopeAll.lean#L11). `SlopeAll` and `SlopeOn` are in [PlaceConjAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/PlaceConjAlt.lean#L97).
- `QuadLift` is in [IsWeight.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/IsWeight.lean#L90) and `DescOffT` in [MatchOfMatchOffTEmpty.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/MatchOfMatchOffTEmpty.lean#L32). We have not unfolded `IsLift`, `MatchOffT`, `Good` or `Slope`.
- The theorem only passes `hL` and `hD` along.
- In `intK` the polarization is supplied as the character $\mathrm{quadChar}^n$.
