---
id: unitary-siegel-domain-exists
title: A Siegel set covers the adelic unitary group, statement form
kind: theorem
decl: GlobalTheory.T.unitary_siegel_domain_exists
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.UnitarySiegelDomainExistsStatement
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the covering by a Siegel set](/entry/cov-main/), which has the proof. Its only user is [the Siegel core for unitary groups](/entry/siegel-core/).

## Statement

Let $E/F$ be a CM extension of number fields with complex conjugation $\sigma$. Let $J$ be a nondegenerate Hermitian $n \times n$ matrix over $E$, and $G = U_J(\mathbb A_F)$ its adelic unitary group. Let $X$, $Y$ be a Witt frame of rank $r$: $X^* J X = 0$, $Y^* J Y = 0$, $X^* J Y = 1$, and $J$ is anisotropic on the vectors orthogonal to $X$ and $Y$. Let $P_0$ be the stabiliser in $G$ of the flag of $X$, and $P_0^1$ its elements whose diagonal entries on that flag have adelic absolute value 1.

For $c > 0$ let the cone be the $t \in \mathbb R_{>0}^r$ with $c\, t_{i+1} \le t_i$ and $c \le t_r$. Let $a(t)$ be an archimedean torus element: it acts by $t$ on $X$, by $t^{-1}$ on $Y$, and trivially on the rest.

**Theorem.** Let $K \subseteq G$ be a compact subgroup with $G = P_0 K$. Assume that $K$ is in good position: each element of $P_0 \cap K$ is $m u$ with $m$ in the Levi subgroup, $u$ in the unipotent radical, and $m, u \in K$. Then there are a compact $\Omega \subseteq P_0^1$ and $c > 0$ such that every $g \in G$ is $g = \gamma\, p\, a(t)\, k$ with $\gamma \in U_J(F)$, $p \in \Omega$, $t$ in the cone and $k \in K$.

This is the Siegel set form of reduction theory for adele groups (Borel, Publ. Math. IHES 16 (1963)).

## Proof

The proof is `cov_main`, applied to the same arguments.

## In the Lean code

The theorem is in [UnitarySiegelDomainExistsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySiegelDomainExistsStatement.lean#L8). `IsWittFrame`, `minParOne`, `cone` and `siegelSet` are in [IsSmoothModerateOfIsAutFunSm.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/IsSmoothModerateOfIsAutFunSm.lean#L21). `cov_main` does not use the good position hypothesis.
