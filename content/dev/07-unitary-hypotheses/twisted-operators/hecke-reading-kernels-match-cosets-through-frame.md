---
id: hecke-reading-kernels-match-cosets-through-frame
title: Hecke kernels match cosets, a second name
kind: theorem
decl: GlobalTheory.T.heckeReading_kernels_match_cosets_through_frame
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeReadingKernelsMatchCosetsThroughFrameStatement
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`heckeTerm`](/entry/hecke-term/). Its statement is the statement of `heckeTerm`, word for word, and its proof only applies `heckeTerm`. Its one user is [the Hecke reading theorem](/entry/hecke-read-tie/). Below it are 336 declarations.

## Statement

Assume the Hecke point laws, `SplitLinearModel D` and `VacFixed D`, and the setting of [the Hecke reading theorem](/entry/hecke-read-tie/): the conditions on $R$, the tie `TieIn`, $\sigma = \sigma_0$, the frame pin, and Hecke data $(\mathfrak{P}, p, k, \alpha, R_c)$ at a split-off prime. Let $h \in G(\mathbb{A})$ be such that the framed point $y_h$ is defined. Then there is a bijection $e \colon \mathcal{C}(y_h) \to R_c$ with two properties for each $C$. First, some point $z$ satisfies $z \in y_h/C$. Second, for each such $z$ and each section $f$ of weight $\kappa_i$,

$$\lambda\, c(h)\mu(h)\, N(\mathfrak{P})^{-\lfloor k n_V/2\rfloor} f(z) = \mu_i(\mathfrak{P})^{-k}\, \varphi_f(h\, e(C)).$$

The notation is that of [the Hecke reading theorem](/entry/hecke-read-tie/).

## Proof

The proof is one tactic line that applies `GlobalTheory.HeckeTerm.heckeTerm`. See [`heckeTerm`](/entry/hecke-term/) for the mathematics.

## In the Lean code

The theorem is in [HeckeReadingKernelsMatchCosetsThroughFrameStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadingKernelsMatchCosetsThroughFrameStatement.lean#L12). The proof is `first | exact @heckeTerm | exact heckeTerm | (intros; apply heckeTerm <;> assumption)`: three forms of the same call. The file imports `Mathlib` twice (lines 1 and 3).
