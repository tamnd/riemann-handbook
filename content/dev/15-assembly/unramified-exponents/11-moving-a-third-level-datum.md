---
title: Moving a third level datum
decls:
  - GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt
  - GlobalTheory.T.moveToBase_of_inputs_serN
  - GlobalTheory.HeightCounting.Up.exists_levelB1_carried_of_levelI_same_gal
  - GlobalTheory.T.levelI_same_gal_transfer_to_levelB1_list
  - GlobalTheory.HeightCounting.Up.multiplicity_lower_bound_of_restricted_copy_alt
  - GlobalTheory.T.multiplicity_pos_of_restricted_eigenform_copy_alt
  - GlobalTheory.HeightCounting.SerCarry.series_restage_of_carry_alt
  - GlobalTheory.T.mem_of_series_carry_alt
  - GlobalTheory.HeightCounting.SerGlue.exists_move_alt
  - GlobalTheory.HeightCounting.Up.geoLaws_at_levelB1_states
  - GlobalTheory.T.geoLaws_iC_at_levelB1_of_serN
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moving a third level datum

This section proves the moving statement: a third level datum at a stage of one column datum moves to a stage of an enlarged column datum, with the Galois data carried and the list condition kept. The second nonvanishing statement of Section 13 needs it. There, a third level datum is built at a stage over a base $B$, and the base is then enlarged to a base $B'$ that avoids a finite set of bad places; the moving statement brings the third level datum to $B'$. The proof has two steps. The first step makes a second level datum on a twisted copy of a stage of $B'$. The second step turns the second level datum into a third level datum, and it uses the geometric Hecke laws proved at the end of this section.

We keep the notation of Sections 6 and 9: the ladder of levels, the published inputs $\mathcal{P}$ of the third layer, the series input $\mathcal{S}$, a recursion datum $h_L$, new twists $N$ and twisted copies. For a stage $x$ we write $D_x$ for its datum.

**Definition 6.11.1 (Enlargements and carried data).** Let $B$ and $B'$ be bases. An *enlargement* $B \to B'$ is a map of bases under which the frames, the twist data and the column data of $B$ have images over $B'$. Two column data $w$ over $B$ and $w'$ over $B'$ *match* if $w'$ is the image of $w$ and they have the same position, the same selection, the same index set $J$ and the same shift $\delta$. A datum $P'$ of $w'$ *extends* a datum $P$ of $w$ if the base point of $P'$ extends the base point of $P$. A datum $D'$ is *carried* from $D$ if the Galois data, the twist and the Hecke data of $D$ go over to $D'$ along a fixed map of coefficient rings.

**Definition 6.11.2 (Moving statement).** Let $h_L$ be a recursion datum. The *moving statement* for $h_L$ says that, eventually along $\mathrm{Step}_w$ from the start condition, for every base $B'$ and column datum $w'$ the following holds. Let $B \to B'$ be an enlargement and $w$ a column datum over $B$ that matches $w'$ and satisfies the start condition. Let $x$ be a stage of a datum $P$ of $w$ with a third level datum. Let $P'$ be a datum of $w'$ that extends $P$, and $x'$ a stage of $P'$ with an intermediate level datum and the same Galois data as $x$. Then there is a stage $x''$ of $P'$ with a third level datum such that $D_{x''}$ is carried from $D_x$ and, for every $c \in \mathbb{R}$, the list condition for $c$ at $x$ implies the list condition for $c$ at $x''$.

The intermediate level datum at $x'$ gives the place: the third level datum is built on a stage of $P'$, and the stage $x$ gives the Galois data. The point is that $x'$ and $x$ have the same Galois data but sit over different bases.

We say that a context $K$ is *good for* $(B', f', w')$ if $K$ lies over the pre-base of $B'$, $\mathrm{KP}_x(B', f')$, the forced condition and the start condition for $w'$ hold, and every stage $X$ with $K$ over its pre-base satisfies the host hypotheses and $8 f r + 4 \leq n_V$, where $f$, $r$ and $n_V$ are the sizes of the real data of $X$.

**Theorem 6.11.3 (Moves of stages).** Let $K$ be good for $(B', f', w')$, let $B \to B'$ be an enlargement and $w$ a column datum over $B$ that matches $w'$ and satisfies the start condition. Let $x$ be a stage of a datum $P$ of $w$ with a same Galois level datum $l$, let $P'$ be a datum of $w'$ that extends $P$, and let $x'$ be a stage of $P'$ with the same Galois data as $x$. Let $N$ be a new twist of $D_{x'}$, let $(\iota, e)$ be a twisted copy of $D_x$ along $N$, and let $x''$ be a stage of $P'$ with a same Galois level datum $l''$ whose object is the twist of the object of $x'$ along $N$. Then there are a map $\iota'$ of coefficient rings and a ring isomorphism $e'$ such that all data of $D_x$ are copied to $D_{x''}$ along $\iota'$ and $e'$, the character frames of $x$ and $x''$ agree, the places $P_q$ of $l$ and $l''$ agree, the geometric data of both stages lie in the geometry of their bases with big hosts, and there is a real move from the side of $x$ to the side of $x''$ along $\iota'$.

Lean: `GlobalTheory.HeightCounting.SerGlue.exists_move_alt`.

*Proof.* The copy of all data comes from the twist relation between the objects. The frames agree because the twist does not change the character frame. The geometric data lie in the geometry of the base by the choice of geometric extensions, and the hosts are big at every stage. The real move is built from the link between the two sides that the copy gives. $\square$

**Theorem 6.11.4 (Series data on the moved stage).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Let $K$ be good for $(B', f', w')$. Let $B \to B'$, $w$, $x$, $P'$ and $x'$ be as in the moving statement, with a third level datum $l_b$ at $x$ and an intermediate level datum $l'$ at $x'$. Let $N$ be a new twist of $D_{x'}$ and $(\iota, e)$ a twisted copy of $D_x$ along $N$, and let $x''$ be a stage of $P'$ with an intermediate level datum $l''$ whose object is the twist of the object of $x'$ along $N$. Assume that the level characters, the row, $P_q$, the rational datum, $S_b$, the Hecke operators, the eigenvalues and the characters $\theta$ of $l''$ are the twists along $N$ of those of $x'$ and $l'$. Let $c_{\mathrm{Hk}}$ be units that agree with the Hecke units of $l_b$. Then there are a real series datum $Y_S$ and a tied datum $X$ for $D_{x''}$ such that:

1. the place data of $X$ are those of $P_q$ of $l''$;
2. at each split prime $\mathfrak{P}$ outside $S_0(i)$ and each $k \leq r$, the endomorphism $e_F$ of $Y_S$ and the Hecke operator $h_{k, F}$ satisfy $e_F \circ h_{k, F} = c_{\mathrm{Hk}}^k \cdot (h_{k, F} \circ e_F)$;
3. each map of $Y_S$ fixes $x$;
4. there are series data for $Y_S$ at the base place with the character frame and $P_q$ of $l''$;
5. the tau condition holds for $X$.

Lean: `GlobalTheory.HeightCounting.SerCarry.series_restage_of_carry_alt` (also `GlobalTheory.T.mem_of_series_carry_alt`, a second name).

*Proof.* The theorem on moves of stages, applied to the same Galois levels below $l_b$ and $l''$, gives the copy maps, the agreement of frames and of $P_q$, and a real move from the side of $x$ to the side of $x''$. The facts of the two stages and the side facts give the tied datum $X$ with the place data of $P_q$ and the tau condition. The series datum of $l_b$, moved along the real move, gives $Y_S$ with the series data at the base place. The Hecke relation holds at $x$ with the units of $l_b$, and the move keeps it, so it holds with $c_{\mathrm{Hk}}$. $\square$

**Theorem 6.11.5 (A second level datum on the twisted copy).** Assume $\mathcal{P}$ and $\mathcal{S}$, let $h_L$ be a recursion datum, and let the data $K$, $B \to B'$, $w$, $x$, $l_b$, $P'$, $x'$, $l'$, $N$, $(\iota, e)$, $x''$ and $l''$ be as in the theorem on series data on the moved stage. Then $x''$ has a second level datum.

Lean: `GlobalTheory.HeightCounting.Up.multiplicity_lower_bound_of_restricted_copy_alt` (also `GlobalTheory.T.multiplicity_pos_of_restricted_eigenform_copy_alt`, a second name).

*Proof.* The Hecke eigenvalues of $l_b$ transfer to the twisted copy: there are units $c_{\mathrm{Hk}}$ that agree with the Hecke units of $l_b$. The theorem on series data on the moved stage gives $Y_S$ and $X$. The side of the copy gives settings forms data for $x''$ whose side is $X$, and its endomorphism agrees with $e_F$. The second level datum is $l''$ with these settings forms data, $Y_S$, the series data and the tau condition. $\square$

**Theorem 6.11.6 (Second level on the enlarged base).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Then eventually along $\mathrm{Step}_w$ from the start condition, with $B'$, $w'$, $B \to B'$, $w$, $x$, $P'$ and $x'$ as in the moving statement, there is a stage $x''$ of $P'$ with a second level datum such that $D_{x''}$ is carried from $D_x$ and, for every $c$, the list condition for $c$ at $x$ implies the list condition for $c$ at $x''$.

Lean: `GlobalTheory.HeightCounting.Up.exists_levelB1_carried_of_levelI_same_gal` (also `GlobalTheory.T.levelI_same_gal_transfer_to_levelB1_list`, a second name).

*Proof.* Eventually every stage satisfies the host hypotheses and the size bound $8 f r + 4 \leq n_V$. The eigensystem of $l_b$ gives a new twist $N$ of $D_{x'}$ and a twisted copy $(\iota, e)$ of $D_x$ along $N$. Along $N$ there is a stage $x''$ of $P'$ with an intermediate level datum that satisfies all the transport conditions of the theorem on series data, and $D_{x''}$ is the twisted datum. The theorem on a second level datum on the twisted copy gives the second level datum at $x''$. The twisted copy carries $D_x$ to $D_{x''}$. The Hecke eigenvalue lists move from $x$ to $x''$ with the twist, so the list condition passes. $\square$

**Definition 6.11.7 (Geometric Hecke laws).** Let $Y_S$ be a real series datum, $f_w$ a framed point and $i_C$ an integral twist index. The *geometric Hecke laws* for $(Y_S, f_w, i_C)$ are seven conditions:

1. the points of $f_w$ detect the algebraic points;
2. the descent of the supports holds on the side;
3. the supports are pinned;
4. the Hecke operators act geometrically;
5. the Hecke quotients are stable;
6. the kernels of the Hecke operators have constant cardinality at each split Hecke prime;
7. the form spaces at the indices $j$ outside $[1, m]$ have at most one element.

**Theorem 6.11.8 (Geometric Hecke laws at the second level).** Assume $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Then at all stages $x$, for each second level datum $l$ over $x$ and each twist index $i$ of $D_x$, the geometric Hecke laws hold for the series datum $Y_S$ of $l$, the framed point of the geometric datum of $x$ and the integral index $i_C(i)$.

Lean: `GlobalTheory.HeightCounting.Up.geoLaws_at_levelB1_states` (also `GlobalTheory.T.geoLaws_iC_at_levelB1_of_serN`, a second name).

*Proof.* Condition 4 holds at all stages by a theorem on the geometric Hecke action at the second level. We check the six others at each stage. Condition 1 holds because the points of $f_w$ detect algebraic points at integral indices, and condition 2 because the supports descend along the geometric tie. Conditions 3 and 7 are parts of the series data of $l$. Condition 5 follows from the integrality of Hecke quotients at a framed point, which is part of $\mathcal{S}$. For condition 6, an index place of the Hecke data is a split Hecke prime off the level, and at such a prime the kernel of the $k$-th Hecke operator on each form space has a constant number of elements. $\square$

**Theorem 6.11.9 (Moving statement).** Assume $\mathcal{P}$ and $\mathcal{S}$. Then the moving statement holds for every recursion datum $h_L$.

Lean: `GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt` (also `GlobalTheory.T.moveToBase_of_inputs_serN`, a second name).

*Proof.* The theorem on the second level on the enlarged base gives, eventually, a stage $x_1$ of $P'$ with a second level datum, carried from $D_x$ and with the list condition. The step from the second level to the third level of item 4 of [the stage statements](/entry/all-stages-of-specializations-alt/), which uses the theorem on geometric Hecke laws, gives a stage $x''$ of $P'$ with a third level datum, with $D_{x''}$ carried from $D_{x_1}$ and with the list condition. Carried data compose, and the two list implications compose. The two eventual statements hold together, so the moving statement holds eventually. $\square$

**Remark 6.11.10 (Formalization).** The theorems are at [MultiplicityBoundOfLocalComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundOfLocalComponents.lean#L17) (second name at line 31), [MultiplicityBoundTransferOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundTransferOfCmDatum.lean#L24) (line 48), [MultiplicityPosOfRestrictedEigenformCopy.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityPosOfRestrictedEigenformCopy.lean#L22) (line 35), [SeriesRestageOfCarry.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesRestageOfCarry.lean#L22) (line 39), [ExistsMove.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsMove.lean#L18) and [GeometricHeckeLawsOfMultiplicityLowerBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeometricHeckeLawsOfMultiplicityLowerBound.lean#L18) (line 40). The moving statement is `MoveToBase` ([ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L40)); the matching of $w$ and $w'$ and the transport conditions are `HEq` hypotheses. In `series_restage_of_carry_alt` the intro at line 23 drops $\mathcal{P}$, $\mathcal{S}$ and the eight transport hypotheses with `_`, so the theorem holds without them. The step from the second to the third level is `exists_levelB2_carried_of_levelB1` (PointsPreservedUnderLevelTransferOfCmDatum.lean, line 24), and the twist comes from `exists_eigenform_copy_of_eigensystem_alt`; neither has an entry here. The names "multiplicity bound of local components", "multiplicity lower bound" and "multiplicity pos" do not describe the statements, which say nothing on multiplicities. We did not unfold `Carried`, `CopyN`, `CopyAll`, `RealMove`, `SerAt`, `TauTrue` or the seven fields of `GeoLaws` (NonemptyPtsOfReading.lean, line 320), so the definitions above give their roles only.
