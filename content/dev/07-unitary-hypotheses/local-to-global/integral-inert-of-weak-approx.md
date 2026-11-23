---
id: integral-inert-of-weak-approx
title: Integrality at inert primes from weak approximation and orthonormal bases
kind: theorem
decl: Formalism.L2.KerInert.integral_inert_of_weakApprox
module: Formalism.LocalToGlobal.InertKernelTheory.IntegralInertOfWeakApprox
covers: 526
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntInert`, the $p$-adic integrality of the theta kernels at an inert prime $p$, stated in [`kernels_integral_inert`](/entry/kernels-integral-inert/). Its input is the conjunction `WeakApproxAndOrthonormalBases`, which [`integral_inert_of_approx_basis`](/entry/integral-inert-of-approx-basis/) builds. The proof gives eleven facts to the assembly lemma `intInert_of`, and that lemma holds the structure of the argument.

## Statement

Assume `CM2`, as an instance. Let `WeakApproxAndOrthonormalBases` be `WAPlaces ∧ OneCopyOrth ∧ IsomONB`.

**Theorem.** If `WeakApproxAndOrthonormalBases` holds, then `IntInert` holds.

## Proof

The proof calls `intInert_of`. It gets `WeakApprox` from `WAPlaces` by `weakApprox_of`. It gets `BasisInv` from `unit_substitution_local` by `basisInv_of_loc`. It gets `ThFourInt` from `thFourInt_of`, which uses `IsomONB` (through `oneCopyLoc_of_isom`), `OneCopyOrth` (through `globONB_of`), `unit_substitution_local` and `four_products_from_one`. The other eight facts, such as `combination_fact`, `pullback_fact` and `tensor_matrix_units_fact`, are theorems with no explicit hypothesis. Of the inputs, `unit_substitution_local` and `oneCopyLoc_of_isom` carry the `CM2` instance.

`intInert_of` works in these steps. Write `IntS` for "integral after substitution of the formal logarithm, for every local orthonormal basis".

1. By `IsComb`, $F$ is a combination $\sum_k r_k F_k$ with $r_k$ integral, where $F_k$ is the Taylor series of the kernel for lattices $(L_k, L'_k)$, translated by a torsion point $t_k$ of order prime to $p$. `CombFact` says that `IntS` is closed under such combinations.
2. `PairFact` says that `IntS` depends only on the lattices at $p$. Since $L_k$ equals $L$ at $p$, it is enough to treat $(L_k, L'_k)$.
3. `WeakApprox` writes $L_k = \gamma M$ and $L'_k = \gamma' M'$, with $\gamma, \gamma'$ unitary and $M, M'$ equal to the standard lattices at $p$. The Euler product identity `eulerProduct_eq_of_curve_ideal` moves the kernel of $(M, M')$ to the kernel of $(\gamma M, \gamma' M')$. `PullTors` and `PullFact` move the torsion point and the integrality.
4. `StdStep` writes the translated kernel of $(M, M')$ as a combination, with integral algebraic coefficients, of translates of the standard kernel `thZero`. `PSerLin` passes the combination through the Taylor series.
5. `TensFact` reduces the standard kernel to the $2 \times 2$ case. `ThFourInt` gives integrality there for some basis (`IntSome`), and `BasisInv` gives it for all bases.

## In the Lean code

The theorem is at [IntegralInertOfWeakApprox.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/IntegralInertOfWeakApprox.lean#L9). `intInert_of` is at [IntAsm.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/IntAsm.lean#L79), and the eleven facts are in [DefsInt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/DefsInt.lean#L33). We have not unfolded `thZero`, `pull` or `tPull`.

`intInert_of` names the hypothesis `admitted` on $(L, L')$ as `_hA` and does not use it. Step 3 uses the `admitted` condition of each $(L_k, L'_k)$ that `IsComb` gives. The same file has `jets_inert_of_weakApprox`, a variant for jets.
