---
title: The period identity for a true package
decls:
  - GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt_alt
  - GlobalTheory.Fam.miAt_of_truePack_alt_alt
  - GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt
  - GlobalTheory.Fam.miStar2_of_allTrue_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The period identity for a true package

This section proves the period identity of [the previous section](/entry/fam-mi-star-row-alt-alt/) for one real package. The package must be true, its datum must have $r_S \geq 1$, and a projection of the ramified vectors must be nonzero. The proof reduces the period identity to the family conditions of [the next section](/entry/fam-all-q-of-all-true-alt/) and to a theorem proved later in this chapter, [the period identity from the family conditions](/entry/mi-star2-of-pu-nz/). The result is used at each good linked bundle in [the Theorem on point conditions](/entry/fam-mi-star-row-alt-alt/).

We fix the objects of this part of the chapter. A *datum* $D$ carries a CM extension $E/F$ of number fields, hermitian spaces $X_j$ and $Y_j$ over $E$ for the levels $j = 0, 1, \dots, m$, with a top space $X'$, a set of words $u$, and integers $m$ and $r_S$. For a hermitian space $V$ of $D$ we write $G(V)$ for the adelic [[unitary group|0R9R0Y1HDK]] of $V$ and $G_f(V)$ for its finite part, the kernel of the projection to the archimedean component, as in [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups). Most data in this chapter are built from base data $B$ and tower data $(I, l, Z)$; we write $D = I(l, Z)$ for the datum they give.

A *real package* $W$ over $D$ is the data of a theta correspondence over $D$: a coefficient space $X_W$ with its maps $e_V$ and $s$ as in [the previous section](/entry/fam-mi-star-row-alt-alt/), a set $T$ of twist indices $t$ with a base index $\mu_0$, a level datum $R_W$ with a set $Q(t)$ of places of $E$ for each $t$ and a set $P_g$ of places, a character $\psi$ of $\mathbb{A}_F$, and the columns, tuples and periods of the package. We use these parts as we meet them and do not unfold the rest.

**Definition 4.3.1 (Family conditions on a package).** Let $D = I(l, Z)$ and let $W$ be a real package over $D$. The *family conditions on* $W$ are six conditions: package hypotheses on $W$ (the conditions $\mathrm{pk}$), the validity of the real package ($\mathrm{tr}$), conditions on the geometric families of $W$ ($\mathrm{tq}$), a standard form of the twisted columns ($\mathrm{tw}$), a level condition ($\mathrm{lev}$) and a recursion condition ($\mathrm{rc}$). A real package is *true* if its datum has the form $I(l, Z)$ and it satisfies the family conditions.

**Definition 4.3.2 (Nonzero projection).** A datum $D$ has *nonzero projection* if for each word $u$ there is a ramified vector $\varphi$ of $u$ with $P_u(\varphi) \neq 0$, where $P_u$ is the projection of the previous section and $\varphi$ is read as a vector of the coefficient space of $u$.

**Theorem 4.3.3 (Period identity for a true package).** Assume the finiteness theorem, the rapid decay of cusp forms, the discrete series cover, the Harish-Chandra modules, the Casselman-Wallach theorem, the unramified Howe duality, the Weil representation of a unitary pair, the Weil-Siegel formula, the Siegel-Weil convergence, the doubling method, the unramified doubling, the classification of discrete series and strong approximation for $\mathrm{SU}$. Let $W$ be a true real package over a datum $D$ with $r_S \geq 1$ and with nonzero projection. Then the coefficient space of $W$ satisfies the period identity $\mathrm{MI}^*_2$.

Lean: `GlobalTheory.Fam.miAt_of_truePack_alt_alt` (also `GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt_alt`, a second name).

*Proof.* Since $W$ is true, $D = I(l, Z)$ and $W$ satisfies the family conditions. Then [the Theorem on family conditions](/entry/mi-star2-of-all-true-alt-alt/) below applies. $\square$

The next theorem needs one more condition on the datum. A datum $D$ is *onto at all levels* if a family of theta maps of $D$, one at each level, is onto. We do not unfold this condition; we only use that it follows from the published statements, through [the doubling method](/learn/theta/#the-doubling-method).

**Theorem 4.3.4 (Period identity from the family conditions on a package).** Assume the thirteen published statements of the previous theorem. Let $D = I(l, Z)$ and let $W$ be a real package over $D$ that satisfies the family conditions. Assume $r_S \geq 1$ and that $D$ has nonzero projection. Then the coefficient space of $W$ satisfies the period identity $\mathrm{MI}^*_2$.

Lean: `GlobalTheory.Fam.miStar2_of_allTrue_alt_alt` (also `GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt`, a second name).

*Proof.* We take four steps.

1. The first eleven published statements, from the finiteness theorem to the unramified doubling, give that $D$ is onto at all levels, by a result of another chapter.
2. The rapid decay of cusp forms, the discrete series cover, the Harish-Chandra modules, strong approximation, the family conditions on $W$, $r_S \geq 1$ and step 1 give the conditions $\mathrm{FAC}(W)$ of [the Theorem on family conditions](/entry/fam-all-q-of-all-true-alt/) of the next section.
3. The package hypotheses of $W$ contain a bottom hypothesis, and the recursion condition gives one recursion datum. From these, a lemma gives the served condition on the places of $W$: for each prime $w$ of the field of coefficients and each rational prime $p$ that lies under a place of the twist set $Q(\mu(w))$, we have $p \notin w$. In fact the lemma proves this condition from the level and tuple data of the package alone, without the two inputs.
4. [The Theorem on the period identity from the family conditions](/entry/mi-star2-of-pu-nz/), with the classification of discrete series, the rapid decay of cusp forms and the Harish-Chandra modules, the bottom hypothesis and the level part of the package hypotheses, step 2, step 3 and the nonzero projection, gives $\mathrm{MI}^*_2$. $\square$

So the published statements enter at three places: in the surjectivity of step 1, in the construction of the families of step 2, and in the local theory of step 4. The rest of this part of the chapter proves step 2.

**Remark 4.3.5 (Formalization).** The theorems are at [MainTheoremFromPublishedResultsAltAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAltAlt.lean#L21) and [MainTheoremFromPublishedResultsAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAlt.lean#L23), with second names at lines 38 and 37. The names "main theorem from published results" do not describe the statements. `TruePackAlt` is an inductive predicate with one constructor, so the first proof is `cases` on it; it is defined in [TruePack.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePack.lean#L13), where `RealPackageCondition W` is the period identity of `packageCoefficientSpace W`. `PuNZ` is in [PairForm.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PairForm.lean#L143). Step 1 is `ontoAll_of_theta_doubling`, step 2 is `apply true_geometry_family_row_data_alt <;> assumption`, and step 3 is `servedQ_of_bot_alt` of [ServedQOfBot.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServedQOfBot.lean#L20), which ignores its two hypotheses `BottomHypotheses W` and `IndefiniteRealisationRecursion W.Q` and returns `served' W` of [NotMemQBase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NotMemQBase.lean#L47); `served'` uses `W.Q.charW.base.lev` and `W.Q.charW.tup`. We did not unfold `RealPackAlt`, `AllFamilyConditions` beyond its six fields, or `OntoAll`. The statement "onto at all levels" is given here only by its name.
