---
id: jet-split-amb-holds
title: The jet bound at split primes for ambient kernels (pass-through)
kind: theorem
decl: GlobalTheory.AtG.jetSplitAmb_holds
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JetTableBoundSplitPrime
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem proves `JetSplitAmb` by a call to [`jetAtSplit_ambOf`](/entry/jet-at-split-amb-of/), which has the same statement in unbundled form. Its user is [`jetTableBound_splitPrime`](/entry/jet-table-bound-split-prime/). The content is in `jetAtSplit_ambOf` and the general bound `jetAtSplit` below it.

## Statement

**Theorem.** `JetSplitAmb` holds.

`JetSplitAmb` is the statement of `jetAtSplit_ambOf`, quantified over all its data; that entry lists the hypotheses. In short: let `ambOf s B χ cD` be an ambient kernel, $N, N'$ self-dual lattices standard at a prime $p \ge 5$, and $p = \pi\bar\pi$ with $\pi \in \mathbb Z[\omega_K]$. Then for $c' > 0$ prime to $p$, $x \in$ `divLat c' (homAt S N N')` and each multi-index $m$,
$$|\iota(\sigma_0(J(pc', x, m)))| \cdot |\iota(\bar\pi)|^{|m|} \cdot |p|^{|\mathrm{Tau}|\, ab} \le 1.$$

Here $J$ is `Amb.jetK`: $J(c, x, m)$ is the element of $K$ whose image under $\sigma_0$ is $\chi_F^{-1} \prod_k c_D(k)^{m_k}\, \partial^m \Theta_{c,x}(0)$, where $\Theta_{c,x}$ is the theta function `thInd` induced at level $c$ from $x$ and $\chi_F$ is the constant `chiF`.

## Proof

The proof introduces 42 variables and hypotheses and passes them to `Formalism.L2.Ker.Test.jetAtSplit_ambOf` in the same order. It leaves out `D`, `X`, `cc`, `δ` and the prime instance, which are implicit there.

## In the Lean code

The theorem is at [JetTableBoundSplitPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JetTableBoundSplitPrime.lean#L7). `JetSplitAmb` is at [JetSplitAmb.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JetSplitAmb.lean#L15), and `Amb.jetK` at [ThDistC.lean](lean:Formalism/LocalToGlobal/KernelLattices/ThDistC.lean#L103).

`jetK` uses a choice (`desc`): it returns $0$ when the complex jet is not in $\sigma_0(K)$. In that case the bound holds trivially.
