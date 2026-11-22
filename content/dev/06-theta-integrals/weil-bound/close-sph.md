---
id: close-sph
title: The assembly of the two theta statements from fourteen inputs
kind: theorem
decl: PositivityTheory.Sph.Tr.closeSph
module: Development.WeilBound.ThetaLifts.SphericalLattices.SphericalClosure.CloseSph
covers: 4632
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThetaIntegralsAgree` and `LocalMatching` from fourteen named inputs. It puts together the proofs of the two theta statements of the [theta matching chapter](/proof/theta-matching/). Its user is [`theoremK_head2_of_mod`](/entry/theorem-k-head2-of-mod/), which fills eleven inputs with theorems and passes the Siegel-Weil formula and the Eisenstein continuation along. Below this theorem are 4,632 declarations.

## Statement

**Theorem.** Suppose that the fourteen statements below hold. Then [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/) hold.

The inputs are about the triples of the theta chapter: two [[Weil representations|H3Q2703KKV]] $\omega$ of $U_V \times U_W$ and $\omega'$ of $U_{V'} \times U_W$ over a CM extension $E/F$, with characters and a finite set $T$ of places. We group them by purpose.

- **Finite places.** `FinRam`, `FinSplit` and `FinInert` say: for each triple and each finite place $v$ in $T$, split outside $T$, or inert outside $T$ (in that order), there are local maps $p_v, p'_v$ from the local Schwartz spaces of $\omega_v, \omega'_v$ onto one irreducible nontrivial space $\Pi_v$. They kill the coinvariants, respect the action of $U_W(F_v)$, match the two vacuum vectors outside $T$ and satisfy a zeta condition at $T$ (the structure `IsFinAt`). `SphTri` says that at each place each of $\omega, \omega'$ is spherical or irreducible, by the names `SphAt` and `IrrAt`. `RamifiedMultiplicityOne` says that at $v \in T$ two local equivariant maps of a given type between the quotients of a triple and a smaller triple are proportional when the first is not zero.
- **Coinvariants.** The input `hKCo` says that a dictionary statement `DictSt` implies `KCoinv`. We have not unfolded `DictSt`, an identification of the local Weil representations with explicit models. `KCoinv` says that at the good places the kernels of matched local maps are the coinvariant spaces. The input `hSo` says that `KFin` (local maps exist at all finite places) implies `SoCoinv`, a statement on coinvariants inside a subspace at one place $v_1$.
- **Infinite places.** `KReal` says that matched maps exist at the infinite places. `ArchLie` says that on the polynomial Fock space the operators of $\omega$ along one-parameter subgroups are differentiable at $0$, with derivative in that space. `LieSecond` says that the Weil representation acts on the Fock model through `fockAct2`; we have not unfolded `ActsBy`.
- **Global inputs.** `SiegelSetUnitary` is reduction theory for $U_J(\mathbb{A})$: an Iwasawa decomposition $g = pak$, and a closed Siegel set whose rational translates cover $U_J(\mathbb{A})$. `WeilEx` says that Weil representations exist for each good model and each suitable pair of Hecke characters. `EisBL` and `SiegelWeilStd` are as in [`theoremK_head2`](/entry/theorem-k-head2/).

## Proof

The proof is about 150 `have` lines, each one lemma applied to earlier lines. The last step is `agree_of_leaves`, which needs `KDecay`, `KCoinv` and a structure `Leaves` with 26 fields. Then `agree_of_parts` gives `ThetaIntegralsAgree` from `KDecay`, `KCoinv` and three facts of `Leaves`: `kConst` (one nonzero constant), `kBeta` and `kAlpha` (the two recursion laws). And `matching_of_parts` gives `LocalMatching` from `KReal` and `KFin`.

So `LocalMatching` uses only the local inputs: `KFin` is `kFin_of` applied to `FinRam`, `FinSplit` and `FinInert`, which split the finite places by type. The global inputs go into `ThetaIntegralsAgree`. The main steps that use them:

1. `ThKEst.kDecay` gets `KDecay` (convergence of the theta integrals) from `SiegelSetUnitary` and `ThetaBasic`.
2. `nonZeroBottom_of_doubling_integral` and `nonZeroAn_of` give `NonZeroAn`, a nonvanishing statement, from the doubling integral, the towers `TowerA` and `TowerB` (from `WeilEx`), and constant terms.
3. `polynomial_vanishing_of_compactness` gives `PolZero` from `SiegelWeilStd`, `EisBL`, `HeckeLEntireAndNonzeroAtOne_holds`, `NonZeroAn` and `Factor`. `Factor` comes from `theta_kills_cusp_forms_spherical`, which uses `SphTri`, `ArchLie` and `SoCoinv`.
4. `locA_of` and `locB_of` give the local facts `LocA'` and `LocB'`. They use the multiplicity one statements at unramified, ramified (`RamifiedMultiplicityOne`) and infinite places.
5. `endAB_sph` gives `EndA` and `EndB` from `SiegelSetUnitary`, `WeilEx`, `hKCo`, the three finite inputs, `LieSecond`, `ArchLie`, `SiegelWeilStd` and `EisBL`.

The rest is bookkeeping. We have not unfolded the statements of most of the 26 fields.

## In the Lean code

The theorem is in [CloseSph.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/CloseSph.lean#L28). The final step `agree_of_leaves` is in [AgreeOfLeaves.lean](lean:Development/WeilBound/ThetaLifts/AgreeOfLeaves.lean#L7). The structure `Leaves` and the proofs of `kConst`, `kBeta`, `kAlpha` are in [CtSmallCone.lean](lean:Development/WeilBound/ThetaLifts/ConeHypotheses/CtSmallCone.lean#L12). `agree_of_parts` and `matching_of_parts` are in [MatchingOfParts.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/MatchingOfParts.lean#L36). `FinRam`, `FinSplit`, `FinInert` and `kFin_of` are in [FinSplit.lean](lean:Development/WeilBound/CoreStatements/CompactAveragingSplitting/EigenvectorLifting/FinSplit.lean#L31).

Odd points:

- The matching part of the conclusion is almost a restatement of the four hypotheses `KReal`, `FinRam`, `FinSplit` and `FinInert`.
- The hypotheses `hKCo` and `hSo` are implications whose premises the proof builds itself: `DictSt` at [L52](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/CloseSph.lean#L52) and `KFin` at [L132](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/CloseSph.lean#L132).
- Lines 129 to 131 only rename three hypotheses. The same term `endAB_sph ...` is built twice (L188 and L190), and so are `ct_all` (L75 and L84) and `coneFac_all` (L182 and L185), once for each component.
