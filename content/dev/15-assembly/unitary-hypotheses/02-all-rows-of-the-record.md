---
title: All rows of the record
decls:
  - GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt
  - GlobalTheory.T.period_entries_tie_and_level_valuations_at_built
  - GlobalTheory.Fc.six_rows_at_member_alt
  - GlobalTheory.Fc.row_aAtG_at_built_alt
  - GlobalTheory.CountRow.row_counts_of_ties_alt
  - GlobalTheory.CountRowByName.row_counts_of_labels_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## All rows of the record

This section proves that the twenty six rows of the record of all rows hold at a parameter set that satisfies the open parameter statements. The [main theorem](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of Section 1 uses it in step 6. Most rows come from the twelve open statements of [the open orbit](/entry/open0-of-unitary-group-hypotheses/), in one step or with no step. Seven rows need no hypothesis, and three of them are proved here. The count row is proved here from the Siegel-Weil formula. The three Siegel-Weil rows, the service row and the definite row have long proofs, and Sections 3, 4 and 5 give them.

We use the language of rows of Section 1. Fix a family of slots $\mathcal{S}$ with built points $Q_{\mathcal{S}}$ and good points $Q'_{\mathcal{S}}$, and a linkage $\Lambda$.

**Lemma 8.2.1 (Six rows at the good points).** For each family of slots $\mathcal{S}$ and each linkage $\Lambda$, six statements $\mathrm{Lg}(K_{P_x}, Q_{\mathcal{S}}, Q'_{\mathcal{S}}, S \mapsto X(S, \Lambda))$ hold. Each row $X$ has the form $\mathrm{Row}(S, \Lambda, (\mathcal{A}, \sigma) \mapsto \mathrm{Closed}(\mathcal{W}_3(\mathcal{A}), P))$, where $\mathcal{W}_3(\mathcal{A})$ is a subclass of $\mathcal{A}$ and $P$ is a property of a family. The six properties $P$ are:

1. eventually, the sixth conclusion of the period identity holds at each point of the family and each word $u$;
2. eventually, the twisted point is integral at each point and its twist;
3. eventually, the period class sum of Weyl type holds at each point;
4. eventually, the twisted period is admissible at each point and its twist;
5. the second layer conditions at the real place hold for the family;
6. eventually, the sharp fifth conclusion and the twisted column bound hold at each point and each word $u$.

Lean: `GlobalTheory.T.period_entries_tie_and_level_valuations_at_built` (also `GlobalTheory.Fc.six_rows_at_member_alt`, the proof).

*Proof.* Take $R = \top$. By the Remark on the true slot of Section 1, the large base condition holds. Every good point is built, and a built point has columns. So each point of $Q'_{\mathcal{S}} \wedge \top$ has columns. [The column valuations at bundle points](/entry/level-prime-column-valuations-bundle-points-over-columns/) and five more lemmas each prove one of the six rows for every slot whose points have columns, every bundle type and every linkage. Apply them to $Q'_{\mathcal{S}} \wedge \top$ and $\Lambda$. $\square$

The next row bounds the valuations of period coordinates at the places over the generator primes. For a datum $D$ with size data $L$ and error data, let $v_w$ be the valuation at a place $w$, let $v_{ij}(u, w)$ be the error valuations for the lifts $j$, and let $c_{\mathrm{err}}(D, L)$ be the error constant.

**Lemma 8.2.2 (Admissibility at generator places).** Let $\mathcal{S}$ be a family of slots whose real datum is the standard one, and let $\Lambda$ be a linkage. Then $\mathrm{Lg}(K_{P_x}, Q_{\mathcal{S}}, Q'_{\mathcal{S}}, S \mapsto \mathrm{Row}(S, \Lambda, H))$ holds, where $H(\mathcal{A}, \sigma)$ says: it is closed on $\mathcal{W}_3(\mathcal{A})$ that there is a constant $C_1$ with two properties. First, eventually, at each index of the family, for $i \in \{0, 1\}$, each place $w$ over the generator of index $i$, each word $u$ with $T(u)$ prime to the residue characteristic of $w$, and each used tuple, the period coordinate is the image of some $y \in L$ with $y = 0$ or

$$v_w(y) \ge -\sum_j v_{ij}(u, w) - C_1\, c_{\mathrm{err}}(D, L).$$

Second, the size of the family is bounded at the type primes with $C_1$.

Lean: `GlobalTheory.Fc.row_aAtG_at_built_alt`.

*Proof.* Take $R = \top$, so the large base condition holds. [The row at bundle points of true columns](/entry/holds-at-bundle-points-of-true-columns/) reduces the row to one claim. Each good point has a part at which a *pin* holds for each tuple $a$: for each word $u$, a linear isomorphism from the space of the period at $u$ and $a$ to the ambient space at $a$, with four compatibilities. A good point is built, so it carries a built datum $b$, and $b$ gives the part. The real datum of $b$ is the standard one by hypothesis. For the standard real datum, the period map matches the row forms, and this gives the pin. $\square$

Now we turn to the counts. The count row rests on one published input.

**Definition 8.2.3 (The convergent Siegel-Weil formula).** Let $E/F$ be a CM extension and $J$ a nondegenerate [[Hermitian form|8NJ7XY6F1S]] of size $M$ over $E$. The *convergent Siegel-Weil formula* says two things. The adelic [[unitary group|0R9R0Y1HDK]] of $J$ has a fundamental domain for its rational points of finite Haar volume. For $2n < M$, each nondegenerate hermitian $T$ of size $n$ and each factorizable test function $\Phi$, the mean over the fundamental domain of the theta sum of $\Phi$ over the vectors with Gram matrix $T$ is $g_\infty(T) \prod_v g_v(T)$. Here $g_\infty$ and $g_v$ are the densities of the push forward of local measures by the Gram map.

This is the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) for one Fourier coefficient in Weil's convergent range (Weil, Acta Math. 113, 1965).

The *label row* at a slot $Q$ and a linkage $\Lambda$ is the row whose statement holds at every selected bundle point $D$: there are a Hida setting $X$, a good operator $G$ and a linear isometry $\iota$ that satisfy three ties, an automorphic tie, a row dictionary tie and a label tie.

**Proposition 8.2.4 (The count row).** Assume the convergent Siegel-Weil formula. Let $Q$ be a slot and $\Lambda$ a linkage, and assume the label row at $Q$ and $\Lambda$. Then there are constants $c_{30}$ and $c_{Ic} > 0$ with these properties. For every family, $0 \le C$ and $2(C_{YL} + 1) \le A$ for two constants $C$ and $A$ of the family. The row at $Q$ and $\Lambda$ holds for the statement: on $\mathcal{D}_3(\mathcal{A})$, the point count of the class holds with the constants, and it is closed that eventually each point has rows $A$ with an injective good label count, the joins of all rows, and the count of all rows with the error $\varepsilon(c_{Ic}, r, f)$.

Lean: `GlobalTheory.CountRow.row_counts_of_ties_alt`.

*Proof.* [The count constants from Siegel-Weil](/entry/count-constants-of-siegel-weil/) give $c_{30}$, the bounds on $C$ and $A$, and the point count for every family. The irreducibility row for concrete automorphic data, with the finite dimension of the rows, gives $c_{Ic} > 0$ and a map. For a class whose families satisfy the size condition, the map turns the three ties into the second statement. Keep the property $E$ of the label row. For a selection $\sigma$, the first statement holds since it holds for every family. The second holds by the map on $\mathcal{D}_3(\mathcal{A})$: the size condition holds in the class, and the ties hold at the selected points by the label row. The threshold of the eventual statement is $0$. $\square$

**Corollary 8.2.5 (The count row, linked).** Assume the convergent Siegel-Weil formula. Let $K$ be a property of bases and $Q, Q'$ slots. If the label row satisfies $\mathrm{Lg}(K, Q, Q', \cdot)$, then the count row satisfies $\mathrm{Lg}(K, Q, Q', \cdot)$.

Lean: `GlobalTheory.CountRowByName.row_counts_of_labels_alt`.

*Proof.* Keep the slot $R$ and the large base condition. This is the Proposition (The count row) applied to the slot $Q' \wedge R$. $\square$

Let $p$ be a parameter set built from an extension, an $S$-extension and a geometry over $h_L$. The *functional row* and the *covolume row* are the rows of [the step on nonempty hypotheses](/step/nonempty-hyps/), and the covolume row is an $L^3$ bound.

**Theorem 8.2.6 (All rows from the open statements).** Assume global [[Artin reciprocity|7938EKMMVR]], the convergent Siegel-Weil formula, the cover of the unitary dual by discrete series, the theory of Harish-Chandra modules, the rapid decay of cusp forms, the Casselman-Wallach theorem, the classification of the discrete series, the surjectivity onto $X$ and the lower bound for lambda. Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/), let $p$ be a parameter set over $h_L$, and let $N$ be a predicate on family classes. Assume that $p$ satisfies the twelve open parameter statements, and that the covolume row, the functional row and the norm row of $N$ are linked at $p$. Then the record of all rows holds at $K_{P_x}$, $Q_p$, $Q'_p$, $\Lambda_p$, $N$ and the [definite side condition](/step/definite-side-condition-def/).

Lean: `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt`.

*Proof.* We give each row of the record.

1. **Copied.** The rows of primitivity, the lambda prime, the divisor, the decomposition point and the selection jump are open statements. The norm row is the hypothesis on $N$.
2. **One step from an open statement.** The row of the twisted operator and the projection row follow from the primitivity row. The twist row follows from the tie row. The count row follows from the label row by the Corollary (The count row, linked).
3. **No hypothesis.** The class count row and the second complement row hold at the constructed points. The admissibility row is the Lemma (Admissibility at generator places), since the real datum of $p$ is the standard one by definition. The Lemma (Six rows at the good points) gives six rows.
4. **Siegel-Weil.** The volume ratio of the Siegel-Weil formula gives the instance row. [The three Siegel-Weil rows](/entry/lg1-s-lp-s-o-h-tf/) of Section 3 give the loop, off-diagonal and frame rows.
5. **Real groups.** The real bound row holds for every slot and linkage by the cover by discrete series, the theory of Harish-Chandra modules, rapid decay and the Casselman-Wallach theorem.
6. **Artin reciprocity.** A bundle linked by $\Lambda_p$ has its reciprocity record linked by the reciprocity linkage of $p$, by the definition of $\Lambda_p$. Then [the service row](/entry/h-serv-of-link-r/) of Section 4 gives a row at $Q'_p$, and the true slot puts it in linked form.
7. **Definite rows.** Join nine rows into one linked row: primitivity, divisor, goodness, weak geometric compatibility, covolume, functional, multiplicity, kappa and defect. The large base conditions join, and each row moves to the smaller slot. Then [the definite rows](/entry/row-r-rows-stage0-alt/) of Section 5 give the definite row from this row, the five results on real groups and the two estimates.

These are the twenty six rows. $\square$

**Remark 8.2.7 (Formalization).** The theorem is at [LinkROfIsLinked.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L50); the file is named after the helper `linkR_of_isLinked'` at line 45, which is step 6. Step 7 joins the rows with `forall_linked_bundles_and_alt`, a copy of `RowL.and`. Steps 2 and 3 use `row_jOn_of_row_hPA_alt`, `zL_of_hPA`, `row_hTw_of_tie_alt`, `classCountBound_paramsLambda_constructedPoints`, `divisionSecondComplement_constructedPoints`, `row_hInstR_of_hU` and `row_hRB_univ_alt`; we did not unfold the rows they prove, so we do not know which are trivial. The predicate $N$ is free and the caller sets $N = N_L$. The six rows lemma at [SixRowsAtMemberStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMemberStatement.lean#L12) renames [SixRowsAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L11); its names say "at built" and "at member", but no membership enters and the built slot plays no role. The admissibility row at [RowAAtGAtBuilt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowAAtGAtBuilt.lean#L10) ignores the selection and the linkage. The count row at [RowCountsOfTies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowCountsOfTies.lean#L12) takes the threshold $x_0 = 0$ at line 21, and it drops the constant $c_{Ic}$ and the bound $c_{Ic} \le c$ that `count_constants_of_siegelWeil` also gives. The linked form at [RowCountsOfLabels.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowCountsOfLabels.lean#L13) is one term.
