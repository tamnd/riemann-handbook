---
id: exists-is-gauge
title: A gauge family for the CM extension of the data
kind: theorem
decl: GlobalTheory.GaugeEx.exists_isGauge
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsIsGaugeOfIsCMExt
covers: 497
status: drafted
drafted_by: writer@claude
---
This theorem gives a gauge family of measures on the adelic unitary groups of a CM extension $E/F$ that is given as `CMData`. It is step 3 of [the built core](/entry/step-w-core/). It only changes the form of the hypothesis and then applies [`exists_isGauge_of_isCMExt`](/entry/exists-is-gauge-of-is-cmext/), which has the mathematics.

## Statement

Let $F$ and $E$ be number fields, with $E$ an $F$-algebra with a star operation. `CMData F E` says: $F$ is totally real, $[E:F] = 2$, the star fixes exactly $F$, and `IsCMUnram E` holds. `IsCMUnram E` says that $E$ is totally complex, that each embedding $\varphi \colon E \to \mathbb{C}$ takes the star to complex conjugation, and a condition at each maximal ideal of the integers of $E$. Let $\sigma$ be the star, as an $F$-algebra map (`cm.sig`; the fixed field clause makes it $F$-linear).

**Theorem.** For each `cm : CMData F E` there is a gauge family $G$ for $\sigma$ with `G.IsGauge`.

## Proof

The proof builds `IsCMExt F E σ` from four clauses: `cm.totReal`, the first and second clauses of `cm.cmUnram`, and `cm.deg2`. Then it applies `exists_isGauge_of_isCMExt`.

## In the Lean code

The theorem is in [ExistsIsGaugeOfIsCMExt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L205). `CMData` and `CMData.sig` are in [DataSpaces.lean](lean:Formalism/LocalRingCardinality/DataSpaces.lean#L14), and `IsCMUnram` is in [CMTraceOnto.lean](lean:Formalism/PeriodIntegrals/CMTraceOnto.lean#L9).

The third clause of `IsCMUnram`, the condition at maximal ideals, is not used. So the theorem holds for a weaker hypothesis than `CMData`.
