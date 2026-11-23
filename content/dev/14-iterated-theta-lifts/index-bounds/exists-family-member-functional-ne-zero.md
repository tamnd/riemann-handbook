---
id: exists-family-member-functional-ne-zero
title: A family member whose functional does not vanish, as a named statement
kind: theorem
decl: GlobalTheory.T.exists_familyMember_functional_ne_zero
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.ExistsFamilyMemberFunctionalNeZeroStatement
covers: 798
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_fam_cfOf_ne_zero`](/entry/exists-fam-cf-of-ne-zero/). It has the same statement, and its proof only applies that lemma. [`detectQ_of_known`](/entry/detect-q-of-known/) uses it to show that the CM family functionals detect the low Fourier-Jacobi coefficients. The real content is in the entry for `exists_fam_cfOf_ne_zero`.

## Statement

**Theorem.** Assume `Known`, `ModelsAt Xo c` and the conditions on the uniformisation $U$, the lattice data at a component $k$, the weight $(a', n)$ and the constants $c_1 > 0$ and $w$ that are listed in the entry for `exists_fam_cfOf_ne_zero`. Let $F$ be a section of weight $(a', n)$ whose readings are cusp forms. If the reading of $F$ at $k$ has a nonzero Fourier-Jacobi coefficient with exponent sum at most $c_1$, then there are a number field $K_1$ over $K = c.F$ and an arc datum $d$ over $K_1$ such that `Fam (nQ …) (LaQ …) c₁ d` holds and $\phi_d(F) = $ `cfOf d.yF d.μ d.jj F` $\neq 0$.

## Proof

The proof is `exists_fam_cfOf_ne_zero`, applied to the same arguments.

## In the Lean code

The theorem is in [ExistsFamilyMemberFunctionalNeZeroStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFamilyMemberFunctionalNeZeroStatement.lean#L9). The proof is `first | exact @GlobalTheory.ArcDetect.exists_fam_cfOf_ne_zero | ...`, so the two statements are the same up to elaboration.
