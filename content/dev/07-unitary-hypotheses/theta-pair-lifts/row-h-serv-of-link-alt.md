---
id: row-h-serv-of-link-alt
title: The service row from Artin reciprocity
kind: theorem
decl: GlobalTheory.row_hServ_of_link_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowHServOfLink
covers: 10828
status: drafted
drafted_by: writer@claude
---
This theorem gives the service row for a linkage of bundles from global Artin reciprocity. The linkage must send each bundle to a reciprocity record that `ReciprocityLinkage p` links. Its user is [`hServ_of_linkR`](/entry/h-serv-of-link-r/), which has the same statement and feeds the field `hServ` of [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/). The proof is short. The real content is in [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/), which dominates 10,819 of the 10,828 declarations below this theorem.

## Statement

`GlobalArtinReciprocity` says: for each number field $E$ and each algebraic closure $\Omega$ of $E$, there is a homomorphism from the ideles of $E$ to the Galois group of the maximal abelian extension of $E$ in $\Omega$ that is a global Artin map. That is, it is an open quotient map, its kernel is the closure of $E^\times$ times the identity component of the infinite ideles, and at each place it sends local units onto inertia, uniformizers to inverse Frobenius elements, and the closure of the image of the local ideles is the decomposition group. This is the Artin reciprocity law of class field theory (J. Neukirch, Algebraic Number Theory, Ch. VI).

**Theorem.** Assume `GlobalArtinReciprocity`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/), let $p$ be parameters for $h_L$, and let $L_k$ be a linkage of bundles. Assume that for each context $K$, point $\beta$, real $c$ and bundle $b$ at $\beta$, if $L_k$ links $b$ then `ReciprocityLinkage p` links the reciprocity record $b.R$ of $b$. Then `SlotServiceCondition (IsGoodE p.s) Lk` holds.

Here `SlotServiceCondition Q Lk` is `Row Q Lk SelectionServesFamily`: there is a property $E$ that, eventually, each bundle at a point of $Q$ linked by $L_k$ has, and each selection $\sigma$ of such bundles with property $E$ serves its family class $\mathcal A$ on the subclass `D3 3 𝒜`. "Serves" has two [closed](/step/closed-def/) parts, `twU` (eventual twist bounds) and `pdv` (conditions on the orbits of the kernel entries). We have not unfolded these parts further.

## Proof

1. `reciprocity_kernel_of_artin`, a renaming of `servH_row_linkR_alt`, gives the row of `ServH` at the slot `IsGoodE p.s` for the linkage `ReciprocityLinkage p` of reciprocity records.
2. `Row.map` moves this row along the map $b \mapsto b.R$ from bundles to records. The slot does not change, and the hypothesis on $L_k$ is the transport of the linkage. This gives the row of `ServH` for $L_k$, with the kernel `b.R.T.ker`.
3. `row_hServ_of_kerServ_alt` turns the row of `ServH` into the service row. It restricts the first part of `ServH` to `D3 3 𝒜`, and it gets `pdv` from the second part.

## In the Lean code

The theorem is at [RowHServOfLink.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfLink.lean#L17). `row_hServ_of_kerServ_alt` is at [RowHServOfKerServ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHServOfKerServ.lean#L13), `reciprocity_kernel_of_artin` at [ServHRowLinkRStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ServHRowLinkRStatement.lean#L14), and `Row.map` at [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L337).

In `row_hServ_of_kerServ_alt` (line 21 and 22), the threshold record for `pdv` is taken from the `twU` part, and the size hypothesis of `pdv` is not used.
