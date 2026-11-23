---
id: pic-localization-strict-henselisation-no-torsion
title: No q-torsion in the Picard group of the generic fibre of a strict henselisation of the line
kind: theorem
decl: GlobalTheory.pic_localization_strictHenselisation_no_torsion
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.PicLocalizationStrictHenselisationNoTorsion
covers: 764
status: drafted
drafted_by: writer@claude
---
This theorem proves that the Picard group of $O_K$, the generic fibre over $T$ of a strict henselisation $O$ of $T[x]$, has no $q$-torsion. It reduces the statement to Kummer theory: a $q$-th root of unity in $T$, and a section of each $\mathbb{Z}/q$-torsor over $O_K$. The sections come from [torsor_trivial](/entry/torsor-trivial/), which has the main content. Its user is [the case of quotients](/entry/pic-generic-fibre-quotient-strict-henselisation-no-torsion/), for the quotient $A = O$. Below this theorem are 764 declarations; 684 of them are below `torsor_trivial`.

## Statement

Let $T$ be a local domain in which each monic polynomial of positive degree has a root, and let $q \geq 1$ be invertible in $T$. Let $O$ be a henselian local $T[x]$-algebra with separably closed residue field. Suppose that $O$ is the union of a directed family of $T[x]$-subalgebras, each isomorphic to the localization at a prime of an étale $T[x]$-algebra. Let $O_K$ be the localization of $O$ at the image of $T \setminus \{0\}$.

**Theorem.** If $c \in \operatorname{Pic} O_K$ and $c^q = 1$, then $c = 1$.

## Proof

1. `isStrictHenselisation_of_directed_union` gives a prime $P$ of $T[x]$ and a map $\varphi \colon T[x]_P \to O$ of $T[x]$-algebras that is a strict henselisation.
2. `exists_pow_eq_one_isUnit_one_sub_pow` gives $\zeta \in T$ with $\zeta^q = 1$ and $1 - \zeta^k$ a unit for $0 < k < q$. Its image in $O_K$ has the same properties.
3. `picard_torsion_trivial_of_torsors_have_sections` is the Kummer step. Let $B$ be a ring in which $q$ is a unit and which has such a $\zeta$. Call a $\mathbb{Z}/q$-*torsor* over $B$ a finite, projective, faithfully flat $B$-algebra $D$ with an action of $\mathbb{Z}/q$ such that the map $D \otimes_B D \to \prod_{g \in \mathbb{Z}/q} D$, $x \otimes y \mapsto (x \cdot g(y))_g$, is bijective. If each such $D$ has a $B$-algebra map $D \to B$, then $\operatorname{Pic} B$ has no $q$-torsion. We take $B = O_K$.
4. [torsor_trivial](/entry/torsor-trivial/) gives the map $D \to O_K$ for each torsor, from $P$, $\varphi$ and step 1.

There is no other step.

## In the Lean code

The theorem is in [PicLocalizationStrictHenselisationNoTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicLocalizationStrictHenselisationNoTorsion.lean#L12). The lemmas:

- `GlobalTheory.StrictHensUnion.isStrictHenselisation_of_directed_union`, in [IsStrictHenselisationOfDirectedUnion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsStrictHenselisationOfDirectedUnion.lean#L195);
- `GlobalTheory.exists_pow_eq_one_isUnit_one_sub_pow`, in [ExistsPowEqOneIsUnitOneSubPow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPowEqOneIsUnitOneSubPow.lean#L5);
- `GlobalTheory.T.picard_torsion_trivial_of_torsors_have_sections`, a second name for `GlobalTheory.KummerStep.kummer_step`, which we have not opened;
- `GlobalTheory.LocAcyc.torsor_trivial`, in [TorsorTrivial.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorTrivial.lean#L20).

The hypotheses have three small oddities. The hypothesis `IsDomain T ∧ AIC` repeats the instance `[IsDomain T]`; only its second part is used. The condition $q > 0$ is a separate hypothesis, where the nearby lemmas use `[NeZero q]`. Inside the hypothesis on $O$, the prime ideal of the étale algebra is also named `q`, which hides the integer $q$.
