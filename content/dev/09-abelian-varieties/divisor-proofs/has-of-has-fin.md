---
id: has-of-has-fin
title: Descent of a uniformisation along a finite extension, through a Galois closure
kind: theorem
decl: GlobalTheory.Mum.has_of_hasFin
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationOfFiniteExt
covers: 442
status: drafted
drafted_by: writer@claude
---
This theorem proves that a uniformisation over a finite extension of the base gives a uniformisation over the base. It makes the extension Galois, pulls the uniformisation up to the Galois extension, and then descends it with the Galois action. It is restated as [`hasSemiAbelianUniformisation_of_finiteExt`](/entry/has-semi-abelian-uniformisation-of-finite-ext/), and that name is used in steps 5 and 7 of [`has_of_base`](/entry/has-of-base/).

## Statement

Let $R$ be a local domain that satisfies `Base R` (noetherian, integrally closed, $\mathfrak{m}$-adically complete, characteristic zero), and let $D$ be degeneration data over $R$ for $\mathfrak{m}$. The [entry for `has_of_base`](/entry/has-of-base/) unfolds `DegData` and `Has`.

**Theorem.** If `HasFin D`, then `Has D`.

Here `HasFin D` says: there are a local domain $R'$, a map $\rho \colon R \to R'$ that is injective and finite, with $R'$ noetherian, normal and complete (`FinExt ρ`), and data $D'$ over $R'$ that are a pullback of $D$ (`IsPullDeg`), with `Has D'`.

## Proof

1. `exists_galois_closure_local_domain_extension`: there is a local map $\sigma \colon R' \to R''$ with `FinExt σ` and `FinExt (σ ∘ ρ)`, such that $\sigma \circ \rho$ is Galois (`IsGal`). In the Lean code this means: the group $\Gamma$ of ring automorphisms of $R''$ that fix the image of $R$ is finite, and its fixed ring is the image of $R$.
2. `exists_degenerationData_pullback_injective_localHom`: the data $D'$ have a pullback $D''$ over $R''$.
3. `hasSemiAbelianUniformisation_pullback_injective_local`: `Has D'` gives `Has D''`, with a semi-abelian $G''$ over $R''$, an abelian variety $A''$ and a uniformisation $U$.
4. `PullDegComp.nonempty_isPullDeg_comp`: $D''$ is also a pullback of $D$ along $\sigma \circ \rho$.
5. `exists_galoisAction_on_uniformisedGroup_pulledData`: $\Gamma$ acts on $G''$ over its action on $\operatorname{Spec} R''$, compatibly with $U$ (`GalAct`).
6. [`uniformised_semiAbelian_galois_descent`](/entry/uniformised-semi-abelian-galois-descent/): a uniformised semi-abelian scheme over a Galois extension with such an action gives `Has D`.

Step 6 is the descent. Steps 1 to 5 only set up its hypotheses.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationOfFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfFiniteExt.lean#L21). The proof has six lines, one for each step. `IsGal` and `GalAct` are in [QuasiCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/QuasiCompact.lean#L81). The composition lemma of step 4 is in [HasSemiAbelianUniformisationOfFiniteExtTrans.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfFiniteExtTrans.lean#L34).

We read the statements of the lemmas in steps 1 to 5, not their proofs. All hypotheses are used. The map $\sigma$ must be local only for step 2 and step 3.
