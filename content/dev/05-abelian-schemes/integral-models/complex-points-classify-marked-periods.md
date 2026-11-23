---
id: complex-points-classify-marked-periods
title: Complex points of the model are classified by marked periods (statement form)
kind: theorem
decl: GlobalTheory.T.complexPoints_classify_markedPeriods
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ComplexPointsClassifyMarkedPeriodsStatement
covers: 431
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [GlobalTheory.UPel.HT.Model.fineAt_univ](/entry/fine-at-univ/), which has the real content. It is step 4 of [the complex uniformisation of the generic models](/entry/g-unif-of/): it gives `FineAt` for the integral model $M$.

## Statement

Use the datum $D$, the base $b$ over $R$ and the model $M$ of level $N$ of [the integral model entry](/entry/model-nonempty/). Let $g = mn[F:\mathbb{Q}]/2$ (`Datum.g`).

**Theorem.** Let $\sigma \colon R \to \mathbb{C}$ be a ring map and $\rho \colon O \to M_g(\mathbb{C})$ a ring map such that $b$ has type $(\sigma, \rho)$ (`Base.IsType`). Let $h$ say that the universal abelian scheme has relative dimension $g$, and $h_L$ that its polarization bundle on the diagonal is a line bundle. Let $0 < N$ with $\gcd(N, p) = 1$. Then the family `M.univ.fam h hL` is `FineAt` level $N$ for the class `D.Cls N`.

The [fineAt_univ entry](/entry/fine-at-univ/) explains `FineAt` and `D.Cls N`.

## Proof

The proof is `first | exact @GlobalTheory.UPel.HT.Model.fineAt_univ | ...`. The statements are the same. See [its entry](/entry/fine-at-univ/).

## In the Lean code

The theorem is in [ComplexPointsClassifyMarkedPeriodsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComplexPointsClassifyMarkedPeriodsStatement.lean#L9). It has two users. One is `gUnif_of`. The other is `model_uniformised` in [QuasiCompactOfQProj.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/QuasiCompactOfQProj.lean#L40), which passes it to `GlobalTheory.PELU.nonempty_unif` to get a full `Unif` for $M$ when $N \geq 3$.
