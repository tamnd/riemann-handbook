---
title: Series data on a twisted copy
decls:
  - GlobalTheory.T.seriesExistList_of_inputs_serN
  - GlobalTheory.HeightCounting.Up.SeriesStep.sb1l_alt_alt
  - GlobalTheory.T.series_copy_embedding_of_cmDatum_alt
  - GlobalTheory.HeightCounting.SerCopy.series_copy_embedding_alt
  - GlobalTheory.HeightCounting.SerCopy.pre_at_twisted_copy_of_side_b_tau_true
  - GlobalTheory.HeightCounting.SerCopy.pre_at_of_side_b_tau_true_lam_ok
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Series data on a twisted copy

This section proves the middle step of item 4 of [the stage statements](/entry/all-stages-of-specializations-alt/) of Section 6: a first level datum at a stage gives a stage with a second level datum, and the list condition passes along. The new stage is a twisted copy of the old one. We choose a new twist of the datum of the stage, prepared so that its side record has a true tau condition, and then build on the copy the prepared data from which the series data follow. The only published input that is used is global Artin reciprocity.

Let $x$ be a stage of a datum $P$ with datum $D_x$, CM field $E$ and coefficient field $L_0$. An intermediate level datum $l$ over $x$ has base data, a choice $P_q$ of a place of $E$ above each finite place of the maximal real subfield, a matrix input, a rationality datum with a finite set $S_b$ of places, Hecke operators, eigenvalues and characters $\theta$, and a cusp condition.

**Definition 6.9.1 (First and second level data).** A *first level* datum over $x$ adds settings forms data: a side datum, the inclusions $S_b \subseteq S_0(i)$ for each index $i$, the place condition that each place of $S_0(i)$ lies over $\ell_i$ or over a low prime of $D_x$, and a lambda datum fully tied to the twist of $x$. A *second level* datum adds series data: the settings forms data together with a series datum, a series condition at the places and the tau condition.

**Definition 6.9.2 (New twists and twisted copies).** A *new twist* $N$ of $D_x$ is a twist datum with exponent data, theta data and local bridges at the twisting places. It gives a twisted datum $N(D_x)$, a twisted character frame, a twisted row and twisted rational data. The *twisted point* of $x$ along $N$ is the point of $x$ with its twist replaced by $N$; a *twisted copy* of $(x, l)$ along $N$ is a stage $x'$ at the twisted point with an intermediate level datum $l'$ whose row and rational data are the twists of those of $l$, whose $P_q$, $S_b$, Hecke operators, eigenvalues and characters agree with those of $l$, and whose real data, group isomorphism and geometric datum are transported from $x$.

**Definition 6.9.3 (Prepared data).** Let $z$ be the base point of a stage, with row, choice $P_q$ and rational inputs. The point is *prepared* if its row character equals the character frame of the column datum at the level and the stage, and there are coefficient fields with a Hecke tie equal to the given one, a side record $B$ over them whose exponent data satisfy the tau condition, and a prepared tie.

The tau condition is a condition on the exponent data of a side record; we do not unfold it here.

**Lemma 6.9.4 (Prepared data at a stage).** Assume global Artin reciprocity. Let $K$ be a context over the pre-base of a base $B$, $w$ a column datum with the start condition, $x$ a stage and $l$ an intermediate level datum over $x$. Assume that there is a side record for $D_x$ with the tau condition, that $S_b \subseteq S_0(i)$ for every $i$, and that there is an admissible lambda datum for $D_x$. Then the base point of $x$ is prepared, with the row, $P_q$ and rational inputs of $l$.

Lean: `GlobalTheory.HeightCounting.SerCopy.pre_at_of_side_b_tau_true_lam_ok`.

*Proof.* From the start condition and $K$ over the base, the choice conditions hold at $x$: the roots of unity of order $g_k(g_k - 1)$ lie in the image of $L_0$, and the row character of $l$ equals the character frame. Transport the side record along this equality; the tau condition is kept. The prepared tie is given by new theta data with series, class sums and lattices, from Artin reciprocity, the geometric and pin data of $x$, the Hecke data of $l$, the inclusions $S_b \subseteq S_0(i)$, the tau condition, the character and valuation data, the splitting of places, the place choice $P_q$, the roots of unity and the lambda datum. $\square$

**Lemma 6.9.5 (Prepared data on a twisted copy).** Assume global Artin reciprocity. Let $K$, $B$, $w$, $x$ and $l$ be as in the lemma above, and let $N$ be a new twist of $D_x$. Assume that there is a side record for $N(D_x)$ with the twisted frame, row and rational data and the tau condition, that $S_b \subseteq S_0(i)$ for the excluded sets of $N$, and that there is an admissible lambda datum for $N(D_x)$. Then the twisted base point of $x$ along $N$ is prepared, with the twisted row and the data of $l$.

Lean: `GlobalTheory.HeightCounting.SerCopy.pre_at_twisted_copy_of_side_b_tau_true`.

*Proof.* There is a twisted copy $(x', l')$ of $(x, l)$ along $N$. The lemma on prepared data at a stage applies at $(x', l')$, whose datum is $N(D_x)$. The base point of $x'$ is the twisted base point of $x$, and the data of $l'$ equal the data of $l$ or their twists. So the conclusion transports back to the twisted base point. $\square$

**Theorem 6.9.6 (Series data on a twisted copy).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Let $K$ be a context over a base $B$ with forced primes for $T$, and $w$ a column datum with the start condition. Let $x$ be a stage of $P$ and $l$ a first level datum over $x$. Then there is a new twist $N$ of $D_x$ such that:

1. every lambda datum fully tied to the twist of $D_x$ is fully tied to the twist of $N$;
2. for every twisted copy $(x', l')$ of $(x, l)$ along $N$, every matrix input at $x'$ whose frames are identity frames gives series data for the geometric datum of $x'$, the data of $l'$ and the frames of the matrix input.

Lean: `GlobalTheory.HeightCounting.SerCopy.series_copy_embedding_alt` (also `GlobalTheory.T.series_copy_embedding_of_cmDatum_alt`, a second name).

*Proof.* There are five steps.

1. From the start condition and $K$ over the base, the roots of unity of order $g_k(g_k - 1)$, for $k = 0, 1$, lie in the image of $L_0$.
2. Artin reciprocity, the side datum of $l$, its valuation datum and step 1 give a prepared twist $N_1$ with item 1. Each twisting set and prime of $N_1$ is one of $D_x$; $N_1$ has no offset and a universal character; and $N_1$ has a side record with the tau condition.
3. The inclusions of the settings forms data of $l$ give $S_b \subseteq S_0(i)$ and the place condition for the twisting sets of $N_1$.
4. [The lemma on prepared data on a twisted copy](/entry/pre-at-twisted-copy-of-side-b-tau-true/) gives a prepared tie on the copy. Let $N$ be $N_1$ with its exponent and theta data taken from this tie. It has the same twist datum, so item 1 holds.
5. For item 2, the prepared tie, the tau condition, step 3 and the properties of $(x', l')$ give the series data. $\square$

**Theorem 6.9.7 (Second level data).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Let $c \in \mathbb{R}$. At all stages $x$, each first level datum over $x$ gives a stage $x'$ of the same datum with a second level datum, and the list condition for $c$ at $x$ implies the list condition for $c$ at $x'$.

Lean: `GlobalTheory.HeightCounting.Up.SeriesStep.sb1l_alt_alt` (also `GlobalTheory.T.seriesExistList_of_inputs_serN`, a second name).

*Proof.* At all stages there is a matrix input whose frames are identity frames. Fix $x$ and a first level datum $l$. [The theorem on series data on a twisted copy](/entry/series-copy-embedding-alt/) gives a new twist $N$ and its transport property. There is a twisted copy $(x', l')$ of $(x, l)$ along $N$. A matrix input with identity frames at $x'$ and item 2 give series data. The second level datum is $l'$ with its matrix input replaced by this one, together with the series data. The list condition passes to the twisted point by item 1. $\square$

**Remark 6.9.8 (Formalization).** The theorems are at [SecondBoundOfPrimitive.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondBoundOfPrimitive.lean#L25) (second name at line 40), [SeriesCopyEmbeddingOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesCopyEmbeddingOfCmDatum.lean#L35) (second name at line 65) and [SeriesStateB1OfGeometry.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesStateB1OfGeometry.lean#L40) (the twisted copy lemma at line 51). Prepared data are `PreAt` ([ExistsNewTwistLamFull.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsNewTwistLamFull.lean#L89)), and the tau condition is `TauTrue`. In `series_copy_embedding_alt`, `SerN` and `Forced K B T` are bound to `_` and not used, and of the published inputs only `hPr.what₂.art` is used; the hypothesis on `l'.rat.S` in item 2 is also not used. So the series input enters this section in name only. The field `rootsOfUnityRing_le_wittIntegers` of `SettingsFormsData` is the place condition `OverSet`; no ring of roots of unity and no Witt vectors appear. The matrix input lemma `exists_matrix_input_identity_frame_of_inputs` is proved by `fun _ => …` and ignores the published inputs. In `pre_at_of_side_b_tau_true_lam_ok` the pattern `⟨h1, h2, h3, h4, -⟩` drops one part of `isChoice_of_start_of_over`. The twisted copy lemma states its conclusion with casts `by with_unfolding_all exact (… :)` and proves it by destructuring the copy and `subst`. The file sets `maxHeartbeats 4000000` and `synthInstance.maxHeartbeats 400000`. The names `sb1l`, "series copy embedding" and "of CM datum" do not describe the statements, and the module name "second bound of primitive" names no bound and no primitive object. We did not unfold `SeriesData`, `PreTie`, `TwNew`, `SideB` or `TauTrue`.
