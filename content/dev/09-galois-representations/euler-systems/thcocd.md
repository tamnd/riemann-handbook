---
id: thcocd
title: The coefficient congruence on inertia for diamond translates
kind: theorem
decl: UpperTheory.Kd.L.thcocd
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.SiegelFixedPoints.Thcocd
covers: 1515
status: drafted
drafted_by: writer@claude
---
This theorem is the coefficient congruence of [`twist`](/entry/twist/), stated for inertia elements and with values in $\overline{\mathbb{Q}}_\ell$. It only translates hypotheses and the form of the congruence. Its only use is in [`thdiam`](/entry/thdiam/), which feeds [the coefficient law](/entry/hco/). The mathematics is in [`law`](/entry/law/), [`mackey`](/entry/mackey/) and [`one`](/entry/one/).

## Statement

Let $X$ be a tower of modular functions (the structure `Tower`) over an algebraic closure $\Omega$ of $\mathbb{Q}$. Let $\ell$ be an odd prime, $j \colon \Omega \to \overline{\mathbb{Q}}_\ell$ an embedding over a place above $\ell$, and $A = \{z : |j(z)| \leq 1\}$. Let $N$ be prime to $\ell$, let $c, d > 1$ be prime to $6\ell N$, let $e \geq 1$, and let $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$. Assume `AdmissibleHodgeTateZetaClassParams`: $N \geq 5$, each $g_m(r_0)$ lies in $\Gamma_1(N)$ with $(g_m(r_0))_{10} \equiv -r_0 (g_m(r_0))_{00} \bmod \ell$, and a projection $\mathrm{pr}$ has $U_\ell$-eigenvalue $\alpha$ with $|\alpha| = 1$ on $B_{N,\ell}(2e-1)$. Also assume a condition on the second row of $g_m \bmod \ell$, and $N \mid (g_m(r_0))_{10}$.

**Theorem.** There are $c_1 \in \mathbb{N}$ and $\kappa_0 \neq 0$ with the following property. Let $x \in \mathbb{Z}/N$, let $\delta$ be prime to $N$, let $1 \leq m \leq n$ and $c_0 \in \mathbb{N}$. Let $b_\sigma \in B_{N,\ell}(2e-1)$ be congruent mod $\ell^n$ to $\ell^{c_0}$ times the weight $2e+1$ Siegel class `clsBmu` at $\sigma$, for each $\sigma$ that fixes the roots of unity of order $\ell^{m+n}N^2$. Let $y \in (\mathbb{Z}/\ell^m)^\times$. Then there is a series $g$ with coefficients in $A$ such that: for each $s$ in the inertia group of $A$ with trivial cyclotomic character mod $\ell^m$, each theta series $\varphi$ (the predicate `IsThB`: a log derivative mod $\ell^n$ of the $q$-expansion of a unit with the given Kummer class) of $\langle \delta \rangle \sum_{y' \mapsto y} b^{\mathrm{top}}(s, y')$, each $t_t$ that satisfies `IsLamG`, and each $\beta$, $t$ with $\beta \equiv y \bmod \ell^m$, $\beta \equiv 1$ and $\ell^m t \equiv 1 \bmod N$,
$$\ell^{c_1} j(\varphi_i) \equiv \ell^{c_1}\bigl(\ell^{c_0+m} \kappa_0 t_t\, j(P_i) + j(s(g_i)) - j(g_i)\bigr) \pmod{\ell^n}.$$
Here $P_i$ is the coefficient at $\ell^m i$ of `pieceT`: $-\ell^{m(2e-3)}$ times a sum over $\gamma \in \mathrm{SL}_2(\mathbb{Z}/\ell^m)$ with first column of units, of products of the smoothed Eisenstein coefficients `smF` for $(c, 2e)$ and $(d, 1)$, at the vectors $(x t \delta^{-1}, 0)$ and $(t \delta^{-1}, 0)$. The class $b^{\mathrm{top}}(s, y')$ is $b_{\rho(y')^{-1} s \rho(y' \chi(s)^{-1})}$ moved by the twisted Galois action of $\rho(y')$, where $\rho$ is a chosen lift of $(\mathbb{Z}/\ell^{m+n}N^2)^\times$ to the Galois group and $\chi$ is the cyclotomic character mod $\ell^{m+n}N^2$.

## Proof

Set $w = 2e-1$, which is odd. Take $c_1$ and $\kappa$ from `twist` for $w$. Build the structure `Par` from the hypotheses. From the place above $\ell$, $\ell$ is a nonunit of $A$. An inertia element preserves $A$ and acts trivially on its residue field. Trivial cyclotomic character mod $\ell^m$ makes $s$ fix the primitive $\ell^m$-th root of unity (`GlobalTheory.Col.fix_of_cycMod`). Apply `twist` to $\delta$ as a unit of $\mathbb{Z}/N$. Last, $a - b = \ell^n z$ with $z \in A$ gives $|j(a) - j(b)| \leq |\ell^n|$.

## In the Lean code

The theorem is in [Thcocd.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thcocd.lean#L13). Several hypotheses are never used. The row condition and $N \mid (g_m)_{10}$ are named `_hrow` and `_hN10` at [line 42](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thcocd.lean#L42). The second one also follows from $\Gamma_1(N)$. The hypothesis that $j$ is holomorphic is cleared unused at line 96, and it repeats the field `j_hol` of `Tower`. The proof uses only the first three clauses of `AdmissibleHodgeTateZetaClassParams`, so $\mathrm{pr}$, $\alpha$ and the $U_\ell$-eigenvalue condition play no role.
