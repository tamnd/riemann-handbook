---
id: tower-ex
title: A tower of modular functions exists
kind: theorem
decl: UpperTheory.V.Z.Kato.Joint.towerEx
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.FrobeniusHodgeTateLaws.TowerEx
covers: 335
status: drafted
drafted_by: writer@claude
---
This theorem says that for each algebraic closure $\Omega$ of $\mathbb{Q}$ and each embedding $\varepsilon \colon \Omega \to \mathbb{C}$ there is a tower of modular functions. It is one of the proved inputs of `glue2` in [the global unit law of smoothed classes](/entry/kato-global-unit-law-of-smoothed-classes/). It is a weak form of a proved theorem.

## Statement

**Theorem.** Let $\Omega$ be an algebraic closure of $\mathbb{Q}$ and $\varepsilon \colon \Omega \to \mathbb{C}$ a ring map. Then the type `Tower Ω ε` is not empty.

A tower is a field $K$ with $q$-expansions, an action of $\mathrm{GL}_2^+(\mathbb{Q})$, a Galois action, a map to meromorphic germs on the upper half plane, levels, Shimura reciprocity, a $j$-function `jK`, bounded denominators and a $q$-expansion principle. We have not unfolded each of these fields of `Tower`.

## Proof

The theorem [`exists_modular_function_tower_algebraic_coefficients`](/entry/exists-modular-function-tower-algebraic-coefficients/) gives a tower $T$ with `IsStd T`, that is, the $j$-function of $T$ is the classical $j$-function. The proof keeps $T$ and drops `IsStd T`. The real content is in [`tower_exists`](/entry/tower-exists/), which builds the tower.

## In the Lean code

The proof is three lines in [TowerEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/TowerEx.lean#L6). The statement `TowerEx` is in [ThickFrames.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/ThickFrames.lean#L111), and `Tower` is in [ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L42).

The conclusion is weaker than the theorem it uses, because it forgets `IsStd`. A different declaration with the name `TowerEx` is in [TwistedInnerProducts/TowerEx.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TowerEx.lean#L229). It is not related.
