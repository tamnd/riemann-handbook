---
id: torsor-trivial
title: Cyclic torsors on the generic fibre of a strictly henselian local ring of the line are trivial
kind: theorem
decl: GlobalTheory.LocAcyc.torsor_trivial
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsorTrivial
covers: 684
status: drafted
drafted_by: writer@claude
---
This theorem says that every $\mathbb{Z}/q$-torsor over the generic fibre of a strict henselisation of the affine line $\mathbb{A}^1_T$ is trivial, when $T$ is an absolutely integrally closed domain and $q$ is invertible in $T$. Its one use is in [the theorem that the Picard group of this generic fibre has no $q$-torsion](/entry/pic-localization-strict-henselisation-no-torsion/). That theorem uses a primitive $q$-th root of unity in $T$ to turn $q$-torsion line bundles into $\mathbb{Z}/q$-torsors. The branch sits below the local steps `Steps` of [the proof that GeoOne holds](/step/geo-one-holds/).

## Statement

Let $T$ be a domain that is *absolutely integrally closed*: each monic polynomial of positive degree in $T[X]$ has a root in $T$. Let $P$ be a prime of $T[X]$. Let $O$ be a local ring that is a $T[X]$-algebra, with a map $\varphi \colon T[X]_P \to O$ of $T[X]$-algebras that is a strict henselisation. In the Lean code this means: $O$ is henselian, its residue field is separably closed, $\varphi$ is local, and $\varphi$ is ind-étale. Let $O_K = O[(T \setminus \{0\})^{-1}]$ be the generic fibre of $O$ over $T$.

For a ring $B$, a *$\mathbb{Z}/q$-torsor* over $B$ is a $B$-algebra $D$ that is finite, projective and faithfully flat, with an action of $\mathbb{Z}/q$ by $B$-algebra automorphisms, such that the map $D \otimes_B D \to \prod_{g \in \mathbb{Z}/q} D$, $x \otimes y \mapsto (x \cdot g(y))_g$, is bijective. It is *trivial* if there is a $B$-algebra map $D \to B$.

**Theorem.** Let $q > 0$ be an integer that is a unit in $T$. Then every $\mathbb{Z}/q$-torsor over $O_K$ is trivial.

## Proof

The proof reduces to the case where $T$ is local and $P$ is the origin $(\mathfrak{m}_T, X)$.

1. **Localize $T$.** `torsorTrivialGenericFibre_of_strictHenselClosedFibre` (an alias of `keyAll_of_keyLocal`) replaces $T$ by $T_{\mathfrak{p}}$ with $\mathfrak{p} = P \cap T$. Then $T_{\mathfrak{p}}$ is again absolutely integrally closed, $P$ lies over its maximal ideal, and $O_K$ does not change up to isomorphism.
2. **Split on $P$.** Now $T$ is local and $P \cap T = \mathfrak{m}_T$. `keyLocal_of` splits into the case $P = \mathfrak{m}_T T[X]$ (the generic point of the closed fibre) and the case of closed points.
3. **Closed points from the origin.** `torsorTrivialClosedPoints_of_origin_closedFibre` (an alias of `keyClosedPts_of_keyOrigin`) uses that the residue field of $T$ is algebraically closed. So $P$ contains some $X - c$, and the change of variable $X \mapsto X + c$ moves $P$ to the origin.
4. **The generic point from closed points.** `keyGeneric_of_keyClosedPts` spreads the torsor out to an étale $T[X]$-algebra, finds a section at a closed point of the closed fibre, and specialises it back to $O$.
5. **The origin.** This is [the case at the origin](/entry/torsor-trivial-strict-henselisation-origin/), proved in [`keyOrigin`](/entry/key-origin/). It has the real content.

## In the Lean code

The theorem is in [TorsorTrivial.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorTrivial.lean#L20). The statement is the proposition `KeyAll` of [TorsorsTrivial.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorsTrivial.lean#L26) with `TorsorsTrivial` and `AbsIntClosed` unfolded. The generic fibre $O_K$ is `GenFib T O`. The variants `KeyLocal`, `KeyGeneric`, `KeyClosedPts` and `KeyOrigin` are `KeyLocalWith S` for four conditions $S$ on $P$, all with $T$ local and $P$ over $\mathfrak{m}_T$.

The lemmas it calls:

- `keyLocal_of`, in the same file.
- `torsorTrivialGenericFibre_of_strictHenselClosedFibre`, `torsorTrivialClosedPoints_of_origin_closedFibre` and `keyGeneric_of_keyClosedPts'`, each a one-line alias.
- `torsor_trivial_strict_henselisation_origin`.

The step from closed points to the generic point calls three lemmas (`spread_torsor_to_etale_algebra`, `exists_section_strictHenselisation_closedFibre_point`, `exists_specialisation_to_strictlyHenselian`) whose proofs we have not opened.
