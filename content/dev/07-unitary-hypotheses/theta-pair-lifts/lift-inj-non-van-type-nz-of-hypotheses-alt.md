---
id: lift-inj-non-van-type-nz-of-hypotheses-alt
title: Injectivity and nonvanishing of the downward theta lifts of a real datum
kind: theorem
decl: GlobalTheory.Core.Rk.LiftOnto.liftInj_nonVan_typeNZ_of_hypotheses_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.LiftInjNonVanTypeNZOfPrints
covers: 4220
status: drafted
drafted_by: writer@claude
---
This theorem proves three facts about the theta lifts of a real datum: they are injective on good eigenvectors, the downward lift of a nonzero eigenvector with a string of parameters is not zero, and a good eigenvector with zero lift is zero. Its only user is the copy [`liftInj_and_nonVan_typeNZ_of_given`](/entry/lift-inj-and-non-van-type-nz-of-given/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The main input is the nonvanishing of the theta lift from a definite space, [`downNe_of_eulerRight_doubling`](/entry/down-ne-of-euler-right-doubling/). Below this theorem are 4,220 declarations.

## Statement

Assume five named inputs: `CuspRapidDecay`, `DoublingMethodLocalZetaIntegrals`, `UnramifiedDoublingGL`, `HeckeLPartialContinuation` and `HoweUnram`. Let $D$ be a datum, $G$ a finite group, $A$ a family over $D$, $K_s$ a number field, $R$ a real datum over $A$ and $K_s$, and $F$ a face. The real datum holds hermitian spaces $V_i$ and $W_i$, Weil representations on the pairs $(V_i, W_i)$, Hecke modules on both sides and linear theta maps $\theta_F$ and $\theta_G$ from the $V$ side to the $W$ side. Assume `Given R F` (a core condition, a choice of parameters, absolute irreducibility of the characters of $A$, good types, a guard, and a gap $\lambda_n - \lambda_{n+1} \ge 100 r^4$) and `R.FullP` (each Weil representation of $R$ is full).

Let $y$ be an eigenvector for a family of Hecke operators that is compatible with $R$, with eigensystem $s$. Say that $s$ *has a string* if at each good place $w$ its Satake multiset is $B' + \{z\, q^{(t-1)/2 - k} : 0 \le k < t\}$, with $q = Nw$ and each $a \in B'$ of size at most $q^{(r-1)/2}$. Then:

1. (`LiftInj`) at $t = \mu_0$: if $x$ and $y$ have the same eigensystem, $\theta_G(x) \neq 0$, $y$ is good and $\theta_G(y) = 0$, then $y = 0$;
2. (`NonVan`) for all $i$ and $t$: if $s$ has a string and $y \neq 0$, there are a theta function $f$, a functional $l$ and a point $g$ with $\int \theta(h, g; f)\, l(y(h))\, dh \neq 0$;
3. (`TypeNZ`) for all $i$ and $t$: if $s$ has a string, $y$ is good and $\theta_G(y) = 0$, then $y = 0$.

We have not unfolded `Hk3.Core`, `GoodTypes`, `QGuard` or the Hecke modules.

## Proof

1. `doublingEulerProductFarRight_of_rapidDecay_unramified` gives the unramified computation of the doubling integral, `EulerRight D`.
2. `simplePole_of_hecke` gives a simple pole of the partial $L$-function of a lifted family, from `HeckeLPartialContinuation`.
3. From these two and the doubling method, [`downNe_of_eulerRight_doubling`](/entry/down-ne-of-euler-right-doubling/) gives `DownNe D`: the theta lift of a form on a definite space is not zero.
4. `thetaLift_nonvanishing_onString_of_definiteDown` turns `DownNe D` into `NonVan`.
5. Six lemmas give the local facts: eigenforms go to eigenforms (`DownEig`), generation at finite and real places (`GenFin`, `GenInf`), good vectors stay good (`GoodMem`), good types exclude the level character (`GoodNoChi`), parameters exist (`ParamsEx`), and the unramified correspondence of parameters holds at all good primes (`UnrCorr`). Three of them use `HoweUnram`.
6. `typeNZ_of_nonVan_gen` proves `TypeNZ` from `NonVan` and the local facts.
7. `liftInj_of_typeNZ` proves `LiftInj` from `TypeNZ` and the local facts at $t = \mu_0$.

The rest is bookkeeping.

## In the Lean code

The theorem is at [LiftInjNonVanTypeNZOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LiftInjNonVanTypeNZOfPrints.lean#L14). All five inputs are used.

- `HeckeLPartialContinuation` is proved outright as `HeckeLPartialContinuation_holds`, and `HoweUnram` as `howeUnram_holds`. This theorem still takes both as hypotheses.
- `liftInj_nonVan_typeNZ_of_classicalTheorems` in [UnramifiedHoweLiftRows.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnramifiedHoweLiftRows.lean#L32) is the same proof with one more input, `RegularisedSiegelWeilFirstTerm`, and with `DoublingMethod` in place of `DoublingMethodLocalZetaIntegrals`.
- The word "prints" in the file name matches no object in the statement.
