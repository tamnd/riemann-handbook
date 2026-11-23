---
id: universal-part-case-a
title: The universal part in the unramified case, a second name
kind: theorem
decl: GlobalTheory.universalPart_caseA
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineUniversalPartCaseA
covers: 377
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It is the proof of [`crystallineUniversalPart_caseA`](/entry/crystalline-universal-part-case-a/), which gives the universal part `adm14` of the [thirteen admitted conditions](/entry/admissible-ranks-of-cmdatum/). It passes its hypotheses to [`universal_general_statement_holds`](/entry/universal-general-statement-holds/), which has the proof.

## Statement

The statement is that of [`crystallineUniversalPart_caseA`](/entry/crystalline-universal-part-case-a/), word for word.

**Theorem.** Let $D$, $HW$, $F$, $C_m$ be as in [local lifting theorem B](/entry/theorem-b-closing/). Assume `AdmUnivA` (saturation, the killer at levels, the $\Gamma$-stability of the uniformizer, and the arc coordinates), the lattice condition `P9`, the lifting statement `ConclusionH`, and $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ over unramified fields. Then `UniversalComponentCaseA` holds: for each prime $\ell \ge 5$, each $K$ unramified over $\mathbb{Q}_\ell$ and each coefficient field $L$ good for $K$ at level 1, the Wach module at $(K, L)$ satisfies `UnivCore` and `UnivNNCore`.

## Proof

The proof is the term `universal_general_statement_holds D HW F Cm hAdm h9 hH h15`. That lemma adds one fact, `invLevCore_fin` (a condition on inverse levels, proved from `P9`), and calls `universal_general_of_level_inverse`.

## In the Lean code

The theorem is in [CrystallineUniversalPartCaseA.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineUniversalPartCaseA.lean#L10). The callee is in [UniversalGeneralStatementHolds.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/UniversalGeneralStatementHolds.lean#L38).

The chain `T.crystallineUniversalPart_caseA`, `universalPart_caseA`, `universal_general_statement_holds` has three names for one statement.
