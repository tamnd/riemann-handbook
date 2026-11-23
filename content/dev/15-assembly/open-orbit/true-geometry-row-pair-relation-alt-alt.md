---
id: true-geometry-row-pair-relation-alt-alt
title: The common rational datum of the off part, in statement form
kind: theorem
decl: GlobalTheory.T.true_geometry_row_pair_relation_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RatDatumXiOffCommonStatement
covers: 308
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ratDatum_xiOff_common_alt`](/entry/rat-datum-xi-off-common-alt/). Its only user is [`QuadraticExtensionData.dat_exists`](/entry/dat-exists/), which takes from it the constants $C_j$ and the rational datum of the off part of the twisted function, before it adds the local combinations of the quadratic extension data. Through the restatement [`true_geometry_row_pair_relation_alt_alt_alt`](/entry/true-geometry-row-pair-relation-alt-alt-alt/), that result goes to step 2 of [the column side of a geometric family](/entry/col-side-alt/). The real content is in `ratDatum_xiOff_common_alt`.

## Statement

The statement is word for word the statement of [`ratDatum_xiOff_common_alt`](/entry/rat-datum-xi-off-common-alt/). In short: let $W$ be a real package with `AllFamilyConditions W`, $u$ a word and $a$ a geometric family with `a.Is`, `a.True` and top matrix $i_A = 1$ at level $m$. Then there are constants $C_j \neq 0$ for $j < m$ such that, for each $t$, each quadratic extension datum $J$ with `J.Reads`, each idempotent sum $e$ on the places $v_T(u) \cup v_{G}$ and each $j < m$ and characters $\alpha$, $\gamma$, the function $z \mapsto C_j\, \xi^{\mathrm{off}}_j(\alpha, \gamma)(z)$ is a rational datum at $e$ for the vacuum of level $j$ and its image under the combinations $d_T(j)$ and then $d_G(j)$.

## Proof

The proof applies `ratDatum_xiOff_common_alt`. Nothing else happens.

## In the Lean code

The theorem is at [RatDatumXiOffCommonStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RatDatumXiOffCommonStatement.lean#L18). The proof is the tactic `first | exact @GlobalTheory.Fam.ratDatum_xiOff_common_alt | ...`, so the theorem only passes its hypotheses along. The name speaks of a "row pair relation". The statement is a rational datum for the off part $\xi^{\mathrm{off}}$, the name of the file.
