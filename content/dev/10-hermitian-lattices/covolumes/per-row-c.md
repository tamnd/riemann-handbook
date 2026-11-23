---
id: per-row-c
title: Pairs of terms over one row lattice, counted by embedded data
kind: theorem
decl: GlobalTheory.TypeAsm.perRowC
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TermPairsRowLatticeCountedViaEmbeddings
covers: 599
status: drafted
drafted_by: writer@claude
---
This theorem proves `PerRowC`. It bounds a weighted sum over pairs of terms with one row lattice $\Lambda$ by a count of triples of lattice data in a definite space $W$. Its statement form is [`termPairs_rowLattice_counted_via_embeddings`](/entry/term-pairs-row-lattice-counted-via-embeddings/), and [`pair_count_bound_of_siegel_mass`](/entry/pair-count-bound-of-siegel-mass/) uses it in step 5 of its proof.

## Statement

Fix a datum $D$ with `Std`, a setting $X$, $Y$ and a word $u$. Let $E$ be the CM field of $D$, $V$ the Hermitian space, $F_0$ the base flag of $u$ (of length $r$), and $\mathfrak d$ the ideal `dI D`, the different of the base field of $D$ extended to $\mathcal O_E$. Each term $t$ has a flag $F_t$, a row lattice $\Lambda_t$, a rank $j_t$, a label $\delta_t$ and the weight
$$\omega(t) = \omega_I(F_0, F_t, \mathfrak d, \Lambda_t) = \inf_N \omega_N(\Lambda_t),$$
over the normal forms $N$ adapted to $(F_0, F_t, \mathfrak d)$ (`omT`, `omI`). Let $W \subseteq V$ carry a Hermitian form that is the restriction of $H$, and suppose that the vectors orthogonal to all frame vectors of $F_0$ are exactly $W + X(F_0)$ (`IsEmb`).

**Theorem.** Let $S$ be a finite set of pairs $(t, t')$ of relevant terms with $\Lambda_t = \Lambda$, $j_t = j'$, $j_{t'} = j''$, $\delta_t = \delta'$, $\delta_{t'} = \delta''$. Then, in $[0, \infty]$,
$$\sum_{(t,t') \in S} w(\Lambda'_t)\, \omega(t)\, \omega(t') \le \sum_{x=1}^{\lfloor \Delta' \rfloor} \sum_{x'=1}^{\lfloor \Delta'' \rfloor} \#\mathrm{Trip}(x, x') \cdot b'(x)\, b''(x').$$

Here $\Delta' = $ `k2Del D j' δ'` and $D'_b = $ `DbL D j' δ'` (products of local norms of the label), $b'(x) = \mathrm{datBd}(k, r, \Delta', D'_b, N_T, x)$ with $k = \dim W$ and $N_T = T_u^f$, and the same for $''$. $w(\Lambda')$ is `wRow`, the inverse of the order of a finite group of automorphisms. $\mathrm{Trip}(x, x')$ is the set of triples $(d, d', \eta)$: two lattice data in $W$ of indices $x, x'$ over $L_0 = (\Lambda + X(F_0)) \cap W$, and an isometry $\eta$ of $W$ that carries $d'$ to $d$. The function `datBd` is stated in [the entry for `sum_weights_per_datum`](/entry/sum-weights-per-datum/).

## Proof

If $S$ is empty, both sides are $0$. Else:

1. For each relevant term $t$, the local lemma `termData` chooses a normal form $N_t$ adapted to $(F_0, F_t, \mathfrak d)$, a term for $\Lambda_t$, with $\Delta(N_t) = \Delta_{j_t,\delta_t}$ and $1 \le x_t \le \Delta(N_t)$, where $x_t$ is the index `gI`. It also gives an isometry $h_t$ of $W$ that agrees with the isometry of $t$ modulo the flags (`IsH`).
2. The local lemma `pairTrip` shows, for $(t, t') \in S$, that $\Lambda_{t'} = \Lambda$ and $(\mathrm{dat}(t), \mathrm{dat}(t'), h_t h_{t'}^{-1}) \in \mathrm{Trip}(x_t, x_{t'})$.
3. `sum_le_encard_fibres` is an abstract fibre count: if each fibre of the map $p \mapsto (\text{triple}, x, x')$ has sum at most $b'(x) b''(x')$, the inequality follows.
4. For one fibre, `sum_pairs_le_classes` bounds the sum by $\bigl(\sum_{\beta} \mathrm{clsOm}(\beta)\bigr)\bigl(\sum_{\beta'} \mathrm{clsOm}(\beta')\bigr)$, over the frame classes of first and of second terms. [`sum_classes_le`](/entry/sum-classes-le/) bounds each factor by $b'(x)$ and $b''(x')$.

The rest is bookkeeping and nonnegativity.

## In the Lean code

The theorem is in [TermPairsRowLatticeCountedViaEmbeddings.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairsRowLatticeCountedViaEmbeddings.lean#L114), and `PerRowC` in [PerRowC.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L56). The lemmas:

- `termData`: `exists_adaptedNormalForm_relevantTerm`, `rowLattice_term_adaptedNormalForm`, `adaptedNormalForm_normsMinors_eq_label`, `embeddedDatum_of_term_definiteSpace`, `exists_star_stable_ideal_absorbing_minors`, `exists_definiteSpace_isometry_of_adapted_pair`.
- `pairTrip`: `termsOverRow_compatible`, `trip_of_terms`.
- `sum_le_encard_fibres` and `sum_pairs_le_classes` are renamings of `T.sum_fibre_two_index_encard_bound` and `T.sum_pairs_definiteIsometry_le_frameClasses`.

The count $\#\mathrm{Trip}$ is an `encard` in $\mathbb N \cup \{\infty\}$. If one of these sets is infinite, the bound says nothing; this theorem does not prove finiteness. We have not unfolded `IsDat` or the group `autLz` in `wRow`.
