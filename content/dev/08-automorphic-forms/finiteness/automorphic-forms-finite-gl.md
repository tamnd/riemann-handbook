---
id: automorphic-forms-finite-gl
title: Finiteness of automorphic forms on GL(a) over a totally complex field
kind: theorem
decl: GlobalTheory.automorphicFormsFiniteGL
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AutomorphicFormsFiniteGL
covers: 720
status: drafted
drafted_by: writer@claude
---
This theorem is Harish-Chandra's finiteness theorem for $\mathrm{GL}_a$ over a totally complex number field: the automorphic forms with a fixed level, a fixed $K_\infty$-type and fixed eigenvalues of the center of the enveloping algebra form a finite-dimensional space. It has 39 direct users in the Lean code, for example the Schur lemma for cuspidal representations, the rapid decay of cusp forms, and several files on Satake parameters. Their common dominator is the step [EveryCharacter](/step/every-character/). The real proof is in [the core statement](/entry/harish-chandra-finiteness-totally-complex-gl-proof/) and [the case of one eigencharacter](/entry/finite-dimensional-single/).

## Statement

Let $E$ be a totally complex number field, $\mathbb{A}_E$ its adeles, $\mathbb{A}_{E,f}$ its finite adeles, and $E_\infty = \prod_{v \mid \infty} \mathbb{C}$. Let $a \geq 0$ and $K_\infty = \mathrm{U}(a)(E_\infty)$, the unitary matrices with entries in $E_\infty$. Let $\mathrm{Sm}$ be the space of functions $\varphi$ on $\mathrm{GL}_a(\mathbb{A}_E)$ such that $y \mapsto \varphi(g y)$ is smooth on $\mathrm{GL}_a(E_\infty)$ for each $g$. An *automorphic form* (`IsAutForm`) is a $\varphi \in \mathrm{Sm}$ that is left invariant under $\mathrm{GL}_a(E)$, fixed by an open subgroup of $\mathrm{GL}_a(\mathbb{A}_{E,f})$, $K_\infty$-finite, finite under the algebra $\mathcal{Z}$ below, and of moderate growth: $|\varphi(g y)| \leq C (1 + \|y\| + \|y^{-1}\|)^N$.

For each complex embedding $\tau$ of $E$ and $u \in \mathbb{C}$, `cap τ u` is an operator on $\mathrm{Sm}$: a Capelli-type determinant in the derivatives $E^\tau_{ij}$ along $\tau$, shifted by $u + \tfrac{a-1}{2}$. It commutes with all $E^\tau_{ij}$ (`cap_comm`). Let $\mathcal{Z}$ (`Zalg`) be the algebra that these operators generate.

**Theorem.** Let $L \subseteq \mathrm{GL}_a(\mathbb{A}_{E,f})$ be an open subgroup, $\rho$ a continuous representation of $K_\infty$ on a finite-dimensional space $W$, and $c(\tau, u)$ any complex numbers. Let $\mathcal{F}$ be the set of automorphic forms $\varphi$ such that $\varphi$ is fixed by $L$, for each $g$ the function $k \mapsto \varphi(g k)$ on $K_\infty$ is in the span of the matrix coefficients of $\rho$, and $\operatorname{cap}_\tau(u)\,\varphi = c(\tau, u)\,\varphi$ for all $\tau, u$. Then the span of $\mathcal{F}$ has finite dimension.

This is Harish-Chandra's theorem (Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Springer 1968), in the adelic form for $\mathrm{GL}_a$.

## Proof

Apply `harishChandra_finiteness_automorphic_GL_of_eigen` to [`harishChandraFinitenessTotallyComplexGL_proof`](/entry/harish-chandra-finiteness-totally-complex-gl-proof/). The first is `automorphicFormsFiniteGL_of_core`: it deduces the theorem from `CoreFiniteGL`. Each $z \in \mathcal{Z}$ acts by one scalar $\chi(z)$ on all $\varphi$ with the eigenvalues $c$ (`center_acts_by_scalar_on_eigenforms`). Thus $\mathcal{F}$ lies in the set `formsGL` with $W$ the matrix coefficient span of $\rho$ (finite-dimensional by `finiteDimensional_matrixCoefficientSpan`), the one eigencharacter $\chi$, and order $N = 1$. `CoreFiniteGL` says that this set spans a finite-dimensional space.

## In the Lean code

The theorem is in [AutomorphicFormsFiniteGL.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AutomorphicFormsFiniteGL.lean#L8). The statement `AutomorphicFormsFiniteGL` is in [ExistsSpanFormsNeBot.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsSpanFormsNeBot.lean#L23). The reduction is in [HarishChandraFinitenessAutomorphicGLOfEigen.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarishChandraFinitenessAutomorphicGLOfEigen.lean#L13).

- The hypothesis that $\rho$ is continuous (`AutFin.IsContRep ρ`) is not used: the reduction introduces it as `_`.
- $L$ need only be open, not compact. This is harmless, since an open subgroup contains a compact open one.
- We have not unfolded `qdet`, the determinant that defines `cap`.
