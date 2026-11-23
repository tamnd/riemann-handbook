---
id: bottom-field-is-number-field
title: The values of the bottom triangles lie in one number field
kind: theorem
decl: GlobalTheory.RowEx.bottomField_isNumberField
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.BottomFieldIsNumberField
covers: 555
status: drafted
drafted_by: writer@claude
---
This theorem proves `NFBot`. For each choice of data there is one number field $M \subset \mathbb{C}$ such that, at every stage $(i, j)$ of the grid, some bottom triangle has all its theta integral values in $M$, up to two fixed periods. The proof takes a field for each stage from [`sums_mem_bottomField`](/entry/sums-mem-bottom-field/) and forms the compositum. That entry has the real content. The theorem is used in item 4 of [the last node of the trunk](/step/nonempty-hyps/), through `evaluation_grid_of_join`, and also by `exists_extension_field_of_join`. Below this theorem are 555 declarations.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/) and `NormSum.Inp D` for every datum $D$. Then `NFBot` holds.

`NFBot` is `Big Q`. `Big Q` says: there is $CF_0$ such that for all $\varepsilon$ and $CF \ge CF_0$ there is $x_0$ such that, for every datum $D$ with $\varepsilon$ and $x \ge x_0$, every real datum $R$ and face $F$ in a `HidaSetting`, and every choice `ch` with `ch.Is` and `ch.AtScale CF b`, the property $Q$ holds for `ch`.

Here $Q$ is `InNF (BotCl ch.W)`: there is a subfield $M \subset \mathbb{C}$, finite over $\mathbb{Q}$, such that for all $i, j$ there is a triangle $X$ with:

- `IsBottomTri W i j X`: the two sides have the bottom ranks `botBig` and `botSmall`, the three rigidifications are standard, and $X$ carries the characters of the stage $(i, j)$;
- `SumsIn W M X`: there are $\Omega, \Omega' \neq 0$ such that for each $t$, each $h$ with trivial archimedean part (`GfC`), and each monomial $x^k$ with an integrable kernel, $I_t(x^k)(h)/\Omega \in M$ and $I'_t(x^k)(h)/\Omega' \in M$.

Here $I_t$ and $I'_t$ are the theta integrals of the two sides of $X$ over a fundamental domain (`Tri.I`, `Tri.I'`). We have not unfolded `NormSum.Inp`, a structure of 22 propositions, or `HidaSetting`.

## Proof

1. Take $CF_0 = 0$ and $x_0 = 0$.
2. The setting gives that $T$ is finite and that `L.Is μ₀` holds for the level character $L$, which we have not unfolded.
3. For each pair $(i, j)$, `exists_bottomTri` gives a bottom triangle $X_{ij}$. Then `sums_mem_bottomField` gives a number field $M_{ij}$ with `SumsIn W M_ij X_ij`.
4. Put $M = \bigvee_{i,j} M_{ij}$. There are finitely many pairs, so $M$ is finite over $\mathbb{Q}$ (`IntermediateField.finiteDimensional_iSup_of_finite`).
5. `sumsIn_mono` moves `SumsIn` from $M_{ij}$ to the larger field $M$.

## In the Lean code

The theorem is at [BottomFieldIsNumberField.lean line 30](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomFieldIsNumberField.lean#L30). `NFBot`, `InNF` and `BotCl` are in [TwistPlacesOffPrimeQZero.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TwistPlacesOffPrimeQZero.lean#L44). `IsBottomTri` and `SumsIn` are in [MemHalfCosetSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/MemHalfCosetSelf.lean#L203). `Big` is in [FormulaAt.lean](lean:Development/AbelianVarietyTheory/Statements/HeckeThetaIntegrals/FormulaAt.lean#L68). `exists_bottomTri` is in [BottomExistsIntegrable.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/BottomExistsIntegrable.lean#L104).

Odd points:

- The thresholds are $0$, and the proof does not use `ch.Is` or `ch.AtScale`. The scale plays no role.
- [NormalFormBottom.lean line 69](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalFormBottom.lean#L69) has `RowEx.nfBot_holds`, with the same statement and the same proof, except that it takes `FunPr.Hypotheses₂` in place of `ThetaLocalInputs`.
