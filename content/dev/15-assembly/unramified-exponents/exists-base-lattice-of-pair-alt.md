---
id: exists-base-lattice-of-pair-alt
title: Membership and bundles from a pair of norm choice extensions
kind: theorem
decl: GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsBaseLatticeOfPrime
covers: 7446
status: drafted
drafted_by: writer@claude
---
This theorem proves `MemberE` and `ExBL` for the parameter of a norm choice extension $N$, given a second extension $N_g$ that refines $N$ and a list of step conditions for both. It is the last step of [`exists_baseLattice_of_prime_alt`](/entry/exists-base-lattice-of-prime-alt/), which applies it to the origin extension and its geometric refinement. The theorem joins three results: an export statement, the [closing theorem for `MemberE`](/entry/member-e-closing-alt-alt/), and a bundle statement.

## Statement

The words *parameter*, $p(N)$, *slot*, `MemberE` and `ExBL` are as in the [entry above](/entry/member-bundles-large-unramified-exponents-alt/). Let `hL : RecTExists`, and let $N$ and $N_g$ be norm choice extensions for `hL`. Write $s = p(N).s$ and $s_g = p(N_g).s$. Assume:

- the hypothesis records `HypAAlt`, `EllipticHypothesis`, `MultiplicityCoverHypotheses` and `LocalLanglandsHypothesis hL` (see the [entry above](/entry/exists-base-lattice-of-prime-alt/));
- (`toB`) each datum of $N$ gives a datum of `extensionWithLaw hL`;
- (`toN`) each datum of $N_g$ gives a datum of $N$, and the condition `GoodO` holds at it;
- (`has3`) `StepW Start (Has3 s)`: eventually, at large bases with `KPx`, each column datum with `Start` has a level three object for $s$;
- (`lv`, `lvg`) `LevelThreeCondition` for $s$ and for $s_g$;
- `PositionMv` $s$;
- (`second`) the pass condition `Pass KPx (IsBuiltE s) r`, where $r$ says that the base has a column datum with `Start` and a level three object for $s_g$;
- (`hMQ`) `MultiplicityCondition` $p(N)$.

Then `MemberE` $s$ and `ExBL KPx (IsBuiltE s) (IsGoodE s) (BundleLinkage p(N))` hold.

We have not unfolded `extensionWithLaw`, `GoodO`, `Lv3`, `LevelThreeCondition` or `PositionMv`.

## Proof

1. [`automorphy_of_hypotheses_alt_alt`](/entry/automorphy-of-hypotheses-alt-alt/) gives `ExportF KPx (IsBuiltE s)`: eventually, at large untwisted bases with `KPx`, every built core exports (`ExportAt`). It uses all 25 fields of `EllipticHypothesis`, rapid decay of cusp forms and global Artin reciprocity from `HypAAlt`, the fields `pr`, `ser` and `parMem` of `LocalLanglandsHypothesis`, and `toB`.
2. [`memberE_closing_alt_alt`](/entry/member-e-closing-alt-alt/) gives `MemberE` $s$. It uses eighteen fields of `HypAAlt` (one of them twice), `hL`, the export statement of step 1, and `has3`, `lv`, `lvg`, `second`, `toN`.
3. `geometric_parameter_uniform_alt` gives the `ExBL` statement. It uses the field `cover` and the part `q12` of the field `h1` of `MultiplicityCoverHypotheses`, nine fields of `HypAAlt`, `toB`, `PositionMv` $s$ and `hMQ`. The type of `hMQ` unfolds to the multiplicity hypothesis that this lemma asks for.

The rest is bookkeeping.

## In the Lean code

The theorem is at [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L36). It calls:

- `GlobalTheory.T.automorphy_of_hypotheses_alt_alt`,
- `GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt`,
- `GlobalTheory.T.geometric_parameter_uniform_alt`.

Odd points:

- The hypothesis of type `PositionMv` $s$ has the local name `intersection_update_fsHerm_neg_one`. The name has no relation to its type.
- In step 2 the field `a6` (rapid decay of cusp forms) is passed twice, because `memberE_closing_alt_alt` takes `CuspRapidDecay` as two separate hypotheses.
- The `ExBL` half of the conclusion is not used by the only chain of callers. [`member_bundles_large_unramified_exponents_alt`](/entry/member-bundles-large-unramified-exponents-alt/) keeps only the `MemberE` half and proves its own `ExBL` with another lemma.
- The names "base lattice" and "of pair" do not match an object in the statement.
