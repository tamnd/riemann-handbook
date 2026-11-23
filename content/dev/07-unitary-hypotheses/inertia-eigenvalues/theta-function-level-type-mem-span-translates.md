---
id: theta-function-level-type-mem-span-translates
title: Clean theta functions of level type are spans of translates, the statement form
kind: theorem
decl: GlobalTheory.T.thetaFunction_levelType_mem_span_translates
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ThetaFunctionLevelTypeMemSpanTranslatesStatement
covers: 408
status: drafted
drafted_by: writer@claude
---
This theorem is a second name with no content of its own. It states the result of [`gen_of_type_clean`](/entry/gen-of-type-clean/) and proves it by calling that theorem. Its only user is [`genFin`](/entry/gen-fin/), in step 3 of its proof.

## Statement

Let $R$, $F$, $i$, $t$ be as in [`genFin`](/entry/gen-fin/), and assume `HoweUnram`, `Given R F` and `R.FullP`. Let $f$ be a theta function of level type (`TypeVec`: the level group of $V$ acts on $f$ by the inverse of the level character) that is clean (`Clean`: each level average `avgW` of $f$ is zero). Then $f$ is in the span of the translates $\omega(1, g)f'$, with $g \in U(W)(\mathbb A)$ and $f'$ of finite type (the set `Gen R i t`).

## Proof

The proof is `first | exact @GlobalTheory.DownLift.GenFinite.gen_of_type_clean | ...`. It applies that theorem. The statements are identical.

## In the Lean code

The theorem is at [ThetaFunctionLevelTypeMemSpanTranslatesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaFunctionLevelTypeMemSpanTranslatesStatement.lean#L12). The target is at [ThetaFunctionLevelTypeMemSpanTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaFunctionLevelTypeMemSpanTranslates.lean#L66). The file sets `maxHeartbeats` to 1,000,000 for a proof of one line.
