---
id: siegel-weil-formula-degree-succ
title: The Siegel-Weil step from degree N to degree N plus one, as a statement
kind: theorem
decl: GlobalTheory.T.siegelWeil_formula_degree_succ
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.SiegelWeilFormulaDegreeSuccStatement
covers: 424
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It states the induction step that [siegel-weil-definite](/entry/siegel-weil-definite/) uses, and its proof only calls [sw-at-succ](/entry/sw-at-succ/). The real content is in that entry.

## Statement

Let $E$ be a CM field with a CM type $\Psi$. Let $n$ be even and let $N$ satisfy $4(N+1) < n$. If `SWAt Ψ n N` holds, then `SWAt Ψ n (N+1)` holds.

`SWAt Ψ n N` says that, for every admitted family of functions on $n \times N$ matrices over $E$, the weighted class sum of theta series equals the class sum of Eisenstein series at every point of the Hermitian upper half space of degree $N$. The entry [siegel-weil-definite](/entry/siegel-weil-definite/) explains the parts of this statement.

## Proof

The proof is one tactic line: `first | exact @GlobalTheory.SW.swAt_succ | ...`. The first branch closes the goal, because `swAt_succ` has the same statement word for word.

## In the Lean code

The theorem is in [SiegelWeilFormulaDegreeSuccStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilFormulaDegreeSuccStatement.lean#L9), in the namespace `GlobalTheory.T`. The proof it calls is `GlobalTheory.SW.swAt_succ` in [SiegelWeilFormulaDegreeSucc.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilFormulaDegreeSucc.lean#L242). The other branches of the `first` tactic are fallbacks that are never reached.
