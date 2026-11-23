---
id: type-primes-finished-loc-comp-of-is-rc-class-map-d-cen-loc
title: Four tie conditions at each layer point, from three lemmas
kind: theorem
decl: GlobalTheory.TypePrimesFinished.locComp_of_isRc_classMapD_cenLoc
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LocalTypeDeterminedAtAllPrimes
covers: 589
status: drafted
drafted_by: writer@claude
---
This theorem shows that at each layer point the datum $D$ satisfies four conditions at the type primes. The proof joins three lemmas. Its second name is [`tieChi_at_members_of_depthZero`](/entry/tie-chi-at-members-of-depth-zero/), which [`final_of_alt`](/entry/final-of-alt/) calls. It is part of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume three inputs:

- `HtCard`: a continuity condition on the representations of the Weil-Deligne sides;
- `PublishedInputsThirdLayerAlt`: a record of fourteen published inputs;
- `DepthZeroSupport`: if an irreducible representation $\pi$ of $\mathrm{GL}_n(k)$, for a local field $k$, has a nonzero vector fixed by $K_1 = \ker(\mathrm{GL}_n(O) \to \mathrm{GL}_n(\text{residue field}))$, then so does each member of its cuspidal support.

Then for each `hL : RecTExists`, at each layer point (`MemberAtLayerPoint hL`), the datum $D = $ `w.D Z` satisfies:

1. `tieChi D`: at each type prime $\ell_i = g_k$ and each $v$, there is $u = \chi_J$ or $u = \chi_J^{-1}$ such that the character `chiGL i` is de Rham at $w = $ `plGw k v` and at its conjugate place, with item polynomial $X - u$ at $w$ and $X - u^{-1}$ at the conjugate;
2. a pending datum $Q$ with `admDZ Q` and `EigSpan Q`. `EigSpan Q` says: if a central element $z$ acts by a scalar $c$ on the types at $x$, then $z$ acts by $c$ on the Hecke eigenvectors at $x$;
3. `TieInePoly D`: for potentially crystalline local representations, the inertia polynomial of the Weil-Deligne representation kills $D_{\mathrm{pcris}}$;
4. `SerLoc D`: if `atPlace (eSer k f)` acts by a nonzero map on $F$ in `MtPar σ'`, then $f$ is the label `labPar k σ' v`.

We have not unfolded `admDZ`, `items₂` or `chiJ`.

## Proof

At each member the proof combines, with `at_member_imp` and `and_z`:

1. [`tieChi_at_mem_of_depth_zero_inputs`](/entry/tie-chi-at-mem-of-depth-zero-inputs/), from all three inputs, for parts 1 and 2;
2. `exists_character_choice_pin_at_of_third_layer`, from the published inputs. It gives a character choice $P$ and a pin. The pin is not used;
3. `serLoc_at_member_of_published_inputs`, from the published inputs, for part 4.

Part 3 is `tieInePoly_of_characterChoice hL D P`. Only the existence of $P$ is used.

## In the Lean code

The theorem is at [LocalTypeDeterminedAtAllPrimes.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalTypeDeterminedAtAllPrimes.lean#L22). The first lemma is at [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L62); its main step is [`PendLayer.locComp_of_isRc_classMapD_cenLoc`](/entry/pend-layer-loc-comp-of-is-rc-class-map-d-cen-loc/). `tieChi` is at [PairedCharacterCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/PairedCharacterCondition.lean#L330), and `DepthZeroSupport` at [DepthZeroSupport.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/DepthZeroSupport.lean#L12).

`HtCard` and `DepthZeroSupport` go only to the first lemma. `DepthZeroSupport` has the form of a depth-zero result on cuspidal support (Moy and Prasad, Comment. Math. Helv. 71, 1996). We have not checked that the form with $K_1$ is their statement. The name `locComp_of_isRc_classMapD_cenLoc` does not describe this statement, and other theorems in other namespaces have the same name.
