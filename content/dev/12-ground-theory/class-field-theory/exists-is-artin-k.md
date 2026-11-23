---
id: exists-is-artin-k
title: An Artin map for each finite extension of the p-adic numbers
kind: theorem
decl: ReciprocityTheory.DiscreteGroups.LocalClassField.exists_isArtinK
module: ReciprocityTheory.ClassFieldTheory.LocalClassField.RecArtin
covers: 750
status: drafted
drafted_by: writer@claude
---
This theorem builds the local Artin map for a finite extension $K$ of $\mathbb{Q}_p$ inside $\overline{\mathbb{Q}}_p$. [Local reciprocity in characteristic zero](/entry/artin-reciprocity-char-zero/) moves the result to an abstract local field. The proof has two parts. `exists_artin_hom` builds a homomorphism from the local pairing, and [`isArtinK_of_isRecip`](/entry/is-artin-k-of-is-recip/) checks the axioms. That second lemma has 682 of the 750 declarations below this one.

## Statement

Let $G_K = \mathrm{Aut}(\overline{\mathbb{Q}}_p / K)$ and let $G_K^{\mathrm{ab}}$ be its topological abelianization. For a field $L$ with $K \subseteq L \subseteq \overline{\mathbb{Q}}_p$, $L$ finite over $\mathbb{Q}_p$, and $[G_K, G_K] \subseteq G_L$, call $L$ *finite abelian* (`IsAbLK`).

**Theorem.** If $K$ is finite over $\mathbb{Q}_p$, there is a homomorphism $\mathrm{Art} \colon K^\times \to G_K^{\mathrm{ab}}$ with the properties `IsArtinK`: it is continuous, injective and has dense image; each lift of $\mathrm{Art}(\pi)$, for $v_K(\pi) = 1$, is a Frobenius; and for each finite abelian $L$, the map $K^\times \to G_K / G_L$ is surjective with kernel the norm group of $L$.

## Proof

The link between $K^\times$ and $G_K$ is the relation `IsRecip`. For $a \in K^\times$ and $g \in G_K$, the relation $\mathrm{IsRecip}_L(a, g)$ says $\chi(g) = \mathrm{inv}(a \cup \delta\chi)$ for each character $\chi \colon G_K \to \mathbb{Q}/\mathbb{Z}$ that is trivial on $G_L$. The right side is the local symbol of Serre (Local Fields, Ch. XIV, §1).

1. For each finite abelian $L$ and each $a$, `exists_isRecip` gives some $g$ with $\mathrm{IsRecip}_L(a, g)$. Two such $g$ agree modulo $G_L$ (`IsRecip.unique`).
2. These choices are multiplicative in $a$ (`IsRecip.mul`) and compatible as $L$ grows (`IsRecip.of_le`), modulo $G_L$. So `exists_hom_GKab` glues them into one homomorphism $\mathrm{Art}$. This is `exists_artin_hom`: each lift $g$ of $\mathrm{Art}(a)$ satisfies $\mathrm{IsRecip}_L(a, g)$ for all finite abelian $L$.
3. `isArtinK_of_isRecip` turns this property into `IsArtinK`.

## In the Lean code

The theorem is in [RecArtin.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecArtin.lean#L87). Its proof is two lines. `exists_artin_hom` is in [the same file](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecArtin.lean#L17). `IsArtinK` and `IsAbLK` are in [RecDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecDefs.lean#L31). `IsRecip` and `pairK` are in [RecPairDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecPairDefs.lean#L38).

- `pairK` is the invariant of the Brauer class of the 2-cocycle $(\delta t) \cdot a$, where $t$ is a locally constant lift of $\chi$ to $\mathbb{Q}$. If no such class exists, `pairBr` gives $0$ by a case split. We have not unfolded `invBr`.
- The same file proves `IsArtinK.unique`: two maps with these properties are equal.
