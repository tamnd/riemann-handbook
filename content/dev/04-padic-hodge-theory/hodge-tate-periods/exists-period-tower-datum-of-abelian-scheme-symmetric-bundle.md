---
id: exists-period-tower-datum-of-abelian-scheme-symmetric-bundle
title: A period tower datum exists for an abelian scheme with a symmetric line bundle
kind: theorem
decl: GlobalTheory.T.exists_periodTowerDatum_of_abelianScheme_symmetricBundle
module: Development.AbelianVarietyTheory.Proofs.UnramifiedDepth.ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBuStatement
covers: 346
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [abelian-period-datum-main](/entry/abelian-period-datum-main/). That entry has the real content. The theorem lies below the [literature step](/step/every-character-of-literature/).

## Statement

The statement is copied word for word from `GlobalTheory.AbelianPeriodDatum.main`. In short: let $G$ be an abelian scheme of relative dimension $g$ over $A_{\inf}/\xi^2$, with a symmetric, rigidified, nondegenerate line bundle $P$ on $G \times G$ and an action of a ring $O_0$ with involution that satisfies a Rosati condition. Then there are a biextension datum $B$ with a natural group isomorphism to the points of $G$, an action of $O_0$ on $B$, and a Hodge-Tate datum $D$ on the tower $O/p^{n+1}$ that matches this action. The full list of hypotheses and conclusions is in the main entry.

## Proof

The proof is one tactic line: `first | exact @GlobalTheory.AbelianPeriodDatum.main | ...`. So the theorem is a renaming.

## In the Lean code

The theorem is in [ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBuStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBuStatement.lean#L20). The source is [ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBu.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBu.lean#L132).

Two callers use this name. The private lemma `htd_of_tower` in [ExistsHodgeTateDatumFormalGroupCharacters.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsHodgeTateDatumFormalGroupCharacters.lean#L154) feeds `exists_htd_chars`. A proof in [FormalGroupChartFamily.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/FormalGroupChartFamily.lean#L167) also uses it, for `exists_htd_act`.
