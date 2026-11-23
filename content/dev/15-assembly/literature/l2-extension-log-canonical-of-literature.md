---
id: l2-extension-log-canonical-of-literature
title: An L2 extension from a finite zero set, as a literature input
kind: theorem
decl: UpperTheory.LiteratureTheorems.l2_extension_log_canonical_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem gives the statement `L2ExtensionLogCanonical`. It takes a proof $O$ of [OpenLiteratureStatements](/step/open-literature-statements-def/) and does not use it. The proof is one term, [`l2ExtensionLogCanonical'`](/entry/l2-extension-log-canonical-prime/), and that entry has the real content. The result fills the field `q8` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). Below this theorem are 389 declarations.

## Statement

Let $n \ge 1$. Let $Y$ be compact, with a weighted atlas: holomorphic charts to $\mathbb{C}^n$, line bundles with weights $\varphi$, the canonical bundle $K$, and a measure $\mu$ (`WeightedAtlas`). Assume that some line bundle has a weight with positive definite Levi form.

Let $E$ and $L$ be line bundles. Let $s_1, \dots, s_n$ be sections of $L$ with a finite common zero set $S$, with $|s|^2 \le 1$, and with a nonzero Jacobian $J(P)$ at each $P \in S$. Put $\psi = n \log |s|^2$. Let $\delta > 0$, and assume that the Levi form of $\varphi_E + \alpha\psi$ is semipositive off $S$ for $1 \le \alpha \le 1 + \delta$.

**Theorem.** For each $f$ there is a holomorphic section $F$ of $K + E$ with $F = f$ on $S$ and

$$\int_Y \frac{2^n\, |F|^2_{K+E}\, e^{-\psi}}{1 + (\delta\psi)^2}\, d\mu \le \frac{34}{\delta}\, c_n \sum_{P \in S} \frac{|f(P)|^2}{|J(P)|^2}\, e^{-\varphi_E(P) + n\varphi_L(P)},$$

with $c_n = 2^{n+1}\pi^n/(n-1)!$.

This is an $L^2$ extension theorem of Ohsawa-Takegoshi type (Ohsawa and Takegoshi, Math. Z. 195, 1987), for a zero-dimensional subvariety. We have not matched the constant $34/\delta$ with a source. We have not unfolded `leviAt`, `sqn` or `nsq`, the Levi form and the norms of the atlas.

## Proof

Apply `GlobalTheory.l2ExtensionLogCanonical'`. The argument $O$ is not used.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean line 451](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L451). The statement is in [L2ExtensionLogCanonical.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/L2ExtensionLogCanonical.lean#L32). The proof below is in [the proof file](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/L2ExtensionLogCanonical.lean#L13). It uses `exists_etale_frame_off_finite_zeroSet` and `l2_extension_etale_coordinates_finite_zeros`.

Odd point. The name says "of literature", but the code proves the statement and ignores $O$.
