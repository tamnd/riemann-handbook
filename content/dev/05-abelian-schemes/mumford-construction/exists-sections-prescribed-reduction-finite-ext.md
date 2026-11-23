---
id: exists-sections-prescribed-reduction-finite-ext
title: Sections with a prescribed reduction after a finite extension (statement)
kind: theorem
decl: GlobalTheory.T.exists_sections_prescribed_reduction_finite_ext
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSectionsPrescribedReductionFiniteExtStatement
covers: 488
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_secs_finExt`](/entry/exists-secs-fin-ext/). It is step 1 of [`exists_emb_of_labCover`](/entry/exists-emb-of-lab-cover/). The content is in [`secs_exists`](/entry/secs-exists/).

## Statement

Let $R$ be a local domain with `Base R`, let $D$ be degeneration data over $R$ for its maximal ideal, and let $C$ be a labelled cover of $D$ ([`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/) unfolds these).

**Theorem.** There are a local domain $R_1$, a ring map $\rho \colon R \to R_1$, degeneration data $D_1$ over $R_1$ and a labelled cover $C_1$ of $D_1$ such that $\rho$ is a finite injective map to a complete normal noetherian local domain (`FinExt ρ`), $D_1$ is a pullback of $D$ along $\rho$ (`IsPullDeg`), and $C_1$ has a datum `Secs C₁.toModif C₁.G C₁.P.L.L C₁.α`.

A `Secs` datum is a family of sections of a power of the line bundle on the generic fibre whose reduction at the closed fibre is a fixed immersion of a smooth group into projective space, together with a theta section that does not vanish on an open part of that group. The [entry for `secs_exists`](/entry/secs-exists/) states it in full.

## Proof

The proof is the term `GlobalTheory.Mum.exists_secs_finExt`, which has the same statement.

## In the Lean code

The theorem is in [ExistsSectionsPrescribedReductionFiniteExtStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSectionsPrescribedReductionFiniteExtStatement.lean#L12). The proof is the usual `first | exact … ` form of a second name.

The name says "finite extension", but no extension is needed: `exists_secs_finExt` takes $R_1 = R$ and $\rho = \mathrm{id}$. The statement is weaker than what is proved, which is `Nonempty (Secs …)` for $C$ itself.
