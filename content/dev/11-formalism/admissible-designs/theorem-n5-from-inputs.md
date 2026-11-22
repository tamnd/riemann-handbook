---
id: theorem-n5-from-inputs
title: The congruence length bound from the local inputs
kind: theorem
decl: Formalism.MainNotions.N.K.Closed.theorem_n5_from_inputs
module: Formalism.AdmissibleDesigns.StatementOneBFromUnramified
covers: 1791
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `GlobalLatticeIndexTheorem` on the congruence length $v_{cc}(\pi)$ from the local hypotheses on the families $r_x$ and $\rho_x$. Its only caller is [the Selmer bound at a point](/entry/selmer-bound-at-point-main/), which supplies the two instances that it needs and puts one hypothesis in the form `UnrIn`. The theorem proves three inputs itself and passes the rest to `theorem_n5_of_open_b`.

## Statement

The notation is that of [the Selmer bound at a point](/entry/selmer-bound-at-point-main/): a datum $D$, a local index $i$, families $r_x$ of rank $n_V$ and $\rho_x$ of rank $r$ over $\mathcal{O}$ for $x \in X$, a point $\pi \in X$, a partition $(\mathrm{row}, \mathrm{col})$ of the places above $\ell$, and functions $\mathrm{len}_{\mathrm{row}}$, $e'$ and a constant $c_B$.

Assume the instances `T2.Core` (facts of class field theory and Galois cohomology) and `FinCore` (finiteness of local invariants). These are section variables of the file. Assume the hypotheses `admG1` to `admG6`, `TameGeneratorConditions`, `admBK`, `BlochKatoAnnihilators`, `FamilyContinuous`, `SemisimpleDecomposition`, `FontaineAtPlacesOverL`, `tateH1FinitenessAtPlacesOver`, `LocalCoefficientCompatibility` and `adm51`, as in the parent entry. Assume also `UnrIn`: at each column place $w$, the unramified 1-cocycles of the local Galois group with trivial coefficients lie in the submodule `finiteCocycles`, which we have not unfolded.

**Theorem.** Under these hypotheses, `LengthBoundAtPlaces`, `LiftExponentAtPlaces` and `admTB` imply `GlobalLatticeIndexTheorem`, the bound on $v_{cc}(\pi)$ stated in the parent entry.

## Proof

The proof applies `theorem_n5_of_open_b`. That theorem takes the hypotheses above, except `admG4`, `admG5` and `LocalCoefficientCompatibility`, and two more inputs.

1. **Self-good places.** `selfGood_rec` reads `K.SelfGood i` from the field `self_good` of the datum $D$.
2. **The last layer.** `RemainingInputsLastLayer` asks for five statements (`RhoOpenA`, `TBOpen`, `ChiOpen`, `FirstLocalConditionOpen`, `RowTieIn`) for the normalized family $r^{\mathrm{N}}$ (`Norm.rN`) and each ring datum `Dd` with `RingDef`. The proof first builds an `IsScalarTower` instance on the block representations from four equations of `RingDef`,. Then `open_inputs_at_normalized` proves the five statements. It moves `admG2`, `admG4` and `admG5` to $r^{\mathrm{N}}$ with the help of `SemisimpleDecomposition`, and calls `StB.hRho_rN`, `StC.tb_of_target`, `StC.chi_of`, `StC.first_local_clause_of` and `KRowA.rowTieIn_of`.
3. **Powers of a tame generator.** `open_inputs_at_normalized` also needs `QS.QPow i`: for each $v \in Q$ and each $g$ in the inertia group at $v$, $\chi_1(g) = \chi_1(\gamma_v)^n$ for some $n$. This is `qpow_of_tw wildTriv_holds`. The theorem `wildTriv_holds` says: let $v$ be a place of $E$ not above $\ell$, let $\varphi$ be a homomorphism from $G_E$ with open kernel whose values have $\ell$-power order, and let $\sigma$ be in the wild inertia group at $v$ (that is, $\sigma(y)/y - 1$ has positive valuation for each $y \neq 0$). Then $\varphi(\sigma) = 1$. The proof: by `wildProP`, $\sigma^{p^k} \in \ker \varphi$ for the residue characteristic $p$ of $v$, so the order of $\varphi(\sigma)$ divides both $p^k$ and a power of $\ell \neq p$. This is the fact that wild inertia is a pro-$p$ group (Serre, *Local Fields*, Ch. IV, §2, for finite extensions).

## In the Lean code

The theorem is in [StatementOneBFromUnramified.lean](lean:Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean#L142), with `open_inputs_at_normalized` at line 74, `wildTriv_holds` at line 99 and the `IsScalarTower` construction at line 152. `theorem_n5_of_open_b` and `RemainingInputsLastLayer` are in [StatementOneBChangedOfOpen.lean](lean:Formalism/AdmissibleDesigns/StatementOneBChangedOfOpen.lean#L351).

Odd points:

- In the last layer, the proof drops three of the hypotheses that `RemainingInputsLastLayer` gives: `LengthBoundAtPlaces` and `LiftExponentAtPlaces` for $r^{\mathrm{N}}$, and $\pi \in Z$. Only `admTB` for $r^{\mathrm{N}}$ is used.
- `SelfGood` is not proved. It is a field of the structure `D7` ([RhoDetPrimeEqMuTildeMulChiPow.lean](lean:Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L266)), so each datum carries it as an assumption.
- The name "n5" does not say what the bound is. The file name speaks of "statement one B".
