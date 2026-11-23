---
id: spec-data
title: A Hecke function with the spectral property from a type
kind: theorem
decl: UpperTheory.Gal.Spc.specData
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ScalarCommutation.SpecData
covers: 806
status: drafted
drafted_by: writer@claude
---
This theorem proves `SpecData` from `WtOf`. It is the last step of [specTopG](/entry/spec-top-g/): there the auxiliary prime $r$, the places $W$ and the type `Ty` are already chosen, and here the Hecke function $f$ is built. The function is $f = u^{*m} * e$, a convolution power of one Hecke operator $u$ applied to the idempotent $e$ of the type. The general spectral step is `specOfF`. This proof checks its hypotheses. Below it are 806 declarations.

## Statement

`SpecData` is in [ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/ExistsIdempotentHeckeOperatorWithRegularSupportAlt.lean#L135). It is `ForData` of a property. `ForData` takes all the data and hypotheses of [specTopG](/entry/spec-top-g/), together with $r$ and $W$ with `SlopeTestRemainingChoices`, a level $N$ with $r \mid N$, and a type with `TyOK`. The property: if `Extra S F.j` holds, then each family $g_j$, $\theta_j$ that passes `Seen F V r` has an $f$ with `IsFnL S.L N f` and `Spec S.L V.lam K_N (g_j.fn) θ f`.

## Proof

The proof is in [SpecData.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/SpecData.lean#L64). Write $e$ for `Ty.tf 1` and $*$ for convolution on $K_N$.

1. `tyTop` gives a level `Lv` with group $K_N$, an open compact `Kw` with `Ty.L.Fact`, an open compact group $J$ with open kernel of `Ty.ψ`, and the fact that each smooth irreducible representation with a nonzero $\psi$-eigenvector is cuspidal.
2. `auxFn` gives Hecke operators $u$, $u'$ with $e * u = u = u * e$ and $u' * u = e$. The operator $u$ commutes with the span `Off2`. For each $m \ge 1$ there are sets $X_w$, $w \in W$, of elements with separable characteristic polynomial, stable under the Iwahori subgroup, that contain the support of $u^{*m} * e$. That support is also integral.
3. `memFn` puts each $g_j$ in the Hecke algebra. `memComm` shows that $g_j * e$ is in `Off2` and that the $g_j$ commute on $e$. `eigEx` gives `HasEig`: a nonzero form fixed by $e$ on which each $g_j$ acts by $\theta_j$.
4. From these facts and `span_fix` the proof builds `Rel`: $e$ is idempotent, $e$ fixes $g_j * e$ and $u * e$, the $g_j$ and $u$ commute on $e$, and $u' * u * e = e$.
5. `splitC` splits the group at $w_0$. With `cuspIrr_kFinite_rep_eq_centralCuspForm` and the cuspidality from step 1, $e$ is a cusp form for this split.
6. For each $m$, the set $A'$ of $y$ with components in $X_w$ for all $w \in W$ is stable under the $g_j$. Its elements are regular by `Extra`: `Half r W` and `sepConj` give separability at every place above $r$.
7. `specOfF`, with `FinCls_holds` (finitely many classes) and `WtOf`, gives $m \ge 1$ with `Spec` for $u^{*m} * e$. `words` puts this function in the Hecke algebra. Step 2 gives integral support. This is `IsFnL`.

## In the Lean code

`powFn K u e m` is `(conv K u)^[m] e`, in [TypeSlice.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/TypeSlice.lean#L72). `SpecOfF` is in [SpecOfF.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ScalarCommutation/SpecOfF.lean#L167). I have not unfolded its proof or the helpers of `Spec`. The hypotheses `Odd n`, `Sc` and the good prime $q$ are not used in this proof. They pass through to `tyTop`, `auxFn`, `memFn`, `memComm` and `eigEx`.
