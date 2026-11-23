---
id: torsor-point-over-strict-henselisation-noetherian-normal
title: A torsor over a noetherian normal model gets a point, a second name
kind: theorem
decl: GlobalTheory.T.torsor_point_over_strictHenselisation_noetherianNormal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsorPointOverStrictHenselisationNoetherianNormStatement
covers: 541
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`torsor_point_of_essFiniteType`](/entry/torsor-point-of-ess-finite-type/), with the same statement. It is step 3 of [`keyOrigin`](/entry/key-origin/): after the torsor has moved down to a noetherian normal base, this theorem gives it a point over the generic fibre of the strict henselisation.

## Statement

In short: let $T$, $P = (\mathfrak{m}_T, X)$, $\varphi \colon T[X]_P \to O$, $O_K$ and $q$ be as in [`keyOrigin`](/entry/key-origin/). Let $A$ be a noetherian, integrally closed local domain, essentially of finite type over $\mathbb{Z}$, with an injective local map $i \colon A \to T$ and $q$ a unit in $A$. Let $E_A$ be an étale $A[X]$-algebra, $Q_A$ a prime of $E_A$ over $(\mathfrak{m}_A, X)$, and $R = (E_A)_{Q_A}$. Let $j_A \colon R \to O$ be a map over $A[X] \to T[X] \to O$, and let $\psi_A \colon R_K \to O_K$ extend $j_A$, where $R_K$ is the generic fibre of $R$ over $A$. Let $D_A$ be a $\mathbb{Z}/q$-torsor over $R_K$.

**Theorem.** There is a ring map $\sigma \colon D_A \to O_K$ that extends $\psi_A$. [The entry of the proof](/entry/torsor-point-of-ess-finite-type/) gives the statement in full.

## Proof

The proof applies `GlobalTheory.KeyOriginNoeth.torsor_point_of_essFiniteType`. The real content is in [that entry](/entry/torsor-point-of-ess-finite-type/).

## In the Lean code

The theorem is in [TorsorPointOverStrictHenselisationNoetherianNormStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorPointOverStrictHenselisationNoetherianNormStatement.lean#L8). Its statement is a copy, symbol for symbol, of the statement of `torsor_point_of_essFiniteType`. The proof is a `first` tactic that applies that theorem in one of three ways. The file imports `Mathlib` twice and raises `maxHeartbeats`.
