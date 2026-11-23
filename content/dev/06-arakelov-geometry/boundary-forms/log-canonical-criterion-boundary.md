---
id: log-canonical-criterion-boundary
title: Cusp forms as canonical forms on a smooth model (second name)
kind: theorem
decl: GlobalTheory.T.log_canonical_criterion_boundary
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.LogCanonicalCriterionBoundary
covers: 359
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [log_canonical_pair_iff](/entry/log-canonical-pair-iff/). It has the same statement, and its proof is that lemma. It is the form that three lemmas below [the covolume bound](/entry/top-covol-g-alt-alt/) call: `exists_vanBd_section_nonzero_of_canonical_twist_nonzero`, `exists_cusp_germ_transfer` and `hodge_bundle_sandwich_bound`. Below this theorem are 359 declarations.

## Statement

The statement is the one of [log_canonical_pair_iff](/entry/log-canonical-pair-iff/). In short: let $\bar X$ be the part of a toroidal flag space over the closure of a connected component, with interior $U$ and boundary $D$. Let $\sigma \colon X' \to \bar X$ be a smooth projective modification that is an isomorphism over $U$, with a Kodaira-Spencer identification $\omega$ of $K_{X'}$ with the automorphic bundle $L(\kappa)$ over $U$. Let $b$ and $s = \kappa + b$ be weights, and let $m$ be a section of $L(s)$ over $U$. Then $m$ extends to a section of $L(s)$ on $\bar X$ that vanishes along $D$ if and only if $\omega \cdot \sigma^* m$ extends to a section of $K_{X'} \otimes \sigma^* L(b)$ on $X'$.

## Proof

The proof is one line, `first | exact @log_canonical_pair_iff | ...`. All the content is in [log_canonical_pair_iff](/entry/log-canonical-pair-iff/).

## In the Lean code

The theorem is at [LogCanonicalCriterionBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/LogCanonicalCriterionBoundary.lean#L49), in the same file as the lemma it restates (line 21). The name says "criterion" and "boundary"; the statement is the equivalence above, with no further condition.
