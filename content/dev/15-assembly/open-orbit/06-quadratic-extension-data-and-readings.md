---
title: Quadratic extension data and readings
decls:
  - GlobalTheory.T.exists_quadratic_extension_reads_of_true
  - GlobalTheory.Fam.readsExists_alt
  - GlobalTheory.T.exists_quadratic_extension_reads_low_of_true
  - GlobalTheory.LowJoin.exists_quadratic_extension_readsLow
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quadratic extension data and readings

This section builds the local data at the places of a twist set. Fix a geometric family $a$ and a twist index $t$. At each place $P$ of $Q(t)$ the family has a local group, and we attach to it a local quadratic extension datum, with its sets of characters at each level and its weights. A quadratic extension datum for $(a, t)$ collects these local data over all places of $Q(t)$ and joins their character sets to the global index sets of the tuple. The main result says that a quadratic extension datum with full readings exists. It is used in the next two sections, where the rescaling by roots of unity and the volumes are computed on such a datum, and through them in [the Theorem on the column side](/entry/true-geometry-family-invariance-alt/).

We keep the notation of [the section on family conditions](/entry/fam-all-q-of-all-true-alt/): $D = I(l, Z)$, $W$ is a real package over $D$ with top level $m \geq 2$, and $a$ is a geometric family for $W$ and a word $u$. For a twist index $t$ let $\chi_K(t, j)$ be the twisted character of $t$ at level $j$.

**Definition 4.6.1 (Quadratic extension datum).** Let $a$ be a geometric family and $t$ a twist index. A *quadratic extension datum* $J$ for $(a, t)$ consists of:

1. index sets $\mathrm{Ch}_0(j)$ for $j \geq 0$ and tuple adelic data $A$ on these sets for the tuple of $t$; the datum $A$ has characters $A.\mathrm{chr}(j)$, base points, compact open subgroups $A.U_j(\beta)$, elements $A.k_b(j, \beta)$ and $A.k_A(j, \beta)$, and functions $A.\xi_j(\beta, \gamma)$ for $\beta \in \mathrm{Ch}_0(j)$, $\gamma \in \mathrm{Ch}_0(j + 1)$;
2. a number $r$ and places $P_1, \dots, P_r$ of $E$ in $Q(t)$; we write $G_i$ for the local group of $a$ at $P_i$, with local field $k_i$ and level $s_i$;
3. for each $i$, a local quadratic extension datum $E_i$ at $G_i$ for the characters $\chi_K(t, \cdot)$, with character sets $E_i.\mathrm{Ch}(j)$, weights $E_i.\mathrm{wt}_j$ and local level vectors $E_i.dL_j$;
4. a bad prime of the tuple for each $i$, signs $\mathrm{sg}_i \in \mathbb{C}$, and the continuity of the additive character of $k_i$;
5. maps $\pi_{i, j} : \mathrm{Ch}_0(j) \to E_i.\mathrm{Ch}(j)$ and $\iota_j : \prod_i E_i.\mathrm{Ch}(j) \to \mathrm{Ch}_0(j)$.

We write $\mathrm{Ch}(j) = \prod_i E_i.\mathrm{Ch}(j)$ and, for $\alpha \in \mathrm{Ch}(j)$, $\mathrm{wt}_j(\alpha) = \prod_i E_i.\mathrm{wt}_j(\alpha_i)$.

So $\iota_j$ joins a family of local characters, one at each place of $Q(t)$, into one global index, and $\pi_{i, j}$ reads off the local character at $P_i$ of a global index.

**Definition 4.6.2 (Readings).** Let $J$ be a quadratic extension datum for $(a, t)$. The *common readings* of $J$ are the following conditions.

1. The tuple data $A$ are good.
2. The places $P_i$ are distinct and every place of $Q(t)$ is some $P_i$.
3. For $j < m$, $A.\mathrm{chr}(j + 1) = \chi_K(t, j)$.
4. Each $G_i$ satisfies the residual condition for the discriminant of $E_i$ and the local residual character of $t$ at $P_i$.
5. The bad prime of index $i$ lies over $P_i$, and $\mathrm{sg}_i = \pm 1$.
6. Each $E_i$, twisted by $\mathrm{sg}_i$, is the twist of the tuple at its bad prime, and the matrix space of $E_i$ is the matrix space of the tuple.
7. For $j < m$ and $j + d = s_i$, the local representation of $E_i$ at $\pi_{i, j}(\beta)$ is the completion at $P_i$ of the global index $\beta$.
8. The set $\mathrm{Ch}_0(m)$ has exactly one element.

$J$ *reads* if, in addition to the common readings:

9. at each place and each index of level $s_i + 1$, the coset of $E_i$ is the coset of the base point of $A$ in every ordered frame;
10. $A.k_b(j, \beta)$ is the standard element of level $j$ for $j + 1 < m$;
11. at the level $j = m - 1$, each $A.k_A(j, \beta)$ is a product $k_0 h$, where $k_0 \in G_f(X_j)$ reduces to the standard element of level $j$ and $h$ is supported at the places of the $G_i$, with a prescribed block form at the places with $s_i + 1 = j$;
12. $\pi_{i, j}(\iota_j(y)) = y_i$ for $j \leq m$;
13. the base points at level $s + 1$ of the local groups of $a$ are integral in every ordered frame;
14. the tuple data are live along the maps $\iota_j$.

$J$ *reads in standard form* if it satisfies the common readings, condition 12, 13, 14, condition 10 for all $j < m$, and in place of 9 an orbit condition of the same shape. $J$ *reads low* if it satisfies the common readings, condition 10 for all $j < m$, and:

- $\pi_{i, j}(\iota_j(y)) = y_i$ for $j \leq m$ with $j + 1 \neq m$;
- $\iota_j$ is injective for $j + 1 \neq m$, and $\iota_0$ and $\iota_m$ are onto;
- for $j + 1 \leq m$ with $j + 2 \neq m$, the function $A.\xi_j(\alpha, \gamma)$ vanishes for every $\gamma$ outside the image of $\iota_{j + 1}$.

The low readings ask nothing at the level $m - 1$, where the local groups have their top character sets. The two later steps, to standard form and to full readings, fix the orbit and coset conditions there.

**Theorem 4.6.3 (Low readings exist).** Let $W$ be a real package over $D = I(l, Z)$ that satisfies the family conditions on a package. Let $a$ be a geometric family for $W$ and $u$ that is good and true and whose commutation datum is good. Then for every twist index $t$ there is a quadratic extension datum for $(a, t)$ that reads low.

Lean: `GlobalTheory.LowJoin.exists_quadratic_extension_readsLow` (also `GlobalTheory.T.exists_quadratic_extension_reads_low_of_true`, a second name).

*Proof.* We use the validity of the real package, the conditions on the geometric families and the twist condition of $W$, and the pins of $a$.

1. The validity of $W$ and its pins give, by a result of another chapter, index sets $\mathrm{Ch}_0$ and good tuple data $A$ for the tuple of $t$ with standard base points: $\mathrm{Ch}_0(m)$ has one element, each index set at an index of the tuple is nonempty, and $A.k_b(j, \beta)$ is standard for $j < m$.
2. The character of $W$ at level $j$ and the condition of the families on $\xi$ give that $A.\mathrm{chr}(j + 1)$ and $\chi_K(t, j)$ are both equal, as characters, to the product of the base character $\mu_0$ at level $j$ with the character $\xi$ of the tuple. Since such a character is unique, $A.\mathrm{chr}(j + 1) = \chi_K(t, j)$ for $j < m$.
3. Enumerate $Q(t)$ as $P_1, \dots, P_r$. This gives condition 2 of the readings. By the conditions on the families, each $P_i$ is a bad prime of the tuple, and it lies outside a fixed set of places of the base data. Let $G_i$ be the local group of $a$ at $P_i$; its level satisfies $s_i + 2 = m$.
4. For each $i$, a result of another chapter, applied with the twist condition of $W$, the good commutation datum and the standard pin of $a$, gives a local quadratic extension datum $E_i$ at $G_i$ with a sign $\mathrm{sg}_i = \pm 1$. It has the right twist and matrix space, its additive character is continuous, and its local representations at levels $j \leq s_i$ are exactly the completions at $P_i$ of the rational twist automorphisms of level $j$.
5. By the decomposition of the twist index set as a product of local representatives, for each $j \leq m - 2$ there is a bijection between the global index set of level $j$ and $\mathrm{Ch}(j) = \prod_i E_i.\mathrm{Ch}(j)$, compatible with the local representations at each $P_i$.
6. We define $\pi$ and $\iota$ level by level, by the three cases $j + 1 < m$, $j + 1 = m$ and $j + 1 > m$. For $j + 1 < m$ we compose the bijection of step 5 with the bijection between the index set of $A$ at $j$ and the global index set; then $\iota_j$ is a bijection and $\pi_{i, j}(\iota_j(y)) = y_i$. For $j = m - 1$ each $E_i.\mathrm{Ch}(j)$ is nonempty, since $j = s_i + 1$ and $E_i$ has a coset there, and $\mathrm{Ch}_0(j)$ is nonempty; we take $\pi$ and $\iota$ constant. For $j \geq m$ each $E_i.\mathrm{Ch}(j)$ has one element, since $E_i$ has one character at the top level and above; we take $\pi$ and $\iota$ constant again, and $\iota_m$ is onto because $\mathrm{Ch}_0(m)$ has one element.
7. The residual condition at $G_i$ follows from the twist of $E_i$, the level condition of $W$ and the bottom hypothesis of the package. The other common readings were found in steps 1 to 4, and condition 7 holds by the compatibility of step 5 for $j + 1 < m$ and by $s_i + 2 = m$ in the other cases.
8. For the last condition of the low readings, let $j + 1 \leq m$ with $j + 2 \neq m$. Then $(j + 1) + 1 \neq m$, so by step 6, $\iota_{j + 1}$ is onto. Hence no $\gamma$ lies outside its image, and the condition holds.

Injectivity of $\iota_j$ for $j + 1 \neq m$ and the surjectivity of $\iota_0$ follow from step 6. $\square$

**Theorem 4.6.4 (Readings exist).** Let $W$, $u$ and $a$ be as in the previous theorem. Then for every twist index $t$ there is a quadratic extension datum for $(a, t)$ that reads.

Lean: `GlobalTheory.Fam.readsExists_alt` (also `GlobalTheory.T.exists_quadratic_extension_reads_of_true`, a second name).

*Proof.* By the previous theorem there is a datum $J$ that reads low. A commutation identity, proved in another chapter, gives from $J$ a datum $J'$ for $(a, t)$ that reads in standard form. A commutation property, also proved there, gives from $J'$ a datum $J''$ that reads. $\square$

The datum that reads is used through conditions 10 and 11 in [the section on volumes](/entry/vol-level-wt-const-alt/), and through the characters and the local level vectors in [the section on rescaling](/entry/dat-exists/).

**Remark 4.6.5 (Formalization).** The structure and the full readings are in [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L23), with `Reads` at line 42; the standard and low readings are `ReadsStd` and `ReadsLow` in [ReadsLow.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsLow.lean#L23). The low readings theorem is at [ExistsReadsLow.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsReadsLow.lean#L33), under `maxHeartbeats 2000000`, and the readings theorem at [ReadsExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsExists.lean#L21). The second names, at [ExistsReadsLowStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsReadsLowStatement.lean#L19) and [ReadsExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsExistsStatement.lean#L18), only pass the hypotheses on. Both theorems take the hypothesis `a.Is` that $a$ is good, but the low readings theorem drops it in its `intro` (the pattern `_`); so the goodness of $a$ is passed on only to the two steps after it. The last condition `dead` of `ReadsLow` is proved by `absurd`, as in step 8, so it holds for every datum built this way. The two steps of the readings theorem are `true_geometry_commutation_identity_alt` and `true_geometry_commutation_property_alt`; the theorem names do not describe the statements. Step 1 is `exists_tupleAdelicData_standardBasePoints`, step 2 `chrEq_mul` and `chrEq_unique`, step 4 `exists_good`, step 5 `exists_bij` with `twistIndexSet_eq_prod_localRepresentatives`, and step 7 `res_of_tw`. We did not unfold `TwDat`, `QExt`, `BadPr`, `AtTwist`, `IsGL`, `Live` or the residual condition `Res`.
