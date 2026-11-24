---
title: The third layer and the point conditions
decls:
  - UpperTheory.One.M.repOfLocal_h_alt
  - GlobalTheory.T.repOfLoc_of_isTrue_laws
  - GlobalTheory.TypesAtPin.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.T.archimedeanSignatureMatching_of_modules
  - UpperTheory.One.M.latticesB_closing_alt
  - GlobalTheory.T.b_conditions_pairLift_splitBC_repOfLoc_of_a
  - GlobalTheory.EigStr.eigString_all_of_aux41_adm7_tieLab
  - GlobalTheory.T.eigString_of_agree_aux41_adm7_tieLab
  - GlobalTheory.RowsAll.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.T.theta_conditions_of_inputs_of_jumpsCard
  - GlobalTheory.HeightCounting.Up.ptSt_of_inputs_geometric_compat
  - GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat
  - GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The third layer and the point conditions

This section proves two results that the record of hypotheses of Section 1 uses. The first is [the third layer inputs](/entry/hyps-e-third-layer-ser-n-of-geometric-galois/) of step 2 there: from the non-endoscopic hypotheses and the geometric compatibility we get the published inputs of the third layer, the local Selmer input and a [[local Langlands|9E45NBX1G0]] recursion $h_L$ with its hypotheses. The second is [the theta conditions](/entry/theta-conditions-of-inputs-of-jumps-card/), the point conditions at a datum, which Section 13 uses for the Galois preconditions. The point conditions have three groups of rows, $\mathrm{A}$, $\mathrm{B}$ and $\mathrm{C}$. We prove the deeper parts first: strong multiplicity one for algebraic modular forms, the local types at the type primes, the rows $\mathrm{B}$, and the strings of Satake parameters.

We keep the notation of Section 12. A character choice $P$ of a datum $D$ has local indices $i$ with spaces $V_i$ and $W_i$ over $E$, automorphic data $\mathrm{AU}_i$ on the unitary groups $U(V_i)$ and $U(W_i)$, and local parameters at the places of $E$. A *true reading* $S$ of $P$ gives at each split place $w$ an irreducible local representation for each point whose Weil-Deligne representation under $h_L$ is the local parameter. It satisfies the *reading laws*: at split places the local components are isomorphic through the reading, and at nonsplit places the data are inert.

**Definition 8.15.1 (Local determination).** Let $P$ be a character choice of $D$ and $i$ an index. *Local determination* at $i$ says: let $\Pi$ and $\Pi'$ be points at $i$ whose local parameters agree at all split places, and whose unramified base changes of the Satake parameters agree at the nonsplit places. Then $\Pi = \Pi'$.

**Theorem 8.15.2 (Strong multiplicity one for algebraic modular forms).** Let $h_L$ be as in Section 7, $D$ a datum, $P$ a character choice and $S$ a faithful reading of $P$ with the reading laws. Then local determination holds at each $i$.

Lean: `UpperTheory.One.M.repOfLocal_h_alt` (also `GlobalTheory.T.repOfLoc_of_isTrue_laws`, a second name).

*Proof.* The reading is faithful, so the map from points to their automorphic representations is injective. At split places the reading laws give isomorphic local components. At nonsplit places the inert data give equal unitary Satake parameters, since the unramified base change determines the Satake parameter. Strong multiplicity one for the algebraic modular forms of the definite group then gives equal representations, and injectivity gives $\Pi = \Pi'$. $\square$

This is the analogue for definite unitary groups of the strong multiplicity one theorem of Jacquet and Shalika for $\mathrm{GL}_n$ (Jacquet and Shalika 1981, Theorem 4.4).

**Definition 8.15.3 (The monodromy and inertia type).** Let $D$ be a datum with a character $\chi_1$, a set $S_i \cup Q_i$ of places at each index $i$ and a tame element $\gamma_0$ of inertia. The *monodromy and inertia type* of $D$ says, at each $i$:

1. at each $w \in Q_i$, and at each $w \in S_i$ over a prime $p_{de}$, the parameter has monodromy zero and the characteristic polynomial of inertia is $(X - 1)^r (X - \chi_1(\sigma))^t$;
2. at each $w \in S_i$ over a type prime $g_k$, where $\chi_1(\gamma_0)$ is a root of multiplicity at most $t$, the parameter splits as $a \oplus b$ with $\dim a = r$ and $\dim b = t$, and $b$ has monodromy zero with inertia polynomial $(X - \chi_1(\gamma_0))^t$;
3. the factor $a$ cancels in the comparison of the two sides.

The type is the local shape of the Galois representation of a theta lift of $\rho \boxplus \chi_1^{\oplus t}$ type at the bad places.

**Theorem 8.15.4 (Local types at the bad places).** Assume the local theta inputs. Let $h_L$, $D$ and $P$ be as above, with row modules at each $i$, and assume the rows $\mathrm{A}$ at $D$. Then the monodromy and inertia type holds at $D$.

Lean: `GlobalTheory.TypesAtPin.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.archimedeanSignatureMatching_of_modules`, a second name).

*Proof.* There are four steps.

1. **A reading.** The finiteness of automorphic forms and the row modules give a true reading of $P$.
2. **Tame splitting.** Bernstein-Zelevinsky finiteness, the geometric lemma, the irreducibility of unlinked products and the injectivity of the depth zero Jacquet functor show that a representation with a tame parahoric vector splits as a product. The same inputs give the split of an irreducible representation with a block vector, as in the Theorem (The block split) of Section 12.
3. **The inertia.** The character of the inertia at the places of $S_i \cup Q_i$ is $\chi_1$ on the twisted block. At the places of $Q_i$ and at the places of $S_i$ not over the type primes the parameter is tame of the stated shape. At the places of $S_i$ over the type primes the block split gives the factor $b$.
4. **The type.** The rows $\mathrm{A}$ identify the inertia polynomials with the local parameters, and the inertial types follow. $\square$

The rows $\mathrm{B}$ need three more conditions at each $i$. The *pair lift condition* says: if a point $\sigma$ on $U(W_i)$ pairs with $\Pi$, then at each split place $w$ the parameter of $\Pi$ is the lift of the parameter of $\sigma$. The *split base change condition* says: if the base change parameters of two points agree at almost all split places, they are permutations of each other. The rows $\mathrm{B}$ are four statements: the size of the rows, the third and fourth admissibility conditions, where the fourth is the monodromy and inertia type, and the first theta row.

**Theorem 8.15.5 (The rows $\mathrm{B}$).** Assume the local theta inputs. Let $h_L$, $D$ and $P$ be as above, with the character choice joined, the rows $\mathrm{A}$, the first admissibility condition and positivity of $\lambda$ at each $i$. Then the rows $\mathrm{B}$ hold, and at each $i$ the pair lift condition, the split base change condition and local determination hold.

Lean: `UpperTheory.One.M.latticesB_closing_alt` (also `GlobalTheory.T.b_conditions_pairLift_splitBC_repOfLoc_of_a`, a second name).

*Proof.* There are five steps.

1. **A reading.** The finiteness of automorphic forms gives a true reading $S$ with its laws, and a unit row.
2. **Pairs.** Bernstein-Zelevinsky finiteness gives the pair reading. With the irreducibility of Bernstein's unitary products it gives the pair lift condition, by the compatibility of the [local theta correspondence](/learn/theta/#the-local-theta-correspondence) with the split places.
3. **Base change.** The Chebotarev input gives a split statement. The tie at $0$ and the second and seventh admissibility conditions give an isomorphism of Galois representations, and this gives the split base change condition. Base change exists by the first admissibility condition, and the types are orthogonal.
4. **Local determination.** This is the Theorem (Strong multiplicity one for algebraic modular forms).
5. **The rows.** The size of the rows comes from the unitary spherical component of the reading. The third admissibility condition comes from the split theta correspondence of the local pairings, the fourth from the Theorem (Local types at the bad places), and the first theta row from the ties. $\square$

**Definition 8.15.6 (Strings of eigenvalues).** Let $X$ be a real record over $P$ and $i$ an index. The *string condition* at $i$ says: at each good point $x$, for each nonzero $y$ that lifts an element of the eigenspace and each Hecke operator $h$, there is an eigensystem $s$ such that $s$ has a string, as in Section 14, and $y$ is an eigenvector with eigensystem $s$.

**Proposition 8.15.7 (Strings at all indices).** Assume the finiteness of automorphic forms on $\mathrm{GL}$. Let $h_L$, $D$ and $P$ be as above, and $X$ a real record that agrees with $P$. Assume the forty first provision, the seventh admissibility condition and the label tie. Then the string condition holds at each $i$.

Lean: `GlobalTheory.EigStr.eigString_all_of_aux41_adm7_tieLab` (also `GlobalTheory.T.eigString_of_agree_aux41_adm7_tieLab`, a second name).

*Proof.* Choose $s$ as the eigenvalue of $h$ on $y$. The theta lift is compatible with the Hecke eigenvalues at the split places and at the inert places, in six cases. Each case gives the eigenvector and the Satake parameter at the place. The family of Satake parameters is the parameter of a form on $U(W_i)$ plus the segment of the twist, so it has a string. $\square$

**Definition 8.15.8 (The point conditions).** The *point conditions* at $D$ are five statements: the rows $\mathrm{A}$, the rows $\mathrm{B}$, the rows $\mathrm{C}$, a recursion for the nonzero types and the constancy of the rank. The rows $\mathrm{A}$ are ten statements: the label tie, a Hecke statement, the tie at $0$, the second admissibility condition, two conditions at $\ell$, the fifth admissibility condition, temperedness, and two Galois conditions. The rows $\mathrm{C}$ are six: a fourth condition at $b$, the residual condition, the depth zero condition, an upper parameter, membership of the downward lift and the good part.

The point conditions take *linked inputs*: a character choice $P$, a real record $X$ that agrees with it and a reading at $0$, with seven named facts (the hypothesis at the points, the first condition, base change, the $\lambda$ condition, internal isotypy, the series condition and the nonzero types).

**Theorem 8.15.9 (The theta conditions).** Assume the local theta inputs, the finiteness of Harish-Chandra and the rapid decay of cusp forms. Let $h_L$ be as above, $D$ a datum with linked inputs and the count of jumps. Then the point conditions hold at $D$.

Lean: `GlobalTheory.RowsAll.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.theta_conditions_of_inputs_of_jumpsCard`, a second name).

*Proof.* There are five steps.

1. **Rows $\mathrm{A}$.** The local theta inputs and the count of jumps give the rows $\mathrm{A}$.
2. **The join.** The agreement of $X$ with $P$ gives the joined character choice. The rank of the theta lift spaces is constant, and the scalars of the localizations are positive.
3. **Rows $\mathrm{B}$.** The Theorem (The rows $\mathrm{B}$) applies, with the first admissibility condition from base change.
4. **Rows $\mathrm{C}$.** The first provision follows from the rows $\mathrm{A}$ and $\mathrm{B}$. With the pair lift, the split base change and local determination it gives the rows $\mathrm{C}$.
5. **Nonzero types.** The Proposition (Strings at all indices), with the forty first provision, the seventh admissibility condition and the label tie, and a good eigensystem from the archimedean signature and the fifth admissibility condition, give the recursion for the nonzero types. $\square$

**Definition 8.15.10 (The point statement).** Let $h_L$ be as above. The *point statement* for $h_L$ says: at all levels and for each datum $D'$ forced by the data at the level, the hypothesis at the points of $D'$ implies the forty first provision, good residual irreducibility, the forty second conclusion and the multiplicity conclusion; and the eigen span and internal isotypy hold.

**Proposition 8.15.11 (The point statement).** Assume the published inputs of the third layer and the geometric compatibility. Then the point statement holds for each $h_L$.

Lean: `GlobalTheory.HeightCounting.Up.ptSt_of_inputs_geometric_compat`.

*Proof.* Four facts hold eventually in the level: the inputs are nonempty, the count of jumps holds by the height count of the compatibility, the eigen span holds, and the eighth admissibility condition holds with the use of $\lambda$. At each forced datum, the Theorem (The theta conditions) gives the point conditions. The first conclusion, good residual irreducibility and the reduced multiplicity give the four conclusions. $\square$

**Theorem 8.15.12 (The third layer inputs).** Assume the non-endoscopic hypotheses and the geometric compatibility of the [[Galois representation|JQEYEQJY2G]]s. Then the elliptic hypothesis holds, the published inputs of the third layer hold, the local Selmer input holds, and there is a witness $h_L$ of [the local Langlands recursion](/step/rect-exists-def/) with the local Langlands hypothesis.

Lean: `GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat` (also `GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois`, a second name).

*Proof.* The non-endoscopic hypotheses have five parts: local representation theory, global automorphic inputs with a global Artin map, twelve facts of Galois cohomology, five transport facts, and a functional equation. There are four steps.

1. **Local Langlands.** The local part and the automorphic part give $h_L$ and the third layer inputs. This is local Langlands for $\mathrm{GL}_n$ (Harris and Taylor 2001; Henniart 2000) with purity at the layer points.
2. **The local Selmer input.** It has six parts. Global Artin reciprocity gives two, three hold with no hypothesis, and a toric transport fact gives the ratio of conjugates.
3. **The elliptic hypothesis.** It has twenty five parts: the Chebotarev and the tame local facts from the cohomology and Artin reciprocity, seven facts of the cohomology, a toric fact, five parts of the Selmer input, three local theta inputs, the local-global compatibility above $\ell$ for cusp forms, and local Bloch-Kato at all primes.
4. **The local Langlands hypothesis.** It holds the third layer inputs and the Selmer input, the archimedean compatibility of local Langlands, the stability of conjugate dual parameters at primes not dividing the level, the Proposition (The point statement) and the cuspidal parameters at the layer points. $\square$

**Remark 8.15.13 (Formalization).** The files are [MRepOfLocalH.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MRepOfLocalH.lean#L19), LocalRepOfReadingLaws.lean (line 14), [GaloisRepLocalTypesDeterminedAtPlace.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisRepLocalTypesDeterminedAtPlace.lean#L22) (lines 22 and 62), [PointsOfTiedLattices.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointsOfTiedLattices.lean#L45), GaloisRepIsGeometricAtRamifiedPlaces.lean (line 21), [EigStringAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EigStringAll.lean#L18), EigStringAllStatement.lean (line 14), [GaloisRepIsGeometricAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisRepIsGeometricAtAllPlaces.lean#L24) (lines 24 and 42), [PointwiseGaloisPropertiesOfLocalInputs.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointwiseGaloisPropertiesOfLocalInputs.lean#L43) and [ThetaLiftHypothesesOfNonvanishing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean#L24) (lines 24 and 51). The monodromy and inertia type is `MonodromyInertiaType` (SumRepresentations.lean, line 311), and `ArchimedeanSignatureMatching` (line 370) is defined as this type; in spite of its name it is a condition at finite places, and the second name `archimedeanSignatureMatching_of_modules` repeats the wrong word. The point conditions are `PointConditions'` with `RowsAAlt`, `RowsB` and `RowsC`; local determination is `RepOfLoc`, the pair lift is `PairLift` and the split base change is `SplitBC`. In the theta conditions, the first provision is a local fact named `Conclusion1`, which is `provisionFirst`. The geometric compatibility is `GeometricGaloisRepCompatibility`, a record of twelve inputs on the Weil representation, discrete series, Harish-Chandra analyticity, trace class, Dixmier-Malliavin, Flath, the Weil-Siegel formula, doubling and a height count; it has no statement on Galois representations. In the third layer inputs the functional equation and three transport facts are not used ([line 27](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean#L27)), the conclusion states the third layer inputs and the Selmer input twice, and `seriesRat_of_seriesRatS` is the identity. We did not unfold the rows $\mathrm{A}$ and $\mathrm{C}$, the six eigenvalue compatibilities, or the Galois conditions of the rows $\mathrm{A}$.
