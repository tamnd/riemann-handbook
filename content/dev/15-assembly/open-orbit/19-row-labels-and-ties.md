---
title: Row labels and ties
decls:
  - GlobalTheory.Fc.LabLinked.row_lab_of_layer_alt_alt
  - GlobalTheory.T.good_ft_entries_alt_alt
  - GlobalTheory.Fc.LabLinked.row_lab_of_good_alt_alt
  - GlobalTheory.Fc.LabLinked.ties_of_built_genPin
  - GlobalTheory.Fc.LabLinked.ties_of_genPin_goodFTAll'
  - GlobalTheory.Fc.LabLinked.ties_of_nAtData_real
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row labels and ties

This section proves [the Theorem on labels](/entry/good-ft-entries-alt-alt/), which step 8 of [the Theorem on the open parameter statements](/entry/open-orbit-of-unramified-exponents-alt/) uses. The label row asks that every selected bundle condition of a good linked bundle carries ties: a Hida setting with a good operator and an isometry of its Poincaré space with the space of the datum, tied to the automorphy, to the row dictionary and to the labels. The theorem derives the label row from the good row, which says that every first term is good. The bridge is a pin on the label data at the witness points: the label data of the local groups are the generic label data. Fact (a) of the open parameter statements gives this pin, through the extensions with law.

We keep the notation of [the section on the open parameter statements](/entry/open-orbit-of-unramified-exponents-alt/) and of [the section on the defect row](/entry/weil-unitary-entries-prime/). $h_L$ is a recursion datum, $N$ an extension choice, $S$ an $S$-extension, $\Gamma$ a geometry, and $p$ the parameter set of $(N, S, \Gamma)$. A datum $D$ has the primes $g_k$ of its host, and at each $g_k$ the generic label datum $\mathrm{gen}_k$ of the type places. An $N$-datum $a$ at $D$ carries local groups with label data $\zeta_k$, a representation $\mathrm{rep}$ of the finite types, a row side and a depth. A witness point $q$ has core data of the point with an $N$-datum.

**Definition 4.19.1 (Ties).** A datum $D$ has *ties* if there are a Hida setting $X$ for $D$, a good operator $G$ on $X$, and a linear isometry $\iota$ of the space $H_D$ of $D$ with the Poincaré space of $X$, such that the automorphy tie holds for $D$ and the places of $X$, the row dictionary tie holds for $(X, G, \iota)$, and the label tie holds for $(X, \iota)$.

**Definition 4.19.2 (Good first terms, generic pin).** $D$ has *good first terms* if every first term $\sigma$ of $D$ gives a good row. An $N$-datum $a$ is *generically pinned* if $\zeta_k = \mathrm{gen}_k$ for every $k$.

The *label row* and the *good row* are

$$
\begin{aligned}
&\mathrm{Row}(Q, \Lambda, \mathrm{AtAll}(\mathrm{Ties})),\\
&\mathrm{Row}(Q, \Lambda, \mathrm{AtAll}(\text{good first terms})),
\end{aligned}
$$

in the notation of [the section on rows](/entry/fam-mi-star-row-alt-alt/).

**Theorem 4.19.3 (Ties of an N-datum).** Assume the green statement for the general linear groups over finite fields and the polynomial ring of Zelevinsky. Let $a$ be an $N$-datum at $D$ with a real datum $R$, a face $F$, a row side, a reading $Y$, norm realisation data $r$ and saturation data $s$. Assume the label tie for $D$ at the generic label data, that $a$ is generically pinned, and that $D$ has good first terms. Then $D$ has ties.

Lean: `GlobalTheory.Fc.LabLinked.ties_of_nAtData_real`.

*Proof.* We get the type labels from the pin, and the ties from a result on spectral objects.

1. *Type labels.* The datum of $a$ is $D$ with the local data of $a$, so we may argue at the datum of $a$. A result of another chapter, stated as local Bessel multiplicity one, gives the type labels of $\mathrm{rep}$ from the green statement, the polynomial ring of Zelevinsky, the label truth of $a$, the representation parameters, the depth of the row, the label tie, and one more hypothesis: at each $k$ and each place $v$ the local group is tame with label datum $\mathrm{gen}_k$. The tameness is a field of $a$, and the label datum is $\mathrm{gen}_k$ because $a$ is generically pinned. The norm realisation data identify $\mathrm{rep}$ with the representation of $a$.
2. A result of another chapter on row frames gives the two row frame parts of the reading $Y$.
3. The saturation data $s$ give a Hida setting $X$ with a good operator $G$ and an isometry $\iota$.
4. [The Theorem on the irreducibility conditions of constructed spectral objects](/entry/constructed-spectral-objects-irreducibility-conditions/), with steps 1 and 2 and the good first terms, gives the three ties for $(X, G, \iota)$. $\square$

**Theorem 4.19.4 (Ties at a witness point).** Under the same two published statements, let $q$ be a witness point of the scale of $p$ whose $N$-datum is generically pinned. If the datum $D_q$ has good first terms, then $D_q$ has ties.

Lean: `GlobalTheory.Fc.LabLinked.ties_of_genPin_goodFTAll'`.

*Proof.* The witness point gives the real datum and the row datum of its core data, saturation data at its weighted point, and the label tie from its rows. Apply the Theorem on ties of an N-datum. $\square$

**Theorem 4.19.5 (Ties of built bundles).** Under the same two published statements, assume that at every context and every witness point of $p$ the $N$-datum is generically pinned. Then for each bundle condition $b$ of $(D, O, c)$ that is built from the linkage of $p$, if $D$ has good first terms, then $D$ has ties.

Lean: `GlobalTheory.Fc.LabLinked.ties_of_built_genPin`.

*Proof.* By induction on the construction. A built bundle condition is the bundle condition of a linked bundle. The linkage gives a witness point $q$ and an equality of $(D, O, b)$ with the data at $q$; in particular $D = D_q$. The Theorem on ties at a witness point applies. $\square$

**Theorem 4.19.6 (Label row from the good row).** Assume the green statement and the polynomial ring of Zelevinsky. Assume that every $N$-datum given by $N$ is generically pinned. If $p$ is linked at the good row, then $p$ is linked at the label row.

Lean: `GlobalTheory.Fc.LabLinked.row_lab_of_good_alt_alt`.

*Proof.* Let $R$ be the predicate of the linkage of the good row, with its large base condition and its row. We keep $R$ and the large base condition, and change the row. The row of good first terms has a property $E$ of bundle conditions, and each value of a selection satisfies $E$ and is built. Let $(\mathcal A, \sigma)$ be a selection and let $\sigma(F, x, i)$ be one of its values, at a datum $D$ with good first terms. The selection gives that $\sigma(F, x, i)$ is built. The hypothesis on $N$ applies at each witness point, since its $N$-datum is given by $N$. So the Theorem on ties of built bundles gives ties for $D$. $\square$

**Theorem 4.19.7 (Labels).** Assume the green statement for the general linear groups over finite fields and the polynomial ring of Zelevinsky. Assume that every $N$-datum given by $N$ has an extension with law. If the parameter set $p$ of $(N, S, \Gamma)$ is linked at the good row, then it is linked at the label row.

Lean: `GlobalTheory.Fc.LabLinked.row_lab_of_layer_alt_alt` (also `GlobalTheory.T.good_ft_entries_alt_alt`, a second name).

*Proof.* The first component of an extension with law contains the generic pin $\zeta_k = \mathrm{gen}_k$. So every $N$-datum given by $N$ is generically pinned, and the Theorem on the label row from the good row applies. $\square$

The published input that does the work is the green statement, through the type labels of step 1 of the first proof. The good first terms are an input of the theorem, as the good row; the label row is the same row with the ties in place of the good first terms.

**Remark 4.19.8 (Formalization).** The theorems are all at [RowLabOfLayer.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowLabOfLayer.lean#L44): the ties of an N-datum at line 44, at a witness point at line 59, of built bundles at line 63, the label row from the good row at line 72, the labels at line 77, and the second name at line 86. Step 1 of the first proof is the lemma `typeLab_of_gen_alt_alt` at line 24. The ties are `Ties` in Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/GoodFtEntries.lean at line 19, the generic pin is `GenPinAlt` in [GenPin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GenPin.lean#L13), and the label row is `RowLabelCondition` in [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L27). Some details:

- The second name `good_ft_entries_alt_alt` is proved at line 87 by a `first` combinator that tries three ways of applying `row_lab_of_layer_alt_alt`. Its statement is the same as that of `row_lab_of_layer_alt_alt`.
- Step 1 of the first proof calls `UpperTheory.Lit.Dz.localBesselMultiplicityOne`. Despite its name, it is a theorem of LocalSeriesConcreteOfDzSwap.lean (line 40), proved from `rowTruth_of_labelTie_alt` and `global_artin_reciprocity_trivial`, and its statement `LocalBesselMultiplicityOne'` concludes type labels, not a multiplicity one statement for Bessel models.
- GoodFtEntries.lean has an older parallel chain (`typeLab_of_gen` at line 31 to `row_lab_labelCondition_of_localLanglands` at line 108) with the extra published hypothesis `DepthZeroInertia` and the local Langlands correspondence in place of the recursion datum.
- The field of a witness point used in the second proof is named `core_data_of_point`, the same last name as the theorem of [the section on true family data](/entry/all-true-family-datum-alt/); the two are unrelated.
- In the proof of the ties of built bundles, line 67 discards two hypotheses of the base case and the bundle witness with `-`.
- GenPin.lean opens and closes an empty `section Rows` (lines 17 and 18).
- We have not opened `RowFrameParts.main`, the saturation data, `lab_of_rows`, nor unfolded the automorphy, row dictionary and label ties, the green statement and the extensions with law.
