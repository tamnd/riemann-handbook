---
title: Hermitian column data in standard form
decls:
  - GlobalTheory.Mem.FormSym.formsTiedSym_std
  - GlobalTheory.T.exists_standardFormComparison_symmetricLevel_members
  - GlobalTheory.Mem.Col2.TC.hermitian_data_at_level_prime
  - GlobalTheory.T.exists_hermitian_data_carT_of_std
  - GlobalTheory.Mem.Col2.TC.colsTiedSym_std
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hermitian column data in standard form

The theta series of Sections 1 to 5 are attached to a datum of the development. In the main line of the proof, this datum is not given at the start. It is assembled from a *true column choice*: a Hermitian frame, characters, a choice of places of $E$ above the places of $F$, and a finite set of character tuples. This section proves that the assembled datum carries a Hermitian column datum together with a family of forms, one for each word, that are tied to the columns and are in *standard form*. Standard form means that all the values, uniformizers, restrictions and readings are the ones that the column choice fixes, and that the Hermitian form at each level is the identity matrix in suitable coordinates. The result is an input of [the step on the nonempty hypotheses](/step/nonempty-hyps/). The background is [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and their [local classification](/learn/hermitian-lattices/#local-classification).

### Columns, levels and charts

Fix a base datum $B$. It gives a CM field $E$ with totally real subfield $F$, a rank $m$, a dimension $N_i$ for each level $0 \le i \le m$, and a set of *words* $u$. A datum $X$ over $B$ gives an element $\pi_T(u)$ of $E$ for each word, the *uniformizer at $T$*. A true column choice $I$ over $(B, X)$ is a column datum of the kind above. We say that $I$ is *admissible* if it satisfies the conditions of the development on its tuples, its signs and its places. The pair $(B, X)$ is *pinned* if two compatibilities of frames and uniformizers hold. The *laws* of $I$ are the compatibilities between the column choice and the Weil representations. Given admissible $I$, pinned $(B, X)$, laws $\ell$ and later data $Z$ for the columns, the development assembles a datum $D = D(I, \ell, Z)$ of the kind used in Sections 1 to 5.

At level $i$, the datum $D$ has a Hermitian space $E^{N_i}$ with Gram matrix $J_i$ and a self-dual lattice $\Lambda_i$. For each word $u$ and level $i$, there is a finite set of *classes* of points in the chain of lattices of $u$, and each class has a stabilizer and a lattice. A *chart* at $(u, i)$ is a decomposition of these classes into groups, with a level structure for each group, coordinates for the lattices, and a point $y$ for each class.

A *form tied to the columns* at a word $u$ is a family of objects: a set $\mathrm{Ch}(u, i)$ of chart labels at each level and a map from classes to labels, level charts, a value at each class, a general linear part $\mathrm{gl}$ with its uniformizer $\pi_G$, a frame at each level, and the data of the up, down and diamond moves, with about twenty compatibilities between them. The form is in *standard form* if each of these objects is the one that $I$ fixes, and its level data *project in standard form* if the level data project by the standard quotient maps and the frame at the top level is $1$.

The Hermitian side has its own data. A *Hermitian column datum* $H$ has level zero data, chart labels, levels, classes, values $v_T$ and functionals $F_v$ at each word. It is *characteristic-compatible* with a family of forms $F$ if both have the same characteristic data: the same lattice, local unit group, points and stabilizers at level zero, the same classes and middle data, the same splitting, and the same frame at level zero.

### Forms in standard form

**Lemma 3.7.1 (Diagonal form).** Let $\sigma$ be a ring endomorphism of a commutative ring $E$, $N \ge 1$, and let $h(x) = \sum_{j,k} \sigma(z_j)\,J_{jk}\,x_k$ be the sesquilinear pairing with matrix $J = 1$ against the vector $z = p\,e_N$. Then $h(x) = \sigma(p)\,x_N$.

*Proof.* With $J = 1$ the pairing is $\sum_j \sigma(z_j) x_j$, and only $j = N$ contributes. $\square$

**Theorem 3.7.2 (Forms in standard form).** Let $I$ be admissible, $(B, X)$ pinned, $\ell$ laws and $Z$ later data, and let $D = D(I, \ell, Z)$. Then there are label sets $\mathrm{Ch}(u, i)$, maps from classes to labels, and for each word $u$ a form $F_u$ tied to the columns, such that:

1. each $F_u$ is in standard form, and its level data project in standard form;
2. every $\mathrm{Ch}(u, i)$ is finite, and $\mathrm{Ch}(u, m)$ has exactly one element;
3. all the forms have the same general linear part: $\mathrm{gl}(F_u) = \mathrm{gl}(F_{u'})$;
4. the general linear part of the base word is compatible with the characters at level $m$.

Lean: `GlobalTheory.Mem.FormSym.formsTiedSym_std` (also `GlobalTheory.T.exists_standardFormComparison_symmetricLevel_members`, a second name).

*Proof.* The development gives a general linear part $G$ with the identity at its places and with tied characters, and it gives coordinates at each level in which $J_i = 1$, the self-dual lattice is $O_E^{N_i}$, and the determinant of each point is the determinant of its coordinate matrix. In these coordinates the matrix $C$ that compares the frame with the standard frame is $1$: then $\sigma(C)^{t} C = J_i$ and the determinant identities hold trivially.

At each word $u$ and each level $i \le m$, the development gives charts with a finite label set; the labels are a single point at levels $0$ and $m$. The charts are modified so that the level of each chart kills the values at the uniformizer $\pi_T(u)$, and the points of the modified chart are the standard points $y$. For $i > m$ there is nothing to choose, and the label set is a point. With the charts fixed, the development gives at each level the value tie, the norm tie of the inner product, the diamond moves, the level functions, the up and down moves, and the tie at the boundary. It also gives, for each label, a general linear level with subgroups and characters at the places that divide the fixed numbers, the step before the top level, the class tie at $T$, and the conjugation of periods. The form $F_u$ is the record of these objects. Each field is equal to the field that $I$ fixes, by the construction of the objects, so $F_u$ is in standard form. Parts 2 to 4 come from the choice of labels and from the common $G$. In the frame computations, the pairing with the last basis vector is the lemma on the diagonal form. $\square$

### Hermitian data at the level prime

**Theorem 3.7.3 (Hermitian data at the level prime).** Let $I$, $(B, X)$, $\ell$ and $Z$ be as above. Let $H$ be a Hermitian column datum for $D$, and let $F$ be a family of forms tied to the columns, in standard form with standard level projections, such that $H$ is characteristic-compatible with $F$. Then there is a family $A$ of data at $T$ for $H$ such that $(H, F, A)$ is compatible at $T$, and $A$ satisfies the symmetric adelic compatibility and the symmetric stabilizer compatibility.

Lean: `GlobalTheory.Mem.Col2.TC.hermitian_data_at_level_prime` (also `GlobalTheory.T.exists_hermitian_data_carT_of_std`, a second name).

*Proof.* The development gives, at each word, the following facts on the Hermitian side: the prime of the level is seen by the Hermitian data; the dual lattice modulo the class lattice is the quotient of the level; the projection of the middle step at one level equals the projection of the chart; the stabilizer map of a hyperplane equals the conjugate class map. It also gives, at each place above the level prime, an up move $g^{+}$, a down move $g^{-}$ and a diamond operator, each with its defining equation on the Hermitian side, and a lattice, a projection and classes that agree with those of the forms.

Put these objects into the data $A_u$ at $T$, together with the lattices and level data of $F_u$. The compatibility of $(H, F, A)$ at $T$ has nine parts. Two are equalities by definition. Two are the agreement of classes and lattices. Three say that the projections of $A$ are those of $F$, at level $i$ and at the middle step. The last two say that coordinates and the general linear parts agree under the standard maps. Each follows from the equations above. The symmetric adelic compatibility has six parts: the up, down and diamond moves at level zero and at the levels $1 \le i \le m$. Each is the second half of the defining equation of the move. The symmetric stabilizer compatibility is the stabilizer fact. $\square$

### Column data tied in standard form

**Theorem 3.7.4 (Columns in standard form).** Let $I$ be admissible, $(B, X)$ pinned, $\ell$ laws and $Z$ later data, and let $D = D(I, \ell, Z)$. Then there is a symmetric tied column datum $C$ for $D$ that is in standard form, and whose forms have level data that project in standard form at every word.

Lean: `GlobalTheory.Mem.Col2.TC.colsTiedSym_std`

*Proof.* [The theorem on forms in standard form](/entry/forms-tied-sym-std/) gives labels, the forms $F_u$, and the facts on the general linear parts. From the forms, their levels and their classes, the development builds a Hermitian column datum $H_0$ with levels, classes, values and functionals. At each word, it builds the level zero data and shows that the uniformizer kills the values; the new level zero data agree with $H_0$ in lattice, units, points, stabilizers, splitting and frame. So the datum $H$ with the new level zero data is characteristic-compatible with $F$. [The Hermitian data at the level prime](/entry/hermitian-data-at-level-prime/) give $A$. The development then gives generators, base lattices and functionals for $(H, F, A)$, and the standard spaces in coordinates.

The datum $C$ is the record of $H$, $F$, $A$ and these objects. Its compatibilities are about twenty equalities. All but two are immediate from the construction. The uniformizer $\pi_G$ is the same at every word, since the general linear part of each $F_u$ has the uniformizer of the base. The frames at level zero and at the level prime are the same at every word, since all forms are in standard form and so their frames are the standard frames. $\square$

**Remark 3.7.5 (Formalization).** The three theorems are in the folder `Proofs/IwasawaDecomposition`, but no Iwasawa decomposition occurs in their statements. The theorem on forms is [ExistsStandardFormComparisonSymmetricLevelMember.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsStandardFormComparisonSymmetricLevelMember.lean#L52), with the helpers `hform_last` (line 33) and `sigD_conj` (line 47); its proof calls about twenty lemmas, among them `MemChart.exists_charts`, `TC.charts_funKilled`, `TC.exists_level_projections` and `OneLevel.stepBefore_oneLevel`, and for $i > m$ it fills the charts with the type `Unit`. The theorem at the level prime is [HermitianDataAtLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HermitianDataAtLevelPrime.lean#L18), and the column theorem is [ExistsStandardColumnComparisonsTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsStandardColumnComparisonsTrueColumns.lean#L20). All three set `maxHeartbeats` to 4000000. The datum `ColsTiedSym` is in [BothSym.lean](lean:Formalism/LocalToGlobal/HermitianForms/BothSym.lean#L27); `StdF` and `StdC` are in [LatAtLattice.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/LatAtLattice.lean#L338), `StdLvC` in [StdLvPr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/StdLvPr.lean#L68), the column choice `ColIn` (with the abbreviation `TC`) in [TrueColumnChoicesHeckeCharReferenceEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TrueColumnChoicesHeckeCharReferenceEqOne.lean#L165), and `gramN` and `selfDualLatticeCoords` in [TiedStep.lean](lean:Formalism/LocalToGlobal/HermitianForms/TiedStep.lean#L20). The caller of the column theorem, [FormsMapAtEveryTrueColumnMember.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FormsMapAtEveryTrueColumnMember.lean#L18), discards the standard level projections. The descriptions of the input lemmas above follow their names and statements; we did not open them, and we did not unfold `Ok`, `Later`, `FormsTiedSym`, `CarH`, `CarT` or `HermColsCh`.
