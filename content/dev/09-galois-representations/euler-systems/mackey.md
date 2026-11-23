---
id: mackey
title: The theta series of a fibre sum of the Siegel zeta class
kind: theorem
decl: UpperTheory.Kd.L.mackey
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.Mackey
covers: 1108
status: drafted
drafted_by: writer@claude
---
This theorem computes the theta series of one partial sum $b^{\mathrm{mid}}(s, z)$ of the Siegel zeta class, for $s$ in an inertia-type subgroup. The answer is $\ell^{c_0} t$ times an explicit sum $F$ of Eisenstein-type coefficients, plus a coboundary, up to a fixed power of $\ell$. It writes the class as a sum over translates of one Siegel unit edge and applies [`one`](/entry/one/) to each translate. Its result is step 3 of the proof of [the coefficient law](/entry/law/).

## Statement

Use the notation of [`law`](/entry/law/), with $M = \ell^{m+n}N^2$. Let $\Gamma = \Gamma_1(N) \cap \Gamma_0(\ell)$, let $G_M$ be its image in $\mathrm{SL}_2(\mathbb{Z}/M)$, and let $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. A set $R \subseteq G_M$ is a set of representatives (`IsReps`) if each $\gamma \in G_M$ is $\rho T^b$ for exactly one pair $\rho \in R$, $0 \leq b < M$. For $z \in (\mathbb{Z}/\ell^{m+n})^\times$, the class $b^{\mathrm{mid}}(s, z)$ is the sum of $b^{\mathrm{top}}(s, y)$ over the $y \in (\mathbb{Z}/\ell^{m+n}N^2)^\times$ above $z$. The sum `Fsum` is, at an integer $r$,
$$F_r = N^3 \sum_{y \mapsto z} \sum_{r_0 \in (\mathbb{Z}/\ell)^\times} \sum_{\gamma \in R} \bigl((g_m(r_0)\tilde\gamma)_{00}\bigr)^w \cdot \rho(y)\bigl(E_r(g_m(r_0)\tilde\gamma)\bigr),$$
and $F_r = 0$ for $r \notin \mathbb{Z}$. Here the first factor is computed mod $\ell^n$, $\rho(y)$ is the chosen Galois element with cyclotomic image $y$, and $E_r(g)$ (`EE`) is a coefficient of the product of two smoothed Eisenstein series for $c$ and $d$ whose parameters come from the entries of $g$.

**Theorem.** Let $\ell$ be a prime. There is $c_c$ with the following property. Take `Par` data, a valuation ring $A$ with $\ell$ in its maximal ideal, $x$, $w$ odd, $m, n \geq 1$, $c_0$, a lift $b$, a set $R$ of representatives, and $z$. Then there is $\xi \colon \mathbb{Q} \to A$ such that for each $s$ that preserves $A$, acts trivially on its residue field and fixes $\zeta_{\ell^{m+n}}$, each $t \in \mathbb{Z}/\ell^n$ with $s(\zeta_{\ell^{m+2n}}) = \zeta_{\ell^n}^t \zeta_{\ell^{m+2n}}$, each theta series $\varphi$ of $b^{\mathrm{mid}}(s, z)$, and each $r$,
$$\ell^{c_c} \varphi_r \equiv s(\xi_r) - \xi_r + \ell^{c_c+c_0}\, F_r\, t \pmod{\ell^n A}.$$

## Proof

Take $c_c$ from [`one`](/entry/one/). Such an $s$ fixes $\mu_M$ (`mem_fixMu_of_inertial`), so its cyclotomic image mod $M$ is $1$ and $b^{\mathrm{top}}(s, y)$ is the twist by $\rho(y)$ of $b$ at $\sigma_y = \rho(y)^{-1} s \rho(y)$.

1. For each $(y, r_0, \gamma)$ with $\gamma \in R$, apply `one` to $g_m(r_0)\tilde\gamma$, in the valuation ring $\rho(y)^{-1}(A)$ and with $\sigma_y$. `reps` gives the conditions that `one` needs: $g_m(r_0)\tilde\gamma \in \Gamma_0(N)$, and $\ell$ divides neither entry of its first column.
2. `wit` gives a unit $f_y$, a power of a product `FF` of translates of `wkMu`, invariant under $\Gamma_1(N\ell^n)$, whose Kummer class mod $\ell^n$ is $b_{\sigma_y}(1, 0)$ (`IsWit`). `FF_eq` writes this product over $R$ with norms.
3. The log derivative of a product of powers is the sum of the log derivatives (`GlobalTheory.T.isLogDerivQExpansion_finset_prod_zpow`). With `isThB_iff`, this gives a theta series of $b^{\mathrm{mid}}(s, z)$.
4. Two theta series of one class agree mod $\ell^n$ (`GlobalTheory.T.cuspFunctionalValueModPrimePow_unique_oddWeight`). Sum the congruences of step 1 over all triples $(y, r_0, \gamma)$, with weights $((g_m(r_0)\tilde\gamma)_{00})^w \ell^{c_0}$ (`cgA_sum`).

The rest is bookkeeping.

## In the Lean code

The theorem is in [Mackey.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Mackey.lean#L334). The name suggests a Mackey formula. The proof of the theorem is the sum over triples of step 4, and it does not compute double cosets. We have not unfolded `wit`, `FF_eq`, `nrm` or `dlgal`.
