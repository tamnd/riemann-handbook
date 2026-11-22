---
id: desc-s
title: Descent of a conjugation-invariant cusp form from an imaginary quadratic field to the rationals
kind: theorem
decl: UpperTheory.ConvolutionTheory.RankTwoDescent.descS
module: Development.AutomorphicArithmetic.Foundations.Convolution.SplitEigenfunctions.AbsNormConj
covers: 1506
status: drafted
drafted_by: writer@claude
---
This theorem starts from a [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_2$ over an imaginary quadratic field $M$ whose Satake parameters do not change under the Galois conjugation. It gives a cuspidal representation of $\mathrm{GL}_2$ over $\mathbb{Q}$ with the same parameters at the split primes. In [the published hypotheses from patching](/entry/published-hypotheses-from-patching-alt/) it fills the field `cyc2` as the left case of `DescS ∨ Down2`. The main work is in [`downN`](/entry/down-n/), which does the same for a normalised representation.

## Statement

Let $M$ be a number field with $[M:\mathbb{Q}] = 2$ that is totally complex. Let `sat'` and `inf'` be the Satake parameters and the infinitesimal characters of a cuspidal representation $P$ of $\mathrm{GL}_2$ over $M$ (the predicate `IsCusp 2`). Suppose that the infinitesimal characters are regular (`RegInf`) and have a gap of at least 2 (`Gap2`). Suppose also that for cofinitely many primes $w$ of $M$, each prime $w'$ over the same rational prime has a common Satake parameter with $w$.

**Theorem.** There are a cuspidal representation $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$, with Satake parameters `sat` and infinitesimal characters `inf`, such that:

1. for cofinitely many primes $w$ of $M$ with $Nw = N(w \cap \mathbb{Z})$, the parameters of $\pi$ at $w \cap \mathbb{Z}$ are the parameters of $P$ at $w$ (`SplitBC`);
2. each infinitesimal character of $P$ at an embedding $\tau$ is an infinitesimal character of $\pi$ at $\tau$ restricted to $\mathbb{Q}$.

The statement has the shape of the descent half of quadratic base change for $\mathrm{GL}_2$ (R. P. Langlands, Base Change for GL(2), Annals of Math. Studies 96, 1980). The Lean proof does not use the trace formula. It goes through `downN`, which uses a theta lift.

## Proof

1. The predicate `IsCusp` has two cases: $M$ totally complex, or $M$ totally real. The second case is impossible, because $M$ has an infinite place that would be both real and complex.
2. The lemma `exists_twist_isNormalised` gives $s \in \mathbb{C}$ such that the twist $P \otimes |\cdot|^s$ is normalised.
3. The private lemma `absNorm_conj` shows that two primes of $M$ over the same rational prime have the same absolute norm. Its proof takes a Galois element that moves one prime to the other. So $|\cdot|^s$ has the same value at the two primes, and the twist is still conjugation invariant.
4. `downN` gives a cuspidal representation $\pi'$ over $\mathbb{Q}$ for the twist.
5. The answer is $\pi = \pi' \otimes |\cdot|^{-s}$. At a split prime $w$ the two twists cancel, because $Nw = N(w \cap \mathbb{Z})$ (the step `h7`). The infinitesimal characters move by $s$ and then by $-s$ (the lemmas `expo_absC`).

## In the Lean code

The theorem is at [line 40 of AbsNormConj.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/AbsNormConj.lean#L40), and `absNorm_conj` is at [line 30](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/AbsNormConj.lean#L30). The statement `DescS` and the predicate `SplitBC` are in [SplitDescentOfImagQuadDescent.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/SplitDescentOfImagQuadDescent.lean#L9). `IsCusp` is in [IsAlgChar.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/IsAlgChar.lean#L21).

The proof starts with `intro M _ _ h2 hM sat' inf' hc _ _ hi` (line 42). So the hypotheses `RegInf` and `Gap2` are never used. The branch for a totally real $M$ (lines 45 to 48) is dead code, because `DescS` asks for $M$ totally complex. The file name `AbsNormConj` names the helper lemma, not the theorem.
