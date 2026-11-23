---
title: The Grothendieck ring of GL(n)
decls:
  - CompanionTheory.Groth.groth_of_cls
  - CompanionTheory.Groth.groth_of_three
  - CompanionTheory.Groth.grothendieckRingPolynomial_of_seg
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Grothendieck ring of GL(n)

This section proves Zelevinsky's theorem that the Grothendieck group of the smooth representations of finite length of all $\mathrm{GL}_n(k)$, with the product given by parabolic induction, is a polynomial ring over $\mathbb{Z}$ with one variable for each segment. The only representation-theoretic hypothesis is the theorem on segment representations. The proof has three layers. The first gets the polynomial ring from the Langlands classification by segments. The second gets that classification from the segment representations and three properties of embeddings. The third proves these properties. The Jacquet module counts use the geometric lemma of Section 16. The result is the [Theorem 4.8.3 of Volume 8](/entry/grothendieck-ring-polynomial-outright/) on the Grothendieck ring, which the step [EveryCharacter](/step/every-character/) uses at the split places. For background see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

Let $k$ be a nonarchimedean local field and $\nu = |\det|$ on every $\mathrm{GL}_d(k)$. All representations are smooth complex representations. For representations $\pi_1, \dots, \pi_h$ of $\mathrm{GL}_{n_1}(k), \dots, \mathrm{GL}_{n_h}(k)$ let $\pi_1 \times \dots \times \pi_h$ be the normalized induction $i_e(\pi_1 \otimes \dots \otimes \pi_h)$ of Section 16, for the bijection $e$ that puts the blocks in their order. Let $\mathrm{Irr}$ be the set of pairs $(n, [\pi])$ with $n \geq 0$ and $[\pi]$ an isomorphism class of irreducible smooth representations of $\mathrm{GL}_n(k)$.

**Definition 1.21.1 (Grothendieck group).** Let $\mathcal{R}(k)$ be the free abelian group on $\mathrm{Irr}$. A representation $\pi$ of $\mathrm{GL}_n(k)$ of finite length has a class $[\pi] \in \mathcal{R}(k)$, the sum of its irreducible subquotients with their multiplicities. Let $1 \in \mathcal{R}(k)$ be the class of the trivial representation of $\mathrm{GL}_0(k)$.

**Definition 1.21.2 (Segments).** A *segment* $\Delta$ consists of integers $d, l > 0$ and the class of an irreducible cuspidal representation $\sigma$ of $\mathrm{GL}_d(k)$. Its *terms* are $\sigma, \sigma\nu, \dots, \sigma\nu^{l-1}$, and $l$ is its *length*. Two segments are *linked* if the union of their sets of terms is the set of terms of a segment and neither set contains the other. A segment $\Delta$ *precedes* $\Delta'$ if they are linked and $\Delta'$ starts at $\sigma\nu^j$ with $j > 0$, where $\sigma$ is the start of $\Delta$. An *ordered form* of a finite multiset $\mathfrak{m}$ of segments is an enumeration $\Delta_1, \dots, \Delta_h$ of $\mathfrak{m}$ such that $\Delta_i$ does not precede $\Delta_j$ for $i < j$.

**Definition 1.21.3 (Segment class).** A *segment class* is a map $Z$ that sends each segment $\Delta$, with data $(d, l, \sigma)$, to an element of $\mathrm{Irr}$ of degree $ld$, with the following property. For every representative $\sigma$, every bijection $e$ from $l$ blocks of size $d$ onto $\{1, \dots, ld\}$, and every irreducible $\pi$ of $\mathrm{GL}_{ld}(k)$, these are equivalent: $[\pi] = Z(\Delta)$; $\pi$ embeds in $i_e(\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1})$; $r_e(\pi) \cong \sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$.

**Definition 1.21.4 (Segment property).** The *segment property* says the following. Let $\sigma$ be an irreducible cuspidal representation of $\mathrm{GL}_d(k)$ and $l > 0$. Then $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$ has exactly one irreducible subrepresentation $S$, and the Jacquet module of $S$ for the parabolic subgroup with $l$ blocks of size $d$ is isomorphic to $\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$.

This holds for every $k$ by Zelevinsky (1980), Sections 2 and 3. In this section it is a hypothesis.

**Definition 1.21.5 (Polynomial ring property).** The *polynomial ring property* says: for every $k$ and every segment class $Z$ there is an isomorphism of abelian groups $\Psi : \mathcal{R}(k) \to \mathbb{Z}[X_\Delta]$, onto the polynomial ring with one variable for each segment, such that $\Psi(1) = 1$, $\Psi(Z(\Delta)) = X_\Delta$ for every $\Delta$, and $\Psi([\pi_1 \times \pi_2]) = \Psi([\pi_1])\,\Psi([\pi_2])$ for all smooth $\pi_1$, $\pi_2$ of finite length such that $\pi_1 \times \pi_2$ has finite length.

### The Langlands classification by segments

An irreducible $\pi$ is $L(\Delta)$ if it is the unique irreducible quotient of $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$. It is $L(\mathfrak{m})$ if it is the unique irreducible quotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$ for some ordered form of $\mathfrak{m}$.

**Definition 1.21.6 (Classification data).** The *classification data* for $k$ are the following properties.
1. (Existence.) For every multiset $\mathfrak{m}$ of segments some irreducible $\pi$ is $L(\mathfrak{m})$.
2. (Exhaustion.) Every irreducible $\pi$ is $L(\mathfrak{m})$ for some $\mathfrak{m}$.
3. (Order.) If $\pi$ is $L(\mathfrak{m})$, then $\pi$ is the unique irreducible quotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$ for every ordered form of $\mathfrak{m}$.
4. (Socle.) If $\pi$ is $L(\mathfrak{m})$, then $\pi$ is the unique irreducible subrepresentation of $L(\Delta_h) \times \dots \times L(\Delta_1)$ for every ordered form.
5. (Jacquet modules.) Let $\pi$ be $L(\Delta)$ and $\tau_1, \dots, \tau_s$ irreducible of positive degrees. The multiplicity of $\tau_1 \otimes \dots \otimes \tau_s$ in the Jacquet module of $\pi$ for the blocks of these degrees is $1$ if $\tau_a = L(\Gamma_a)$ for a cut of $\Delta$ into consecutive segments $\Gamma_1, \dots, \Gamma_s$ with $\Gamma_1$ on top, and $0$ otherwise.
6. (Segments.) For every segment $\Delta$ some irreducible $\pi$ is $L(\Delta)$.
7. (Unlinked products.) If $\Delta_1, \dots, \Delta_h$ are pairwise not linked, then $L(\Delta_1) \times \dots \times L(\Delta_h)$ is irreducible.
8. (Commutation.) If $\Delta$ and $\Delta'$ are not linked, then $L(\Delta) \times L(\Delta') \cong L(\Delta') \times L(\Delta)$.

The proof uses the following inputs.

**Theorem 1.21.7 (Inputs on products).**
1. (Admissibility.) Every irreducible smooth representation of $\mathrm{GL}_n(k)$ is admissible.
2. (Finite length.) If $\pi_1$ and $\pi_2$ are smooth of finite length, then $\pi_1 \times \pi_2$ is of finite length. Parabolic induction and the Jacquet module are exact.
3. (Contragredient.) For irreducible $\pi$ of $\mathrm{GL}_n(k)$, the composition of $\pi$ with $g \mapsto w\,{}^tg^{-1}w^{-1}$, for the antidiagonal $w$, is isomorphic to the contragredient of $\pi$.
4. (Segment representations.) For every segment $\Delta$ some irreducible $\pi$ is $L(\Delta)$. If the segment property holds, item 5 of the classification data holds and the product of the $L(\Delta_i)$ over pairwise unlinked segments is irreducible.

Item 1 is Bernstein (1974). Item 2 is Bernstein and Zelevinsky (1977), Section 2. Item 3 is the theorem of Gelfand and Kazhdan, Bernstein and Zelevinsky (1976), Section 7. Item 4 is Zelevinsky (1980), Sections 3 and 4, and Section 9 for the representations $L(\Delta)$.

Lean: `GlobalTheory.T.irreducible_smooth_admissible_GL` (also `GlobalTheory.T.parabolicProduct_hasFiniteLength_GL`, `GlobalTheory.T.product_irreducible_finite_length`, `GlobalTheory.T.gelfand_kazhdan_contragredient`, `GlobalTheory.T.exists_segment_representation`, `GlobalTheory.T.segment_jacquet_all`, `CompanionTheory.Exh.lUnlinkedIrr_of_seg`).

**Theorem 1.21.8 (Polynomial ring from the classification).** Suppose that the classification data hold for every nonarchimedean local field $k$. Then the polynomial ring property holds.

Lean: `CompanionTheory.Groth.groth_of_cls`.

*Proof.* Fix $k$ and a segment class $Z$.

Step 1: the ring. For $x, y \in \mathrm{Irr}$ put $x \cdot y = [x \times y]$, and extend bilinearly. By input 2 the class of $\pi_1 \times \pi_2$ depends only on the classes of $\pi_1$ and $\pi_2$, and it is their product. Induction in stages gives associativity. The product is commutative, because $x \times y$ and $y \times x$ have the same irreducible subquotients by input 3. The class $1$ is a unit. So $\mathcal{R}(k)$ is a commutative ring, and the class of $\pi_1 \times \dots \times \pi_h$ is the product of the classes.

Step 2: the Langlands basis. For a multiset $\mathfrak{m}$ put $\mathrm{sq}(\mathfrak{m}) = \sum_{\Delta \in \mathfrak{m}} \mathrm{len}(\Delta)^2$. Let $\Delta_1, \dots, \Delta_h$ be an ordered form of $\mathfrak{m}$. If $L(\mathfrak{n})$ is a subquotient of $L(\Delta_1) \times \dots \times L(\Delta_h)$, then $\mathfrak{m}$ and $\mathfrak{n}$ have the same terms with multiplicity, and $\mathfrak{n} = \mathfrak{m}$ or $\mathrm{sq}(\mathfrak{m}) < \mathrm{sq}(\mathfrak{n})$. The multiplicity of $L(\mathfrak{m})$ in this product is $1$. Both facts follow from items 3 to 5 of the classification data and the geometric lemma. By items 1 and 2, the classes $[L(\mathfrak{m})]$ form a basis of $\mathcal{R}(k)$. A unitriangular matrix over a well-founded order is invertible. So the ring map $\Phi_L : \mathbb{Z}[X_\Delta] \to \mathcal{R}(k)$ with $X_\Delta \mapsto [L(\Delta)]$ is bijective.

Step 3: a functional for each segment. For a segment $\Delta$ of length $l$ and $\pi$ of finite length, let $\ell_\Delta([\pi])$ be the alternating sum, over the subsets $S$ of $\{1, \dots, l-1\}$, of $(-1)^{|S|}$ times the multiplicity in the Jacquet module of $\pi$ of the tensor product of the terms of $\Delta$ in the order given by $S$. The terms in $S$ come first in decreasing order, then the other terms in increasing order. By the exactness of the Jacquet module, $\ell_\Delta$ is additive. For a product $L(\Gamma_1) \times \dots \times L(\Gamma_h)$ the geometric lemma and item 5 express the multiplicities as counts of shuffles. A combinatorial identity then gives $\ell_\Delta(\Phi_L(p)) = (-1)^{l-1} c_\Delta(p)$, where $c_\Delta(p)$ is the coefficient of $X_\Delta$ in $p$. For $Z(\Delta)$, the definition of a segment class gives multiplicity $1$ for $S = \emptyset$ and $0$ for the other $S$, so $\ell_\Delta(Z(\Delta)) = 1$.

Step 4: the change of variables. Write $Z(\Delta) = \Phi_L(p_\Delta)$. By Step 3 the coefficient of $X_\Delta$ in $p_\Delta$ is $(-1)^{l-1}$. Every other monomial of $p_\Delta$ is a multiset with the terms of $\Delta$ and at least two segments, so it uses only segments shorter than $\Delta$. A ring endomorphism $\psi$ of $\mathbb{Z}[X_\Delta]$ with $\psi(X_\Delta) = \pm X_\Delta$ plus a polynomial in shorter variables is bijective, by induction on the length. Put $\psi(X_\Delta) = p_\Delta$. Then $\Phi_Z = \Phi_L \circ \psi$ is a bijective ring map with $\Phi_Z(X_\Delta) = Z(\Delta)$, and $\Psi = \Phi_Z^{-1}$ has the three properties by Step 1. $\square$

For the segment $\Delta = (1, \nu)$ of $\mathrm{GL}_2(k)$, the class of $1 \times \nu$ is the sum of the character $Z(\Delta)$ and a twist $L(\Delta)$ of the Steinberg representation. So $p_\Delta = X_{(1)} X_{(\nu)} - X_\Delta$, with the coefficient $(-1)^{2-1}$ at $X_\Delta$.

### From segments to the classification

For irreducible $x$ and a list $A$ of irreducible representations, say that $x$ *embeds in* $A$ if $x$ is isomorphic to a subrepresentation of the product of the list. Write $A \cdot M \cdot B$ for the concatenation of lists.

**Definition 1.21.9 (Embedding properties).** The three *embedding properties* for $k$ are as follows.
1. (Middle.) If $x$ embeds in $A \cdot M \cdot B$, then some irreducible subquotient $\sigma$ of the product of $M$ has the property that $x$ embeds in $A \cdot (\sigma) \cdot B$.
2. (Refinement.) If $\sigma$ embeds in $M$ and $x$ embeds in $A \cdot (\sigma) \cdot B$, then $x$ embeds in $A \cdot M \cdot B$.
3. (Swap.) If $a = L(\Delta)$ and $b = L(\Gamma)$ with $\Delta$ and $\Gamma$ not linked, and $x$ embeds in $A \cdot (a, b) \cdot B$, then $x$ embeds in $A \cdot (b, a) \cdot B$.

**Theorem 1.21.10 (Classification from three inputs).** Suppose that the segment property holds. Suppose that for every $k$ the products of the $L(\Delta_i)$ over pairwise unlinked segments are irreducible, and that for every $k$ the three embedding properties hold. Then the polynomial ring property holds.

Lean: `CompanionTheory.Groth.groth_of_three`.

*Proof.* By the previous theorem it suffices to prove the classification data for each $k$. Item 7 is a hypothesis. Item 8 follows from item 7: if $L(\Delta) \times L(\Delta')$ is irreducible, it has the same subquotients as $L(\Delta') \times L(\Delta)$ by input 3, so the two are isomorphic. Item 3 follows from item 8 and input 1, because two ordered forms of a multiset differ by swaps of unlinked neighbours. Item 4 follows from item 3 and input 3, which turns quotients into subrepresentations and reverses the order of the factors. Items 5 and 6 are input 4. Item 1 follows from the segment property and item 7, which give the unique irreducible quotient of each standard product. Item 2 needs more work. Every irreducible $x$ embeds in a product of cuspidal representations, by the refinement property. With the three embedding properties one groups the cuspidal factors into segments and takes off one $L(\Delta)$ at a time, from a minimal segment. Induction on the degree then shows that $x$ is $L(\mathfrak{m})$ for some $\mathfrak{m}$. $\square$

**Theorem 1.21.11 (Polynomial ring from segments).** If the segment property holds, then the polynomial ring property holds.

Lean: `CompanionTheory.Groth.grothendieckRingPolynomial_of_seg`.

*Proof.* Apply the previous theorem. The irreducibility of unlinked products is input 4. The middle property holds because $x$ is admissible by input 1, and the product of $A \cdot M \cdot B$ is induced in stages from the product of $M$, so an embedding of $x$ factors through an irreducible subquotient of the middle factor. The refinement property holds because parabolic induction is exact, so an embedding of $\sigma$ into the product of $M$ induces an embedding of $A \times \sigma \times B$ into the product of $A \cdot M \cdot B$. The swap property follows from item 8, which holds by input 4 and the argument of the previous proof. $\square$

### Classical form

In Zelevinsky (1980), Section 7, the ring $\mathcal{R} = \bigoplus_n \mathcal{R}_n$ is shown to be the polynomial ring in the classes $\langle \Delta \rangle$, and these are the $Z(\Delta)$ above. The representations $L(\Delta)$ are his $\langle \Delta \rangle^t$, the essentially square-integrable representations of Bernstein and Zelevinsky. Zelevinsky proves the polynomial ring for the $Z(\Delta)$ first. Here the order is reversed: the polynomial ring in the $L(\Delta)$ comes from the Langlands classification, and Step 4 changes the variables.

**Remark 1.21.12 (Formalization).** The three theorems are in [GrothOfCls.lean](lean:CompanionTheory/AutomorphicTheory/ProductFormulaTheory/GrothendieckRingPolynomial/GrothOfCls.lean#L16), [GrothOfThree.lean](lean:CompanionTheory/AutomorphicTheory/ProductFormulaTheory/GrothendieckRingPolynomial/GrothOfThree.lean#L7) and [GrothendieckRingPolynomialOfSeg.lean](lean:CompanionTheory/AutomorphicTheory/ProductFormulaTheory/GrothendieckRingPolynomial/GrothendieckRingPolynomialOfSeg.lean#L8), under a ProductFormulaTheory path. A second copy of the whole chain, with the same statements, is in the namespace `PositivityTheory.Groth` under Development/WeilBound, and the embedding properties also have two copies, `CompanionTheory.Exh` and `PositivityTheory.Exh`. The segment property and the polynomial ring property are `GlobalTheory.Published.SegmentRepresentation` and `GlobalTheory.Published.GrothendieckRingPolynomial`; the latter quantifies the product rule over a proof that $\pi_1 \times \pi_2$ has finite length. The product of Step 1 is built in the proof as `mulR`; associativity, commutativity and the unit enter as `Fact` instances. The classification data are the structure `Cls` with eight fields, and item 8 is a field although the proof derives it from item 7 (`comm_of`). The irreducibility of unlinked products is defined twice with the same body, as `Zc.Cos.LUnlinkedIrr` and `GlobalTheory.BZSeg.LUnlinkedIrr`, and `grothendieckRingPolynomial_of_seg` passes one for the other by unfolding. The lemma `multOne` takes two hypotheses that it does not use. The algebraic lemmas of Steps 2 and 4 are the propositions `UniTri` and `TriAut`, proved separately and passed as hypotheses to `groth_of_steps`. We did not unfold `IsSocle`, `IsCosocle`, `jhMult` or `multiProd`, and we read the statements of the inputs, not their proofs.
