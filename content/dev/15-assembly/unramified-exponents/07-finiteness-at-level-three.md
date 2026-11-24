---
title: Finiteness at level three
decls:
  - GlobalTheory.T.sFin_and_sFinl_of_archCmp_sEta_thetaData
  - GlobalTheory.HeightCounting.Fin3.sFin_and_sFinl_of_theta_data_exists
  - GlobalTheory.HeightCounting.Fin3.lv3_of_third_alt_alt
  - GlobalTheory.HeightCounting.Fin3.builtEx_of_published_inputs'
  - GlobalTheory.T.side_rational_hecke_data_alt
  - GlobalTheory.HeightCounting.locAll_exists_alt
  - GlobalTheory.T.side_rational_eigen_data_alt
  - GlobalTheory.HeckeLocN.ndSpec_exists_alt
  - GlobalTheory.HeightCounting.Fin3.start_at_all_pre2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness at level three

This section proves item 6 of [the stage statements](/entry/all-stages-of-specializations-alt/) of Section 6: at every stage with a strict henselian acyclic level datum, there is a level three object at the parameter set of the extension with law, with the same weights and a kept norm choice. This is the finiteness statement, and it has a form with the list condition. At one stage the proof has three inputs: rows at the stage, the eta statement of Section 8, and theta data. To apply the eta statement one must first know that the automorphic side exists: for each finite set of numbers, there are localization data of the Hecke modules with an automorphic specialization and semisimple residual representations. Most of the section builds these localization data.

Let $P$ be a datum over a context $K$ and a column datum $w$, and let $x$ be a stage of $P$. A strict henselian acyclic level datum $l$ over $x$ carries coefficient data $A$, a family $M$, a norm choice $\chi$ and a tuple.

**Definition 6.7.1 (Rows at a datum).** The datum $P$ has *rows* if for every stage $x$ of $P$ whose eta values agree with those of $P$ there are row data $t$ with a nonempty row set that match the level, the base point, the reading and the column weight of $x$.

**Definition 6.7.2 (Localization data and the automorphic side).** Let $D$ be a datum with coefficient data $A$, a family $M$, a norm choice $C$ and a tuple. Let $\mathrm{big}$ assign a finite set of complex numbers to each place. A *Hecke specification* for $\mathrm{big}$ over a localization datum $X$ and twist data $T$ consists of:

1. for each index $i$ of $X$, a prime $\ell_i$, a ring $O_i$ and an embedding $\iota_i$ of its fraction field into $\overline{\mathbb{Q}}_{\ell_i}$ whose image reaches each number of $\mathrm{big}$;
2. for each base, a Hecke algebra $\mathbb{T}_{j,w}$ over a ring $O_{j,w}$, such that the indices at $(j, w)$ are in bijection with the maximal ideals $\mathfrak{m}$ of $\mathbb{T}_{j,w}$ and $O_i \cong O_{j,w}$;
3. an injective map from the lattice of $i$ onto the $\mathfrak{m}$-part of the module of the base;
4. the points of $i$: the algebra maps $\mathbb{T}_{j,w} \to O_{j,w}$ with kernel class $\mathfrak{m}$ and a nonzero eigenspace.

*Localization data* $L$ for $D$ add to a Hecke specification an automorphic specialization, which ties $L$ to $A$, $M$ and the tuple, and type data. The *automorphic side exists* for $(A, M, C)$ if for each $\mathrm{big}$ there are localization data $L$ with a Hecke specification for $\mathrm{big}$, an automorphic specialization, and residual representations $\bar\rho_{\sigma,\lambda}$ that are all semisimple.

**Definition 6.7.3 (Unique blocks).** A datum $D$ has *unique blocks* if two lists of conjugate self-dual blocks with the same total rank and the same local classes at all split places have the same multiset of pairs $(a, d)$ of block sizes and multiplicities.

The standard facts on Hecke operators say: for a CM field $L$, a weight, a level $J \subset \mathrm{GL}_n(\mathbb{A}_{L,f})$ and a character $\chi$ of $J$ trivial on a congruence subgroup, the Hecke operators $T_{s,\varpi,k}$ at good split places $s$ preserve the type space, are linear and commute, and for each eigenvalue $\mu$ and each prime $\ell$ below no such $s$, some $d\mu$ with $d$ prime to $\ell$ is integral.

**Theorem 6.7.4 (Hecke specifications).** Assume global Artin reciprocity and the standard facts on Hecke operators. Let $D$ be a datum with a character frame, an embedding of its CM field $E$ into $\overline{\mathbb{Q}}$, coefficient data $A$, rational data with two characters $\theta_k$ of $(\mathbb{Z}/g_k)^\times$, a side datum, a family $M$, a norm choice $C$ and a tuple tied to $C$. Assume:

1. a choice side and a matrix input;
2. the ring $L_0$ is stable under conjugation;
3. the exponents of $D$ are integers;
4. the places of $E$ over two given primes split;
5. density of split Frobenius elements;
6. at each twisted place $w$ the twist character $\psi_w$ has values in $L$;
7. the map from the integers to $L$ is injective, with image the integral elements of a subfield.

Then for each $\mathrm{big}$ there are a localization datum $X$, twist data $T$ over $X$, and a Hecke specification for $\mathrm{big}$ over $X$ and $T$.

Lean: `GlobalTheory.HeckeLocN.ndSpec_exists_alt` (also `GlobalTheory.T.side_rational_eigen_data_alt`, a second name).

*Proof.* There are six steps.

1. The conductor sets of $C$ lie over the real places and are stable under conjugation. With the matrix input, the places of the Hecke generators lie outside the level.
2. By the standard facts, the double coset operators lift to linear operators over the coefficients, and the lifts commute.
3. At each $w$ take four finite extensions of $\mathbb{Q}_\ell$: one holds all Hecke eigenvalues, one holds the coefficient field and the numbers of $\mathrm{big}$, one gives the local bridges, and one gives the ring maps for the twists. Their compositum is the coefficient datum.
4. On the localized base the Hecke ring is local, acts faithfully on the localized lattice, and has a nonzero eigenspace at each point.
5. By Artin reciprocity and the density of split Frobenius elements, each twist character $\psi_w$, as a Galois character, is ramified at each place of its conductor set and trivial on the decomposition groups above $\ell$.
6. These parts assemble into the Hecke specification. $\square$

**Theorem 6.7.5 (Localization data).** Assume global Artin reciprocity. Let $D$ be a datum with the data of the theorem on Hecke specifications, and assume its hypotheses 1 to 7 and that $D$ has unique blocks. Then for each $\mathrm{big}$ there are localization data $L$ and a Hecke specification for $\mathrm{big}$ for $L$, with an automorphic specialization and with every residual representation of $L$ semisimple.

Lean: `GlobalTheory.HeightCounting.locAll_exists_alt` (also `GlobalTheory.T.side_rational_hecke_data_alt`, a second name).

*Proof.* The standard facts on Hecke operators are proved, so [the theorem on Hecke specifications](/entry/nd-spec-exists-alt/) gives $X$, $T$ and the Hecke specification. The level data give automorphic data, base change data and an automorphic specialization, and from the specialization come the local bridges. The values of the characters $\chi_i$ at the chosen elements are Teichmüller lifts of the character values or of their inverses. For two indices with the same $\mu$ and $j$, the sums of the type spaces agree. From unique blocks, the density of split Frobenius elements and these two facts there are type data with their three ties, and the residual representations are semisimple. $\square$

**Theorem 6.7.6 (Automorphic side at a stage).** Assume $\mathcal{P}$. Let $x$ be a stage and $l$ a strict henselian acyclic level datum over $x$ with data $A$, $M$, $\chi$ and a tuple. Then the automorphic side exists for $(A, M, \chi)$.

Lean: `GlobalTheory.HeightCounting.Fin3.builtEx_of_published_inputs'`.

*Proof.* Apply the theorem on localization data to the datum of $x$. Global Artin reciprocity is a field of $\mathcal{P}$, and the density of split Frobenius elements follows from Chebotarev for primes of degree one. The matrix input follows from the level datum. The conditions on conjugation, on the exponents and on split places are fields of $l$. The values of the twist characters lie in $L$. The map from the integers is a field of $l$. Unique blocks follow from five published inputs and the cohomology datum of $l$. $\square$

**Theorem 6.7.7 (Rows at all stages).** For every datum $P$ reached by $\mathrm{Step}_w$ from the start condition, $P$ has rows.

Lean: `GlobalTheory.HeightCounting.Fin3.start_at_all_pre2`.

*Proof.* From pinned data with the column condition, row data exist at every datum; the steps from the start condition reach pinned data, and the property passes to all data along the steps. $\square$

**Theorem 6.7.8 (Level three object at a stage).** Assume the Weil representation of a unitary dual pair, existence of discrete series, $\mathcal{P}$ and the archimedean comparison. Let $x$ be a stage of a datum $P$ with rows, and $l$ a strict henselian acyclic level datum over $x$ with data $A$, $M$ and norm choice $\chi$. Let $N$ be a norm choice extension. Assume:

1. if the automorphic side exists for $(A, M, \chi)$, then for large enough coefficient data the localized datum $D'$ is large and its eta values $\eta_j(v)$ equal those of $P$ for $1 \le j \le m$;
2. there are theta data whose sets are all full for $1 \le j \le m$;
3. each core that lies in the extension with law and has the list condition for every $c$ with the list condition at $x$ has a datum of $N$.

Then for each $S$-extension $S$ and geometry $\Gamma$ there are a stage $Z$ and a level three object $v$ at the parameter set of $(N, S, \Gamma)$ with the same weights as $P$, whose norm choice is kept by $\chi$: the two norm choices agree in their Galois data, twist data, forms and twist fields.

Lean: `GlobalTheory.HeightCounting.Fin3.lv3_of_third_alt_alt`.

*Proof.* By [the automorphic side at a stage](/entry/built-ex-of-published-inputs-prime/) and hypothesis 1 there are localization data $L$ such that the localized datum is large with the right eta values. The archimedean comparison gives level data at all levels for $l$ and $L$. From the rows of $P$ and the eta values there are a row side, row data with a nonempty row set and a reading related to $L$. There is a core in the extension with law with the list condition, and hypothesis 3 gives a datum of $N$ at it. The object $v$ is assembled from these parts, with the local character choice of $L$ and $l$ as norm choice, which is kept by $\chi$. $\square$

**Theorem 6.7.9 (Finiteness).** Assume the Weil representation of a unitary dual pair, existence of discrete series and $\mathcal{P}$. Let $h_L$ be a recursion datum with the archimedean comparison, the eta statement and the existence of theta data. Then:

1. at every stage $x$ of a datum $P$, for every strict henselian acyclic level datum $l$ over $x$, every $S$ and every $\Gamma$, there is a level three object at the parameter set of the extension with law, $S$ and $\Gamma$, with the weights of $P$ and its norm choice kept by the character choice of $l$;
2. for each real $c$, the same holds at stages with the list condition for $c$, at the parameter set of the extension with list for $c$.

Lean: `GlobalTheory.HeightCounting.Fin3.sFin_and_sFinl_of_theta_data_exists` (also `GlobalTheory.T.sFin_and_sFinl_of_archCmp_sEta_thetaData`, a second name).

*Proof.* By the theorem on rows at all stages, every datum reached has rows; join this to the eta statement and the existence of theta data along the steps. At one stage, [the level three object at a stage](/entry/lv3-of-third-alt-alt/) applies with $N$ the extension with law, and hypothesis 3 is immediate. For item 2 take $N$ the extension with list: a datum of it pairs a datum of the extension with law with the list pin given by the list condition at $x$. $\square$

**Remark 6.7.10 (Formalization).** The theorems are at [FinitenessOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinitenessOfHyp.lean#L85) (the second name at line 102, the level three object at line 61, the automorphic side at line 35), [LocAllExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocAllExists.lean#L17), [LocAllExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocAllExistsStatement.lean#L11), [NdSpecExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NdSpecExists.lean#L21), [NdSpecExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NdSpecExistsStatement.lean#L11) and [RowsAtStart.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsAtStart.lean#L145). In `ndSpec_exists_alt` the conjugation and exponent hypotheses are introduced as `_ _` (line 22) and not used, and the section `Psi` at lines 13 to 19 declares variables and no declaration. `HeckeStdPlain` is a hypothesis of `ndSpec_exists_alt` but is the proved theorem `heckeStdPlain`, supplied by `locAll_exists_alt`. `ThetaDataExists` speaks of second level data, and the finiteness proof uses it at a third level datum through `⟨l.toLI, l.b.toSeriesState⟩`. The name `builtEx_of_published_inputs'` says "built", but its conclusion is `AutomorphicSideExists`; the older `builtEx` in the IwasawaDecomposition folder proves `BuiltEx`. The names `side_rational_hecke_data_alt` and `side_rational_eigen_data_alt` speak of rational data, but their conclusions are localization data and a Hecke specification. The proof of `start_at_all_pre2` is `Step.trans exists_rowsT (Step.of_all …)`, with `exists_rowsT` at [ExistsRowsT.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsRowsT.lean#L28). The level three object copies `lv3_of_third` of the older folder, with `PublishedInputsThirdLayerAlt` and `RecTExists` in place of `PrN` and `LocalLanglandsGL`. We did not unfold `Lv3`, `NormChoiceCore`, `RowsT`, `ThData`, `LocAll`, the type data or `QOver` and `QConj`, and read the statements of the lemmas, not their proofs.
