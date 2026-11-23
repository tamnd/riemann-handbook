---
title: Full rank and inert Satake parameters
decls:
  - GlobalTheory.T.fullRank_thetaSeries_forms_of_rational_scalars
  - GlobalTheory.TieRank.rank_of_ties
  - GlobalTheory.T.goodForms_classSums_of_projectedLift_range
  - GlobalTheory.RankOnto.sumOnto_of_goodRange
  - GlobalTheory.T.inert_satake_parameters_agree_under_dictionary
  - GlobalTheory.InertDict.satake_agree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Full rank and inert Satake parameters

Section 4 shows that the rows of theta series are rational after a scalar. This section shows that they are also large enough: the theta series of a rational row span, over the fraction field of the coefficient ring, the whole space of forms of the given type. The proof goes through the classical fact that a theta series reads as a class sum of a model vector, together with the theorem that the theta translates of the archimedean model fill the good part of the model. The section ends with a separate result on Satake parameters at inert places: a dictionary between an automorphic representation and a space of automorphic forms on a definite unitary group keeps the Satake parameters at the places of $F$ that are inert in $E$. The full rank theorem is used by [the export at a bundle](/entry/export-at-of-bundles-alt/) in the theta pair lifts of Volume 7.

### Forms of a fixed type

We keep the series side $Y$ over the real side $X$ of Section 4. For a twist index $i$, an index $j$ and a sign $b$, the integral Hecke data give a finite group $U$ of units that acts on the space $\mathcal{F}_{ijb}$, a character $\psi_{ib}$ of $U$ with values in $K_i^\times$, and an equivariant map $e$ on $\mathcal{F}_{ijb}$. Put
$$\mathcal{F}^0_{ijb} = \{x \in \mathcal{F}_{ijb} : u \cdot x = \psi_{ib}(u)\,x \text{ for all } u \in U\}, \qquad V^0_{ijb} = e(\mathcal{F}^0_{ijb}) .$$
This is the space of *forms of type $(i, j, b)$*. The Hecke data also fix a set $\Sigma^0_{ijb}$ of *base data*, whose theta series $\theta_a$ ($a \in \Sigma^0_{ijb}$) are equivariant under $U$ with the character $\psi_{ib}$.

**Definition 3.5.1 (Full rank).** A set $\Sigma \subset \Sigma^0_{ijb}$ of data has *full rank* if the images $A(\theta_a)$, $a \in \Sigma$, of the theta series under the averaging map $A$ lie in $V^0_{ijb}$, and the $K_i$-span of these images is all of $V^0_{ijb}$.

**Definition 3.5.2 (Base tuple).** The series side has a *base tuple* at $i$ if, for every $(j, b)$, the real side has a family $t$ of characters with the same Hecke character and the same set of places as the data of the row $(i, j, b)$.

For each index $j$, the archimedean model of $X$ has a space $H_j$ of harmonic vectors, a map $\theta^G_{j,t}$ from the Fock space of a family $t$ to $H_j$, and a *good model* $G_j \subset H_j$: the inverse image under the evaluation map of the vectors fixed by the trivial level. The real side has *good range* if $\theta^G_{j,t}$ maps onto $G_j$ for every $j$ and $t$; this is the archimedean form of the statement that the theta lift of the vacuum is the full lowest weight space (see [the Fock model](/learn/theta/#the-fock-model) and [the local theta correspondence](/learn/theta/#the-local-theta-correspondence)).

**Definition 3.5.3 (Class sums onto).** The reading $\mathrm{rd}$ is *onto class sums* at $i$ if every $x \in V^0_{ijb}$ has a reading of the form $\mathrm{rd}(x) = \Sigma(\Phi)$, where $\Phi$ is in the $\mathbb{C}$-span of the model translates of the row and $\Sigma$ is the class sum at level $1$ with the empty set of places.

### Class sums

**Proposition 3.5.4 (Forms are class sums).** Let the real side have good range, and let the series side have a base tuple at $i$. Then the reading is onto class sums at $i$.

Lean: `GlobalTheory.RankOnto.sumOnto_of_goodRange` (also `GlobalTheory.T.goodForms_classSums_of_projectedLift_range`, a second name).

*Proof.* Let $x \in V^0_{ijb}$. The development gives a vector $w$ of the good model with $\mathrm{rd}(x) = \nu^{-1}\,\mathrm{ev}(w)$, where $\nu \neq 0$ is the scalar of the row and $\mathrm{ev}$ evaluates a model vector at the base vacuum. It also proves that the reading of a form of good type is right invariant under the lifts of the translates. Multiply by $\nu$: the function $\mathrm{ev}(w)$ is $\nu\,\mathrm{rd}(x)$, and it has the same invariance. The good range and the base tuple now give $\Phi$ in the span of the translates with $\Sigma(\Phi) = \mathrm{ev}(w)$, at base level. Then $\nu^{-1}\Phi$ is in the same span, and $\Sigma(\nu^{-1}\Phi) = \nu^{-1}\,\mathrm{ev}(w) = \mathrm{rd}(x)$, since $\Sigma$ is linear. $\square$

### Full rank

**Theorem 3.5.5 (Full rank of theta series).** Assume that cusp forms decay rapidly. Let the series side have a base tuple at $i$, and let every row $(i, j, b)$ be rational. Then for every $j$ with $1 \le j \le m$ and every $b$, the set $\Sigma^0_{ijb}$ of base data has full rank.

Lean: `GlobalTheory.TieRank.rank_of_ties` (also `GlobalTheory.T.fullRank_thetaSeries_forms_of_rational_scalars`, a second name).

*Proof.* Rapid decay of cusp forms, together with the size condition, the level, the group record, the family and the models of $X$, gives good range for every $j$ and $t$. By [the class sum proposition](/entry/sum-onto-of-good-range/), the reading is onto class sums at $i$. The development proves that a reading onto class sums is spanned by theta series: every $\mathrm{rd}(x)$, $x \in V^0_{ijb}$, is in the $\mathbb{C}$-span of the theta series of the data. The reading is faithful: it is injective, and a scalar that relates two nonzero readings comes from $K_i$. The development then proves that a faithful reading of rational rows, whose readings are spanned over $\mathbb{C}$ by the theta series and whose theta series are all forms of the right type, has full rank. The idea is a descent of a spanning set from $\mathbb{C}$ to $K_i$, and faithfulness is what makes the descent possible. $\square$

The hypothesis that every row is rational is the conclusion of [the rationality theorem](/entry/rat-and-xi-bdd/). In the development the two are joined at the export at a bundle.

### Inert Satake parameters

Let $L$ be a CM field with maximal real subfield $L^+$, and let $n \ge 1$. Let $\pi$ be an automorphic representation of $\mathrm{GL}_n$ over $L$ in the sense of the development, and let $U$ be a space of functions on the adelic points of a unitary group $\mathrm{U}_n$ for $L/L^+$. A *finite identification* is a ring isomorphism of the finite adeles of $L$ with $L \otimes \mathbb{A}_{L^+,f}$ that is the identity on $L$ and continuous at each place, together with a surjection $j$ from the finite adelic points of the general linear group onto the finite part of the unitary group that is compatible with the local matrices. A *dictionary* between $\pi$ and $U$ is a finite identification such that $U$ is an automorphic representation of $\mathrm{U}_n$ and the pull back of $U$ along $j$ is the span of the matrix coefficients of $\pi$.

Let $v$ be a finite place of $L^+$ and $w$ a place of $L$ above $v$. Let $s$ be a ring endomorphism of $L_w$ that extends complex conjugation of $L$, let $\varpi \in L_w$ and let $q \ge 2$. We say that $(s, \varpi, q)$ is an *unramified involution* if $s$ is an isometric involution of $L_w$ that fixes $\varpi$, $\varpi$ is a uniformizer, $s$ acts nontrivially on the residue field, and the residue field has $q^2$ elements. Then $L_w / L_w^{s}$ is the unramified quadratic extension, so $v$ is inert in $L$. An *inert datum* at $(v, w)$ is an identification $L \otimes_{L^+} L^+_v \cong L_w$ that carries complex conjugation to $s$, a uniformizer $\varpi$, and an integral matrix $P$ with $s(P)^{t}P$ equal to the antidiagonal matrix $J$. A *Satake parameter* of $U$ at $w$ is a tuple $\alpha \in (\mathbb{C}^\times)^{\lfloor n/2 \rfloor}$ such that, after conjugation by an integral $b$ with $s(b)^{t} b = J$, the local component of $U$ at $w$ is the unramified representation with parameter $\alpha$ (see [unramified representations](/learn/representations/#unramified-representations)).

**Theorem 3.5.6 (Inert Satake parameters agree).** Let $F$ be a finite identification and assume a dictionary between $\pi$ and $U$. Let $w$ be over $v$.

1. If $\pi$ is spherical at $v$, then $U$ is unramified at $w$.
2. Let $(s, \varpi, q)$ be an unramified involution, where $s$ extends complex conjugation. Then there is an inert datum at $(v, w)$ with involution $s$ and uniformizer $\varpi$. Let $D_v$ be any inert datum with these $s$ and $\varpi$, and let $\alpha$ be a Satake parameter of $\pi$ at $D_v$. Then all entries of $\alpha$ are nonzero, and $\alpha$ is a Satake parameter of $U$ at $w$ for $(s, \varpi, q)$.

Lean: `GlobalTheory.InertDict.satake_agree` (also `GlobalTheory.T.inert_satake_parameters_agree_under_dictionary`, a second name).

*Proof.* Part 1: a spherical vector of $\pi$ at $v$ gives, through the dictionary, a nonzero vector of $U$ fixed by the local maximal compact subgroup at $w$.

Part 2. Since $(s, \varpi, q)$ is an unramified involution, $w$ is unramified and not split over $v$, and $q$ is the order of the residue field of $v$. An involution and a uniformizer of this kind give an inert datum: the identification of the completions, and a matrix $P$ with $s(P)^{t}P = J$, by the classification of Hermitian lattices over the unramified extension (see [local classification](/learn/hermitian-lattices/#local-classification)).

Now let $D_v$ and $\alpha$ be given. A Satake parameter of $\pi$ at $D_v$ comes with a spherical vector, so $\pi$ is spherical at $v$, and by Part 1, $U$ is unramified at $w$. A definite unitary representation that is unramified at an inert place has a Satake parameter $\alpha_0$ at $(s, \varpi, q)$. The Hecke eigenvalues of $\pi$ at $D_v$ and of $U$ at $w$ agree under the dictionary. So the Satake transforms of $\alpha$ and $\alpha_0$ take the same values on the spherical Hecke algebra. Two parameters with the same Satake transform have the same nonzero entries; in particular each $\alpha_i \neq 0$. Then $\alpha$, read as a tuple of units, satisfies the defining property of a Satake parameter of $U$ with the matrix $b$, the local map and the representation of $\alpha_0$, since the eigenvalues of $\alpha$ and $\alpha_0$ agree on each Hecke operator. $\square$

**Remark 3.5.7 (Formalization).** The full rank theorem is `TieRank.rank_of_ties` in [FullRankThetaSeriesFormsOfRationalScalars.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FullRankThetaSeriesFormsOfRationalScalars.lean#L82). It is assembled from `AdSpan.goodRangeAt`, `T.averaged_series_full_rank_of_complex_span_good` and `T.goodForms_spanned_by_thetaSeries_of_classSums`, which we did not open. The same file has a helper `faithful_serSide` (line 77) and an unused definition `scR` (line 34). Its sections `Onto`, `Comparison₂`, `Tie2` and `Main` (lines 39 to 72) declare variables and nothing else. The predicates `FullRk`, `V0` and `SgJ` are in [IntegralHeckeForms.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/IntegralHeckeForms.lean#L177); `SgJ` is the whole set `Dat0`, so the theorem states full rank for all base data. The good range `GoodRangeAt` is in [ThetaTranslateRangeGap.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/ThetaTranslateRangeGap.lean#L33), and `SumOnto` and `BaseTup` are in [UnivChar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnivChar.lean#L133). The class sum proposition is [GoodFormsClassSumsOfProjectedLiftRange.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GoodFormsClassSumsOfProjectedLiftRange.lean#L19). The Satake theorem is at [InertSatakeParametersAgreeUnderDictionary.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InertSatakeParametersAgreeUnderDictionary.lean#L18). It uses `FinIso` and `Dict` ([FinIso.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FinIso.lean#L14)), `IsUnramInv` ([StatementF.lean](lean:Formalism/SatakeDualWeyl/StatementF.lean#L14)), `InertDatum` ([InertDatumExists.lean](lean:Formalism/AlgebraicWeights/InertDatumExists.lean#L18)), and `HasSatAt` ([BaseChangeDefiniteUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BaseChangeDefiniteUnitary.lean#L133)). The six inputs of its proof, from `T.isUnramified_of_sphericalVector_dictionary` to `T.satakeParameter_ne_zero_of_sameTransform`, were not opened; the description of their content above follows their names and statements. A different `Dict` structure, for theta series, is in `SeriesRay.lean`.
