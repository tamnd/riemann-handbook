---
title: The Grothendieck ring of GL(n)
decls:
  - GlobalTheory.grothendieckRingPolynomial_outright
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Grothendieck ring of GL(n)

This section records one more result that the step [EveryCharacter](/step/every-character/) takes from this part of the development: Zelevinsky's theorem that the Grothendieck ring of finite length representations of the groups $\mathrm{GL}_n$ over a $p$-adic field is a polynomial ring on the segments. It has no relation to the fundamental lemma. It is the composition of two results proved in other chapters: the theorem on [segment representations](/entry/companion-theory-rg-gu-segment-representation/), and [the theorem that segment representations give a polynomial ring](/entry/companion-theory-groth-grothendieck-ring-polynomial-of-seg/). For the background, see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups) and [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments).

Let $k$ be a nonarchimedean local field and $\nu = |\det|$ on each $\mathrm{GL}_d(k)$. All representations are complex representations of the groups $\mathrm{GL}_n(k)$. For representations $\pi_1$ of $\mathrm{GL}_r(k)$ and $\pi_2$ of $\mathrm{GL}_t(k)$, let $\pi_1 \times \pi_2$ be the normalized parabolic induction of $\pi_1 \otimes \pi_2$ to $\mathrm{GL}_{r+t}(k)$ from the standard block upper triangular parabolic subgroup.

**Definition 4.8.1 (Grothendieck group).** Let $\mathcal{R}(k)$ be the free abelian group on the pairs $(n, [\pi])$, where $n \ge 0$ and $[\pi]$ is an isomorphism class of irreducible representations of $\mathrm{GL}_n(k)$. A representation $\pi$ of $\mathrm{GL}_n(k)$ of finite length has a class $[\pi] \in \mathcal{R}(k)$: the sum of its irreducible subquotients, with multiplicity, each placed in degree $n$. The *unit* $1 \in \mathcal{R}(k)$ is the class of the trivial representation of $\mathrm{GL}_0(k)$.

**Definition 4.8.2 (Segments).** A *segment* $\Delta$ is given by integers $d, l > 0$ and the class of an irreducible cuspidal representation $\sigma$ of $\mathrm{GL}_d(k)$. It stands for the sequence $\sigma, \sigma\nu, \dots, \sigma\nu^{l-1}$. A *segment class map* is a map $Z$ that assigns to each segment $\Delta$ an irreducible class of $\mathrm{GL}_{ld}(k)$, with the following property. For every segment $\Delta$, every representative $\sigma$ of its cuspidal class, and every irreducible $\pi$ of $\mathrm{GL}_{ld}(k)$:

1. $[\pi] = Z(\Delta)$ if and only if $\pi$ embeds in $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$;
2. $[\pi] = Z(\Delta)$ if and only if the Jacquet module of $\pi$ along the parabolic subgroup with $l$ blocks of size $d$ is isomorphic to $\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$.

So $Z(\Delta)$ is Zelevinsky's representation $\langle \Delta \rangle$: the unique irreducible subrepresentation of the induced representation of the segment.

**Theorem 4.8.3 (Polynomial Grothendieck ring).** Let $k$ be a nonarchimedean local field and $Z$ a segment class map. Then there is an isomorphism of abelian groups
$$\Psi : \mathcal{R}(k) \to \mathbb{Z}[X_\Delta : \Delta \text{ a segment}]$$
onto the polynomial ring in one variable $X_\Delta$ for each segment, such that:

1. $\Psi(1) = 1$;
2. $\Psi([\pi_1 \times \pi_2]) = \Psi([\pi_1])\, \Psi([\pi_2])$ for all smooth representations $\pi_1$, $\pi_2$ of finite length such that $\pi_1 \times \pi_2$ has finite length;
3. $\Psi(Z(\Delta)) = X_\Delta$ for every segment $\Delta$.

Lean: `GlobalTheory.grothendieckRingPolynomial_outright`.

*Proof.* By [the theorem on segment representations](/entry/companion-theory-rg-gu-segment-representation/), for every irreducible cuspidal $\sigma$ of $\mathrm{GL}_d(k)$ and every $l > 0$, the representation $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$ has a unique irreducible subrepresentation, and its Jacquet module is $\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$. By [the polynomial ring theorem](/entry/companion-theory-groth-grothendieck-ring-polynomial-of-seg/), this statement implies the Theorem. $\square$

The multiplication of item 2 makes $\mathcal{R}(k)$ a commutative ring, and the Theorem says that the classes $Z(\Delta)$ are free polynomial generators of it. In Zelevinsky's work the proof has two parts. First, the products $Z(\Delta_1) \times \dots \times Z(\Delta_m)$, with the segments in a standard order, have a unique irreducible subrepresentation, and every irreducible representation arises in this way from exactly one multiset of segments. Second, the class of the product is this irreducible class plus classes that are smaller for an order on multisets. So the products of the $Z(\Delta)$ are a basis of $\mathcal{R}(k)$, related to the basis of irreducible classes by a unitriangular matrix.

**Remark 4.8.4 (Formalization).** The theorem has nothing to do with the Jacquet-Rallis fundamental lemma; it sits in the same folder of the code only because the step EveryCharacter uses both. Its two users are proofs of the Zelevinsky polynomial ring statement, one for the spherical classification and one together with the geometric lemma ([IsSphericalIffUnrOfLawsT.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsSphericalIffUnrOfLawsT.lean#L66), [GeometricLemmaAndZelevinskyPolynomialRing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GeometricLemmaAndZelevinskyPolynomialRing.lean#L16)). The proof is one line ([GrothendieckRingPolynomialOutright.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GrothendieckRingPolynomialOutright.lean#L9)). The Grothendieck group is the group of finitely supported integer functions on the pairs $(n, [\pi])$, and the theorem gives only an additive isomorphism with the product rule; the ring structure on $\mathcal{R}(k)$ is not defined separately. Given the theorem on segment representations, the hypothesis on $Z$ fixes $Z(\Delta)$ uniquely, so the conclusion does not depend on a choice. A second copy of the polynomial ring theorem, with the same statement, is in another namespace ([GrothendieckRingPolynomialOfSeg.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/GrothendieckRingPolynomialOfSeg.lean#L8)).

## Notes and references

The chapter proves the Jacquet-Rallis fundamental lemma for the unit functions in every rank, and the unit lemma for counts of self-dual lattices, both in the Lie algebra form and in the group form. The unit lemma is used in the step [EveryCharacter](/step/every-character/). Its Lie algebra form also enters [the matching of principal congruence functions](/entry/match-principal-congruence-inert/) of the unitary trace formula in this volume. The last section gives Zelevinsky's polynomial ring theorem, which the same step uses for representations of $\mathrm{GL}_n$.

The fundamental lemma was conjectured by Jacquet and Rallis. Yun proved it for large residue characteristic by geometric methods, and Gordon's appendix passes to characteristic $0$. Beuzart-Plessis gave a local proof that works in all residue characteristics, and the proof here is of the same kind: an induction on the rank, with a Weil representation of $\mathrm{SL}_2$ on each side, and an argument with a monoid generated by $w$ and the unipotent elements. The step from the Weil representation to the Fourier transform uses W. Zhang's theorem that the transfer commutes with the Fourier transform up to a Weil constant. Here the Weil constant of the standard form is computed directly, and the rank one transfer is proved by truncated Whittaker integrals. Section 2 builds the Weil representation of $\mathrm{SL}_2$ for a quadratic space over an étale algebra from the field case, by an explicit presentation of $\mathrm{SL}_2$. Sections 6 and 7 translate the fundamental lemma into counts of lattices and deduce the unit lemma by a limit argument in a torus, with no use of the geometry of affine Springer fibers.

- H. Jacquet and S. Rallis, *On the Gross-Prasad conjecture for unitary groups*, in *On Certain L-functions*, Clay Math. Proc. 13 (2011).
- Z. Yun, *The fundamental lemma of Jacquet and Rallis*, Duke Math. J. 156 (2011), with an appendix by J. Gordon.
- R. Beuzart-Plessis, *A new proof of the Jacquet-Rallis fundamental lemma*, Duke Math. J. 170 (2021).
- W. Zhang, *Fourier transform and the global Gan-Gross-Prasad conjecture for unitary groups*, Ann. of Math. 180 (2014).
- A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964).
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II. On irreducible representations of GL(n)*, Ann. Sci. École Norm. Sup. 13 (1980), §7.
