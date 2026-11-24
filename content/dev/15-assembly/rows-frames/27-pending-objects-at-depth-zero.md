---
title: Pending objects at depth zero
decls:
  - GlobalTheory.T.exists_pending_objects_depthZero_admissible_eigenSpan
  - GlobalTheory.PendClose.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pending objects at depth zero

The inertia argument at the two type primes $g_0$ and $g_1$ needs a package of objects that are not part of a datum: the representation theory of $\mathrm{GL}_r$ over the residue fields, the tame inertia characters, an action of the centre of a group algebra on the spaces of modular forms, and some compatibilities among them. We call such a package a *pending object*. This section proves that a pending object exists with two properties, depth zero admissibility and the eigenspace property, from hypotheses on a family of motives. The result is used in [the closing step for the local components](/entry/pin-close-loc-comp-of-is-rc-class-map-d-cen-loc/).

### Pending objects

Let $D$ be a datum. For $k \in \{0, 1\}$ write $g = g_k$, $\mathbb{F}_g$ for the field with $g$ elements, and $G^0$ for the finite group of the level. For a local index $i$ of $D$ let $\mathcal{O}_i$ be its coefficient ring, $\mathbb{T}_i$ its Hecke algebra, and $M_i$ its module of forms.

**Definition 7.27.1 (Pending object).** A *pending object* $P$ for $D$ consists of the following data.

1. For each $k$, finite group data $\Lambda_k$ for $\mathrm{GL}_r(\mathbb{F}_{g_k})$: a set of irreducible classes $\tau$, a label $\mathrm{lab}(\tau) \in \mathbb{F}_g[X]$, a central idempotent $e_\tau$, and a Harish-Chandra relation $\mathrm{hc}$ between classes. The series idempotent of $D$ at a polynomial $f$ is
$$e_{\mathrm{ser}}(f) = \sum_{\mathrm{lab}(\tau) = f} e_\tau,$$
and each of its coefficients comes from the row field.
2. For each $i$, a primitive root of unity in $\mathcal{O}_i$ of the order of the finite group of the rows.
3. Tame inertia characters $\omega_{k,w,x}$ for $x \in \bar{\mathbb{F}}_g^\times$ and places $w$ of $E$: they are $1$ at $1$, multiplicative in $\sigma$ on the inertia group and in $x$, trivial on wild inertia and on an open subgroup, injective in $x$ at the places over $g$, and equal to the Teichmüller character at the fixed tame generator.
4. The eigenvalue law: at each place over $g$, the characteristic polynomial of $\sigma$ in the inertia group on a local piece $L$ of degree $\dim L$ is
$$\prod_{x} \bigl(X - \omega_{k,w,x}(\sigma)\bigr),$$
the product over the roots $x$ of the polynomial of $L$ in $\bar{\mathbb{F}}_g$. Twisting $L$ by a character with polynomial $X - u$ multiplies these roots by $u$.
5. For each $i$, an algebra map $z \mapsto Z_i(z)$ from the centre of $\mathcal{O}_i[G^0]$ to the endomorphisms of $M_i$ that commutes with $\mathbb{T}_i$, is compatible with the action of central elements on the rational forms, and is compatible with the projection to $M_i \otimes K_i$.
6. The type projection law: the projection of a type vector of a point $p$ lies in the Hecke eigenspace of $p$, and it is $0$ if there is no point.
7. Parameter surjectivity: each local parameter of a type comes from a global parameter.
8. For each $i$, each automorphic vector $\Pi$ and each place $v$ over $g_k$, the set $\mathrm{kty}(i, \Pi, k, v)$ of classes $\tau$ with $e_\tau$ acting by a nonzero map on some type vector of $\Pi$ at $v$.

Let $\chi_J$ be the level character at $(i, k, v)$, an element of $\mathbb{F}_g^\times$.

**Definition 7.27.2 (Depth zero admissible).** A pending object $P$ is *depth zero admissible* if the following holds. Let $\tau \in \mathrm{kty}(i, \Pi, k, v)$ have a squarefree label that has neither $\chi_J$ nor $\chi_J^{-1}$ as a root. Then there is $u \in \{\chi_J, \chi_J^{-1}\}$ such that the local piece of $\Pi$ at the place $w$ over $v$ is of depth zero, its polynomial is
$$\mathrm{lab}(\tau) \cdot (X - u)^t,$$
and at each place $w'$ conjugate to $w$ the local piece is of depth zero with polynomial of degree $n_V$.

**Definition 7.27.3 (Eigenspace property).** A pending object $P$ has the *eigenspace property* if the following holds for each $i$, each central element $z$, each point $x$ and each $c \in \mathcal{O}_i$. Suppose that $z$ acts by $c$ on every type vector of every automorphic vector with point $x$. Then $Z_i(z)$ acts by $c$ on the Hecke eigenspace of $x$ in $M_i \otimes K_i$.

### The theorem

**Theorem 7.27.4 (Pending objects exist).** Let $D$ be a datum and let $M$ be a family of motives for $D$. Assume:

1. the family is tied to the Hecke eigenvalues, rational, and tied to the abelian varieties;
2. each local parameter of a form comes from a global parameter;
3. the first tie, the admissibility condition of weight $5$, the inertia representation hypothesis, the depth and generation hypotheses on labels, the stability of the rational centre, the integrality of the centre, and the condition that the action on forms preserves type vectors;
4. the coefficients of the series idempotents lie in the row field, and the coefficient rings have the roots of unity of item 2;
5. the depth zero hypothesis and the admissibility of depth zero types.

Then there is a pending object $P$ for $D$ that is depth zero admissible and has the eigenspace property.

Lean: `GlobalTheory.T.exists_pending_objects_depthZero_admissible_eigenSpan` (also `GlobalTheory.PendClose.main`).

*Proof.* We build the fields of $P$ in order, and then check the two properties.

1. Every place over a type prime has a split conjugate place with a uniformizer, by the split existence theorem for every datum.
2. For each $i$ there is a section of the localized forms at the type sections: the Hecke operators at all places act by scalars on the type spaces, and with the three ties this gives a nonempty set of sections.
3. The finite group data $\Lambda_k$ with the series identity of item 1 exist.
4. The inertia characters $\omega$ with the eigenvalue law exist, by the inertia, depth and generation hypotheses.
5. The twist law of item 4 holds: twisting by a tame label multiplies the roots, from the first tie and the hypotheses on labels.
6. The centre action $Z_i$ exists, from the sections, the stability of the rational centre, the integrality of the centre and the preservation of type vectors.
7. The type projection law holds, from the sections.
8. Each place over a type prime is split, and with the parameter hypothesis, the first tie, the weight $5$ condition and the depth hypotheses, each local parameter of a type is a global parameter.

These fields with the hypotheses of item 4 form a pending object $P$. Depth zero admissibility of $P$ follows from the admissibility of depth zero types, applied to the data of $P$. The eigenspace property follows from the sections of step 2 and the preservation of type vectors: a central element that acts by $c$ on the type vectors acts by $c$ on the eigenspace, because the eigenspace is spanned by the projections of type vectors. $\square$

The proof is an assembly of eleven cited results, one for each field or property. The content is in those results. The theorem itself fixes the order: the sections of step 2 are used three times, for the centre, for the projection law and for the eigenspace property.

In the classical language, the labels are the Green polynomials of the irreducible characters of $\mathrm{GL}_r(\mathbb{F}_g)$, grouped by the characteristic polynomial of their semisimple part. The depth zero condition says that a type of label $f$ forces the local Galois representation at $w$ to be tamely ramified, with inertia eigenvalues the Teichmüller lifts of the roots of $f$ and of $u$, the last one $t$ times.

**Remark 7.27.5 (Formalization).** The relay is at line 7 of [ExistsPendingObjectsDepthZeroAdmissibleEigenSpanStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsPendingObjectsDepthZeroAdmissibleEigenSpanStatement.lean#L7). The target `GlobalTheory.PendClose.main` is at line 20 of [ExistsPendingObjectsDepthZeroAdmissibleEigenSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsPendingObjectsDepthZeroAdmissibleEigenSpan.lean#L20); it builds the object with the constructor `mk` of `GlobalTheory.PendOf` and returns it with the two properties. The structure `Pend` is at line 46 of [PairedCharacterCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/PairedCharacterCondition.lean#L46) and `admDZ` at line 359 of the same file. The property `EigSpan` is at line 14 of [StepJumpDirect.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/StepJumpDirect.lean#L14). The comparison with Green polynomials and tame ramification is our reading of the fields; the Lean fields do not name them.
