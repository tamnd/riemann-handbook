---
id: sum-harmonic-values-formal-kernel-similitude
title: A sum of harmonic values over the formal kernel of a similitude (statement form)
kind: theorem
decl: GlobalTheory.T.sum_harmonicValues_formalKernel_similitude
module: Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.SumHarmonicValuesFormalKernelSimilitudeStatement
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`sum_hv_formal_kernel`](/entry/sum-hv-formal-kernel/), with the same type. Its only user is [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/), which applies it once on each coset of the kernel of $q$.

## Statement

The setting is that of [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/), with $(pq)^*(pq) = N^2$ for an odd $N$. Here the points $a_i$, for $i \in J$, run once over the $n$-tuples killed by $pq$ whose coordinates lie in the formal group of $C$. The sections $F_b$ of $L^{N^2}$ are regular on the integral model. For each $i$ with $q a_i = 0$, the translate $G_i$ of $F$ by $a_i$ is $F$ times integral scalars $r_b$ with $\prod_b r_b = 1$. The conclusion is the same equation: there is $z$ with $v(z)/e \geq -\rho$ and

$$\iota(s) \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q a_i = 0\} \cdot \iota\Bigl(\prod_{\tau} \tau(\det p)^{m_\tau}\Bigr) \cdot z.$$

The entry [`sum_hv_formal_kernel`](/entry/sum-hv-formal-kernel/) gives all the hypotheses.

## Proof

The proof is the tactic `first | exact @GlobalTheory.PlaceInt.FormSum.sum_hv_formal_kernel | ...`. The first branch succeeds. So this theorem is `sum_hv_formal_kernel` under a second name.

## In the Lean code

The theorem is in [SumHarmonicValuesFormalKernelSimilitudeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHarmonicValuesFormalKernelSimilitudeStatement.lean#L11). It is a renaming, with no content of its own. The real proof is in [`sum_hv_formal_kernel`](/entry/sum-hv-formal-kernel/).
