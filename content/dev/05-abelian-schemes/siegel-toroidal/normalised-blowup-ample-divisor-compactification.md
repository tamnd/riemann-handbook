---
id: normalised-blowup-ample-divisor-compactification
title: A normalized blowup with an ample twist, stated
kind: theorem
decl: GlobalTheory.T.normalisedBlowup_ampleDivisor_compactification
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormalisedBlowupAmpleDivisorCompactificationStatement
covers: 449
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is $\mathrm{PoinSt}$ and its proof is [`poinSt`](/entry/poin-st/), which has the real content. It is input 3 of [the toroidal compactification with polarized charts](/entry/siegel-toroidal-pol-charts/). Below it are 449 declarations.

## Statement

$\mathrm{PoinSt}$ is stated in full in [the proof entry](/entry/poin-st/). In short, let $i \colon X \to Z$ be a theta compactification of a Siegel moduli scheme of genus $g \geq 1$ and odd level $n \geq 3$, let $\mathcal{O}_Z(1)$ be ample, and let $\varphi$ be a polarization function for $g$. Then there are $d \geq 1$ and an ideal $J$ on $Z$ off $i(X)$ whose pullback along each trait has the valuation $d\varphi(\beta)$ (`ValOn`). A normalized blowup $\pi \colon S \to Z$ of $J$ is projective over $\mathbb{Z}[\zeta_n, 1/n]$, and $X$ is a dense open of $S$ through $j$, with $\pi \circ j = i$ and $\pi^{-1}(i(X)) = j(X)$. The divisor $B$ with $\mathcal{O}(-B) = J\mathcal{O}_S$ satisfies `ValOn` for $j$, and $\pi^*\mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ is ample for all large $k$.

## Proof

The proof is the term `GlobalTheory.PoincTop.poinSt`.

## In the Lean code

The theorem is in [NormalisedBlowupAmpleDivisorCompactificationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedBlowupAmpleDivisorCompactificationStatement.lean#L8). The proof is `first | exact @GlobalTheory.PoincTop.poinSt | ...`. `PoinSt` is in [IsThetaCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsThetaCompact.lean#L85). In [`poinSt`](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedBlowupAmpleDivisorCompactification.lean#L19), the hypothesis `hOZ : OZ.IsLB` is introduced but never used.
