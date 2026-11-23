---
id: howe-unram-holds
title: The unramified Howe statement holds
kind: theorem
decl: GlobalTheory.Hk3.howeUnram_holds
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.RhoMemOfMkEq
covers: 364
status: drafted
drafted_by: writer@claude
---
This theorem proves the proposition `HoweUnram`. That proposition is a statement about a Weil representation in its lattice model over an unramified quadratic extension of local fields. The [literature step](/step/every-character-of-literature/) passes this theorem to [the separation of functionals](/proof/bessel-seesaw/). So `HoweUnram` is not a hypothesis of the main theorem. The step [nonempty-hyps](/step/nonempty-hyps/) says the same thing.

## Statement

Let $L$ be a complete field of characteristic $0$ with a discrete valuation, and let $\sigma$ be an involution of $L$ that makes $L$ unramified over its fixed field, with odd residue characteristic. Let $J_S \in GL_n(L)$ and $J_T \in GL_{n'}(L)$ be integral hermitian matrices, with unitary groups $U(J_S)$ and $U(J_T)$. Let $\delta$ be a unit with $\sigma\delta = -\delta$, and put $\langle x, y \rangle = \delta \operatorname{tr}(J_S^{-1} (y^\sigma)^{T} J_T x)$ on $\mathrm{Mat}_{n' \times n}(L)$. Let $\rho$ be a map from $\mathrm{Mat}_{n' \times n}(L)$ to the operators on a complex vector space $M$, with $\rho(0) = 1$ and $\rho(x)\rho(y) = \psi\big((\langle x,y \rangle + \sigma\langle x,y \rangle)/2\big)\rho(x+y)$ for a character $\psi$ of $L$ that is trivial on the $\sigma$-fixed integers and not on $\varpi^{-1}$ times them. Let $\omega$ be a representation of $U(J_S) \times U(J_T)$ on $M$ with $\omega(g,h)\rho(x) = \rho(h x g^{-1})\omega(g,h)$, and suppose that integral pairs $(g,h)$ fix vacuum vectors. The record `LocPair` collects these conditions. Let $s \neq 0$ be a vacuum vector: $\rho(u)s = s$ for every integral $u$. Suppose that the vectors $\rho(x)s$ span $M$. Then:

1. every vector fixed by $\omega(g, 1)$ for all integral $g \in U(J_S)$ lies in the span of the $\omega(1, h)s$, $h \in U(J_T)$;
2. every vector fixed by $\omega(1, h)$ for all integral $h \in U(J_T)$ lies in the span of the $\omega(g, 1)s$, $g \in U(J_S)$.

## Proof

Clause 2 is [fixed-mem-span](/entry/fixed-mem-span/), which has the real argument. For clause 1, the proof uses `unramifiedLocalDualPair_swap_hermitianAdjoint`. That lemma turns the data into a `LocPair` with the roles of $J_S$ and $J_T$ exchanged: $\delta$ becomes $-\delta$, and $\rho$ is replaced by $X \mapsto \rho(J_T^{-1} (X^\sigma)^{T} J_S)$. The vacuum vector and the span condition carry over. Then fixed-mem-span for the swapped data gives clause 1.

## In the Lean code

The theorem is in [RhoMemOfMkEq.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L250). The statement is [HoweUnram.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisGeometry₂/HoweUnram.lean#L8), and the record is [`LocPair`](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/NormalFam.lean#L166). The swap lemma is proved by `HoweSwap.locPair_swap`; we read its statement only.

`HoweUnram` sits in a folder named PublishedTheorems, but the code proves it. Some other entries, for example [scalars-of-given-all](/entry/scalars-of-given-all/), still take it as a hypothesis.
