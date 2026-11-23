---
id: siegel-weil-std-pre
title: The Siegel-Weil formula from Poisson summation and the constant term split
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilStandard.SiegelWeilStdPre
covers: 1128
status: drafted
drafted_by: writer@claude
---
This theorem gives the Siegel-Weil formula `SiegelWeilStd` from two hypotheses: a Poisson summation formula `Poisson` and the constant term split `CTSplit`. Its user is [`siegelWeilStd_of_ct`](/entry/siegel-weil-std-of-ct/), which proves `Poisson`. That result goes to [the Siegel-Weil formula](/proof/siegel-weil/). This theorem gets the action of the Weyl element in the Schrödinger model, and the inputs that the main proof needs. Below it are 1,128 declarations.

## Statement

**Theorem.** Suppose that `Poisson` and `CTSplit` hold. Then `SiegelWeilStd` holds.

`SiegelWeilStd` is the formula of the [Siegel-Weil chapter](/proof/siegel-weil/), and `CTSplit` is stated in [the entry above](/entry/siegel-weil-std-of-ct/). `Poisson` says: for each Siegel-Weil datum $d$, each measure $\nu$ on the adelic $m \times n$ matrices with `IsCov` (a [[Haar measure|CE0V9686M8]] with a [[fundamental domain|WEGEXJBX26]] of measure 1 for the rational matrices), each sign $\varepsilon$ and each $f$ in the [[Schwartz space|GE020MY43M]] `d.schM`,

$$\sum_{X \in M_{m \times n}(E)} \int \psi\bigl(\varepsilon \operatorname{tr} \operatorname{gram}(X, Z)\bigr) f(Z)\, d\nu(Z) = \sum_{X \in M_{m \times n}(E)} f(X).$$

This is the adelic Poisson summation formula of Tate's thesis (J. Tate, Fourier analysis in number fields and Hecke's zeta-functions, in Cassels and Fröhlich, Algebraic Number Theory, 1967, Chapter XV), for the space of matrices.

## Proof

A Siegel-Weil datum $d$ bundles the objects of `SiegelWeilStd` with its hypotheses. It defines a transform $T\Phi(X) = l(\rho(X b_2^T)\Phi)$ of a Schwartz function $\Phi$, on adelic $m \times n$ matrices $X$. The proof has four steps.

1. **The Weyl element.** `tWeyl_of` proves `TWeyl`: for a Weyl element $w$ with sign $\varepsilon$, $T(\omega(w)\Phi)(X) = \int \psi(\varepsilon \operatorname{tr} \operatorname{gram}(X, Z))\, T\Phi(Z)\, d\nu(Z)$. By `TW.Twu.uniq` and `TW.UpToPf.upTo_of`, this holds up to a constant $C$ that does not depend on $\Phi$. By `TW.ThetaWPf.thetaW`, $\omega(w)$ preserves the theta sum, and some $\Phi_0$ has $\theta(\Phi_0) \neq 0$. By `tTheta`, $\theta(\Phi) = \sum_X T\Phi(X)$ over rational $X$. By `tBij`, $T\Phi_0$ is in `d.schM`, so the Poisson formula applies to it. Then $C\,\theta(\Phi_0) = \theta(\Phi_0)$, so $C = 1$.
2. **The five properties.** `tAll_of` puts `TWeyl` together with `tBij`, `tPar`, `tTheta` and `thetaAuto` into `TAll`. The Siegel-Weil chapter states these five properties of $T$.
3. **Two inputs from `TAll`.** `KFP.kFinPoly_of` proves `KFinPoly`: for each $K$-finite $\Phi$, the function $T\Phi$ lies in the subspace `R.fock` of each datum `R`. It uses `tUnit`, `tHeis`, `kfour.auxEx`, `fockMem` and two local lemmas. `Ald.ldEx_of` proves `LDEx` from `TAll` and `kfour.auxEx`: for $n \geq 2$ each datum has a lower rank datum. We have not unfolded `R.fock` and the lower rank datum.
4. **The assembly.** `siegelWeilStd_mid` gives `SiegelWeilStd` from `TWeyl`, `KFinPoly`, `LDEx` and `CTSplit`.

## In the Lean code

The theorem is in [SiegelWeilStdPre.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdPre.lean#L19). The lemmas it calls:

- `tWeyl_of`, in the same file ([L16](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdPre.lean#L16)), and `TW.tWeyl_of` in [TWeylOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WeylTheta/TWeylOf.lean#L26). `Poisson` is defined there at [L19](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/WeylTheta/TWeylOf.lean#L19).
- `tAll_of` in [SiegelWeilStdOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean#L39).
- `KFP.kFinPoly_of` in [KFinPolyOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/RealAdelicFockSpace/KFinPolyOf.lean#L24), `Ald.ldEx_of` in [LdExOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LagrangianDecomposition/LdExOf.lean#L15), `locOpEx_of_tAll` and `locInst_of`.
- `siegelWeilStd_mid` in [SiegelWeilStdMid.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdMid.lean#L16).

The term `tWeyl_of hP` occurs twice in the proof, once for `TAll` and once as an argument of `siegelWeilStd_mid`. The hypothesis `kfour.auxEx` has the type `AuxiliaryPrimeFunction` ([AuxiliaryPrimeFunction.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/AuxiliaryPrimeFunction.lean#L206)). The name is misleading. The statement only says that a measure with `IsCov` and a rational Weyl element exist, and that the group is a locally compact, Hausdorff, second countable topological group. The copy [`siegelWeilStd_pre_k`](/entry/siegel-weil-std-pre-k/) has the same form, with `kfour.auxiliaryExistence_holds` in the place of `kfour.auxEx`.
