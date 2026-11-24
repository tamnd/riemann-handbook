---
title: The service row
decls:
  - GlobalTheory.T.hServ_of_linkR
  - GlobalTheory.row_hServ_of_link_alt
  - GlobalTheory.T.reciprocity_kernel_of_artin
  - GlobalTheory.Svd.servH_row_linkR_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The service row

This section proves the service row of the record of all rows from global Artin reciprocity. Step 6 of [the theorem on all rows](/entry/all-rows-of-open0-alt/) uses it. A bundle carries a reciprocity record, and the bundle linkage $\Lambda_p$ links a bundle only when the reciprocity linkage of $p$ links its record. So it is enough to prove a row for records and then to move it to bundles. The row for records is a special case of [the general service row](/entry/serv-h-row-of-artin/), and that row holds the analytic content. Here we check its two side conditions and move the row.

**Definition 8.4.1 (Global Artin reciprocity).** *Global Artin reciprocity* says: for each number field $E$ and each algebraic closure $\Omega$ of $E$, there is a homomorphism from the ideles of $E$ to the Galois group of the maximal abelian extension of $E$ in $\Omega$ with five properties. It is an open quotient map. Its kernel is the closure of $E^\times$ times the identity component of the infinite ideles, so it factors through the [[idele class group|9GHD9MXNYV]]. At a finite place $v$, the local units map onto the inertia group. A uniformizer at $v$ maps to the inverse of a Frobenius element. The closure of the image of the local ideles at $v$ is the decomposition group.

This is the reciprocity law of [global class field theory](/learn/class-field-theory/#global-class-field-theory) (Neukirch, Algebraic Number Theory, Chapter VI; Tate, Global class field theory, in Cassels and Fröhlich, Algebraic Number Theory, Chapter VII).

Fix $h_L$ as in [the local Langlands recursion](/step/rect-exists-def/) and a parameter set $p$ over $h_L$. Each point $q$ with data $O$ has a type of *reciprocity records*. A record $R$ has a kernel entry $\ker R$, which is a datum of the record. It is not the kernel of the Artin map. The *reciprocity linkage* $\Lambda^{\mathrm{rec}}_p$ links a record $R$ at a point $q$ of the good slot $Q'_p$ when $R$ is compatible with $q$ in the extended sense. This compatibility has the spectral data, a pin of the kernel and the unit coordinates, and three more conditions. One of these is the standard tie of the kernel entry.

**Definition 8.4.2 (The service statement).** Let $\kappa$ map each record to its kernel entry. For a family class $\mathcal{A}$ and a selection $\sigma$, the *service statement* $\mathrm{Serv}_\kappa(\mathcal{A}, \sigma)$ has two parts. First, it is [closed](/step/closed-def/) on $\mathcal{A}$ that the twist bounds hold eventually. Second, past a threshold, the kernel entry $\kappa(b)$ of each selected record $b$ satisfies the orbit conditions. The *service row* at a slot $Q$ and a linkage $\Lambda$ of bundles is the row $\mathrm{Row}(Q, \Lambda, H)$ where $H(\mathcal{A}, \sigma)$ says that $\sigma$ serves its family class on $\mathcal{D}_3(\mathcal{A})$: the twist bounds hold on $\mathcal{D}_3(\mathcal{A})$ in the closed sense, and so do the orbit conditions.

The first part of $\mathrm{Serv}_\kappa$ does not depend on $\sigma$ or on $\kappa$.

**Theorem 8.4.3 (The service row for records).** Assume global [[Artin reciprocity|7938EKMMVR]]. Let $h_L$ and $p$ be as above. Then $\mathrm{Row}(Q'_p, \Lambda^{\mathrm{rec}}_p, \mathrm{Serv}_{\ker})$ holds.

Lean: `GlobalTheory.Svd.servH_row_linkR_alt` (also `GlobalTheory.T.reciprocity_kernel_of_artin`, a second name).

*Proof.* [The general service row](/entry/serv-h-row-of-artin/) gives $\mathrm{Row}(Q, \Lambda, \mathrm{Serv}_\kappa)$ for each slot $Q$, each linkage $\Lambda$ of records and each kernel map $\kappa$. It needs Artin reciprocity and two side conditions.

1. *Every point of $Q'_p$ has a part.* A good point is built, and a built point has a part.
2. *Eventually, each record that $\Lambda^{\mathrm{rec}}_p$ links has the standard tie for its kernel entry.* A linked record is compatible in the extended sense, and the standard tie is one of the conditions of this compatibility. This holds at all points, so it holds eventually.

So the general service row applies, with $\kappa = \ker$. $\square$

Artin reciprocity is only passed to the general service row. The two side conditions hold by the definitions of the good slot and of the reciprocity linkage.

**Theorem 8.4.4 (The service row).** Assume global Artin reciprocity. Let $h_L$ and $p$ be as above, and let $\Lambda$ be a linkage of bundles. Assume that for each context, each point $\beta$, each $c \in \mathbb{R}$ and each bundle $b$ at $\beta$, if $\Lambda$ links $b$, then $\Lambda^{\mathrm{rec}}_p$ links the reciprocity record $b.R$ of $b$. Then the service row at $Q'_p$ and $\Lambda$ holds.

Lean: `GlobalTheory.row_hServ_of_link_alt` (also `GlobalTheory.T.hServ_of_linkR`, a second name).

*Proof.* There are three steps.

1. The Theorem (The service row for records) gives $\mathrm{Row}(Q'_p, \Lambda^{\mathrm{rec}}_p, \mathrm{Serv}_{\ker})$.
2. A row moves along a map of bundles. Let $m$ send a bundle $b$ to its record $b.R$. The hypothesis says that $\Lambda$ links $b$ only if $\Lambda^{\mathrm{rec}}_p$ links $m(b)$. So the row of step 1 gives the row $\mathrm{Row}(Q'_p, \Lambda, \mathrm{Serv}_{\ker \circ m})$. Take for the property of bundles the pull back by $m$ of the property of records, and compose each selection with $m$.
3. The service statement on $\mathcal{A}$ gives the service row statement on $\mathcal{D}_3(\mathcal{A})$. The twist bounds restrict from $\mathcal{A}$ to the subclass $\mathcal{D}_3(\mathcal{A})$. The orbit conditions on $\mathcal{D}_3(\mathcal{A})$ come from the second part of the service statement, with the threshold of the twist bounds. $\square$

In step 6 of the theorem on all rows, the hypothesis on $\Lambda = \Lambda_p$ holds by the definition of $\Lambda_p$. The service row at $Q'_p$ then becomes a linked row with the true slot of Section 1.

**Remark 8.4.5 (Formalization).** The record row is at [ServHRowLinkR.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServHRowLinkR.lean#L14), and its second name at [ServHRowLinkRStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServHRowLinkRStatement.lean#L14). The service row is at [RowHServOfLink.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfLink.lean#L17), and its second name at [RowHServOfLinkStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfLinkStatement.lean#L14). Both second names are proved by a `first | exact … | …` tactic whose first branch closes the goal. The general row is `servH_row_of_artin`, used through its renaming `bundle_bothParts_of_standardKernel_of_globalArtinReciprocity`; the side conditions are `builtC_hasPart` and `linkR_stdTie_entry`, which reads the field `std` of `RecordCompatibleExtended`. Step 2 is `Row.map` and step 3 is `row_hServ_of_kerServ_alt`; at lines 21 to 22 of [RowHServOfKerServ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfKerServ.lean#L21), the threshold of the orbit part `pdv` is taken from the twist part `twU`, and the size hypothesis of `pdv` is not used. The name `reciprocity_kernel_of_artin` suggests the kernel of the Artin map, but the kernel is the record entry `R.T.ker`.
