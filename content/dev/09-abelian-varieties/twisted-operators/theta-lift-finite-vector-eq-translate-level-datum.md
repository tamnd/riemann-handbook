---
id: theta-lift-finite-vector-eq-translate-level-datum
title: A theta level vector is a translate of a level-datum vector (second name)
kind: theorem
decl: GlobalTheory.T.thetaLiftFiniteVector_eq_translate_levelDatum
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaLiftFiniteVectorEqTranslateLevelDatumStatement
covers: 309
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`thP_vec_eq_translate`](/entry/th-p-vec-eq-translate/). It has the same statement word for word, and its proof only calls that theorem. The real content is in `thP_vec_eq_translate`. Step 1 of [`span_std`](/entry/span-std/) uses it under this name.

## Statement

Let $C$ be a context `Ctx S T` with $\operatorname{rank} T \le \operatorname{rank} S$, let $\omega$ be a weak Weil representation, and let $B$ be a good basis. Let $\Lambda_T$ be a self-dual lattice with `IsAA C.X.Λ ΛT`, and let $\beta_S$, $\beta_T$ be frames of the standard lattice and of $\Lambda_T$. Let $P_g \ne \emptyset$ and $Q$ be finite sets of places, none above $2$. Let $f$ be a theta level vector (`IsThPVecOf`). Then there are a level datum $L_v$, a natural number $M$, a vector $f'$ and $k_0 \in G_S(\mathbb A_f)$ such that

$$f = \omega(k_0, 1)\, u, \qquad u = \texttt{C.uVec}\ L_v\ f',$$

$u$ is a nonzero theta Fock vector, $f'$ is a base vector for $L_v$, $0 < M \in \mathfrak m$, and each $k$ in the level group of $L_v$ stabilizes $\beta_T$ and reduces to $1$ at the places of $P_g$. See [`thP_vec_eq_translate`](/entry/th-p-vec-eq-translate/) for the terms.

## Proof

The proof is `first | exact @GlobalTheory.LiftLevel.thP_vec_eq_translate | ...`. The first branch closes the goal, since the two statements are equal.

## In the Lean code

The theorem is at [ThetaLiftFiniteVectorEqTranslateLevelDatumStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaLiftFiniteVectorEqTranslateLevelDatumStatement.lean#L11). The file only gives the theorem a name in the namespace `GlobalTheory.T`.
