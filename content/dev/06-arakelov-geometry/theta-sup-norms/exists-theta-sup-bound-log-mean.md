---
id: exists-theta-sup-bound-log-mean
title: The sup bound of a theta section, the statement form
kind: theorem
decl: GlobalTheory.T.exists_theta_sup_bound_log_mean
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.ExistsThetaSupBoundLogMeanStatement
covers: 406
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. Its proof calls [the mean of the log sup](/entry/mean-log-sup/), which holds the content. Its one user is [the line of the key](/entry/line-of-key/), which applies it to the theta section of the key line.

## Statement

There is a constant $C \geq 0$ with this property. Let $E$ be a CM field, $L$ a number field and $D$ principally polarized data over $\mathcal{O}_L$ of genus $g \geq 1$. Let $\vartheta$ be a section of degree one and let $\Phi \geq 0$. If $\vartheta$ has $L^2$ norms $b_\sigma$ at the complex places with $\operatorname{mean}_\sigma \log b_\sigma \leq \Phi$ (`HasTheta`), then there are numbers $M_\sigma > 0$ that bound the normalized norm of $\vartheta$ in every frame at $\sigma$ (`SupLe`), with

$$\operatorname{mean}_\sigma \log M_\sigma \leq \Phi + C g \log(2 + g + \Phi).$$

Here $\operatorname{mean}_\sigma f = \frac{1}{[L:\mathbb{Q}]}\sum_{\sigma \colon L \to \mathbb{C}} f(\sigma)$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.Sl.Sup.mean_log_sup | ...`. The statement is the same as that of `mean_log_sup`.

## In the Lean code

The theorem is in [ExistsThetaSupBoundLogMeanStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ExistsThetaSupBoundLogMeanStatement.lean#L12). `HasTheta`, `SupLe` and `mean` are in [IsThetaMeanSquareNorm.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsThetaMeanSquareNorm.lean#L113). The user `line_of_key` is in [LineOfKeyDegree.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/LineOfKeyDegree.lean#L271).
