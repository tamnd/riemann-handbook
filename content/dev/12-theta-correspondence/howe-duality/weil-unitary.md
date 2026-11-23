---
id: weil-unitary
title: The Siegel-Weil formula for unitary groups in the convergent range
kind: theorem
decl: UpperTheory.Lit.Sw47.weilUnitary
module: Development.AutomorphicArithmetic.ThetaCorrespondence.FockModels.FockAnisoFree
covers: 1767
status: drafted
drafted_by: writer@claude
---
This theorem proves `WeilSiegelFormulaUnitary`: convergence of theta integrals for a unitary dual pair, and the Siegel-Weil formula when the Eisenstein series converges absolutely. It joins two earlier results. Its result has two users: the leaf `weil_siegel_formula_unitary_of_literature`, which fills fields of three bundles of [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) (`published_results_analytic`, [`published_results_eigen`](/step/published-results-eigen/) and [`published_results_first`](/step/published-results-first/)), and the theorem `fa` of the same file. Most of its weight is in [`weilSiegelFormula`](/entry/weil-siegel-formula/) (1,728 of 1,767 declarations).

## Statement

Let $D$ be a datum of type `D7`. It carries a number field $F$, an extension $E$ with a complex conjugation (a local instance `cmStar`), and many more conditions that we have not unfolded. Let $A$ and $B$ be Hermitian spaces over $E$ of ranks $n \geq 1$ and $m$, and let $r$ be the Witt index of $B$. Let $dh$ be a Haar measure on $U(B)(\mathbb{A})$. Suppose that $r = 0$ or $n + r < m$. Then:

1. For each basis of $E$ over $F$ there is a continuous seminorm $\nu$ on the adelic Schwartz space such that the absolute theta integral is bounded by $\nu$: $$\int_{U(B)(F) \backslash U(B)(\mathbb{A})} \sum_{\xi \in M_{m \times n}(E)} \lvert \varphi(h^{-1} \xi) \rvert \, dh \leq \nu(\varphi).$$
2. Let $\omega$ be a [[Weil representation|H3Q2703KKV]] of $U(A \oplus A^{-}) \times U(B)$ for characters $\psi$ and $\chi$ (the condition `IsWeilDatumO`), and let $f$ be a theta function (`IsThetaFunO`). Here $A \oplus A^{-}$ is the doubled space `dblSp A`. Then for each $g$ the theta kernel $h \mapsto \theta(g, h; f)$ is integrable on $U(B)(F) \backslash U(B)(\mathbb{A})$.
3. If also $2n < m$, let $\mathcal{G}$ be a fundamental domain of measure $1$ for the rational points of $M_{m \times n}$ (`IsCovolOne`), and let $\Phi_f(g)$ be the integral of $\omega(g, 1) f$ over the points $(y, -y)$ with $y \in \mathcal{G}$. Then $\Phi_f$ is left invariant under the rational Siegel parabolic $P$, the [[Eisenstein series|3NZBZXYWAJ]] $\sum_{\gamma \in P(F) \backslash G(F)} \Phi_f(\gamma g)$ converges, and it equals the average of $\theta(g, \cdot\,; f)$ over $U(B)(F) \backslash U(B)(\mathbb{A})$.

Part 3 has the form of the Siegel-Weil formula of Weil (Acta Math. 113, 1965) for the pair $(U(n,n), U(B))$. We have not unfolded `IsWeilDatumO`, `IsThetaFunO` or `D7`, so we do not claim that each condition matches Weil's.

## Proof

The proof is `weilSiegelFormulaUnitary_of_two` applied to two results.

- `UpperTheory.Lit.weilThetaConvergence` proves `WeilThetaConvergence`: under the same rank condition, the absolute theta integral of each Schwartz function is finite. Its proof is `weilThetaConvergence_of_siegelSet` applied to `siegelSetUnitary_of_core`, which proves `SiegelSetUnitary` (by its name, a result on Siegel sets; not unfolded).
- [`weilSiegelFormula`](/entry/weil-siegel-formula/) proves `WeilSiegelFormula`: for $2n < m$ and a Weil representation in the Schwartz model, the Siegel Eisenstein series of $\Phi$ at $1$ equals the average of the theta sum.

`weilSiegelFormulaUnitary_of_two` gets part 1 from the first result by `absoluteThetaIntegral_le_continuousSeminorm`, part 2 from it by `integrable_thetaKernel_weilRange`, and part 3 from the second result by `siegelFormula_theta_of_schwartz'`.

## In the Lean code

The theorem is at [FockAnisoFree.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/FockAnisoFree.lean#L12). The statement is at [WeilSiegelFormulaUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/WeilSiegelFormulaUnitary.lean#L56). `weilSiegelFormulaUnitary_of_two` is at [SiegelFormulaThetaOfSchwartz.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/SiegelFormulaSchwartz/SiegelFormulaThetaOfSchwartz.lean#L112).

- The statement is not for an arbitrary CM extension. The fields come from a `D7` datum, which fixes much more data.
- In the same file, `fockAniso_free` takes a hypothesis of type `SiegelWeilAnisotropicUnitary` and does not use it ([L17](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/FockAnisoFree.lean#L17)). An `example` checks that its type is the type of `siegelWeilFockAniso_of_siegelWeilAnisotropic`. So that theorem is proved with its hypothesis unused.
