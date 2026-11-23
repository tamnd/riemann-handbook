---
id: theta-measure-nonzero-vectors-bound
title: A polynomial bound for the theta measure of a box
kind: theorem
decl: GlobalTheory.T.theta_measure_nonzero_vectors_bound
module: CompanionTheory.SpectralGeometry.LocalGlobalProofs.AdelicAnalysis.ThetaMeasureNonzeroVectorsBoundStatement
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the mean count in a box](/entry/mean-count-box/). It bounds the theta measure of the nonzero vectors on an adelic box by a polynomial in the radius. Three lemmas use it: `theta_measure_locally_finite`, `theta_frames_zero` and `main_bound` in the Siegel-Weil archimedean density file. Through them it lies below [EveryCharacter](/step/every-character/).

## Statement

The statement is word for word that of [`mean_count_box`](/entry/mean-count-box/). In short: let $E/F$ be a CM extension of number fields, $J$ a nondegenerate hermitian $M \times M$ matrix with $M \geq 3$, $H = U(J)$ its unitary group, $\mu$ a Haar measure on $H(\mathbb{A}_F)$ and $\mathcal{F}$ a fundamental domain for $H(F)$. For $N \geq 1$ there is $C$ such that for all $r > 0$, the theta measure of the nonzero vectors of $E^M$ on the box $B(N, r)$ is at most $C\,(r^{[F:\mathbb{Q}] M} + r^{2[F:\mathbb{Q}] M})$. The objects are defined in that entry.

## Proof

The Lean proof applies `GlobalTheory.CompanionTheory.SW.MeanCount.mean_count_box`. There is no other step.

## In the Lean code

The theorem is in [ThetaMeasureNonzeroVectorsBoundStatement.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaMeasureNonzeroVectorsBoundStatement.lean#L7). The proof is a `first | exact … | …` combinator that tries three ways to apply `mean_count_box`. Since the two statements are the same, the first way suffices. The statement file is a public name in the namespace `GlobalTheory.T` for a lemma proved in [ThetaMeasureNonzeroVectorsBound.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaMeasureNonzeroVectorsBound.lean#L36). All the content is in [the mean count in a box](/entry/mean-count-box/).
