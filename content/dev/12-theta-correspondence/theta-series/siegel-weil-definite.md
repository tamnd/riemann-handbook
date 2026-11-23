---
id: siegel-weil-definite
title: The definite Hermitian Siegel-Weil identity, by induction on the degree
kind: theorem
decl: GlobalTheory.SW.siegel_weil_definite
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.SiegelWeilDefiniteHermitianOfFourMulLt
covers: 431
status: drafted
drafted_by: writer@claude
---
This theorem is the proof behind the statement [siegel-weil-definite-hermitian-of-four-mul-lt](/entry/siegel-weil-definite-hermitian-of-four-mul-lt/), which has the same form. It is a short induction on the degree $N$. The base case is trivial and the step is [siegel-weil-formula-degree-succ](/entry/siegel-weil-formula-degree-succ/), whose real proof is [sw-at-succ](/entry/sw-at-succ/).

## Statement

Let $E$ be a CM field and let $\Psi$ be a CM type of $E$: for each embedding $\tau \colon E \to \mathbb{C}$, $\tau \in \Psi$ if and only if $\bar\tau \notin \Psi$. Let $n$ be even and let $N$ satisfy $4N < n$. Then `SWAt Ψ n N` holds.

`SWAt Ψ n N` says the following. Take positive integers $M, R$ and an admitted family $\varphi$. It gives a function $\varphi_\Lambda$ on $n \times N$ matrices over $E$ for each self-dual lattice $\Lambda \subset E^n$ that agrees with the standard lattice away from $M$. The function is supported on $x$ with $Rx$ in $\Lambda$, and it is periodic modulo $R\Lambda$. Take $Z$ in the Hermitian upper half space of degree $N$. Then the sum over lattice classes, with weight one over the order of the stabilizer, of the difference between the theta series $\theta(\varphi_\Lambda)(Z)$ and the Eisenstein series $E(\varphi_\Lambda)(Z)$ is zero. In short, the class average of theta series is an Eisenstein series. This has the shape of a Siegel-Weil formula for definite Hermitian forms (compare the [[Weil representation|H3Q2703KKV]]). The Lean statement does not cite a source.

## Proof

Induction on $N$.

1. $N = 0$. The theta series and the Eisenstein series both equal $\varphi_\Lambda(0)$, so the difference is zero. The hypothesis $4 \cdot 0 < n$ is not used.
2. $N \to N + 1$. From $4(N+1) < n$ we get $4N < n$, so the induction gives `SWAt Ψ n N`. The step theorem then gives `SWAt Ψ n (N+1)`.

## In the Lean code

The theorem is in [SiegelWeilDefiniteHermitianOfFourMulLt.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilDefiniteHermitianOfFourMulLt.lean#L11). The base case uses `Base.swd_zero` (a `rfl` lemma) and `Base.swDiff_deg_zero` in [FirstCoordinateAdmissible.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/FirstCoordinateAdmissible.lean#L475). The step calls `GlobalTheory.T.siegelWeil_formula_degree_succ`. `SWAt` is in [IsHeatZero.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/IsHeatZero.lean#L15); `thH`, `eis`, `swd` and `classSum` are in FirstCoordinateAdmissible.lean.
