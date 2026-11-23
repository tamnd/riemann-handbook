---
id: g-tlower-of
title: The integral branching maps, given the integral duality of Weyl modules
kind: theorem
decl: gTLower_of
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.GTLower
covers: 700
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTLower`: for interlacing dominant weights of $\mathrm{GL}_N$ and $\mathrm{GL}_{N-1}$, there are branching maps between the polynomial models of the two representations that are equivariant, integral and bounded in the Fock norm. It is a pass-through. It takes one hypothesis and hands it, with three proved theorems, to [`PI.WGL.gTLower_of`](/entry/wgl-g-tlower-of/), which has the real content and states `GTLower` in full. Its caller [`branching_interlacing_pairs`](/entry/branching-interlacing-pairs/) supplies the hypothesis.

## Statement

For a dominant weight $\lambda$ of $\mathrm{GL}_N$, let $\nabla_R(\lambda)$ and $\Delta_R(\lambda)$ be the two $R$-submodules of $R[x_{ij}]_{1 \leq i,j \leq N}$ that the code calls `nablaSq` and `delSq`. Let $\langle \cdot, \cdot \rangle_\lambda$ be the Fock pairing $\langle f, g \rangle = \sum_m f_m \overline{g_m} \, m!$ over monomials $m$, with $m! = \prod_k m_k!$, divided by its value on the extremal vector of $\lambda$.

`FactDelDualNabla` says: for $f \in \nabla_{\mathbb Q}(\lambda)$, the pairing $\langle f, g \rangle_\lambda$ is an integer for every $g \in \nabla_{\mathbb Z}(\lambda)$ if and only if $f$ comes from $\Delta_{\mathbb Z}(\lambda)$. In other words, $\Delta_{\mathbb Z}(\lambda)$ is the dual lattice of $\nabla_{\mathbb Z}(\lambda)$.

**Theorem.** `FactDelDualNabla` implies `GTLower`.

## Proof

The proof is one line:

```
PI.WGL.gTLower_of h2 highest_weight_irreducible gelfand_tsetlin_branching schur_fock
```

The three theorems prove `HwIrred` (irreducibility and the highest weight line), `GTBranch` (the Gelfand-Tsetlin branching rule) and `SchurFock` (a Fock norm bound).

## In the Lean code

The theorem is in [GTLower.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/GTLower.lean#L7), in the root namespace. `FactDelDualNabla` is in [DataCoeff.lean](lean:Formalism/LocalRingCardinality/DataCoeff.lean#L126), and `GTLower` in [GTLower.lean](lean:Formalism/PeriodIntegrals/GTLower.lean#L10).

The hypothesis is proved in the code: [`branching_interlacing_pairs`](lean:Formalism/LocalToGlobal/Divisibility/BrJoint.lean#L13) passes `factDelDualNabla`. This theorem and `PI.WGL.gTLower_of` have the same short name.
