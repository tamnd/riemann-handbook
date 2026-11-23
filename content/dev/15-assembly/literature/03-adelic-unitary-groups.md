---
title: Adelic unitary groups
decls:
  - UpperTheory.LiteratureTheorems.strong_approx_su_of_literature
  - UpperTheory.LiteratureTheorems.flath_tensor_product_of_literature
  - UpperTheory.LiteratureTheorems.flath_factorisation_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Adelic unitary groups

This section states two global facts on the adelic points of a unitary group: strong approximation for the special unitary group, and Flath's theorem that an irreducible unitary representation of the adelic group is a restricted tensor product of local representations. We prove the strong form of Flath's theorem from the weak form and from the admissibility of irreducible unitary representations of $p$-adic groups. Strong approximation and the strong form of Flath's theorem are fields of the bundles of the [unitary group hypotheses](/step/published-results-eigen/) and of the [local theta inputs](/step/published-results-first/). Background is in [unitary groups](/learn/groups/#unitary-groups), [strong approximation](/learn/groups/#strong-approximation), [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups) and [automorphic representations](/learn/automorphic-forms/#automorphic-representations).

Throughout, $F$ is a totally real number field, $E / F$ is a CM extension with conjugation $c$, and $J \in M_n(E)$ is a nondegenerate Hermitian matrix: ${}^t c(J) = J$ and $\det J \neq 0$. Let $G = U(J)$ be the [[unitary group|0R9R0Y1HDK]] over $F$, and let $SU(J) \subseteq G$ be the subgroup of determinant one. We write $\mathbb{A} = \mathbb{A}_F$, $G(\mathbb{A})$ for the adelic points and $G_v = G(F_v)$ for the local groups.

### Strong approximation

For a finite set $S$ of places of $F$, let $SU(J)(F_S) \subseteq SU(J)(\mathbb{A})$ be the subgroup of adelic points $g$ with $g_v = 1$ for $v \notin S$.

**Theorem 1.3.1 (Strong approximation for $SU$).** Let $n \geq 2$. Let $S$ be a finite set of places of $F$ such that $SU(J)(F_S)$ is not compact. Then $SU(J)(F) \cdot SU(J)(F_S)$ is dense in $SU(J)(\mathbb{A})$.

Lean: `UpperTheory.LiteratureTheorems.strong_approx_su_of_literature`.

The group $SU(J)$ is simply connected and almost simple over $F$, so this is a case of the strong approximation theorem of Kneser and Platonov (Platonov and Rapinchuk, *Algebraic Groups and Number Theory*, §7.4). The noncompactness of $SU(J)(F_S)$ means that $S$ contains a place where $SU(J)$ is isotropic.

*Proof.* We take the result from Platonov and Rapinchuk. In the development it is [Theorem 1.13.2 of Volume 10](/entry/strong-approx-su/). $\square$

### Flath's theorem

For each place $v$ let $(\pi_v, H_v)$ be an irreducible unitary representation of $G_v$. For almost all finite $v$ let $\xi_v \in H_v$ be a unit vector. The *restricted tensor product* $\bigotimes'_v (H_v, \xi_v)$ is the completion of the direct limit, over finite sets $T$ of places, of the spaces $\bigotimes_{v \in T} H_v$, with the maps $x \mapsto x \otimes \xi_v$. A *factorisation* of a unitary representation $\pi$ of $G(\mathbb{A})$ is a family $(\pi_v, \xi_v)$ as above together with a unitary $G(\mathbb{A})$-isomorphism $B : \bigotimes'_v (H_v, \xi_v) \to H$.

**Theorem 1.3.2 (Flath, weak form).** Every irreducible unitary representation of $G(\mathbb{A})$ on a Hilbert space has a factorisation.

Lean: `UpperTheory.LiteratureTheorems.flath_tensor_product_of_literature`.

*Proof.* This is Flath, *Decomposition of representations into tensor products* (Proc. Sympos. Pure Math. 33, part 1, 1979), together with the type I property of $G_v$. In the development it is [Theorem 2.6.9 of Volume 7](/entry/flath-tensor-product/). $\square$

The strong form adds two properties of the local factors at the finite places. For an $\mathcal{O}_E$-lattice $L \subseteq E^n$ and a finite place $v$, let $K_v(L)$ be the stabiliser of $L \otimes \mathcal{O}_{F_v}$ in $G_v$. It is a compact open subgroup, and for almost all $v$ it is a hyperspecial maximal compact subgroup.

**Lemma 1.3.3 (Admissibility).** Let $v$ be a finite place, let $\pi_v$ be an irreducible unitary representation of $G_v$ on a Hilbert space, and let $K \subseteq G_v$ be a compact open subgroup. Then the space of $K$-fixed vectors is finite-dimensional.

*Proof.* This is Bernstein's theorem that irreducible unitary representations of a reductive $p$-adic group are admissible (Bernstein, *All reductive p-adic groups are tame*, 1974). We take it from the literature. $\square$

**Theorem 1.3.4 (Flath, strong form).** Let $\pi$ be an irreducible unitary representation of $G(\mathbb{A})$ on a Hilbert space $H$. Then $\pi$ has a factorisation $(\pi_v, \xi_v, B)$ with these properties.

1. For each finite place $v$, the smooth vectors of $\pi_v$ form an irreducible admissible smooth representation of $G_v$.
2. For each $\mathcal{O}_E$-lattice $L \subseteq E^n$ and for almost all finite $v$, the space of $K_v(L)$-fixed vectors in $H_v$ is the line $\mathbb{C} \xi_v$.

Lean: `UpperTheory.LiteratureTheorems.flath_factorisation_of_literature`.

*Proof.* Take a factorisation $(\pi_v, \xi_v, B)$ from the weak form.

For part 1, fix a finite $v$. By the Lemma each compact open subgroup has a finite-dimensional space of fixed vectors in $H_v$. An irreducible unitary representation with this property has an irreducible admissible space of smooth vectors. This gives part 1.

For part 2, fix a lattice $L$. For almost all $v$ three things hold. The vector $\xi_v$ has norm one. The vector $\xi_v$ is fixed by $K_v(L)$, since it is part of the restricted tensor product. There is a continuous anti-involution $\theta$ of $G_v$ that fixes each double coset $K_v(L) \, g \, K_v(L)$. Fix such a $v$. Then $\xi_v$ is a smooth vector, because its stabiliser contains the open subgroup $K_v(L)$, and it is not zero. By Gelfand's trick, $\theta$ makes the Hecke algebra of $K_v(L)$-biinvariant functions commutative. So in the irreducible admissible representation of part 1 the space of $K_v(L)$-fixed vectors has dimension at most one. It contains $\xi_v$, so it is $\mathbb{C} \xi_v$. $\square$

The strong form is the form used in practice: almost all local factors are unramified for the lattice $L$, and $\xi_v$ is their spherical vector.

**Remark 1.3.5 (Formalization).** All three theorems take the record of open statements as an argument and do not use it. Strong approximation and the weak form of Flath's theorem are the terms `GlobalTheory.StrongApproxSUProof.strongApproxSU` and `CompanionTheory.Rg.Fl.B.flathTensorProduct` ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L373), lines 373 and 517). The strong form is `PositivityTheory.Prw.flathFactorisation_of` applied to the weak form and to the Lemma ([BridgesRep.lean](lean:Development/WeilBound/CoreStatements/AbelianHeightsDuality/PublishedTheoremStatements/BridgesRep.lean#L15)), which only forwards to the proof in [FlathFactorisationOfTensorProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FlathFactorisationOfTensorProduct.lean#L15). The Lemma is the term `CompanionTheory.Rg.Fl.B.unitaryIrreducibleAdmissible` at line 375 of the main file, stated at [UnitaryIrreducibleAdmissible.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/UnitaryIrreducibleAdmissible.lean#L12). The step from the Lemma to part 1, the anti-involution and the multiplicity one statement are the theorems `GlobalTheory.T.unitary_irreducible_smooth_admissible`, `GlobalTheory.T.eventually_exists_doubleCoset_antiInvolution_unitary` and `GlobalTheory.T.gelfand_pair_spherical_vector_unique`, which we did not read. The predicate `IsFactorisation` ([ForallEventuallyFinLocIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ForallEventuallyFinLocIff.lean#L106)) and the predicate `IsIrrUnitary` were not unfolded; the description of the restricted tensor product above is the standard one. The strong form is stated at [ExistsFactorisationCuspidal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/ExistsFactorisationCuspidal.lean#L36). In strong approximation the set $S$ is given by an idempotent adele $\varepsilon$, and $SU(J)(F_S)$ is the set of $g$ with $\varepsilon (g - 1) = g - 1$ ([NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L33)). A second proof of the same statement, also named `strongApproxSU` but in another namespace, is in [ImportsBis.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/ImportsBis.lean#L16).
