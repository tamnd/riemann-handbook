---
id: low-iso2
title: A K-type that occurs in a Harish-Chandra module of GL(n, C)
kind: theorem
decl: UpperTheory.V.Z.GSp4Splitting.lowIso2
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.TraceFormula.GL4GeometricSide.PartSum
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{LowIso}$: in a module for $\mathrm{GL}_n(\mathbb{C})$ with $K = U(n)$, a $K$-type below a bound forces a given $K$-type to occur. The trace formula lemmas `global_haarAverage_trace_identity` and `Mult.Pi.global_twisted_trace_bound` take it as a hypothesis. It sits below [EveryCharacter from the Galois row](/step/every-character/). For `IsLefK` see [the core definitions](/entry/core-g/).

## Statement

Let $\lambda \in \mathbb{Z}^n$ be decreasing. Let $E$ be a finite-dimensional unitary representation of $U(n)$ with an operator $T$ such that $(E, T)$ satisfies `IsLefK` for $\lambda$. Let $V$ be an inner product space with two families $E_1(a,b)$, $E_2(a,b)$ of operators, a representation $\sigma$ of $U(n)$ and an operator $A$. Suppose (`IsLoc`):

- $E_1$, $E_2$ satisfy the relations `IsPair`, which we have not unfolded, and the Gelfand elements of each act by the scalars of the infinitesimal character of $\lambda$;
- the derivative of $\sigma$ is the $\mathfrak{k}$-action built from $E_1$, $E_2$;
- $A^2 = 1$, $A$ is an isometry, $A$ commutes with $\sigma$, and $A E_1 = E_2 A$.

Put $m_0(\lambda)_a = 2\lambda_a + (n-1) - 2a$.

**Theorem.** Suppose some $\nu \in \mathbb{R}^n$ has a nonzero $K$-highest weight space in $V$, and $m_0(\lambda) - \nu$ is a sum of positive roots $e_a - e_b$ ($a < b$) with coefficients in $\mathbb{N}$. Then there is a nonzero $U(n)$-map from the dual $\mathrm{Hom}(E, \mathbb{C})$ to $V$.

## Proof

1. $\nu$ is dominant (`irrCh`) and integral.
2. `diracW` gives an inequality of Dirac type between $\lambda$ and $\nu$ (not unfolded here). With the cone condition, `harmonic_of_norm_bound` puts $\nu$ in the finite set $\mathrm{harmSet}(\lambda)$.
3. `lefData` builds the dual $E' \cong \mathrm{Hom}(E, \mathbb{C})$ with a $\mathfrak{gl}_n$-action $F$, and gives the trace of $T'$ on the $\nu$-highest weight space of $E'$ as $2^n$ times a coefficient of a character product. For $\nu$ in $\mathrm{harmSet}(\lambda)$, `harmDom` makes this coefficient 1. A trace of $2^n \neq 0$ forces the space to be nonzero.
4. `homSurj` extends a map between the $\nu$-spaces of $E'$ and $V$ to a $\mathfrak{gl}_n$-map $t \colon E' \to V$ that hits the chosen nonzero vector. `derAt` shows that $t$ commutes with $U(n)$.

## In the Lean code

The theorem is in [PartSum.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GL4GeometricSide/PartSum.lean#L82), and $\mathrm{LowIso}$ is in [InnerEq.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GL4GeometricSide/InnerEq.lean#L127).

- The proof uses only the fields `pair`, `ch1`, `ch2` and `der` of `IsLoc`. The field `isK` and the four conditions on $A$ are never used.
- The names `GSp4Splitting`, `LowRankIsomorphism`, `GL4GeometricSide` and `lowIso2` do not describe the statement. No $\mathrm{GSp}_4$ and no $\mathrm{GL}_4$ occur; $n$ is arbitrary.
