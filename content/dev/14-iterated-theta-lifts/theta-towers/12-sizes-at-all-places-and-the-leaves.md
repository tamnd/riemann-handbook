---
title: Sizes at all places and the join of the leaves
decls:
  - GlobalTheory.T.sum_size_bound_all_places
  - GlobalTheory.SumSize.Join.sum_size_finite_away_archimedean_combined
  - GlobalTheory.T.finDatK_of_theta_inputs
  - GlobalTheory.FunDat.finDatK_alt
  - GlobalTheory.T.field_pair_comparison
  - GlobalTheory.FPair.lift_splits_locally
  - GlobalTheory.BigTop.Fun.fun0Fit_of_leaves_alt
  - GlobalTheory.T.leafMinimalMass_of_setAt
  - GlobalTheory.BigTop.Fun.LeafMMTie.mm_tie_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sizes at all places and the join of the leaves

The proof of the slope bound in [Section 3.9.5](/entry/fitted-function-at-zero-close-alt/) uses bounds on the sums of sizes at the finite places, away from the level and at the infinite places, and it joins sixteen leaf bounds into one inequality. This section states the bounds on sizes, shows how they are assembled from bounds on single factors, and states the joining lemma together with one leaf, the leaf of minimal mass.

The bounds live on a number field $L$ of the datum $D$, with an embedding into $\mathbb C$. For a finite place $w$ of $L$, $v_w$ is its valuation and $\ell_w$ the logarithm of its norm. A loss function of total $B$ is a function $d$ on the finite places with $d(w) \ge 0$, $d(w) = 0$ for all but finitely many $w$, and $\sum_w \ell_w\, d(w) \le B$. A complex number $z$ has loss at most $a$ at $w$ if $z$ is the image of some $y \in L$ with $y = 0$ or $v_w(y) \ge -a$. A vector $v$ is in the lattice $\Lambda$ at $w$ with loss $a$ if $s v$ lies in $\Lambda$ for some $s \neq 0$ in $L$ with $v_w(s) \le a$.

Fix a grid choice $\mathrm{ch}$ with grid $G$, and constants $C$ and $b$. Let $f$ be the degree and $m$ the size of $D$, $N$ its bound, and $\sigma_G$ the sum of the depths of $G$ times the logarithms of the norms of the places of its exceptional set. Put

$$\begin{aligned} b_1 &= C f m N^2 (\log b + \sigma_G)\, b, \\ a_1 &= C f N b \log b + C m N^2 \sigma_G. \end{aligned}$$

A place $w$ is away from the level at $t$ if each prime of the level at $t$ either lies over the exceptional set of $G$ or lies over a rational prime that is not in $w$.

**Definition 3.12.1 (Size bounds).** Each of the following is a statement at large scale, in the sense that there is $C_{F,0}$ such that for $C_F \ge C_{F,0}$ there is $C_0$ such that for all $\varepsilon$ and $C \ge C_0$ there is $x_0$ such that it holds for all data of exponent $\varepsilon$ with $x \ge x_0$, all real data in the Hida setting and all grid choices at scale $C_F$ with the field condition.

1. The finite bound: there is a loss function of total $m b_1 / 2$ such that for every test lattice $M$, every $t$ and place $w$ away from the level at $t$, and every vector $x$ of the form lattice, the coordinates of the value at $x$ have a nonzero multiple $s y \in M$ with $v_w(s) \le d(w)$.
2. The away bound: every place $w$ is away from the level at the index attached to $w$.
3. The infinite bound: for every test lattice $M$, every metric on the form lattice at the base point and every linear map $V$ that gives the values at the base point, the height of $V$ is at most $m\, a_1$.

The data bound asks for a loss function of total $m b_1$ such that, at places away from the level, the products of the data of the terms of the grid choice have loss at most $d(w)$. The pair bounds ask for a loss function of total $b_1$ such that the last pairing of two lattice vectors adds at most $d(w)$ to their losses, and, at each infinite place, that the last pairing of two vectors of norms at most $B$ and $B'$ has square absolute value at most $e^{a_1} B B'$.

**Theorem 3.12.2 (Sizes at all places).** Under the local inputs, the finite bound, the away bound and the infinite bound hold.

Lean: `GlobalTheory.SumSize.Join.sum_size_finite_away_archimedean_combined` (also `GlobalTheory.T.sum_size_bound_all_places`, a second name).

*Proof.* The record $\mathrm{Inp}(D)$ holds for every $D$ with no hypothesis. The local inputs give the condition on sums, and from it the depth bound, and with $\mathrm{Inp}$ a dictionary of sizes. They also give the bounds at both kinds of places for the scalar, the form values, the pairs ([Theorem 3.12.4](/entry/fpair-lift-splits-locally/)) and the test vectors. With the dictionary and the depth bound, they give the bounds for the top terms and the rows at the finite places, and the mean bounds for the top terms and the rows at the infinite places. At the finite places, a lemma turns the nine factor bounds (scalar, coefficients, data by [Theorem 3.12.3](/entry/fin-dat-k-alt/), the inverse orders of the classes, top terms, rows, pairs, test vectors and form values) into the finite bound: the total of the sum of the loss functions is controlled by $m b_1 / 2$. At the infinite places a second lemma turns nine factor bounds (scalar, tensors, counts of terms, counts of classes, top terms, rows, pairs, test vectors and form values) into the infinite bound. The away bound is a property of the twisted local factors away from the level. $\square$

**Theorem 3.12.3 (Data at the finite places).** Under the local inputs, the data bound holds.

Lean: `GlobalTheory.FunDat.finDatK_alt` (also `GlobalTheory.T.finDatK_of_theta_inputs`, a second name).

*Proof.* The loss of a product of data is the sum of two losses: the loss of the flips at the exceptional places, and the loss of the valuations of the unfolding integral of a moved tensor. Both are bounded with no hypothesis, and a lemma adds them. $\square$

**Theorem 3.12.4 (Pairs at all places).** Under the local inputs, both pair bounds hold.

Lean: `GlobalTheory.FPair.lift_splits_locally` (also `GlobalTheory.T.field_pair_comparison`, a second name).

*Proof.* The finite pair bound and the infinite pair bound are each proved with no hypothesis. $\square$

We now turn to the leaves. The fit of constant functions is defined in Section 9. Each leaf is a condition on the fitted points of a family, of the form: there is $C_{F,0}$ such that for $C_F \ge C_{F,0}$ a statement is closed in the class of families, and at large $x$ it holds at each fitted point for each $C$ above a threshold. The sixteen leaves are: minimal mass, a unique map, the kernel, the fixed point, the height map, the infinite places, a unique square root, density, integrality, an archimedean condition, the theta bound, the weight bound, a descent height condition, a rank gap bound, a ramified sum bound and a polynomial descent condition. The leaves of the infinite places and the last four leaves do not depend on the tie of the comparison; the others do.

**Lemma 3.12.5 (Join of the leaves).** Let a field datum and a tie of the comparison be given. Assume the bundle condition, the scale condition, the existence of a function in the field datum for the tie, and the sixteen leaves. Then constant functions fit.

Lean: `GlobalTheory.BigTop.Fun.fun0Fit_of_leaves_alt`.

*Proof.* A conjunction of two leaves is a leaf, with the larger threshold, and a leaf that does not depend on the tie is a leaf for every tie. So the sixteen leaves join into one leaf with threshold $a$. The existence of a function gives a threshold $b$; take $C_{F,0} = \max(a, b)$. Fix a family and a fitted point $p$ with a grid $G$ and a Weil datum $W$. The existence of a function gives a datum $d$ of the field at $p$. The bundle condition gives a lattice gluing and its record at $p$. With the constant $C = \max(C_0, 1)$ for the threshold $C_0$ of the leaves, the numeric lower bound for the functional under the conditions gives the slope inequality from the sixteen leaf bounds at $d$. Two of its inputs need a change: the leaves are stated for the datum with scale $1$, and the datum of $d$ has scale $\zeta^{-1}$ for a root of unity $\zeta$ with $\zeta = 1$ at the base point. The kernel and the values at the base point do not change, and the bound at the finite places is invariant under a root of unity. $\square$

The leaf of minimal mass asks the following of each fitted datum $d$ and constant $C$. The module $M$ of $d$ is finitely generated and not $0$, the determinant of the metric matrix at each infinite place is a unit, and

$$\mu_{\max}(M) \le E_{MM}(C),$$

where $E_{MM}(C)$ is an explicit expression in $C$ and the data of $d$, which we have not unfolded. The setting at a point is a closed condition on the families: at large $x$ each fitted point has a test datum.

**Theorem 3.12.6 (Leaf of minimal mass).** If the setting at a point holds, then the leaf of minimal mass holds for the tie of the comparison.

Lean: `GlobalTheory.BigTop.Fun.LeafMMTie.mm_tie_alt` (also `GlobalTheory.T.leafMinimalMass_of_setAt`, a second name).

*Proof.* Take $C_{F,0} = 0$ and, at each fitted point, the threshold $1$ for $C$. The setting gives the closed condition; at a fitted point it gives a test datum $a$ for $d$. A lemma on the multiplicity at fitted points gives the leaf bound from the test datum for every $C \ge 1$. $\square$

**Remark 3.12.7 (Formalization).** Several results here do not use their hypotheses. The data bound ([FiniteDataBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FiniteDataBound.lean#L27)) and the pair bounds ([FieldPairComparison.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FieldPairComparison.lean#L13)) ignore the local inputs. The name of the pair theorem speaks of lifts that split locally, which does not match the statement. In the size theorem ([SumSizeFiniteAwayArchimedeanCombined.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SumSizeFiniteAwayArchimedeanCombined.lean#L26)) the record $\mathrm{Inp}(D)$ is proved with no hypothesis, and the away bound is a lemma that ignores the local inputs ([TwistedLocalFactorAwayFromLevel.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedLocalFactorAwayFromLevel.lean#L16)). The leaf of minimal mass ([MmTie.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MmTie.lean#L23)) uses the setting at a point only for its closed condition; the bound itself comes from the test datum. The joining lemma is in [LeafInfinitePlaceBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LeafInfinitePlaceBound.lean#L83), a file named for one of the leaves, and the second name of the minimal mass leaf is in [MmTieStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MmTieStatement.lean#L11). We have not opened the factor bounds, the two assembly lemmas, the numeric lower bound for the functional or the multiplicity lemma.
