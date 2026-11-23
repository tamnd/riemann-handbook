---
title: Segments and generic representations
decls:
  - PositivityTheory.RgGu.NR.redClC
  - PositivityTheory.RgGu.NR.rhoNuRhoReducibleC
  - PositivityTheory.RgGu.segmentRepresentation
  - GlobalTheory.RgGu.genericUnique
  - GlobalTheory.RgGu.genericUnique_of
  - GlobalTheory.RgGu.genericUnlinkedGL_of_segRep2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Segments and generic representations

This section proves three facts of the Bernstein and Zelevinsky theory for $\mathrm{GL}_N$ over a nonarchimedean local field. First, for a [[cuspidal representation|9AZ164C298]] $\rho$, the product $\rho \times \rho\nu$ is reducible. Second, the product along a segment $\rho, \rho\nu, \dots, \rho\nu^{l-1}$ has a unique irreducible subrepresentation, with the expected Jacquet module. Third, an irreducible generic representation is determined by its cuspidal support, and it is a product of essentially square-integrable segment representations with pairwise unlinked segments. These facts describe the generic representations to which the [exponent bound](/entry/exp-bound/) applies, and with [Bernstein's theorem](/entry/bern-at/) they give the form of the generic unitary local components used in step [EveryCharacter](/step/every-character/).

Background: [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments), [generic representations](/learn/representations/#generic-representations-and-local-factors), [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Notation

Let $k$ be a nonarchimedean local field and $\nu = |\det|$. For irreducible smooth representations $x_1, \dots, x_h$ of $\mathrm{GL}_{d_1}(k), \dots, \mathrm{GL}_{d_h}(k)$, let $x_1 \times \dots \times x_h$ be the normalized parabolic induction from the standard parabolic subgroup of type $(d_1, \dots, d_h)$. For $s \in \mathbb{C}$ write $x\nu^s$ for the twist of $x$ by $\nu^s$. Let $r_{(d_1, \dots, d_h)}$ be the normalized Jacquet functor to the Levi subgroup $\mathrm{GL}_{d_1}(k) \times \dots \times \mathrm{GL}_{d_h}(k)$.

A *segment* is a list $\Delta = (\rho, \rho\nu, \dots, \rho\nu^{l-1})$ with $\rho$ irreducible cuspidal and $l \ge 1$. Two segments are *linked* if their union is a segment and neither contains the other. Every irreducible smooth $\pi$ of $\mathrm{GL}_N(k)$ is a subquotient of a product $\rho_1 \times \dots \times \rho_h$ of cuspidal representations. The multiset $\{\rho_1, \dots, \rho_h\}$ is unique, and it is the *cuspidal support* of $\pi$. For a segment $\Delta$, let $L(\Delta)$ be the unique irreducible quotient of $\rho \times \rho\nu \times \dots \times \rho\nu^{l-1}$. It is essentially square-integrable.

### Reducibility at $\nu$

**Theorem 7.8.1 (Reducibility at $\nu$).** Let $y$ be an irreducible cuspidal representation of $\mathrm{GL}_d(k)$, $d \ge 1$. Then $y \times y\nu$ is reducible.

Lean: `PositivityTheory.RgGu.NR.redClC` (also `PositivityTheory.RgGu.NR.rhoNuRhoReducibleC`).

The proof uses two inputs.

**Proposition 7.8.2 (Some reducibility).** Let $\rho$ be an irreducible unitarisable cuspidal representation of $\mathrm{GL}_d(k)$. Then there is $s \ge 0$ such that $\rho\nu^{-s} \times \rho\nu^{s}$ is reducible.

*Proof.* Assume that $\pi_s = \rho\nu^{-s} \times \rho\nu^{s}$ is irreducible for all $s \ge 0$. Realize all $\pi_s$ on one space, the induced space of $\rho \otimes \rho$ restricted to a maximal compact subgroup. On a fixed compact open subgroup $K_0$ the action does not depend on $s$, and each matrix entry is a finite sum of exponentials in $s$. The representation $\pi_0$ is unitarisable, since $\rho \otimes \rho$ is unitary. Each $\pi_s$ has a nonzero invariant Hermitian form: $\rho$ is unitary, so its complex conjugate is its contragredient, and the Hermitian dual of $\pi_s$ is again $\pi_s$, with the two factors exchanged. Since $\pi_s$ is irreducible and admissible, the form is unique up to a scalar. On each finite-dimensional space of $K$-types, the form depends continuously on $s$ and never becomes degenerate. A nondegenerate Hermitian form that varies continuously keeps its signature. At $s = 0$ the form is definite, so all $\pi_s$ are unitarisable.

Now let $t \in k^\times$ with $|t| < 1$. The scalar matrix $t$ in the first block acts on $\rho\nu^{-s} \otimes \rho\nu^{s}$ by a scalar $c$ with $|c| = |t|^{-ds}$. For a unitarisable admissible product induced from a representation where this element acts by $c$, the matrix coefficients are bounded, and this gives $|c|\, |t|^{d^2/2} \le 1$. So $|t|^{d(d/2 - s)} \le 1$, which fails for $s > d/2$. This is a contradiction. $\square$

**Proposition 7.8.3 (Pairs of cuspidals).** Let $x$ and $y$ be irreducible cuspidal representations with $x \ne y\nu$ and $y \ne x\nu$. Then $x \times y$ is irreducible.

This is the result of Bernstein and Zelevinsky on products of two cuspidal representations. It is proved from the Jacquet module of $x \times y$, which has the two constituents $x \otimes y$ and $y \otimes x$, and from the compatibility of the Jacquet functor with contragredients.

*Proof of the theorem.* Every irreducible cuspidal $y$ has the form $\rho\nu^{z}$, with $\rho$ unitarisable cuspidal and $z$ real. Take $s \ge 0$ from the first proposition, so $\rho\nu^{-s} \times \rho\nu^{s}$ is reducible. By the second proposition, $\rho\nu^{s} = \rho\nu^{-s}\nu$ or $\rho\nu^{-s} = \rho\nu^{s}\nu$. Since $d \ge 1$, the map $u \mapsto \rho\nu^u$ is injective on real $u$. The second case gives $s = -\tfrac12$, which is impossible, and the first gives $s = \tfrac12$. So $\rho\nu^{-1/2} \times \rho\nu^{1/2}$ is reducible. Twist by $\nu^{z + 1/2}$: the product $y \times y\nu$ is reducible, since twisting by a character preserves irreducibility. $\square$

### The segment representation

**Theorem 7.8.4 (Segment representation).** Let $\rho$ be an irreducible cuspidal representation of $\mathrm{GL}_d(k)$ and $l \ge 1$. Let $\Pi = \rho \times \rho\nu \times \dots \times \rho\nu^{l-1}$. Then $\Pi$ has a unique irreducible subrepresentation $Z$, and
$$r_{(d, \dots, d)}(Z) \cong \rho \otimes \rho\nu \otimes \dots \otimes \rho\nu^{l-1}.$$

Lean: `PositivityTheory.RgGu.segmentRepresentation`.

*Proof.* By the geometric lemma of Bernstein and Zelevinsky, $r_{(d, \dots, d)}(\Pi)$ has a filtration whose layers are the tensor products $\rho\nu^{w(0)} \otimes \dots \otimes \rho\nu^{w(l-1)}$, one for each permutation $w$ of $\{0, \dots, l-1\}$. These tensor products are pairwise non-isomorphic, since the exponents are distinct. So the standard tensor $\tau_0 = \rho \otimes \rho\nu \otimes \dots \otimes \rho\nu^{l-1}$ occurs exactly once in the Jacquet module.

By Frobenius reciprocity, every irreducible subrepresentation $S$ of $\Pi$ has $\tau_0$ as a quotient of $r(S)$. Since $\tau_0$ has multiplicity one in $r(\Pi)$ and $r$ is exact, two different irreducible subrepresentations cannot both contain it. This gives the unique $Z$.

It remains to show that $r(Z)$ has no other constituent. Each constituent of $r(Z)$ is a tensor $\tau_w$ for some $w$. Fix $i$ with $i + 1 < l$. One shows that $\Pi$ has a nonzero subrepresentation $T$ such that every constituent $\tau_w$ of $r(T)$ has $w^{-1}(i) < w^{-1}(i+1)$: the factor $\rho\nu^{i}$ comes before $\rho\nu^{i+1}$. Take $T = \rho \times \dots \times \rho\nu^{i-1} \times Z_2 \times \rho\nu^{i+2} \times \dots$, where $Z_2$ is the unique irreducible subrepresentation of $\rho\nu^{i} \times \rho\nu^{i+1}$. By the theorem on reducibility at $\nu$, $\rho\nu^{i} \times \rho\nu^{i+1}$ has length two. Its Jacquet module has the two constituents $\rho\nu^{i} \otimes \rho\nu^{i+1}$ and $\rho\nu^{i+1} \otimes \rho\nu^{i}$, and $Z_2$ has only the first. Since $T$ contains an irreducible subrepresentation, and that one is $Z$, the constituents of $r(Z)$ satisfy the same order condition for every $i$. A permutation with $w^{-1}(i) < w^{-1}(i+1)$ for all $i$ is the identity. So $r(Z)$ has only $\tau_0$ as a constituent, with multiplicity one, and $r(Z) \cong \tau_0$. $\square$

The representation $Z$ is the representation $Z(\Delta)$ of Zelevinsky. The same argument with the order reversed gives the unique irreducible quotient $L(\Delta)$.

### Generic representations

Fix a nontrivial character $\psi$ of $k$. A smooth representation of $\mathrm{GL}_N(k)$ is *generic* if it has a nonzero Whittaker functional for the character $\psi(u_{12} + \dots + u_{N-1,N})$ of the upper unipotent group. This does not depend on the choice of $\psi$.

**Theorem 7.8.5 (Uniqueness of generic representations).** Let $\pi$ and $\sigma$ be irreducible generic representations of $\mathrm{GL}_N(k)$ with the same cuspidal support. Then $\pi \cong \sigma$.

Lean: `GlobalTheory.RgGu.genericUnique` (also `GlobalTheory.RgGu.genericUnique_of`).

The proof uses four results of the Bernstein and Zelevinsky theory. Let $\rho_1, \dots, \rho_h$ be irreducible cuspidal.

1. *Realization.* An irreducible $\pi$ with cuspidal support $\{\rho_1, \dots, \rho_h\}$ is a subquotient of $\rho_1 \times \dots \times \rho_h$, in some order of the factors.
2. *Swap.* If an irreducible generic $\sigma$ is a subquotient of $\rho_1 \times \dots \times \rho_h$, it is also a subquotient of the product with two adjacent factors exchanged.
3. *Rank.* The product $\rho_1 \times \dots \times \rho_h$ has a space of Whittaker functionals of dimension at most one. This follows from the heredity of Whittaker models under induction and from the fact that each cuspidal $\rho_i$ has a Whittaker functional unique up to a scalar.
4. *Extension.* If a representation of finite length has a space of Whittaker functionals of dimension at most one, then it has at most one generic irreducible subquotient, up to isomorphism. This uses the exactness of the Whittaker functor.

*Proof.* By realization, $\pi$ is a subquotient of $\rho_1 \times \dots \times \rho_h$ and $\sigma$ of $\rho_{\tau(1)} \times \dots \times \rho_{\tau(h)}$, for one numbering of the support and a permutation $\tau$. Every permutation is a product of adjacent transpositions. By the swap result, applied once for each transposition, $\sigma$ is also a subquotient of $\rho_1 \times \dots \times \rho_h$. This product has Whittaker rank at most one, and $\pi$ and $\sigma$ are both generic irreducible subquotients. By the extension result, $\pi \cong \sigma$. $\square$

**Theorem 7.8.6 (Zelevinsky).** Let $k$ have characteristic zero, and let $\pi$ be an irreducible generic representation of $\mathrm{GL}_N(k)$. Then there are segments $\Delta_1, \dots, \Delta_h$, pairwise not linked, such that
$$\pi \cong L(\Delta_1) \times \dots \times L(\Delta_h).$$

Lean: `GlobalTheory.RgGu.genericUnlinkedGL_of_segRep2`.

*Proof.* Let $s$ be the cuspidal support of $\pi$. The multiset $s$ is a union of segments $\Delta_1, \dots, \Delta_h$ that are pairwise not linked. To see this, group $s$ by cuspidal lines $\{\rho\nu^{m} : m \in \mathbb{Z}\}$, and on each line take repeatedly the longest segment that remains in the multiset. For unlinked segments, the product $L(\Delta_1) \times \dots \times L(\Delta_h)$ is irreducible. This is proved from the segment theorem and the theorem on reducibility at $\nu$: the Jacquet modules of the $L(\Delta_i)$ are known, and a nonzero intertwining operator between the products in two orders exists only for linked segments. Each $L(\Delta_i)$ is generic, and a product of generic representations is generic, by the heredity of Whittaker models. So $L(\Delta_1) \times \dots \times L(\Delta_h)$ is irreducible, generic, and has support $s$. By the uniqueness theorem it is isomorphic to $\pi$. $\square$

The hypothesis of characteristic zero comes from the statement in the literature. None of the inputs of the proof uses it.

**Remark 7.8.7 (Formalization).** The reducibility at $\nu$ is in [RhoNuRhoReducibleC.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SegmentJacquetSubquotients/RhoNuRhoReducibleC.lean#L17). The reduction to some reducibility point is in [RhoNuRhoOfC.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SegmentJacquetSubquotients/RhoNuRhoOfC.lean#L30), and the complementary series argument in [SomeRed.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SomeRed.lean#L111). The constancy of the signature is proved in [PosMkIff.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/PosMkIff.lean#L353), a file named after a small lemma. The segment theorem is in [SegmentRepresentation.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SegmentJacquetSubquotients/SegmentRepresentation.lean#L9), with the order argument in [SegRepOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/SegmentJacquetSubquotients/SegRepOf.lean#L46), which raises the heartbeat limit to one million. The library has two more proofs of the same segment statement, under other names: a copy of this whole tree in [the companion RhoNuRhoReducibleC.lean](lean:CompanionTheory/RealGroups/GeneralUnitaryRepresentations/ArchimedeanJacquetSegments/SegmentSubquotients/RhoNuRhoReducibleC.lean#L17), filed under real groups although it is about $p$-adic groups, and a separate proof in [RankEquivariantFunctionalsCongr.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/RankEquivariantFunctionalsCongr.lean#L37). The uniqueness theorem is in [TopAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/GenericUnlinkedGL/TopAll.lean#L10), and its proof by adjacent transpositions in [ExistsEquivOfMapUnivEq.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/GenericUnlinkedGL/ExistsEquivOfMapUnivEq.lean#L73), named after a lemma on multisets. Zelevinsky's theorem is in [GenericUnlinkedGLOfSegRep2.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/GenericUnlinkedGL/GenericUnlinkedGLOfSegRep2.lean#L11); the assembly in [GenericUnlinkedGLOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/GenericUnlinkedGL/GenericUnlinkedGLOf.lean#L21) asks for characteristic zero in each of its three inputs, but it is given results proved for all local fields. In the formal statement, $L(\Delta)$ is defined as the unique irreducible quotient of the segment product, and the four results of the Bernstein and Zelevinsky theory are separate statements in the library.
