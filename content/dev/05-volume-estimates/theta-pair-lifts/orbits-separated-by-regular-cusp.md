---
id: orbits-separated-by-regular-cusp
title: A cusp form with a regular level determinant, second name
kind: theorem
decl: GlobalTheory.T.orbits_separated_by_regular_cusp
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsCuspRegularLevelDeterminant
covers: 761
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [exists_cusp_regular_level_determinant](/entry/exists-cusp-regular-level-determinant/). It gives, on a good cover, a cusp form $u$ whose group determinant over a finite group $S$ of level automorphisms is not a zero divisor in the ring of modular forms. It has two users, `exists_short_integral_vector` and `regular_embeddings_cover_bad_embedding_locus_alt`, through which [the covolume bound](/entry/top-covol-g-alt-alt/) reaches it. Below this theorem are 761 declarations.

## Statement

**Theorem.** Assume the six published inputs, $p, q \ge 1$ at level $j$, $[E:\mathbb{Q}]/2 > 2$, $1 \le j \le m$ (`InR`), a good cover $Y$ for $(e, o)$ with $4 \le e$, and $r + 1 < g_k$ for both host primes. Let $S$ be `grpHR fr` or `grpGHR fr k`. Then there is a cusp form $u$ of weight $c_0 \cdot \lambda_H$ with $\operatorname{levDet}_S(u)\, f = 0 \Rightarrow f = 0$ for each $f$ in `secRing`.

The notation is that of the renamed theorem.

## Proof

The proof is `first | exact exists_cusp_regular_level_determinant | ...`. The two statements are the same, hypothesis for hypothesis.

## In the Lean code

The theorem is at [ExistsCuspRegularLevelDeterminant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsCuspRegularLevelDeterminant.lean#L205), in the same file as the theorem that it renames.

- The name says that orbits are separated. The statement is about a regular determinant. The orbit separation is the input [separate_orbits_by_cusp](/entry/separate-orbits-by-cusp/).
- The hypothesis $4 \le e$ is copied from the renamed theorem, which does not use it.
