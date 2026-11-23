---
id: strong-resolution-of-singularities-char-zero-of-principalization-algorithm
title: Strong resolution from a functorial principalization algorithm
kind: theorem
decl: FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero_of_principalizationAlgorithm
module: Development.ResolutionOfSingularities.EmbeddedResolution.StrongResolution.GlobalResolutionFromAffine
covers: 591
status: drafted
drafted_by: writer@claude
---
This theorem is steps 2 to 4 of [strong resolution in characteristic zero](/entry/strong-resolution-of-singularities-char-zero/), as one implication. It takes a principalization algorithm and facts about it, and gives the resolution rule. The parent applies it to `principalizationWithRadicalCenters`.

## Statement

Let $A$ be a principalization algorithm: for a smooth $X$ over a field $k$ of characteristic $0$, an ideal nonzero on each component and a boundary with strict normal crossings, it gives a sequence of blow-ups. For an affine reduced $Y$ of finite type over $k$, embed $Y$ in some $\mathbb A^n_k$ and apply $A$ to the ideal of $Y$. When the strict transforms of $Y$ are blow-ups, dropping the isomorphisms gives an affine rule $B_A(Y)$ (`affineResolutionRuleOfPrincipalization`).

**Theorem.** Assume:

1. three facts on affine space: each affine $Y$ of finite type embeds in some $\mathbb A^n_k$; $\mathbb A^n_k$ is smooth; the empty boundary has strict normal crossings;
2. $A$ is functorial: it commutes with pushforward, field extension and smooth pullback;
3. the strict transforms are blow-ups, for every embedding and for the chosen one;
4. two closed embeddings of $Y$ in $\mathbb A^n_k$ and $\mathbb A^m_k$ are related by an automorphism of $\mathbb A^{n+m}_k$;
5. $B_A(Y)$ is a strong resolution of $Y$ for every affine $Y$.

Then strong resolution in characteristic $0$ holds, in the form of the parent entry.

## Proof

Hypotheses 1 to 4 give four compatibilities of $B_A$: with étale covers, open immersions, field extensions and smooth maps of fixed relative dimension. Hypothesis 5 is passed along unchanged. Then `strongResolutionOfSingularitiesCharZero_of_affineResolutionRule` (L359) glues.

1. Compatibility with open immersions gives that no centre of $B_A(Y)$ is the whole scheme. With this and étale compatibility, `existsGluedBlowupSequence_of_center_ne_top` gives, for each $X$, a sequence $R(X)$ that is the strict pullback of $B_A(W)$ along every surjective étale map $W \to X$ from an affine $W$ (`IsInducedByAffineRule`).
2. `isCompatibleWithSmoothMorphisms_of_isInducedByAffineRule` and `inducedRuleCompatibleWithFieldExtension` give properties 4 and 5 of $R$.
3. `isStrongResolution_of_isInducedByAffineRule` (L287) carries properties 1 to 3 from the affine charts to $X$.

## In the Lean code

The theorem is in [GlobalResolutionFromAffine.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/GlobalResolutionFromAffine.lean#L390). Three compatibility lemmas are in [AffineResolutionRuleCompatibility.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/ResolutionDescent/AffineResolutionRuleCompatibility.lean#L59). The smooth one is `isCompatibleWithSmoothOfRelativeDimension_affineResolutionRule` at L53 of the same file as the theorem. `IsInducedByAffineRule` is in [AffineResolutionRule.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/ResolutionDescent/AffineResolutionRule.lean#L84). We have not read the proofs of the compatibility lemmas.

The real work on the affine case is the hypothesis $5$, which the caller proves. The body is one term.
