---
title: Fibre sums, traces and the coefficient law
decls:
  - UpperTheory.Kd.L.mackey
  - UpperTheory.Kd.L.arith
  - UpperTheory.Kd.L.law
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fibre sums, traces and the coefficient law

This section computes, on inertia, the logarithmic derivative of a zeta class built from Siegel units. Up to a coboundary and a fixed power of $\ell$, its coefficients are $\ell^{c_0 + m} \kappa\, t$ times the coefficients of an explicit sum of products of two smoothed Eisenstein series. The proof has three steps. The first sums the edge congruence of [the previous section](/entry/one/) over the terms of a fibre of the class. The second is an arithmetic computation of the normalized trace of that sum. The third takes the trace along the cyclotomic tower and assembles the result. The coefficient law of this section is extended to diamond translates in [the next section](/entry/twist/). The Galois background is in [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology) and [the cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

### Classes on a tower

Fix a tower $K$ over $\Omega$, a prime $\ell$ and a level $N$. Let $\mathcal{A}_\ell \subseteq \widehat{K}_\ell$ be the span of the classes that, at each level $n$, are $\ell^n$-th powers up to units at the cusps. Let $\mathcal{F}$ be the space of maps $\mathbb{Z}_\ell^2 \to \widehat{K}_\ell$.

**Definition 5.2.1.** For a natural number $w$, let $P_w \subseteq \mathcal{F}$ be the maps $u \mapsto \sum_i a_i u_0^i u_1^{w-i}$ with $a_i \in \mathcal{A}_\ell$. A matrix $\gamma$ acts on $\mathcal{F}$ by $(\gamma b)(u) = b(u\gamma) | \gamma$. Let $\Gamma = \Gamma_1(N) \cap \Gamma_0(\ell)$, and let $B_{N,\ell}(w)$ be the $\mathbb{Z}_\ell$-span of the elements of $P_w$ that are fixed by $\Gamma$. A Galois element $s$ acts on $\mathcal{F}$ by $(s \ast b)(u) = s\bigl(b(u_0, \chi(s) u_1)\bigr)$, with $\chi$ the [[cyclotomic character|XSGB5K2KEG]].

**Definition 5.2.2.** Fix Siegel data $c, d, g_m$ and $x \in \mathbb{Z}/N$. Let $m, n \geq 1$ and $M = \ell^{m+n} N^2$. For a Galois element $\sigma$ the *zeta class of weight $k$* is
$$z_\sigma = \sum_{r_0 \in (\mathbb{Z}/\ell)^\times} \sum_{\gamma} g_m(r_0) \tilde\gamma \cdot \bigl(u \mapsto u_0^{k-2} [w_\sigma]\bigr),$$
where $\gamma$ runs over the image of $\Gamma$ in $\mathrm{SL}_2(\mathbb{Z}/M)$, $\tilde\gamma$ is a fixed lift of $\gamma$ to $\mathrm{SL}_2(\mathbb{Z})$, and $w_\sigma$ is the Kummer element of the previous section. A family $(b_\sigma)$ of elements of $\mathcal{F}$ is a *lift with exponent $c_0$ in weight $w$* if, for each $\sigma$ that fixes the roots of unity of order $M$, $b_\sigma \in B_{N,\ell}(w)$ and $b_\sigma \equiv \ell^{c_0} z_\sigma \bmod \ell^n$, with $z_\sigma$ of weight $w + 2$.

Fix a map $\rho$ from $(\mathbb{Z}/M)^\times$ to the Galois group with $\chi(\rho(y)) \equiv y \bmod M$. For a lift $b$, a Galois element $s$ and $y \in (\mathbb{Z}/M)^\times$, put
$$b^{\mathrm{top}}(s, y) = \rho(y) \ast b_{\rho(y)^{-1} s \rho(y \chi(s)^{-1})}.$$
For $z \in (\mathbb{Z}/\ell^{m+n})^\times$, let $b^{\mathrm{mid}}(s, z)$ be the sum of $b^{\mathrm{top}}(s, y)$ over the $y$ above $z$. For $y \in (\mathbb{Z}/\ell^m)^\times$, let $b^{\mathrm{bot}}(s, y)$ be the sum of $b^{\mathrm{top}}(s, y')$ over the $y'$ above $y$.

**Definition 5.2.3.** Let $A$ be a valuation ring of $\Omega$ and $b \in \mathcal{F}$. A series $\varphi$ is a *logarithmic derivative of $b$ mod $\ell^n$* if there is $f \in K^\times$ fixed by $\Gamma_1(N \ell^n)$ with these properties: $b(1, 0) \equiv [f]_n \bmod \ell^n$; for each $\delta \in \Gamma_1(N)$ with $-\delta \in \Gamma(\ell^n)$, the product $f \cdot (f|\delta)$ is the $\ell^n$-th power of an element fixed by $\Gamma_1(N\ell^n)$; and $\varphi$ is a logarithmic derivative of $f$ mod $\ell^n$ with period 1.

### The fibre sum

A set $R \subseteq \mathrm{SL}_2(\mathbb{Z}/M)$ is a *set of representatives* if $R$ lies in the image of $\Gamma$ and each $\gamma$ in that image is $\rho' T^b$ for exactly one pair with $\rho' \in R$ and $0 \leq b < M$, where $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

**Definition 5.2.4.** For a set of representatives $R$, $z \in (\mathbb{Z}/\ell^{m+n})^\times$, an odd $w$ and $r \in \mathbb{Q}$, let $F_r = 0$ if $r \notin \mathbb{Z}$, and otherwise
$$F_r = N^3 \sum_{y \mapsto z} \sum_{r_0} \sum_{\gamma \in R} \bigl(g_m(r_0)\tilde\gamma\bigr)_{11}^{\,w} \cdot \rho(y)\bigl(E_r(g_m(r_0)\tilde\gamma)\bigr),$$
where the first factor is the $w$-th power of the least residue of the entry mod $\ell^n$.

**Theorem 5.2.5 (fibre sum).** Let $\ell$ be a prime. There is $c_c$ with the following property. Take a tower $K$, $N \geq 1$, Siegel data $c, d, g_m$, a valuation ring $A$ of $\Omega$ with $\ell$ in its maximal ideal, $x \in \mathbb{Z}/N$, an odd $w$, $m, n \geq 1$, $c_0 \in \mathbb{N}$, a lift $b$ with exponent $c_0$ in weight $w$, a set of representatives $R$ and $z \in (\mathbb{Z}/\ell^{m+n})^\times$. Then there is $\xi \colon \mathbb{Q} \to A$ such that for each $s$ that maps $A$ onto $A$, acts trivially on the residue field of $A$ and fixes $\zeta_{\ell^{m+n}}$, each $t \in \mathbb{Z}/\ell^n$ with $s(\zeta_{\ell^{m+2n}}) = \zeta_{\ell^n}^t \zeta_{\ell^{m+2n}}$, each logarithmic derivative $\varphi$ of $b^{\mathrm{mid}}(s, z)$ mod $\ell^n$, and each $r \in \mathbb{Q}$,
$$\ell^{c_c}\varphi_r \equiv s(\xi_r) - \xi_r + \ell^{c_c + c_0} F_r\, t \pmod{\ell^n A}.$$

Lean: `UpperTheory.Kd.L.mackey`

*Proof.* Take $c_c$ from [the edge congruence](/entry/one/). Such an $s$ acts trivially on the residue field and fixes $\zeta_{\ell^{m+n}}$. So it fixes the roots of unity of order $M$, and $\chi(s) \equiv 1 \bmod M$. Then $b^{\mathrm{top}}(s, y)$ is the twist by $\rho(y)$ of $b$ at $\sigma_y = \rho(y)^{-1} s \rho(y)$.

1. For each triple $(y, r_0, \gamma)$ with $\gamma \in R$, apply the edge congruence to $g_m(r_0)\tilde\gamma$, in the valuation ring $\rho(y)^{-1}(A)$ and with $\sigma_y$. The representatives give what it needs: $g_m(r_0)\tilde\gamma \in \Gamma_0(N)$, and $\ell$ divides neither entry of its first column.
2. There is a unit $f_y$, a power of a product of translates of $w_{\sigma_y}$, fixed by $\Gamma_1(N\ell^n)$, whose Kummer class mod $\ell^n$ is $b_{\sigma_y}(1, 0)$. The product runs over $R$, and the norms along $T$ take care of the factor $T^b$.
3. The logarithmic derivative of a product of powers is the sum of the logarithmic derivatives. This gives a logarithmic derivative of $b^{\mathrm{mid}}(s, z)$.
4. Two logarithmic derivatives of one class in odd weight agree mod $\ell^n$. Sum the congruences of step 1 over all triples, with the weights $(g_m(r_0)\tilde\gamma)_{11}^{\,w} \ell^{c_0}$. $\square$

### The arithmetic of the trace

Let $\mathbb{Z}_{(\ell)}[\zeta]$-integral mean: $D F \in \mathbb{Z}[\zeta_{\ell^k}]$ for some $D$ prime to $\ell$; we say $F$ is *$\ell$-integral at level $k$*. For $F \in \Omega$, an element $F'$ is a *normalized trace of $F$ from level $m+n$ to level $m$* if there are automorphisms $\tau_a$ with $\tau_a(\zeta_{\ell^{m+n}}) = \zeta_{\ell^{m+n}}^a$ and $\ell^n F' = \sum_{a \equiv 1 \bmod \ell^m} \tau_a(F)$, the sum over $a \in (\mathbb{Z}/\ell^{m+n})^\times$.

**Definition 5.2.6.** For integers $k$, $u$, $v$, a root of unity $\zeta$ of order $N\ell^m$ and $i \in \mathbb{N}$, let $P^{(k)}_i(u, v; \zeta)$ be the coefficient of $q^{\ell^m i}$ in
$$-\ell^{m(k-4)} \sum_{\gamma} E^{(k-1), c}_{N\gamma_{11} + \ell^m u,\ N\gamma_{12}} \cdot E^{(1), d}_{N\gamma_{21} + \ell^m v,\ N\gamma_{22}},$$
where $\gamma$ runs over $\mathrm{SL}_2(\mathbb{Z}/\ell^m)$ with $\ell \nmid \gamma_{11}$ and $\ell \nmid \gamma_{21}$, the entries are least residues, and both series have level $N\ell^m$ and the root $\zeta$. This is the *Eisenstein piece*.

**Theorem 5.2.7 (arithmetic of the trace).** Let $\ell$ be a prime, $N \geq 1$ and $w \geq 1$. There are $\kappa \in \mathbb{Q}$, $\kappa \neq 0$, and $L_0 \in \mathbb{N}$ with the following property. Take Siegel data $c, d, g_m$, $x \in \mathbb{Z}/N$, $m \geq 1$, $n$, a set of representatives $R$ and $z \in (\mathbb{Z}/\ell^{m+n})^\times$. Then:

1. each $F_r$ is $\ell$-integral at level $m+n$;
2. if $L_0 \leq m+n$, then for each $i \in \mathbb{N}$, each normalized trace $F'$ of $F_i$ from level $m+n$ to level $m$, and all integers $\beta, t, a$ with $a \equiv g_m(1)_{11} \bmod N$, $\beta \equiv z \bmod \ell^m$, $\beta \equiv 1 \bmod N$ and $\ell^m t \equiv 1 \bmod N$, there is $E$, $\ell$-integral at level $m$, with
$$F' = \kappa\, \ell^m P^{(w+2)}_i\bigl(x a t, a t; \zeta_{N\ell^m}^{\beta}\bigr) + \ell^n E.$$

Lean: `UpperTheory.Kd.L.arith`

*Proof.* The constants are $\kappa = -N \varphi(N^2) \mu$, where $\mu > 0$ is a count of matrices, and $L_0 = (w+1)^2 \ell$. For part 1: by the representatives, $\ell$ divides neither entry of the first column of $g_m(r_0)\tilde\gamma$. Each $E_r$ of such a matrix is $\ell$-integral at level $m+n$: for $r < 0$ it is zero, and otherwise it is a coefficient of a product of two smoothed series of weight one. The $\ell$-integral elements at level $m+n$ form a ring that is stable under the Galois action on $\mathbb{Q}(\zeta_{\ell^{m+n}})$. So the sum $F_r$ is $\ell$-integral.

For part 2, write the trace of $F_i$ as a sum over $a \equiv 1 \bmod \ell^m$, over $y$, over $r_0$ and over $\gamma \in R$. Exchange the four sums. Each matrix $h$ in $\mathrm{SL}_2(\mathbb{Z}/\ell^{m+n})$ with first column of units arises from the same number $\mu$ of pairs $(r_0, \gamma)$, and the sum over $y$ gives the factor $\varphi(N^2)$. The trace of the product of two series of weight one along $\zeta_{\ell^{m+n}} \mapsto \zeta_{\ell^{m+n}}^a$ collapses the level from $\ell^{m+n}$ to $\ell^m$. It produces the factor $\ell^{m(w-2)}$ and the raising of the weight of the first series from 1 to $w+1$, up to terms divisible by $\ell^n$. The bound $L_0 \leq m + n$ makes the binomial terms of degree up to $w+1$ in $\ell^{m+n}$ small enough. $\square$

### The coefficient law

**Theorem 5.2.8 (coefficient law).** Let $\ell$ be a prime, $N \geq 1$ and $w$ odd. There are $c_1 \in \mathbb{N}$ and $\kappa \in \mathbb{Q}$, $\kappa \neq 0$, with the following property. Take a tower $K$, Siegel data $c, d, g_m$, a valuation ring $A$ of $\Omega$ with $\ell$ in its maximal ideal, $x \in \mathbb{Z}/N$, $1 \leq m \leq n$, $c_0 \in \mathbb{N}$, a lift $b$ with exponent $c_0$ in weight $w$, and $y \in (\mathbb{Z}/\ell^m)^\times$. Then there is a series $g$ with coefficients in $A$ such that the following holds. Let $s$ map $A$ onto $A$, act trivially on the residue field of $A$ and fix $\zeta_{\ell^m}$. Let $\varphi$ be a logarithmic derivative of $b^{\mathrm{bot}}(s, y)$ mod $\ell^n$. Let $t_t \in \mathbb{Z}/\ell^n$ with $s^{\ell^{n-m}}(\zeta_{\ell^{2n}}) = \zeta_{\ell^n}^{t_t} \zeta_{\ell^{2n}}$. Let $\beta \in \mathbb{N}$ and $t, a \in \mathbb{Z}$ with $a \equiv g_m(1)_{11} \bmod N$, $\beta \equiv y \bmod \ell^m$, $\beta \equiv 1 \bmod N$ and $\ell^m t \equiv 1 \bmod N$. Then for each $i \in \mathbb{N}$,
$$\begin{aligned} \ell^{c_1} \varphi_i \equiv \ell^{c_1} \Bigl( &\ell^{c_0+m} \kappa\, t_t\, P^{(w+2)}_i\bigl(x a t, a t; \zeta_{N\ell^m}^{\beta}\bigr) \\ &+ s(g_i) - g_i \Bigr) \pmod{\ell^n A}. \end{aligned}$$

Lean: `UpperTheory.Kd.L.law`

*Proof.* Siegel data have $\ell \neq 2$. Take $\kappa$ and $L_0$ from [the arithmetic of the trace](/entry/arith/). There is $c_2$ such that $\ell^{c_2} P^{(w+2)}_i \in A$ for all $m \leq L_0$. Take $c_c$ from [the fibre sum](/entry/mackey/) and $c$ from the corestriction lemma below. Put $c_1 = c + c_c + L_0 + c_2 + v$, where $\ell^v \kappa \in A$.

If $m + n < L_0$, take $g = 0$. Then $n < L_0$, and both sides lie in $\ell^n A$ because of the factor $\ell^{c_1}$. Now let $m + n \geq L_0$.

1. Each fibre sum $b^{\mathrm{mid}}(s, z)$ lies in $B_{N,\ell}(w)$. Its logarithmic derivatives form a cocycle mod $\ell^n$ in $s$.
2. Each class in $B_{N,\ell}(w)$ with $w$ odd and $\ell$ odd has a logarithmic derivative mod $\ell^n$.
3. The fibre sum theorem gives, at a lift $z$ of $y$, the logarithmic derivative as $\ell^{c_0} F t$ plus a coboundary.
4. A corestriction lemma, a form of Shapiro's lemma along the cyclotomic tower, sums the cocycle over $u \equiv 1 \bmod \ell^m$. It replaces $F$ by its normalized trace $F'$ from level $m + n$ to level $m$, and $t$ by $t_t$.
5. The arithmetic of the trace gives $F'_i = \kappa \ell^m P^{(w+2)}_i + \ell^n E$ with $E$ integral.
6. The sum of the classes $b^{\mathrm{mid}}(s, uz)$ is $b^{\mathrm{bot}}(s, y)$. Two logarithmic derivatives of one class agree mod $\ell^n$, so the congruence holds for $\varphi$. $\square$

**Remark 5.2.9 (Formalization).** The fibre sum is in [Mackey.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Mackey.lean#L334). The name points to a Mackey formula, but the proof is the sum over triples of step 4 and computes no double cosets. Its steps 2 and 3 use `wit`, `FF_eq`, `nrm` and `dlgal`, which we have not unfolded; we did not open the proof of the uniqueness lemma `GlobalTheory.T.cuspFunctionalValueModPrimePow_unique_oddWeight`. The arithmetic of the trace is in [TwistColumnZero.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/TwistColumnZero.lean#L140). It asks $1 \leq w$, while the other two theorems ask $w$ odd. It does not involve the tower. The count $\mu$ comes from `UpperTheory.Kd.L.count`; our sketch of the collapse of levels summarizes lemmas of that file that we read only in part. The coefficient law is in [ExistsSeries.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/ExistsSeries.lean#L264). Its case $\ell = 2$ is a vacuous branch at line 268. At line 275 the letter `c` is reused for the corestriction constant, beside the smoothing integer $c$. Step 1 is `zcoc` in [RedTopCycM.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/RedTopCycM.lean#L190), step 2 is `GlobalTheory.T.exists_cuspFunctional_oddWeight_oddPrime`, and the corestriction lemma is `GlobalTheory.T.corestriction_cyclotomic_shapiro_normalisedTrace`, proved as `GlobalTheory.Glue.CorShap.cores_law`, which we have not unfolded. The space $\mathcal{A}_\ell$ is `A` from `Un` in [Letter.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/Letter.lean#L16); our words "units at the cusps" read the valuations in `Un` as those at the cusps, which the definition does not say. In the Lean code the matrix entries are indexed from 0, so our $\gamma_{11}$ is `γ 0 0`.
