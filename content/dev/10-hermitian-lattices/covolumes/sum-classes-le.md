---
id: sum-classes-le
title: The weights of the frame classes in one datum, local name
kind: theorem
decl: GlobalTheory.TypeAsm.PerRow.sum_classes_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TermPairsRowLatticeCountedViaEmbeddings
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem is a local name, in the file of [`perRowC`](/entry/per-row-c/), for [`sum_frameClassWeights_le_datumBound`](/entry/sum-frame-class-weights-le-datum-bound/). That theorem is in turn a renaming of [`sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/), which has the proof. `perRowC` uses this theorem twice in step 4 of its proof: once for the first terms of a fibre of pairs, once for the second terms.

## Statement

The setting is that of [`perRowC`](/entry/per-row-c/): a datum $D$ with `Std`, a space $W$ with `IsEmb`, and a row lattice $\Lambda$. Let $j, x \in \mathbb N$, let $\delta$ be a label, let $d$ be a lattice datum in $W$, and let $N$ choose a normal form for each term.

**Theorem.** Let $A$ be a nonempty finite set of terms. Suppose that each $t \in A$ is relevant, $\Lambda_t = \Lambda$, $j_t = j$, $\delta_t = \delta$, $N(t)$ is adapted to $(F_0, F_t, \mathfrak d)$ and is a term for $\Lambda$, the index $\mathrm{gI}(N(t), \Lambda)$ is $x$, and the datum of $t$ is $d$. Then
$$\sum_{\beta \in \{[t] : t \in A\}} \mathrm{clsOm}(\beta) \le \mathrm{datBd}(k, r, \Delta_{j,\delta}, D_{b;j,\delta}, N_T, x).$$

Here $[t]$ is the frame class of $t$, and $\mathrm{clsOm}([t]) = \omega(t)$, as in [the entry for `sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/).

## Proof

The proof is the term `GlobalTheory.T.sum_frameClassWeights_le_datumBound`, applied to all the arguments. There is nothing else.

## In the Lean code

The theorem is at [TermPairsRowLatticeCountedViaEmbeddings.lean line 49](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairsRowLatticeCountedViaEmbeddings.lean#L49). The chain has three names for one statement: `PerRow.sum_classes_le`, `T.sum_frameClassWeights_le_datumBound` and `PerRow.sum_clsOm_le_datBd`.
