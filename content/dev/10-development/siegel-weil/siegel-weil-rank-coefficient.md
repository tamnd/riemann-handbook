---
id: siegel-weil-rank-coefficient
title: The represented block case, restated
kind: theorem
decl: GlobalTheory.T.siegel_weil_rank_coefficient
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeil.ArchimedeanSiegelWeil.PlaceIntegrals.SiegelWeilRankCoefficientStatement
covers: 1306
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`siegel_frame`](/entry/siegel-frame/), with the same statement and a proof that only cites it. [The singular case of the Siegel-Weil identity](/entry/siegel-deg/) calls it after it puts the Gram matrix in block normal form. The content is in [`siegel_frame`](/entry/siegel-frame/).

## Statement

We use the notation $I_\varphi(\beta)$, $W_\varphi(\beta)$ and the hypothesis `Hyp` of [`siegelDeg`](/entry/siegel-deg/).

**Theorem.** Assume `Hyp` for $\varphi$ on $M_{m \times r}(\mathbb{A}_E)$. Let $t < r$ and let $\beta = \begin{pmatrix} \beta_0 & 0 \\ 0 & 0 \end{pmatrix} \in \mathrm{Herm}_r(E)$ with $\beta_0$ an invertible $t \times t$ matrix. Suppose that $\beta = x^* J x$ for some $x \in M_{m \times r}(E)$ of rank $r$. Then $I_\varphi(\beta) = W_\varphi(\beta)$.

## Proof

The proof is `first | exact @siegel_frame | exact siegel_frame`. The statement is the statement of `siegel_frame`, word for word.

## In the Lean code

The theorem is in [SiegelWeilRankCoefficientStatement.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/SiegelWeilRankCoefficientStatement.lean#L9). It is the only declaration of the file. The file imports `SiegelWeilRankCoefficient.lean`, which holds the proof under the name `siegel_frame`. So the file whose name ends in `Statement` holds the copy, and the file with the plain name holds the original. The same pattern of a `Statement` file whose proof is one `first | exact …` occurs for the other lemmas that [`siegelDeg`](/entry/siegel-deg/) calls.
