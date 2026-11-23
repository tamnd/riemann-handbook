---
id: bernstein-unitary-product-irreducible
title: Bernstein's theorem that a product of unitary representations is irreducible
kind: theorem
decl: PositivityTheory.RgUd.All.bernsteinUnitaryProductIrreducible
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.BernsteinExponentBounds.BernAll
covers: 689
status: drafted
drafted_by: writer@claude
---
This theorem proves the published input `BernsteinUnitaryProductIrreducible`: over a non-archimedean local field, the parabolic induction of two irreducible unitary representations of general linear groups is irreducible. It is the same statement as [`bernAt`](/entry/bern-at/), with the field quantified. Its three callers are `bernstein_unitary_product_irreducible_of_literature`, which fills a field of the [published inputs](/step/theta-local-inputs-def/) (see [the bundle from the literature](/step/published-results-first/)), `bernstein_unitary_product_irreducible_of_open`, and `liftIso_of`, for the theta lift. The first step above it is [EveryCharacter from the Galois row](/step/every-character/).

## Statement

Let $k$ be a non-archimedean local field. A complex representation is *unitarizable* if it has a positive definite invariant Hermitian form. For representations $\pi_1$ of $\mathrm{GL}_r(k)$ and $\pi_2$ of $\mathrm{GL}_t(k)$, let $\pi_1 \times \pi_2$ be the normalized parabolic induction of $\pi_1 \otimes \pi_2$ from the block upper triangular parabolic subgroup of $\mathrm{GL}_{r+t}(k)$ (smooth vectors).

**Theorem.** For every $k$, if $\pi_1$ and $\pi_2$ are smooth, irreducible and unitarizable, then $\pi_1 \times \pi_2$ is irreducible.

This is the theorem of J. N. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N) (non-archimedean case)*, Lecture Notes in Math. 1041, Springer, 1984. We have not checked whether that paper covers fields of positive characteristic; the Lean statement does.

## Proof

The proof is `fun k _ _ _ _ => bernAt k`. The content is in [`bernAt`](/entry/bern-at/).

## In the Lean code

The theorem is at [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L27). The statement is `GlobalTheory.Published.BernsteinUnitaryProductIrreducible` in [BernsteinUnitaryProductIrreducible.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/BernsteinUnitaryProductIrreducible.lean#L10). The induction is `prod₂`, which is `ind₂` along `stdSum`, and `parInd` twists by `deltaHalf` before inducing. Irreducibility and unitarizability are algebraic: no Hilbert space completion appears.
