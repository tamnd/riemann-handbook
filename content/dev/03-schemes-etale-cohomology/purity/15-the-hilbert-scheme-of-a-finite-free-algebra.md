---
title: The Hilbert scheme of a finite free algebra
decls:
  - GlobalTheory.T.hilbert_scheme_finite_free_algebra_affine_exists
  - GlobalTheory.HilbAff.hilbertScheme_exists
  - GlobalTheory.ValuativeQuotient.main
  - GlobalTheory.T.affineHilbertScheme_valuativeCriterion_existence
  - GlobalTheory.T.affineHilbert_valuativeCriterion_uniqueness
  - GlobalTheory.T.affineHilbertScheme_representing_qc_qs_finiteType
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hilbert scheme of a finite free algebra

This section proves that $\operatorname{Spec} B \to \operatorname{Spec} A$ has a Hilbert scheme of every rank $r$ when $B$ is free of finite rank over $A$. The charts of section 14 show that the Hilbert functor is represented by a scheme $H$ of finite type over $A$. Properness comes from the valuative criterion: over a valuation ring, a finite flat subscheme of the generic fibre has exactly one flat closure. The next section glues this affine case to prove [Theorem 2.16.6](/entry/hilbert-scheme-finite-locally-free-representable-proper/). We keep the notation of section 14: $B$ has a basis $e_1, \dots, e_N$ over $A$, $\operatorname{Hilb}^r$ is the Hilbert functor, and $X_\sigma$ and $W_\sigma(y)$ are the charts and the basic loci.

**Theorem 2.15.1 (Valuative criterion of properness).** A morphism $h : H \to S$ is proper if and only if it is quasi-compact, quasi-separated and locally of finite type, and for every [[valuation ring|QSX12D8RQM]] $R$ with fraction field $K$ and every commutative square formed by $\operatorname{Spec} K \to H$ and $\operatorname{Spec} R \to S$ there is exactly one morphism $\operatorname{Spec} R \to H$ that makes both triangles commute.

See R. Hartshorne, *Algebraic Geometry*, Theorem II.4.7, for noetherian schemes, and the Stacks Project, chapter *Morphisms of Schemes*, section *Valuative criteria*, in general. We use it in this form.

**Lemma 2.15.2 (Flat closure).** Let $R$ be a valuation ring with fraction field $K$, let $P$ be an $R$-algebra and let $I$ be an ideal of $K \otimes_R P$. There is exactly one ideal $J \subseteq P$ such that $P/J$ is flat over $R$ and $J$ generates $I$. It is the inverse image of $I$ in $P$.

Lean: `GlobalTheory.ValuativeQuotient.main` (also `GlobalTheory.T.exists_flat_ideal_valuationRing_pullback`, the existence in the language of affine schemes).

*Proof.* Flatness can be tested on finitely generated ideals (Matsumura, §7), and over a valuation ring these are principal. So a module over $R$ is flat if and only if it has no torsion. The ring $K \otimes_R P$ is the localization of $P$ at the nonzero elements of $R$. Let $J$ be the inverse image of $I$. Then $P/J$ embeds into $(K \otimes_R P)/I$, which has no torsion, so $P/J$ is flat, and $J$ generates $I$ since localization commutes with taking ideals. Let $J'$ be a second such ideal. Clearly $J' \subseteq J$. If $b \in J$, then $m b \in J'$ for some nonzero $m \in R$, and since $P/J'$ has no torsion, $b \in J'$. $\square$

**Lemma 2.15.3 (Constant rank over a local base).** Let $R$ be a local ring and $f : V \to \operatorname{Spec} R$ finite and flat. Then $\operatorname{rk}_t(f)$ does not depend on $t$.

Lean: `GlobalTheory.HilbAff.finrank_const_of_isLocalRing`.

*Proof.* The scheme $V$ is affine, $V = \operatorname{Spec} M$, and $M$ is finite and flat over the local ring $R$, so free of some rank $n$ (Matsumura, Theorem 7.10). Every localization of $M$ is then free of rank $n$. $\square$

**Proposition 2.15.4 (Existence part).** Let $H$ represent $\operatorname{Hilb}^r$, with universal element $(h, U)$. Then $h : H \to \operatorname{Spec} A$ satisfies the existence part of the valuative criterion.

Lean: `GlobalTheory.T.affineHilbertScheme_valuativeCriterion_existence` (also `GlobalTheory.HilbAff.valuativeExistence`).

*Proof.* Let $R$, $K$ be as in the criterion and let $\operatorname{Spec} K \to H$ and $g : \operatorname{Spec} R \to \operatorname{Spec} A$ form a commutative square. The map $\operatorname{Spec} K \to H$ is a pair $(g_K, V_K)$, where $g_K$ is $g$ restricted to $\operatorname{Spec} K$ and $V_K$ is a closed subscheme of $Z_{\operatorname{Spec} K}$. The scheme $Z_{\operatorname{Spec} R} = \operatorname{Spec}(R \otimes_A B)$ is affine with generic fibre $Z_{\operatorname{Spec} K}$. The Lemma on flat closure gives a closed subscheme $V \subseteq Z_{\operatorname{Spec} R}$, flat over $R$, with generic fibre $V_K$. It is finite over $R$, as a closed subscheme of a finite scheme. By the Lemma on constant rank, its rank at the closed point equals its rank at the generic point, which is the rank $r$ of $V_K$. So $(g, V) \in \operatorname{Hilb}^r(\operatorname{Spec} R)$, and it restricts to $(g_K, V_K)$. The corresponding map $\operatorname{Spec} R \to H$ is the lift. $\square$

**Proposition 2.15.5 (Uniqueness part).** In the same situation, $h$ satisfies the uniqueness part of the valuative criterion.

Lean: `GlobalTheory.T.affineHilbert_valuativeCriterion_uniqueness` (also `GlobalTheory.HilbAff.valuativeCriterion_uniqueness`).

*Proof.* Two lifts correspond to pairs $(g, V)$ and $(g, V')$ over $\operatorname{Spec} R$ with the same generic fibre. Both are flat over $R$, so by the uniqueness in the Lemma on flat closure their ideals are both the inverse image of the ideal of the generic fibre. Hence $V = V'$, and the two lifts agree. $\square$

**Lemma 2.15.6 (Finiteness).** Let $H$ represent $\operatorname{Hilb}^r$, with universal element $(h, U)$. Then $h$ is quasi-compact, quasi-separated and locally of finite type.

Lean: `GlobalTheory.T.affineHilbertScheme_representing_qc_qs_finiteType` (also `GlobalTheory.HilbAff.representing_qc_qs_loft`).

*Proof.* For each $\sigma$ let $W_\sigma \subseteq H$ be the basic locus of the universal element. Both $W_\sigma$ and $X_\sigma$ represent the $\sigma$-basic pairs, so $W_\sigma \cong X_\sigma$ over $\operatorname{Spec} A$. So each $W_\sigma$ is affine and of finite type over $A$. By the Lemma on basic neighbourhoods the finitely many $W_\sigma$ cover $H$, so $H$ is quasi-compact. The intersection $W_\sigma \cap W_\tau$ is the $\tau$-basic locus inside the affine $W_\sigma$, which is quasi-compact by the Lemma on the basic locus. So $H$ is quasi-separated. $\square$

### The theorem

**Theorem 2.15.7 (Hilbert scheme of a finite free algebra).** Let $A$ be a ring, $B$ an $A$-algebra that is free of finite rank as an $A$-module, and $r \geq 0$. Then $\operatorname{Spec} B \to \operatorname{Spec} A$ has a Hilbert scheme of rank $r$.

Lean: `GlobalTheory.T.hilbert_scheme_finite_free_algebra_affine_exists` (also `GlobalTheory.HilbAff.hilbertScheme_exists`).

*Proof.* Choose a basis $e_1, \dots, e_N$ of $B$; if $A = 0$, take $N = 0$. For each injective $\sigma$ take the chart $(X_\sigma, \xi_\sigma)$ of the Lemma on charts and the basic loci $W_\sigma(y)$ of the Lemma on the basic locus. First, every pullback $f^* \xi_\sigma$ is $\sigma$-basic: the basic locus of $\xi_\sigma$ is all of $X_\sigma$, since $\xi_\sigma$ is $\sigma$-basic, so every $f$ has image in it. We check the three conditions of the Lemma on representability by open charts for $F = \operatorname{Hilb}^r$, which is a Zariski sheaf. Condition 1: $a$ has image in $W_\sigma(y)$ if and only if $a^* y$ is $\sigma$-basic, and this holds if and only if $a^* y = f^* \xi_\sigma$ for some $f$, by the Lemma on charts and the first step. Condition 2 is the uniqueness in the Lemma on charts. Condition 3 is the Lemma on basic neighbourhoods. So $\operatorname{Hilb}^r$ is represented by a scheme $H$ with universal element $(h, U)$. A morphism $f : T \to H$ with $h \circ f = g$ sends $(h, U)$ to the inverse image of $U$, so the universal property of a Hilbert scheme is the representability of $\operatorname{Hilb}^r$. The morphism $h$ is quasi-compact, quasi-separated and locally of finite type by the Lemma on finiteness, and it satisfies the valuative criterion by the two Propositions. So $h$ is proper. $\square$

**Remark 2.15.8.** The classical construction embeds the Hilbert scheme into the Grassmannian of locally free quotients of rank $r$ of $B$. The charts $X_\sigma$ are the intersections of the Hilbert scheme with the standard affine charts of the Grassmannian. The Grassmannian is projective, and this gives properness without the valuative criterion.

**Remark 2.15.9 (Formalization).** The theorem states the universal property in full instead of using the definition `IsHilbRep` of [IsHilbRep.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsHilbRep.lean#L11). In [HilbertSchemeFiniteFreeAlgebraAffineExists.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSchemeFiniteFreeAlgebraAffineExists.lean#L32) the proof chooses the facts that $X_\sigma$ is affine and locally of finite type and does not use them, and line 33 drops the compactness of the basic locus. Both facts are used again inside the Lemma on finiteness, which chooses its own basis of $B$. The Lemma on flat closure is in [ImportsAlt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsAlt.lean#L8), a file name that says nothing about it. The existence proof discards the uniqueness half of that Lemma, and the uniqueness proof proves it again for sheaves of ideals.
