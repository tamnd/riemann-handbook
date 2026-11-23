---
id: twisted-jet-one-of-all
title: Periods of one basis element are multiples of class sums
kind: theorem
decl: GlobalTheory.RowClaim.JetsAssembly.twisted_jet_one_of_all
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedJetSuccEqAssembly
covers: 999
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It gives the statement `JetsOne` for all large admissible choices, and [the jet step of the row test](/entry/twisted-jet-succ-eq-assembly/) uses it as the case of one basis element. The proof is one term: the lemma [`twisted_pairing_identity`](/entry/twisted-pairing-identity/). That entry has the real content.

## Statement

**Theorem.** Assume `ThetaLocalInputs`, the [record of named literature statements](/step/theta-local-inputs-def/), and `SumOKK`. Then $\mathrm{Big}(\texttt{JetsOne})$ holds.

`JetsOne ch` says: for each polynomial datum $P$ on the column and the row there is $\kappa \in \mathbb{C}$ such that, for all $t$, $a$, $\beta$ in the support, volumes $M$ with `IsTermVol`, expansions $\tau$ with `IsExpansion`, and all $y$, the combination of periods $P_M$ at the single element $P$ equals $\kappa$ times the class sum at $\beta$. The notation is that of [the parent entry](/entry/twisted-jet-succ-eq-assembly/).

## Proof

The proof is the term `GlobalTheory.T.twisted_pairing_identity`. The statement of that lemma is `JetsOne` with the definition written out, so Lean accepts it as is.

## In the Lean code

The theorem is in [TwistedJetSuccEqAssembly.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedJetSuccEqAssembly.lean#L16). `JetsOne` is in [JetsOfOrthogonalSum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/JetsOfOrthogonalSum.lean#L31).

- The words "of all" in the name do not match any part of the statement.
- There is a twin, `jetsOne_all`, in [JetsOfOrthogonalSum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/JetsOfOrthogonalSum.lean#L46). It assumes `Hypotheses₂` in place of `ThetaLocalInputs` and is the term `term_volume_class_sum`.
