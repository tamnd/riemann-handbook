---
id: kato-tame-relation-projected
title: The tame norm relation for a weighted sum of zeta systems
kind: theorem
decl: UpperTheory.V.Z.Kato.Nb.kato_tame_relation_projected
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.EulerFactorBounds.KatoTameRelationProjected
covers: 531
status: drafted
drafted_by: writer@claude
---
This theorem gives the tame relation at almost all primes $w$ for the weighted sum $Y$ of zeta systems. It is step 3 of the proof of [the gluing of zeta classes](/entry/k4-top/). At each $w \notin S'$ it gives a cocycle family $Y^w$ whose sum over an extra variable is $P \cdot \ell^k Y$ up to a coboundary.

## Statement

Take $\ell$, $\Omega$, $\iota$, $e$, $g$, $A$, $W$, $X$, $N$, $c$, $d$, $g_m$, $\psi$, $c_w$, the coefficient ring $\mathcal{O}$ and $S$ as in [the parent entry](/entry/k4-top/), with the same hypotheses: `Nf`, $g_m(r_0) \in \Gamma_1(N)$, a holomorphic $j$-function, `AdmWn` and the rest. Let $Y$ satisfy `IsZWc` with exponent $c_0$. For $u \in (\mathbb{Z}/\ell^r)^\times$ put $\eta(u) = \langle u \rangle^{-e} \chi_K(u)$, and write $\mathrm{spec}_\eta(Z)(s) = \sum_u \eta(u) Z(s, u)$.

**Theorem.** There are $k \geq 0$ and a finite set $S'$ of places such that inertia at each place over $w \notin S'$ lies in $\ker W$, and the following holds. Let $n \geq 1$, $w \notin S'$ with $\ell^n \mid Nw - 1$, and $\psi_w \colon G_{\mathbb{Q}} \to \mathbb{Z}/\ell^n$ surjective and trivial on $G_{\mathbb{Q}(\mu_{Nw})}$ (`KillsMu`). Then there are maps $Y^w_r$ on $G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^n \times (\mathbb{Z}/\ell^r)^\times)$, elements $P, u$ and vectors $b_r$ with:

1. $Y^w_r(st, x) = Y^w_r(s, x) + \rho(s) Y^w_r(t, x\kappa(s))$, with $\kappa = (\psi_w, \chi_{\mathrm{cyc}}^{-1})$;
2. $Y^w_r$ is continuous, has values in $\mathcal{O}$, and $Y^w_r$ is the sum of $Y^w_{r+1}$ over fibres;
3. $P \in \mathcal{O}$, $|u| = 1$, $b_r \in \mathcal{O}^2$;
4. $\bigl|\sum_{a} \mathrm{spec}_\eta(Y^w_r(\cdot, (a, \cdot)))(s) - P \ell^k \mathrm{spec}_\eta(Y_r)(s) - (W(s) b_r - b_r)\bigr| \leq |\ell^r|$;
5. $P \equiv u \det(W(\sigma) - 1) \pmod{\ell^n}$ for each Frobenius $\sigma$ at $w$.

The shape is that of the norm relation of an Euler system at a tame prime, as in K. Kato (Astérisque 295, 2004). We do not claim that this exact statement is in that paper.

## Proof

1. `mlTOf`, with [`symEx`](/entry/sym-ex/) and nine other lemmas, gives $c_1$ and for each $x$ a zeta system $Y'_x$ at level $Nw$ with exponent $c_0 + c_1$.
2. `sN2rho` gives an integer $m(x)$ for each $x$ with $c_w(x) \neq 0$. `sInteg` gives integrality.
3. `sEuler` gives $S' \supseteq S$. For $w \notin S'$, $Nw$ is a prime not dividing $\ell N c d$, with Hecke eigenvalues $a, \delta$ that give the Frobenius trace and determinant of $\rho$. `sEulCg` shows $P = 1 - a\, Nw^{-(e+1)} + \delta\, Nw^{-2}$ (the function `eul`) lies in $\mathcal{O}$ and satisfies 5 with $u = 1$.
4. `sLiftOk`, `sRel0` and `sRelT` compare $Y_x$ and $Y'_x$ with Kato-type classes. The lemma `kato_norm_relation_tame_prime`, summed over $r_0$ by the private `coh_sum`, gives the norm relation in cohomology. `sSpec` passes it to $\mathrm{spec}_\eta$ with the factor $P$.
5. Put $M = \max m(x)$ and $Y^t = \sum_x c_w(x) \ell^M Y'_x$. Then `sPushPsi` pushes $Y^t$ along $\psi_w$ to give $Y^w$. Take $k = M + c_1$, and build $b_r$ from the coboundary terms of step 4.

The rest is bookkeeping.

## In the Lean code

The theorem is at [line 50 of KatoTameRelationProjected.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/KatoTameRelationProjected.lean#L50). The statement `KatoTameRelationProjected` and `eul` are in [SPushPsi.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/SPushPsi.lean#L115). We have not unfolded `mlTOf`, `sEuler`, `sRelT` or `kato_norm_relation_tame_prime`.

Two hypotheses are never used: $g_m(r_0) \in \Gamma_1(N)$ and the holomorphy of $j$. They are named `hgm` and `hj` at line 52 and appear again only in a `clear` at line 86. The proof uses instead that $N$ divides the lower left entry of $g_m(r_0)$, which comes from `AdmWn`.
