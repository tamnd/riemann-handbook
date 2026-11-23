---
id: sums-mem-bottom-field
title: The values of one bottom triangle lie in a number field
kind: theorem
decl: GlobalTheory.RowEx.BotField.sums_mem_bottomField
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.BottomFieldIsNumberField
covers: 553
status: drafted
drafted_by: writer@claude
---
This lemma treats one bottom triangle $X$. It gives a number field $M \subset \mathbb{C}$ that holds the theta integral values of both sides of $X$, up to two periods. [The field of all bottom triangles](/entry/bottom-field-is-number-field/) uses it at each stage and takes the compositum. The proof is a short argument on fields. The real content is in four lemmas on spanning and algebraicity, which this lemma calls. Below this lemma are 553 declarations.

## Statement

**Lemma.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/) and `NormSum.Inp D` for every $D$. Let $T$ be finite, let `L.Is μ₀` hold for the level character $L$, and let $X$ be a bottom triangle at the stage $(i, j)$ (`IsBottomTri`). Then there is a subfield $M \subset \mathbb{C}$, finite over $\mathbb{Q}$, with `SumsIn W M X`.

`IsBottomTri` and `SumsIn` are as in [the parent entry](/entry/bottom-field-is-number-field/). In short, there are $\Omega, \Omega' \neq 0$ with $I_t(x^k)(h)/\Omega \in M$ and $I'_t(x^k)(h)/\Omega' \in M$ for all $t$, all monomials $x^k$ with an integrable kernel, and all $h$ in `GfC`.

## Proof

The core is `field_of_gens`. Let $v(t, h, k)$ be values. Assume that there are finite sets $H$ and $K$ and a number field $M_0$ such that each $v(t, h, k)$ is an $M_0$-linear combination of the values $v(t, h', k')$ with $h' \in H$ and $k' \in K$. Assume also that there is $\Omega \neq 0$ with each $v/\Omega$ algebraic over $\mathbb{Q}$. Then all $v/\Omega$ lie in $M_0(S)$, where $S$ is the finite set of the $v(t, h', k')/\Omega$. This field is finite over $\mathbb{Q}$ because $T$ is finite.

1. Apply `field_of_gens` to $v = I_t(x^k)(h)$. The spanning input is `bottom_spanned_by_classSums`, and the algebraicity input is `bottom_classSums_algebraic`. This gives $M_1$ and $\Omega$.
2. Apply it to $v = I'_t(x^k)(h)$, with `bottom_spanned_by_twistedClassSums` and `bottom_twistedClassSums_algebraic`. This gives $M_2$ and $\Omega'$.
3. Take the compositum $M = M_1 M_2$.

## In the Lean code

The lemma is at [BottomFieldIsNumberField.lean line 18](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomFieldIsNumberField.lean#L18). `field_of_gens` is in [NormalFormBottom.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalFormBottom.lean#L26).

The four inputs are `first | exact` wrappers. For example, `bottom_spanned_by_classSums` at [BottomSpannedByClassSums.lean line 81](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomSpannedByClassSums.lean#L81) wraps `BotSpan.classSums_span_bottom` at line 26, and `bottom_classSums_algebraic` wraps `BotAlgI.classSums_isAlgebraic` at [ClassSumKernelIsAlgebraic.lean line 63](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ClassSumKernelIsAlgebraic.lean#L63). We did not follow their proofs.

Odd points:

- The proof shows the membership for every monomial and every $h$ in `GfC`. The integrability premise in `SumsIn` is not used.
- [NormalFormBottom.lean line 49](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalFormBottom.lean#L49) has `sumsIn_bottom`, with the same statement and proof. It takes `FunPr.Hypotheses₂` in place of `ThetaLocalInputs` and calls four other lemmas.
