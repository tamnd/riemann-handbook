---
id: fin-all-of
title: The Frobenius relation follows from the comparison inputs
kind: theorem
decl: UpperTheory.Ru.crystallineComparison.finAll_of
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.FinAllOf
covers: 726
status: drafted
drafted_by: writer@claude
---
This theorem is the reduction step inside [the proof of `FinAll`](/entry/fin-all/). It chooses a residue datum $r$ and proves that the Frobenius $x \mapsto x^{\ell^f}$ is the identity on its field. Then it passes everything to [the theorem `final`](/entry/final/). The main argument is in `final` and in [the comparison theorem](/entry/crystalline-comparison-top/).

## Statement

**Theorem.** Assume that `CIn l K r f` holds for each prime $\ell$, each finite extension $K$ of $\mathbb{Q}_\ell$, each residue datum $r$ for $K$ and each $f > 0$. Then `FinAll` holds.

A residue datum `Res l K` is a perfect field $k$ of characteristic $\ell$, a surjective ring map $\rho \colon \mathcal{O}_K \to k$, and a ring map $s$ from $k$ to the ring `Ob l`. The condition is that the untilt of $s(\rho(x))$ is at distance less than $1$ from $x$, for each $x \in \mathcal{O}_K$.

## Proof

Fix the data of `FinAll`. The residue field of $\mathcal{O}_K$ has $\ell^f$ elements.

1. `resEx` gives a residue datum $r$.
2. The kernel of $\rho$ is a maximal ideal, because $\rho$ is surjective. $\mathcal{O}_K$ is local, so this kernel is the maximal ideal.
3. So $k$ is isomorphic to the residue field of $\mathcal{O}_K$, and $|k| = \ell^f$. In particular $k$ is finite.
4. For a finite field, $x^{|k|} = x$ (`FiniteField.pow_card`). So $x^{\ell^f} = x$ for all $x \in k$.
5. Apply `final` to $r$, to this identity and to `CIn l K r f`.

## In the Lean code

- The theorem is in [FinAllOf.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/FinAllOf.lean#L11). `Res` is in [IsUnitWitt.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/IsUnitWitt.lean#L15).
- The only real step is the identity $x^{\ell^f} = x$ on $k$. The rest passes hypotheses to `final`.
- The hypothesis is stronger than needed. It asks for `CIn` for every residue datum, but the proof uses it only for the one datum from `resEx`.
- We have not unfolded `resEx`.
