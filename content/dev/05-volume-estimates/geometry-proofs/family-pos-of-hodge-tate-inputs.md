---
id: family-pos-of-hodge-tate-inputs
title: Lattice families at ramified places, from five Hodge-Tate inputs
kind: theorem
decl: GlobalTheory.T.family_pos_of_hodge_tate_inputs
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FamilyPosOfHodgeTateInputsStatement
covers: 1619
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the existence of lattice families](/entry/family-exists-pos-holds/). It has the same statement and its proof only calls that theorem. The entry [the good tower and the volume theorem, from reduced inputs](/entry/good-tower-volume-of-reduced/) uses it once, to get the statement `FamilyExistsPos`. That statement then goes to [the good tower volume theorem](/entry/good-tower-volume-theorem/). The real content is in [the entry of `familyExistsPos_holds`](/entry/family-exists-pos-holds/).

## Statement

**Theorem.** Suppose that these five statements hold:

1. a Hodge-Tate image bound for $p$-divisible groups over a subring of an algebraically closed, $p$-adically complete field of characteristic 0 (`FarguesHodgeTate`);
2. the existence of the quotient of a polarized abelian scheme by a finite flat subgroup (`QuotientByFiniteFlatStatement`);
3. a retract statement for abelian schemes over valuation rings (`ZarhinStatement`);
4. the existence of Hodge-Tate data for polarized abelian schemes (`HodgeTateDatumStatement`);
5. the existence of an abelian scheme with a given form of $p$-torsion (`OrdinaryCurveStatement`).

Then `FamilyExistsPos` holds: at each place above an odd prime $p$ that satisfies the conditions, there is a family of lattice data on the charts of the model. The [entry of `familyExistsPos_holds`](/entry/family-exists-pos-holds/) states the conclusion in full.

## Proof

The proof is `familyExistsPos_holds`. Nothing else is done.

## In the Lean code

The theorem is in [FamilyPosOfHodgeTateInputsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FamilyPosOfHodgeTateInputsStatement.lean#L20). The proof is the tactic `first | exact @familyExistsPos_holds | ...`. The first branch closes the goal, so the types are equal. The caller is in [FinalTheoremOfInputsRight.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRight.lean#L35). There the inputs 4 and 5 are proved theorems (`GR.Top.main` and `ordinary_curve_statement_holds`), and the inputs 1, 2 and 3 are hypotheses of the caller. The file sets `maxHeartbeats` to 1000000 for a proof of one line.
