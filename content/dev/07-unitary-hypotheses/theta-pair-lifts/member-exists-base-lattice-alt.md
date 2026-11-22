---
id: member-exists-base-lattice-alt
title: Membership and bundles at the origin parameters (a second name)
kind: theorem
decl: GlobalTheory.T.member_exists_baseLattice_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsBaseLatticeOfPrime
covers: 13155
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_baseLattice_of_prime_alt`](/entry/exists-base-lattice-of-prime-alt/). It has the same statement and its proof only calls that theorem. Its one caller is [`member_bundles_large_unramified_exponents_alt`](/entry/member-bundles-large-unramified-exponents-alt/), which uses only the first half of its conclusion. The real content is in the entry [exists-base-lattice-of-prime-alt](/entry/exists-base-lattice-of-prime-alt/).

## Statement

Let $p_0$ be the parameter `parametersOfExtension (extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)`. Assume the hypothesis records `HypAAlt`, `EllipticHypothesis` and `MultiplicityCoverHypotheses`, and the statement `ExistsUnlocalizedSaturatedState`. Let `hL : RecTExists`, assume `LocalLanglandsHypothesis hL`, and let $c_{\mathrm{Dep}} \in \mathbb R$. If `MultiplicityCondition` $p_0$ holds, then `MemberE` $p_0.s$ holds and `ExBL KPx (IsBuiltE p₀.s) (IsGoodE p₀.s) (BundleLinkage p₀)` holds. The entry of [`exists_baseLattice_of_prime_alt`](/entry/exists-base-lattice-of-prime-alt/) says what these mean.

## Proof

The proof is the other theorem. The rest is bookkeeping.

## In the Lean code

The theorem is at [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L80), in the same file as `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt` (line 57). The two statements are the same text. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with the other theorem in each branch.

The name speaks of a "base lattice". No lattice is named in the statement: the conclusion is about built points, good points and bundles, through `MemberE` and `ExBL`. We have not unfolded `BundleLinkage`, so we do not say what the name refers to.
