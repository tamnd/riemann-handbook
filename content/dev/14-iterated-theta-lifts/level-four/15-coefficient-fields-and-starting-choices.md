---
title: Coefficient fields and starting choices
decls:
  - GlobalTheory.Mem.R3.OkVals.large_coefficientField_contains_twist_values
  - GlobalTheory.T.exists_rowLiftReading_definiteFormCoordinates
  - GlobalTheory.Mem.R3.Rw.PkExist.rowPk_nonempty
  - GlobalTheory.T.nonempty_rowLiftFamily_over_columnChoices
  - GlobalTheory.Mem.R3.Rw.exists_pre2_of_fine_of_resChar_mem
  - GlobalTheory.T.constructionStartingChoices_of_fine_adelicData
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coefficient fields and starting choices

The construction starts from a fine adelic datum and a stage, and it needs two more inputs before the first rows exist. The first is a coefficient field large enough to hold the values of the twisting characters and the Hecke eigenvalues. The second is a row package: a family of lifts of the rows with readings in the coordinates of the definite forms. In this section we prove both, and then we build a starting choice from a fine adelic datum. The three results enter [the large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/).

### Large coefficient fields

Let $B$ be a base with coefficient field $L_B$, frame $f$ and twist data $T$. Column input data $I$ over $B$ have characters $\xi_a$ for the indices $a$, and sets $Q_a$ of primes. We say that the values of $I$ lie in $L_B$ if for each $a$ and each prime $P$ where $\xi_a$ is unramified, $\xi_a(P)$ lies in the image of $L_B$, and for each $a$ and each $P \in Q_a$, the field $L_B$ contains a primitive root of unity of order $N(P)$.

**Theorem 1.15.1 (Large coefficient fields).** Eventually in the context and at all large bases, the following holds. Let $I$ be good column input data over $B$ with frame $f$, whose characters form the set of twists of $T$. Then the values of $I$ lie in $L_B$. For each set $U$ of indices, each finite set of absolutely irreducible characters and each trace datum, the column family of level three of $I$ is good at $1$.

Lean: `GlobalTheory.Mem.R3.OkVals.large_coefficientField_contains_twist_values`.

*Proof.* There is a finite set $S_v$ of algebraic numbers such that the values of $I$ lie in $L_B$ whenever $S_v \subset L_B$. There is a finite set $S_o$ of algebraic numbers such that $S_o \subset L_B$ puts the Hecke eigenvalues of the row and lift points in $L_B$. Both sets come from results of the chapter on coefficient fields, which we use as given. A base is large if $S_v \cup S_o \subset L_B$. The first claim is then the property of $S_v$. For the second, the column family of level three is good under four conditions: the infinite place of the embedding of $L_B$ into $\mathbb{C}$ is conjugation stable, by the star structure of $L_B$; the characters are absolutely irreducible; the Hecke operators of the rows and of the lifts commute; and the eigenvalues lie in $L_B$, by $S_o$. $\square$

### Row packages

Let $D$ be an ambient datum, $R$ a real datum with a face, an isomorphism $c_G$ and a ring $O$ inside the image of $K_s$. The rows are indexed by the tuples, and a tuple $t$ gives a row of matrices $r(t)$ for the definite forms and matrices $l(t, i)$ for the lifts at the levels $i$. A row datum $y$ at a stage consists of a tuple map and the data of the rows. A coordinate map $m_A$ for the definite forms and a coordinate map $m_L$ for the lifts are maps on tuples that satisfy the laws of coordinates.

**Definition 1.15.2 (Row reading).** A reading datum $p$ for $y$ fixes the coordinate map $m_L$ of the lifts. A reading of $y$ with coordinates $m_A$ and $p$ consists of a representation of the group of the stage on the multiplicity space with its representatives, the matrices of the definite forms and of the lifts with their laws, the Hecke operators on both sides, the characters, the level forms, the dimension of the multiplicity space and a reading map.

**Theorem 1.15.3 (Row readings in definite coordinates).** Assume the inputs from the literature, the pins of the real datum and the condition on the holds. Let $y$ be a row datum, and let $m_A$ and $m_L$ satisfy their laws, with $m_A(y(t)) = r(t)$ and $m_L(y(t))(i+1) = l(t, i)$. Then there is a reading datum $p$ with lift coordinates $m_L$ and a reading of $y$ with coordinates $m_A$ and $p$.

Lean: `GlobalTheory.T.exists_rowLiftReading_definiteFormCoordinates` (also `GlobalTheory.Mem.R3.Rw.PkRead.exists_pkT`, the proof).

*Proof.* There is a chain of levels over the top spaces. Over the definite forms there are lifts of the spaces, and a basis of the rows comes from the quotient of the reference tuple. The multiplicity space is finite dimensional, by the finiteness theorem of Harish-Chandra among the inputs. These give the representation, the matrices and the Hecke operators of the reading, with the coordinates $m_A$ and $m_L$. $\square$

**Definition 1.15.4 (Row package).** A row package for a column datum $w$ at a stage $z_0$ consists of a row datum $y$, a tuple map, a reading datum $p$, a reading $t$ of $y$, the lift coordinates, the period map, the base spaces $W_0$ with their forms, the scalars $\mu$, the sharp tie, the indices $n$, the constants $\kappa$ and the numbers of the rows.

**Theorem 1.15.5 (Existence of row packages).** Assume the inputs from the literature. Let $w$ be a column datum and $z_0$ a stage of $w$. Assume that the field $F$ of the host is the maximal real subfield of $E$, that the lattice of $Y_0$ and the lattices of all $W_i$ are standard, that the condition on the holds is true, and that the set $W_t$ of places is stable under conjugation. Then there is a row package for $w$ at $z_0$.

Lean: `GlobalTheory.Mem.R3.Rw.PkExist.rowPk_nonempty` (also `GlobalTheory.T.nonempty_rowLiftFamily_over_columnChoices`, a second name).

*Proof.* Choose a tuple map, with the tuple of $\mu_0$ as the fallback. A row datum $y$ exists. The definite forms of all tuples satisfy the laws of coordinates, and the index of the family of tuples gives $m_A(y(t)) = r(t)$. The theorem on row readings then gives $p$ and $t$. The period map of the forms is equivalent to the forms of the row lifts at the upper level, which gives the period map and the base spaces. The rows datum with the prescribed tuples and the defined weights uses that $W_t$ is stable under conjugation, and gives $\mu$, the sharp tie, $n$ and $\kappa$. Numbers with the right properties exist for the rows. $\square$

### Starting choices

A starting choice for a context $K$ and a column datum $w$ has a first stage $Z_0$, a top space, the set $W_t$ of places, an adelic datum $z$, the row package and a support condition. A fine adelic datum and the set $W_1$ are defined in [Section 1.13.6](/entry/dat-ext-rest/).

**Theorem 1.15.6 (Starting choices from fine adelic data).** Assume the Weil representation of a unitary dual pair, the existence of the discrete series of $U(p,q)$, the finiteness theorem of Harish-Chandra, rapid decay of cusp forms, and the weight case condition. Then there is a column step from "a start" to the following. For every stage $Z$ with a top space and every adelic datum $z$ over $Z$ with places $\{v : \text{the residue characteristic of } v \text{ is in the prime set of } T\}$, such that the stage is good, the groups are true and fit, $\kappa$ is defined, $z$ is fine, $W_1(z)$ lies in the places of $z$, and the character $\psi_T$ of $T$ is $1$ at each place off $W_1(z)$, there is a starting choice $P$ with first stage $Z$ and $W_t = W_1(z)$ whose adelic datum extends $z$.

Lean: `GlobalTheory.Mem.R3.Rw.exists_pre2_of_fine_of_resChar_mem` (also `GlobalTheory.T.constructionStartingChoices_of_fine_adelicData`, a second name).

*Proof.* Step 1. The five hypotheses give the inputs from the literature. The frames of the host hold eventually in the context, so the step may keep them. Step 2. The set $W_1(z)$ is stable under conjugation, by its definition. Restrict $z$ to the places in $W_1(z)$. The restriction is exact at its places, has geometry and is standard, its set $W_1$ is again $W_1(z)$, and it extends $z$. Step 3. The weight case condition gives the condition on the holds. The frames of the host give that $F$ is the maximal real subfield of $E$ and that the lattices of $Y_0$ and of the $W_i$ are standard. The theorem on row packages, with $W_t = W_1(z)$, gives a row package. Step 4. These data form the starting choice. The condition that $\psi_T$ is $1$ off $W_1(z)$ is its support condition. $\square$

**Remark 1.15.7 (Formalization).** In [LargeCoefficientFieldContainsTwistValues.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LargeCoefficientFieldContainsTwistValues.lean#L23) the lemma `ev_of_forall` makes "eventually in the context" trivial, and of the largeness conditions only $S_v \cup S_o \subset L_B$ is used; the other sets are empty. The goodness conditions `Ok3` of the column family are not unfolded here. The restriction of the adelic datum is `res` in [ConstructionStartingChoicesOfFineAdelicData.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ConstructionStartingChoicesOfFineAdelicData.lean#L47), with its properties at lines 69 to 105, and the main theorem is at line 195. The second names in the files `NonemptyRowLiftFamilyOverColumnChoicesStatement.lean`, `ExistsRowLiftReadingDefiniteFormCoordinatesStatement.lean` and `ConstructionStartingChoicesOfFineAdelicDataStatement.lean` repeat the long statements word for word. The row package is `RowPk` ([ReadPk.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ReadPk.lean#L75)).
