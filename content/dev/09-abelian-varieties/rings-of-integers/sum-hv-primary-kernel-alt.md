---
id: sum-hv-primary-kernel-alt
title: A sum of harmonic values over the primary part of a kernel (statement form)
kind: theorem
decl: GlobalTheory.T.sum_hv_primary_kernel_alt
module: Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.SumHvPrimaryKernelStatement
covers: 575
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/), with the same type. It has three users: `ShortPrime.ell_part`, `SupFull.ell_part` and `SupFull.isotropicLPart_shortSeries_bound_mul`. They sit below the [literature layer](/step/every-character-of-literature/).

## Statement

Let $C$ be an integral chart over a complete discrete valuation ring $T$. Let $\ell$ be a prime that is not a unit in $T$, and let $N$ be odd. Let $p, q$ be $n \times n$ matrices over $\mathcal{O}_E$ with $(pq)^* (pq) = N^2$. Let $a_i$, for $i \in J$, run once over the $n$-tuples of points that $pq$ kills and that have $\ell$-power order. Let $G_i$ be the translates by $a_i$ of a family $F$ of sections of $L^{N^2}$. Then, for a polynomial $P$ in the set `HH c w n` and a scalar $s$ under an integrality condition, there is $z$ with $v(z)/e \geq -\rho$ and

$$s \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q \text{ kills } a_i\} \cdot \prod_{\tau} \tau(\det p)^{m_\tau} \cdot z.$$

The entry [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/) defines each object and gives all the hypotheses.

## Proof

The proof is the tactic `first | exact @GlobalTheory.sum_hv_primary_kernel | ...`. The first branch succeeds. So this theorem is `sum_hv_primary_kernel` under a second name.

## In the Lean code

The theorem is in [SumHvPrimaryKernelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHvPrimaryKernelStatement.lean#L11). It is a renaming. The real proof is in [`sum_hv_primary_kernel`](/entry/sum-hv-primary-kernel/).
