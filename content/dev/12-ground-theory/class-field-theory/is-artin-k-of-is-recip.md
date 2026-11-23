---
id: is-artin-k-of-is-recip
title: The axioms of the Artin map, from the local symbol
kind: theorem
decl: ReciprocityTheory.DiscreteGroups.LocalClassField.isArtinK_of_isRecip
module: ReciprocityTheory.ClassFieldTheory.LocalClassField.RecArtin
covers: 682
status: drafted
drafted_by: writer@claude
---
This lemma holds most of local class field theory in the project. Its input is a homomorphism $\mathrm{Art} \colon K^\times \to G_K^{\mathrm{ab}}$ that agrees with the local symbol on each finite abelian extension. Its output is the list `IsArtinK` of [the parent theorem](/entry/exists-is-artin-k/). The parent entry defines $G_K$, finite abelian $L$, and the relation $\mathrm{IsRecip}_L(a, g)$; we use the same names here.

## Statement

Let $K \subseteq \overline{\mathbb{Q}}_p$ be finite over $\mathbb{Q}_p$. Let $\mathrm{Art} \colon K^\times \to G_K^{\mathrm{ab}}$ be a homomorphism. Assume that for each $a \in K^\times$, each $g \in G_K$ whose image in $G_K^{\mathrm{ab}}$ is $\mathrm{Art}(a)$, and each finite abelian $L$, we have $\mathrm{IsRecip}_L(a, g)$.

**Theorem.** $\mathrm{Art}$ satisfies `IsArtinK`: it is continuous, injective and has dense image; it sends a uniformizer to the class of a Frobenius; and for each finite abelian $L$, the induced map $K^\times \to G_K / G_L$ is surjective with kernel the norm group $N_L$.

## Proof

Two facts about a single finite abelian $L$ carry the proof. Both are in `PairKEqZeroOfMemNormGrp.lean`.

- (`exists_isRecip_of_gal`) Each $g \in G_K$ satisfies $\mathrm{IsRecip}_L(a, g)$ for some $a$.
- (`IsRecip.mem_subG_iff`) If $\mathrm{IsRecip}_L(a, g)$, then $g \in G_L$ if and only if $a \in N_L$.

The second fact comes from `recipHom_ker`. The map $a \mapsto g$ gives a homomorphism $\varphi \colon K^\times \to G_K / G_L$, and the first fact makes it surjective (`exists_recipHom`). The local symbol vanishes on norms (`pairK_eq_zero_of_mem_normGrp`), so $N_L \subseteq \ker \varphi$. The index of $N_L$ is at most $[L : K]$ (`index_normGrp_le`). The index of $\ker\varphi$ is $[L : K]$, so the two subgroups are equal. We have not unfolded the proofs of these two inputs.

With these facts, the conditions follow.

1. **Surjective onto $G_K / G_L$.** Take $a$ from the first fact; a lift of $\mathrm{Art}(a)$ agrees with $g$ modulo $G_L$ by `IsRecip.unique`.
2. **Kernel.** This is the second fact.
3. **Dense.** `denseRange_GKab_iff` reduces density to step 1 for all $L$.
4. **Continuous.** `continuous_GKab_iff` reduces it to this: for $y$ near $x$, lifts of $\mathrm{Art}(x)$ and $\mathrm{Art}(y)$ agree modulo $G_L$. The set $x N_L$ is open (`isOpen_normGrp`), and `IsRecip.inv_mul_mem` turns $x^{-1} y \in N_L$ into the claim.
5. **Injective.** If $\mathrm{Art}(a) = 1$, then $a \in N_L$ for all $L$ by the second fact. `eq_one_of_forall_mem_normGrp` gives $a = 1$. Its proof uses the existence theorem (`existence`): each subgroup of finite index is a norm group.
6. **Frobenius.** On the unramified fields $K_n$, the symbol of a uniformizer is the Frobenius `frobK` (`isRecip_uniformiser_Kn`). Then `isFrob_of_forall_Kn` shows that $g$ acts as a Frobenius.

## In the Lean code

The lemma is in [RecArtin.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecArtin.lean#L58). The two facts are in [PairKEqZeroOfMemNormGrp.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/PairKEqZeroOfMemNormGrp.lean#L128) and [the same file](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/PairKEqZeroOfMemNormGrp.lean#L186). The existence theorem is in [Existence.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/Existence.lean#L102), and the criteria for $G_K^{\mathrm{ab}}$ are in [GabLim.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/GabLim.lean#L155).

- `IsFrob` asks $\|g x - x^q\| < 1$ for all $x$ with $\|x\| \leq 1$, where $q$ is the order of the residue field.
- The field $K_n$ is $K$ with all roots of unity of order $q^n - 1$ adjoined.
- Steps 1 to 6 are proved with no new mathematics; the depth is in the inputs.
