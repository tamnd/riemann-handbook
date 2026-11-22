---
id: ordinary-eisenstein-eigenfunctional-exists
title: An ordinary eigenfunctional and an Eisenstein measure (second name)
kind: theorem
decl: GlobalTheory.T.ordinaryEisensteinEigenfunctional_exists
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExistsStatement
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the ordinary eigenfunctional theorem](/entry/chapter-m-holds/), which proves the statement $\mathrm{CuspidalUnitaryTwistsClaim}$. That entry has the real content. [The global unit law from smoothed classes](/entry/kato-global-unit-law-of-smoothed-classes/) lists this theorem among the 19 proved inputs of the lemma `glue2`.

## Statement

**Theorem.** $\mathrm{CuspidalUnitaryTwistsClaim}$ holds.

For an ordinary newform $g$ of weight $2e+1$, it gives a level $N$, an ordinary Hecke eigenfunctional $\lambda$ for $g$ on forms of level $N\ell$, and an $\ell$-adic measure built from $\lambda$ and Eisenstein series, with a nonzero value. The full statement is in [the entry with the proof](/entry/chapter-m-holds/).

## Proof

The proof is `exact @GlobalTheory.EisM.chapterM_holds`. The two statements are the same.

## In the Lean code

The theorem is in [OrdinaryEisensteinEigenfunctionalExistsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinaryEisensteinEigenfunctionalExistsStatement.lean#L11). The statement $\mathrm{CuspidalUnitaryTwistsClaim}$ is in [CuspidalUnitaryTwistsClaim.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/CuspidalUnitaryTwistsClaim.lean#L13).

The names do not match. The Lean name speaks of an Eisenstein eigenfunctional, but $\lambda$ is a Hecke eigenfunctional with the eigenvalues of the cusp form $g$. The Eisenstein series enter only through the measure. The claim name speaks of cuspidal unitary twists. A near copy, `ChapterMu` in [ChapterMu.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ChapterMu.lean#L43), has the same shape but builds the measure from the character $\theta$ itself, where $\mathrm{CuspidalUnitaryTwistsClaim}$ uses its finite Fourier transform $\hat\theta$, and it has only one of the two conditions on $d_1$.
