---
id: pointwise-alt-alt
title: First level data at one stage, from a grid
kind: theorem
decl: GlobalTheory.HeightCounting.Up.PointwiseSettings.pointwise_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ReductionSeriesB0
covers: 764
status: drafted
drafted_by: writer@claude
---
This theorem does the work of [first level data from the published inputs](/entry/settings-forms-exist-list-of-published-inputs/) at one stage. From an intermediate level datum and a grid, it builds twist rings, twist data and the side record `SideB`, and then a new stage with a first level datum and the list condition. The main input is [the second step](/entry/second-step-alt/), reached through [its relay](/entry/row-cusp-multiplicity-input-alt/).

## Statement

Let $x$ be a stage, and let $D$ be the datum `Dof x` of type `D7` that $x$ carries, with host field $E$ and coefficient field $L_0$. Let $l$ be an intermediate level datum over $x$. Let $G$ be a grid datum for the level characters of $x$ at the parameters $(1, c, b)$, with `FieldHas G`, and suppose that $\lambda(G)$ satisfies `Ok`, has the character frame of $x$, and has the value `q0` of $D$. The words are those of [first level data from the published inputs](/entry/settings-forms-exist-list-of-published-inputs/).

**Theorem.** Assume `PublishedInputsThirdLayerAlt` ($P$), `SerN` ($S$) and $h_L \in$ `RecTExists`. Then there is a stage $x'$ of the same datum as $x$ with a first level datum and with `ListSt c x'`.

## Proof

1. **Galois representations.** `galEx_of_cgTrue_alt` gives `GalEx D` (an $\ell$-adic representation for each $\pi$ of the right type; see [the second step](/entry/second-step-alt/)) from the fields `fin` and `gal` of $P$ and the datum `cg` of $l$. `chebSplit_nd` gives `ChebSplit` from the field `cheb` of $P$.
2. **Two bounds on local fields.** [The second step](/entry/second-step-alt/), called as `row_cusp_multiplicity_input_alt`, gives a choice $c_f$ of a finite extension of $\mathbb{Q}_\ell$ for each $\ell$ and each embedding of $L_0$. `exists_twistRings_characters_classGroups` gives a second choice $c_r$. Let $b_0 = c_f \sqcup c_r$, the pointwise join.
3. **The exceptional set.** `exists_Sx` gives a finite set $S_x$ of places of $E$ that contains all places over the primes of `lowAll D`, lies over these primes, and is closed under conjugation.
4. **Twist rings.** `exists_twistRings_characters_classGroups` at $(b_0, b_0, S_x)$ gives twist rings $T'$ and a ring specification `Sp`. Its field `ringSpec_excludedPlaces_eq` writes each excluded set $S_0(i)$ as a union of five sets, one of which is $S_x$. So $S_x \subseteq S_0(i)$.
5. **Twist data.** The second step at $(b_0, b_0, S_x, T', \mathrm{Sp})$ gives twist data $F$, a datum `ex` with finitely generated spanning lattices, and `SideB` for the empty toric list.
6. **Toric characters.** `exists_cyclotomic_integers` and `exists_iC_of_clC` give a map `iC` on each cyclotomic closure. `exists_toricCharacters_in_twistCoefficientRings` (from `cheb`, `art` and the field `ratio` of $S$) gives a list $L$ such that the twist datum with $L$ is fully tied to $\lambda(G)$ and `SideB` passes from the empty list to $L$. `conductor_primes_in_low_set` checks its hypothesis on conductor primes.
7. **Assembly.** `exists_nth_of_fg_full` builds the remaining data `th0` and `th1`, and step 6 gives `SideB` with $L$. Then `side_data_over_set_levels_alt` gives $x'$. Its last hypothesis, that each $S_0(i)$ lies over $\{\ell_i\} \cup$ `lowAll D`, comes from the five-set description by a case split.

## In the Lean code

The theorem is in [ReductionSeriesB0.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReductionSeriesB0.lean#L26). `side_data_over_set_levels_alt` is in [RestageStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RestageStatement.lean#L14), a relay for `restage_alt`. We have read the statements of the lemmas above, not their proofs. Both twist ring calls use $b_0$ for the two bounds `b0` and `b1`. Of $S$, only the field `ratio` is used; of $P$, only four fields of `what₂`. The name says nothing about the statement. The file [ReductionSeriesB0.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ReductionSeriesB0.lean#L45) in another folder has an older twin, `pointwise`, with the record `PrN` and `LocalLanglandsGL` in place of $P$ and $h_L$.
