---
id: has-ext-of-setup
title: Extension from a setup, second name
kind: theorem
decl: GlobalTheory.Desc.hasExt_of_setup
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasExtOfSetup
covers: 429
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`Setup.hasExt`](/entry/has-ext/). Its only user is [`hasExt_awayMap_of_charts`](/entry/has-ext-away-map-of-charts/), which builds a `Setup` from the charts and an ample divisor and then calls this theorem.

## Statement

**Theorem.** Let $\sigma$ be a `Setup`: a noetherian integrally closed domain $R$, an element $f \neq 0$, an abelian scheme $A$ over $\operatorname{Spec} R_f$ with an ample divisor $D$, and at each point $x$ of $\operatorname{Spec} R$ a chart $G_x$ with the closure $D_{1,x}$ of $D$ on it. Then $A$ extends to a semi-abelian scheme over $\operatorname{Spec} R$.

The fields of `Setup` are listed in [`Setup.hasExt`](/entry/has-ext/). Extensions are defined in [`hasExt_opensRange`](/entry/has-ext-opens-range/).

## Proof

The proof is the term `Setup.hasExt`. The theorem is stated as `∀ σ : Setup, HasExt (awayMap σ.f) σ.A`, and `Setup.hasExt` has the same type with $\sigma$ as an explicit argument. There is nothing else.

## In the Lean code

The theorem is at [HasExtOfSetup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasExtOfSetup.lean#L20), five lines below `Setup.hasExt` in the same file. The definition is `hasExt_of_setup : ∀ σ : Setup, HasExt (awayMap σ.f) σ.A := Setup.hasExt`. The second name gains nothing: the caller could use `Setup.hasExt` or `σ.hasExt` directly.
