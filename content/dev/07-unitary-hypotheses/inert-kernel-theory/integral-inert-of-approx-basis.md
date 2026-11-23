---
id: integral-inert-of-approx-basis
title: Integrality at inert primes from weak approximation and a local basis
kind: theorem
decl: Formalism.L2.KerInert.integral_inert_of_approx_basis
module: Formalism.LocalToGlobal.InertKernelTheory.IntegralInertOfApproxBasis
covers: 746
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntInert` from two inputs: weak approximation at the primes above $p$ (`WAPlaces`) and a local orthonormal basis (`LocBasisMM`). It is a pass-through. It builds the conjunction `WeakApproxAndOrthonormalBases` and calls [`integral_inert_of_weakApprox`](/entry/integral-inert-of-weak-approx/), which has the real proof. Its only user is [`kernels_integral_inert`](/entry/kernels-integral-inert/), which states `IntInert` and supplies the two inputs.

## Statement

Assume `CM2`, as an instance.

**Theorem.** If `WAPlaces` and `LocBasisMM` hold, then `IntInert` holds.

- `WAPlaces`: for a lattice $L$ that is isometric to the standard lattice at each prime above $p$, there is one global isometry of the standard hermitian form that sends the standard lattice to $L$ at all these primes at once.
- `LocBasisMM`: for $p \ge 5$ inert, the space `YYl` of the standard lattice of rank $1$ has a local basis at $p$ with a unit Gram determinant.

## Proof

The proof fills the three parts of `WeakApproxAndOrthonormalBases`. The first is the hypothesis `WAPlaces`.

1. `OneCopyOrth` is `one_theta_orthonormal`, from a Gram-Schmidt step. It gives an orthogonal local basis $e_i$ of the same space with $h(e_i, e_i)$ a positive rational that is a $p$-adic unit.
2. `IsomONB` is `isomONB_ofLB hLB`, which applies `isomONB_of_facts` to `LocBasisMM` and three proved facts: `conjugation_extension_inert`, `rational_coordinates` and `conjugation_fixed_closure`. `IsomONB` gives an isometry $g_1$ of a space of dimension $4|\mathrm{Tau}|$, a frame, a conjugation $\sigma_p$ of $\mathbb C_p$ and a local orthonormal basis for $\sigma_p$.

## In the Lean code

The theorem is at [IntegralInertOfApproxBasis.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/IntegralInertOfApproxBasis.lean#L15), and the helper `isomONB_ofLB` at line 10 of the same file. `OneCopyOrth` is in [DefsMMOnb.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/DefsMMOnb.lean#L9) and `IsomONB` in [OneCopyTh1S.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/OneCopyTh1S.lean#L51). We have not unfolded `IsFrameH`, `IsConjP` or `IsLocONB`.

The `CM2` instance comes from `variable [Fact CM2] in` at line 13. This theorem only passes it on to `integral_inert_of_weakApprox`.
