---
title: True family data
decls:
  - GlobalTheory.XGeoStd.exists_xgeo_alt
  - GlobalTheory.T.all_true_family_geometry_alt
  - GlobalTheory.GeoExists.core_data_of_point
  - GlobalTheory.GeoExists.exists_geoAll_alt
  - GlobalTheory.T.all_true_family_datum_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## True family data

This section builds the geometric family $a$ that sections 4 to 10 assume. [The Theorem on family conditions](/entry/fam-all-q-of-all-true-alt/) starts from [the Theorem on true family data](/entry/all-true-family-datum-alt/): for each word $u$ there is a geometric family $a$ that is good and true, whose top orthogonal decomposition has the identity matrix $i_A = 1$, and whose Bessel datum $a.\mathcal B$ is framed. We prove it in three steps. First we build the geometric datum at the point: the chain of spaces, the vacuum vectors, the line vector $\zeta_0$ and the constants $c_0$. This is where strong approximation enters. Then we fill in the rest of the family from that datum: the rational data, the measures, the level data $v$, the type data $o$, the lattices and base points, and the bottom datum. This is where the discrete series inputs enter. The third step puts the two together.

We keep the notation of [the section on the column side](/entry/col-side-alt/). $W$ is a real package over $D$ that satisfies the family conditions on a package. $u$ is a word and $T_u$ its twist number, a prime. $P_g$ is the set of type places of the package and $Q$ the set of extra places. $X_0, \dots, X_m$ are the spaces of the chain, $X'$ is the top space and $\Lambda_X$ its lattice. For a geometric datum, $x_j$ is the space at level $j$ with lattice $L_j$, $\mathrm{vac}_j$ the vacuum vectors, $L_z$ a line with a vector $\zeta_0$, $b_T$ an element and $L_T$ a lattice of $X'$, and $o_T$ the top orthogonal decomposition at level $m$ with matrix $i_A$.

**Definition 4.13.1 (Geometric datum at a point).** A *geometric datum at the point* for $W$ and $u$ is a geometric datum $a$ with constants $c_0 \colon \mathbb N \to \mathbb C$ such that:

1. each $x_j$ is good for $j \leq m$;
2. the pin condition holds: the vacuum vectors moved by the base points of the chain are the multiples $c_0(j)$ of the vacuum vectors, for the standard character $\psi$ and the infinity type $\theta$ of $W$;
3. $b_T = 1$, $i_A = 1$ and $L_T = \Lambda_X$;
4. $\zeta_0$ spans $L_z$, and $\langle \zeta_0, \zeta_0 \rangle = T_u$;
5. the top embedding of $o_T$ is the embedding of the point $z_0(u)$, and the Bessel vector of $o_T$ at $\zeta_0$ is $z_0(u)$;
6. at each place there is a self-dual lattice $L_Z$ of $L_z$ for which the orthogonality condition of $o_T$ holds with $L_m$ and $L_T$;
7. at each place of $P_g$ or $Q$ there are local data with standard frames.

**Theorem 4.13.2 (Geometric data at a point).** Assume strong approximation for the special unitary group. Let $W$ satisfy the family conditions on a package. Then for each word $u$ there is a geometric datum at the point for $W$ and $u$.

Lean: `GlobalTheory.XGeoStd.exists_xgeo_alt` (also `GlobalTheory.T.all_true_family_geometry_alt`, a second name).

*Proof.* We take the standard datum of the package and check the seven conditions.

1. The twist data of $W$ are good and pinned. The character $\psi$ of $W$ is standard with sign $-1$, and $\theta$ is an infinity type. A result of another chapter gives vacuum vectors $\mathrm{vac}_j$ for $\psi$ and $\theta$ at each level.
2. For each level $i$ with $i + 1 \leq m$, a result of another chapter gives a constant $c_i$ such that the vacuum vector moved by the base point is $c_i$ times the vacuum vector, for all tuples at once. This result is the one place where [strong approximation](/learn/groups/#strong-approximation) is used; we have not opened its proof. Put $c_0(j) = c_j$ for $j + 1 \leq m$ and $c_0(j) = 1$ otherwise.
3. Let $a$ be the standard datum built from the vacuum vectors, the word $u$ and the lattice $\Lambda_X$. Its spaces are the standard spaces, so they are good, and their lattices are the lattices of the package. With step 2 this gives the pin condition.
4. By construction $b_T = 1$ and $L_T = \Lambda_X$. The top decomposition has the identity matrix, so $i_A = 1$.
5. The line vector $\zeta_0$ is the standard vector of $u$. It spans $L_z$ and has norm $T_u$. The top embedding is the embedding of the decomposition of the top space, and its Bessel vector at $\zeta_0$ has one nonzero coordinate, the last one, equal to $z_0(u)$.
6. At each place, the frame lattice $L_Z$ of the line is self-dual. The lattice $\Lambda_X$ is the frame lattice of $X'$, since the frame of the package is self-dual. The top decomposition is orthogonal at every place for these lattices.
7. At a place of $P_g$ or $Q$, a result of another chapter finds an index of the reading of the package at that place, and the vacuum data of a true family give the local data with standard frames. $\square$

**Theorem 4.13.3 (Core data of a point).** Assume that the discrete series cover the tempered spectrum and that Harish-Chandra modules globalize. Let $W$ satisfy the package hypotheses. Let $u$ be a word, $P_g$ a set of type places, $T_u \neq 0$ not in any place of $P_g$, and no place of $Q$ in $P_g$. Let $j$ be a leading reading of $W$ at $u$ and $1$. Let $(a, c_0)$ satisfy conditions 1, 3, 4, 6 and 7 of a geometric datum at the point, with condition 6 only at the places prime to $T_u$. Let $R$ be a property of type data, and assume: for all rational data $y$, measures, base points and level data $v$ with $v.N_T = L_T$, with twist places the places that divide $T_u$, with $v.\tau = y.\tau$ and with the twist condition of $y$, there are type data $o$ with the pre-type condition for $v$ and $o$, $o.\zeta_0 = \zeta_0$ and $R(o)$. Then there is a geometric family $A$ for $W$ and $u$ that is good, with constants $c_0$, with geometric datum $a$, with framed Bessel datum, and with $R$ for its type data.

Lean: `GlobalTheory.GeoExists.core_data_of_point`.

*Proof.* We build the parts of the family in order.

1. A result of another chapter on line vectors gives rational data $y$ and a Bessel datum $\mathcal B$ on $X_0$. It is adapted and framed, it has norm $-T_u$, and its level is the Bessel datum of $y$ at $(0, r_S)$.
2. A result of another chapter gives measures $m$ for $y$ and the geometric datum, with the volume condition at the last level. The two published inputs give the conditions on the common datum, through a result on the coordinates of the geometric measures.
3. Let $P_T$ be the set of places that divide $T_u$, and $P_G$ the set of places under $P_g$. They are disjoint, since $T_u$ is in no place of $P_g$.
4. Let $v_0$ be level data with level places $P_G$, twist places $P_T$, base points $1$ and zero test data. The hypothesis on $R$ gives type data $o$ with the pre-type condition and $R(o)$.
5. At the type places, a result of another chapter gives symmetric data and readings. Their bases give a basis family that is $1$ off $P_g$.
6. [The Theorem on lattices, frames and base points](/entry/lattices-frames-base-points-exist-alt/) gives lattices $N_j$, base points $b_j$, a twist $d_T$, the lattices and frames of $o$, the shape condition and the local normal frames at each place.
7. The measure condition does not depend on the base points, so $m$ still works with the base points $b_j$.
8. Results of another chapter give the test functions and their ties, the level groups and the local groups $G_1, \dots, G_n$, and the data at the places of $Q$.
9. The bottom datum is $(\mathcal B, b_0, 1, 1, 1)$. The family $A$ collects all of this. It is good by steps 1 to 8, and its Bessel datum is framed by step 1. $\square$

**Theorem 4.13.4 (True family data).** Assume that the discrete series cover the tempered spectrum, that Harish-Chandra modules globalize, and strong approximation for the special unitary group. Let $W$ satisfy the family conditions on a package. Then for each word $u$ there is a geometric family $a$ for $W$ and $u$ that is good and true, with $i_A = 1$, and whose Bessel datum is framed.

Lean: `GlobalTheory.GeoExists.exists_geoAll_alt` (also `GlobalTheory.T.all_true_family_datum_alt`, a second name).

*Proof.* We feed the first theorem into the second.

1. The Theorem on geometric data at a point gives $(a, c_0)$ with the seven conditions.
2. The family conditions on a package contain a leading reading $j$ of $W$ at $u$ and $1$.
3. The base fields have prime twist numbers, so $T_u$ is prime and $T_u \neq 0$. By the level condition of the package, $T_u$ is in no place of $P_g$, and no place of $Q$ is in $P_g$.
4. Apply the Theorem on core data of a point, with $R$ the standard condition on type data. Its hypothesis on $R$ is a result of another chapter on the columns of a true family, which uses the pin condition, the line vector, the Bessel vector and the orthogonality of step 1.
5. This gives a good family $A$ with constants $c_0$, geometric datum $a$ and framed Bessel datum. $A$ is true: its four conditions are the pin condition of step 1, the standard condition of step 4, and the two parts of condition 5 of step 1. Step 1 also gives $i_A = 1$. $\square$

So the published inputs split cleanly. Strong approximation is used only for the constants $c_0$ of the pin condition. The discrete series inputs are used only for the conditions on the common datum.

**Remark 4.13.5 (Formalization).** The theorems are at [ExistsXgeo.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsXgeo.lean#L19) and [CoreDataOfPoint.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreDataOfPoint.lean#L52) (core data at line 52, true family data at line 133). The second names are relays at [ExistsXgeoStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsXgeoStatement.lean#L17) and [CoreDataOfPointStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreDataOfPointStatement.lean#L19). Strong approximation enters at line 27 of ExistsXgeo.lean through `exists_const_movedVacuum_all_tuples`, and nowhere else in the section. Some details:

- `core_data_of_point` takes the constants $c_0$ as given and stores them. Nothing in its proof constrains them; the pin condition is checked only later, in `exists_geoAll_alt`.
- The matrix condition $i_A = 1$ is not passed to `core_data_of_point`. It is added at the end of `exists_geoAll_alt` (line 145).
- The type data $o$ are built for base points $1$ (step 4) and reused for the base points $b_j$.
- The disjointness of $P_G$ and $P_T$ is proved here and again in LatticesFramesBasePointsExist.lean at line 43.
- Lines 36 to 38 of CoreDataOfPoint.lean open and close an empty `section Transport`.
- The name `all_true_family_geometry_alt` speaks of a true family, but the conclusion is about a geometric datum at a point; the family is built only in `core_data_of_point`.
- We have not unfolded the published inputs, the pre-type condition or the standard condition on type data, nor opened `line_vector_bessel_existence_alt` and the results of step 8.
