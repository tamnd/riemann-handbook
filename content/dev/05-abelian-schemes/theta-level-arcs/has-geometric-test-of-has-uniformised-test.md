---
id: has-geometric-test-of-has-uniformised-test
title: Uniformised tests give geometric tests (statement form)
kind: theorem
decl: GlobalTheory.T.hasGeometricTest_of_hasUniformisedTest
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.HasGeometricTestOfHasUniformisedTestStatement
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`GeoExist.hasGeo_of_hasU`](/entry/has-geo-of-has-u/), with the same type. It is step 3 of [`baseFacts_hasGeo_exists_clos`](/entry/base-facts-has-geo-exists-clos/), and it is the only place where that theorem uses `UTorsSt`.

## Statement

**Theorem.** Assume `UT.LL` and `UTorsSt`. Let $S$ be a theta system over $o \subset \Omega$ with `S.Big`, and $\rho$ a realization of $S$. If $\rho$ has uniformised tests (`HasU`), then $\rho$ has geometric tests (`HasGeo`).

Both properties are for each prime $p$, each $y_0 \colon R \to \mathbb{C}_p$ integral on $o$, and each finite set $F_s$ of elements of $\mathbb{C}_p$. A uniformised test is a complete discrete valuation ring $V$ in $\mathbb{C}_p$ that contains $F_s$ in its fraction field, with degeneration data and a uniformisation of $A$ over $V$, a label map, and a test of $S$ that matches it. A geometric test adds sections $\sigma$ of an adapted basis, a model (`Mod`), and an invertible link matrix $b$ whose rows span the test lattice over $\mathcal{O}_p$ and have the class weights.

## Proof

The proof is the tactic `first | exact @GlobalTheory.ZH.GeoExist.hasGeo_of_hasU | ...`. The two types agree, so the first branch closes the goal.

## In the Lean code

The theorem is in [HasGeometricTestOfHasUniformisedTestStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTestStatement.lean#L14). It is a renaming. The file sets `maxHeartbeats` to 1000000 for this one-line proof. The real proof is in [HasGeometricTestOfHasUniformisedTest.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTest.lean#L33). It builds the geometric test from the uniformised one with five lemmas and `link_smul`.
