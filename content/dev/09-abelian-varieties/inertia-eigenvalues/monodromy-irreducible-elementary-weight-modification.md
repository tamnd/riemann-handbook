---
id: monodromy-irreducible-elementary-weight-modification
title: The weight modification step, a second name
kind: theorem
decl: GlobalTheory.T.monodromy_irreducible_elementary_weightModification
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.MonodromyIrreducibleElementaryWeightModificationStatement
covers: 655
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`modStep_holds`](/entry/mod-step-holds/). It proves `ModStep`, step 5 of the induction in [the $p$-adic monodromy theorem in matrix form](/entry/mat-thm-holds/). The real content is in [`modStep_holds`](/entry/mod-step-holds/).

## Statement

`ModStep`. Use the notation of [`matThm_holds`](/entry/mat-thm-holds/). Let $\ell$ be a prime, $P$, $A$ period data with a tie `LocTied l P A`, $K$ a finite extension of $\mathbb{Q}_\ell$, $r \ge 0$, $n$ a finite index set, $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ and $w \colon \{0, \dots, r-1\} \times n \to \mathbb{Z}$. Let $x \ne y$ be two indices in $\{0, \dots, r-1\} \times n$. Assume `IsRat r ρ`, that $\rho$ is framed with weight $w$, and that $\rho$ does not split (`¬ Splits r ρ`). Then there is $\rho' \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ with `IsRat r ρ'`, framed with weight $w + \varepsilon_{x,y}$, such that `AdmSt P ρ'` implies `AdmSt P ρ`.

Here $\varepsilon_{x,y}$ is $-1$ at $x$, $+1$ at $y$ and $0$ elsewhere. So the weight at $x$ drops by one, the weight at $y$ rises by one, and the total weight does not change.

## Proof

The tactic `first | exact @X | …` closes the goal with $X$ = `PMon.modStep_holds`. Nothing else happens.

## In the Lean code

The theorem is in [MonodromyIrreducibleElementaryWeightModificationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MonodromyIrreducibleElementaryWeightModificationStatement.lean#L7). `ModStep` is in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L72), and `Framed`, `Splits` and $\varepsilon$ (`eps`) are in [AdmSt.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmSt.lean#L50).

The word "irreducible" in the name stands for the hypothesis that no change of basis fixed by $\mathrm{Fr}^r$ makes $\rho$ block upper triangular. "Monodromy" refers to the theorem that uses the step, not to a monodromy operator in the statement.
