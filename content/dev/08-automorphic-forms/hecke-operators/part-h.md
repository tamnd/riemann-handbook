---
id: part-h
title: Closed relative cochains are cohomologous to automorphic harmonic cochains
kind: theorem
decl: UpperTheory.V.Cj.partH
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ConjugateRepresentations.LocalLimitConjugates.PartH
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem proves `PartH`, a Hodge-type statement for the relative Lie algebra cochains of $\mathrm{GL}_a$ over a totally complex field. It gives a space of closed cochains, made of automorphic forms with a fixed infinitesimal character, that meets each cohomology class of compact support. The proof of [Clozel's conjugation theorem](/entry/clozel-conj-c/) uses it in the step `embed_of`. The proof here is one line: it applies `partH_of` to eight proved statements.

## Statement

Let $E$ be a totally complex number field, $a \geq 1$, and $\mathfrak{p}$ the real space of Hermitian matrices in $\mathfrak{gl}_a(E \otimes \mathbb{R})$. Let $\Xi$ be an irreducible algebraic representation of $\mathrm{GL}_a(E \otimes \mathbb{R})$ on $V = \mathbb{C}^d$. Let $A$ be the space of smooth functions on $\mathrm{GL}_a(\mathbb{A}_E)$. A $q$-cochain is a real alternating map $\omega \colon \mathfrak{p}^q \to A \otimes V$. It is *of level* if, for some open compact $U \subset \mathrm{GL}_a(\mathbb{A}_{E,f})$, it is a relative cochain ($K_\infty$-equivariant, $0$ when one argument is the identity matrix) with values in sums of $\varphi \otimes v$, $\varphi$ left $\mathrm{GL}_a(E)$-invariant and right $U$-invariant, with the central character that $\Xi$ fixes. Let $d$ be the Chevalley-Eilenberg differential for $\mathfrak{gl}_a \otimes A \otimes V$. A cochain is *exact* if it is $d\eta$ for a cochain $\eta$ of some level. It has *compact support* if it vanishes at large height.

Let $m$ assign to each embedding $t \colon E \to \mathbb{C}$ a multiset of $a$ complex numbers, such that $\Xi$ has infinitesimal character $-m(t)$ at each $t$ (`AlgInfChar`).

**Theorem.** For each $q$ there is a subspace $M$ of $q$-cochains with these properties.

1. $M$ is stable under right translation by $\mathrm{GL}_a(\mathbb{A}_{E,f})$.
2. Each $\omega \in M$ is closed and of level.
3. Each component of each value of $\omega \in M$ is an automorphic form (`IsAutForm`) with infinitesimal character $m$ (`HasChar m`).
4. The only exact element of $M$ is $0$.
5. Each closed cochain of level and of compact support is $\omega$ plus an exact cochain, for some $\omega \in M$.

So $M$ maps injectively to cohomology, and its image contains the image of the cohomology with compact support.

## Proof

`partH_of` first reduces `PartH` to `PartHss`, by `partH_of_ss` and `exactSub`. `PartHss` replaces clause 4 by: each invariant subspace of $M$ has an invariant complement. For `PartHss`, $M$ is the space of cochains with the property `IsH`: of level, closed, automorphic with infinitesimal character $m$, and with values in the span of square-integrable functions. `harmSub`, `harmSS` and `hodgeEx` give clause 1, the complements, and clause 5.

- `exactSub`: the exact cochains form an invariant subspace $B$. Then $M \cap B$ has a complement $N$ in $M$, and $N$ has clauses 1 to 5.
- `frameEx`, `oneReal`: $\mathfrak{p}$ has a frame, and $\Xi$ acts on the identity matrix by a real scalar.
- `hodgeEx`: each closed compactly supported cochain of level $U$ is a coclosed, square-integrable cochain $h$ of moderate growth plus an exact cochain of level $U$.
- `charOf`: such an $h$ has infinitesimal character $m$.
- `autOf`: a function of level with infinitesimal character $m$ and moderate growth is an automorphic form.

## In the Lean code

- The theorem is in [PartH.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/LocalLimitConjugates/PartH.lean#L10). `PartH`, `PartHss`, `ExactSub` and `partH_of_ss` are in [PartHOfSs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/PartHOfSs.lean#L45).
- `partH_of` and the statements `HodgeEx`, `HarmSub`, `HarmSS`, `CharOf`, `AutOf` are in [CasimirResolventProjection.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/LocalLimitConjugates/CasimirResolventProjection.lean#L502). `IsH` is at line 98.
- The relative cochain condition `IsRelCochain` is in [IsRelCochain.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/IsRelCochain.lean).
- All eight inputs are theorems, not hypotheses. We have not unfolded their proofs.
- For $q = 0$, "exact" means "equal to $0$", so clause 4 is empty.
