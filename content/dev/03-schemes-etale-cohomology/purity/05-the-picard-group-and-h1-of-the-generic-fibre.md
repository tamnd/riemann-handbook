---
title: The Picard group and H^1 of the generic fibre
decls:
  - GlobalTheory.pic_localization_strictHenselisation_no_torsion
  - GlobalTheory.pic_generic_fibre_quotient_strictHenselisation_no_torsion
  - GlobalTheory.T.pic_generic_fibre_quotient_strictHenselisation_no_torsion_alt
  - GlobalTheory.LocAcycDegOne.picL
  - GlobalTheory.LocAcycDegOne.tateTwistCohomology_genericFibre_henselLine_subsingleton
  - GlobalTheory.T.subsingleton_ht_one_genericFibre_of_sh_etale_cover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Picard group and H^1 of the generic fibre

Let $T$ be an absolutely integrally closed local domain with fraction field $K$, and let $q$ be a unit in $T$. This section proves that $H^1(\operatorname{Spec}(K \otimes_T A), \mathbb{Z}/q(i)) = 0$ for every $i$, when $A$ is a strictly henselian $T[x]$-algebra that is a quotient of a strict henselisation of $T[x]$. By the Kummer sequence, $H^1$ with coefficients $\mu_q$ is built from the units modulo $q$-th powers and the $q$-torsion of the [[Picard group|3Z9DCWYXQZ]]. So the proof shows that both vanish. For the Picard group it uses [the theorem on cyclic torsors](/entry/torsor-trivial/) of the previous section. The result is the degree one case of the local acyclicity of the relative affine line over $T$, and two proofs of local acyclicity in the étale part of the Galois row use it, for the case $n = 1$.

We keep the notation of the previous section: $O_K$ is the generic fibre of a $T$-algebra $O$, and a ring is *strictly henselian* if it is a henselian local ring with separably closed residue field. We say that a $T[x]$-algebra $O$ is *ind-étale of local type* if it is the directed union of $T[x]$-subalgebras, each isomorphic to a localization $E_{\mathfrak{P}}$ of an étale $T[x]$-algebra $E$ at a prime $\mathfrak{P}$.

**Lemma 2.5.1 (Picard torsion from torsors).** Let $B$ be a ring and $q \geq 1$ a unit in $B$. Assume that there is $\zeta \in B$ with $\zeta^q = 1$ such that $1 - \zeta^k$ is a unit for $0 < k < q$. If every $\mathbb{Z}/q$-torsor over $B$ has a section, that is, a $B$-algebra map to $B$, then $\mathrm{Pic}(B)$ has no $q$-torsion.

Lean: `GlobalTheory.T.picard_torsion_trivial_of_torsors_have_sections` (also `GlobalTheory.KummerStep.kummer_step`).

*Proof.* Let $L$ be an invertible $B$-module with $L^{\otimes q} \cong B$. Choose a $q$-linear form $\phi : L \times \dots \times L \to B$ that comes from such an isomorphism; then for each prime $\mathfrak{p}$ there is $e \in L$ with $\phi(e, \dots, e) \notin \mathfrak{p}$. Let $D = \bigoplus_{k=0}^{q-1} L^{\otimes k}$, with the multiplication that uses $\phi$ to identify $L^{\otimes q}$ with $B$. Then $D$ is finite, projective and faithfully flat over $B$. Let the generator of $\mathbb{Z}/q$ act by $\zeta^k$ on $L^{\otimes k}$. Since $q$ and the $1 - \zeta^k$ are units, $D$ is a $\mathbb{Z}/q$-torsor. By assumption it has a section $s : D \to B$. Let $f = s|_L : L \to B$. Then $f(e)^q = \phi(e, \dots, e)$ for all $e \in L$. So the image of $f$ lies in no maximal ideal, and $f$ is surjective. A surjection between invertible modules is bijective, so $L \cong B$. $\square$

**Theorem 2.5.2 (Picard group of the generic fibre).** Let $T$ be an absolutely integrally closed local domain, and let $q \geq 1$ be a unit in $T$. Let $O$ be a strictly henselian $T[x]$-algebra that is ind-étale of local type. Then $\mathrm{Pic}(O_K)$ has no $q$-torsion.

Lean: `GlobalTheory.pic_localization_strictHenselisation_no_torsion`.

*Proof.* We take as given that $O$ is a strict henselisation of $T[x]_P$ for some prime $P$ of $T[x]$, in the sense of the previous section. The cyclotomic polynomial $\Phi_q$ has a root $\zeta \in T$, because $T$ is absolutely integrally closed. Since $q$ is a unit, $\zeta^q = 1$ and $1 - \zeta^k$ is a unit for $0 < k < q$. The images of $q$ and $\zeta$ in $O_K$ have the same properties. By [the theorem on cyclic torsors](/entry/torsor-trivial/), $\mathbb{Z}/q$-torsors over $O_K$ are trivial. The lemma on Picard torsion now applies to $B = O_K$. $\square$

Lean: `GlobalTheory.exists_pow_eq_one_isUnit_one_sub_pow` (also `GlobalTheory.StrictHensUnion.isStrictHenselisation_of_directed_union`).

**Theorem 2.5.3 (Picard group of a quotient).** Let $T$, $q$ and $O$ be as in the previous theorem, and let $\pi : O \to A$ be a surjective map of $T[x]$-algebras. Then $\mathrm{Pic}(K \otimes_T A)$ has no $q$-torsion.

Lean: `GlobalTheory.pic_generic_fibre_quotient_strictHenselisation_no_torsion` (also `GlobalTheory.T.pic_generic_fibre_quotient_strictHenselisation_no_torsion_alt`, the same statement).

*Proof.* The ring $T$ is integrally closed, since every monic polynomial over $T$ of positive degree has a root in $T$. We take as given that an ind-étale algebra of local type over the normal domain $T[x]$ is a normal domain, so $O$ is a domain. There are two cases.

If $\ker \pi = 0$, then $\pi$ is an isomorphism, and $K \otimes_T A \cong K \otimes_T O = O_K$. The previous theorem applies.

If $\ker \pi \neq 0$, we show that every prime of $K \otimes_T A$ is maximal. Let $Q \subseteq Q'$ be primes of $K \otimes_T A$, and let $\mathfrak{p} \subseteq \mathfrak{p}'$ be their inverse images in $O$. Both contain $\ker \pi \neq 0$ and both meet $T$ only in $0$. Let $P \subseteq P'$ be their inverse images in $T[x]$. Then $P \neq 0$, since $O$ is a domain that is ind-étale over $T[x]$, and $P' \cap T = 0$. Localize at $T \setminus \{0\}$: in $K[x]$ the nonzero prime $P K[x]$ is maximal, so $P = P'$. An ind-étale map has no inclusions between distinct primes over the same prime, so $\mathfrak{p} = \mathfrak{p}'$ and $Q = Q'$. We take as given two facts: an ind-étale map has no inclusions between distinct primes over the same prime (incomparability), and a ring in which every prime is maximal has trivial Picard group. So $\mathrm{Pic}(K \otimes_T A)$ is trivial, and the hypothesis on $q$ is not used in this case. $\square$

The next lemma says that the algebras of the main theorem are such quotients.

**Lemma 2.5.4 (Strictly henselian algebras as quotients).** Let $T$ be a ring and $A$ a strictly henselian $T[x]$-algebra in which every element lies in the image of some étale $T[x]$-algebra. Then there are a strictly henselian $T[x]$-algebra $O$ that is ind-étale of local type and a surjective map $O \to A$ of $T[x]$-algebras.

Lean: `GlobalTheory.T.surj_of_strictHenselisation_polynomial_alt`.

We take this lemma as given.

**Corollary 2.5.5 (Picard group of the generic fibre of A).** Let $T$ be an absolutely integrally closed local domain, $q \geq 1$ a unit in $T$, and $A$ as in the last lemma. Then $\mathrm{Pic}(K \otimes_T A)$ has no $q$-torsion.

Lean: `GlobalTheory.LocAcycDegOne.picL`.

*Proof.* This is the theorem on quotients, applied to the surjection $O \to A$ of the last lemma. $\square$

**Lemma 2.5.6 (Units of the generic fibre).** Under the hypotheses of the corollary, every unit of $K \otimes_T A$ is a $q$-th power.

Lean: `GlobalTheory.LocAcycDegOne.unitsL` (also `GlobalTheory.T.henselian_directed_union_subalgebras` and `GlobalTheory.QUnits.tensorFractionRing_units_pow_surj`, the form for a surjection $O \to A$ as in the theorem on quotients).

*Proof.* Write $A$ as a quotient of $O$ by the last lemma. If the kernel is zero, we take as given that every unit of $O_K$ has a $q$-th root. Otherwise $K \otimes_T A$ has dimension zero, as in the proof of the theorem on quotients. Also, each of its elements is congruent to an element $c/d$ of $K$ modulo each maximal ideal. Since $K$ is algebraically closed, a unit $u$ has a $q$-th root modulo each maximal ideal: take a root $r \in T$ of $X^q - c d^{q-1}$ and the class of $r/d$. We take as given that in a ring of dimension zero in which $q$ is a unit, $q$-th roots of a unit modulo each maximal ideal lift to a $q$-th root of the unit. This gives a $q$-th root of $u$. $\square$

**Lemma 2.5.7 (Kummer criterion).** Let $B$ be a ring and $q \geq 1$ a unit in $B$. If every unit of $B$ is a $q$-th power and $\mathrm{Pic}(B)$ has no $q$-torsion, then $H^1(\mathrm{sp}(B), \mathbb{Z}/q(1)) = 0$.

Lean: `GlobalTheory.T.kummer_etale_vanishing` (also `GlobalTheory.EtC.kummer_vanishing`).

*Proof.* Let $x$ be a class of degree $1$. It dies on an étale cover, and this cover can be refined to one étale, faithfully flat $B$-algebra $C$. By the Čech description of classes that die on $C$, $x$ comes from a $1$-cocycle $u$ with values in the $q$-th roots of unity of $C \otimes_B C$. As a cocycle of units, $u$ defines by descent an invertible $B$-module, whose $q$-th power is trivial because $u^q = 1$. By assumption this module is trivial, so $u = w_1 / w_2$ for a unit $w$ of $C$, where $w_1, w_2$ are its images under the two maps $C \to C \otimes_B C$. Then $w^q$ descends to a unit $a$ of $B$. By assumption $a = v^q$ for a unit $v$ of $B$. Then $w v^{-1}$ is a $q$-th root of unity in $C$, and its coboundary $(w v^{-1})_1 / (w v^{-1})_2 = w_1 / w_2$ is $u$. So $x = 0$. $\square$

This is the argument behind $H^1(X_{\mathrm{et}}, \mu_q)$ as an extension of $\mathrm{Pic}(X)[q]$ by $\Gamma(X, \mathcal{O}_X)^\times / q$, with Hilbert's Theorem 90 in the form $H^1(X_{\mathrm{et}}, \mathbb{G}_m) = \mathrm{Pic}(X)$; see Milne, *Étale Cohomology*, Chapter III, Proposition 4.9.

**Lemma 2.5.8 (Twists are isomorphic).** Let $q \geq 1$ and let $B$ be a ring in which $q$ is a unit and $\Phi_q$ has a root. Then $H^n(\mathrm{sp}(B), \mathbb{Z}/q(i)) \cong H^n(\mathrm{sp}(B), \mathbb{Z}/q(j))$ for all $n, i, j$.

Lean: `GlobalTheory.T.tateTwistCohomology_spec_twist_independent` (also `GlobalTheory.EtC.untwist`).

We take this lemma as given. A root $\zeta$ of $\Phi_q$ is a primitive $q$-th root of unity, since $q$ is a unit, and it gives an isomorphism $\mathbb{Z}/q(i) \cong \mathbb{Z}/q(j)$ of coefficients on $\mathrm{sp}(B)$.

**Theorem 2.5.9 ($H^1$ of the generic fibre).** Let $T$ be an absolutely integrally closed local domain with fraction field $K$, and let $q \geq 1$ be a unit in $T$. Let $A$ be a strictly henselian $T[x]$-algebra in which every element lies in the image of some étale $T[x]$-algebra. Then for every $i \in \mathbb{Z}$,
$$
H^1(\mathrm{sp}(K \otimes_T A), \mathbb{Z}/q(i)) = 0.
$$

Lean: `GlobalTheory.LocAcycDegOne.tateTwistCohomology_genericFibre_henselLine_subsingleton` (also `GlobalTheory.T.subsingleton_ht_one_genericFibre_of_sh_etale_cover`, the same statement).

*Proof.* Let $B = K \otimes_T A$. Then $q$ is a unit in $B$. The polynomial $\Phi_q$ has a root in $T$, since $T$ is absolutely integrally closed, and so it has a root in $B$. By the lemma on twists, it is enough to treat $i = 1$. By the lemma on units and the corollary on the Picard group, every unit of $B$ is a $q$-th power and $\mathrm{Pic}(B)$ has no $q$-torsion. The Kummer criterion gives $H^1(\mathrm{sp}(B), \mathbb{Z}/q(1)) = 0$. $\square$

**Remark 2.5.10.** Here $\mathrm{sp}(B)$ is the constant space of $\operatorname{Spec} B$, so $H^1$ is the cohomology of the first section of this chapter. The theorem is the case $n = 1$ of local acyclicity for the relative affine line over $T$.

**Remark 2.5.11 (Formalization).** The statement of the theorem on the Picard group of the generic fibre asks for $T$ to be a domain twice, once as a standing assumption and once together with absolute integral closure, and it asks for $0 < q$ separately, which follows from $q$ being a unit in a nonzero ring. In its hypothesis of ind-étale type the prime of $E$ has the bound name `q`: [PicLocalizationStrictHenselisationNoTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicLocalizationStrictHenselisationNoTorsion.lean#L12). The case $\ker \pi \neq 0$ of the theorem on quotients is at [PicGenericFibreQuotientStrictHenselisationNoTors.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicGenericFibreQuotientStrictHenselisationNoTors.lean#L92). For the incomparability lemma, the lemma on rings of dimension zero, the lemma on strictly henselian algebras as quotients and the lemma on twists, we read the statements, not the proofs. For the theorem on quotients and for the main theorem, the two names have the same statement, and one of the two proofs tries the other name in three ways, with the heartbeat limit raised to $10^6$.
