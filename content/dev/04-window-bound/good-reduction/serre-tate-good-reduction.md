---
id: serre-tate-good-reduction
title: The theorems of Serre and Tate on good reduction
kind: theorem
decl: UpperTheory.Lit.serreTateGoodReduction
module: Development.AutomorphicArithmetic.ThetaCorrespondence.GoodReduction.SerreTate
covers: 489
status: drafted
drafted_by: writer@claude
---
This theorem proves `SerreTateGoodReductionSt`, the field `st` of the structure that [the CM and abelian variety inputs](/step/cm-abelian-inputs-from-literature/) fill. It has no hypothesis. The statement is the conjunction of three results of Serre and Tate on the reduction of [[abelian varieties|R7W03TXRS9]] (J.-P. Serre and J. Tate, Good reduction of abelian varieties, Ann. of Math. 88, 1968): the criterion of Néron, Ogg and Shafarevich, the criterion for potential good reduction, and potential good reduction for complex multiplication.

## Statement

Let $R$ be a discrete valuation ring with fraction field $K$ and residue field $k$. Let $\Omega$ be a separable closure of $K$, let $V$ be a valuation ring of $\Omega$ above $R$, and let $I \subset \mathrm{Gal}(\Omega/K)$ be its inertia group. Let $A$ be an abelian variety over $K$: a smooth, proper, geometrically connected commutative group scheme over $\operatorname{Spec} K$ (see [abelian varieties and abelian schemes](/learn/elliptic-curves/#abelian-varieties-and-abelian-schemes)).

- $A$ has *good reduction* if there is an [[abelian scheme|JDDXZ89N33]] $G$ over $R$ whose generic fibre is isomorphic to $A$ as a group.
- $A$ has *potential good reduction* if there are a finite extension $L/K$ and a discrete valuation ring $W$ of $L$ above $R$ such that $A_L$ has good reduction over $W$.
- The $m$-torsion is *unramified* if $I$ fixes each point $x \in A(\Omega)$ with $mx = 0$. The [[Tate module|4CSMQFTGD8]] $T_\ell(A)$ is *unramified* if $I$ acts trivially on it.

**Theorem.** The following three statements hold.

1. (Néron, Ogg, Shafarevich.) Suppose that $k$ is perfect. Then these are equivalent: $A$ has good reduction; the $m$-torsion is unramified for each $m$ with $m \neq 0$ in $k$; it is unramified for infinitely many such $m$; $T_\ell(A)$ is unramified for some prime $\ell$ with $\ell \neq 0$ in $k$.
2. Suppose that $k$ is perfect and that $\ell$ is a prime with $\ell \neq 0$ in $k$. Then $A$ has potential good reduction if and only if the image of $I$ in $\operatorname{Aut} T_\ell(A)$ is finite.
3. Suppose that $k$ is finite. Let $F$ be a number field with $[F:\mathbb{Q}] = 2\dim A$, and suppose that a ring $O$ with fraction field $F$ acts on $A$ by group endomorphisms. Then $A$ has potential good reduction.

## Proof

The proof is a triple of three theorems.

1. [`neronOggShafarevich`](/entry/lit-neron-ogg-shafarevich/) gives the first statement.
2. `potentialGoodReduction` gives the second. It applies `potentialGoodReduction_of_neronOggShafarevich` to the first statement. That theorem pairs two lemmas, one for each direction, whose proofs we have not unfolded.
3. `cmPotentialGoodReduction` gives the third, by `cmPotentialGoodReduction_of_nos` applied to the first statement. That proof takes a prime $\ell$ that is nonzero in $k$. It uses the facts that the Galois action on $T_\ell(A)$ commutes with $O$, that the image of inertia has bounded exponent when $k$ is finite, and that $A[\ell^2](\Omega)$ is finite. It concludes that the image of inertia is finite and applies the second statement.

## In the Lean code

The theorem is in [SerreTate.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/SerreTate.lean#L15). The three statements and the definitions `HasGoodReduction`, `HasPotentialGoodReduction`, `TorsionUnramified`, `TateUnramified` and `HasCMBy` are in [TateUnramifiedOfTorsionUnramified.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/TateUnramifiedOfTorsionUnramified.lean#L108). `cmPotentialGoodReduction_of_nos` is in [CMGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/CMGood.lean#L18).

The first two statements assume that $k$ is perfect; the proof uses this to make the residue field of the maximal unramified extension algebraically closed (see [the last step of the criterion](/entry/has-good-reduction-of-infinite-torsion-unramified/)). In `HasCMBy`, the action of $O$ is a ring map to the endomorphisms of $A$ (the structure `OAct`); it is not required to be injective, and $F$ is not required to be a CM field.
