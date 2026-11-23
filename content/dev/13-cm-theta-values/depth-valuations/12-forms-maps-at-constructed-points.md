---
title: Forms maps at constructed points
decls:
- GlobalTheory.T.referenceChainEvaluationAtBundlePoints_of_overCols
- GlobalTheory.Fc.PeriodEntriesOverColumns.referenceChainEvaluation_bundlePoints_overColumns
- GlobalTheory.Fc.PeriodEntriesOverColumns.constructedPoint_referenceChainWord_formsMap
- GlobalTheory.T.aux_of_ok_of_pins
- GlobalTheory.Mem.Col2.TC.formsMap_at_every_trueColumnMember
- GlobalTheory.RedPt0.formsMap_of_symmetricComparison_lowerMap_finiteChar
- GlobalTheory.Fc.ClassTwoEntries.divisionSecondComplement_constructedPoints
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Forms maps at constructed points

This section proves two row statements about constructed points. The first says that at every point of a slot over columns the forms map of every word has five properties: the class map is injective, the stabilizer maps are bijective, the forms go to the point space, the point map is rational and integral with a bound at every infinite place, and the point map is bounded for the Petersson norms. The second says that the inputs of the second complement hold along every family of constructed points, for every slot. Both rows feed the period entries and the class two entries of the global theory, beside the level prime row of [the sharp column valuations](/entry/cm-theta-values/depth-valuations/#sharp-column-valuations-at-level-primes). The first row is the longer one. It goes down through the true columns view to a single datum and a single word, where it becomes a statement about a symmetric system of forms.

### The five properties of a forms map

We keep the notation of the section on sharp column valuations: a datum $D$, a word $u$ of $D$, the top level $m$ and the CM field $L$ of the member datum at $u$. The member datum at $u$ has a finite set $\mathrm{Cl}'$ of classes one level below the top, a class map $t$ from $\mathrm{Cl}'$ to the classes at the top level, and for each class $c$ a stabilizer map $s_c$. It has a space $F_m$ of forms at the top level, a Hermitian lattice $\Lambda_m$ over $L$, a point space with a subspace $P_C$ and a Hermitian lattice $\Lambda_P$, and an embedding $\varepsilon$ of $L$ into $\mathbb{C}$. The *point map* is $\mathrm{Pt} = \lambda \circ \mathrm{ev}_0$, the evaluation at zero followed by the lower map. For each embedding $\tau$ the datum has a degree $d_\tau$ and a positive real number $\beta_\tau$, and with $T = T(u)$ we put
$$B_{\mathrm{pt}} = \prod_\tau T^{-d_\tau}\, \beta_\tau^2 .$$
When the point map is rational, a proof $h$ of rationality gives an $L$-linear map $\mathrm{Pt}_h$ from $\Lambda_m \otimes \mathbb{Q}$ to $\Lambda_P \otimes \mathbb{Q}$. For an infinite place $v$ of $L$ write $\|x\|_v^2$ for the real part of the majorant at $v$. We did not unfold the class map, the stabilizer maps, the forms, the lower map, the integrality of $\mathrm{Pt}_h$ or the Petersson products $\langle\ ,\ \rangle_P$ and $\langle\ ,\ \rangle_m$.

**Definition 4.12.1 (forms map properties).** The *forms map properties* of $D$ at $u$ are the following five statements.
1. The class map $t$ is injective.
2. Every stabilizer map $s_c$ is bijective.
3. For every $\varphi \in F_m$, $\mathrm{Pt}(\varphi) \in P_C$.
4. There is a proof $h$ of rationality such that $\mathrm{Pt}_h$ is integral and $\|\mathrm{Pt}_h x\|_v^2 \le B_{\mathrm{pt}} \|x\|_v^2$ for every infinite place $v$ of $L$ and every $x \in \Lambda_m \otimes \mathbb{Q}$.
5. For every $\varphi \in F_m$, $\mathrm{Re}\,\langle \mathrm{Pt}(\varphi), \mathrm{Pt}(\varphi)\rangle_P \le B_{\mathrm{pt}}\, \mathrm{Re}\,\langle \varphi, \varphi \rangle_m$.

The first four are the clauses of [the class map of a symmetric system](/entry/symmetric-level-clauses-hold/), except that part 4 also asks for integrality. Part 5 is a norm bound on the forms themselves rather than on lattice vectors.

### A single datum

A *symmetric system* $T$ of forms at $u$, for a family of characters on the classes, is the object of the theorem on the class map of a symmetric system. At the top level it carries a level structure with a finite group $U$ and a character $\chi : U \to \mathbb{C}^\times$. Two conditions on $T$ come from the same theorem: the *tie of the lower map*, and the *branching norm identity*, which says that each $\beta_\tau$ equals the operator norm of the standard branching map at $\tau$. We say that the *top character is finite and rational* if there is $n > 0$ with $\chi(x)^n = 1$ for all $x \in U$, and every value $\chi(x)$ is $\varepsilon(r)$ for some $r \in L$.

**Theorem 4.12.2 (forms map from a symmetric comparison).** Let $T$ be a symmetric system of forms of $D$ at $u$. Assume the tie of the lower map, the branching norm identity, and that the top character of $T$ is finite and rational. Then the forms map properties of $D$ at $u$ hold.

Lean: `GlobalTheory.RedPt0.formsMap_of_symmetricComparison_lowerMap_finiteChar`

*Proof.* Step 1. From the three hypotheses there is a *pending object* $P$ whose branching maps are branching maps for the standard pair at every $\tau$. A pending object gives coordinates at each place for the forms at the top level and for the points, and $P$ expresses the point map in those coordinates through its branching maps. Its existence is the step that uses the finiteness and rationality of the top character.

Step 2. By the theorem on the class map of a symmetric system, which needs only the tie of the lower map and the branching norm identity, the class map is injective, the stabilizer maps are bijective, every $\mathrm{Pt}(\varphi)$ lies in $P_C$, and the bound $\|\mathrm{Pt}_h x\|_v^2 \le B_{\mathrm{pt}}\|x\|_v^2$ holds for every proof $h$ of rationality, every place $v$ and every $x$. This gives parts 1, 2 and 3.

Step 3. Since the branching maps of $P$ are branching maps and the forms go to $P_C$, the point map is rational: this gives a proof $h$ of rationality. For this $h$ the map $\mathrm{Pt}_h$ is integral. The bound of Step 2 at $h$ completes part 4.

Step 4. For part 5, write $\varphi \in F_m$ as $\sum_a z_a e_a$, where $e_a$ are the images in $F_m$ of a basis $b_a$ of $\Lambda_m$ and $z_a \in \mathbb{C}$. Both sides of the inequality are Hermitian forms in $z$, so the set of $z$ where it holds is closed. When every $z_a$ is $\varepsilon(r_a)$ with $r_a \in L$, the form $\varphi$ is the image of $x = \sum_a r_a b_a$, and the inequality is the bound of Step 2 at $h$, at $x$ and at the place induced by $\varepsilon$. Since $\varepsilon(L)$ is dense in $\mathbb{C}$, these $z$ are dense, and the inequality holds for all $z$. $\square$

### True column members

A *true column datum* $I$ over a base $B$ is the datum of the section on sharp column valuations, with its laws $l$ and later stages $Z$. It assembles a datum $D(l, Z)$. The datum $I$ may be *good* and the base may carry *pins*. Neither condition is unfolded here.

**Theorem 4.12.3 (forms map at true column members).** Let $I$ be a good true column datum over a base $B$ with pins, let $l$ be laws for $I$, and let $Z$ be later stages. Then the forms map properties of $D(l, Z)$ hold at every word $u$.

Lean: `GlobalTheory.T.aux_of_ok_of_pins` (also `GlobalTheory.Mem.Col2.TC.formsMap_at_every_trueColumnMember`, a second name).

*Proof.* Step 1. By [the standard tied symmetric columns](/entry/cols-tied-sym-std/), there is a system of columns of $D(l, Z)$ that is standard, with a symmetric system of forms $T_u$ at each word $u$ that is standard at the level of $u$.

Step 2. Fix $u$. The lower map of a standard symmetric system is tied, so $T_u$ satisfies the tie of the lower map.

Step 3. The branching norm identity holds at every word of $D(l, Z)$. This is the branching norm identity for true column members.

Step 4. The coefficient field $L$ contains a primitive root of unity of order $g_i$ and one of order $g_i - 1$, for $i = 0, 1$, where $g_0, g_1$ are the two natural numbers of the host datum. From these roots of unity the top character of $T_u$ is finite and rational.

Step 5. The theorem on the forms map from a symmetric comparison now applies to $T_u$. $\square$

### The two rows

We use the slots, the bundles, the links and the family classes of the section on sharp column valuations. For a datum $D$ let $R_6(D)$ say that the forms map properties of $D$ hold at every word. The *reference chain row* of a slot $Q$ and a link of bundles says: there is a bundle property that holds eventually at all points in $Q$ and all linked bundles, and for each class $\mathcal{A}$ and selection for it, $R_6(F.D(x, i))$ holds for all $i$ and all large $x$, [closed](/step/closed-def/) on the class $W_3(\mathcal{A})$. Here $W_3(\mathcal{A})$ is the class of families in $\mathcal{A}$ that satisfy the divisibility, tameness, box, row, smoothness, twist and choice conditions of the global theory, a bound by $9$ on the cylinder index, and two size conditions. We did not unfold these conditions.

**Theorem 4.12.4 (forms maps at constructed points).** Let $Q$ be a slot over columns and let $\beta$ be a constructed point in $Q$. Then $R_6(\beta.D)$ holds.

Lean: `GlobalTheory.Fc.PeriodEntriesOverColumns.constructedPoint_referenceChainWord_formsMap`

*Proof.* Since $Q$ is over columns, $\beta$ comes from a column datum $w$, later stages $Z$, an object and a column view. A property of the pair $(D, O)$ that holds at $(w.D(Z), O)$ for every such $w$, $Z$ and $O$ holds at every point over columns, by the true columns view. The column datum $w$ carries a good true column datum with pins and laws, and $w.D(Z)$ is its datum $D(l, Z)$. The theorem on true column members gives $R_6$ there. $\square$

**Theorem 4.12.5 (reference chain row).** Let $Q$ be a slot over columns. Then for every bundle type and every link the reference chain row of $Q$ holds.

Lean: `GlobalTheory.T.referenceChainEvaluationAtBundlePoints_of_overCols` (also `GlobalTheory.Fc.PeriodEntriesOverColumns.referenceChainEvaluation_bundlePoints_overColumns`, a second name).

*Proof.* Step 1. As in the level prime row, the row for any bundle type and link follows from the row for the trivial bundle type, so the bundles play no role.

Step 2. By the previous theorem $R_6(\beta.D)$ holds at every constructed point in $Q$, for all parameters. A property that holds at every constructed point in $Q$ gives a row for the trivial bundle type: take the bundle property to be the property itself. Closedness then holds with threshold $\varepsilon_1 = 1$, the zero size bound and starting point $x_0 = 0$, since every point of a selected family satisfies the property. $\square$

The second row has no hypothesis on the slot. For a family $F$ the *second complement inputs* say that there are constants $C_{\deg}, C_g, C_T, C_G, C_d, C_I$ with $C_g \ge 0$ and a point $x_0$ such that for all $x \ge x_0$ and all $i$ the datum $F.D(x, i)$ satisfies eight conditions: the level primes are not type primes, the norms decompose, the degrees are counted by $C_{\deg}$, the type primes have size bounded by $C_{\deg}$ and $C_g$, the level primes fit in a budget $C_T$, the stabilizers have logarithm bounded by $C_G$, the discriminant offset is bounded by $C_d$, and the loss at inert primes is bounded by $C_I$. We did not unfold the eight conditions. They give the isotypic rank bound with constant $2C_g + C_T + C_G + C_d + C_I$.

**Theorem 4.12.6 (second complement at constructed points).** For every bundle type, every slot $Q$ and every link, the *second complement row* holds: there is a bundle property that holds eventually at all points in $Q$, and for each class $\mathcal{A}$ and selection, the second complement inputs are closed on $W_3(\mathcal{A})$.

Lean: `GlobalTheory.Fc.ClassTwoEntries.divisionSecondComplement_constructedPoints`

*Proof.* Step 1. By Step 1 of the previous proof, it suffices to treat the trivial bundle type. A property of classes alone that holds for every class gives such a row, with the trivial selection.

Step 2. Fix $\mathcal{A}$. Every family in $W_3(\mathcal{A})$ satisfies the two size conditions. We show that the second complement inputs are closed on any class whose families satisfy the two size conditions. Take $\varepsilon_1 = 1/100$ and any size bound. Let $0 < \varepsilon \le 1/100$, so $\varepsilon < 1/52$. By [the admissible second complement along a family](/entry/admissible-complement-two-along-family/), every family with parameter $\varepsilon$ in $(0, 1/52)$ that satisfies the two size conditions satisfies the second complement inputs. $\square$

**Remark 4.12.7 (Formalization).** All the `T.` statements here are relays: `first | exact @…` under `maxHeartbeats 1000000` ([ReferenceChainEvaluationBundlePointsOverColumnsAStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsAStatement.lean#L8), [FormsMapAtEveryTrueColumnMemberStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FormsMapAtEveryTrueColumnMemberStatement.lean#L8)). The names "reference chain evaluation" and "aux_of_ok_of_pins" describe nothing in the statements, which are about the five forms map properties, `Conclusion6` ([ProductFirstZerothParts.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/ProductFirstZerothParts.lean#L334)). In `constructedPoint_referenceChainWord_formsMap` the column view, the base signs and `RealTied` are wildcards and are not used ([ReferenceChainEvaluationBundlePointsOverColumnsA.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsA.lean#L15)). In `formsMap_of_symmetricComparison_lowerMap_finiteChar` the class map clauses come whole from `symmetric_level_clauses_hold`, which gives the bound at every place and every $h$, and the pending object serves only for rationality and integrality ([FiniteModelOfAdmissibleTransports.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/FiniteModelOfAdmissibleTransports.lean#L2259)). `beOnTie_true` ignores goodness and pins ([BranchingNormIdentityTrueColumnsMembers.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/BranchingNormIdentityTrueColumnsMembers.lean#L62)), and `trueCols_exists_primitiveRoots` takes no pins. In the closedness of the row the thresholds are $1$, zero and $0$, so "eventually" is "always" ([ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L388)). In `admissibleConstants_closed_under_sizeBounds` the size bound is an arbitrary element built from zeros and the largeness hypothesis is not used ([AdmissibleConstantsClosedUnderSizeBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdmissibleConstantsClosedUnderSizeBounds.lean#L13)). We did not open the proofs of the pending object, of the standard tied columns, of the branching norm identity or of the primitive roots.
