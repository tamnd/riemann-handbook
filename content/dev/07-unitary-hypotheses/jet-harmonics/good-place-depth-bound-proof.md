---
id: good-place-depth-bound-proof
title: The local depth bound at a good place (statement form)
kind: theorem
decl: GlobalTheory.T.goodPlaceDepthBound_proof
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.GoodPlaceDepthBoundProofStatement
covers: 810
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It states `NuGoodSt` and proves it by [`nuGood`](/entry/nu-good/), which has the real content. Its one user is [`leafGood`](/entry/leaf-good/), which takes from it the constant $C_c$ and the bound on the depth $\nu_W(\lambda)$ at a good place $\lambda$.

## Statement

**Theorem.** `NuGoodSt` holds.

`NuGoodSt` says: for each $C_1 \ge 0$ there is $C_c > 0$ such that, for a moduli space $X$ over a CM field $E$ whose algebraic integral points have charts and that satisfies the seven package statements `PkgSt`, and for each place $\lambda$ of the coefficient field with good residue characteristic $\ell$, the depth $\nu_W(\lambda)$ is finite, $T\nu_W(\lambda)/e_\lambda$ is at most $F_j(\ell)$ plus $C_c$ times an explicit error term, and $\nu_W(\lambda) = 0$ when $\ell$ exceeds the total weight $D_F$. [The entry for `nuGood`](/entry/nu-good/) gives the full statement.

## Proof

The statement is that of `GlobalTheory.GoodDepth.nuGood`, and the proof applies it.

## In the Lean code

The theorem is in [GoodPlaceDepthBoundProofStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPlaceDepthBoundProofStatement.lean#L6). The proof is `first | exact @GlobalTheory.GoodDepth.nuGood | ...`, a tactic that tries the alias in three forms, under `set_option maxHeartbeats 1000000`, which a one-line alias does not need. `NuGoodSt` is in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L165).
