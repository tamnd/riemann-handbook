---
title: Compatibility on a class of places
decls:
  - UpperTheory.Gal.Int.Row.galoisLocalGlobal_of_placeClassCompatibility
  - UpperTheory.Gal.Int.Row.galoisLocalGlobal_of_localGlobalCompatibility
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Compatibility on a class of places

The proof of [the Galois row from the spherical Galois row](/entry/rest/) uses three inputs: the spherical Galois row (Definition 3.18.2), compatibility for plain toral components (Definition 3.17.3), and compatibility at depth zero (Definition 3.17.4). This section gives the assembly step in detail. We state the depth-zero input for a class of places, so that one argument gives both the Galois row at all $\mathbb{Q}_g$ places (Definition 3.18.3) and the form with $w$ big for $a$. The main result is [Theorem 3.23.10](/entry/galois-local-global-of-place-class-compatibility/), and [Corollary 3.18.4](/entry/galois-local-global-of-local-global-compatibility/) is the form that the proof of Theorem 3.18.4 uses.

We keep the notation of Section 17 and Section 18. In particular $E$ is a CM field, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $\pi$ is a cuspidal representation of $\mathrm{GL}_a(\mathbb{A}_E)$ in scope with $\chi$, and $r$ is attached to $\pi$. For a local component $\sigma$ of $\pi$ at $w$ we write $\sigma^\circ = \sigma \otimes |\det|^{(1-a)/2}$, and for a reciprocity map $\mathrm{rc}$ that satisfies the laws of [the local reciprocity step](/step/is-rect-def/) we write $y_\sigma = \mathrm{rc}(\sigma^\circ)$. Toral, tame and square-free Weil-Deligne representations are as in Section 07.

### The depth-zero input for a class of places

A *class of places* is a rule $Q$ that assigns to each number field $E$, each finite place $w$ of $E$ and each $n \geq 1$ a statement $Q(E, w, n)$. Two examples are the class of all places and the class of places that are big for $n$.

**Definition 3.23.1 (Compatibility on a class of places).** Let $Q$ be a class of places. *Compatibility on $Q$* holds if, for all data $E, \ell, \iota, n, \pi, \chi, r$ as above, every place $w$ and every local component $\sigma$ of $\pi$ at $w$ such that $\sigma$ has depth zero, $Q(E, w, n)$ holds, $E_w \cong \mathbb{Q}_g$ for a prime $g$ and $\sigma^\circ$ is apart, the following holds for every valuation ring $A$ over $w$ and every reciprocity map $\mathrm{rc}$ such that $\mathrm{rc}(\sigma^\circ)$ has zero monodromy:

1. if $w \nmid \ell$, then $\mathrm{WD}_w(r)$ has zero monodromy, and $\operatorname{charpol}_t \mathrm{WD}_w(r) = \operatorname{charpol}_t \mathrm{rc}(\sigma^\circ)$ for every $t$ in the inertia group;
2. if $w \mid \ell$, then $r$ is de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ inducing $w$, and for all comparison data $r$ is potentially semistable at $w$, $\mathrm{WD}_w(r)$ has zero monodromy, and $\operatorname{charpol}_t \mathrm{WD}_w(r) = \operatorname{charpol}_t \mathrm{rc}(\sigma^\circ)$ for every $t$ in the inertia group.

Lean: `UpperTheory.Gal.Int.Row.LocalGlobalCompatibilityAtPlaceClass` (also `UpperTheory.Gal.Int.Row.PlaceClass`).

**Lemma 3.23.2 (Depth zero gives every class).** If compatibility at depth zero holds, then compatibility on $Q$ holds for every class of places $Q$.

Lean: `UpperTheory.Gal.Int.Row.localGlobalAtPlaceClass_of_localGlobal`.

*Proof.* The hypotheses of compatibility on $Q$ contain the second case of Definition 3.17.4: $\sigma$ has depth zero, $E_w \cong \mathbb{Q}_g$ and $\sigma^\circ$ is apart. The conclusions are the same. The hypothesis $Q(E, w, n)$ is not used. $\square$

### Local facts

The next lemmas are the four local facts in the proof of Theorem 3.18.4.

**Lemma 3.23.3 (Inertia and degree zero).** Let $x$ and $y$ be Weil-Deligne representations at $A$ with $\operatorname{charpol}_t x = \operatorname{charpol}_t y$ for every $t$ in the inertia group. Then $x$ and $y$ have the same dimension, and $\operatorname{charpol}_g x = \operatorname{charpol}_g y$ for every $g$ of degree $0$ in the Weil group.

Lean: `UpperTheory.Gal.Int.Row.charPol_of_ine` (also `UpperTheory.Gal.Int.Row.dim_of_ine`).

*Proof.* Let $\varphi$ be a Frobenius element, of degree $1$. Every $g$ in the Weil group is $\varphi^k t$ with $k = \deg g$ and $t$ in the inertia group. If $\deg g = 0$, then $g = t$ is in the inertia group. The dimension is the degree of the characteristic polynomial of the identity, which is in the inertia group. $\square$

**Lemma 3.23.4 (Generic components).** For every local component $\sigma$ of $\pi$, the representation $\sigma^\circ$ is generic. If $E_w \cong \mathbb{Q}_g$ and $y_\sigma$ is tame and square-free with zero monodromy, then $\sigma$ has depth zero and $\sigma^\circ$ is apart.

Lean: `UpperTheory.Gal.Int.Row.guard_tame` (also `UpperTheory.Gal.Int.Row.generic_algNorm`).

*Proof.* A local component of a cuspidal representation is generic, and a twist of a generic representation by a character of the determinant is generic. For the second statement, the laws of $\mathrm{rc}$ and genericity give that $\sigma^\circ$ has depth zero and that every support of $\sigma^\circ$ is unlinked, with no two members of size at least $2$ unramified twists of each other. So $\sigma^\circ$ is apart. Depth zero of the twist $\sigma^\circ$ gives depth zero of $\sigma$. $\square$

The picture behind the second statement is in the proof of Theorem 3.18.4. The fact that a toral $y_\sigma$ with zero monodromy makes $\sigma^\circ$ plain toral is also used, from the same source (see the Remark).

**Definition 3.23.5 (Matching on a class).** Let $q$ be a statement, and let $x, y$ be Weil-Deligne representations at a place $w$. Then $x$ and $y$ *match under $q$* if they have the same dimension, $x = y$ when $y$ is toral with zero monodromy, and, when $q$ holds, $E_w \cong \mathbb{Q}_g$ and $y$ is tame and square-free with zero monodromy, $x$ has zero monodromy and the same characteristic polynomial as $y$ on every element of degree $0$.

Lean: `UpperTheory.Gal.Int.Row.Cmp`.

With $q$ true this is the matching of clause 3 in Definition 3.18.3. With $q$ the statement "$w$ is big for $\dim y$" it is the matching of Section 07, since a big place has $E_w \cong \mathbb{Q}_g$.

### Away from $\ell$ and above $\ell$

**Lemma 3.23.6 (Away from $\ell$).** Assume compatibility for plain toral components and compatibility on $Q$. Let $w \nmid \ell$, let $\sigma$ be a local component of $\pi$ at $w$, and let $\mathrm{rc}$ be a reciprocity map. Then $\mathrm{WD}_w(r)$ and $y_\sigma$ match under $Q(E, w, a)$.

Lean: `UpperTheory.Gal.Int.Row.away`.

*Proof.* The dimension of $\mathrm{WD}_w(r)$ is $a$, and the laws of $\mathrm{rc}$ give $\dim y_\sigma = a$. If $y_\sigma$ is toral with zero monodromy, then $\sigma^\circ$ is plain toral, and item 1 of Definition 3.17.3 gives $\mathrm{WD}_w(r) = y_\sigma$. Let $Q(E, w, a)$ hold, $E_w \cong \mathbb{Q}_g$, and let $y_\sigma$ be tame and square-free with zero monodromy. By the lemma on generic components, $\sigma$ has depth zero and $\sigma^\circ$ is apart. Item 1 of compatibility on $Q$ gives zero monodromy and equal characteristic polynomials on inertia. The lemma on inertia gives them on every element of degree $0$. $\square$

**Lemma 3.23.7 (Above $\ell$).** Assume compatibility for plain toral components and compatibility on $Q$. Let $w \mid \ell$, fix comparison data, let $\sigma$ be a local component of $\pi$ at $w$, and let $\mathrm{rc}$ be a reciprocity map such that $y_\sigma$ has zero monodromy. Suppose that $y_\sigma$ is toral, or that $Q(E, w, a)$ holds, $E_w \cong \mathbb{Q}_g$ and $y_\sigma$ is tame and square-free. Then $r$ is de Rham at $w$ with Hodge-Tate jumps $\mathrm{HT}(\tau)$ at each $\tau$ inducing $w$, $r$ is potentially semistable at $w$, and $\mathrm{WD}_w(r)$ and $y_\sigma$ match under the statement that $E_w \cong \mathbb{Q}_g$.

Lean: `UpperTheory.Gal.Int.Row.above`.

*Proof.* Let $y_\sigma$ be toral. Then $\sigma^\circ$ is plain toral, and item 2 of Definition 3.17.3 gives the de Rham property, potential semistability, zero monodromy and equal characteristic polynomials on the whole Weil group. Two Weil-Deligne representations with zero monodromy and equal characteristic polynomials everywhere are equal, so $\mathrm{WD}_w(r) = y_\sigma$. This gives all parts of the matching.

Let $y_\sigma$ not be toral. Then $Q(E, w, a)$ holds, $E_w \cong \mathbb{Q}_g$, and $y_\sigma$ is tame and square-free. By the lemma on generic components, $\sigma$ has depth zero and $\sigma^\circ$ is apart, and item 2 of compatibility on $Q$ gives the de Rham property, potential semistability, zero monodromy and equal characteristic polynomials on inertia. The lemma on inertia gives the dimension and the polynomials on elements of degree $0$. The toral part of the matching is empty, since $y_\sigma$ is not toral. $\square$

### Weights and spherical places

**Lemma 3.23.8 (Weights).** There are an integer $\mathrm{wt}$ and multisets $\mathrm{HT}(\tau)$ of integers, for the embeddings $\tau : E \to \overline{\mathbb{Q}}_\ell$, such that $\mathrm{HT}(\tau) = \{\tfrac{a-1}{2} - z\}$ for $z$ in the infinitesimal character of $\pi$ at $\iota \circ \tau$, and $\mathrm{HT}(\tau \circ c) = \{\mathrm{wt} - j : j \in \mathrm{HT}(\tau)\}$.

Lean: `UpperTheory.Gal.Int.Row.exists_weights`.

*Proof.* Since $\pi$ is regular algebraic, each $\tfrac{a-1}{2} - z$ is an integer, which defines $\mathrm{HT}(\tau)$. Since $\pi$ is polarized by $\chi$, it has a weight $\mathrm{wt}$: the infinitesimal character at $\iota \circ \tau \circ c$ is $\{a - 1 - \mathrm{wt} - z\}$, for $z$ in the infinitesimal character at $\iota \circ \tau$. Then $\tfrac{a-1}{2} - (a - 1 - \mathrm{wt} - z) = \mathrm{wt} - (\tfrac{a-1}{2} - z)$, which is the second formula. We did not open the proof that the weight exists. $\square$

**Lemma 3.23.9 (Spherical places above $\ell$).** Assume the spherical Galois row. If $\sigma$ is a spherical local component of $\pi$ at $w$, then $r$ satisfies the crystalline clause and the de Rham clause of Definition 3.18.2 at $w$.

Lean: `UpperTheory.Gal.Int.Row.crys` (also `UpperTheory.Gal.Int.Row.exists_hasSat`).

*Proof.* A spherical local component has Satake parameters, so $\pi$ has Satake parameters $B$ at $w$. Item 2 of Definition 3.18.2 applies to $B$. $\square$

### The assembly

**Theorem 3.23.10 (The Galois row from compatibility on all places).** Assume the spherical Galois row, compatibility for plain toral components, and compatibility on the class of all places. Then the Galois row at all $\mathbb{Q}_g$ places holds.

Lean: `UpperTheory.Gal.Int.Row.galoisLocalGlobal_of_placeClassCompatibility`.

*Proof.* Let $\pi$ be regular algebraic and polarized by $\chi$. Then $\pi$ is in scope. Item 1 of Definition 3.18.2 gives an attached $r$, and $r$ is continuous and semisimple, which is clause 1 of Theorem 3.7.5. The lemma on weights gives $\mathrm{wt}$ and $\mathrm{HT}$ with clause 2.

Clause 3. Let $w \nmid \ell$. The lemma away from $\ell$, with $Q$ the class of all places, gives that $\mathrm{WD}_w(r)$ and $y_\sigma$ match under a true statement. This is the matching of Definition 3.18.3.

Clause 4. Let $w \mid \ell$ and fix comparison data. If $\sigma$ is spherical, the lemma on spherical places gives that $r$ is crystalline and de Rham at $w$, with jumps given by the infinitesimal character, which are $\mathrm{HT}(\tau)$. If $y_\sigma$ has zero monodromy and is toral, or tame and square-free with $E_w \cong \mathbb{Q}_g$, the lemma above $\ell$ gives the de Rham property with jumps $\mathrm{HT}(\tau)$, potential semistability, and the matching. $\square$

**Corollary 3.23.11 (The Galois row from compatibility at depth zero).** Assume the spherical Galois row, compatibility for plain toral components, and compatibility at depth zero. Then the Galois row at all $\mathbb{Q}_g$ places holds.

Lean: `UpperTheory.Gal.Int.Row.galoisLocalGlobal_of_localGlobalCompatibility`.

*Proof.* By the lemma that depth zero gives every class, compatibility on the class of all places holds. Apply [Theorem 3.23.10](/entry/galois-local-global-of-place-class-compatibility/). $\square$

The proof of Theorem 3.18.4 applies the corollary with [the theorem on plain toral components](/entry/toral-galois-galois-compat-unlinked-support-of-spherical/) and Theorem 3.17.12.

The same assembly with the class of places that are big for $n$ gives the conclusion of Theorem 3.7.5 itself. In the lemma away from $\ell$, the statement "$w$ is big for $a$" becomes "$w$ is big for $\dim y_\sigma$", since $\dim y_\sigma = a$. A big place has $E_w \cong \mathbb{Q}_g$.

**Remark 3.23.12 (Formalization).** The file is [GaloisLocalGlobalOfLocalGlobalCompatibility.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/InertCharpoly/GaloisLocalGlobalOfLocalGlobalCompatibility.lean#L157). The theorem is used only with the class $Q$ that is always true, through the corollary at line 192. The class of big places appears in `galois_realisation_of_rank_two` (line 173), which proves `Row0b`. The lemma that depth zero gives every class ignores the hypothesis $Q$ (line 45). Its partner `rank_two_general_of_rank_two` (line 42) and `galois_realisation_of_rank_two` have names that do not refer to rank two. The condition $E_w \cong \mathbb{Q}_g$ has two definitions with the same body: `IsQg` in [IsQg.lean](lean:Development/AbelianVarietyTheory/Statements/EllipticCurveLevels/IsQg.lean#L28) and `IsQp` in [WeightsConjAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjAlt.lean#L20); the proofs pass one for the other by definitional unfolding. The toral and tame facts are `plainTor_of_tor` and `mixed_of_tame` in [CharPolOfInert.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/InertCharpoly/CharPolOfInert.lean#L97); we opened their statements only. We also did not open `exists_isWeight` or `cuspRep_satake_iff_localComponent_satake`.
