---
id: finite-h-step
title: Finite cohomology on a proper scheme, the inductive step
kind: theorem
decl: GroundTheory.Arith.SchemeCoh.finiteH_step
module: GroundTheory.ArithmeticGeometry.SchemeCohomology.ProperCohomology.FinitenessStep
covers: 668
status: drafted
drafted_by: writer@claude
---
This theorem is the inductive step in the proof that coherent cohomology on a proper scheme is finite, and holds all its mathematics. Its parent, [`finiteH_of_supportedIn`](/entry/finite-h-of-supported-in/), runs the induction. It lies below [EveryCharacter](/step/every-character/).

## Statement

Let $A$ be a Noetherian ring and let $X$ be a scheme with a proper morphism $X \to \operatorname{Spec} A$. For a sheaf $\mathcal{F}$ of $\mathcal{O}_X$-modules, say that $\mathcal{F}$ has *finite cohomology* if $H^p(X, \mathcal{F})$ is a finitely generated $A$-module for each $p \geq 0$. Here $H^p$ is Mathlib's `Sheaf.H` of the underlying abelian sheaf, with $A$ acting through $\Gamma(X, \mathcal{O}_X)$. Say that $\mathcal{F}$ is *supported in* a set $T$ if every section of $\mathcal{F}$ over an open set disjoint from $T$ is zero.

**Theorem.** Let $T \subseteq X$ be closed. Suppose that every coherent sheaf supported in a closed set $T' \subsetneq T$ has finite cohomology. Then every coherent sheaf supported in $T$ has finite cohomology.

With the induction, this gives the finiteness theorem of Grothendieck (EGA III$_1$, Théorème 3.2.1).

## Proof

Let $\mathcal{F}$ be coherent and supported in $T$.

1. **Reduction to an integral piece.** Let $j \colon Z \to X$ be the closed subscheme cut out by the annihilator of $\mathcal{F}$. Then $|Z| \subseteq T$ and $\mathcal{F} \cong j_* \mathcal{G}$ with $\mathcal{G}$ coherent (`exists_pushforward_iso_of_supportedIn`). If $|Z| \neq T$, the hypothesis applies; if $Z = \emptyset$, $\mathcal{F} = 0$. Otherwise take an irreducible component $c \colon Z_1 \to Z$ and a nonempty open $O \subseteq Z$ over which $c$ is an isomorphism (`exists_irreducible_isIso_restrict`).
2. **Chow's lemma.** There are a closed immersion $i \colon Z' \to \mathbb{P}^N_A$ and a morphism $\pi \colon Z' \to Z_1$ over $A$ that is an isomorphism over a nonempty open $U_1$ (`exists_chow`). Put $\psi = j \circ c \circ \pi \colon Z' \to X$ and $\mathcal{G}' = \psi^* \mathcal{F}$.
3. **The comparison map.** For $n$ large, $\psi_*(\mathcal{G}'(n))$ is coherent and has the same cohomology as $\mathcal{G}'(n)$ on $Z'$ (`ProjScheme.exists_relativeSerre`), which is finite by the projective case (`ProjScheme.finite_H`). Also $\mathcal{O}(n)$ is globally generated, so a global section $s$ generates it near a point $y$ over $U_1 \cap c^{-1}(O)$. Let $\alpha \colon \mathcal{F} \to \psi_* \psi^* \mathcal{F} \to \psi_*(\mathcal{G}'(n))$ be the unit of adjunction followed by multiplication by $s$.
4. **An isomorphism on an open set.** There is an open $W \ni \psi(y)$ over which $\psi$ is a closed immersion, the unit is bijective (`bijective_unit_app_of_le`, since $\mathcal{F}$ comes from $Z$) and multiplication by $s$ is bijective. So $\alpha$ is an isomorphism over $W$.
5. **Induction.** $\ker \alpha$ and $\operatorname{coker} \alpha$ are coherent and supported in $T \setminus W$ (`kernel_supportedIn`, `cokernel_supportedIn`), which is strictly smaller than $T$ because $\psi(y) \in T \cap W$. So both have finite cohomology.
6. **Long exact sequences.** Since $A$ is Noetherian, the sequences $0 \to \ker \alpha \to \mathcal{F} \to \operatorname{im} \alpha \to 0$ and $0 \to \operatorname{im} \alpha \to \psi_*(\mathcal{G}'(n)) \to \operatorname{coker} \alpha \to 0$ give finite cohomology for $\operatorname{im} \alpha$ and then for $\mathcal{F}$ (`FiniteH.of_shortExact₁`, `FiniteH.of_shortExact₂`).

## In the Lean code

The theorem is in [FinitenessStep.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperCohomology/FinitenessStep.lean#L40). The parent supplies the hypothesis `IH` by well-founded induction on the closed sets of the Noetherian space $X$. The lemmas named above are in the same folder, except `ProjScheme.finite_H` in ProjectiveCohomology.

We have not opened the proofs of Chow's lemma or of the relative Serre vanishing. The open set $W$ is the complement of the images of three closed sets, and about 80 lines check its properties. The rest is bookkeeping.
