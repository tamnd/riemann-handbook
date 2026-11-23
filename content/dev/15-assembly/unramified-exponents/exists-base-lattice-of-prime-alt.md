---
id: exists-base-lattice-of-prime-alt
title: Membership and bundles at the origin parameters
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsBaseLatticeOfPrime
covers: 13154
status: drafted
drafted_by: writer@claude
---
This theorem proves the membership statement `MemberE` and the bundle statement `ExBL` for one fixed parameter, the parameter of the origin extension at a constant $c_{\mathrm{Dep}}$. It does this by building the inputs of the general [pair theorem](/entry/exists-base-lattice-of-pair-alt/) for two norm choice extensions, the origin extension and its geometric refinement. It reaches [`member_bundles_large_unramified_exponents_alt`](/entry/member-bundles-large-unramified-exponents-alt/) through the second name [`member_exists_baseLattice_alt`](/entry/member-exists-base-lattice-alt/).

## Statement

The words *parameter*, $p(N)$ and *slot* are as in the [entry above](/entry/member-bundles-large-unramified-exponents-alt/). Let $N_0 = $ `extensionWithOrigin hL cDep` and $p_0 = p(N_0)$.

**Theorem.** Assume:

- `HypAAlt`, a record of 21 propositions named after results on ray class fields, principal ideals, Harish-Chandra modules, rapid decay of cusp forms, Casselman-Wallach, the Weil representation of a unitary pair, existence and uniqueness of discrete series of $U(p,q)$, Siegel-Weil convergence, a Siegel mass ratio, global Artin reciprocity and others;
- `EllipticHypothesis`, a record of 25 propositions named after Chebotarev, Poitou-Tate, local and global Euler characteristics, local Tate duality, Greenberg-Wiles and others;
- `MultiplicityCoverHypotheses`: a discrete series cover, theta condition theorems, a continuation of partial Hecke $L$-functions, and two multiplicity statements `multL`, `multW`;
- `ExistsUnlocalizedSaturatedState`: eventually, at large bases with `KPx`, every column datum $w$ that satisfies `Start` has a datum $P$ with `SatU P` and a state $x$ over $P$ whose type `Loc` is empty and with $\eta_j(v) = 0$ for all $j, v$;
- `hL : RecTExists` and `LocalLanglandsHypothesis hL`, a record of six statements (`pr`, `ser`, `arch`, `par`, `pt`, `parMem`);
- $c_{\mathrm{Dep}} \in \mathbb R$ and `MultiplicityCondition` $p_0$: eventually, at every point of the slots of $p_0$, the multiplicity statement `MultEq` holds.

Then `MemberE` $p_0.s$ and `ExBL KPx (IsBuiltE p₀.s) (IsGoodE p₀.s) (BundleLinkage p₀)`.

We have not unfolded `Pre2`, `St`, `SatU` or `MultEq`.

## Proof

1. `w_of_weight_residue_char` gives `WeightCaseCondition` from three fields of `MultiplicityCoverHypotheses`.
2. `fineAdelicDatum_extends_to_larger_field_of_hypotheses` gives `DatExt` from the discrete series cover and six fields of `HypAAlt`.
3. [`all_stages_at_member_of_specializations_alt`](/entry/all-stages-at-member-of-specializations-alt/) gives ten stage statements. The proof keeps six: a same Galois level statement, `SMt`, a rationality statement, a cusp statement, a nonempty strict henselian acyclic level, and, for each constant, four list statements (settings and forms, series, moduli points, finiteness).
4. `sFino_and_secondNo_of_sFinl'` gives, at $c_{\mathrm{Dep}}$, a spectral finiteness statement and a second nonvanishing statement.
5. `has3_neo_of_localLanglands_alt` combines `ExistsUnlocalizedSaturatedState` with the stage statements and spectral finiteness. It gives `StepW Start (Has3 p₀.s)`: eventually, at large bases with `KPx`, each column datum with `Start` has a level three object `Lv3`.
6. `lv3Mv_extensionWithOrigin_and_NEog` gives `LevelThreeCondition` for $p_0$ and for $p(N_g)$, where $N_g = $ `GeometricNormExtension hL cDep` is $N_0$ with the extra condition `GoodO`.
7. [`exists_baseLattice_of_pair_alt`](/entry/exists-base-lattice-of-pair-alt/) with $N = N_0$ and $N_g$ gives the conclusion. The two maps it needs are projections of the product types. `PositionMv` comes from `slot_mv_extension_with_origin_geo_cl`, and the pass hypothesis is the second nonvanishing statement of step 4.

## In the Lean code

The theorem is at [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L57). The lemmas it calls are the seven of the proof above, and `slot_mv_extension_with_origin_geo_cl`.

Odd points:

- Step 3 is written as `repeat (first | specialize h hA.a8 | specialize h hA.a9 | … | specialize h hN.pt)`: the hypotheses of `all_stages_at_member_of_specializations_alt` are found by trial, not named. Its first two arguments are given as `by first | exact hA.a5 | exact hA.a7` twice, so the tactic picks Harish-Chandra modules or Casselman-Wallach by type.
- Four of the ten parts of step 3 are dropped (`-`): the three intermediate levels and `FinitenessStatement`.
- The field `par` of `LocalLanglandsHypothesis` is not used here, nor in the pair theorem.
- `MultiplicityCondition` $p_0$ is a hypothesis. Its only caller gets it from `member_multiplicatively_closed_alt`, a theorem that proves it from ten literature hypotheses for every parameter $p(N)$, with any $N$.
- The names "base lattice" and "of prime" do not match an object or a prime in the statement.
