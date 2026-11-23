---
id: exists-good-cut-facts-tie4
title: A good cut with the norm choice facts and the four ties
kind: theorem
decl: UpperTheory.GalC.exists_good_cut_facts_tie4
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CFacts
covers: 371
status: drafted
drafted_by: writer@claude
---
This theorem proves the cut hypothesis `CutGivesAlt` for one datum. [The closed link bound](/entry/final-alt-alt/) gives it to [its main lemma](/entry/final-of-alt/), and from there it reaches [the bound LinkN for one family](/entry/link-n-of-tw-good-galois-preconditions/). This is step 4 of branch 1 in the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 371 declarations.

## Statement

A *cut* $c$ of a datum $D$ (`CutD`) keeps some local indices $i$ and, at each kept index, a nonempty set $X_i$ of points. It is *good* if $i$ is kept exactly when the set $Z^{\mathrm{good}}_i$ of good points is nonempty, $Z^{\mathrm{good}}_i \subseteq X_i$, the points of $Z_i \cap X_i$ are good, a Hecke-equivariant endomorphism acts on eigenvectors by a fixed nonzero integer at good points and by $0$ outside $X_i$, and the local parameters at the kept points satisfy a condition `Nc` at the places above $g_0$ and $g_1$. The cut datum is `cut D c`, and a norm choice $x$ of $D$ gives the norm choice `nchCut c x` of the cut datum.

**Theorem.** Assume the Chebotarev input `TwSys.Cheb` and the three local Galois cohomology inputs `LocalFiniteness`, `LocalTateDuality` and `LocalEulerChar`. Let $D$ be a datum and $x$ a norm choice with `GaloisPreconditions D x` and `Tie4 D`. Then there is a good cut $c$ such that the cut datum satisfies `NormChoiceFacts` with `nchCut c x`, and `Tie4`.

`GaloisPreconditions` is a record of 18 named conditions. `NormChoiceFacts` has 21 fields: 17 of these, and four new ones, one of which contains the 18th (see [the next entry](/entry/facts-of-galois-preconditions-of-cut-rec/)). `Tie4` is the conjunction of four conditions; the first two are in [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/). We have not unfolded `Nc` or the inputs.

## Proof

1. `exists_good_alt` gives a good cut $c$ from `GaloisPreconditions` and `Tie4`. Its other input `CentralElt` comes from `central_elements_from_idempotent_coeffs` applied to `centralIdemCoeff`.
2. `pre_cut_alt` moves `GaloisPreconditions` to the cut datum.
3. `cutRec_cut`: the cut datum satisfies `CutRec`, that is, `Nc` at every point. This is the last field of a good cut.
4. [`facts_of_galois_preconditions_of_cutRec`](/entry/facts-of-galois-preconditions-of-cut-rec/) turns steps 2 and 3 into `NormChoiceFacts` of the cut datum. All four inputs are used here.
5. `compatibilityTies_eigenRestriction` moves `Tie4` to the cut datum.

## In the Lean code

The theorem is in [CFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFacts.lean#L58), with `pre_cut_alt` at line 23 and `facts_of_galois_preconditions_of_cutRec` at line 45. `CutD`, `Good`, `CutRec` and `Tie4` are in [RhoBar.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/RhoBar.lean#L12). `exists_good_alt` is in the module `ExistsGood`, and `cutRec_cut` in [Tie0CutOfTie0.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/Tie0CutOfTie0.lean#L164).

`CutGivesAlt` in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L35) writes the cut norm choice as `nchTr c nch`. [The caller](/entry/final-alt-alt/) passes this theorem for it, so Lean accepts the two forms as equal.
