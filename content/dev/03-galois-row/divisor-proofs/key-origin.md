---
id: key-origin
title: Cyclic torsors at the origin, by reduction to a noetherian normal base
kind: theorem
decl: GlobalTheory.KeyOriginCut.keyOrigin
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsorTrivialStrictHenselisationOrigin
covers: 576
status: drafted
drafted_by: writer@claude
---
This theorem proves `KeyOrigin`: cyclic torsors over the generic fibre of the strict henselisation of $\mathbb{A}^1_T$ at the origin are trivial. It is restated as [the case at the origin](/entry/torsor-trivial-strict-henselisation-origin/), which feeds [the triviality of cyclic torsors on the generic fibre](/entry/torsor-trivial/). The proof moves the torsor down to a finite étale stage and then to a noetherian normal base. The point over that base comes from the next entry.

## Statement

We use the notation of [the case at the origin](/entry/torsor-trivial-strict-henselisation-origin/): $T$ is an absolutely integrally closed local domain, $P = (\mathfrak{m}_T, X)$, $\varphi \colon T[X]_P \to O$ is a strict henselisation, $O_K$ is the generic fibre of $O$ over $T$, and $q > 0$ is a unit in $T$.

**Theorem.** Every $\mathbb{Z}/q$-torsor $D$ over $O_K$ has an $O_K$-algebra map $D \to O_K$.

## Proof

For a ring $R$ over a domain $A$, write $R_K = R[(A \setminus \{0\})^{-1}]$. Three lemmas give the proof, and the rest is bookkeeping.

1. **A finite stage.** `strict_henselisation_prime_eq` gives an étale $T[X]$-algebra $E$, a prime $Q$ of $E$ over $P$, a map $j \colon E_Q \to O$ of $T[X]$-algebras, a map $\psi \colon (E_Q)_K \to O_K$ that extends $j$, and a $\mathbb{Z}/q$-torsor $D_1$ over $(E_Q)_K$. A ring map $D_1 \to O_K$ that extends $\psi$ gives an $O_K$-algebra map $D \to O_K$.
2. **A noetherian model.** `exists_noetherian_model_torsor_origin` gives a noetherian, integrally closed local domain $A$, essentially of finite type over $\mathbb{Z}$, with an injective local map $i \colon A \to T$ and $q$ a unit in $A$. It also gives an étale $A[X]$-algebra $E_A$ with a prime $Q_A$ over $(\mathfrak{m}_A, X)$, a map $j_A \colon (E_A)_{Q_A} \to O$ over $A[X] \to T[X] \to O$, a map $\psi_A$ that extends $j_A$ to generic fibres, and a $\mathbb{Z}/q$-torsor $D_A$ over $((E_A)_{Q_A})_K$. A ring map $D_A \to O_K$ that extends $\psi_A$ gives a ring map $D_1 \to O_K$ that extends $\psi$.
3. **A point over the model.** [The torsor point over a noetherian normal base](/entry/torsor-point-over-strict-henselisation-noetherian-normal/) gives a ring map $D_A \to O_K$ that extends $\psi_A$.

Then step 2 and step 1, in this order, carry the point back to $D$.

By their statements, steps 1 and 2 are limit arguments: the first passes from $O$ to one étale neighbourhood, the second from $T$ to a noetherian subring. We have not opened their proofs.

## In the Lean code

The theorem is in [TorsorTrivialStrictHenselisationOrigin.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsorTrivialStrictHenselisationOrigin.lean#L12). The lemmas it calls:

- `GlobalTheory.T.strict_henselisation_prime_eq`, an alias of `KeyOriginCut.exists_stage_torsor`.
- `GlobalTheory.T.exists_noetherian_model_torsor_origin`, an alias of `KeyOriginNoeth.exists_noetherian_model`.
- `GlobalTheory.T.torsor_point_over_strictHenselisation_noetherianNormal`.

The torsor condition here is `KeyOriginCut.IsZTorsor`. It has the same body as `LocAcyc.IsZModTorsor` in TorsorsTrivialIff.lean. The proof does not use the hypothesis $P \cap T = \mathfrak{m}_T$ of `KeyOrigin`, which follows from $P = (\mathfrak{m}_T, X)$. The name `strict_henselisation_prime_eq` does not describe its statement, which descends a torsor to a finite étale stage.
