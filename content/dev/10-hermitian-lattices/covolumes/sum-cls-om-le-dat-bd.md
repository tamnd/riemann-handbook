---
id: sum-cls-om-le-dat-bd
title: The weights of the frame classes in one datum
kind: theorem
decl: GlobalTheory.TypeAsm.PerRow.sum_clsOm_le_datBd
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SumFrameClassWeightsLeDatumBound
covers: 453
status: drafted
drafted_by: writer@claude
---
This theorem bounds the total weight of the frame classes of a set of terms that share one lattice datum. It moves the general count [`sum_weights_per_datum`](/entry/sum-weights-per-datum/) into the setting of terms of a word $u$. Its statement form is [`sum_frameClassWeights_le_datumBound`](/entry/sum-frame-class-weights-le-datum-bound/), and through [`sum_classes_le`](/entry/sum-classes-le/) it gives the fibre bound in [`perRowC`](/entry/per-row-c/).

## Statement

The notation is that of [`perRowC`](/entry/per-row-c/). Two flags $G, G'$ are *frame equivalent* for $F_0$ and $\Lambda$ (`FrEqv`) if there is an isometry $n$ of $V$ in the unipotent group of $F_0$ (`InN`) with $n\Lambda = \Lambda$ and $n(G.e_a) \equiv G'.e_a$ modulo $G'.X_a$ for each frame vector. The *frame class* $[t]$ of a term $t$ (`frCls`) is the set of flags frame equivalent to $F_t$. The class weight $\mathrm{clsOm}(\beta)$ is $\omega(t)$ for some term $t$ with $\Lambda_t = \Lambda$ and $[t] = \beta$, and $0$ if there is none. By `clsOm_frCls`, $\mathrm{clsOm}([t]) = \omega(t)$ when $\Lambda_t = \Lambda$.

**Theorem.** Assume `Std` and `IsEmb` for $W$. Let $A$ be a nonempty finite set of terms, and $N$ a choice of normal form for each term. Suppose that each $t \in A$ is relevant, $\Lambda_t = \Lambda$, $j_t = j$, $\delta_t = \delta$, $N(t)$ is adapted to $(F_0, F_t, \mathfrak d)$ and is a term for $\Lambda$, $\mathrm{gI}(N(t), \Lambda) = x$, and the datum of $t$ is $d$. Then
$$\sum_{\beta \in \{[t] : t \in A\}} \mathrm{clsOm}(\beta) \le \mathrm{datBd}(k, r, \Delta_{j,\delta}, D_{b;j,\delta}, N_T(u), x).$$

## Proof

1. Fix $t_0 \in A$. `embeddedDatum_of_term_definiteSpace` gives $x \ge 1$ and, with $\dim V = 2r + k + 1$, $\dim W = k$. `exists_star_stable_ideal_absorbing_minors` and `adaptedNormalForm_normsMinors_eq_label` give $\Delta_{j,\delta} \ge 1$ and $D_{b;j,\delta} \ge 1$.
2. For each class $\beta$, choose $t \in A$ with $[t] = \beta$ and put $G(\beta) = F_t$. Then $\mathrm{clsOm}(\beta) = \omega_I(F_0, G(\beta), \mathfrak d, \Lambda)$.
3. Apply [`sum_weights_per_datum`](/entry/sum-weights-per-datum/) to the flags $G(\beta)$, with the label $\bar\delta$. Its three hypotheses: `adaptedNormalForm_normsMinors_eq_label` gives the invariants $j$, $T$, $\Delta$, $D_b$ and the label of each normal form; the datum is $d$ by hypothesis; and distinct classes are not frame equivalent, by `frCls_eq_iff`.
4. Since $\dim W = k$ and the number of infinite places of $E$ is $f$, the bound of step 3 is the bound of the theorem.

## In the Lean code

The theorem is in [SumFrameClassWeightsLeDatumBound.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SumFrameClassWeightsLeDatumBound.lean#L23). `frCls`, `clsOm`, `frCls_eq_iff` and `clsOm_frCls` are in [ClsOmNonneg.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ClsOmNonneg.lean#L16), and `FrEqv` in [AdaptSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/AdaptSelf.lean#L39). `unitaryHostFieldArithmeticConditions` supplies `IsCMUnram` for $E$, the equality of $f$ with the number of infinite places of $E$, and $\dim V = 2r + k + 1$.

The representative $G(\beta)$ is chosen with `Exists.choose`, and is $F_0$ for a set $\beta$ that is not a class of $A$. The sum is over classes, not terms: two terms of $A$ in one class count once.
