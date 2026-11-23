---
id: jet-table-bound-split-prime
title: The jet bound at split primes for ambient kernels (restatement)
kind: theorem
decl: GlobalTheory.T.jetTableBound_splitPrime
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JetTableBoundSplitPrimeStatement
covers: 319
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`jetSplitAmb_holds`](/entry/jet-split-amb-holds/), with the same statement `JetSplitAmb`. Its user is [`row_aAtG_of_rowPin`](/entry/row-a-at-g-of-row-pin/), which gives it as the hypothesis `JetSplitAmb` of `row_atG_pinned`. The content is in [`jetAtSplit_ambOf`](/entry/jet-at-split-amb-of/), which `jetSplitAmb_holds` calls.

## Statement

**Theorem.** `JetSplitAmb` holds.

`JetSplitAmb` is a $p$-adic bound on the jets of an ambient kernel `ambOf s B χ cD`. The prime $p \ge 5$ splits as $p = \pi\bar\pi$ with $\pi \in \mathbb Z[\omega_K]$, does not divide $d$ or $\operatorname{disc}(E)$, and the self-dual lattices $N, N'$ are standard at $p$. For $c' > 0$ prime to $p$, $x \in$ `divLat c' (homAt S N N')` and a multi-index $m$, the jet $J$ of level $pc'$ at $x$ and $m$ satisfies
$$|\iota(\sigma_0(J))| \cdot |\iota(\bar\pi)|^{|m|} \cdot |p|^{|\mathrm{Tau}|\, ab} \le 1.$$
The [entry for `jetAtSplit_ambOf`](/entry/jet-at-split-amb-of/) lists the hypotheses, and the [entry for `jetSplitAmb_holds`](/entry/jet-split-amb-holds/) unfolds the jet.

## Proof

The proof is `exact @jetSplitAmb_holds`, through a `first | exact … | …` tactic block.

## In the Lean code

The theorem is at [JetTableBoundSplitPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JetTableBoundSplitPrimeStatement.lean#L5). `JetSplitAmb` is at [JetSplitAmb.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JetSplitAmb.lean#L15).

The name speaks of a "jet table". The statement has no table: it is one bound for each jet.
