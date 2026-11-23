---
id: final
title: The Frobenius relation from the comparison data
kind: theorem
decl: UpperTheory.Ru.crystallineComparison.final
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.QuasiCompactOfProj
covers: 724
status: drafted
drafted_by: writer@claude
---
This theorem is the last step of [the reduction of `FinAll`](/entry/fin-all-of/). It unpacks the comparison data `CIn`, builds the two key inputs `InjE` and `AbsInv`, and checks two finiteness conditions on the model. Then it calls [the comparison theorem `top`](/entry/crystalline-comparison-top/), which has the real proof of the relation.

## Statement

**Theorem.** `Final` holds. `Final` is `FinAll` with three more hypotheses: a residue datum $r$, the identity $x^{\ell^f} = x$ on its field $k$, and `CIn l K r f`. The conclusion is the same: for each period datum $B_0$ there is $N$ with
$$\sum_{i=0}^{n} (-1)^i (\ell^f)^{\binom{i}{2}} \, (A_i \otimes \varphi^{f(n-i+N)})\, x = 0$$
for each Galois-invariant $x$ in $V \otimes B_0$.

## Proof

1. Unpack `CIn`: line data `Amp`, an integer $N$ with $f \mid N$, a datum `F`, the period facts, `EtSide`, the laws, maps `BMap` and `PMap`, a Teichmüller congruence, and `Pin` and `BIn` for each smooth model.
2. `etMap` gives an étale comparison family $e$ with `e.Good`. `ePin` glues it into a map $e'$ on limits. `pbIota` gives an injective ring map $\iota$ from $B_0$ to the period ring, compatible with Galois.
3. `injOf` gives `InjE`: if the image of a vector under $e$ is killed by a power of $t$ in each degree, then the vector in $V \otimes B_0$ is zero.
4. `absInvOf`, with `pbInv`, gives `AbsInv`. It uses $x^{\ell^f} = x$, $f \mid N$, the Teichmüller congruence, `Pin` and `BIn`. It gives a map $g$ with $g(\varpi) = 0$, a Frobenius $F$ and a map $\rho$. For each invariant vector there is a class $y$ with $\varphi^f(y) = F^*(y)$ such that $\ell^a t^u \, e(\varphi^{fN} c) = t^{u+r} \rho^*(y)$ in each degree. Here $c$ are the coefficients of the vector.
5. `M.Sm` gives that $M \to \operatorname{Spec} \mathcal{O}_K$ is projective and smooth. Projective gives quasi-compact (`quasiCompact_of_proj`, through properness) and `AffFin` (`affFin_of`).
6. Apply `top`.

## In the Lean code

- The theorem is in [QuasiCompactOfProj.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/QuasiCompactOfProj.lean#L26). `Final` and `CIn` are in [Final.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/Final.lean#L20). `Top`, `InjE` and `AbsInv` are in [VecZero.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/VecZero.lean#L87).
- Every field of `CIn` is used. The integer $N$ of `CIn` is not the $N$ of the conclusion. That one comes from `top`.
- `Top` does not ask for `FiniteDimensional ℚ_[l] K`, but `pbInv` does.
- The file name refers to the private helper `quasiCompact_of_proj`, not to `final`. The name `final` does not describe the statement.
- We have not unfolded `injOf`, `absInvOf`, `ePin` or `PtId`.
