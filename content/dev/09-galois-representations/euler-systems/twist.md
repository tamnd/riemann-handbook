---
id: twist
title: The coefficient congruence for a diamond translate, from the untwisted law
kind: theorem
decl: UpperTheory.Kd.L.twist
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.Imports
covers: 1509
status: drafted
drafted_by: writer@claude
---
This theorem extends [the coefficient law](/entry/law/) from a class to its translates by the diamond operators $\langle \delta \rangle$, $\delta \in (\mathbb{Z}/N)^\times$. It does this by a change of the matrices $g_m$: a diamond translate of the class for $g_m$ is the class for $g_m \sigma_\delta$. Its result goes to [`thcocd`](/entry/thcocd/). The analytic and Galois content is in [`law`](/entry/law/).

## Statement

The diamond operator $\langle \delta \rangle$ is the action of a matrix $\sigma_\delta \in \Gamma_0(N) \cap \Gamma_0(\ell)$ whose lower right entry is $\delta \bmod N$. The matrix is a fixed choice (`sgD`, by `Classical.epsilon`).

**Theorem.** Let $\ell$ be a prime, $N \geq 1$, and $w$ odd. There are $c_1 \in \mathbb{N}$ and $\kappa \in \mathbb{Q}$, $\kappa \neq 0$, such that the following holds. Take a tower $X$, integers $c$, $d$, and $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$ that satisfy `Par` (see [`law`](/entry/law/)), with each $g_m(r_0) \in \Gamma_1(N)$. Take a valuation ring $A$ with $\ell$ in its maximal ideal, and $x$, $m \leq n$, $c_0$, $b$, $y$ as in [`law`](/entry/law/). Let $\delta \in (\mathbb{Z}/N)^\times$. Then there is a series $g$ with coefficients in $A$ such that for each $s$ that preserves $A$, acts trivially on its residue field and fixes $\zeta_{\ell^m}$, and each theta series $\varphi$ of the class $\langle \delta \rangle \sum_{y' \mapsto y} b^{\mathrm{top}}(s, y')$,
$$\ell^{c_1} \varphi_i \equiv \ell^{c_1}\bigl(\ell^{c_0+m} \kappa\, t_t\, P_i(x t \delta^{-1}, t \delta^{-1}) + s(g_i) - g_i\bigr) \pmod{\ell^n A}.$$
Here $P_i(u, v)$ is the Eisenstein-type coefficient of [`thcocd`](/entry/thcocd/) at the vectors $(u, 0)$ and $(v, 0)$, and $t_t$, $\beta$, $t$ are as there. The constants depend only on $\ell$, $N$ and $w$.

## Proof

Take $c_1$ and $\kappa$ from `law`. Let $\sigma_\delta$ be the matrix of $\langle \delta \rangle$; it exists because $\delta$ is prime to $N$ (`DiamU.isDiam_sgD_of_coprime'`). By `actcls`, the map $r_0 \mapsto g_m(r_0) \sigma_\delta$ satisfies `Par`, and $\sigma_\delta b$ lifts the class for $g_m \sigma_\delta$. Apply `law` to these data, with $a$ the representative of $\delta^{-1}$. Two things remain.

1. The twisted Galois action commutes with $\sigma_\delta$ on $B_{N,\ell}(w)$ (`GlobalTheory.T.galB_act_comm_gamma0CapGamma0Level_shimuraReciprocity`). So the class built from $\sigma_\delta b$ is $\langle \delta \rangle$ of the class built from $b$, and $\varphi$ is a theta series of it.
2. `law` asks that $a \equiv (g_m(1)\sigma_\delta)_{00} \bmod N$. Since $g_m(1) \in \Gamma_1(N)$, this entry is $(\sigma_\delta)_{00}$. Since $\det \sigma_\delta = 1$ and $(\sigma_\delta)_{10} \equiv 0$, it is $\delta^{-1} \bmod N$.

## In the Lean code

The theorem is in [Imports.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Imports.lean#L13). The file name does not say what the file holds. The hypothesis $g_m(r_0) \in \Gamma_1(N)$ is used only for $r_0 = 1$, in step 2. `actcls` is in [Actcls.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Actcls.lean#L161). We have not unfolded the proof of the commutation lemma.
