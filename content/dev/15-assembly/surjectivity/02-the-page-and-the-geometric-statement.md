---
title: The page and the geometric statement
decls:
  - GlobalTheory.BigOn.geoSt_of_pageSt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The page and the geometric statement

This section proves the geometric statement about the record objects of a family from the page statement. The page statement holds with no hypothesis; it is a list of numerical facts about the record objects. The geometric statement gives the lattices of a record object at the twisted places: they are full, stable under the finite group, and they satisfy an index bound and four depth bounds. The surjectivity statement of [Section 5.10.7](/entry/onto-x-of-hypotheses-alt-alt/) uses the geometric statement twice: for the rank statement and for the last assembly. Below the theorem of this section there are 5,131 declarations, and 4,843 of them are below [the depth bound for record objects](/entry/leaf-depth-all-record/).

Fix a family $\mathcal{F}$ and a point $p$ of it. The point carries two *runs*: two parameter runs at two special primes of the host field, and a level structure for the finite group of $p$. Section 3 gives them. A *record object* $O$ at $p$ along a pair of runs $r$ is an object that the runs record. It carries, for each level $j$, a representation $\rho_j$ of a finite group $P$ on $K^{n_j}$, a subgroup $U \subseteq P$ with a character $\psi$, lattices $M_j$, and at each finite place $v$ lattices $\Theta_v, \Theta^K_v, \Theta^0_v$ and exponents $e_0(v, j)$, with some real constants.

**Definition 5.2.1 (Constant record).** A *constant record* is a triple $c = (C, C_{b1}, C_{b2})$ of real numbers. It is *bad* if

$$\begin{aligned} C_{b1} &\ge 14, \\ C_{b2} &\ge 66 C + 4. \end{aligned}$$

Lean: `Formalism.L2.Indef.Tree.OnPage.ConstBad`.

**Definition 5.2.2 (For all record objects).** Let $Q$ be a property of record objects. The statement *$Q$ holds at all record objects* is the closed property, for the class $\mathcal{C}_{\mathrm{fam}}$, of $(\mathcal{F}, C_H)$: there is $c_0$ such that for each bad constant record $c$ with $C \ge c_0$, eventually at the points of $\mathcal{F}$, for each rich point $p$, each pair of runs $r$ at $p$ and each object $O$ recorded at $p$ along $r$, $Q(O)$ holds.

Lean: `GlobalTheory.BigOn.ForallRecordObjects`.

**Definition 5.2.3 (Page statement).** The *page statement* says that the following nine facts hold at all record objects $O$, with $b$ the size constant of the point.

1. The constants of $O$ are at least $1$, $f \ge 8$, and the numbers $g_1, g_2, q_1, d$ are four distinct primes outside a finite set $s_m$.
2. The sizes of $O$ satisfy the size conditions.
3. The height of $O$ satisfies the condition on $x$.
4. The bad constants of $O$ satisfy their bound.
5. The level of $O$ is a square in the sense of the level condition at the residue data and $f$.
6. The bound on $y$ holds.
7. $O.b = b$.
8. $E_{1u} \ge 0$.
9. For all $C$ and $C_H$, the error constant of the scale $N(C, C_H)$ is given by its defining formula.

Lean: `GlobalTheory.BigOn.PageStatement`.

**Definition 5.2.4 (Geometric statement).** The *geometric statement* says that the following facts hold at all record objects $O$.

1. Each $M_j$ is a full lattice and is stable under $\rho_j(P)$.
2. At each twisted place $w$ and at $\bar w$, $\Theta_v$ and $\Theta^K_v$ are full lattices; $\Theta_v \subseteq M_j$ is stable under $P$ and lies in $\sigma \Theta^K_v$ for some $\sigma \ne 0$; $\Theta^0_v$ is finitely generated, lies in the $(U, \psi)$-eigenspace and contains $|U|$ times the cut of $\Theta^K_v$.
3. There are lattices $\Theta^1_v$ and constants that bound the index of $M_j \cap W$ over $\Theta^1_v \cap W$ for each subspace $W$.
4. For all $C$ and $C_H$, four depth bounds hold for the scale $N(C, C_H)$: bounds on $e_0(w, j)$ and $e_0(\bar w, j)$ at twisted places $w$, one for each kind of residue characteristic. The kinds are: $q_1$ or $d$; a prime in $s_m$; $g_1$ or $g_2$; all other primes.

Lean: `GlobalTheory.BigOn.GeometricStatement'`.

Facts 1 and 2 are the lattice facts. Fact 3 is the index bound. Fact 4 bounds the depth of the lattices at the places that the scale counts.

**Theorem 5.2.5 (The geometric statement).** The page statement implies the geometric statement.

Lean: `GlobalTheory.BigOn.geoSt_of_pageSt_alt` (also `GlobalTheory.T.geoSt_of_pageSt'`, a second name).

*Proof.* We first collect four facts along the family.

1. From the core ties at a point, there are a constant $C_K$ and a height $x_a$ such that the runs hold for each pair of runs that satisfies the core ties and a numerical condition at $x_a$.
2. There is a height $x_b$ such that facts 1 and 2 of the geometric statement hold at each record object, if the runs hold, the numerical condition holds at $x_b$, and the group and tuple conditions hold. This is [the leaf, span and data theorem](/entry/leaves-sup-span-data/).
3. There is a constant $C_d$ such that the four depth bounds hold at each record object $O$, if $O$ satisfies facts 1 and 2 of the page statement and the height satisfies some size conditions. This is [the depth bound for record objects](/entry/leaf-depth-all-record/). It also uses an equality of contents of the split part at an indefinite point.
4. Eventually along the family, the numerical condition holds at $x_a$ and at $x_b$, and the size conditions of step 3 hold.

Now take the page statement and the facts of step 4. Choose $c_0$ and the height threshold as the largest of the constants that they give. Let $p$ be a rich point beyond the threshold, $r$ a pair of runs at $p$ and $O$ a record object. The places of single index of $p$ are twisted; so $p$ has links, and these give the group and tuple conditions. Step 1 gives that the runs hold. Step 2 gives facts 1 and 2 of the geometric statement. The index bound, fact 3, follows from the runs, facts 1 and 2, and the equation $O.b = b$ of the page statement. Step 3 gives fact 4. $\square$

The proof uses only facts 1, 2 and 7 of the page statement. The other facts are used again in Section 10, where the page statement enters the final assembly.

**Remark 5.2.6 (Formalization).** The theorem is in [GeoStOfPageSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeoStOfPageSt.lean#L21), and the two statements are in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L37). The proof drops six of the nine page facts at line 34. The section `Comparison₂` at lines 17 to 20 is empty: it declares variables and nothing else. The second name in GeoStOfPageStStatement.lean is a one-line call with `maxHeartbeats` set to 1000000. We have not unfolded the closed class of families, the record relation, the condition that the runs hold, the numerical condition or the facts 2 to 6 and 9 of the page statement; we give them by their roles. The index bound is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L77).
