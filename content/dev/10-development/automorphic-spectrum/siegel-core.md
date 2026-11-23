---
id: siegel-core
title: The Siegel core for unitary groups
kind: theorem
decl: GlobalTheory.CompanionTheory.SiegelRed.siegelCore
module: Development.AutomorphicSpectrum.Proofs.GlobalProofs.SiegelSetUnitary
covers: 467
status: drafted
drafted_by: writer@claude
---
This theorem collects the facts of reduction theory for the adelic unitary group $U_J(\mathbb{A}_F)$ in one statement. It gives a compact subgroup $K$ and a Siegel set that covers the group modulo $U_J(F)$, with the bounds that the theory of cusp forms needs. It has four users, among them `siegelSetUnitary`, on the way to the step [every character](/step/every-character/).

## Statement

Let $E/F$ be a CM extension with conjugation $\sigma$, and $J$ a nondegenerate Hermitian $n \times n$ matrix over $E$. Let $G = U_J(\mathbb{A}_F)$. Let $X$, $Y$ be a Witt frame of rank $r$, as in [the covering statement](/entry/unitary-siegel-domain-exists/). Let $P_0$ be the minimal parabolic subgroup of the flag of $X$, $P_0^1$ its elements of norm $1$, and $a(t)$ the torus element for $t$ in the cone. The Siegel set is $\mathfrak{S}(\Omega, c, K) = \Omega \cdot a(\text{cone}_c) \cdot K$.

**Theorem.** There are a compact subgroup $K \subseteq G$, a compact $\Omega \subseteq P_0^1$ and $c > 0$ with:

1. $G = P_0 K$, and $K$ is in good position: each $p \in P_0 \cap K$ is $m u$ with $m$ in the Levi subgroup, $u$ in the unipotent radical, and $m, u \in K$;
2. every $g \in G$ is $\gamma s$ with $\gamma \in U_J(F)$ and $s \in \mathfrak{S}(\Omega, c, K)$;
3. there is a compact $C$ with $a(t)^{-1} p\, a(t) \in C$ for all $p \in \Omega$ and $t$ in the cone;
4. there are $C$ and $A$ with $\operatorname{ht}(g) \le C \operatorname{ht}(\gamma g)^A$ for $g$ in the Siegel set and $\gamma \in U_J(F)$;
5. for every smooth cuspidal $\varphi$ of moderate growth and every $N$, $\lvert \varphi(g) \rvert \operatorname{ht}(g)^N$ is bounded on the Siegel set.

Part 2 is the Siegel set form of reduction theory (Borel, Publ. Math. IHES 16, 1963). Part 5 is the rapid decay of cusp forms on Siegel sets, as in Moeglin and Waldspurger, *Spectral decomposition and Eisenstein series* (Cambridge, 1995), Chapter I.

## Proof

The proof joins six lemmas.

1. `exists_kInf` gives a compact $K_1$ at the archimedean places with the Iwasawa decomposition and good position.
2. `unitary_adelic_iwasawa_compact` gives the same at the finite places, with a compact $K_2$.
3. `exists_compact_iwasawa` puts $K_1$ and $K_2$ together into $K$. This gives part 1.
4. [`unitary_siegel_domain_exists`](/entry/unitary-siegel-domain-exists/) gives $\Omega$ and $c$ with part 2.
5. `conj_compact` gives part 3.
6. `cusp_form_siegel_bound` gives part 4, and `cusp_form_rapid_decay` gives part 5.

## In the Lean code

The theorem is in [SiegelSetUnitary.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/SiegelSetUnitary.lean#L17). `SiegelCore`, `minPar`, `leviMin`, `unipMin` and `GoodPosition` are in [SiegelCore.lean](lean:Development/WeilBound/ThetaLifts/Reductions/SiegelCore.lean#L37). `siegelSet`, `cone` and `IsCuspidal` are in [IsSmoothModerateOfIsAutFunSm.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/IsSmoothModerateOfIsAutFunSm.lean#L21). We have not unfolded `GAd`, `ratPts` or `height`.

The four lemmas in `GlobalTheory.T` are second names, proved by `first | exact …`. `unitary_siegel_domain_exists` restates [`cov_main`](/entry/cov-main/). `cusp_form_siegel_bound` restates `SiegelHt.height_le_pow`, and its statement has no cusp form in it. We have not opened the proofs of the six lemmas. `siegelSetUnitary` gets the stronger `SiegelSetUnitary` from this theorem by `siegel_of_core`.
