---
id: canonical-algorithm-rules-is-correct
title: The canonical principalization rules reduce by dimension
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.canonicalAlgorithmRules_isCorrect
module: Development.ResolutionOfSingularities.EmbeddedResolution.StrongResolution.PrincipalizationWithRadicalCenters
covers: 3839
status: drafted
drafted_by: writer@claude
---
This theorem says that the canonical rules of the principalization algorithm satisfy the induction on dimension. It is the top of the [[resolution of singularities|MB52NDA6WN]] part of the Lean code that the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) reaches. The principalization algorithm `principalizationWithRadicalCenters` and the affine resolution rule of the same file use it. Through them it reaches [functorial resolution in characteristic zero](/entry/functorial-resolution-char-zero/) and [strong resolution in characteristic zero](/entry/strong-resolution-of-singularities-char-zero/), which give the inputs `ResolutionCharZero` and `PrincipalisationCharZero` of the [volume branch](/learn/geometry/#resolution-of-singularities). The theorem is a specialization: the real content is in [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/).

## Statement

Let $\mathcal{B}$ be the canonical principalization rules, built from the proof `strictTransformIsBlowupOfClosedSubscheme` that the strict transform of a closed subscheme under a [[blow-up|4SFS82N88K]] is the blow-up of that subscheme. Then $\mathcal{B}$ reduces inductively on dimension.

The rules $\mathcal{B}$ are three ways to make a sequence of blow-ups for a marked ideal: divisor reduction, order reduction and maximal order reduction. "Reduces inductively on dimension" is a list of four properties of these three rules. The entry [the rules reduce by dimension, given the hypotheses](/entry/is-correct-canonical-algorithm-rules-of-hypotheses/) states both in full.

## Proof

Apply [the rules reduce by dimension](/entry/is-correct-canonical-algorithm-rules/), `isCorrect_canonicalAlgorithmRules`, to the proof `strictTransformIsBlowupOfClosedSubscheme`. That is the whole proof.

## In the Lean code

The theorem is in [PrincipalizationWithRadicalCenters.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/PrincipalizationWithRadicalCenters.lean#L42). Its proof is one line: `isCorrect_canonicalAlgorithmRules strictTransformIsBlowupOfClosedSubscheme`. It has no hypotheses.

- `strictTransformIsBlowupOfClosedSubscheme` is proved in [BlowupClosedSubscheme.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrictTransformCharts/BlowupClosedSubscheme.lean#L309). Its statement `StrictTransformIsBlowupOfClosedSubscheme` ([BlowupProperties.lean](lean:Development/ResolutionOfSingularities/Foundations/Blowup/BlowupProperties.lean#L12)) says: let $X$ be locally noetherian, $S \hookrightarrow X$ a closed subscheme, and $\pi \colon X_1 \to X$ the blow-up along $Z$; if no irreducible component of $S$ lies in $Z$, then the strict transform of $S$ maps to $S$ as the blow-up of $S$ along the pullback of $Z$ to $S$, compatibly with $\pi$. This is the form of Hartshorne, *Algebraic Geometry*, Corollary II.7.15. We have not read its Lean proof.
- In the same file, `detachedLocusIsOpenForEmbeddings_principalizationWithRadicalCenters` and `isFunctorialPrincipalization_principalizationWithRadicalCenters` use this theorem.

The name and the name of its source `isCorrect_canonicalAlgorithmRules` differ only in word order. The Lean code has no predicate "is correct": the statement is `ReducesInductivelyOnDimension`.
