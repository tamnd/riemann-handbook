---
title: Rows data, series ties and levels
decls:
  - GlobalTheory.Mem.R3.Rw.St.exists_rowsT
  - GlobalTheory.HeightCounting.SerCopy.exists_preTie
  - GlobalTheory.T.exists_newThetaData_series_classSums_lattices
  - GlobalTheory.HeightCounting.SerCarry.exportTie_move
  - GlobalTheory.HeightCounting.SerCarry.serAt_move
  - GlobalTheory.HeightCounting.SerCarry.series_move
  - GlobalTheory.LevCmp.levEq
  - GlobalTheory.Mem.Col2.TC.RcHyp.chTh_ok_chi
  - GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rows data, series ties and levels

This section collects five results that the starting stages of the construction use. First, a starting choice and a stage over it give a rows datum, the object that the theta data of [Section 1.10.3](/entry/rec-fun-of-rows/) start from. Second, a real side with its pins gives an export tie: a theta datum for the series of new exponents with its class sums and its lattices. Third, an export tie and a series tie move along a copy of the ambient datum. Fourth, two forms with the same Hecke eigenvalues on a parahoric level have the same level and character. Fifth, the character conditions of the columns hold for the twisted normal forms. The results feed the starting stages of Volume 15: [the start at all choices](/entry/start-at-all-pre2/), [the side condition](/entry/pre-at-of-side-b-tau-true-lam-ok/), [the restaged series](/entry/series-restage-of-carry-alt/), [the stage existence from Harish-Chandra theory](/entry/stage-cexists-of-harish-chandra-ser-n/) and [the square integrable columns](/entry/square-integrable-columns-of-witnesses/).

### Rows data from a starting choice

A starting choice $P$ for a column datum $w$ has a first stage $Z_0$, a set $W_t$ of places, an adelic datum and the characters $\eta_j$ of its quotient datum. A stage $x$ over $P$ has a later stage $Z$ of $w$, characters $\eta_j$, a base row side $p_0$, a fine adelic datum $z$ with its rows $Y$, and the twists $j_W$ of its stage. A rows datum at $Z$ with places $W_t$ and base row side $p_0$ consists of an adelic datum $z$, the rows $Y$, a stage, the facts that $z$ is exact and has geometry, and the fits of the groups.

**Theorem 1.12.1 (Rows data).** There is a column step from "pinned and with a row package" to the following property of $w$. For every starting choice $P$ and every stage $x$ over $P$ whose characters $\eta_j$ agree with those of $P$ for $1 \leq j \leq m$, there is a rows datum $t$ at the stage $Z$ of $x$, with the places $W_t$ of $P$ and the base row side of $x$, which has a reading of its rows, whose top space is the top space of $P$, and whose adelic datum, rows and twists are those of $x$.

Lean: `GlobalTheory.Mem.R3.Rw.St.exists_rowsT`.

*Proof.* The places $W_t$ of $P$ are the set $W_1$ of the adelic datum of $x$. Indeed $W_t$ is the set $W_1$ of $P$ for the field $F_0$ of the first stage, $P$ is exact, and the field $F_0$ is the same at $Z_0$ and at $Z$, by the condition on $\kappa$ of the starting choice. Now take for $t$ the top space of $P$, the rows of $x$ for the characters $\eta$, and the exactness, the geometry and the fits of $x$. The reading of the rows of $t$ comes from the row package. $\square$

### Export ties

An export tie for a real side $X$ is the theta datum of the series of new exponents. It consists of a setup of rank $\rho$, a good place, a pin, an extremal vector, scalars $\nu$ with the property that they act as scalars, a tie of the theta datum to the series, a Hecke tie, and the universality of a character.

**Theorem 1.12.2 (Export ties).** Assume global Artin reciprocity (Artin; see [global class field theory](/learn/class-field-theory/#global-class-field-theory)). Let $D$ be an ambient datum and $R$ a real datum over a family of multiplicity spaces, with a face, a group isomorphism $c_G$, a map $k$ from the field $K_s$ to $L_0$ compatible with the algebra map, a row side and a map $P_q$ from the finite places of $F$ to primes. Assume that the real datum has pins and that its geometry holds; that extremal vectors exist; that the form of $K_s$ and the Hecke operators are admissible; that the set $S_b$ lies in the set $S_0$; that the $\tau$ condition, the character side, the value condition at $L_0$ and the lambda data hold; that the places over the primes $d_E$ and $d'_E$ split; that $P_q$ lies over the right places, is a choice, and has the primes of the real datum in its range; and that the standard condition holds. Then there is an export tie.

Lean: `GlobalTheory.HeightCounting.SerCopy.exists_preTie` (also `GlobalTheory.T.exists_newThetaData_series_classSums_lattices`, a second name).

*Proof.* The characterisation of weak real data gives the characters of $R$. The places over $d_E$ and over $d'_E$ split into primes. The number of primes over a split prime $p$ is $[E : \mathbb{Q}]$, since $p$ splits completely. This gives the setup and its characters, with the Weil representation of the unitary dual pair, which is proved in an earlier chapter. Next we find scalars $\nu$ that act as scalars, a faithful real reading, an identity frame and a reading of the series. The theorem on ties with series gives the tie of the theta datum, and the second step of the Hecke operators with normalised sums gives the Hecke tie. $\square$

### Moving ties along a copy

A copy of an ambient datum $D$ is a second datum $D'$ with a map $\iota$ and an identification $e$ of all parts. A copy of the twists copies only the twisted parts, a full copy copies all parts. A real move from $X$ to $X'$ along $\iota$ carries the real side of $D$ to that of $D'$.

**Theorem 1.12.3 (Moving an export tie).** Let $D'$ be a copy of the twists of $D$ and let $X \to X'$ be a real move. Let $Y_S$ be a real series datum for $X$, whose supports agree with those of the rational datum $S$. Then each export tie of $Y_S$ at the place $v_0$ of $X$ moves to an export tie of the moved series at the place $v_0$ of $X'$, with the same setup, the same scalars $\nu$ and the same reading at each twist $i$ and its copy $i'$.

Lean: `GlobalTheory.HeightCounting.SerCarry.exportTie_move`.

*Proof.* Each part of the export tie moves along the copy: the setup, the real reading, the tie, the scalars and the Hecke tie. The universal character is the same on a copy. $\square$

**Theorem 1.12.4 (Moving a series tie).** Let $D'$ be a full copy of $D$ and $X \to X'$ a real move. Assume that the tied exponent data move, that the row characters are kept on both sides, that the character frames are the same, and that the maps $P_q$ correspond. Then a series tie of $Y_S$ at $v_0$ for these data moves to a series tie of the moved series at the place $v_0$ of $X'$.

Lean: `GlobalTheory.HeightCounting.SerCarry.serAt_move`.

*Proof.* A full copy is a copy of the twists, so the export tie moves by the previous theorem. The other parts of the series tie are vectors and characters, and they move with the copy. $\square$

**Theorem 1.12.5 (Moving a series).** Let $D'$ be a full copy of $D$ and $X \to X'$ a real move, with geometric halves on both sides. Let $Y_S$ be a real series datum whose maps $f_i$ are the identity, with a lower datum, admissible Hecke data $H$ and $H'$ over sets $S_b$ and $S'_b$ over the lower places, a Hecke law and a character side on each side with the same units and the same frame. Then there are a real series datum $Y'_S$ for $X'$ and tied exponent data with the law of $P_q$ and the Hecke law, with identity maps $f_i$, with a series tie at $v_0$ and with the $\tau$ condition.

Lean: `GlobalTheory.HeightCounting.SerCarry.series_move`.

*Proof.* The tied exponent data move along a copy. The law of $P_q$ and the Hecke law move with the copy. The series tie moves by the previous theorem, applied with the vectors of the series. $\square$

### Equal Hecke eigenvalues give equal levels

A level datum for a tuple $\mu$ is a level $J$, a product of local compact open subgroups, with a character $\chi$ of $J$. Two level data are equal if the levels are equal and the characters agree on $J$.

**Theorem 1.12.6 (Levels from Hecke eigenvalues).** Let $\eta$ be a Hecke character and $m$ a real level datum for $\mu$, with level $J$ and character $\chi$. Assume:

1. the places of $D$ are good, and at each ramified split place $s$ and each component $\xi$ of $\eta$ there is a unit $a$ with $|a|_s = 1$ and $\xi(a) \neq 1$;
2. $J$ is a product level, $(J, \chi)$ has parahoric shape, at the type places $J$ and $\chi$ have a unipotent level for a character $\psi_0$ and a component $\xi$, and the hypothesis outside the good and ramified places holds;
3. the bad places lie among the good and ramified places, and the cell of $X$ at $j$, with the character carried by an embedding $e$, has parahoric shape and the other conditions of 2;
4. the two level data have a common form with the same Hecke eigenvalues.

Then the level datum of $m$ equals the level datum of the cell.

Lean: `GlobalTheory.LevCmp.levEq`.

*Proof.* Both level data have the shape of a group, by the parahoric shape. A class with trivial stabiliser gives nonzero forms $f$ and $f'$ of the two levels. The rank bounds give $2 \leq r < n_V$. By the theorem on product levels it is enough to compare the local components. At a type place, the Hecke character of a split component is unique, and an additive character with a common eigenvector of the unipotent level is determined. At a ramified place, an automorphism that maps one parahoric to the other fixes the split place, and the parahoric with its character is rigid. At the other places both levels are maximal and both characters are $1$. $\square$

### Character conditions of the columns

**Theorem 1.12.7 (Theta characters at a later stage).** Let $I$ be a column datum with laws, $Z$ a later stage with jets, and $\chi$ a character on the ideals of $E$ that agrees with the character of $I$ on the ideals of norm one. Then the theta character datum of the ambient datum of $I$ at $u$ and $m-2$, with the character $\chi$, is good.

Lean: `GlobalTheory.Mem.Col2.TC.RcHyp.chTh_ok_chi`.

*Proof.* The restriction of $\chi$ to the ideals of norm one is a character. The hypothesis on the bad primes holds with local factor $1$, and the smooth part holds. The jets are rational for $\chi$. At each step $i < m$ the theta equivalence of the ambient datum is tied. These facts give the laws of the theta character datum and then that it is good. $\square$

**Theorem 1.12.8 (Column conditions from twisted normal forms).** Let $I$ be a good column datum with pins and laws, $Z$ a later stage with twisted normal forms and jets, and $\chi$ as in the previous theorem. Then for each $a$ and $u$: the column characters are good for all $j$, the evaluation datum of the base tuple is good, the index matrix of $I$ at $a$ is in normal form, and the kernel of the column is equivalent to the rational kernel for every $b$.

Lean: `GlobalTheory.Mem.Col2.TC.RcHyp.hyps_of_isTw`.

*Proof.* The evaluation datum of the base tuple is good because its value is $1$, with the trivial true column tuple. The index matrix is in normal form because the twisted normal forms give it. The kernel equivalence is the rational kernel theorem applied to the good theta character datum of the previous theorem. The column characters are good by the laws of $I$. $\square$

**Remark 1.12.9 (Formalization).** The theorem `hyps_of_isTw` takes the pins of the column as `_` and does not use them ([EvaluationDatumOkBaseTuple.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/EvaluationDatumOkBaseTuple.lean#L172)). The export tie theorem uses the proved Weil representation constant `weilRepresentationUnitaryPair` of `ImportsBis.lean`, not a hypothesis ([ExistsNewThetaDataSeriesClassSumsLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsNewThetaDataSeriesClassSumsLattices.lean#L52)). The file of `levEq` is named after the Casselman-Wallach theorem, but `levEq` does not take it as a hypothesis ([StatementCOfCasselmanWallach.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/StatementCOfCasselmanWallach.lean#L90)); the rigidity step is `para_rigid` at line 74. The second name `exists_newThetaData_series_classSums_lattices` speaks of class sums and lattices, but its conclusion is only the existence of an export tie. The three move theorems are in [ExportTieMove.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExportTieMove.lean#L31) (lines 31, 71 and 98), and they move each part by a lemma on copies that is not unfolded here.
