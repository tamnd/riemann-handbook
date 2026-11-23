---
id: artin-reciprocity-char-zero
title: Local reciprocity for local fields of characteristic zero
kind: theorem
decl: ReciprocityTheory.DiscreteGroups.LocalClassField.artin_reciprocity_char_zero
module: ReciprocityTheory.ClassFieldTheory.LocalClassField.TransportC
covers: 770
status: drafted
drafted_by: writer@claude
---
This theorem gives a local Artin map for each nonarchimedean local field of characteristic $0$. It is used by [the index-two theorem for norm groups](/entry/mul-mem-range-norm/) in Volume 9. The proof moves the field inside $\overline{\mathbb{Q}}_p$ and uses [the Artin map for finite extensions of $\mathbb{Q}_p$](/entry/exists-is-artin-k/). That entry and [its main lemma](/entry/is-artin-k-of-is-recip/) hold 750 of the 770 declarations below this one.

## Statement

Let $K$ be a nonarchimedean local field of characteristic $0$, with algebraic closure $\overline{K}$ and $G_K^{\mathrm{ab}}$ the abelianization of $\mathrm{Gal}(\overline{K}/K)$. A homomorphism $\mathrm{Art} \colon K^\times \to G_K^{\mathrm{ab}}$ is a *local Artin map* (`IsLocalArtinMap`) if:

1. it is continuous, injective and has dense image;
2. for each uniformizer $\pi$, each $g \in \mathrm{Gal}(\overline{K}/K)$ with image $\mathrm{Art}(\pi)$ is a Frobenius lift: $g(x) - x^q$ lies in the maximal ideal for each integral $x$, where $q$ is the order of the residue field;
3. for each finite abelian extension $L \subseteq \overline{K}$ of $K$, the map $K^\times \to \mathrm{Gal}(L/K)$ is surjective with kernel $N_{L/K}(L^\times)$.

**Theorem.** $K$ has a local Artin map (`LocalReciprocity K`).

Condition 3 is the local reciprocity law (Neukirch, Algebraic Number Theory, Ch. V, Thm. 1.3).

## Proof

1. `exists_model` gives a prime $p$ and a model of $K$: a finite extension $K'$ of $\mathbb{Q}_p$ inside $\overline{\mathbb{Q}}_p$, a homeomorphic field isomorphism $e \colon K \to K'$ that matches the integers, and an isomorphism $\overline{K} \to \overline{\mathbb{Q}}_p$ that extends $e$. It finds $p$ as the residue characteristic, a continuous map $\mathbb{Q}_p \to K$, and shows that $K$ is finite over $\mathbb{Q}_p$.
2. `exists_isArtinK` gives a map $\mathrm{Art}'$ for $K'$ with the properties `IsArtinK`, the same three conditions stated for subfields of $\overline{\mathbb{Q}}_p$.
3. `Model.artin_reciprocity_of_model` moves $\mathrm{Art}'$ back to $K$. It takes the isomorphism of Galois groups that the model induces (`exists_isGalIso`) and the induced homeomorphism of abelianizations (`exists_abIso`). Then `Model.isLocalArtinMap_iff` shows that the two lists of conditions match under these maps.

## In the Lean code

The theorem is in [TransportC.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportC.lean#L155). `LocalReciprocity` and `IsLocalArtinMap` are in [Reciprocity.lean](lean:ReciprocityTheory/NeutralLocalFields/Reciprocity.lean#L79), `IsArtinK` in [RecDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecDefs.lean#L31), and `Model` in [TransportDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportDefs.lean#L9).

- `exists_model` is in [TransportA.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportA.lean#L251). `Model.isLocalArtinMap_iff` and `Model.artin_reciprocity_of_model` are in the same file as the theorem.
- `CharZero K` is what gives the map from $\mathbb{Q}$, and then from $\mathbb{Q}_p$, into $K$. So the theorem covers only characteristic $0$. The standard theorem also holds for fields of characteristic $p$.
- The two definitions differ in form. `IsLocalArtinMap` uses Mathlib's `normGroup`, the image of the field norm. `IsArtinK` uses `normGrp`, defined through a product over coset representatives; `Model.mem_normGroup_iff` in [TransportB.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportB.lean#L46) shows that $e$ sends one to the other.
