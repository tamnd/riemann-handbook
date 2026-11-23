---
id: siegel-weil-std-pre-k
title: The Siegel-Weil formula from Poisson summation and the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilFinPre
covers: 1148
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd_k` from two hypotheses: a Poisson summation formula and the constant term split. Its user is [`siegelWeilStd_of_ct_k`](/entry/siegel-weil-std-of-ct-k/), which proves the Poisson formula. That result goes to [the Siegel-Weil formula of the Galois row](/entry/siegel-weil-std-k/). This theorem gets the action of the Weyl element in the Schrödinger model, and the inputs that the main proof needs. Below it are 1,148 declarations.

## Statement

**Theorem.** Suppose that `Poisson_k` and `CTSplit_k` hold. Then `SiegelWeilStd_k` holds.

`SiegelWeilStd_k` is stated in [the Siegel-Weil formula of the Galois row](/entry/siegel-weil-std-k/), and `CTSplit_k` in [the entry above](/entry/siegel-weil-std-of-ct-k/). `Poisson_k` says: for each Siegel-Weil datum, each Haar measure $\nu$ on the adelic $m \times n$ matrices with a fundamental domain of volume 1 for the rational matrices, each sign $\varepsilon$ and each Schwartz function $f$,

$$\sum_{X \in M_{m \times n}(E)} \int \psi\bigl(\varepsilon \operatorname{tr} \operatorname{gram}(X, Z)\bigr) f(Z)\, d\nu(Z) = \sum_{X \in M_{m \times n}(E)} f(X).$$

## Proof

A Siegel-Weil datum $d$ bundles the objects of `SiegelWeilStd_k` with its hypotheses. It defines a transform $T\Phi(X) = l(\rho(X b_2^T)\Phi)$ of a Schwartz function $\Phi$, on adelic $m \times n$ matrices $X$. The proof has four steps.

1. **The Weyl element.** `tWeyl_of_k` proves `TWeyl_k`: for a Weyl element $w$ with sign $\varepsilon$, $T(\omega(w)\Phi)(X) = \int \psi(\varepsilon \operatorname{tr} \operatorname{gram}(X, Z))\, T\Phi(Z)\, d\nu(Z)$. The argument is this. By `TW.Twu.uniq_k` and `TW.UpToPf.upTo_of_k`, the formula holds up to a constant $C$ that does not depend on $\Phi$. By `TW.ThetaWPf.thetaW_k`, $\omega(w)$ preserves the theta sum, and some $\Phi_0$ has $\theta(\Phi_0) \neq 0$. By `tTheta_k`, $\theta(\Phi) = \sum_X T\Phi(X)$ over rational $X$. Apply the Poisson formula to $T\Phi_0$. Then $C\,\theta(\Phi_0) = \theta(\Phi_0)$, so $C = 1$.
2. **The five properties.** `tAll_of_k` puts `TWeyl_k` together with `tBij`, `tPar_k`, `tTheta_k` and `thetaAuto_k` into `TAll_k`. The [Siegel-Weil chapter](/proof/siegel-weil/) states these five properties for the copy without `_k`.
3. **Two inputs from `TAll_k`.** `KFP.kFinPoly_of_k` proves `KFinPoly_k`: for each $K$-finite $\Phi$, the function $T\Phi$ lies in the subspace `R.fock` of each datum `R`. It uses `tUnit_k`, `tHeis_k`, `fockMem_k` and two local lemmas. `Ald.ldEx_of_k` proves `LDEx_k`: for $n \geq 2$ each datum has a lower rank datum, which embeds the problem of size $n - 1$. We have not unfolded `R.fock` and the lower rank datum.
4. **The assembly.** `siegelWeilStd_mid_k` gives `SiegelWeilStd_k` from `TWeyl_k`, `KFinPoly_k`, `LDEx_k` and `CTSplit_k`.

## In the Lean code

The theorem is in [SiegelWeilFinPre.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinPre.lean#L30). The lemmas it calls:

- `tWeyl_of_k`, in the same file ([L28](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinPre.lean#L28)), and `TW.tWeyl_of_k` in [SiegelWeilTwSt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilTwSt.lean#L25).
- `tAll_of_k` in [SiegelWeilFinCore.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinCore.lean#L43).
- `KFP.kFinPoly_of_k`, `Ald.ldEx_of_k`, `locOpEx_of_tAll_k` and `locInst_of_k`.
- `siegelWeilStd_mid_k` in [SiegelWeilFinMid.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinMid.lean#L23).

The theorem is a copy of [`siegelWeilStd_pre`](/entry/siegel-weil-std-pre/) with `_k` added to each name. The term `tWeyl_of_k hP` occurs twice in the proof, once for `TAll_k` and once as an argument of `siegelWeilStd_mid_k`.
