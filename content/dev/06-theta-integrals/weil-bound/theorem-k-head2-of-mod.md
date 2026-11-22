---
id: theorem-k-head2-of-mod
title: Theta integrals agree and local matching, given a modulus identity at inert places
kind: theorem
decl: PositivityTheory.ThKR.theoremK_head2_of_mod
module: Development.WeilBound.ThetaLifts.Reductions.FiniteClosure.TheoremKOfMod
covers: 6655
status: drafted
drafted_by: writer@claude
---
This theorem gives `ThetaIntegralsAgree` and `LocalMatching` from three inputs: an identity `ModSt` on indices of compact open subgroups at inert places, the Eisenstein continuation `EisBL`, and the Siegel-Weil formula `SiegelWeilStd`. It fills eleven of the fourteen hypotheses of [the assembly `closeSph`](/entry/close-sph/) with theorems of the code. Its user is [`theoremK_head2`](/entry/theorem-k-head2/), which proves `ModSt`. Below this theorem are 6,655 declarations.

## Statement

Let $v$ be a finite place of $F$ that is inert in $E$. Let $W$ be a skew-hermitian space of dimension $d = 2m$ with its lattice $L_v$ at $v$. Let $Y$ be a Lagrangian at $v$ (the span of $m$ free isotropic columns), adapted to $L_v$: there is a second Lagrangian $X$ with $L_v = (L_v \cap Y) + (L_v \cap X)$. Let $P$ be the stabilizer of $Y$ in $U_W(F_v)$, let $K$ be the stabilizer of $L_v$, and put $K_P = P \cap K$. For $p \in P$, write $pY = Y$ with the matrix $t$, and let $u = N_{E_v/F_v}(\det t)$. Then `ModSt` says

$$[K_P : K_P \cap p^{-1} K_P p] = |u|_v^{\,m} \, [K_P : K_P \cap p K_P p^{-1}],$$

where $|u|_v$ is the factor by which multiplication by $u$ scales a [[Haar measure|CE0V9686M8]] of $F_v$ (Mathlib's `distribHaarChar`).

**Theorem.** If `ModSt`, `EisBL` and `SiegelWeilStd` hold, then `ThetaIntegralsAgree` and `LocalMatching` hold.

The other three statements are described in [the entry above](/entry/theorem-k-head2/).

## Proof

Apply [`closeSph`](/entry/close-sph/). Its fourteen hypotheses are filled as follows.

1. **Finite places, by type.** `Close.finRam` and `Close.finSplit` give the local quotient maps at the places of the ramification set $T$ and at the split places outside $T$. Both come from one result, `PositivityTheory.Geo.geometricLemmaFiltration`. The same file gives `Close.kCoinv`, `Close.soCoinv` and `Close.ramifiedMultiplicityOne`.
2. **Inert places.** `finInert_of` gives the local quotient maps at the inert places outside $T$, from `vacInert howeInert`, from `locRepEx`, and from `sphFun_of_modSt hM`. This is the only use of `ModSt`. The proof of `sphTri_of sphSplit_geo (vacInert howeInert)` gives `SphTri`: at each place each of the two Weil representations is spherical or irreducible (by the names `SphAt` and `IrrAt`, which we have not unfolded).
3. **Infinite places.** `lieSecond2`, `archLie'` and `kReal'` get `LieSecond`, `ArchLie` and `KReal` from one theorem `localLift_holds`.
4. **Global inputs.** `siegel_of_core siegelCore_holds` gives the reduction theory statement `SiegelSetUnitary`, and `ThKW.weilEx` gives the existence of Weil representations `WeilEx`. The inputs `EisBL` and `SiegelWeilStd` are passed along.

## In the Lean code

The theorem is in [TheoremKOfMod.lean](lean:Development/WeilBound/ThetaLifts/Reductions/FiniteClosure/TheoremKOfMod.lean#L14). The lemmas it calls:

- `Close.kCoinv`, `Close.soCoinv`, `Close.ramifiedMultiplicityOne`, `Close.finRam`, `Close.finSplit` in [RamifiedMultiplicityOne.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/BernsteinNarrowness/BernsteinClosure/RamifiedMultiplicityOne.lean#L9).
- `sphTri_of` and `finInert_of` in [HoweInert.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/HoweInert.lean#L81) and [FinInert.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/FinInert.lean#L219); `sphFun_of_modSt` in [FunTop.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/FunTop.lean#L13).
- `kReal'` in [KReal.lean](lean:Development/WeilBound/ThetaLifts/Reductions/KReal.lean#L6), `lieSecond2`, `archLie'`, `localLift_holds`.
- `siegel_of_core`, `Prw.siegelCore_holds` and `ThKW.weilEx`.

In the Lean code, `ModSt` is stated with `relIndex` of the subgroups `PSub` and `KSub`, for all number fields and all such data at once. The name says "Mod" for the modulus, which matches the statement.

The same file has `thetaIntegralsAgree_and_localMatching_of_siegelWeil` ([L22](lean:Development/WeilBound/ThetaLifts/Reductions/FiniteClosure/TheoremKOfMod.lean#L22)). It is this theorem with one more hypothesis `_P : GlobalTheory.FunPr.Hypotheses₂`, which its proof does not use.

The infinite places use `PositivityTheory.RL.derEx` in `lieSecond2`, while `kReal'` calls `lieSecond2` again with `PositivityTheory.KRealA.i_derex`. Two theorems prove the same statement `DerEx`. This has no effect on the result.
