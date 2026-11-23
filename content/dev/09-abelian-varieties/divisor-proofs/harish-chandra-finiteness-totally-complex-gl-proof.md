---
id: harish-chandra-finiteness-totally-complex-gl-proof
title: The core finiteness statement for GL(a), by induction on a
kind: theorem
decl: GlobalTheory.T.harishChandraFinitenessTotallyComplexGL_proof
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HarishChandraFinitenessTotallyComplexGLProofStatement
covers: 712
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for `HCFGL.coreFiniteGL`. It gives [the finiteness of automorphic forms on GL(a)](/entry/automorphic-forms-finite-gl/). The real content is in [the case of one eigencharacter](/entry/finite-dimensional-single/).

## Statement

We use the notation of [the parent entry](/entry/automorphic-forms-finite-gl/). Let $\chi$ be a function from operators on $\mathrm{Sm}$ to $\mathbb{C}$, and $N \geq 0$. Say that $\varphi$ is a *generalized eigenvector of order $N$* for $\chi$ (`CentralNilGL`) if
$$(z_1 - \chi(z_1)) \cdots (z_N - \chi(z_N))\,\varphi = 0 \quad \text{for all } z_1, \dots, z_N \in \mathcal{Z}.$$
For an open subgroup $L \subseteq \mathrm{GL}_a(\mathbb{A}_{E,f})$, a finite-dimensional space $W$ of functions on $K_\infty$, and a set $X$ of such functions $\chi$, let $\mathcal{F}(L, W, X, N)$ (`formsGL`) be the set of automorphic forms $\varphi$ that are fixed by $L$, have $k \mapsto \varphi(g k)$ in $W$ for each $g$, and are generalized eigenvectors of order $N$ for some $\chi \in X$.

**Theorem** (`CoreFiniteGL`). For each totally complex $E$, each $a$, $L$ and $W$ as above, each finite set $X$ and each $N$, the span of $\mathcal{F}(L, W, X, N)$ has finite dimension.

## Proof

The proof is `HCFGL.coreFiniteGL`, an induction on $a$ that sums [the case of one eigencharacter](/entry/finite-dimensional-single/) over $\chi \in X$.

## In the Lean code

The theorem is in [HarishChandraFinitenessTotallyComplexGLProofStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarishChandraFinitenessTotallyComplexGLProofStatement.lean#L4). `CoreFiniteGL` and `formsGL` are in [CentralNilGL.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CentralNilGL.lean#L23), and `coreFiniteGL` is in [HarishChandraFinitenessTotallyComplexGLProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarishChandraFinitenessTotallyComplexGLProof.lean#L35).

The proof is a `first | … ` tactic. Its first branch, `exact @coreFiniteGL`, closes the goal. The later branches name `finiteDimensional_single`, whose type is different, so they never run.
