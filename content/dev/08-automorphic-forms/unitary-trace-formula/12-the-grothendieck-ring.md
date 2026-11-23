---
title: The Grothendieck ring
decls:
  - PositivityTheory.Groth.groth_of_cls
  - PositivityTheory.Groth.groth_of_three
  - PositivityTheory.Groth.grothendieckRingPolynomial_of_seg
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Grothendieck ring

This section proves Zelevinsky's theorem that the Grothendieck ring of the finite length representations of the groups $\mathrm{GL}_n$ over a $p$-adic field is a polynomial ring on the segments, from the theorem on segment representations. The proof is in three layers. The first derives the polynomial ring from a list of properties of the Langlands classification by segments. The second derives that list from the segment representations, the irreducibility of products of unlinked segments, and three properties of embeddings into induced representations. The third supplies these inputs. The result is the one recorded in [the Grothendieck ring of GL(n)](/entry/grothendieck-ring-polynomial-outright/), and it is used in the step [every character](/step/every-character/) for the representations of $\mathrm{GL}_n$ at the split places. For the background, see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module) and [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments).

### Setting

Let $k$ be a nonarchimedean local field and $\nu = |\det|$ on each $\mathrm{GL}_d(k)$. All representations are smooth complex representations of the groups $\mathrm{GL}_n(k)$. For representations $\pi_1, \dots, \pi_h$ of $\mathrm{GL}_{n_1}(k), \dots, \mathrm{GL}_{n_h}(k)$, let $\pi_1 \times \dots \times \pi_h$ be the normalized parabolic induction of $\pi_1 \otimes \dots \otimes \pi_h$ from the standard block upper triangular parabolic subgroup.

**Definition 2.12.1 (Grothendieck group).** Let $\mathcal{R}(k)$ be the free abelian group on the pairs $(n, [\pi])$, where $n \ge 0$ and $[\pi]$ is an isomorphism class of irreducible representations of $\mathrm{GL}_n(k)$. A representation $\pi$ of finite length has a class $[\pi] \in \mathcal{R}(k)$, the sum of its irreducible subquotients with multiplicity. The unit $1$ is the class of the trivial representation of $\mathrm{GL}_0(k)$.

**Definition 2.12.2 (Segments).** A *segment* $\Delta$ is given by integers $d, l > 0$ and the class of an irreducible cuspidal representation $\sigma$ of $\mathrm{GL}_d(k)$. It stands for the sequence $\sigma, \sigma\nu, \dots, \sigma\nu^{l-1}$, and $l$ is its *length*. Two segments are *linked* if their union is a segment and neither contains the other. A segment $\Delta$ *precedes* $\Delta'$ if they are linked and $\Delta'$ starts at $\sigma\nu^j$ with $j > 0$, where $\Delta$ starts at $\sigma$. A *multisegment* is a finite multiset of segments; an *ordered form* of a multisegment is an enumeration $\Delta_1, \dots, \Delta_h$ in which $\Delta_i$ does not precede $\Delta_j$ for $i < j$.

**Definition 2.12.3 (Segment representations).** The *segment representation* statement says: for every irreducible cuspidal $\sigma$ of $\mathrm{GL}_d(k)$ and every $l > 0$, the representation $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$ has a unique irreducible subrepresentation $Z(\Delta)$, and the Jacquet module of $Z(\Delta)$ along the parabolic subgroup with $l$ blocks of size $d$ is $\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$. Here $\Delta$ is the segment of $\sigma$ of length $l$.

**Definition 2.12.4 (Polynomial Grothendieck ring).** The *polynomial ring* statement says: for every $k$ and every map $Z$ from segments to irreducible classes with the two properties of the segment representations, there is an isomorphism of abelian groups $\Psi : \mathcal{R}(k) \to \mathbb{Z}[X_\Delta]$, onto the polynomial ring with one variable for each segment, such that $\Psi(1) = 1$, $\Psi([\pi_1 \times \pi_2]) = \Psi([\pi_1])\, \Psi([\pi_2])$ whenever $\pi_1$, $\pi_2$ and $\pi_1 \times \pi_2$ have finite length, and $\Psi(Z(\Delta)) = X_\Delta$.

### The Langlands classification by segments

For a segment $\Delta$, an irreducible $\pi$ is $L(\Delta)$ if it is the unique irreducible quotient of $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$. For a multisegment $\mathfrak{m}$, an irreducible $\pi$ is $L(\mathfrak{m})$ if it is the unique irreducible quotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$ for some ordered form of $\mathfrak{m}$.

**Definition 2.12.5 (Classification data).** The *classification data* for $k$ are the following eight properties.

1. *Existence.* For every multisegment $\mathfrak{m}$ some irreducible representation is $L(\mathfrak{m})$.
2. *Exhaustion.* Every irreducible representation is $L(\mathfrak{m})$ for some $\mathfrak{m}$.
3. *Independence of the order.* If $\pi$ is $L(\mathfrak{m})$, then $\pi$ is the unique irreducible quotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$ for every ordered form of $\mathfrak{m}$.
4. *Socle.* If $\pi$ is $L(\mathfrak{m})$, then $\pi$ is the unique irreducible subrepresentation of $L(\Delta_h) \times \dots \times L(\Delta_1)$ for every ordered form.
5. *Jacquet modules of segments.* The Jacquet module of $L(\Delta)$ along a parabolic subgroup contains an irreducible $\tau_1 \otimes \dots \otimes \tau_s$ with multiplicity $1$ if the $\tau_i$ are the $L(\Gamma_i)$ for a cut of $\Delta$ into consecutive segments $\Gamma_1, \dots, \Gamma_s$ from the top, and with multiplicity $0$ otherwise.
6. *Segments exist.* For every segment some irreducible representation is $L(\Delta)$.
7. *Unlinked products.* If $\Delta_1, \dots, \Delta_h$ are pairwise unlinked, then $L(\Delta_1) \times \dots \times L(\Delta_h)$ is irreducible.
8. *Commutation.* If $\Delta$, $\Delta'$ are unlinked, then $L(\Delta) \times L(\Delta') \cong L(\Delta') \times L(\Delta)$.

**Theorem 2.12.6 (Polynomial ring from the classification).** Suppose that the classification data hold for every nonarchimedean local field $k$. Then the polynomial ring statement holds.

Lean: `PositivityTheory.Groth.groth_of_cls`

*Proof.* Fix $k$ and $Z$.

*Step 1: a ring.* Define a product on $\mathcal{R}(k)$ by $[\pi] \cdot [\pi'] = [\pi \times \pi']$ on irreducible classes, extended bilinearly. Parabolic induction is exact and the Jacquet functor is exact, so the class of $\pi_1 \times \pi_2$ depends only on the classes of $\pi_1$ and $\pi_2$, and the product of classes is the class of the product. Induction in stages gives associativity, the product is commutative since $\pi_1 \times \pi_2$ and $\pi_2 \times \pi_1$ have the same Jordan-Hölder factors, and $1$ is a unit. So $\mathcal{R}(k)$ is a commutative ring, and the class of $\pi_1 \times \dots \times \pi_h$ is the product of the classes.

*Step 2: the Langlands basis.* For a multisegment $\mathfrak{m}$ put $\mathrm{sq}(\mathfrak{m}) = \sum_{\Delta \in \mathfrak{m}} \mathrm{len}(\Delta)^2$. If $L(\mathfrak{n})$ is a subquotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$ for an ordered form of $\mathfrak{m}$, then $\mathfrak{m}$ and $\mathfrak{n}$ have the same cuspidal support, and $\mathfrak{n} = \mathfrak{m}$ or $\mathrm{sq}(\mathfrak{m}) < \mathrm{sq}(\mathfrak{n})$. The multiplicity of $L(\mathfrak{m})$ in this product is $1$. Both facts come from items 3 to 5 and the computation of Jacquet modules. So the classes of the products are related to the classes $[L(\mathfrak{m})]$ by a unitriangular matrix. By items 1 and 2 the classes $[L(\mathfrak{m})]$ are a basis of $\mathcal{R}(k)$. So the ring map $\Phi_L : \mathbb{Z}[X_\Delta] \to \mathcal{R}(k)$ with $X_\Delta \mapsto [L(\Delta)]$ is bijective.

*Step 3: from $L$ to $Z$.* For each segment $\Delta$ write $Z(\Delta) = \Phi_L(p_\Delta)$. Every monomial of $p_\Delta$ is a multisegment with the cuspidal support of $\Delta$. A Jacquet module count with item 5 and an alternating sum over the subsets of $\{1, \dots, l - 1\}$ shows that the coefficient of $X_\Delta$ in $p_\Delta$ is $(-1)^{l-1}$. The other monomials have the same support as $\Delta$ and at least two segments, so they involve only segments shorter than $\Delta$. A ring endomorphism $\psi$ of $\mathbb{Z}[X_\Delta]$ with $\psi(X_\Delta) = \pm X_\Delta + (\text{a polynomial in shorter variables})$ is bijective, by induction on the length. So $\Phi_Z = \Phi_L \circ \psi$, with $\psi(X_\Delta) = p_\Delta$, is a bijective ring map with $\Phi_Z(X_\Delta) = Z(\Delta)$. Put $\Psi = \Phi_Z^{-1}$. $\square$

For $\Delta = (1, \nu)$ in $\mathrm{GL}_2$, the class of $1 \times \nu$ is the sum of $Z(\Delta)$, a character, and $L(\Delta)$, a twist of the Steinberg representation. So $p_\Delta = X_{(1)} X_{(\nu)} - X_\Delta$, with the coefficient $(-1)^{2-1}$ at $X_\Delta$.

### From segment representations to the classification

For irreducible $x$ and a list $A$ of irreducible representations, say that $x$ *embeds in* $A$ if $x$ is a subrepresentation of the product of the list. Write $A \cdot M \cdot B$ for concatenation of lists.

**Definition 2.12.7 (Embedding properties).** The three *embedding properties* for $k$ are:

1. *Middle.* If $x$ embeds in $A \cdot M \cdot B$, then there is an irreducible subquotient $\sigma$ of the product of $M$ such that $x$ embeds in $A \cdot (\sigma) \cdot B$.
2. *Refinement.* If $\sigma$ embeds in $M$ and $x$ embeds in $A \cdot (\sigma) \cdot B$, then $x$ embeds in $A \cdot M \cdot B$.
3. *Swap.* If $a = L(\Delta)$ and $b = L(\Gamma)$ with $\Delta$, $\Gamma$ unlinked, and $x$ embeds in $A \cdot (a, b) \cdot B$, then $x$ embeds in $A \cdot (b, a) \cdot B$.

**Theorem 2.12.8 (Classification from three inputs).** Suppose that the segment representation statement holds, that for every $k$ the products of $L(\Delta_i)$ over pairwise unlinked segments are irreducible, and that for every $k$ the three embedding properties hold. Then the polynomial ring statement holds.

Lean: `PositivityTheory.Groth.groth_of_three`

*Proof.* By the previous Theorem it is enough to prove the classification data for each $k$. We use that every irreducible representation of $\mathrm{GL}_n(k)$ is admissible. Item 7 is a hypothesis, and item 8 follows from it: if $L(\Delta) \times L(\Delta')$ is irreducible, it is isomorphic to $L(\Delta') \times L(\Delta)$, since the two have the same Jordan-Hölder factors. Item 3 follows from item 8 and admissibility, because two ordered forms of a multisegment differ by swaps of unlinked neighbours. Item 4 follows from item 3 and the Langlands classification of the irreducible admissible representations. Item 5 follows from the segment representations by the computation of the Jacquet modules of segment products, and item 6 holds for every segment by admissibility. Item 1 follows from the segment representations and item 7, which give the unique irreducible quotient of each standard product. Item 2 is the main point. Every irreducible $x$ embeds in a product of cuspidal representations. Using the three embedding properties, one groups the cuspidal factors into segments and peels off one $L(\Delta)$ at a time, starting from a minimal segment. An induction on the degree then shows that $x$ is $L(\mathfrak{m})$ for a multisegment $\mathfrak{m}$. $\square$

### The inputs

**Theorem 2.12.9 (Polynomial ring from segment representations).** If the segment representation statement holds, then the polynomial ring statement holds.

Lean: `PositivityTheory.Groth.grothendieckRingPolynomial_of_seg`

*Proof.* Apply the previous Theorem. The irreducibility of unlinked products follows from the segment representations. The middle property holds because an irreducible representation is admissible and the product of $A \cdot M \cdot B$ is induced in stages from the product of $M$: an embedding of $x$ factors through a subquotient of the middle factor. The refinement property holds since parabolic induction is exact, so an embedding $\sigma \hookrightarrow \prod M$ induces an embedding of $A \times \sigma \times B$ into $A \times \prod M \times B$. The swap property follows from the commutation of unlinked $L(\Delta)$ and $L(\Gamma)$, item 8 above. $\square$

In Zelevinsky's paper the polynomial ring is proved first for the $Z(\Delta)$. Here the order is reversed: the polynomial ring on the $L(\Delta)$ comes from the Langlands classification, and the change of variables of Step 3 passes to the $Z(\Delta)$.

**Remark 2.12.10 (Formalization).** The Grothendieck group is the group of finitely supported integer functions on the pairs $(n, [\pi])$, and the product of Step 1 is defined on it in the proof; the polynomial ring statement asks only for an additive isomorphism with the product rule. Associativity, commutativity and the unit enter the proof as instances of `Fact` ([ClassGlEqClass.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/ClassGlEqClass.lean#L17)). The two algebraic lemmas of Steps 2 and 3, on unitriangular matrices and on triangular substitutions, are stated as propositions and proved separately, then passed to the main argument as hypotheses ([ProdList.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/ProdList.lean#L84)). The classification data are a structure with eight fields ([ProdList.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/ProdList.lean#L37)); item 8 is a field although it follows from item 7, and the proof derives it that way. The lemma on multiplicity one in Step 2 takes two hypotheses that it does not use ([MultOne.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/MultOne.lean#L150)). The derivation of the classification data from the three inputs is a separate result ([PeelGood.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/PeelGood.lean#L131)), which uses named results on admissibility, the Langlands classification, and Jacquet modules of segments; we did not unfold them. The three embedding properties are defined at [CuspEmbP.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/LanglandsExhaustion/CuspEmbP.lean#L24). The whole chain has a second copy with the same statements in another namespace, which is the one used by the outright theorem ([GrothendieckRingPolynomialOfSeg.lean](lean:CompanionTheory/AutomorphicTheory/ProductFormulaTheory/GrothendieckRingPolynomial/GrothendieckRingPolynomialOfSeg.lean#L8)).

## Notes and references

The chapter proves the unitary trace formula in the form that the comparison with the twisted trace formula of $\mathrm{GL}_n$ needs. On the spectral side it builds pseudo-coefficients of discrete series, isolates the elliptic part, and separates multiplicities with Iwahori traces. On the geometric side it computes the transfer at inert places through lattice counts and the unit lemma of [the Jacquet-Rallis chapter](/entry/unit-match-all/), the transfer at split places through constant terms, and the stabilized class sum of a definite unitary group through Hermitian forms. The last section gives Zelevinsky's polynomial ring theorem. All these results are used in the step [every character](/step/every-character/), and the matching at inert places also uses [the unit lemma](/entry/unit-lemma-lie-and-group/). The archimedean side of base change is in [the archimedean base change](/entry/archimedean-base-change-first/).

The simple trace formula with pseudo-coefficients follows Arthur and Clozel. The pseudo-coefficients at the real places come from the Paley-Wiener theorem of Clozel and Delorme. The comparison of a twisted trace formula with the trace formula of a unitary group follows Rogawski and Labesse. The descent of orbital integrals to a Levi subgroup is Harish-Chandra's. The trace formula of a definite unitary group as a finite sum over classes, with masses, is the setting of Gross's algebraic modular forms, and the masses are Tamagawa volumes in the sense of Kottwitz. The local-global principle for Hermitian forms over a CM field is Landherr's theorem. The polynomial ring theorem is Zelevinsky's, and the Jacquet module computations rest on the geometric lemma of Bernstein and Zelevinsky.

- J. Arthur and L. Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Annals of Math. Studies 120, Princeton University Press, 1989.
- J. Arthur, *The $L^2$-Lefschetz numbers of Hecke operators*, Invent. Math. 97 (1989), 257-290.
- L. Clozel and P. Delorme, *Le théorème de Paley-Wiener invariant pour les groupes de Lie réductifs*, Invent. Math. 77 (1984), 427-453.
- J. D. Rogawski, *Automorphic Representations of Unitary Groups in Three Variables*, Annals of Math. Studies 123, Princeton University Press, 1990.
- J.-P. Labesse, *Cohomologie, stabilisation et changement de base*, Astérisque 257 (1999).
- Harish-Chandra, *Harmonic Analysis on Reductive p-adic Groups*, notes by G. van Dijk, Lecture Notes in Math. 162, Springer, 1970.
- B. H. Gross, *Algebraic modular forms*, Israel J. Math. 113 (1999), 61-93.
- R. E. Kottwitz, *Tamagawa numbers*, Ann. of Math. 127 (1988), 629-646.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. École Norm. Sup. 10 (1977), 441-472.
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II. On irreducible representations of GL(n)*, Ann. Sci. École Norm. Sup. 13 (1980), 165-210.
