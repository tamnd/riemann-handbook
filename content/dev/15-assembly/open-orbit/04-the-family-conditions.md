---
title: The family conditions
decls:
  - GlobalTheory.T.true_geometry_family_row_data_alt
  - GlobalTheory.MiTop.famAllQ_of_allTrue_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The family conditions

This section proves step 2 of [the period identity from the family conditions on a package](/entry/mi-star2-of-all-true-alt-alt/). For a real package $W$ that satisfies the family conditions, we find one central element $z$ of the finite adelic unitary group of $Y_0$ and, for each word $u$, a family character and a bottom datum with eight properties. These are the inputs of [the period identity from the family conditions](/entry/mi-star2-of-pu-nz/). The proof puts together four constructions, each proved in a later section or in the second part of the chapter: a central pin, a geometric family, a row choice and a column choice.

Fix $D = I(l, Z)$ and a real package $W$ over $D$, as in [the previous section](/entry/mi-at-of-true-pack-alt-alt/). Let $m$ be the top level of $D$.

A *geometric family* $a$ for $W$ and a word $u$ is a geometry $g$ (lattices $L_j$, vacuum vectors $\mathrm{vac}_j$, adelic elements $b_j$ and $b_T$, volumes and a top matrix $i_A$), a linear map $j$, a nonarchimedean local field $k$, commuting vector data $v$, type data $o$, local groups $G_1, \dots, G_n$ at the places of the set $P_g$, local data $a.Q(P, t)$ at the places $P$ of each twist set $Q(t)$, a bottom datum and a sequence $c_0$. Two predicates on geometric families matter: $a$ is *good* if twelve conditions hold (on the measures, the volumes, the shape, the ties, a top reading and others), and $a$ is *true* if four conditions hold (pins, a standard form, an embedding and the vector at zero). A *row choice* gives a row for each twist index $t$, and a *column choice* gives a column for each $t$. A geometric family $a$ with a row choice and a column choice gives a *family character* $f = a(\mathrm{row}, \mathrm{col})$: a geometry $f.g$, a linear map $f.j$ and, for each $t$, a tuple $f.t(t)$ with columns $\mathrm{col}_j$, ramified columns at each level, tails, periods and two coefficients $c^{\mathrm{top}}_n(t)$ and $c^{\mathrm{bot}}(t)$.

**Definition 4.4.1 (Bottom datum and pin).** A *bottom datum* $d$ for $W$ and $u$ is a Bessel datum $\mathcal{B}$ on $X_0$ with an embedding $\iota_{\mathcal{B}} : G(X_0) \to G(Y_0)$, elements $b, k \in G(Y_0)$ and $a_0, a \in G(X_0)$, and a period map $d.\mathrm{per}$. For $z \in G(Y_0)$, the datum $d$ is *pinned at* $z$ if: $\mathcal{B}$ is adapted to the weight of the twist of $u$ and $a_0$ is a transport adelic correction; $a \in G_f(X_0)$ is central in $G(X_0)$; $k$ lies in the level set $J_W$; and

$$\iota_{\mathcal{B}}(a_0 a)\, b = x_u \, z \, t_S \, k,$$

where $x_u \in G(Y_0)$ is the base point of $u$ and $t_S \in G(Y_0)$ is the translation element of $W$.

Let $\mu_0$ be the base twist index, and for an index $t$ let $S_t$ be the set of rational primes $p$ that lie in a place of $Q(t)$.

**Definition 4.4.2 (Unit ratio).** Let $S$ be a set of primes and $x, y \in \mathbb{C}$. We say that $x/y$ is an $S$-*unit ratio* if $y \neq 0$ and there are $N > 0$ and a rational number $r \neq 0$ with $(x/y)^N = r$ and $v_p(r) = 0$ for each prime $p \notin S$.

For instance, if $x = c\,\zeta$ and $y = c\,\zeta'$ with $c \neq 0$ and $\zeta, \zeta'$ roots of unity, then $x/y$ is an $S$-unit ratio for every $S$, with $r = 1$.

**Definition 4.4.3 (Family conditions on characters).** Let $W$ be a real package over $D$. The *family conditions* $\mathrm{FAC}(W)$ say: there is $z \in G_f(Y_0)$, central in $G(Y_0)$, such that for each word $u$ there are a family character $f$ and a bottom datum $d$ with the following eight properties.

1. *Pin:* $d$ is pinned at $z$.
2. *Place laws:* the tuples $f.t$ satisfy the place laws, nine laws on the commutation datum, local finiteness, a real equality, values, last values, kernels, periods and readings.
3. *Vanishing link:* for each $n$ with $2n + 2 = m$, each $t$ and each row vector $\varphi$, the twisted column $\mathrm{col}^0_t(\varphi)$ is ramified at level $0$, and its level $0$ periods are the periods of $d$: $\mathrm{per}_0(\mathrm{col}^0_t(\varphi), G, y, v) = d.\mathrm{per}(\varphi, G, y, v)$.
4. *Tail link:* for each $n$ with $2n = m$, each $t$, $\varphi$, $F$ and each $G$ whose linear part is the leading linear map of $F$, the tail at level $2n$ of the column $\mathrm{col}_{2n}(\mathrm{col}^0_t(\varphi))$ at $G$ is the column period of $\varphi$ at the image of $F$ under the row map of $t$.
5. *Descent link:* for each $n$ with $2n + 2 = m$, each $t$ and each $F$, there is $G$ whose linear part is the leading linear map of $F$ and whose descent to level $0$ is the row form of $F$.
6. *Surjective link:* for each $n$ with $2n + 2 = m$, each element $T$ of the base row space of $W$ is the descent to level $0$ of some $G$ at $\mu_0$.
7. *Commuting link:* for each $n$ with $2n = m$, there are a linear automorphism $S$ of the space $M_u$ of row vectors, a real $r > 0$ with $\|S\varphi\| = r \|\varphi\|$ for all $\varphi$, and $s \neq 0$, such that for all $t$, $\varphi$ and $F$,

$$\mathrm{tail}_{2n}\bigl(\mathrm{up}_n(\mathrm{col}^0_t(\varphi)), F\bigr) = s \cdot \mathrm{tail}_{2n}\bigl(\mathrm{col}_{2n}(\mathrm{col}^0_t(S\varphi)), F\bigr).$$

8. *Ratio:* for each $n$ with $2n = m$ and each $t$, $c^{\mathrm{top}}_n(t) \neq 0$, and the quotient of $c^{\mathrm{top}}_n(t)/c^{\mathrm{bot}}(t)$ by $c^{\mathrm{top}}_n(\mu_0)/c^{\mathrm{bot}}(\mu_0)$ is an $S_t$-unit ratio.

The conditions 3 to 7 are the *links* between the family character and the rows: the columns at level $0$ are the twisted rows, the tail at the top is a column period, descent recovers the row form, descent is onto, and raising a column commutes with a similarity $S$ up to a scalar. The ratio condition says that the top coefficients of the tuples differ from those at $\mu_0$ by units at the primes outside $S_t$, up to a power.

**Theorem 4.4.4 (Family conditions).** Assume the rapid decay of cusp forms, the discrete series cover, the Harish-Chandra modules and strong approximation for $\mathrm{SU}$. Let $D = I(l, Z)$ and let $W$ be a real package over $D$ that satisfies the family conditions on a package. Assume $r_S \geq 1$ and that $D$ is onto at all levels. Then $\mathrm{FAC}(W)$ holds.

Lean: `GlobalTheory.MiTop.famAllQ_of_allTrue_alt` (also `GlobalTheory.T.true_geometry_family_row_data_alt`, a second name).

*Proof.* We take the steps in order.

1. By [the Theorem on one central pin](/entry/exists-bot-dat-of-placed-p-framed/), from the package hypotheses and $r_S \geq 1$, there is a central $z \in G_f(Y_0)$ such that each placed and framed Bessel datum $\mathcal{B}$ for a family character $f$ carries a bottom datum $d$ with $d.\mathcal{B} = \mathcal{B}$, $d.b = f.g.b_0$, pinned at $z$. We fix this $z$ for all words.
2. Fix $u$. By [the Theorem on true family data](/entry/all-true-family-datum-alt/), from the discrete series cover, the Harish-Chandra modules and strong approximation, there is a geometric family $a$ that is good and true, whose top matrix is $i_A = 1$, and whose Bessel datum $a.\mathcal{B}$ is framed.
3. From the rapid decay of cusp forms, a result of another chapter gives a row choice at the geometry of $a$ in which each row is good and all rows have the same shape.
4. For each choice $k$ of family constants, [the Theorem on the column side](/entry/true-geometry-family-invariance-alt/) gives a column choice with a column condition and an output condition at $k$. Then [the Theorem on column data](/entry/true-geometry-family-column-data-alt/) gives one column choice $\mathrm{col}$ for which $f = a(\mathrm{row}, \mathrm{col})$ has good rows, the place laws, the chart condition at zero, the tail link, the commuting link and the ratio condition.
5. Since the rows of $f$ are good, the commutation datum of $f$ is good. By [the Theorem on placed data](/entry/placed-p-of-true-geometry/), the Bessel datum $a.\mathcal{B}$ is placed for $f$. Since it is also framed, step 1 gives a bottom datum $d$ on $a.\mathcal{B}$, pinned at $z$, with $d.b = f.g.b_0$.
6. The descent link follows from the good rows of $f$, and the surjective link follows from the good rows and from the fact that $D$ is onto at all levels. The vanishing link follows from the chart condition at zero and from the level identity at the bottom, which is part of the goodness of $a$ and holds at $d$ because $d.\mathcal{B} = a.\mathcal{B}$.

This gives the eight properties for $f$ and $d$. $\square$

**Remark 4.4.5 (Formalization).** The theorem is at [FamAllQOfAllTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrue.lean#L38), and its second name `true_geometry_family_row_data_alt` at [FamAllQOfAllTrueStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrueStatement.lean#L16) only passes its hypotheses on. The conditions are in [FamAllQ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQ.lean#L29) and the links in [NotMemQBase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NotMemQBase.lean#L26); `UnitRatio` is in [UnitRatio.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/UnitRatio.lean#L22), where the condition on primes is that $v_p(r) \neq 0$ implies $p \in S$. The name "row data" does not describe the statement. In the link conditions the hypotheses on $n$ are written `0 + 2 * n + 2 = D.R.m` and `2 * n + 2 * 0 + 2 = D.R.m`, with terms `0` and `2 * 0`. Step 3 is `exists_pairwise_same_choices_at_geo`, the only use of the rapid decay of cusp forms; the links of step 6 are `linkDown_of_famCh`, `linkOnto_of_ontoAll'` (the only use of `OntoAll`) and `linkZero_of_chartZero'`, and the goodness of the commutation datum is `famCh_is_and_tuples_is_of_colOK`, whose main hypothesis is `RowOK`. We did not open these four lemmas, and we did not unfold `GeometricFamily.Is`, `GeometricFamily.True`, `LawsX`, `Pin` beyond its four clauses, or the period and tail maps.
