---
id: siegel-weil-std-of-ct-k
title: The Siegel-Weil formula, given the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilFinLt
covers: 1192
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd_k` from one hypothesis, the constant term split `CTSplit_k`. It fills the other hypothesis of [the assembly step](/entry/siegel-weil-std-pre-k/), a Poisson summation formula, with a theorem. Its user is [the Siegel-Weil formula of the Galois row](/entry/siegel-weil-std-k/), which also proves `CTSplit_k`. The real content is in the assembly step. Below this theorem are 1,192 declarations.

## Statement

**Theorem.** If the constant term split `CTSplit_k` holds, then the Siegel-Weil formula `SiegelWeilStd_k` holds.

`SiegelWeilStd_k` is stated in [the entry above](/entry/siegel-weil-std-k/). `CTSplit_k` is the statement of the induction step on the rank $n$ of $Y$: for a lower rank datum that embeds the problem of size $n - 1$ into the problem of size $n$, the integral over a unipotent group of a Fourier coefficient of the Siegel Eisenstein series is a Fourier coefficient of the lower rank Eisenstein series, plus a term $c_2$ with $c_2(\iota(y)x) = e^{\tau(n-2z)} c_2(x)$ for each $y$ with `IsDil` of parameter $\tau$ (a dilation by its name; not unfolded here). The [Siegel-Weil chapter](/proof/siegel-weil/) describes the same statement for the copy without `_k`.

## Proof

Apply [`siegelWeilStd_pre_k`](/entry/siegel-weil-std-pre-k/) to `TW.Twp.poisson_k` and the hypothesis. The theorem `poisson_k` proves the Poisson summation formula `Poisson_k`: for each Siegel-Weil datum, each Haar measure $\nu$ on the adelic $m \times n$ matrices with a fundamental domain of volume 1 for the rational matrices, each sign $\varepsilon$ and each Schwartz function $f$,

$$\sum_{X \in M_{m \times n}(E)} \int \psi\bigl(\varepsilon \operatorname{tr} \operatorname{gram}(X, Z)\bigr) f(Z)\, d\nu(Z) = \sum_{X \in M_{m \times n}(E)} f(X),$$

with $\operatorname{gram}(X, Z) = X^{T} J_A \sigma(Z)$ and $\operatorname{tr}$ the trace from $M_n(\mathbb{A}_E)$ to $\mathbb{A}_F$. The proof of `poisson_k` changes coordinates by a basis of $E/F$ and calls `GlobalTheory.TowU.FourWeyl.theta_four`, whose statement we have not unfolded.

## In the Lean code

The theorem is in [SiegelWeilFinLt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinLt.lean#L14). Its proof is `siegelWeilStd_pre_k TW.Twp.poisson_k hCT`. `CTSplit_k` is defined in [LiftedSchrodingerDatum.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/LiftedSchrodingerDatum.lean#L81), `Poisson_k` in [SiegelWeilTwSt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilTwSt.lean#L20), and `poisson_k` in [SiegelWeilTwpMain.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilTwpMain.lean#L30).

The theorem only passes its hypothesis along. It is a copy of [`siegelWeilStd_of_ct`](/entry/siegel-weil-std-of-ct/) with `_k` added to each name.
