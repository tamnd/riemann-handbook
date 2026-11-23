---
id: has-geo-of-has-u
title: A geometric test from a uniformised test
kind: theorem
decl: GlobalTheory.ZH.GeoExist.hasGeo_of_hasU
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.HasGeometricTestOfHasUniformisedTest
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem proves [`hasGeometricTest_of_hasUniformisedTest`](/entry/has-geometric-test-of-has-uniformised-test/), which has the same statement and only calls it. It turns a uniformised test at each prime into a geometric test. The theorem itself does little: it puts five lemmas together and scales one matrix. The work is in those five lemmas.

## Statement

Assume `LL` (the five bundles `Laws` to `Laws5` of facts on abelian schemes) and `UTorsSt` (the torsion points of the generic fibre of a uniformisation, read off from the degeneration data). Let $o \to \Omega$ be an `ArithBase`: $o$ is a Dedekind domain of finite type over $\mathbb{Z}$, $\Omega$ is a field of characteristic zero, and $o \to \Omega$ is injective. Let $S$ be a theta system over $(o, \Omega)$ and let $\rho$ be a realisation of $S$ by a polarized abelian scheme with theta structure. Suppose that $S$ is big, that is, $N$ and $rN$ are large in terms of $g$.

If $\rho$ has uniformised tests (`HasU`), then $\rho$ has geometric tests (`HasGeo`). `HasU` says: for each prime $p$, each $y_0$ with $\|y_0(a)\| \le 1$ for all $a \in o$, and each finite set of values, there are a uniformisation $u$ over a complete DVR, a labelling $l$ and a $p$-adic test $\tau$ that match. `HasGeo` asks for the same data and, in addition, a model with theta series, an invertible link matrix $b$, the equality of the test lattice with the span of the rows of $b$, and the weights of these rows.

## Proof

Take $u$, $l$, $\tau$ from `HasU`. Then:

1. `exists_adapted_basis_sections_mod_k` (with $k = N$) gives an adapted basis $\sigma$ with classes `cls`.
2. `uniformisedModel_adaptedBasis_is_modelWithSeries` gives a model with series for $\sigma$.
3. `exists_invertible_adaptedBasis_link_matrix` gives a matrix $b$ over $\operatorname{Frac} V$ with $\det b \neq 0$ that links $u$ and $\sigma$.
4. `testLattice_eq_span_model_sections` gives $c \neq 0$ such that the test lattice is the $O_p$-span of the rows of $cb$. This step uses that $S$ is big.
5. The local lemma `link_smul` shows that $cb$ is still a link matrix.
6. `adaptedBasis_rows_have_class_weight` gives the weights of the rows of $cb$.

These data form the geometric test.

## In the Lean code

The theorem is in [HasGeometricTestOfHasUniformisedTest.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTest.lean#L33), and `link_smul` is at [L21](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTest.lean#L21). The five lemmas are in the `*Statement.lean` files of the same folder. Each is a second name for a lemma in another file. I have not unfolded `Link`, `Basis` or `Mod`. The hypothesis `UTorsSt` is used only in steps 2 and 6, and bigness only in step 4.
