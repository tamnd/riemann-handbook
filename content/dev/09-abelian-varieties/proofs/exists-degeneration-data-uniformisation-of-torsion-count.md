---
id: exists-degeneration-data-uniformisation-of-torsion-count
title: Degeneration data and a uniformisation exist, given the torsion count
kind: theorem
decl: GlobalTheory.T.exists_degenerationData_uniformisation_of_torsionCount
module: Development.AbelianVarietyTheory.Proofs.UniformizationProofs.ExistsDegenerationDataUniformisationOfTorsionCouStatement
covers: 823
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for `GlobalTheory.UU.exists_degData_unif`. The real content is in [exists-deg-data-unif](/entry/exists-deg-data-unif/). The theorem lies below the step [every-character](/step/every-character/).

## Statement

Assume three facts:

1. For an algebraically closed field $k$, an abelian variety $B$ of dimension $g$ over $k$, and $n$ nonzero in $k$, the group $B[n](k)$ has $n^{2g}$ elements. This is a standard result (Mumford, *Abelian Varieties*, Chapter II).
2. `Laws`, a record of 24 facts about abelian schemes, such as the theorem of the cube, rigidity and the Weil pairing.
3. `Laws2`, a record of 4 more such facts.

Then for every `HidaSetting` there are degeneration data $D$ and a uniformisation $U$ that match the setting. A `HidaSetting` has a complete discrete valuation ring $V$, a semi-abelian scheme $G$ over $V$ whose generic fibre is a polarized abelian variety $A$, a cubical line bundle on $G$, a character group $X$ that is free of finite rank, and a torus quotient at level $0$ with an even trivialization. "Match" means that $U$ has the same line bundle, the same generic isomorphism and the same cubical structure as the setting.

These names follow the degeneration theory of Faltings and Chai (*Degeneration of Abelian Varieties*, Springer 1990). We have not compared the definitions `DegData` and `Unif` with that book.

## Proof

The proof is one tactic line: `first | exact @GlobalTheory.UU.exists_degData_unif | ...`. So the theorem is a renaming.

## In the Lean code

The theorem is in [ExistsDegenerationDataUniformisationOfTorsionCouStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationOfTorsionCouStatement.lean#L17). The source is in [ExistsDegenerationDataUniformisationOfTorsionCou.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationOfTorsionCou.lean#L21). The setting is in [IsCPPullback.lean](lean:Development/AbelianVarietyTheory/Definitions/Uniformization/IsCPPullback.lean#L34).

The three hypotheses are proved elsewhere in the code. The torsion count is `card_torsion_points_unconditional`, and `Laws` and `Laws2` come from `abelianScheme_laws_unconditional`. This `HidaSetting` has nothing to do with Hida theory. The code has 23 unrelated structures with this name.
