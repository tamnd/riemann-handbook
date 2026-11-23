---
id: has-all-ktypes-of-closure-discrete-series-coefficients
title: Limits of discrete series coefficients are coefficient series, restated
kind: theorem
decl: GlobalTheory.T.hasAllKTypes_of_closure_discreteSeriesCoefficients
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.HasAllKTypesOfClosureDiscreteSeriesCoefficientsStatement
covers: 561
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/), and that entry has the real content. Its only caller is [`closure_model`](/entry/closure-model/), which is itself a second name for this theorem. Below this theorem are 561 declarations; all but one are below `hasTypeAll_of_closure`.

## Statement

Let $G = U(p,q) \subset \mathrm{GL}_n(\mathbb{C})$ and let $\sigma$ be a [[discrete series|9AB7HYGPEK]] representation of $G$ with Harish-Chandra parameter $\lambda$. Assume the literature statements `HarishChandraModules` and `CasselmanWallach`.

**Theorem.** Let $f$ be a continuous function on $G$ of uniform moderate growth. Suppose that on each compact set, $f$ is a uniform limit of finite sums $\sum_j \ell_j(\sigma(y) v_j)$, with $v_j$ smooth vectors and $\ell_j$ functionals bounded by a Sobolev seminorm. Then $f(g) = \sum_{i \geq 0} \ell_i(\sigma(g) v_i)$ on $G$, a series that converges absolutely in every Sobolev seminorm.

The [entry for `hasTypeAll_of_closure`](/entry/has-type-all-of-closure/) defines each object.

## Proof

The proof is the term `hasTypeAll_of_closure`. The rest is bookkeeping.

## In the Lean code

The theorem is in [HasAllKTypesOfClosureDiscreteSeriesCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/HasAllKTypesOfClosureDiscreteSeriesCoefficientsStatement.lean#L17). The proof is the tactic `first | exact @hasTypeAll_of_closure | ...`. The two statements are the same, so the first branch suffices.

The name speaks of "all $K$-types", but the conclusion is `HasTypeAll`: a series of matrix coefficients that converges in all Sobolev norms. The hypothesis `IsHCParam lam` is not used in the proof below it. The chain `closure_model`, this theorem, `hasTypeAll_of_closure` gives three names to one statement.
