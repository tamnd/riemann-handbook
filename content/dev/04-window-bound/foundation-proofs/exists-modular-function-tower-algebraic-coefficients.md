---
id: exists-modular-function-tower-algebraic-coefficients
title: A tower of modular functions with algebraic coefficients exists
kind: theorem
decl: GlobalTheory.T.exists_modular_function_tower_algebraic_coefficients
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsModularFunctionTowerAlgebraicCoefficientsStatement
covers: 334
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`tower_exists`](/entry/tower-exists/). It says that for each algebraic closure $\Omega$ of $\mathbb{Q}$ and each embedding $\varepsilon \colon \Omega \to \mathbb{C}$ there is a tower of modular functions over $\Omega$ whose $j$-function is the classical one. [The theorem `towerEx`](/entry/tower-ex/) uses it and keeps only the existence of the tower.

## Statement

**Theorem.** Let $\Omega$ be an algebraic closure of $\mathbb{Q}$ and $\varepsilon \colon \Omega \to \mathbb{C}$ a ring map. Then there is a tower $T$ of modular functions over $(\Omega, \varepsilon)$ with $\mathrm{IsStd}(T)$.

A tower (the Lean structure `GlobalTheory.KZ.Tower`) is a field $K$ over $\Omega$ with a $q$-expansion map, an action of $\mathrm{GL}_2^+(\mathbb{Q})$, an action of $\mathrm{Gal}(\Omega/\mathbb{Q})$, an analytic realization as meromorphic functions on the upper half plane, and a distinguished element $j_K$. [The entry for `tower_exists`](/entry/tower-exists/) lists its axioms. $\mathrm{IsStd}(T)$ says that the analytic realization of $j_K$ is the germ of the classical function $j = E_4^3/\Delta$.

## Proof

The proof is `tower_exists`. Nothing else happens.

## In the Lean code

The theorem is in [ExistsModularFunctionTowerAlgebraicCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsModularFunctionTowerAlgebraicCoefficientsStatement.lean#L12). Its proof is a `first | ... | ...` tactic whose three alternatives all apply `GlobalTheory.FN.tower_exists`. `Tower` is in [ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L42), and `IsStd` is in [MemRingOfInR.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/MemRingOfInR.lean#L42).

The parent `towerEx` drops $\mathrm{IsStd}$: its statement $\mathrm{TowerEx}$ asks only that the type of towers is nonempty.
