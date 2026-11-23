---
id: exists-all-tied-eq-tied-on
title: A theta datum tied to true automorphic forms
kind: theorem
decl: GlobalTheory.Mem.Th.exists_allTied_eqTied_on
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsAllTiedEqTiedOnOfRealised
covers: 526
status: drafted
drafted_by: writer@claude
---
This theorem makes, for one datum $D$, a theta datum $X$ tied to automorphic forms, a Weil representation and Bessel periods. [`thEx_main`](/entry/th-ex-main/) calls it once for each level 4 object.

## Statement

Assume five published results: the Weil representation of a unitary pair, rapid decay of cusp forms, existence and uniqueness of discrete series of $U(p,q)$ with a given Harish-Chandra parameter, and existence of a discrete series datum `DSRep` with a given parameter.

Let $D$ be a datum, $C$ a character frame, $\xi$ a map from tuples to Hecke characters of $E$, and $U$ a set of tuples. Assume `RealTied D`. Assume also: for each infinity type $\theta$ (`IsInfFam`), each standard additive character $\psi$ of sign $-1$ and each Weil function $W_f$ for $\psi$, there is a record of functions $R$ (`RecFun`) with the characters $\xi$ (`ChrIs`), the identity `IoTie` with $W_f$, and, for $\mu \in U$ and $j \le m$, the identity $m_Y c_{\mathrm{pet}} \int \overline{\mathrm{row}(x)}\,\mathrm{row}(y) = \langle x, y \rangle$ (`IsQuotInt`).

**Theorem.** There is a theta datum $X$ with:

1. `TieIo`;
2. for $\mu \in U$ and $j \le m$, the rows are isometric: $\langle \mathrm{row}(x), \mathrm{row}(y) \rangle_X = \langle x, y \rangle$;
3. a provision $A$ and a record $a$ of type `AllTied D X A` whose Weil part satisfies `WeilThetaCompatibility`;
4. for each choice `nch` and each tuple record $T_p$ with characters $\xi$, a character record `ThetaChrTied` whose characters equal those of $a$.

## Proof

The theorem applies the companion `exists_allTied_eqTied_on_of_realised` (line 28). Its inputs come from:

- `TypAdd D`, from `typAdd_of_discreteSeries` and the existence and uniqueness of discrete series;
- a Weil function of equal rank for each standard $\psi$, from `exists_weilFun_eqRank`, from the Weil representation and `weilTwEq`;
- a tower of Hermitian spaces, from `exists_tow`;
- `RealisedExE D`, from [`exists_realisedE`](/entry/exists-realised-e/). Its five integrability inputs `PetInt`, `TopInt`, `BesInt`, `LiftAut` and `LiftAutEq` all come from rapid decay of cusp forms;
- a provision with `ProvisionCompatibility`, from `exists_realPlace_record_tied` and the `DSRep` statement.

The companion fixes $\theta$ (`exists_isInfFam_family`), the unique standard $\psi$ of sign $-1$ (`existsUnique_isStdChar`), a Weil function, a tower and the record $R$. `RealisedExE` gives $X$, and the fields of `AllTied` come from its ties. The isometry of rows comes from the Petersson field `pet` of the tie and the quotient integral identity of $R$. The character record comes from `exists_thetaChrTied`.

## In the Lean code

The theorem is in [ExistsAllTiedEqTiedOnOfRealised.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsAllTiedEqTiedOnOfRealised.lean#L54). `AllTied` is in [AllTied.lean](lean:Formalism/LocalToGlobal/BesselHermitianTheta/AllTied.lean#L20) and `RealisedExE` in [ExistsSplittingCharacterSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsSplittingCharacterSelf.lean#L185).

All five published hypotheses are used. We have not unfolded `RecFun`, `IsQuotInt` or `ProvisionCompatibility`.
