---
id: closure-model
title: Limits of discrete series coefficients are coefficient series (third name)
kind: theorem
decl: GlobalTheory.ClosureSeries.closure_model
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.AutomorphicFormUniformLimitDiscreteSeriesSeries
covers: 562
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`hasAllKTypes_of_closure_discreteSeriesCoefficients`](/entry/has-all-ktypes-of-closure-discrete-series-coefficients/), which is itself a second name for [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/). The real content is in `hasTypeAll_of_closure`. In the same file, `closure_to_series` uses it to prove `automorphicForm_uniformLimit_discreteSeries_series`, the Type step of [`cuspidal_lift_smooth_at_of_cuspidal_lift`](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/).

## Statement

Let $G = U(p,q) = \{g : g^* J_\varepsilon g = J_\varepsilon\}$ (`UJset ε`), and let $\sigma$ be a [[discrete series|9AB7HYGPEK]] representation of $G$ with Harish-Chandra parameter $\lambda$ (`IsHCParam`, `IsDS`). Assume `HarishChandraModules` and `CasselmanWallach`.

**Theorem.** Let $f$ be continuous on $G$ and of uniform moderate growth (`UMG`). Suppose that for each compact set $C$ and each $\delta > 0$ there are finitely many Sobolev functionals $\ell_j$ and smooth vectors $v_j$ with $\lvert f(y) - \sum_j \ell_j(\sigma(y) v_j) \rvert < \delta$ for $y \in C \cap G$. Then $f(g) = \sum_i \ell_i(\sigma(g) v_i)$ on $G$, a series that converges absolutely in every Sobolev seminorm (`HasTypeAll`).

The entry for [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/) defines each object.

## Proof

The proof is the term `GlobalTheory.T.hasAllKTypes_of_closure_discreteSeriesCoefficients`. The two statements are equal.

## In the Lean code

The theorem is at [AutomorphicFormUniformLimitDiscreteSeriesSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/AutomorphicFormUniformLimitDiscreteSeriesSeries.lean#L49). The name says "model", but the statement is about closures and series of matrix coefficients; there is no model in it. With the two names above it, one statement has three names. Its other caller is in `SeriesAverageOtherPlaceType.lean`, line 128.
