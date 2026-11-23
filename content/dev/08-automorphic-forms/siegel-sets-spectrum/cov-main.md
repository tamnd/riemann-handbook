---
id: cov-main
title: A Siegel set covers the adelic unitary group
kind: theorem
decl: GlobalTheory.CompanionTheory.RedCov.cov_main
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.UnitarySiegelDomainExists
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem proves reduction theory for the adelic unitary group of a Hermitian form: $G = U_J(F) \cdot \mathfrak S$ for a Siegel set $\mathfrak S$. Its second name, [the statement form](/entry/unitary-siegel-domain-exists/), passes it to the Siegel core.

## Statement

The statement and the notation ($E/F$, $J$, $G$, the Witt frame $X$, $Y$ of rank $r$, $P_0$, $P_0^1$, the cone, $a(t)$, $K$) are those of [the statement form](/entry/unitary-siegel-domain-exists/).

## Proof

Write $a(s)$ for the torus element with parameter $e^{s}$, $s \in \mathbb R^r$. The proof has two parts.

**A weak form with a compact remainder.** Say that the frame has a reduction if there are a compact $C \subseteq G$ and $c > 0$ such that every $g$ is $\gamma\, q\, a(s)\, \kappa$ with $\gamma \in U_J(F)$, $q \in P_0^1$, $e^s$ in the cone for $c$, and $\kappa \in C$ (`HasRed`). `hasRed_all` proves this for every $J$ and every frame, by induction on $r$. For $r = 0$, take $C = \{1\}$. For the step from $r$ to $r+1$ (`step`):

1. `witt_frame_reduce_rank` gives a form $J'$ with a frame of rank $r$ and a continuous embedding $\iota$ of $U_{J'}(\mathbb A_F)$ into $G$. It fixes the first frame vector $x_1$, maps rational points and $P_0^1$ into the same for $J$, and commutes with $a(s_1, 0)$.
2. For $g \in G$, `exists_near_minimal_vector` gives a nonzero isotropic $v \in E^n$ whose height at $g$ is at most twice the height of every other nonzero isotropic vector. `rational_unitary_sends_isotropic` gives $\gamma_1 \in U_J(F)$ with $\gamma_1 x_1 = v$.
3. The Iwasawa decomposition (`unitary_adelic_iwasawa`) and the decomposition of $P_0$ along $\iota$ reduce $\gamma_1^{-1} g$ to $J'$. The induction hypothesis applies there.
4. `reduction_theory_height_bound` and `reduction_theory_lower_bound` bound $e^{-s_1}$ and $e^{s_2 - s_1}$. So the new parameter lies in a cone. `minimal_parabolic_rational_compact` moves the $P_0^1$ factor into a compact set, modulo rational points.

**From the weak form to the Siegel set.** Let $C$, $c$ be as above for $J$ and $X$, $Y$. Write $\kappa = p k$ with $p \in P_0$, $k \in K$, by the hypothesis $G = P_0 K$. Then $p$ lies in the compact set $CK \cap P_0$. `exists_tau` gives a continuous homomorphism $\tau : P_0 \to \mathbb R^r$ with $p\, a(\tau(p))^{-1} \in P_0^1$. So $|\tau(p)_i| \le B$ for a constant $B$. Let $u = \tau(p)$. Then $g = \gamma\, Q\, a(s+u)\, k$ with $Q = q \cdot a(s)\, p\, a(u)^{-1} a(s)^{-1} \in P_0^1$, by `conj_mem_one` and `mul_mem_one`. `minimal_parabolic_rational_compact` writes $Q = \delta \omega$ with $\delta$ rational and $\omega \in \Omega$. The parameter $e^{s+u}$ lies in the cone for $c\, e^{-2B}$.

## In the Lean code

The theorem is in [UnitarySiegelDomainExists.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySiegelDomainExists.lean#L202), with `step` at L73 and `hasRed_all` at L171. `HasRed`, `NearMin` and the height are in [RatVInjective.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/RatVInjective.lean#L29). We have not read the proofs of the lemmas named above.

The good position hypothesis on $K$ is introduced as `_` at L203 and never used. Inside `step`, the Iwasawa compact group comes from `unitary_adelic_iwasawa`, not from the given $K$.
