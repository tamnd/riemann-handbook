---
id: wach-lattice-later-clauses-hold
title: Seventeen properties of the Wach lattices, a second name
kind: theorem
decl: GlobalTheory.T.wachLattice_laterClauses_hold
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.WachLatticeLaterClausesHoldStatement
covers: 738
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the seventeen properties of the Wach lattices](/entry/wach-used-clauses/). That entry has the content. Ten declarations below the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) use this name. Among them are [the top local theorem](/entry/bloch-kato-top-of-local-tate-duality-euler-char-alt/), [the admissible ranks of a CM datum](/entry/admissible-ranks-of-cmdatum/) and [the closing of theorem B](/entry/theorem-b-closing/). Each takes some of the seventeen properties.

## Statement

**Theorem.** For each datum $D$ (`D7`) and all local data $HW$, $F$, $Cm$ over it (`HWOf`, `FonOf`, `CmpOf`), the statement `DeltaInvariantNormBound D HW F Cm` holds.

`DeltaInvariantNormBound` is a conjunction of seventeen properties of the Wach lattices that $HW$ attaches to crystalline lattices. It has no hypothesis. It is stated in [the entry with the content](/entry/wach-used-clauses/).

## Proof

The proof applies `GlobalTheory.NL.wach_used_clauses`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [WachLatticeLaterClausesHoldStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHoldStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 7), which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames it.

The name `DeltaInvariantNormBound` says "norm bound", but the statement is a list of structural properties of Wach lattices and their Herr complexes. Only a few of the clauses are bounds.
