---
title: The bundle statement
decls:
  - GlobalTheory.T.geometric_parameter_uniform_alt
  - GlobalTheory.Mem.Top.Bl.exBL_isLinked_prmR_alt
  - GlobalTheory.T.local_langlands_prm_reduction_alt
  - GlobalTheory.Mem.R3.SelAll.bwit_exists_alt
  - GlobalTheory.T.selected_realization_side_alt
  - GlobalTheory.Mem.R3.RecInAt.recIn_parts_exists_alt
  - GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The bundle statement

This section proves the bundle statement $\mathrm{ExB}(\mathrm{KP}_x, Q_s, Q'_s, \Lambda)$ of Section 1 for the parameter set of a norm choice extension $N$ whose data give data with law. It is the bundle half of [the pair theorem](/entry/exists-base-lattice-of-pair-alt/) in Section 2, where it enters as step 3. The proof joins three inputs: a witness condition, which comes from the moving condition; a zeta compatibility at every weighted point; and bundle witnesses. The bundle witnesses are the deep part. They rest on a recursive input whose rows of parts hold because the parameters of the isotypic parts are fixed by Harish-Chandra's discrete series and by global Artin reciprocity.

Throughout, $h_L$ is a recursion datum, $N$ is a norm choice extension for $h_L$ and $\Gamma$ is a geometric predicate. We write $p = p(N, \Gamma)$ for the parameter set with position $\mathrm{RX}$, extension $N$, the trivial $S$-extension and geometry $\Gamma$, and $s$ for its scale. So $p(N)$ of Section 1 is $p(N, \Gamma)$ for the closure of the trivial geometry. We say that *the data of $N$ have laws* if every datum of $N$ at a point gives a datum of the extension with law of Section 1 at the same point.

**Definition 6.10.1 (Weighted points, records and bundles).** A *weighted point* $q$ of $s$ over a context $K$ consists of a base $B$, a frame $f$, a twist datum $T$, a column datum $w$, a stage $Z$ of $w$, an object $O$ of $s$ at the datum $D_q = D_w(Z)$, and the extra data of $s$ at this object. The extra data contain a third level datum with a base point $z$ and a real datum $R_q$, and a saturation $(S_P, S_R)$ of $D_q$ at the forms of $O$: an $S$-pack and an $S$-rest. A *record* for $O$ is a recursion datum for the local Langlands laws at $O$; it carries the forms of the columns of $O$. A record $R$ is *compatible* with $q$ if its reciprocity data agree with those of $q$ at all places of the weight. For $c \in \mathbb{R}$, a *bundle condition* $b$ at $(D_q, O, c)$ is a bundle of $O$ at the constant $c$ with a record $b_R$, and a *bundle witness* for $q$ and $b$ is a selected realization of the bundle that fits the base point of $q$.

The *multiplicity condition* for $p$ says that eventually, at every weighted point $q$ of $s$, the multiplicity equation holds for $R_q$. The *witness condition* $\mathrm{Wit}(s)$ says that the witnesses of $s$ pass from a set to each part of a division of it, and it follows from the moving condition $\mathrm{Mv}(s)$ of Section 2 (the position slot of $s$ moves to each new stage). The *zeta compatibility* at $q$ says that the zeta values of the readings of $q$ agree with the tied zeta data of $D_q$.

We take as given the following statements from the literature. They are among the fields of $\mathcal{H}_A$ and $\mathcal{H}_M$ in Section 1.

1. Green's classification of the cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_q)$ ([depth zero representations and types](/learn/representations/#depth-zero-representations-and-types)).
2. The discrete series cover and the existence of [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees) of $U(p, q)$ with given Harish-Chandra parameter, and the finiteness theorem of Harish-Chandra for automorphic forms.
3. The theory of Harish-Chandra modules and the Casselman-Wallach theorem.
4. The [Weil representation](/learn/theta/#the-weil-representation) of a unitary dual pair.
5. Rapid decay of [cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms).
6. [Global Artin reciprocity](/learn/class-field-theory/#global-class-field-theory), the existence of ray class fields, and Weber's construction of ray class fields.

**Theorem 6.10.2 (Parts of the recursive input).** Assume statements 1 to 5, global Artin reciprocity and the existence of ray class fields. Let the data of $N$ have laws, let $K$ be a context and $q$ a weighted point of $s$ over $K$. Assume that every assembled stage $X$ with $K$ over its pre-base satisfies the host hypotheses, that the field $F$ of its host is the maximal real subfield of $E$, that its hermitian forms $W_c(i)$ and $V_c(i)$ are diagonal, that $V_c(i)$ is positive definite, that its lattices are standard, and that $V_c(i)$ and $X'$ have orthonormal frames that span their lattices over $\mathcal{O}_E$. Assume the multiplicity equation for $R_q$. Let $R$ be a record compatible with $q$, let $(S_P, S_R)$ be the saturation of $q$, read at the forms of $R$, let $a$ be a twist argument of $O$ with twist input $x$, and let $y$ be a real input. Then there is a recursive input $r$ for $y$ such that the realization of $r$ satisfies the row of parts condition.

Lean: `GlobalTheory.Mem.R3.RecInAt.recIn_parts_exists_alt` (also `GlobalTheory.T.selected_realization_side_alt`, a second name).

*Proof.* The level of the twist argument $a$ gives the character data of $x$ and the field condition at the stage. The matrix reading of the base point gives the tuple of $y$. A row of parts holds as soon as the eigensystem index set is fixed and the characters are good, and we check two conditions for this.

1. For each character $\chi$ of the index set, $e_\chi \, e_{\mathrm{lvl}} \neq 0$, where $e_\chi$ is the idempotent of $\chi$ and $e_{\mathrm{lvl}}$ is the level idempotent. This holds because the geometric parameter of the reciprocity record is attained: by global Artin reciprocity and the existence of ray class fields, every character of the index set is the character of a class at the level.
2. On every nonzero isotypic part, $\log \Lambda = \log \lambda_3$, where $\Lambda$ is the parameter of the part and $\lambda_3$ is the third parameter of the real datum. The isotypic part is a discrete series at the real place, its Harish-Chandra parameter is fixed by the existence theorem of statement 2, and the parameter of its reciprocity record is the same by Green's classification at the depth zero places.

The finiteness of Harish-Chandra and the rapid decay of cusp forms give that the parts are finite dimensional and that the eigensystem sum is direct. The Weil representation gives the eigensystem of the theta lift. With these two conditions, the row of parts condition holds for the recursive input whose tuple is the tuple of $y$. $\square$

**Theorem 6.10.3 (Bundle witnesses).** Assume statements 1 to 5, global Artin reciprocity and the existence of ray class fields. Let the data of $N$ have laws, and assume the multiplicity condition for $p$. Then eventually in $K$ the following holds. Let $q$ be a weighted point of $s$ over $K$, $R$ a record compatible with $q$, $c \in \mathbb{R}$, and $(n_1, n_2)$ a pair of natural numbers with $\Delta(D_q) = n_1$ and $\eta(O) = m \, n_2$, where $m$ is the number of rows of $D_q$. If the scale of $O$ is the scale of $K$ and the values of $O$ lie in the bounds of $K$, then there is a bundle condition $b$ at $(D_q, O, c)$ with $b_R = R$ and a bundle witness for $q$ and $b$.

Lean: `GlobalTheory.Mem.R3.SelAll.bwit_exists_alt` (also `GlobalTheory.T.local_langlands_prm_reduction_alt`, a second name).

*Proof.* Eventually in $K$, every stage over $K$ satisfies the host and frame conditions of the theorem on parts, and the multiplicity condition holds. Fix $q$, $R$ and $c$. The saturation of $q$ gives an $S$-pack and an $S$-rest at the forms of $R$. We build the bundle in five steps.

1. There is a selected realization of the bundle at $(D_q, O, c)$ for the record $R$; it is geometric, so its lower map lies in the geometric data of $q$.
2. The real side of the realization comes from the theorem on parts above: its recursive input has a row of parts. This is the only step that uses Green's classification.
3. The lower map of the realization holds at the base point of $q$.
4. A host datum for the realization exists by global Artin reciprocity, with the pins of the weighted point given by the existence of ray class fields.
5. The side realization holds with this host datum.

The bundle condition $b$ has the realization of step 1 and the record $R$, so $b_R = R$, and steps 2 to 5 give the bundle witness. $\square$

**Lemma 6.10.4 (Square integrable columns).** Let $q$ be a weighted point of $s$, let $t$ be a tied kernel entry of the object of $q$ that is pinned at $q$, and assume that the position slot of $q$ is nonempty. Then there are a column datum $D_c$, a spectral datum $S_{p,0}$, a scale datum $Z_0$ and a reading $C_0$ of $(D_c, S_{p,0}, Z_0)$ with the following property. For every kernel datum with kernel $t$, and every argument $a$ with twist input $x$ such that the column datum of $a$ is $D_c$, there is a record $C$ of square integrable columns whose face, spectral datum and weights are those of $a$ and of the base of $q$, and whose column characters are compatible.

Lean: `GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses`.

*Proof.* The standard model of the pinned kernel entry $t$ gives the column datum $D_c$ and the scale datum $Z_0$. A reading $C_0$ exists with the identity as its unitary part, for the trivial period datum on $\mathbb{C}$. For a given argument $a$ with the column datum $D_c$, the record $C$ takes the face and the spectral datum of $a$, the weights of the base of $q$ and the group of $x$, and the column characters agree because both come from the standard model of $t$. $\square$

**Theorem 6.10.5 (Bundle statement).** Assume statements 1 to 6. Let the data of $N$ have laws, assume the moving condition $\mathrm{Mv}(s)$ and the multiplicity condition for $p$. Then $\mathrm{ExB}(\mathrm{KP}_x, Q_s, Q'_s, \Lambda_p)$ holds, where $Q_s$ and $Q'_s$ are the slots of built and good cores and $\Lambda_p$ is the bundle linkage of $p$.

Lean: `GlobalTheory.Mem.Top.Bl.exBL_isLinked_prmR_alt` (also `GlobalTheory.T.geometric_parameter_uniform_alt`, a second name).

*Proof.* There are three inputs.

1. The moving condition gives the witness condition $\mathrm{Wit}(s)$, since witnesses pass along divisions of sets.
2. The discrete series cover, Harish-Chandra modules, Casselman-Wallach, Harish-Chandra finiteness and rapid decay give the zeta compatibility at every weighted point. At a weighted point $q$ we take a pinned kernel entry, the lemma on square integrable columns gives a reading $C_0$, and the reading, moved to the face of $q$, gives rational division pairings on the rational points; the law of the datum of $N$ at $q$ then ties the zeta values.
3. The theorem on bundle witnesses gives the bundle witnesses.

A linking theorem for bundles, which uses global Artin reciprocity, Weber's ray class fields and the existence of ray class fields, takes the three inputs to the bundle statement. Its slot $R$ is the slot of all cores, so the large base condition $\mathrm{LB}(\mathrm{KP}_x, Q_s, R)$ holds. $\square$

**Remark 6.10.6 (Formalization).** The theorems are at [ExBLIsLinkedPrmR.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExBLIsLinkedPrmR.lean#L21), [BwitExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BwitExists.lean#L53), [RecInPartsExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RecInPartsExists.lean#L30) and [ExistsRowsKCColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsRowsKCColPins.lean#L213); the second names are relays by `first | exact … | …`. In `bwit_exists_alt` the line `rintro κ K - ⟨hH, hMK⟩ q R hR c DH _ _` (line 56) drops the hypotheses that the scale of $O$ is $K_s$ and that the values lie in the bounds, so they are unused. In `square_integrable_columns_of_witnesses` the hypothesis on `eNu` is dropped with `_`, only the field `std` of `KPin` is used, the reading $C_0$ is built from a dummy period datum (`ℂ`, zero maps, `⊥`), and the record `SquareIntegrableColumns` has only data and equality fields: it states no square integrability. Its only caller, `ze_u_prm_of_extension_with_law` ([ZeUPrmRNEb.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ZeUPrmRNEb.lean#L42)), keeps $D_c$, $S_{p,0}$, $Z_0$ and $C_0$ and discards the rest. The linking theorem `exBL_isLinked_alt` takes the slot `fun _ _ _ _ _ => True`, so the large base condition is trivial. The names "geometric parameter uniform", "local Langlands prm reduction" and "selected realization side" do not describe the statements. We did not unfold `BundleCondition`, `BundleWitness`, `BundleLinkage`, `RecordCompatibleExtended`, `ZeU`, `WitExE` or the row of parts condition, so the definitions above give only their roles; the steps of the proofs follow the statements of the lemmas called.
