---
title: The stage statements and the first level
decls:
  - GlobalTheory.T.all_stages_at_member_of_specializations_alt
  - GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt
  - GlobalTheory.T.settingsFormsExistList_of_inputs_serN
  - GlobalTheory.HeightCounting.Up.PointwiseSettings.settings_forms_exist_list_of_published_inputs
  - GlobalTheory.HeightCounting.Up.PointwiseSettings.pointwise_alt_alt
  - GlobalTheory.T.row_cusp_multiplicity_input_alt
  - GlobalTheory.HeightCounting.FormsStep.second_step_alt
  - GlobalTheory.T.exists_weight_data_integral_alt
  - GlobalTheory.HeightCounting.FormsStep.wt_weights_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The stage statements and the first level

This section states the thirteen stage statements and proves the first step of the ladder of levels: an intermediate level datum at a stage gives a stage with a first level datum. [The Theorem on the origin extension](/entry/exists-base-lattice-of-prime-alt/) of Section 1 uses the stage statements to build $\mathrm{Has}_3$ for the parameter set $p(N_0)$. Each stage statement comes from a separate lemma; this section proves the first level step, and Sections 7 to 9 prove the others. The first level step rests on the second step: over twist rings with a large bound on the local coefficient fields, a datum has twist data and a side record. The bound comes from Galois representations and from weight data.

**Definition 6.6.1 (Stages and levels).** Let $K$ be a context and $w$ a column datum, and let $P$ be a datum over $(K, w)$. A *stage* of $P$ is a point $x$ over $P$. A statement holds *at all stages* if it holds at every stage of every such $P$, for the steps that $\mathrm{Step}_w$ admits from the start condition. Over a stage $x$ there is a ladder of data:

1. a *same Galois level* datum;
2. an *intermediate level* datum, which adds a matrix input, a rationality input and the row cusp condition;
3. a *first*, *second* or *third level* datum, which adds settings forms data, series data or moduli points data;
4. a *strict henselian acyclic level* datum, which adds height counting character data.

For a real number $c$, the *list condition* at $x$ says that there is a grid datum $G$ for the level characters of $x$ with the field condition, such that the twist datum of $x$ is fully tied to the character $\lambda(G)$.

We write $\mathcal{P}$ for the published inputs of the third layer, a record of fourteen statements, and $\mathcal{S}$ for the series input, a record of six statements. They are fields of $\mathcal{H}_L(h_L)$ in Section 1.

**Theorem 6.6.2 (Stage statements).** Assume the Casselman-Wallach theorem, the theory of Harish-Chandra modules, the Weil representation of a unitary dual pair, existence and uniqueness of discrete series of $U(p, q)$, the multiplicity cover statements, $\mathcal{P}$ and $\mathcal{S}$. Let $h_L$ be a recursion datum, and assume the archimedean comparison and the point statement for $h_L$. Then at all stages $x$:

1. if the local index set of $x$ is empty, there is a stage $x'$ with a same Galois level datum and the same Galois data as $x$;
2. $x$ has a matrix input, and a rationality input when it has a same Galois level datum;
3. each same Galois level datum over $x$ satisfies the row cusp condition;
4. an intermediate level datum over $x$ gives a stage with a first level datum; a first level datum gives a stage with a second level datum; a second gives a stage with a third;
5. each third level datum over $x$ extends to a strict henselian acyclic level datum;
6. each such datum gives, for each $S$-extension $S$ and geometry $\Gamma$, a level three object at the parameter set of the extension with law, with the same weights and a kept norm choice.

Also, for each real $c$, the three steps of item 4 hold with the list condition for $c$ carried along, and item 6 holds at stages with the list condition for $c$, at the parameter set of the extension with list for $h_L$ and $c$.

Lean: `GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt` (also `GlobalTheory.T.all_stages_at_member_of_specializations_alt`, a second name).

*Proof.* Item 2 follows from $\mathcal{P}$ for the matrix input, and from the isotypic internal inputs at all stages for the rationality input. Item 3: $\mathcal{P}$ and the matrix input give the parameter statement, and the parameter statement gives the row cusp condition. Item 1 follows from $\mathcal{P}$ and the comparison field of the archimedean comparison. Item 4 with lists is the theorem on first level data below and its analogues for series data (Section 9) and moduli points data, all from $\mathcal{P}$ and $\mathcal{S}$; item 4 without lists is the case $c = 0$ with the list condition dropped. Item 5 follows from the cover field of the multiplicity cover statements, Casselman-Wallach, Harish-Chandra modules, $\mathcal{P}$ and $\mathcal{S}$. For item 6, [the eta statement](/entry/s-eta-alt-alt-alt/) of Section 8 follows from the point statement; with the existence of theta data it gives item 6 and its list form by [the finiteness theorem](/entry/s-fin-and-s-finl-of-arch-cmp-s-eta-theta-data/) of Section 7. $\square$

**Definition 6.6.3 (Bounds and twist rings).** Let $D$ be a datum with CM field $E$, maximal real subfield $F^+$ and coefficient field $L_0$. A *bound* for $D$ chooses a finite extension of $\mathbb{Q}_\ell$ for each prime $\ell$ and each embedding $L_0 \to \overline{\mathbb{Q}}_\ell$; bounds are ordered by inclusion, with a least bound $\bot$ and a join $\sqcup$. *Twist rings* $T$ give for each index $i$ a prime $\ell_i$, a discrete valuation ring $O_0(i)$ finite over $\mathbb{Z}_{\ell_i}$ with embeddings of $L_0$ into its fraction field, and an extension $O(i)$. A *ring specification* ties $T$ to two bounds $b_0, b_1$ and a finite set $S_x$ of places of $E$.

The *side record* of a datum with twist data and exponent data has twenty-nine conditions: a twist frame, characters that agree with a given character frame, tied exponent data, a comparison of forms with a rational datum, Hecke and Frobenius compatibilities at split places, and the Galois representations of the signatures.

**Theorem 6.6.4 (Weight data).** Assume global Artin reciprocity. Let $D$ be a datum with a character frame and an embedding datum, and assume that the image of complex conjugation preserves $L_0$ and that the exponents of $D$ are integers. Then there is a bound $c_2$ such that for all bounds $b_0 \ge c_2$, $b_1$, sets $S_x$ and twist rings $T$ with a ring specification, there are weight data such that for each index $i$ and each $j$ with $1 \le j \le m$:

1. the weight representation at $(i, j)$ is irreducible and algebraic;
2. the representations at each embedding $k$ are irreducible;
3. at each embedding $t$, the dual representation has a highest weight $\lambda$;
4. for each $t$, each half integral $h$ with infinitesimal character $\{h\}$ and each highest weight $\lambda$ at $t$, the infinitesimal character of $\lambda$ equals the parameter of $D$ at $t$ and $j - 1$ for $h$.

Lean: `GlobalTheory.HeightCounting.FormsStep.wt_weights_alt` (also `GlobalTheory.T.exists_weight_data_integral_alt`, a second name).

*Proof.* Take $c_2 = \bot$. Build the weight representations as tensor products of the standard representations at each embedding with the prescribed weights. They are irreducible and algebraic, and their duals have highest weights. The lift of the weight parameter equals the infinitesimal character for half integral parameters, and the infinitesimal character of the parameter is half integral. This gives item 4. $\square$

**Theorem 6.6.5 (Second step).** Assume global Artin reciprocity. Let $D$ be a datum with a character frame $c_f$, an embedding datum $A$, a rational datum with a finite set $S_b$ of places, a finite set $\mathrm{low}$ of primes, and for each finite place $v$ of $F^+$ a place $P_q(v)$ of $E$. Assume:

1. a matrix input for $D$;
2. $P_q(v)$ lies over $v$ for each $v$;
3. each conjugate self-dual regular algebraic cuspidal $\pi$ of $D$ has, for each $\ell$ and each $\iota$, a continuous semisimple $\ell$-adic representation that matches $\pi$ at almost all places;
4. the row cusp condition for $A$: each good row that occurs comes from such a $\pi$, with the local data of $A$ at split places and, at almost all places, coefficients in $L_0$;
5. density of split Frobenius elements;
6. $L_0$ is closed under the conjugation of $L$;
7. the exponents of $D$ are integers;
8. the places over two given primes split in $E / F^+$.

Then there is a bound $c_0$ such that, for all $b_0 \ge c_0$, $b_1$, $S_x$ and $T$ with a ring specification, with $S_b \subseteq S_x$, $S_x$ closed under conjugation and containing all places over $\mathrm{low}$, there are twist data $F$ and exponent data whose lattices are finitely generated and span over the fraction field of $O(i)$, such that the side record holds for the new datum.

Lean: `GlobalTheory.HeightCounting.FormsStep.second_step_alt` (also `GlobalTheory.T.row_cusp_multiplicity_input_alt`, a second name).

*Proof.* From hypotheses 3 to 6 and Artin reciprocity there are a bound $c_1$ and, over every $b_0 \ge c_1$, continuous representations with values in $\mathrm{GL}_r(O_0(i))$ attached to the twists of the $\pi$ of hypothesis 4. The theorem on weight data gives $c_2$. Take $c_0 = c_1 \sqcup c_2$. The twist data and the exponent data are built from these representations and the weight data; the lattices are finitely generated and span, the Hecke stabilizers are closed under conjugation, and the signatures span. The conditions of the side record come from the tied clauses, from the splitting of the places over the real subfield (hypotheses 2 and 8) and from the equality of the twisted lift forms with the base change of the forms of the rational datum. $\square$

**Theorem 6.6.6 (Pointwise step).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Let $x$ be a stage with datum $D$, $l$ an intermediate level datum over $x$, and $G$ a grid datum for the level characters of $x$ with the field condition, such that $\lambda(G)$ is admissible, has the character frame of $x$ and the base value of $D$. Then there is a stage $x'$ of the same datum with a first level datum and with the list condition for $c$.

Lean: `GlobalTheory.HeightCounting.Up.PointwiseSettings.pointwise_alt_alt`.

*Proof.* There are seven steps.

1. The finiteness and Galois fields of $\mathcal{P}$ and the cohomology datum of $l$ give the Galois representations of hypothesis 3 of the second step; the Chebotarev field gives the density of split Frobenius elements.
2. The second step gives a bound $c_f$, and the existence of twist rings with characters and class groups gives a bound $c_r$. Let $b_0 = c_f \sqcup c_r$.
3. There is a finite set $S_x$ of places of $E$ that contains all places over the low primes of $D$, lies over these primes and is closed under conjugation.
4. Twist rings $T'$ with a ring specification exist at $(b_0, b_0, S_x)$; each excluded set $S_0(i)$ is a union of five sets, one of which is $S_x$, so $S_x \subseteq S_0(i)$.
5. The second step at $(b_0, b_0, S_x, T')$ gives twist data, exponent data and the side record for the empty toric list.
6. From cyclotomic integers, Chebotarev, Artin reciprocity and the ratio field of $\mathcal{S}$, there is a list of toric characters in the twist coefficient rings such that the twist datum with this list is fully tied to $\lambda(G)$ and the side record passes to it. The conductor primes lie in the low set.
7. The remaining theta data are built from the finitely generated lattices, and the restaging lemma gives $x'$. Its last hypothesis, that each $S_0(i)$ lies over $\{\ell_i\}$ and the low primes, follows from the five set description. $\square$

**Theorem 6.6.7 (First level data).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. For each real $c$, at all stages $x$, each intermediate level datum over $x$ gives a stage $x'$ of the same datum with a first level datum and the list condition for $c$.

Lean: `GlobalTheory.HeightCounting.Up.PointwiseSettings.settings_forms_exist_list_of_published_inputs` (also `GlobalTheory.T.settingsFormsExistList_of_inputs_serN`, a second name).

*Proof.* At every stage there is a grid datum with the field condition that fits $x$. By transitivity of steps it is enough to treat one stage, and there the pointwise step applies with this grid. $\square$

**Remark 6.6.8 (Formalization).** The theorems are at [AllStagesAtMemberOfSpecializations.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AllStagesAtMemberOfSpecializations.lean#L32) (second name at line 52), [ReductionSeriesB0.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReductionSeriesB0.lean#L26) (first level data at line 87, its second name at line 98), [SecondStep.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondStep.lean#L21), [SecondStepStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondStepStatement.lean#L11), [WtWeights.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/WtWeights.lean#L16) and WtWeightsStatement.lean. The second names are relays proved by `first | exact … | …`, with `maxHeartbeats 1000000`. In the second step the hypothesis `MtInput D M tup Q` is introduced as `hM` and never used, and the fields `qs_pos`, `chiI`, `lamG`, `thU_empty` and `psi` of `SideB` are filled by eliminating an element of an empty type. In `wt_weights_alt` the proof begins `intro _ D cf jE A _ _` (line 27), so global Artin reciprocity, the conjugation hypothesis and the integrality of the exponents are unused, and line 28 sets `c2 := ⊥`, so the bound is trivial. The pointwise step uses only the field `ratio` of `SerN` and four fields of `what₂` of the published inputs; both twist ring calls use $b_0$ for both bounds. In the stage statements, item 4 without lists is a weak form of item 4 with lists, and the caller discards it and item 6 without lists ([ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L64)). The words "specializations", "at member", "row cusp multiplicity" and "strict henselian acyclic" match no object of the statements. Older twins exist: `pointwise` in the IwasawaDecomposition folder with `PrN` and `LocalLanglandsGL`, and `row_cusp_multiplicity_input`. We did not unfold `St`, `StepW`, `SettingsFormsData`, `HeightCountingCharacterData`, `SideB` beyond its list of fields, or the grid lemma, so the proofs above follow the statements of the lemmas, not their proofs.
