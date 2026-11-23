---
id: lift-rows-injective-and-type-properties-of-nonvanishing
title: Nonvanishing of the downward lifts gives injectivity of the theta lift
kind: theorem
decl: GlobalTheory.DownLift.liftRows_injective_and_typeProperties_of_nonvanishing
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftRowsInjectiveAndTypePropertiesOfNonvanishing
covers: 620
status: drafted
drafted_by: writer@claude
---
This theorem collects properties of the theta lifts of a real datum. Its main output is `TypeNZ`: a good Hecke eigenvector with a string and zero theta lift is zero. It is the proof behind the second name [`liftInj_and_properties_of_rallis_of_nonVan`](/entry/lift-inj-and-properties-of-rallis-of-non-van/), which [`lift_splits_locally`](/entry/at-real-lift-splits-locally/) uses.

## Statement

As in [`lift_splits_locally`](/entry/at-real-lift-splits-locally/), let $R$ be a real datum over a datum $D$, with hermitian spaces $V_i$, $W_i$, and $F$ a face. For each $i$ and each $t$ there are two theta maps on the space $H_{V_i}$: $\theta_G$ into a Hecke space $H_{W_i}$, and $\theta_F$ into the automorphic forms on $W_i$. A vector $y$ is *good* (`GoodVt`) if an average over the finite group $G$ fixes it; we did not unfold this average (`gaL`). The facts in the conclusion, from [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L53):

- `NonVan`: a nonzero eigenvector whose eigensystem has a string has a theta function $f$ with nonzero downward integral.
- `GoodMem`: $e(\theta_G y) = \theta_F y$ for good $y$, with $e$ the inclusion of $H_{W_i}$.
- `DownEig`: for each eigensystem $s$ there is $c$ with $\theta_F(y)$ in the $c$-part for all $s$-eigenvectors $y$.
- `UnrCorr`: at good places the Satake parameters of $s$ are those of $c$, twisted by `valV`/`valW`, plus a string.
- `Saturated`: for $s$ with a string there is $c$ such that each good $s$-eigenvector $y$ is $\theta_G^*(x)$ for some $x$ in the $c$-part.

`LiftInj R` says: at $t = \mu_0$, if $x$ and $y$ have the same eigensystem, $\theta_G(x) \ne 0$, $y$ is good and $\theta_G(y) = 0$, then $y = 0$.

**Theorem.** Assume `CuspRapidDecay`, `HoweUnram`, `Given R F`, `R.FullP`, `RallisConv D`, and `NonVan R i t` for all $i, t$. Then `LiftInj R` holds, and for all $i, t$ so do `TypeNZ`, `GoodMem`, `DownEig`, `UnrCorr` at all places, and `Saturated`.

## Proof

1. Six facts come from `Given` and `FullP` alone: `DownEig` (`downEig`, uses `HoweUnram`), `GenFin` ([`genFin`](/entry/gen-fin/), uses `HoweUnram`), `GenInf` ([`genInf`](/entry/gen-inf/)), `GoodMem` (`goodMem_of_given`), `GoodNoChi` (`goodNoChi`) and `ParamsEx` (`paramsEx`, uses `CuspRapidDecay`).
2. `unrCorr_inert` (uses `HoweUnram`) gives `UnrCorr` at places $w$ with $\bar w = w$, and `unrCorr_split` at the others. A case split gives `UnrCorr` at all places.
3. `TypeNZ` (`typeNZ_of_nonVan_gen`). Let $y \ne 0$ be good with $\theta_G y = 0$. By `GoodMem`, $\theta_F y = 0$. By `GenInf`, the downward integrals of $y$ against the finite-like theta functions vanish. By `GoodNoChi`, $y$ has no level character. Then `GenFin` says $y$ has no nonzero downward integral, against `NonVan`.
4. `LiftInj` (`liftInj_of_typeNZ`). From $\theta_G x \ne 0$ we get $\theta_F x \ne 0$. Then `hasString_of_lift` gives a string for $s$, from `DownEig`, both halves of `UnrCorr` and `ParamsEx`. Then `TypeNZ` gives $y = 0$.
5. `Saturated` (`Sat.saturated`). Let $N$ be the space of good $s$-eigenvectors. Then $\theta_G^*\theta_G$ preserves $N$ (`eig_keep`, uses `HoweUnram`), and $\theta_G$ is injective on $N$ by `TypeNZ`. So $\theta_G^*\theta_G$ maps $N$ onto $N$ (`exists_adjoint_comp`), and each $y \in N$ is $\theta_G^*(x)$ with $x = \theta_G y'$. `DownEig` and `GoodMem` put $x$ in the $c$-part.

## In the Lean code

The theorem is in [LiftRowsInjectiveAndTypePropertiesOfNonvanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftRowsInjectiveAndTypePropertiesOfNonvanishing.lean#L30). `LiftInj` and `Given` are in [RealLowestKTypeCoeffSquareIntegrable.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L73).

The proof also calls [`rawLift_main`](/entry/raw-lift-main/). This call is the only use of `RallisConv D`, and it gives `UpInj` for each $(i, t)$. This `UpInj` goes to `saturated`, with `UnrCorr` and `ParamsEx`. But `saturated` drops these three arguments: its `intro` names them `_` ([ExistsAdjointComp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsAdjointComp.lean#L313)). So `RallisConv D` and the subtree of `rawLift_main`, 582 of the 620 declarations, do no logical work. One could drop `RallisConv D` after a change to the signature of `saturated`.
