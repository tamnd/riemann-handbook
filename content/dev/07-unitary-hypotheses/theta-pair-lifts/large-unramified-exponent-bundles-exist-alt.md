---
id: large-unramified-exponent-bundles-exist-alt
title: Membership and bundles at the stronger parameters (a second name)
kind: theorem
decl: GlobalTheory.T.large_unramified_exponent_bundles_exist_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MemberBundlesLargeUnramifiedExponents
covers: 19960
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the membership and bundle theorem](/entry/member-bundles-large-unramified-exponents-alt/). It has the same statement and its proof only calls that theorem. Its one caller is [`hypotheses_nonempty_of_unramified_exponents_alt`](/entry/hypotheses-nonempty-of-unramified-exponents-alt/), the first branch of the [unitary hypotheses node](/proof/unitary-hypotheses/). That caller uses it as step 1 of its proof. The real content is in the entry [member-bundles-large-unramified-exponents-alt](/entry/member-bundles-large-unramified-exponents-alt/).

## Statement

Assume the record of literature hypotheses `UnitaryGroupThirdPlaceHypotheses` and the row statement `RowRat`. Let `hL` be a proof of `RecTExists`, let $c_{\mathrm{Dep}}$ be a real number, and let $A$ be a property of bases that holds eventually for large bases (`EvLgG A`). Then three things hold: the Siegel mass ratio for CM fields (`SiegelMassRatioCM`), the membership statement `MemberE` for the parameters of the extension `extensionWithAtProperty hL (extensionWithOrigin hL cDep) A`, and the existence statement `ExBL` of bundles for the same parameters. The [entry of the theorem it renames](/entry/member-bundles-large-unramified-exponents-alt/) says what each part means.

## Proof

The proof is the other theorem. The rest is bookkeeping.

## In the Lean code

The theorem is in [MemberBundlesLargeUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L69), in the same file as `GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt` (line 34). The two statements are the same text. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with the other theorem in each branch. The index lists that theorem as its only direct use outside the statement. So the two subtrees differ by almost nothing: 19,960 declarations here and 19,958 there.

The name speaks of "large unramified exponents". No object with that name occurs in the statement. The word "large" may refer to the hypothesis `EvLgG A`, which asks that $A$ holds for large bases, but the code does not say so.
