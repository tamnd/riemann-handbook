---
id: term-pairs-row-lattice-counted-via-embeddings
title: Pairs of terms over one row lattice, counted by embedded data, statement form
kind: theorem
decl: GlobalTheory.T.termPairs_rowLattice_counted_via_embeddings
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TermPairsRowLatticeCountedViaEmbeddingsStatement
covers: 600
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`perRowC`](/entry/per-row-c/). It has the same statement and no proof of its own. The theorem [`pair_count_bound_of_siegel_mass`](/entry/pair-count-bound-of-siegel-mass/) takes it as a proved input. The real content is in the entry for `perRowC`.

## Statement

**Theorem.** `PerRowC` holds. Fix a datum $D$ with `Std`, a setting $X$, $Y$, a word $u$, and a positive definite Hermitian subspace $W$ that is embedded along the base flag (`IsEmb`). Fix a row lattice $\Lambda$, ranks $j', j''$ and labels $\delta', \delta''$. Let $S$ be a finite set of pairs $(t_1, t_2)$ of relevant terms such that $t_1$ has row lattice $\Lambda$, and the $t_i$ have the given ranks and labels. Then
$$\sum_{(t_1, t_2) \in S} w(\Lambda'_{t_1})\, \omega(t_1)\, \omega(t_2) \leq \sum_{x = 1}^{\lfloor \Delta' \rfloor} \sum_{x' = 1}^{\lfloor \Delta'' \rfloor} \bigl\lvert \mathrm{Trip}(x, x') \bigr\rvert \, d(x)\, d(x'),$$
in $[0, \infty]$. Here $\Delta'$ and $\Delta''$ are the norms attached to $(j', \delta')$ and $(j'', \delta'')$, $\mathrm{Trip}(x, x')$ is the set of embedded triples in $W$ over the lattice $\Lambda$ pulled back to $W$, and $d$ is `datBd`. The objects are those of [the entry for `perRowC`](/entry/per-row-c/), and we have not unfolded `omT`, `Trip` or `datBd` here.

## Proof

The proof is the term `perRowC`. There is nothing else.

## In the Lean code

The theorem is at [TermPairsRowLatticeCountedViaEmbeddingsStatement.lean#L6](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairsRowLatticeCountedViaEmbeddingsStatement.lean#L6). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `maxHeartbeats` set to 1,000,000. `PerRowC` is at [PerRowC.lean#L56](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean#L56).
