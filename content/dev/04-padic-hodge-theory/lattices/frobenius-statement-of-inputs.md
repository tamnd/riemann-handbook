---
id: frobenius-statement-of-inputs
title: Local lifting theorem B from twenty separate inputs
kind: theorem
decl: Formalism.MainNotions.N.Ln17.frobenius_statement_of_inputs
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusStatementOfFontaine
covers: 858
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. [`stmt_holds`](/entry/stmt-holds/) calls it after it takes the admitted conditions apart. It reduces local lifting theorem B to one prime and one pair of fields, and calls [`thmB_at`](/entry/thm-b-at/), which has the content.

## Statement

Use the notation of [local lifting theorem B](/entry/theorem-b-closing/).

**Theorem.** Let $C \ge 320$. Assume:

1. the five lattice conditions `P2`, `P3`, `P4`, `P5`, `P9`;
2. `adm2`, which includes the lift condition `coreLiftA`;
3. the saturation conditions `adm5`, `SaturationFrobeniusPullback` and the killer conditions `KillerLevL`, `KillerModL`;
4. `adm9` to `adm15`;
5. `adm22`, `adm23` and the global letter condition.

Then for each prime $\ell$, each unramified finite extension $K$ of $\mathbb{Q}_\ell$, and each $L$ good for $K$ at level 1, the bound `ThmB` holds with the constant $C$ for the Wach module at $(K, L)$.

## Proof

Fix $\ell$, $K$ and $L$. `ThmB` assumes $p \ge 11$, and $p = \ell$. So $\ell \ne 2$, and $(K, L)$ is in case A. The proof puts the 17 conditions of items 1 to 4 into the record `AdmBoundsB`, puts the three of item 5 into the record `UsedJ`, and calls `thmB_at`.

## In the Lean code

The theorem is in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L197). The conclusion `ArcLiftingSetup.aux₃` unfolds to `TheoremBLocal` in [CrystallineMapLemmas.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineMapLemmas.lean#L178). The records are `AdmBoundsB` in [AdmBoundsBOfAdm.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/AdmBoundsBOfAdm.lean#L67) and `UsedJ` in [ExistsGaloisExtendingAlgHom.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ExistsGaloisExtendingAlgHom.lean#L116).

The name is misleading: no Frobenius statement occurs here.
