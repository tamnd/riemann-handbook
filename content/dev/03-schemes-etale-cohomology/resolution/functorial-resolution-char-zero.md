---
id: functorial-resolution-char-zero
title: Functorial resolution of singularities in characteristic zero
kind: theorem
decl: FunctorialResolution.functorialResolutionCharZero
module: Development.ResolutionOfSingularities.HasSimpleNormalCrossingsOfInStrictNormalCrossing
covers: 1126
status: drafted
drafted_by: writer@claude
---
This theorem is the form of [[resolution of singularities|MB52NDA6WN]] that the [volume branch](/learn/geometry/#resolution-of-singularities) of the proof uses. It reaches the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) by two paths. It is a renaming: the real content is in [strong resolution in characteristic zero](/entry/strong-resolution-of-singularities-char-zero/).

## Statement

**Theorem.** There is a rule $R$ that assigns to each field $k$ of characteristic $0$ and each reduced scheme $X$, locally of finite type and quasi-compact over $k$, a finite sequence of [[blow-ups|4SFS82N88K]] $X_n \to \cdots \to X_0 \cong X$ with these properties:

1. $X_n$ is smooth over $k$, and $X_n \to X$ is proper;
2. $X_n \to X$ is an isomorphism over the smooth locus $U$ of $X$, and the preimage of $U$ is dense;
3. each centre lies over $X \setminus U$, and the reduced preimage of $X \setminus U$ has strict normal crossings;
4. $R$ is compatible with smooth morphisms $X' \to X$ of relative dimension $r$, and with extensions $K/k$ of fields for which $X_K$ is reduced.

Compatible means that the sequence of $X'$ (or $X_K$) is the pullback of the sequence of $X$, after we drop the blow-ups whose centre pulls back to the empty set. This is Hironaka's theorem (Ann. of Math. 79, 1964) in the functorial form of Bierstone and Milman (Invent. Math. 128, 1997) and Włodarczyk (J. AMS 18, 2005).

## Proof

Take the rule $R$ of `strongResolutionOfSingularitiesCharZero` and its three properties. Copy each sequence of blow-ups into the structure of this statement, field by field. The three properties then hold with no change.

## In the Lean code

The theorem is in [HasSimpleNormalCrossingsOfInStrictNormalCrossing.lean](lean:Development/ResolutionOfSingularities/HasSimpleNormalCrossingsOfInStrictNormalCrossing.lean#L15). The statement `FunctorialResolutionCharZero` is in [Statements.lean](lean:Development/ResolutionOfSingularities/Statements.lean#L150). It is the same as `StrongResolutionOfSingularitiesCharZero` with other names: `BlowupSequence` for `SequenceOfBlowups`, `IsResolutionRuleCharZero` for `IsStrongResolutionRule`, and so on. The file name speaks of simple normal crossings; that matches other lemmas of the file, not this theorem. The theorem feeds `resolutionCharZero` and `resW`, both in the folder `WeilBound/CoreStatements/ResolutionCharZero`.
