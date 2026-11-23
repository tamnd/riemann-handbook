---
id: jet-at-split-amb-of
title: The jet bound at a split prime, for the ambient kernel of a seam
kind: theorem
decl: Formalism.L2.Ker.Test.jetAtSplit_ambOf
module: Formalism.LocalToGlobal.KernelLattices.KernelLocalFactors.SelfDualLatticeNorms
covers: 317
status: drafted
drafted_by: writer@claude
---
This theorem bounds the $p$-adic size of the Taylor jets of the theta kernel at a prime $p$ that splits in $K$. It applies the general bound `jetAtSplit` to the ambient kernel `ambOf s B χ cD` of a seam. Its user is [`jetSplitAmb_holds`](/entry/jet-split-amb-holds/), which only restates it, and through it [`jet_table_bound_split_prime`](/entry/jet-table-bound-split-prime/). The real content is in `jetAtSplit`.

## Statement

Let $s$ be a seam with `s.Ok`, $B$ and $\chi$ as in [`IntInert`](/entry/kernels-integral-inert/), and numbers $c_D$. Let $N, N'$ be self-dual lattices of even ranks $a, b$ that are standard at $p$, $S$ a set of primes of $E$, and $\iota \colon \mathbb C \to \mathbb C_p$ a field isomorphism. Assume $p \ge 5$, $p \nmid d$, $p \nmid \mathrm{disc}(E)$, $|\iota(c_D(\tau))| \le 1$, and `LaHyp a b S`. Let $\pi = m + n\omega_K$ with $\pi \bar\pi = p$, and $p_E$ an element of $O_E$ that the embeddings send to $\pi$, such that a prime $P$ above $p$ is in $S$ exactly when $p_E \notin P$ (`SplitS`).

**Theorem.** For $c' > 0$ prime to $p$, $x$ in the lattice `divLat c' (homAt S N N')`, and a multi-index $m$,
$$|\iota(\sigma_0(J_{S,N,N'}(p c', x, m)))| \cdot |\iota(\bar\pi)|^{\deg m} \cdot |p|^{|\mathrm{Tau}|\, a b} \le 1,$$
where $J$ is the jet `jetK` of the kernel. We have not unfolded `jetK` or `LaHyp`.

## Proof

`kerStdEx` gives CM data $a_0, b_0, c_0, \lambda$ and the standard kernel facts `KerStd` for $N, N'$ at $p$. Then `jetAtSplit` applies, with $p \ne 2$ from $p \ge 5$.

## In the Lean code

The theorem is at [SelfDualLatticeNorms.lean](lean:Formalism/LocalToGlobal/KernelLattices/KernelLocalFactors/SelfDualLatticeNorms.lean#L110). `JetAtSplit` is in [StatementKer.lean](lean:Formalism/LocalToGlobal/AlgebraicTheory/StatementKer.lean#L59) and `jetAtSplit` in [LocNormScale.lean](lean:Formalism/LocalToGlobal/AlgebraicTheory/LocNormScale.lean#L12).

The theorem is in a namespace `Test`, but it is used in the main proof. The parent `jetSplitAmb_holds` at [JetTableBoundSplitPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JetTableBoundSplitPrime.lean#L7) is a pure renaming of this theorem.
