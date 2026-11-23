---
id: law
title: The coefficient law for the Siegel zeta class
kind: theorem
decl: UpperTheory.Kd.L.law
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.ExistsSeries
covers: 1477
status: drafted
drafted_by: writer@claude
---
This theorem computes, on inertia, the coefficients of a theta series of a zeta class built from Siegel units. Up to a coboundary and a fixed power of $\ell$, they are $\ell^{c_0+m}\kappa$ times the coefficients of a sum of products of two smoothed Eisenstein series. [`twist`](/entry/twist/) extends it to diamond translates. Through [`thcocd`](/entry/thcocd/) and [`thdiam`](/entry/thdiam/), it feeds [the coefficient law](/entry/hco/).

## Statement

Let $\ell$ be a prime, $N \geq 1$, $w$ odd, and $M = \ell^{m+n}N^2$. The structure `Par` collects these conditions on $c$, $d$ and $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$: $\ell \neq 2$, $N \geq 5$, $\ell \nmid N$, $c, d > 1$ prime to $6\ell N$, each $g_m(r_0) \in \Gamma_0(N)$ with $(g_m(r_0))_{00} \equiv (g_m(1))_{00} \bmod N$ and $(g_m(r_0))_{10} \equiv -r_0 (g_m(r_0))_{00} \bmod \ell$.

The class `clsBmu` at $\sigma$ is $\sum_{r_0} \sum_{\gamma} g_m(r_0)\tilde\gamma \cdot \bigl(u \mapsto u_0^{w} \,[w_\sigma]\bigr)$, where $\gamma$ runs over the image of $\Gamma_1(N) \cap \Gamma_0(\ell)$ in $\mathrm{SL}_2(\mathbb{Z}/M)$, $\tilde\gamma$ is a lift, and $[w_\sigma]$ is the Kummer class of an element `wkMu` built from the Siegel units for $c$ at $(N + x t' \ell^{m+n}, 0)$ and for $d$ at $(t'\ell^{m+n}, N)$, with an integer $t'$ (`topT`). We have not unfolded `wkMu` further. A family $b_\sigma \in B_{N,\ell}(w)$ *lifts* it (`LiftB`) if $b_\sigma \equiv \ell^{c_0}\,\mathrm{clsBmu}_\sigma \bmod \ell^n$ for each $\sigma$ that fixes $\mu_M$.

**Theorem.** For $\ell$, $N$, $w$ there are $c_1$ and $\kappa \in \mathbb{Q}^\times$ such that: for all $X$, $c$, $d$, $g_m$ with `Par`, each valuation ring $A$ with $\ell$ in its maximal ideal, $x \in \mathbb{Z}/N$, $1 \leq m \leq n$, $c_0$, a lift $b$, and $y \in (\mathbb{Z}/\ell^m)^\times$, there is a series $g$ over $A$ with
$$\ell^{c_1} \varphi_i \equiv \ell^{c_1}\bigl(\ell^{c_0+m} \kappa\, t_t\, P_i(x a t, a t) + s(g_i) - g_i\bigr) \pmod{\ell^n A}$$
for the $s$, $\varphi$, $t_t$, $\beta$, $t$ of [`twist`](/entry/twist/) with $\delta = 1$, and each integer $a \equiv (g_m(1))_{00} \bmod N$.

## Proof

The case $\ell = 2$ is excluded by `Par`. The constants: `arith` gives $\kappa = -N \varphi(N^2)\mu$ and a bound $L_0 = (w+1)^2\ell$; `small` gives $c_2$ with $\ell^{c_2}P_i \in A$ for $m \leq L_0$; [`mackey`](/entry/mackey/) gives $c_c$; the corestriction lemma gives $c$. Then $c_1 = c + c_c + L_0 + c_2 + v$, where $\ell^v\kappa \in A$.

If $m + n < L_0$, take $g = 0$: since $n < L_0$, both sides lie in $\ell^n A$ (`small_close`). Otherwise:

1. `zcoc`: each partial sum $b^{\mathrm{mid}}(s, z)$ of the class over the fibre above $z \in (\mathbb{Z}/\ell^{m+n})^\times$ lies in $B_{N,\ell}(w)$. Its theta series form a cocycle mod $\ell^n$ in $s$.
2. Each such class has a theta series (`GlobalTheory.T.exists_cuspFunctional_oddWeight_oddPrime`).
3. [`mackey`](/entry/mackey/) gives, at a lift $z$ of $y$, the theta series as $\ell^{c_0}F t_t$ plus a coboundary, where $F$ = `Fsum` is an explicit Eisenstein sum.
4. `GlobalTheory.T.corestriction_cyclotomic_shapiro_normalisedTrace` sums the cocycle over $u \equiv 1 \bmod \ell^m$. It replaces $F$ by its normalized trace $F'$ from $\mathbb{Q}(\zeta_{\ell^{m+n}})$ to $\mathbb{Q}(\zeta_{\ell^m})$.
5. `arith`: $F'_i = \kappa \ell^m P_i + \ell^n E$ with $E$ integral.
6. The sum of the $b^{\mathrm{mid}}(s, uz)$ is the class of the statement (`sum_fib`, `thb_sum`). Two theta series of one class agree mod $\ell^n$ (`GlobalTheory.T.cuspFunctionalValueModPrimePow_unique_oddWeight`). `final_step` assembles the congruence.

## In the Lean code

The theorem is in [ExistsSeries.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/ExistsSeries.lean#L264). The vacuous branch $\ell = 2$ is at line 268. `arith` is in [TwistColumnZero.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/TwistColumnZero.lean#L140), `small` in [NotDvdOfCoprime.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/NotDvdOfCoprime.lean#L209), `zcoc` in [RedTopCycM.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/RedTopCycM.lean#L190). The corestriction lemma is proved as `GlobalTheory.Glue.CorShap.cores_law`; we have not unfolded it. The name `law` and the file name say little.
