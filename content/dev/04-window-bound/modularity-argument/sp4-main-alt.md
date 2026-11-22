---
id: sp4-main-alt
title: The counts in cases II and III, with the roots of unity removed
kind: theorem
decl: UpperTheory.V.Th.sp4Main_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ConductorAtMapInjectiveCoeff
covers: 574
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{CountII}$ and $\mathrm{CountIII}$ from nine inputs. Its user [`countII_and_countIII_of_printsH_of_sp4In`](/entry/count-ii-and-count-iii-of-prints-h-of-sp4-in/) supplies them. The bound itself is in the private lemma [`main_big`](/entry/main-big/), which needs extra roots of unity in the coefficient ring. This theorem removes that condition by a change of coefficients. That step is short, but it is not only a pass-through.

## Statement

**Theorem.** Assume `SymplecticFourImageDense`, `CohomologyHyp`, `LemmaM`, `LemmaM'`, `LemmaP`, `NumberSp4Alt`, `RigiditySymplecticFour`, `X.CorX`, and `SoV` and `SoFin` for each $\Omega$ and $l$. Then $\mathrm{CountII}$ and $\mathrm{CountIII}$ hold.

The counts are stated in [the parent entry](/entry/count-ii-and-count-iii-of-prints-h-of-sp4-in/). The inputs are described in [`main_big`](/entry/main-big/).

## Proof

First the theorem proves the count for the case condition "case II or case III". Fix $\chi$ and take $C$ from `main_big`. Let $h$, $l$, the coefficient ring $c$, $e$ and $\psi$ be given.

1. `main_big` needs $\mathcal{O}_c$ to contain the $2^{n_{II}}$-th and $2^{n_{III}}$-th roots of unity, where $n_{II} = n_{II}(l, \psi)$ and $n_{III} = n_{III}(l, \psi)$ are defined by `Host.nII` and `Host.nIII`.
2. `exists_coef` gives a coefficient ring $c_1$ with enough $2^{n_{II} + n_{III}}$-th roots of unity. `coefSup` gives $c'$ that contains both $c$ and $c_1$. So $c'$ has enough roots of unity of both orders.
3. Let $f \colon \mathcal{O}_c \to \mathcal{O}_{c'}$ be the inclusion, and let $\psi' = f \circ \psi$. Since $f$ is injective, $\psi'$ has the same order, kernel, parity and values of `n0` and `c2` as $\psi$. So $n_{II}$ and $n_{III}$ do not change, $\psi'$ is in $h.X\ c'\ e$, and $\psi'$ is in the same case.
4. `main_big` gives the bound for $\psi'$ over $c'$. `coefIndep` says that $V_{\mathrm{len}}$ and $V_n$ do not depend on the coefficient ring when the values of the characters agree in $\overline{\mathbb{Q}}_l$. This gives the bound for $\psi$ over $c$.

Then $\mathrm{CountII}$ and $\mathrm{CountIII}$ follow by restriction to each case.

## In the Lean code

The theorem is in [ConductorAtMapInjectiveCoeff.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean#L131). The transfer lemmas (`chHom_inj`, `chHom_ord`, `chHom_chiP`, `chHom_ker`, `chHom_even`) and `enough_of_le` are private lemmas in the same file. `coefIndep` is in [CoefIndep.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/CoefIndep.lean#L68). `nII` and `nIII` are in [DirichletPrimeToLPartMulLPowerPart.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean#L221).

Two lemma names do not match their statements. `conductor_at_map_injective_coeff` (line 35) proves that `n0` does not change, and `n0` is defined by a multiplicative order, not a conductor. `parity_at_map_injective_coeff` (line 46) proves that `c2`, the 2-part of a conductor, does not change. The parity statement is `chHom_even`.

The theorem is a copy of `UpperTheory.V.GradeZeroInterpolatingElement.main` in [SymplecticGSp4/ConductorAtMapInjectiveCoeff.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/ConductorAtMapInjectiveCoeff.lean#L152). The copy takes `SymplecticFourImageDense`, `NumberSp4Alt` and `RigiditySymplecticFour` in place of `Aut.Sp4In`, `Af.NumberSp4` and `Af.AdVanishQ`. The two files have the same name and the same private lemmas.
