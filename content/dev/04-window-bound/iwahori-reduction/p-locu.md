---
id: p-locu
title: The zeta class does not vanish on inertia
kind: theorem
decl: UpperTheory.Kd.C7.pLocu
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.LangPolynomials.NormFactorLeOne
covers: 614
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ZetaEulerSystemNonvanishing}(\mathrm{Pin7})$, one of the two halves of [the unramified zeta theorem](/entry/zeta-ur/). It is a pass-through: it gives two theorems to [`LocalUnitsRoots.main`](/entry/local-units-roots-main/), and that entry has the real argument.

## Statement

Let $\ell$, $e$, $S$, $A$, $W$ satisfy $\mathrm{Nf}$, and let $g$ be a newform of weight $2e+1$ with $\mathrm{SrcUr}$, as in [the unramified zeta theorem](/entry/zeta-ur/). Let $y$ be a class with $\mathrm{Sys}$, let $(Z_r)$ be a system of local cocycles with $\mathrm{IwSys2}$, linked to $y$ by $\mathrm{SpLink}$, and suppose $\mathrm{Pin7}$.

**Theorem.** $\mathrm{NzAt}$ holds: there is $s$ in the inertia group at $A$ with $\bar\chi(s) = 1$, $W(s)_{22} = 1$ and $y(s)_2 \neq 0$.

[The entry for `LocalUnitsRoots.main`](/entry/local-units-roots-main/) unfolds $\mathrm{SpLink}$ and $\mathrm{Pin7}$.

## Proof

The proof is one term: `LocalUnitsRoots.main` applied to two theorems.

- `GlobalTheory.T.nonvanishing_transfer_characterSums_powerSeries` fills the hypothesis `h48`. It says: if the twisted sums of two power series $G$ and $L$ agree up to units and the factor $1 - c_0\psi^{-1}(c_0)$, and the moments of $L$ against $\varphi(x)x^e$ do not vanish, then the moments of $G$ do not vanish. It is a second name of `GlobalTheory.KZ.Cmp.nonvanishing_transfer`.
- `GlobalTheory.T.quotient_char_trivial_inertia_cyclotomic_tower` fills `h50`: under $\mathrm{Nf}$ and $\mathrm{SrcUr}$, $W(s)_{22} = 1$ for each $s$ in inertia with $\bar\chi(s) = 1$. It is a second name of `GlobalTheory.quot_eq_one_of_cycBar_eq_one`.

We have not opened the proofs of these two theorems.

## In the Lean code

The theorem is at [NormFactorLeOne.lean, line 162](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L162). The statement is in [ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean#L28). Of its 614 declarations, 483 are below `LocalUnitsRoots.main`. That theorem is `private`, at line 99 of the same file.
