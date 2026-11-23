---
id: k-stability-main
title: Homological stability for general linear groups over a ring of finite stable range
kind: theorem
decl: GlobalTheory.HomStab.kStability_main
module: Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.HomologicalStability.LinkExactnessStability.HomologicalStabilityTheorem
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem proves `KStability`: the stabilization map $H_i(\mathrm{GL}_n(R)) \to H_i(\mathrm{GL}_{n+1}(R))$ is an isomorphism for $n \geq 2i + s + 2$, when $R$ has stable range at most $s$. The [entry under the second name](/entry/k-stability/) states it in full and lists the callers. The proof is an induction on $i$ that proves surjectivity and injectivity together. The work is in the action of $\mathrm{GL}_{m+1}(R)$ on a complex of split unimodular sequences.

## Statement

Let $R$ be a commutative ring with stable range at most $s$, in the sense of [`StableRangeLe`](/entry/k-stability/). Let $\iota_m \colon \mathrm{GL}_m(R) \to \mathrm{GL}_{m+1}(R)$ be $g \mapsto \mathrm{diag}(g, 1)$, and $H_i$ group homology with coefficients in the trivial module $\mathbb{Z}$.

**Theorem.** For all $i$ and $n$ with $n \geq 2i + s + 2$, the map $(\iota_n)_* \colon H_i(\mathrm{GL}_n(R)) \to H_i(\mathrm{GL}_{n+1}(R))$ is an isomorphism.

Homological stability for $\mathrm{GL}_n$ over rings of finite stable range is due to W. van der Kallen (Homology stability for linear groups, Invent. Math. 60, 1980). We have not compared his range with the range in the Lean statement.

## Proof

By strong induction on $i$, prove for all $m$:

- $(\iota_m)_*$ is surjective on $H_i$ if $m \geq 2i + s + 1$;
- $(\iota_m)_*$ is injective on $H_i$ if $m \geq 2i + s + 2$.

The case $i$ uses both claims for all $q < i$. Each step is one lemma, `groupHomology_GL_stab_surjective_of_stableRange_induction` and `groupHomology_GL_stab_injective_of_stableRange_induction`. Both have the same plan.

1. A split sequence in $R^{m+1}$ is a list of pairs $(v_j, w_j)$ of vectors with $w_j \cdot v_k = \delta_{jk}$. Let $C_p$ be the free $\mathbb{Z}$-module on the split sequences of size $p$, a permutation module for $\mathrm{GL}_{m+1}(R)$ (`splitRep`). The differential $C_{p+1} \to C_p$ is the alternating sum of the maps that delete one pair (`splitD`). Its square is $0$ (`splitSequence_rep_complex_exact`).
2. Stable range gives exactness of $C$ at $p$ when $m + 1 \geq 2p + s + 1$ (`splitSeq_exactAt_of_two_mul_add_stableRange_le`).
3. The lemma `splitSeq_firstPage_iso_and_differential` identifies $H_q(\mathrm{GL}_{m+1}(R), C_p)$ with $H_q(\mathrm{GL}_{m+1-p}(R))$ when $p + s \leq m + 1$. Under this identification the differential $C_{p+1} \to C_p$ induces $(\iota_{m-p})_*$ for even $p$ and $0$ for odd $p$.
4. An abstract lemma on a complex of $G$-modules that is exact in low degrees (`quillen_stabilisation_surjective_bottom`, and its injective twin) then gives the claim for $(\iota_m)_*$ in degree $i$ from the claims for the lower maps in degrees $q < i$.

Then $n \geq 2i + s + 2$ gives injectivity and surjectivity of $(\iota_n)_*$ on $H_i$. A bijective map of $\mathbb{Z}$-modules is an isomorphism.

## In the Lean code

- The theorem is in [HomologicalStabilityTheorem.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/HomologicalStabilityTheorem.lean#L10).
- The two induction steps are `grpHMap_stab_surjective_step` in [GroupHomologyGLStabSurjectiveOfStableRangeInduct.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/GroupHomologyGLStabSurjectiveOfStableRangeInduct.lean#L17) and `homStab_GL_inj_step` in [GroupHomologyGLStabInjectiveOfStableRangeInducti.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/GroupHomologyGLStabInjectiveOfStableRangeInducti.lean#L12). The `GlobalTheory.T` names are one-line wrappers of these, by `first | exact ...`.
- The exactness lemma is in [SplitSeqExactAtOfTwoMulAddStableRangeLe.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/SplitSeqExactAtOfTwoMulAddStableRangeLe.lean#L83), the first page in [SplitSeqFirstPageIsoAndDifferential.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/SplitSeqFirstPageIsoAndDifferential.lean#L47), and the abstract lemma in [QuillenStabilisationSurjectiveBottom.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/QuillenStabilisationSurjectiveBottom.lean#L40). The folder has 70 files for this proof; we have opened only these.
- `splitSeq` and `splitRep` are in [SubClosed.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/SubClosed.lean#L27) and [MemSplitSeqIff.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/MemSplitSeqIff.lean#L67). We have not unfolded the proof of step 3. Since $C_p$ is a permutation module, the standard argument is Shapiro's lemma for the stabilizer $\mathrm{GL}_{m+1-p}(R)$ of a standard sequence (`stdList`).
- The file ends with an empty `section` that opens namespaces and does nothing.
