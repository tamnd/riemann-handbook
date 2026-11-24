---
title: The twelve open parameter statements
decls:
  - GlobalTheory.T.open0_of_unitary_group_hypotheses
  - GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twelve open parameter statements

This section proves the main theorem of the chapter: under the unitary group hypotheses, the parameter set of dependence satisfies twelve open parameter statements. Each statement says that one row statement holds on the bundles that are linked to the parameter set. Eleven of the rows come from results proved in other chapters, and the proof below says where each one comes from. The multiplicity row comes from [the Theorem on multiplicity rows](/entry/main-theorem-published-inputs-third-alt-alt/) of the next section, and the rest of the chapter proves that theorem. The main theorem is item 7 of the step [nonempty hypotheses](/step/nonempty-hyps/), and it is branch 3 of [the unitary hypotheses](/proof/unitary-hypotheses/).

We keep the language of rows of [the unitary hypotheses](/proof/unitary-hypotheses/). A *parameter set* $p$ has a scale $s(p)$. At this scale there are two predicates on bundles: a bundle can be *built* and it can be *good*. We write $Q_p$ and $Q'_p$ for them. There is a *bundle linkage* $\Lambda_p$, a relation between a context $K$, a built bundle $\beta$, a real number $c$ and a bundle condition $b$ of $\beta$. A *row statement* $r$ takes a predicate $S$ on bundles and a linkage and gives a proposition $r(S, \Lambda)$.

**Definition 4.1.1 (Linked rows).** Let $p$ be a parameter set and $r$ a row statement. We say that $p$ is *linked at* $r$ if there is a predicate $R$ on bundles such that the large base condition $\mathrm{LB}(K_{P_x}, Q_p, R)$ holds and $r(Q'_p \wedge R, \Lambda_p)$ holds:

$$\mathrm{Linked}_p(r) \iff \exists R : \ \mathrm{LB}(K_{P_x}, Q_p, R) \ \text{ and } \ r(Q'_p \wedge R, \Lambda_p).$$

Here $K_{P_x}$ is a fixed constant of the large base condition. So a linked row is a row statement that holds on the good bundles after we remove a set of bundles of small base.

**Definition 4.1.2 (Open parameter statements).** A parameter set $p$ satisfies the *open parameter statements* if it is linked at each of the following twelve row statements: the primitivity row, the lambda prime row, the divisor row, the decomposition point row, the selection jump row, the tie row, the label row, the good row, the weak geometric compatibility row, the multiplicity row, the kappa row and the defect row.

The multiplicity row is defined in the next section. The defect row is the row form of the definite side condition, as in [the unitary hypotheses](/proof/unitary-hypotheses/). The other ten rows are defined and proved in other chapters of this volume, and we use them only through the results that prove them.

**Definition 4.1.3 (Unitary group hypotheses).** The *unitary group hypotheses* are a list of published statements, which we take as given from [the literature](/proof/literature/). The list contains: a cover of the unitary dual by discrete series, the theory of Harish-Chandra modules, the Casselman-Wallach theorem, the Weil representation of a unitary dual pair, the existence of discrete series, the finiteness theorem of Harish-Chandra, the rapid decay of cusp forms, the Weil-Siegel formula for unitary groups, two forms of the convergence of the Siegel-Weil integral for unitary groups, the doubling method for local zeta integrals, the unramified doubling for the general linear group, the classification of discrete series, strong approximation for the special unitary group, analyticity of Harish-Chandra, the trace class property of cusp forms, the factorization of Dixmier and Malliavin, the factorization of Flath, the polynomial ring of Zelevinsky, the geometric lemma, green cuspidal and green regular characters, and the ray class field statement.

Let $h_L$ be a recursion datum for the local Langlands correspondence and let $c \in \mathbb{R}$. The *parameter set of dependence* $p(h_L, c)$ is the parameter set of the extension choice $N(h_L, c)$ given by the extensions with list at the constant $c$, with the empty $S$-extension and the closure of the trivial geometry.

**Theorem 4.1.4 (The open parameter statements).** Assume the unitary group hypotheses. Then for each recursion datum $h_L$ and each $c \in \mathbb{R}$, the parameter set $p(h_L, c)$ satisfies the twelve open parameter statements.

Lean: `GlobalTheory.T.open0_of_unitary_group_hypotheses` (also `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt`, the proof).

*Proof.* Write $p = p(h_L, c)$ and $N = N(h_L, c)$. We first note two facts. (a) Each extension with list carries an extension with law: the first component of an extension with list is one. (b) At each witness point of the scale of $p$, the bundle law holds, since it is one of the components of the witness. Now we prove the twelve rows, in an order in which each one uses only the rows before it.

1. The primitivity row and the decomposition point row hold at the parameter set of every extension choice. No hypothesis is needed.
2. The tie row follows from the discrete series cover, the Harish-Chandra modules, the Casselman-Wallach theorem, the Weil representation, the existence of discrete series, the finiteness theorem and the rapid decay of cusp forms, together with fact (a).
3. The selection jump row follows from the same seven statements and from the primitivity, decomposition point and tie rows.
4. [The Theorem on multiplicity rows](/entry/main-theorem-published-inputs-third-alt-alt/) of the next section applies to $N$, the empty $S$-extension and the trivial geometry. It needs fourteen published statements. Thirteen of them are in the unitary group hypotheses. The fourteenth, the unramified Howe duality, is [the Theorem](/entry/howe-unram-holds/) proved in another chapter. It gives two linked rows: the period identity at all points, and the multiplicity row.
5. The divisor row follows from seven statements of the list, from fact (b), and from the first row of step 4.
6. The lambda prime row follows from twelve statements of the list: the Weil representation, the existence of discrete series, the finiteness theorem, the rapid decay of cusp forms, analyticity, classification of discrete series, the trace class property, the two factorizations, the polynomial ring of Zelevinsky, the geometric lemma and green cuspidal.
7. The kappa row follows from thirteen statements of the list and from the lambda prime row.
8. Green regular characters give the green statement for the general linear groups over finite fields. With the polynomial ring of Zelevinsky and fact (a), this gives two rows. The second is the good row. The first gives the label row by [the Theorem on labels](/entry/good-ft-entries-alt-alt/).
9. The weak geometric compatibility row follows from the ray class field statement, fact (a), the divisor row and the tie row.
10. The defect row follows from the Weil representation, the existence of discrete series, the finiteness theorem and the rapid decay of cusp forms, by [the Theorem on the defect row](/entry/weil-unitary-entries-prime/).

The twelve rows are the twelve open parameter statements. $\square$

So the deep part of the theorem is step 4. The rest of the chapter proves it.

**Remark 4.1.5 (Formalization).** The theorem is at [OpenOrbitOfUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L75), and its proof only passes the hypotheses to the second name at line 39. The words "open orbit" and "unramified exponents" in the names do not occur in any hypothesis or conclusion; the name `open0` matches the structure `OpenParameterStatements`. The hypothesis `HoweUnram` of step 4 is not a field of the unitary group hypotheses; it is supplied by the theorem `GlobalTheory.Hk3.howeUnram_holds` (line 51). The list contains two different statements with the same last name `SiegelWeilUnitaryConvergent`, the fields `siegelWeilUnitaryConvergent` and `siegelWeilUnitaryConvergent2`. The theorem is stated at `parametersOfDependence hL cDep`, and the rows are proved at `parametersOfExtension (extensionWithList hL cDep) SExt.none (geoCl anyGeometry)`; the two agree by definition. We did not unfold `GlobalTheory.GLq.Green` (the green statement of step 8, from `green_of_regular`), `RecTExists`, `IsBuiltE`, `IsGoodE`, `KPx`, `LargeBaseCondition`, `BundleLinkage` or the row statements other than the multiplicity row. The results of steps 1 to 3 and 5 to 9 are `linkedAt_hPA_prmR`, `linkedAt_hDcPtG_prmR`, `linkedAt_tie_of_nonempty_extensionWithLaw`, `entries_combined_real_alt`, `bk_law_entries_alt`, `real_group_inputs_combined_alt_alt`, `harish_chandra_inputs_combined_alt_alt`, `linked_bundles_good_of_local_langlands_alt_alt` and `linkedAt_geometricWeakTies_of_tie`; we did not open them.
