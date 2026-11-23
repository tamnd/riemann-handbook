---
id: sum-weights-per-datum
title: The weights of inequivalent flags with one datum
kind: theorem
decl: GlobalTheory.DegAsm.sum_weights_per_datum
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.FlagFrameVectorMemCommonSubspace
covers: 452
status: drafted
drafted_by: writer@claude
---
This theorem bounds the sum of the weights $\omega_I$ over pairwise inequivalent flags that share one lattice datum and one set of invariants. It sorts the flags by two discrete invariants of their normal forms, counts the sorts, and bounds each sort with [`one_class`](/entry/one-class/). [`sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/) applies it to the frame classes of terms.

## Statement

Let $K$ be a number field with an involution that satisfies `IsCMUnram` (stated in [the entry for `pair_count_bound_of_siegel_mass`](/entry/pair-count-bound-of-siegel-mass/)). Let $f$ be the number of infinite places of $K$ and $c_f = 1 + \log_2 [K : \mathbb Q]$. Let $(V, H)$ and $(W, H_W)$ be Hermitian spaces, $e \colon W \to V$ linear, $F$ a flag of length $r$ in $V$, and $\mathfrak d$ an ideal. For reals $\Delta, D_b, N_T, x$ put
$$\mathrm{datBd}(k, r, \Delta, D_b, N_T, x) = \Bigl(\frac{\Delta}{x}\Bigr)^{k/2} \, 8^{r+1} f^2 \, \Delta^{3c_f + 6} N_T^2 \, (D_b \Delta N_T)^{10000 (r+1)^3}.$$

**Theorem.** Let $g, j, T, x \in \mathbb N$, $\delta \colon \mathbb N \to K$, $\Lambda$ an $\mathcal O_K$-lattice, $d$ a datum, and $\Delta, D_b$ reals, with $g, x, \Delta, D_b \ge 1$. Let $(G_i)_{i \in s}$ be a finite family of flags. Assume:

1. $e$ satisfies `IsEmb` for $F$;
2. for each $i$ there is a normal form $N$ adapted to $(F, G_i, \mathfrak d)$ that is a term for $\Lambda$, with $j(N) = j$, $T(N) = T$, $\Delta(N) = \Delta$, $D_b(N) = D_b$ and $\mathrm{gI}(N, \Lambda) = x$;
3. for each $i$ the label of $(F, G_i)$ up to $j$ is $\delta$, and the datum of $(F, G_i, e, g, \Lambda)$ is $d$;
4. no two distinct $G_i$ are frame equivalent for $F$ and $\Lambda$.

Then $\sum_{i \in s} \omega_I(F, G_i, \mathfrak d, \Lambda) \le \mathrm{datBd}(\dim W, r, \Delta, D_b, T^f, x)$.

## Proof

If $s$ is empty, the right side is nonnegative. Else choose the normal forms $N_i$. Sort the indices by the pair $(P_i, c_i)$, where $P_i$ is the $j \times j$ matrix $H(N_i.F.e_a, N_i.F'.e_b)$ and $c_i$ is the unit of $N_i$ ($c_i \bar c_i = 1$).

1. The matrix $P_i$ has the signed shape of a normal form, and its leading minors are $\delta(1), \dots, \delta(j)$ by hypothesis 3. `signedBlockAntidiag_with_leadingMinors_encard_le` bounds the number of such matrices by $8^j \le 8^r$.
2. `hermFramePair_scalar_eq_quot_ideals_norm_le` gives nonzero ideals $\mathfrak a, \mathfrak a'$ of norm at most $\Delta$ with $tc_i \in \mathfrak a \iff t \in \mathfrak a'$. `NormOneCount.main` bounds the number of such $c$ by $8 f^2 \Delta^{2(2 + c_f)}$.
3. In one sort, all $N_i$ have the same $j$, $c$, $T$ and pairing matrix. [`one_class`](/entry/one-class/), with the base $N_{i_0}$, bounds the sum over the sort by $N_T^2 (\Delta/x)^{\dim W/2} \Delta^{c_f + 2} (D_b \Delta N_T)^{10000(r+1)^3}$, with $N_T = T^f$.
4. `sum_le_of_fibres` multiplies the bound of step 3 by the number of sorts. Since $8^r \cdot 8 = 8^{r+1}$ and $2(2 + c_f) + (c_f + 2) = 3c_f + 6$, the product is $\mathrm{datBd}$.

## In the Lean code

The theorem is in [FlagFrameVectorMemCommonSubspace.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagFrameVectorMemCommonSubspace.lean#L204), and `datBd` in [AdaptSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/AdaptSelf.lean#L42). The local lemmas `sum_le_of_fibres`, `sqM` (the matrix $P_i$), `sqM_shape` and `pairM_eq` are in the same file. `NormOneCount.main` is in [IsIntegralOfMulMem.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsIntegralOfMulMem.lean#L116).

The file is named after `flagFrameVector_mem_commonSubspace`, a small lemma in it, not after this theorem. The hypothesis $x \ge 1$ is introduced as `hx` and is not used by name in the proof.
