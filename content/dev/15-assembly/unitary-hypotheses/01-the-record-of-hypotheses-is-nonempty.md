---
title: The record of hypotheses is nonempty
decls:
  - GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The record of hypotheses is nonempty

This section proves the main theorem of the chapter. Under the unitary group hypotheses, a rational row condition and three linked rows, the record of hypotheses of [the unitary hypotheses](/proof/unitary-hypotheses/) has an element. This is branch 1 of that node. The step [nonempty hypotheses](/step/nonempty-hyps/) applies it once, at one constant. The proof does no new mathematics. It collects the two other branches, the bundles of [the chapter on unramified exponents](/entry/large-unramified-exponent-bundles-exist-alt/), the closed link bound of Section 6 and the record of all rows of Section 2. First we fix the language of rows that the whole chapter uses.

We keep the language of [the open orbit](/entry/open0-of-unitary-group-hypotheses/). A *point* is a base $B$ with its columns, rows, stages and a core. A *slot* is a predicate on points. For slots $Q$ and $R$ we write $Q \wedge R$ for the slot of points in both. A *bundle* at a point is a set of data over the point, and a *linkage* $\Lambda$ is a relation between a context, a point, a real number and a bundle at the point. A *parameter set* $p$ has a scale. At this scale there are two slots, the built points $Q_p$ and the good points $Q'_p$, and a good point is built. There is also a bundle linkage $\Lambda_p$.

**Definition 8.1.1 (Linked rows).** Let $K$ be a property of bases and $Q$, $R$ slots. The *large base condition* $\mathrm{LB}(K, Q, R)$ says: eventually in the scale, for each base $B$ with property $K$, each point of $Q$ over $B$ is in $R$. Let $Q'$ be a slot and $r$ a statement about slots. We put

$$\mathrm{Lg}(K, Q, Q', r) \iff \exists R : \ \mathrm{LB}(K, Q, R) \ \text{ and } \ r(Q' \wedge R).$$

For a parameter set $p$ and a statement $r(S, \Lambda)$ about a slot and a linkage, $r$ is *linked at* $p$ if $\mathrm{Lg}(K_{P_x}, Q_p, Q'_p, S \mapsto r(S, \Lambda_p))$ holds. We write $\mathrm{Linked}_p(r)$. Here $K_{P_x}$ is a fixed property of bases.

**Remark 8.1.2 (The true slot).** Let $\top$ be the slot that holds at every point. Then $\mathrm{LB}(K, Q, \top)$ holds for every $K$ and $Q$, since each point is in $\top$. So $r(Q' \wedge \top)$ implies $\mathrm{Lg}(K, Q, Q', r)$. In this case $K$ and $Q$ play no role. Many rows of this chapter are proved in this way.

**Definition 8.1.3 (Rows).** A *family class* $\mathcal{A}$ is a predicate on families, as in [the closed bound](/step/closed-def/). A *selection* $\sigma$ for $\mathcal{A}$ picks a bundle $\sigma(F, x, i)$ for each family $F$ in $\mathcal{A}$, each $x$ above the threshold of $F$ and each index $i$ of $F$ at $x$. Let $Q$ be a slot, $\Lambda$ a linkage and $H(\mathcal{A}, \sigma)$ a statement. The *row* $\mathrm{Row}(Q, \Lambda, H)$ says: there is a property $E$ of bundles such that, eventually, each bundle at a point of $Q$ that $\Lambda$ links has $E$, and $H(\mathcal{A}, \sigma)$ holds for each family class $\mathcal{A}$ and each selection $\sigma$ of bundles with $E$.

Three facts about rows are direct from the definition. If $H(\mathcal{A}, \sigma)$ holds for every selection, the row holds with $E$ the true property. Two rows at the same $Q$ and $\Lambda$ give the row of $H \wedge H'$, with the property $E \wedge E'$. A row at $Q$ holds at each smaller slot.

**Definition 8.1.4 (Norm rows).** For a family class $\mathcal{A}$ let $\mathcal{D}_3(\mathcal{A})$ be the subclass of the families of $\mathcal{A}$ that are smooth, have good twists, carry a chosen datum with constant $3$ and satisfy two size conditions. This is the class of the record of hypotheses in [the step on the record](/step/hyps-alt-def/). For a predicate $N$ on family classes, the *norm row* is

$$\mathrm{NRow}(Q, \Lambda, N) = \mathrm{Row}\bigl(Q, \Lambda, (\mathcal{A}, \sigma) \mapsto N(\mathcal{D}_3(\mathcal{A}))\bigr).$$

Let $N_L(\mathcal{C})$ be the closed bound $\mathrm{Closed}(\mathcal{C}, \mathrm{LinkN})$ for the link inequality of Section 6, and let $B_{23}(\mathcal{C})$ be the closed bound $\mathrm{Closed}(\mathcal{C}, \mathrm{B}_{2,3})$ for the bound at the primes $2$ and $3$ of [the unitary hypotheses](/proof/unitary-hypotheses/).

**Definition 8.1.5 (The record of all rows).** Let $K$ be a property of bases, $Q$ and $Q'$ slots, $\Lambda$ a linkage, $N$ a predicate on family classes and $\mathrm{DR}$ a predicate on bundles and constants. The *record of all rows* has twenty six fields. Each field is $\mathrm{Lg}(K, Q, Q', S \mapsto \rho(S, \Lambda))$ for one row statement $\rho$. The rows are:

1. the class count row, the row of a twisted operator on the Hecke module, the instance row and the second complement row;
2. six rows on period entries, twisted points, ties and column valuations, and the row of admissibility at generator places;
3. the real bound row and the twist row;
4. the five open rows for primitivity, the lambda prime, the divisor, the decomposition point and the selection jump;
5. the three Siegel-Weil rows (a loop bound, an off-diagonal bound and a frame bound), the service row and the row of projections onto the period space;
6. the count row;
7. the definite row with the predicate $\mathrm{DR}$;
8. the norm row $\mathrm{NRow}(S, \Lambda, N)$.

The record of hypotheses has one field for each of these rows, and Part 2 of the chapter reads the fields off the rows.

Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/) and let $c \in \mathbb{R}$. Let $p(h_L, c)$ be the parameter set of dependence of [the open orbit](/entry/open0-of-unitary-group-hypotheses/). Let $A$ be a property of extensions that holds eventually. Let $p_A(h_L, c)$ be the parameter set of the extension with the property $A$ over the extension with origin, with the empty $S$-extension and the closure of the trivial geometry. An element of this extension is a tuple. Its first part has a first part that is an element of the extension with list of $p(h_L, c)$. So $p_A(h_L, c)$ is a stronger parameter set than $p(h_L, c)$.

**Theorem 8.1.6 (The record of hypotheses is nonempty).** Assume the [unitary group hypotheses](/step/unitary-group-third-place-hypotheses-def/) and the rational row condition. Let $h_L$, $c$ and $A$ be as above. Assume:

1. the closed bound at two and three is linked at $p(h_L, c)$, that is $\mathrm{Linked}_{p(h_L,c)}\bigl(\mathrm{NRow}(\cdot, \cdot, B_{23})\bigr)$;
2. the functional row is linked at $p_A(h_L, c)$;
3. the covolume row is linked at $p_A(h_L, c)$.

Then the record of hypotheses with the norm predicate $N_L$ and the [definite side condition](/step/definite-side-condition-def/) has an element.

Lean: `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`.

*Proof.* Write $p = p(h_L, c)$ and $p_A = p_A(h_L, c)$. The proof has seven steps.

1. **Bundles.** [The theorem on bundles of large unramified exponents](/entry/large-unramified-exponent-bundles-exist-alt/) applies to the unitary group hypotheses, the rational row, $h_L$, $c$ and $A$. It gives three facts: a Siegel mass ratio for CM data, the membership condition for $p_A$, and bundles with a large base condition at $p_A$. This is the only use of the rational row condition.
2. **Third layer inputs.** [The third layer inputs](/entry/hyps-e-third-layer-ser-n-of-geometric-galois/) apply to two parts of the unitary group hypotheses, the non-endoscopic hypotheses and the Galois hypotheses. They give the published inputs of the third layer and a local Selmer input.
3. **The other branches.** [Branch 2](/entry/onto-x-and-lam-low-of-unitary-group-hypotheses-prime/) gives the surjectivity onto $X$ and the lower bound for lambda. [Branch 3](/entry/open0-of-unitary-group-hypotheses/) gives the twelve open parameter statements at $p$.
4. **The link bound.** [The closed link bound](/entry/final-alt-alt/) of Section 6 takes the link field of the hypotheses, the two inputs of step 2, the Galois hypotheses, the depth zero support, local finiteness, local Tate duality, the local Euler characteristic, $h_L$, $c$ and hypothesis 1. It gives $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, N_L))$.
5. **The stronger parameters.** A linked statement at $p$ moves to $p_A$ along the projection of the extensions above. This is a general transfer from a weaker extension to a stronger one. It moves the open parameter statements of step 3 and the norm row of step 4 to $p_A$.
6. **All rows.** [The theorem on all rows](/entry/all-rows-of-open0-alt/) of Section 2 takes global Artin reciprocity, the convergent Siegel-Weil formula, five named results on real groups, the two estimates of step 3, $h_L$, $N_L$, the open statements and the norm row at $p_A$, and hypotheses 2 and 3. It gives the record of all rows at $p_A$ with $N_L$ and the definite side condition.
7. **The record.** [The record from all rows](/entry/nonempty-hyps-of-all-rows-alt/) builds an element from the record of step 6. Its other inputs are the facts of step 1, four theorems with no hypothesis (on thin scales, on the decay of a gap, on finite dimensional rows and on positivity at the type primes), three consequences of the Siegel-Weil formula (a row bound, a main equality and a volume ratio) and the genus mass at $2$.

Every hypothesis is used. Hypotheses 2 and 3 enter in step 6, and hypothesis 1 in step 4. $\square$

**Remark 8.1.7 (Formalization).** The theorem is at [HypothesesNonemptyOfUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L41). The record of all rows is `AllRowsAlt` ([AllRows.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AllRows.lean#L12)), with fields `hn4`, `jOn`, `hInstR`, `aC2`, `aP10`, `aAtG`, `aPt0`, `aPtTw`, `aPer0`, `aPerTw`, `tie`, `hRB`, `hTw`, `hPA`, `hLamP`, `hDivG`, `hDcPtG`, `selJ`, `sLp`, `sO`, `hServ`, `zL`, `hTF`, `c30`, `rRows` and `nRest`; `Lg1` is in [GlobalTwisting/AllRows.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/AllRows.lean#L15), and the true slot lemma is `largeBaseProperty_true` in [EventuallyAllScaleContextsAndOfBoth.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/EventuallyAllScaleContextsAndOfBoth.lean#L91). The transfer of step 5 is `GlobalTheory.Glob.open_and_linked_of_stronger_extension_alt`, called with the projection `fun … x => ⟨x.1.1⟩`; its second half moves the open statements and its first half the norm row. Hypothesis 1 is redundant: `boundAtTwoThree_linked_of_recT` in [At23OfAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/At23OfAll.lean#L24) proves it from the link field `P.nLink`, and the top caller gets it that way. Step 7 uses the field `siegelWeilUnitaryConvergent2`, one of two fields with the last name `SiegelWeilUnitaryConvergent`. The words "unramified exponents" occur in no hypothesis and no conclusion.
