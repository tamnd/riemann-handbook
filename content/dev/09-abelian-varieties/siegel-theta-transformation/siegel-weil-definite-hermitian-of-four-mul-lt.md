---
id: siegel-weil-definite-hermitian-of-four-mul-lt
title: The Siegel-Weil formula for definite hermitian lattices (statement)
kind: theorem
decl: GlobalTheory.T.siegelWeil_definiteHermitian_of_four_mul_lt
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.SiegelWeilDefiniteHermitianOfFourMulLtStatement
covers: 433
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`siegel_weil_definite`](/entry/siegel-weil-definite/), which has the real content. Its proof only calls that theorem. Its user is the [kernel identity](/entry/kernel-identity/), which applies it in degree $N = r$ to the doubled test functions of a theta system.

## Statement

Let $E$ be a CM field and $\Psi$ a CM type of $E$. Let $n$ be even and $N$ a natural number with $4N < n$. Then `SWAt Ψ n N` holds: for all $M$ and $R$, for each family $\varphi$ of test functions on $M_{n \times N}(E)$, indexed by lattices and `admitted M R`, and for each $Z$ in the hermitian upper half space $\mathcal{H}_N$,
$$\mathrm{swd}(\varphi)(Z, 0, 0) = 0.$$
Here `swd` is the class sum, over the genus of positive definite self-dual lattices `Vset E n M` with weights $1/\#\mathrm{Stab}(\Lambda)$, of the theta series of $\varphi_\Lambda$ minus the Eisenstein series of $\varphi_\Lambda$. So the weighted genus average of theta series equals the Eisenstein series. This has the form of the Siegel-Weil formula for a definite hermitian space in the range of convergence; see A. Weil, "Sur la formule de Siegel dans la théorie des groupes classiques", Acta Math. 113 (1965). The [entry for `siegel_weil_definite`](/entry/siegel-weil-definite/) gives the proof.

## Proof

The proof is `siegel_weil_definite`, an induction on $N$ that uses [`siegelWeil_formula_degree_succ`](/entry/siegel-weil-formula-degree-succ/) for the step.

## In the Lean code

The theorem is in [SiegelWeilDefiniteHermitianOfFourMulLtStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilDefiniteHermitianOfFourMulLtStatement.lean#L9). The proof is the tactic `first | exact @GlobalTheory.SW.siegel_weil_definite | ...`. The two statements are identical, so the first `exact` closes the goal. `SWAt` is in [IsHeatZero.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/IsHeatZero.lean#L15). I have not unfolded the fields of `admitted` beyond their names.
