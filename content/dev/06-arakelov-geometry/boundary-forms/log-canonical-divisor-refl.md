---
id: log-canonical-divisor-refl
title: Cusp forms as canonical forms on the flag space (second name)
kind: theorem
decl: GlobalTheory.T.logCanonical_divisor_refl
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.LogCanonicalReflOfBoundary
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [logCanonical_refl_of_boundary](/entry/log-canonical-refl-of-boundary/). It has the same statement, and its proof is that lemma. Its only user is [log_canonical_pair_iff](/entry/log-canonical-pair-iff/), which applies it to the trivial modification and then moves the result to any smooth projective model. Below this theorem are 339 declarations.

## Statement

We use the notation of [log_canonical_pair_iff](/entry/log-canonical-pair-iff/). Take the modification $X' = \bar X$ with $\sigma$ the identity (`Modif.refl`), and a canonical identification $\omega_0$ of it. Assume the Kodaira-Spencer isomorphism `KSIso` at every framed point over every field. Then for weights $s = \kappa + b$ and a section $m$ of $L(s)$ over $U$: $m$ extends to a global section that vanishes along $D$ if and only if $\omega_0 \cdot m$ extends to a global section of $K_{\bar X} \otimes L(b)$.

## Proof

The proof is one line, `first | exact @logCanonical_refl_of_boundary | ...`. The content is in [logCanonical_refl_of_boundary](/entry/log-canonical-refl-of-boundary/).

## In the Lean code

The theorem is at [LogCanonicalReflOfBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/LogCanonicalReflOfBoundary.lean#L77), in the same file as the lemma it restates (line 20). The word "divisor" in the name does not match the statement, which has no divisor in it; the boundary enters only through `vanBd`.
