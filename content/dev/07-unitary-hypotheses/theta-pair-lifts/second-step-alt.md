---
id: second-step-alt
title: Twist data and the side record over twist rings
kind: theorem
decl: GlobalTheory.HeightCounting.FormsStep.second_step_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SecondStep
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem builds, over given twist rings, the twist data and the side record `SideB` of a datum of type `D7`, for every large bound on the local coefficient fields. Through [its relay](/entry/row-cusp-multiplicity-input-alt/) it goes to [the pointwise step](/entry/pointwise-alt-alt/).

## Statement

Let $D$ be a datum of type `D7` with host field $E$, maximal real subfield $F^+$, and coefficient field $L$ with a subfield $L_0$. A *bound* (`Big D`) chooses a finite extension of $\mathbb{Q}_\ell$ for each prime $\ell$ and each embedding $L_0 \to \overline{\mathbb{Q}}_\ell$. *Twist rings* $T$ (`TwR`) give, for each index $i$, a prime $\ell_i$, a discrete valuation ring $O_0(i)$ finite over $\mathbb{Z}_{\ell_i}$ with embeddings of $L_0$ into its fraction field, and an extension $O(i)$. A *ring specification* (`RingSpec`) ties $T$ to two bounds $b_0, b_1$ and a finite set $S_x$ of places of $E$.

Let $c_f$ be a character frame, $A$ a datum `CharFrameHostEmbedding`, $(S, I)$ a rational datum with data `RatIn` (with a finite set $S_b$ of places), $\mathrm{low}$ a finite set of primes, and $P_q$ a place of $E$ over each finite place of $F^+$. Assume:

1. `GlobalArtinReciprocity`;
2. `MtInput D M tup Q`, for data $M$, `tup`, $Q$;
3. $P_q(v)$ lies over $v$ for each $v$;
4. `GalEx D`: each $\pi$ in `CG a` with `csd` and `ralg` has, for each $\ell$ and $\iota$, a continuous semisimple $\rho$ that matches $\pi$ at almost all places;
5. `RowCusp D A.row`: each good row that occurs comes from such a $\pi$, with the local data of $A$ at split places and, at almost all places, coefficients in $L_0$;
6. `ChebSplit`, a density condition on split Frobenius elements;
7. $L_0$ is closed under the conjugation of $L$;
8. the exponents `eExp D j g` are integers;
9. the places over the primes `pde` and `pde'` split in $E / F^+$.

**Theorem.** There is a bound $c_0$ such that the following holds. Let $b_0 \ge c_0$, $b_1$, $S_x$, $T$ and a ring specification be given, with $S_b \subseteq S_x$, $S_x$ closed under conjugation and containing all places over $\mathrm{low}$. Then there are twist data $F$ (`TwF`: signatures with Galois representations, lattices, Hecke operators) and a datum `ex` (`NExp`) whose lattices are finitely generated and span over $\operatorname{Frac} O(i)$, such that `SideB` holds for the new datum, whatever its field `th`.

`SideB` has 29 fields: a twist frame, characters that agree with $c_f$, a datum `NExpTied`, a comparison of the forms of `ex` with those of $S$, Hecke and Frobenius compatibilities at split places, and the Galois representations of the signatures.

## Proof

1. `exists_galois_rep_family_bounded_alt` (from 1, 4 to 7) gives a bound $c_1$, and over any $b_0 \ge c_1$ continuous $\rho$ with values in $\mathrm{GL}_r(O_0(i))$ attached to the twists of the $\pi$ of item 5.
2. `exists_weight_data_integral_alt` (from 1, 7, 8) gives a bound $c_2$ and weight data: irreducible algebraic representations with prescribed highest weights. Take $c_0 = c_1 \sqcup c_2$.
3. `mkF` and `mkEx` build $F$ and `ex`, with inputs from `twisted_lattice_finitely_generated_spanning` (the lattice condition), `hkStab_of_subset_of_star_closed` and `exists_signature_data_span_alt`.
4. The fields of `SideB` come mainly from `tied_U_clauses`, `places_over_real_subfield_split_alt` (from 3 and 9, for the level data) and `twistLiftForms_eq_baseChange_rationalDatumForms`. The rest is bookkeeping.

## In the Lean code

The theorem is in [SecondStep.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondStep.lean#L21). `SideB` is in [RingSpecNormalisedCharacterEq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/RingSpecNormalisedCharacterEq.lean#L185). We have read the statements of the lemmas, not their proofs.

- Hypothesis 2 is never used: `hM` is introduced and not mentioned again. So $M$, `tup` and $Q$ are idle.
- The fields `qs_pos`, `chiI`, `lamG`, `thU_empty` and `psi` are filled by eliminating an element of an empty type.
