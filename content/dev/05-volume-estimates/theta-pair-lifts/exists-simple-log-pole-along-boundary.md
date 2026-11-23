---
id: exists-simple-log-pole-along-boundary
title: The canonical identification has a simple pole along the boundary (second name)
kind: theorem
decl: GlobalTheory.T.exists_simple_log_pole_along_boundary
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsSimpleLogPoleAlongBoundary
covers: 321
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [log_pole_along_boundary_is_simple](/entry/log-pole-along-boundary-is-simple/). It has the same statement, and its proof is that lemma. Its user is [logCanonical_refl_of_boundary](/entry/log-canonical-refl-of-boundary/), which needs it to show that $\omega_0$ has a simple pole along the boundary. Below this theorem are 321 declarations.

## Statement

We use the notation of [logCanonical_refl_of_boundary](/entry/log-canonical-refl-of-boundary/). Let $y \in D$, let $V$ be an open set that contains $y$, and let $t$ be a reduced equation of $D$ on $V$ (a unit exactly on $U$, dividing each function that vanishes on $D$). Then there are an open $V' \subseteq V$ that contains $y$, charts $i$ of $K_{\bar X}$ and $j$ of the common chart system that contain $V'$, and a function $u$ on $V'$ that is a unit at every point, such that $t\,\omega_0 = u$ at each point of $V' \cap U$ in these charts.

## Proof

The proof is one line, `first | exact @log_pole_along_boundary_is_simple | ...`. The content is in [log_pole_along_boundary_is_simple](/entry/log-pole-along-boundary-is-simple/), which compares $t$ with the logarithmic determinant of [exists_log_pole_along_boundary](/entry/exists-log-pole-along-boundary/).

## In the Lean code

The theorem is at [ExistsSimpleLogPoleAlongBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsSimpleLogPoleAlongBoundary.lean#L179), in the same file as the lemma it restates (line 135). That lemma names two of its hypotheses `_` at line 136 and does not use them: `GrothendieckDeformation` and $y \notin U$. So neither is used in this proof.
