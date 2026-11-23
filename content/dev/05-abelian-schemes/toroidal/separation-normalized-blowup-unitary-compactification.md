---
id: separation-normalized-blowup-unitary-compactification
title: Separation on the normalized blowup of a unitary compactification (restatement)
kind: theorem
decl: GlobalTheory.T.separation_normalizedBlowup_unitaryCompactification
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SeparationNormalizedBlowupUnitaryCompactificatioStatement
covers: 534
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for `USep.sepB_of_normBl`, and [that entry](/entry/sep-b-of-norm-bl/) has the real content. Its only caller is [`uPoinStX_sep`](/entry/u-poin-st-x-sep/), where it is the last step: it gives the separation property `SepB` for the normalized blowup $S$ of the compactification.

## Statement

Take a CM field $E$, a hermitian datum of signature $(p, q)$ with $p + q \ge 1$, and a fan function $\varphi$ with `IsPolFan` and `NoSelfInt`, as in [`uPoinStX_sep`](/entry/u-poin-st-x-sep/). Take a level, the moduli scheme $X$, a coefficient field $F$, and a compactification datum `UCompact` with normal projective $Z$ over $F$ and dense open immersion $i \colon X_F \to Z$.

**Theorem.** Let $d \ge 1$, and let $J$ be an ideal on the model $Z_o$ of $Z$ over the ring $o$ of `UCompact`, supported off the image of $X$, with the valuations of $d\varphi$ (`UValOn`). Let $\pi \colon S \to Z$ be proper and a normalized blowup of $J\mathcal{O}_Z$ (`IsNormBl`), and let $j \colon X_F \to S$ be an open immersion with $\pi \circ j = i$ and $\pi^{-1}(i(X_F)) = j(X_F)$. Then $j$ satisfies `SepB`.

`SepB` is stated in [`uPoinStX_sep`](/entry/u-poin-st-x-sep/). In short: at a point of $S$ over monomial degeneration data, the monomial parameters vanish, the abelian part comes from an algebraically closed subfield $k_0$, and under `FromBase` the extra units take values in $k_0$.

## Proof

The proof is `first | exact @GlobalTheory.USep.sepB_of_normBl | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [SeparationNormalizedBlowupUnitaryCompactificatioStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SeparationNormalizedBlowupUnitaryCompactificatioStatement.lean#L13). The proof it names is in [SeparationNormalizedBlowupUnitaryCompactificatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SeparationNormalizedBlowupUnitaryCompactificatio.lean#L97). That proof proves the three clauses of `SepAtB` with `T.poincareApprox_values_at_point_of_elements`, which is where `NoSelfInt` is used. For the units, it extends a coordinate form on a lattice up to a nonzero multiple (`USep.Alg.exists_extend_smul`). This puts a nonzero power of each unit in $k_0$. Since $k_0$ is algebraically closed, the unit itself is in $k_0$ (`USep.Alg.mem_of_zpow_mem`). The file names end in "Compactificatio", without the final "n".
