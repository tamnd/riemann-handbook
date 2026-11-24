---
title: The definite rows
decls:
  - GlobalTheory.Fc.StageZeroRow.row_rRows_stage0_alt
  - GlobalTheory.T.indefinite_scale_theta_nonvanishing_alt
  - GlobalTheory.RowPlacementReal.placement_of_realisation_alt
  - GlobalTheory.T.eventually_small_of_seeEx_primitive
  - GlobalTheory.Fc.Ind.small_along_alt
  - GlobalTheory.T.indefScale_theta_degree
  - GlobalTheory.passIn3_at_realT_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The definite rows

This section proves the definite row of the record of all rows. Step 7 of [the theorem on all rows](/entry/all-rows-of-open0-alt/) uses it. The definite row asks for nine constant bounds at the selected bundles, with one constant, and for the definite side condition. Five bounds come from the rows that step 7 joins. Two come from the estimates of branch 2. The last two, the small bounds and the passing bound, need the real place: a normalised indefinite realisation extends, by the classification of the [[discrete series|9AB7HYGPEK]], and the passing condition holds when the coefficient field is totally complex. The analytic content is in [the placement of a row](/entry/exists-row-placement-finite-element-matches-levels/) and in [the passing condition from rows](/entry/pass-in3-of-rows/).

We first treat the real place, then the small bounds, then the definite row.

**Definition 8.5.1 (Classification of the discrete series).** The *classification of the discrete series* says: for each sign vector $\varepsilon \in \{0,1\}^n$ and each strictly decreasing $\lambda \in \mathbb{R}^n$ with $\lambda_a - \tfrac{n-1}{2} \in \mathbb{Z}$ for all $a$, there is an irreducible square integrable [[unitary representation|74BPYJNZTM]] $\pi(\varepsilon, \lambda)$ of the real [[unitary group|0R9R0Y1HDK]] of signature $\varepsilon$, with infinitesimal character $\lambda$ and lowest $K$-type $\lambda + \rho_n - \rho_c$. Each such representation is isomorphic to one $\pi(\varepsilon \circ s, \mu)$.

This is Harish-Chandra's classification of the [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees) (Acta Math. 116, 1966), with the lowest $K$-type of Hecht and Schmid (Invent. Math. 31, 1975).

Let $D$ be a datum with coefficient field $L$, let $P$ be a row side family and $S$ a set of spectral ties, and let $K_s$ be a number field with $L$ a $K_s$-algebra. An *indefinite realisation* $Q$ over these data is a real model of the rows at the place of signature changes. It is *normalised* if it has thirteen properties, among them a pin of the group record, a finite element $t_S$ and a pin of $t_S$. We say that $Q$ *extends* if there is an element $t$ of the finite group of the datum with a level conjugation condition and a row level match, and an evaluation tie holds at $t_S$ with some constant.

**Proposition 8.5.2 (The placement of the real realisation).** Assume the classification of the discrete series. Let $Q$ be a normalised indefinite realisation over $D$, $P$, $S$ and $K_s$. Assume that the embedding $\iota_E$ of $S$ is the identity. Then $Q$ extends.

Lean: `GlobalTheory.RowPlacementReal.placement_of_realisation_alt` (also `GlobalTheory.T.indefinite_scale_theta_nonvanishing_alt`, a second name).

*Proof.* There are two steps.

1. **The idempotent is real.** Let $e_0$ be the type idempotent of $D$. Each coefficient of $e_0$ is fixed by complex conjugation. For a monic $f$ over $\mathbb{F}_{g_k}$ with $f(0) \neq 0$, conjugation sends the coefficients of the idempotent $e(f)$ to the coefficients of $e(f(0)^{-1} f^{\mathrm{rev}})$, and this gives the claim.
2. **The placement.** [The placement of a row](/entry/exists-row-placement-finite-element-matches-levels/) gives the conclusion from the data of $Q$, step 1, the hypothesis on $\iota_E$, and three properties of the normalisation: the group pin, the finite element $t_S$ and its pin. In that proof one lemma finds $t$ with the level condition, a second gives the row level match, and the pin of $t_S$ moves both to $t_S$. Only the evaluation tie uses the classification of the discrete series. $\square$

The level condition and the row level match are also the premise of the pin of $t_S$. So the proposition only shows that such a $t$ exists.

Now the small bounds. Let $\mathcal{A}$ be a family class and $\sigma$ a selection of *point summands* for $\mathcal{A}$: each selected object is a point summand $b$, with a bundle $b.B$ and a realisation $b.B.Q$. A point summand is *visible* if its realisation extends. It is *primitive* if its rows are primitive with the constant $3$ and its types are separated.

The *small bounds* at a point summand, with constants $C$ and $C_H$, are three statements:

1. each word with the first weight condition is in the set of twisted places;
2. the isomorphism of the special endomorphisms holds;
3. the *passing condition* holds: there are a finite set $S$, a finite dimensional representation $\tau_s$ of the finite group $G$ of the datum over $L$ for each $s \in S$, and an integer $\bar n > 0$, with the passing condition of size $3$ for the family at $C$ and $C_H$.

We say that the small bounds hold *eventually with constants* along $\sigma$ on $\mathcal{A}$ if it is closed on the subclass $\mathcal{W}_3(\mathcal{A})$ that there is $C_0 \ge 0$ such that, for each $C \ge C_0$, eventually each selected point summand has the small bounds at $C$ and $C_H$.

**Lemma 8.5.3 (The passing condition at a totally complex field).** Let $D$ be a datum with size data $L$. Assume that the coefficient field of $D$ is totally complex, that the level ratio bound holds, that the first realness condition of size $3$ holds, and that the rows are primitive with the constant $3$. Then the passing condition holds for every $C$ and $C_H$.

Lean: `GlobalTheory.passIn3_at_realT_alt` (also `GlobalTheory.T.indefScale_theta_degree`, a second name).

*Proof.* This is [the passing condition from rows](/entry/pass-in3-of-rows/) applied to the characters of the datum, the realness condition, the primitive rows and the series labels of the types. The two identities it asks for, $d_e = 8fr/\min(g_0, g_1)$ and $\lambda = \log|G|$, hold by definition. $\square$

The passing condition from rows builds the representations $\tau_s$ from a good family with given characters and multiplicity one, and it takes $\bar n > 0$.

**Theorem 8.5.4 (Small bounds along a selection).** Let $\mathcal{A}$ be a family class and $\sigma$ a selection of point summands for $\mathcal{A}$. Assume that each selected point summand is visible and primitive. Then the small bounds hold eventually with constants along $\sigma$ on $\mathcal{A}$, with $C_0 = 0$.

Lean: `GlobalTheory.Fc.Ind.small_along_alt` (also `GlobalTheory.T.eventually_small_of_seeEx_primitive`, a second name).

*Proof.* Take $C_0 = 0$. Let $F$ be a family of the class and $C \ge 0$. The bound $4fr \le \min(g)$ for the family gives a threshold $x_0$, and at this threshold the level ratio bound holds with $0$. Let $b$ be a point summand selected at some $x > x_0$.

1. The first small bound is part of the definition of the bundle $b.B$.
2. The second small bound holds since $b$ is visible: the limit of the indefinite realisation at the scale gives the isomorphism.
3. The third small bound is the Lemma (The passing condition at a totally complex field). The coefficient field is totally complex for the datum, the level ratio bound holds past $x_0$, the realness condition holds for the bundle, and the rows are primitive since $b$ is primitive. $\square$

The separation of types is not used.

Now the definite row. For a predicate $\mathrm{DR}$ on bundles and constants, the *definite statement* $\mathrm{Def}_{\mathrm{DR}}(\mathcal{A}, \sigma)$ says: it is closed on $\mathcal{D}_3(\mathcal{A})$ that there is $C \ge 0$ such that, eventually along $\sigma$, each selected bundle $b$ has the nine constant bounds at $C$ and satisfies $\mathrm{DR}(b, C, C_H)$. The nine bounds are: the first weight bound, the covolume bound, the norm bound, the $L^6$ bound, the isomorphism bound, the multiplicity bound, the functional bound, the passing bound and the kappa bound. The *definite row* at $Q$ and $\Lambda$ is $\mathrm{Row}(Q, \Lambda, \mathrm{Def}_{\mathrm{DR}})$ with $\mathrm{DR}$ the [definite side condition](/step/definite-side-condition-def/).

**Theorem 8.5.5 (The definite row).** Assume the cover of the unitary dual by discrete series, the theory of Harish-Chandra modules, the rapid decay of [[cusp form|SV5EEBF861]]s, the Casselman-Wallach theorem and the classification of the discrete series. Assume the surjectivity onto $X$ and the lower bound for lambda. Let $Q$ be a slot and $\Lambda$ a linkage, and assume nine rows at $(Q, \Lambda)$: primitivity, divisor, goodness, weak geometric compatibility, covolume (an $L^3$ bound), functional, multiplicity, kappa and defect. Then the definite row at $(Q, \Lambda)$ holds.

Lean: `GlobalTheory.Fc.StageZeroRow.row_rRows_stage0_alt`.

*Proof.* There are six steps.

1. **Reduction.** It is enough to prove four rows: a row with five eventual bounds on a compatible selection of point summands, and the multiplicity, kappa and defect rows. Then take the largest of the six constants and the largest of the eight thresholds. The defect row is the definite side condition, so this part of the conclusion is a hypothesis.
2. **A compatible selection.** Join the first six rows by the second fact about rows of Section 1. The weak geometric compatibility row gives, by choice, a compatible selection $\tau$ of point summands. Its point summands satisfy the embedding condition, the class sum pin, the compatibility conditions and a further point condition.
3. **Point conditions.** The first four results on real groups, primitivity, the divisor row and goodness give the point conditions eventually, from the class sum pin. The divisor row first moves to the pieces of the family.
4. **Norm and $L^6$.** The surjectivity onto $X$ gives the norm bound from the further point condition. The lower bound for lambda gives the $L^6$ bound.
5. **Small bounds.** Each point summand of $\tau$ is primitive by the primitivity row. It is visible by the Proposition (The placement of the real realisation), which uses the classification of the discrete series. The Theorem (Small bounds along a selection) gives the isomorphism and passing bounds.
6. **Covolume and functional.** The $L^3$ bound and the functional bound are the covolume and functional rows. $\square$

**Remark 8.5.6 (Formalization).** The definite row is at [TupAllUsedAtPart.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TupAllUsedAtPart.lean#L46); the file is named after the helper `tupAllUsed_at_part_alt` at line 30, and the name says "stage 0" for no visible reason. Step 1 is `row_rRows_of_parts_alt`, step 3 is `eventually_pDiv_ties_of_class_sum_pin` with `p_div_at_piece_of_div3g` (line 43), and step 4 is `eventually_norm_bound_of_more_points` and `eventually_L6_bound_of_lamLow`; these are one line renamings of `evW_pRows_of_rows_alt`, `onto_at_chosen_alt` and `eventual_L6_of_lower_scalar_alt`. The nine bounds are the fields `w1`, `covol`, `onto`, `lamLow`, `seeIso`, `miStar`, `fun0`, `pass` and `kap`. The placement is at [PlacementOfRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacementOfRealisation.lean#L18); its second name `indefinite_scale_theta_nonvanishing_alt` mentions a theta series, a scale and a nonvanishing statement, and none of them occurs. In the same way the name `indefScale_theta_degree` of the passing lemma ([PassIn3AtRealTStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PassIn3AtRealTStatement.lean#L14)) mentions no theta series and no degree, and `eventually_small_of_seeEx_primitive` renames `small_along_alt` ([SmallAlong.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SmallAlong.lean#L15)). The proof of the passing lemma at [PassIn3AtRealT.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PassIn3AtRealT.lean#L17) passes the data `S`, `Del`, `h0` and `c` to `passIn3_of_rows`, which does not use them, and closes the two identities with `rfl rfl`. In `small_along_alt` the threshold comes from `four_f_r_le_min_g_family`, and the type separation `hp.2` is never used.
