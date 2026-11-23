---
id: ordinary-curve-hodge-prime
title: The test point clause of the lattice families, second name
kind: theorem
decl: GlobalTheory.T.ordinary_curve_hodge_prime
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.OrdinaryCurveHodgePrimeStatement
covers: 1032
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the facts at test points](/entry/test-pt-test-facts/). It has the same statement, and its proof only calls that theorem. [The existence of lattice families](/entry/family-exists-pos-holds/) uses it once, for the test clause of `IsPreFamily`. The real content is in [the entry of `testFacts`](/entry/test-pt-test-facts/).

## Statement

**Theorem.** Assume the five inputs `FarguesHodgeTate`, `QuotientByFiniteFlatStatement`, `ZarhinStatement`, `HodgeTateDatumStatement` and `OrdinaryCurveStatement` of [the lattice families](/entry/family-pos-of-hodge-tate-inputs/). Take the data of `FamilyExistsPos` at a place $O$ above $p$, the orbit data $(\Sigma, e, \varphi', F, w, \sigma)$, the torsion data, an open chart $c$ with its chart pack, and maps $i_\tau$ with the exact sequence conditions, such that the chart data $D_c$ satisfy `Base`. Then for each test point $R_C \subset C$ of the chart ring and each lift $\chi$ of $\sigma$ to $C$, the base change of $D_c$ to $R_C$ satisfies `Facts`.

The [entry of `testFacts`](/entry/test-pt-test-facts/) states the test points, the lifts and the six clauses of `Facts`.

## Proof

The proof is `testFacts`. Nothing else is done.

## In the Lean code

The theorem is in [OrdinaryCurveHodgePrimeStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/OrdinaryCurveHodgePrimeStatement.lean#L11). The proof is the tactic `first | exact @testFacts | ...`, and the first branch closes the goal. The caller is `familyExistsPos_holds`, at [line 124 of FamilyPosOfHodgeTateInputs.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FamilyPosOfHodgeTateInputs.lean#L124).

The name says "ordinary curve" and "Hodge prime". The statement is about lattice data at test points, and `OrdinaryCurveStatement` is only one of its five hypotheses.
