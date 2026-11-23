---
id: hermitian-double-coset-second-type-family-amp-sq-le
title: The mean square over one family of second-type terms, statement form
kind: theorem
decl: GlobalTheory.T.hermitianDoubleCoset_secondType_family_ampSq_le
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermitianDoubleCosetSecondTypeFamilyAmpSqLeStatement
covers: 414
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`family_bound`](/entry/family-bound/). Its only user is [`ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/), which uses it as the bound for the second type of terms. The content is in [`family_bound`](/entry/family-bound/).

## Statement

The notation $\mathrm{ampSq}$, $\mathrm{nn}$, $H$, $q$ and the defect is in [the entry for `ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/).

**Theorem.** Let $S$ be a datum of type `Frames L r k` over a nonarchimedean local field of characteristic $0$, with $4r + 7 \leq k$. For all $\beta, J, \beta_J \in \mathbb{N}$, let $\mathcal{F}(\beta, J, \beta_J)$ be the second-type terms with defect index $\beta$, largest level $J$ and $\beta_J$ cosets of $M(d, \Lambda)$ at level $J$ (`InFF β J βJ`). Then
$$\mathrm{ampSq}\bigl(\mathcal{F}(\beta, J, \beta_J)\bigr) \leq 98 \, H^{9(r+1)^2 + 12(r+1)} \cdot 4 H^{4(r+1)} \cdot \bigl(q^{1 - (k - 2r - 3)}\bigr)^2 \, \mathrm{nn}.$$

## Proof

The proof is the term `GlobalTheory.HL.FamilyBound.family_bound`. There is nothing else.

## In the Lean code

The theorem is at [HermitianDoubleCosetSecondTypeFamilyAmpSqLeStatement.lean line 9](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetSecondTypeFamilyAmpSqLeStatement.lean#L9). The two statements have the same text, so the first branch of the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` closes the goal. The file sets `maxHeartbeats` to 1,000,000 for this one line. As in the other statement forms of this group, the name speaks of a double coset, but the statement has none.
