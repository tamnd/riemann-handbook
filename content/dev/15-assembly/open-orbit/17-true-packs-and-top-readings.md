---
title: True packs and top readings
decls:
  - GlobalTheory.Fam.truePack_of_bWit_alt
  - GlobalTheory.T.true_pack_of_bundle_witness
  - GlobalTheory.TopVal.exists_read_at_pack_b_of_b_wit
  - GlobalTheory.T.exists_read_at_packB_of_bWit
  - GlobalTheory.Core.HypAt.hypL_at_points_alt
  - GlobalTheory.T.degHypL_all_linked_good_members
status: drafted
drafted_by: writer@claude-opus-5-5
---
## True packs and top readings

This section proves [the Theorem on bundle witnesses](/entry/true-pack-of-bundle-witness/), used in the proof of the Theorem on period identities from point conditions in [the section on rows](/entry/fam-mi-star-row-alt-alt/). A bundle condition $b$ at a witness point $q$ comes with a package $W_b$. If $b$ has a bundle witness, the point $q$ has a real datum, and $b$ satisfies the point conditions, then $W_b$ is a true package: it satisfies the six family conditions on a package of [the section on the period identity for a true package](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/). One of the six needs a construction, a leading reading of $W_b$ at each word with constant $1$. We build it in the second theorem. The section ends with the degree hypothesis at the points, an eventual row of numerical bounds that the nonzero projection row of section 2 uses.

We keep the notation of [the section on rows](/entry/fam-mi-star-row-alt-alt/) and of [the section on the period identity for a true package](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/). $h_L$ is a recursion datum, $p$ a parameter set for $h_L$, $K$ a context and $q$ a witness point of the scale of $p$ at $K$, with datum $D_q = I(l, Z)$ and object $O_q$. A bundle condition $b$ for $(D_q, O_q)$ and a real $c$ gives the package $W_b$. The conditions $\mathrm{pk}$, $\mathrm{tr}$, $\mathrm{tq}$, $\mathrm{tw}$, $\mathrm{lev}$ and $\mathrm{rc}$ are the six family conditions on a package. $\mathrm{BPC}(b)$ are the ten point conditions of [the section on rows](/entry/fam-mi-star-row-alt-alt/).

**Definition 4.17.1 (Leading reading).** Let $W$ be a real package, $u$ a word, $j$ a linear map from the vectors of the top space to the functions on the frame space, and $x \in G(X')$. Then $(j, x)$ is a *leading reading* of $W$ at $u$ if $j$ is a reading map for $u$ (the condition $\mathrm{IsJ}$), $x \in G_f(X')$, and for each twist index $t$:

1. the level condition holds at $t$: an element lies in the level group of the reference tuple at $t$ exactly when it lies in the level group of the twisted class, and the character of the twisted class is trivial there;
2. for each $F$ at $t$, the coefficients of the leading linear map of $F$ are read by $j$ at $x$.

**Definition 4.17.2 (Bundle witness).** A *bundle witness* for $b$ at $q$ is the record that $b$ is the bundle condition of the witness point $q$: its datum is $D_q$, its columns are the true columns of $q$, its twists are standard, and its characters are those of $q$. We use only the consequences listed in the proofs below.

**Theorem 4.17.3 (Top readings at a pack).** Let $q$ be a witness point, $b$ a bundle condition with a bundle witness at $q$, and assume that $q$ has a real datum. Then for each word $u$ there is a map $j$ such that $(j, 1)$ is a leading reading of $W_b$ at $u$.

Lean: `GlobalTheory.TopVal.exists_read_at_pack_b_of_b_wit` (also `GlobalTheory.T.exists_read_at_packB_of_bWit`, a second name).

*Proof.* We find a valuation map from the real datum, turn it into a reading map, and check the two conditions.

1. A result of another chapter on bundle witnesses gives that the tower data are ok and pinned, that the columns are standard, and that the twists are standard.
2. With the pins, a result of another chapter on true column spaces gives that the Gram matrix of the frame space is the identity.
3. The real datum gives a standard real structure. From it, a result of another chapter gives a valuation map $c_v$ from the values of the base to the top vectors, which is a valuation equivalence and which computes the package at each point.
4. *A reading map.* A result of another chapter gives a reading map $j_0$ of the true columns. If $c_v = 0$, the values vanish: a result of another chapter shows that every value of a restricted frame vanishes when the package vanishes at all unitary points, and we take $j = j_0$. If $c_v \neq 0$, a result of another chapter on families with unit Gram matrix gives a scalar $\alpha \neq 0$ such that $j = \alpha j_0$ satisfies, for all frames $\varphi$, restricted points $x$ and values $d$,
   $$\mathrm{pr}_X\bigl(c_v(\mathrm{val}(\varphi, d))\bigr)(v) = \bigl\langle j(v), \mathrm{val}(\varphi, d) \bigr\rangle.$$
   In both cases $j$ is a reading map for $u$.
5. $x = 1$ lies in $G_f(X')$.
6. *Level condition.* Three results of another chapter give the two directions of the level equivalence and the triviality of the character of the twisted class at $t$.
7. *Coefficients.* For $F$ at $t$, a result of another chapter gives a frame $\varphi$, restricted at a point, whose recursion value is the leading linear map of $F$. For $g \in G_f(X')$ the character of the top space is trivial at $g^{-1}$, so the map of the package at the point $g$ is the projection of the package at $g$. With the identity of step 4 and the decorated lattice of an adelic matrix, this shows that $j$ reads the coefficients of the leading linear map of $F$ at $1$. $\square$

**Theorem 4.17.4 (Bundle witnesses).** Let $q$ be a witness point and $b$ a bundle condition at $q$ with a bundle witness. Assume that $q$ has a real datum and that $b$ satisfies the point conditions $\mathrm{BPC}(b)$. Then $W_b$ is a true package.

Lean: `GlobalTheory.Fam.truePack_of_bWit_alt` (also `GlobalTheory.T.true_pack_of_bundle_witness`, a second name).

*Proof.* We check the six family conditions.

1. As in step 1 of the previous proof, the bundle witness gives that the tower data are ok and pinned, that the twists are standard, that the columns are standard, and the standard condition on the twisted columns. The last is $\mathrm{tw}$.
2. A result of another chapter on matching characters gives the characters of $W_b$, the condition on $\xi$, the twist sets $Q$, the level condition $\mathrm{lev}$, the recursion condition $\mathrm{rc}$, the real tuples, the ok condition at level 3, the identity condition and the level map.
3. The Theorem on top readings at a pack gives, for each word $u$, a leading reading $(j, 1)$.
4. $\mathrm{tr}$: the real package $W_b$ is valid, with the ok, pin, twist, standard and character conditions of steps 1 and 2, and the leading readings of step 3 with constant $1$.
5. $\mathrm{tq}$: the conditions on the geometric families are the condition on $\xi$, the twist sets and the leading readings of step 3.
6. $\mathrm{pk}$: a result of another chapter gives the package hypotheses of a real package from the point conditions (the join, the decomposition point, the frames, the extension, the primitive rows and separated types, the two gaps and finiteness), from the parts of step 2, and from $\mathrm{tr}$ and $\mathrm{tq}$.
7. With $\mathrm{pk}$, $\mathrm{tr}$, $\mathrm{tq}$, $\mathrm{tw}$, $\mathrm{lev}$ and $\mathrm{rc}$, $W_b$ satisfies the family conditions on a package, so it is true. $\square$

The point condition $1 \leq r_S$ is not used here. It is used, with the true package, in [the Theorem on period identities for a true package](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/).

We end with a row of numerical bounds on the data of good linked bundles. For a datum $D$ write $k, m, f, n, r_S$ for its integers, $L$ for the logarithmic scale of the object and $b = e^L$, and $\mathrm{Tr}(D, u)$ for the trace of the word $u$. The *degree hypothesis* $\mathrm{HypL}(D, L, C', C_l, C_g, c_b, C_u, c_T, C_T)$ is a list of about twenty inequalities. Among them are
$$\begin{aligned} 1 &< L, \\ C' m^5 f L &\leq k, \\ m^4 \leq f &\leq k, \\ \log f &\leq \sqrt{r_S}, \\ b^{c_T m} \leq \mathrm{Tr}(D, u) &\leq b^{C_T m}, \end{aligned}$$
together with bounds on the gaps of the levels and on the two gamma factors of the host.

**Theorem 4.17.5 (Degree hypothesis at the points).** Let $h_L$ be a recursion datum, $p$ a parameter set and $A, B$ functions of the constant record $C$. Then the eventual row of the good linked bundles of $p$ holds for the degree hypothesis

$$\mathrm{HypL}\Bigl(D, L, \max(A(C), 8 C_\Gamma), \max(B(C), 40), C_{YL} + 1, \tfrac14, 3, \tfrac12, C_{Tu}\Bigr).$$

Lean: `GlobalTheory.Core.HypAt.hypL_at_points_alt` (also `GlobalTheory.T.degHypL_all_linked_good_members`, a second name).

*Proof.* Two results of another chapter give the eventual rows of the lower bound $b^{m/2} \leq \mathrm{Tr}(D, u)$ and of the upper bound $\mathrm{Tr}(D, u) \leq b^{C_{Tu} m}$ at all words, in the good linked bundles. Their conjunction is again an eventual row. A third result of another chapter says that, eventually in the points, the two trace bounds at a bundle imply the degree hypothesis with the stated constants. Combine the row with this eventual implication. $\square$

**Remark 4.17.6 (Formalization).** The theorems are at [TruePackOfBWit.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePackOfBWit.lean#L35), [TopReadAtOfBWit.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopReadAtOfBWit.lean#L74) and [HypLAtPoints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypLAtPoints.lean#L16). The second names are relays at [TruePackOfBWitStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePackOfBWitStatement.lean#L17), [TopReadAtOfBWitStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopReadAtOfBWitStatement.lean#L18) and [HypLAtPointsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypLAtPointsStatement.lean#L15). The leading reading is `LeadingReadAt` in [TopReadAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopReadAt.lean#L47), a true package is the one constructor inductive `TruePackAlt` in [TruePack.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePack.lean#L13), and the point conditions are `BundlePointConditions` in [PackB.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PackB.lean#L23). Some details:

- Step 4 of the first proof is the lemma `exists_is_j_pair_val_of_vanishing` at line 46 of TopReadAtOfBWit.lean, and step 7 is `reads_pk_alt` at line 62, through `to_map_pr_x_eq_pk_at` at line 38. These three lemmas sit in `section True`, from line 33.
- In the first proof, the third output of `colsStd_of_bWit_alt` (the standard twist condition) is discarded with `-` (line 76); the fifth output is passed instead.
- The point conditions have ten fields, but the proof of the bundle witness theorem does not use `rS`, the field $1 \leq r_S$.
- The degree hypothesis is `HypL` in Development/AbelianVarietyTheory/Definitions/LatticeFrames/VanishingGramTermsBoundParams.lean at line 12. The eventual rows are `RowE` and `EvP` of Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean (lines 261 and 130), and the implication of step 3 of the last proof is `evP_hypL` in DegreeHypothesisAllMembers.lean. The theorem is used by `puNZ_member_alt` (PuNZMember.lean), and also in AdmissibleRanksOfMass.lean and MemberSizes.lean.
- The name `degHypL_all_linked_good_members` speaks of members, and the statement is a row over the good linked bundles.
- We have not opened `colsStd_of_bWit_alt`, `characters_match_bundle_alt`, `pkHyp_of_real_alt`, `exists_valEqv_of_bWit_std`, `unit_gram_family_property_alt`, the three level lemmas of step 6 of the first proof, nor the two trace bound rows.
