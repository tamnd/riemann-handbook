---
id: exists-secs-fin-ext
title: Sections with a prescribed reduction, with the trivial extension
kind: theorem
decl: GlobalTheory.Mum.exists_secs_finExt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSectionsPrescribedReductionFiniteExt
covers: 487
status: drafted
drafted_by: writer@claude
---
This theorem proves [`exists_sections_prescribed_reduction_finite_ext`](/entry/exists-sections-prescribed-reduction-finite-ext/). It puts the result of [`secs_exists`](/entry/secs-exists/) into the form of a statement over a finite extension, and it takes the identity as that extension. The content is in `secs_exists`.

## Statement

The statement is the one in the [statement entry](/entry/exists-sections-prescribed-reduction-finite-ext/): for $R$ with `Base R`, degeneration data $D$ over $R$ and a labelled cover $C$ of $D$, there are $\rho \colon R \to R_1$ with `FinExt ρ`, a pullback $D_1$ of $D$ along $\rho$, and a labelled cover $C_1$ of $D_1$ with a `Secs` datum.

## Proof

Take $R_1 = R$, $\rho = \mathrm{id}_R$, $D_1 = D$ and $C_1 = C$. Then:

- `FinExt id` holds: $R$ is noetherian, integrally closed and complete by the first part of `Base R`, and the identity is injective and finite (`RingHom.Finite.id`).
- $D$ is a pullback of itself along the identity, by `GlobalTheory.DegPullId.exists_isPullDeg_id_self`.
- $C$ has a `Secs` datum, by `GlobalTheory.Mum.SecsAsm.secs_exists`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsSectionsPrescribedReductionFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSectionsPrescribedReductionFiniteExt.lean#L120). The lemmas it calls:

- `GlobalTheory.DegPullId.exists_isPullDeg_id_self`, in [ExistsPullDegIdentitySelfAdmissible.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPullDegIdentitySelfAdmissible.lean#L14). It also says that the identification is the identity on the lattice and on the abelian part; this proof drops those clauses.
- `GlobalTheory.Mum.SecsAsm.secs_exists`, at [line 34](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSectionsPrescribedReductionFiniteExt.lean#L34) of the same file.

The name says "finite extension", but the extension is the identity. The existential form only matches the shape that [`exists_emb_of_labCover`](/entry/exists-emb-of-lab-cover/) expects.
