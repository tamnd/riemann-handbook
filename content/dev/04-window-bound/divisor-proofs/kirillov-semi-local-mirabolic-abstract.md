---
id: kirillov-semi-local-mirabolic-abstract
title: The abstract semi-local Kirillov statement for a space of Whittaker-type functions
kind: theorem
decl: GlobalTheory.T.kirillov_semiLocal_mirabolic_abstract
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemiLocalMirabolicAbstractStatement
covers: 310
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the semi-local Kirillov statement on the mirabolic subgroup](/entry/kirillov-semi-local/), which has the real content. [The assembly for a cuspidal vector](/entry/kirillov-semilocal/) applies it to a space of Whittaker functions of a cusp form.

## Statement

The statement of [the semi-local Kirillov statement](/entry/kirillov-semi-local/), word for word. In short: let $b$ satisfy conditions 1 to 4 of [the bump theorem](/entry/kirillov-semilocal-bump/). Let $\mathcal{W}$ be a complex vector space of functions on $\mathrm{GL}_{m+1}(\mathbb{A})$ whose elements transform by $\psi_N$ on the left, are right invariant under an open subgroup at the finite places, and have moderate growth at infinity. Suppose $\mathcal{W}$ is stable under right translation by $G_S$ and under the archimedean kernel operators of rapid decay.

**Theorem.** If some $W_0 \in \mathcal{W}$ is not zero at some point of $P_S$, then some $W \in \mathcal{W}$ equals $b$ on $P_S$.

No representation and no irreducibility appear in the hypotheses. One function that is not zero on $P_S$ is enough.

## Proof

The proof is `exact MirSemi.kirillov_semiLocal`. See [the semi-local Kirillov statement](/entry/kirillov-semi-local/).

## In the Lean code

The theorem is in [KirillovSemiLocalMirabolicAbstractStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemiLocalMirabolicAbstractStatement.lean#L8). The proof is a `first` combinator around `exact`. Its target `MirSemi.kirillov_semiLocal` and the user `MirSemi.kirillov_semilocal` are in the same namespace, and their names differ only in the case of one letter.
