---
id: down-ne-k-of-hypotheses-prime
title: The theta lift from a definite space is not zero, by the doubling method
kind: theorem
decl: GlobalTheory.Core.Rk.Exh.Top.downNe_k_of_hypotheses'
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.KplugFill
covers: 4128
status: drafted
drafted_by: writer@claude
---
This theorem proves `DownNe D`: the theta lift of a suitable automorphic form on a positive definite unitary group is not identically zero. It is `downNe_of_core` with one hypothesis filled in by the proved theorem [`resCore`](/entry/res-core/), and that theorem is 3,947 of the 4,128 declarations below this one. Its only user is the copy [`downNe_of_eulerRight_doubling`](/entry/down-ne-of-euler-right-doubling/), which feeds the [lift injectivity theorem](/entry/lift-inj-non-van-type-nz-of-hypotheses-alt/).

## Statement

Assume `ResidueKilled.DM` and `SimplePole`, and let $D$ be a datum with `EulerRight D`. Then `DownNe D`.

- `DM` is the doubling method input. For a space of positive rank, the Siegel Eisenstein series of a section of the degenerate principal series continues and is regular up to some order. For cusp forms $f_1, f_2$, the basic identity of the doubling method holds for $\operatorname{Re} s > \operatorname{rank}/2$ and the zeta integral continues.
- `SimplePole`: let $c$ be a family of $r$ parameters of size at most $Nw^{(r-1)/2}$ off a finite set $S$, and let $P$ be its twist plus a segment of length $t \ge r + 5$. Then $L^S(s, P) = L^S(s, c) \prod_{i < t} \zeta^S(s + \tfrac{t-1}{2} - i)$, $L^S(s, c)$ is holomorphic and nonzero for $\operatorname{Re} s > \tfrac{r+1}{2}$, and the product has a simple pole at $s = \tfrac{1+t}{2}$.
- `EulerRight D`: off $S$, the doubling zeta integral equals $L^S(s + \tfrac12)/d^S(s)$ times an integral over the places in $S$, for $\operatorname{Re} s > \operatorname{rank} A + 1$.

`DownNe D` is stated in the [entry of the copy](/entry/down-ne-of-euler-right-doubling/).

## Proof

The proof is `downNe_of_core hDM resCore hSP`. `downNe_of_core` takes `ResCore` as a hypothesis, and `resCore` proves it. `ResCore` says that, at $s = t/2$, the coefficients `cf … k` of a regularised Siegel Eisenstein series vanish for $k \ge 2$, and the coefficient for $k = 1$ integrates to $0$ against any $\kappa$ that kills all theta integrals. We have not unfolded `cf`.

`downNe_of_core` argues by contradiction. Suppose that all theta lifts of $u$ vanish.

1. A Witt decomposition writes a larger space $B$ as $W$ plus hyperbolic planes $H$. A vacuum vector on $(A, H)$ and the given $\Phi$ give a Fock vector on $(A, B)$.
2. Since all lifts vanish, the doubling integrals against theta kernels vanish (`doubling_integrals_vanish_of_all_lifts_vanish`). Then `Kplug.res_killed'`, with `ResCore`, gives a residue coefficient $E_1 = 0$.
3. `zeta_eq_integral_integrand_nc` (from `DM`) and `EulerRight` write the zeta integral as $L^S(s + \tfrac12, \mathrm{par}, \chi_W)/d^S(s) \cdot C$, with $C \neq 0$ by `levelPlaces_integral_nonzero_constant`.
4. `zeta_integral_eisenstein_residue` makes the coefficient of $(s - t/2)^{-1}$ equal to $0$.
5. `zeta_residue_ne_zero_of_simple_pole_lift_L_function`, from `SimplePole`, says that this coefficient is not $0$.

This is the shape of the doubling method of Piatetski-Shapiro and Rallis (Gelbart, Piatetski-Shapiro, Rallis, *Explicit constructions of automorphic L-functions*, LNM 1254, 1987): a pole of the $L$-function forces a theta lift to be nonzero.

## In the Lean code

The theorem is at [KplugFill.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/KplugFill.lean#L18). `downNe_of_core` is at [Rethread.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ResidueVanishing/Rethread.lean#L19), and `ResCore` at [HasLevel.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/SingularNullSets/HasLevel.lean#L19).

The definition of `DM` has a conjunct `True` in the middle ([DmOfHyp.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinResidues/AnisotropicGlobalForms/DmOfHyp.lean#L18)), and `dm_of_two`, which proves `DM`, takes an argument of type `True`.
