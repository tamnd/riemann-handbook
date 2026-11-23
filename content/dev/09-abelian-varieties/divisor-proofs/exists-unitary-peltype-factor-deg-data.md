---
id: exists-unitary-peltype-factor-deg-data
title: Degeneration data are a factor of data of unitary PEL type (statement)
kind: theorem
decl: GlobalTheory.T.exists_unitaryPELType_factor_degData
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryPELTypeFactorDegDataStatement
covers: 559
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.exists_pelOK_factor`](/entry/exists-pel-ok-factor/), which has the real content. Its proof only calls that theorem. It is step 2 of [`has_of_base`](/entry/has-of-base/): it reduces Mumford's construction for general degeneration data to data with an action of the integers of a CM field.

## Statement

Let $R$ be a local domain with maximal ideal $\mathfrak{m}$ that satisfies `Base R` (noetherian, integrally closed, $\mathfrak{m}$-adically complete, of characteristic zero). Let $D$ be degeneration data over $R$ for $\mathfrak{m}$ (`DegData`, unfolded in the [entry for `has_of_base`](/entry/has-of-base/)) whose lattice $X$ is not zero.

**Theorem.** There are a CM field $E$, a host $H$ for $E$, a unitary datum $\mathrm{Dm}$ for $H$, degeneration data $D'$ over $R$ with an $\mathcal{O}_E$-module structure on its lattice and an action $o$ of $\mathcal{O}_E$ on $D'$, such that

1. $(\mathrm{Dm}, D', o)$ is of unitary PEL type with signature $p = q \geq 1$ (`PelOK`);
2. $D$ is a factor of $D'$ (`Factor`) that satisfies the condition `Factor.Alg`.

The [entry for `exists_pelOK_factor`](/entry/exists-pel-ok-factor/) unfolds `Host`, `Datum`, `PelOK` and `Factor.Alg`.

## Proof

The proof is `Mum.exists_pelOK_factor`.

## In the Lean code

The theorem is in [ExistsUnitaryPELTypeFactorDegDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryPELTypeFactorDegDataStatement.lean#L13). The proof is the tactic `first | exact @GlobalTheory.Mum.exists_pelOK_factor | ...`. The two statements are identical, so `exact` closes the goal.
