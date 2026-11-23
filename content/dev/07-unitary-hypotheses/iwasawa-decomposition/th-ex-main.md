---
id: th-ex-main
title: Theta data for every level 4 object
kind: theorem
decl: GlobalTheory.ThetaRecordTrue.thEx_main
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsThetaDataTrueRowsColumnsAllCompatible
covers: 807
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThEx` for a slot. It is the proof of [`exists_thetaData_trueRowsColumns_allCompatible`](/entry/exists-theta-data-true-rows-columns-all-compatible/), which the [membership theorem](/entry/member-e-closing-alt-alt/) calls.

## Statement

The hypotheses are those of the [renamed form](/entry/exists-theta-data-true-rows-columns-all-compatible/): seven published results and the vanishing of $\mathrm{io}_{\mu,j}$ for unused tuples $\mu$ at rows objects of the slot.

A *theta datum* `ThetaX D` is an abstract model of automorphic forms on the unitary groups $U(V)$ of $D$: spaces with cuspidal subspaces and Petersson forms, actions at the places, characters, Schwartz spaces, theta lifts and Bessel periods. For a level 4 object $l$, the certificate `ThT l.n X` asks for:

- a provision $A$ and a record `AllTied D X A`. It ties $X$ to functions on the adelic groups (`ThetaTied`), to a Weil representation (`WeilTied`) and to Bessel periods (`BesselTied`), with further conditions such as $K$-finiteness;
- equivariance of the Weil representation (`WeilCompatibleEquivariance`);
- a character record `ThetaChrTied` for the tuple datum $l.n.\mathrm{tp}$, with the same characters as the theta record (`SameChr`);
- a standard additive character $\psi$ of sign $-1$ (`IsStdChar`);
- the identity `TieIo`: $\langle \mathrm{dn}(\mathrm{row}_{j+1}(y)), \mathrm{row}_j(x) \rangle = \langle \mathrm{io}_{\mu,j}(y), x \rangle$ for all $\mu$ and $j < m$, in the Petersson form of $X$.

**Theorem.** Under the hypotheses, `ThEx 𝒮` holds: at all large bases where `KPx` and the forced primes hold, each pinned column datum $w$ and each level 4 object $l$ at a stage $Z$ have a theta datum $X$ with `ThT l.n X`.

## Proof

Fix $w$, $Z$ and $l$ (`StepW.of_all`). Let $U$ be the set of used tuples.

1. `recFun_of_rows` (line 25) gives for each $\theta$, $\psi$ and Weil function a record of functions with the characters of $l$, the identity `IoTie`, and the Petersson norms of the rows on $U$. The vanishing of $\mathrm{io}$ enters here.
2. [`exists_allTied_eqTied_on`](/entry/exists-all-tied-eq-tied-on/), with the realness field `l.real`, gives $X$ with `TieIo`, a provision $A$, a record $a$ with `WeilThetaCompatibility`, and a character record $H$ that agrees with $a$.
3. `weilTiedEq_of_eqTied` turns `WeilThetaCompatibility` into `WeilCompatibleEquivariance`, and `sameChr_of_chrEq` turns the agreement into `SameChr`. The field `ψ_std` of the Weil record gives the standard character.

## In the Lean code

The theorem is in [ExistsThetaDataTrueRowsColumnsAllCompatible.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsThetaDataTrueRowsColumnsAllCompatible.lean#L46). `ThEx` is in [NonzeroPlacesOverPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L187) and `ThT` in [TiedColumnData.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TiedColumnData.lean#L135).

Odd points:

- The hypotheses `CasselmanWallach` and `HarishChandraModules` are bound to `_` and never used.
- The Petersson identity on $U$ in the output of `exists_allTied_eqTied_on` is dropped; `ThT` does not ask for it.
- We have not unfolded the fields of `ThetaX` beyond the list above, nor `RecFun`.
