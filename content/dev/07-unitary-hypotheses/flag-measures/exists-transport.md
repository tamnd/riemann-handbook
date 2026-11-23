---
id: exists-transport
title: A transport from a Hida setting to each form, with matching level
kind: theorem
decl: GlobalTheory.St.SpectralData.exists_transport
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsGlobalSetting
covers: 467
status: drafted
drafted_by: writer@claude
---
This lemma builds, for a Hida setting $X$ of a datum $D$ and a word $u$, a transport of $X$ to the given form $F(u)$ with matching lattice and level. [`exists_setting`](/entry/exists-setting/) calls it with the identity isomorphism of adele rings for its property 5. It assembles five existence results.

## Statement

Let $D$ be a datum with hermitian space $V$ over the CM field $E$, $F(u)$ the form `Forms0 D u` for each word $u$, and $X$ a Hida setting for $D$.

A *transport* of $X$ to $F(u)$ (`Transport`) consists of:

1. an isometry $w$ of $V$ that maps the hyperbolic frame and the vector $z_u$ of $X$ to those of $D$;
2. a ring isomorphism $\iota_A$ from $E \otimes \mathbb{A}_{F,f}$ for $X$ to that for $D$, compatible with $E$ and the integral adeles;
3. a finite adelic point $h_0$ of the unitary group of $D$, and for each class $c$ an element $h_c$ of the finite group of $X$ that represents $y_c h_0^{-1}$, with $y_c$ the element of $F(u)$ at $c$;
4. an equivariant conjugate-linear map $J$ from the representation space of $X$ at $u$ to functions on frames, isometric for the inner product of $D$ and $F(u)$.

`LevelMatch` says: $x$ lies in the lattice of $F(u)$ after $h_0^{-1}$ if and only if its image under $w$ and $\iota_A^{-1}$ lies in the lattice of $X$; and for corresponding $h$ and $y$, $h$ lies in the level group of $X$ if and only if $h_0^{-1} y h_0$ lies in that of $F(u)$, with equal level characters.

**Lemma.** Assume that the level set $K_2$ of $X$ is a subgroup with a unitary character (`LevelSubgroupCharacter`), and that some $\iota_A$ as in 2 exists. Then for each word $u$ there is a transport $T$ of $X$ to $F(u)$ with `LevelMatch X T`.

## Proof

1. `wittExists` gives $w$.
2. With $\iota_A$ from the hypothesis, `genusMatch_holds` gives a point $g_0$ for which the lattices match.
3. `levelConj_holds` replaces $g_0$ by a point $h_0$ for which the lattices, the level groups and the characters match. Only this step uses the hypothesis on $K_2$.
4. `hcExists_all` gives the representatives $h_c$.
5. `jExists_all` gives $J$.

## In the Lean code

The lemma is in [ExistsGlobalSetting.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsGlobalSetting.lean#L32). `Transport` and `LevelMatch` are in [ColDict.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ColDict.lean#L57). `WittExists`, `GenusMatch`, `LevelConj`, `HcExists` and `JExists` are in [LevelMatchIff.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LevelMatchIff.lean#L71).

The lemma holds for every Hida setting with an adele isomorphism. It does not use the measures of $X$ or the hypotheses of `exists_setting`. The point $g_0$ of step 2 is dropped after step 3.
