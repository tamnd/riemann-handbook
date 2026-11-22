---
id: torsor-trivial-strict-henselisation-origin
title: Cyclic torsors are trivial at the origin, a second name
kind: theorem
decl: GlobalTheory.T.torsor_trivial_strict_henselisation_origin
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsorTrivialStrictHenselisationOriginStatement
covers: 577
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`keyOrigin`](/entry/key-origin/). It states the case at the origin of [the triviality of cyclic torsors on the generic fibre](/entry/torsor-trivial/). That theorem derives the cases of the other points from this one.

## Statement

The statement is the proposition `KeyOrigin`. Let $T$ be a local domain that is absolutely integrally closed (each monic polynomial of positive degree has a root in $T$). Let $P = (\mathfrak{m}_T, X)$ be the origin of the closed fibre of $\mathbb{A}^1_T$. Let $\varphi \colon T[X]_P \to O$ be a strict henselisation, in the sense of [the parent entry](/entry/torsor-trivial/), and let $O_K = O[(T \setminus \{0\})^{-1}]$.

**Theorem.** Let $q > 0$ be a unit in $T$. Then every $\mathbb{Z}/q$-torsor over $O_K$ has an $O_K$-algebra map to $O_K$.

`KeyOrigin` also has the hypothesis $P \cap T = \mathfrak{m}_T$. It follows from $P = (\mathfrak{m}_T, X)$.

## Proof

The proof applies `GlobalTheory.KeyOriginCut.keyOrigin`. The real content is in [`keyOrigin`](/entry/key-origin/).

## In the Lean code

The theorem is in [TorsorTrivialStrictHenselisationOriginStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorTrivialStrictHenselisationOriginStatement.lean#L7). `KeyOrigin` is defined in [TorsorsTrivial.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorsTrivial.lean#L51) as `KeyLocalWith` with the condition `P = (maximalIdeal T).map C ⊔ Ideal.span {X}`. The proof is a `first` tactic that applies `keyOrigin` in one of three ways. The file raises `maxHeartbeats` and imports `Mathlib` twice. Neither has an effect on the statement.
