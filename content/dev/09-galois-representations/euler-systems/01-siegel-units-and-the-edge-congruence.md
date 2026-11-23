---
title: Siegel units and the edge congruence
decls:
  - UpperTheory.Kd.L.one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Siegel units and the edge congruence

This section proves the congruence for one term of a zeta class made from Siegel units. The term is a Kummer element built from two Siegel units and moved by one matrix $g \in \Gamma_0(N)$. Its logarithmic derivative mod $\ell^n$ is $N^3 t$ times a coefficient of a product of two smoothed Eisenstein series of weight one, plus a coboundary. The sum over all terms of the class is in [the next section](/entry/mackey/), and the result goes up through [the coefficient law for diamond translates](/entry/thdiam/) to [the coefficient law](/entry/hco/) of the zeta argument in the [window bound](/proof/vwin/). The background on [modular forms](/learn/automorphic-forms/#modular-forms) and [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) is in Volume 1.

### Towers of modular functions

Fix an algebraic closure $\Omega$ of $\mathbb{Q}$ and an embedding $\varepsilon \colon \Omega \to \mathbb{C}$.

**Definition 5.1.1.** A *tower of modular functions* over $\Omega$ is a field $K$ with these data:

1. a $q$-expansion map from $K$ to formal series $\sum_{r \in \mathbb{Q}} a_r q^r$ with coefficients in $\Omega$, whose coefficients have bounded denominators;
2. an action $f \mapsto f|\gamma$ of $\mathrm{GL}_2^+(\mathbb{Q})$ on $K$;
3. an action of $\mathrm{Gal}(\Omega/\mathbb{Q})$ on $K$, compatible with the action on the $q$-expansion coefficients;
4. an embedding of $K$ into meromorphic functions on the upper half plane $\mathbb{H}$, and a reciprocity law that joins the two actions;
5. an element $j \in K$ whose $q$-expansion is that of the $j$-function and which is holomorphic on $\mathbb{H}$.

For a prime $\ell$, let $K_\ell = \mathbb{Z}_\ell \otimes K^\times$ and let $\widehat{K}_\ell$ be its $\ell$-adic completion. For $f \in K^\times$ write $[f]_n$ for the class of $f$ mod $\ell^n$.

**Definition 5.1.2.** Let $A$ be a valuation ring of $\Omega$ and let $s$ be a positive integer, the *period*. For $f \in K^\times$, a series $\varphi = \sum_r \varphi_r q^r$ is a *logarithmic derivative of $f$ mod $\ell^n$ with period $s$* if its coefficients lie in $A$ and there are $a, b \in K$ and a constant $\kappa \neq 0$ with these properties: $f b = \kappa a$; the $q$-expansions $a(q)$ and $b(q)$ have coefficients in $A$ and are primitive; and
$$\varphi \cdot a(q)\, b(q) \equiv \theta_s(a(q))\, b(q) - a(q)\, \theta_s(b(q)) \pmod{\ell^n A},$$
where $\theta_s$ multiplies the coefficient of $q^r$ by $s r$.

So $\varphi$ is $\theta_s f / f$ mod $\ell^n$, written without a denominator.

### Siegel units and Eisenstein series

**Definition 5.1.3.** Let $L \geq 1$, let $\zeta$ be a root of unity of order $L$, let $j \geq 1$ and $a_1, a_2 \in \mathbb{Z}$. The *Eisenstein $q$-series* $E^{(j)}_{a_1, a_2}$ of weight $j$ and level $L$ has a constant term that is a Bernoulli value (with a special formula when $j = 1$), and for $n \geq 1$ its $n$-th coefficient is
$$\sum_{d \mid n} \Bigl( [\,n/d \equiv a_1\,] \bigl(\tfrac{n/d}{L}\bigr)^{j-1} \zeta^{a_2 d} - [\,-n/d \equiv a_1\,] \bigl(\tfrac{-n/d}{L}\bigr)^{j-1} \zeta^{-a_2 d} \Bigr),$$
where the congruences are mod $L$. For an integer $c$, the *smoothed series* is
$$E^{(j), c}_{a_1, a_2} = c^2 E^{(j)}_{a_1, a_2} - c^{2 - j} E^{(j)}_{c a_1, c a_2}.$$

The Siegel unit $g_c(a_1, a_2)$ is the element of $K$ whose analytic function is the classical Siegel unit with smoothing integer $c$. Its logarithmic derivative is a smoothed Eisenstein series of weight two, and the cup product of two Kummer classes of Siegel units gives a product of two series of weight one. This is the source of the products below.

**Definition 5.1.4.** *Siegel data* for a prime $\ell$ and a level $N$ are integers $c, d$ and a map $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$ with:

1. $\ell \neq 2$, $N \geq 5$ and $\ell \nmid N$;
2. $c, d > 1$, both prime to $6 \ell N$;
3. each $g_m(r_0)$ lies in $\Gamma_0(N)$;
4. $g_m(r_0)_{11} \equiv g_m(1)_{11} \pmod N$ and $g_m(r_0)_{21} \equiv -r_0\, g_m(r_0)_{11} \pmod \ell$.

Fix Siegel data and $x \in \mathbb{Z}/N$. Let $m, n \geq 1$, $L = m + n$ and $M = \ell^{m+n} N^2$. Let $t'$ be the inverse of $\ell^L$ mod $N$, as an integer. For each Galois element $s$ there is an element $w_s \in K^\times$ built from the two Siegel units $g_c(N + x t' \ell^L, 0)$ and $g_d(t'\ell^L, N)$, both moved by $\mathrm{diag}(N, 1)$. It is the Kummer element of the edge of these two units.

**Definition 5.1.5.** For $g \in \mathrm{SL}_2(\mathbb{Z})$ and $r \in \mathbb{Q}$, let $E_r(g)$ be the coefficient of $q^{\ell^L r}$ (zero if $\ell^L r$ is not a natural number) in the product
$$E^{(1), c}_{g_{11}(N + x t' \ell^L),\ N^2 g_{12}} \cdot E^{(1), d}_{g_{11} t' \ell^L + g_{21},\ N g_{22}},$$
where both series have level $N \ell^L$ and $\zeta = e^{2\pi i/(N \ell^L)}$, read in $\Omega$ through $\varepsilon$.

### The edge congruence

**Theorem 5.1.6 (edge congruence for one translate).** Let $\ell$ be a prime. There is $c_c \in \mathbb{N}$ with the following property. Let $K$ be a tower over $\Omega$, $N \geq 1$, and let $c, d, g_m$ be Siegel data. Let $A$ be a valuation ring of $\Omega$ with $\ell$ in its maximal ideal. Let $x \in \mathbb{Z}/N$, let $m, n \geq 1$, and let $g \in \Gamma_0(N)$ with $\ell \nmid g_{11}$ and $\ell \nmid g_{21}$. Then:

1. $E_r(g) \in A$ for each $r \in \mathbb{Q}$;
2. there is $\xi \colon \mathbb{Q} \to A$ such that, for each Galois element $s$ that fixes the roots of unity of order $M$ and maps $A$ onto $A$, each $t \in \mathbb{Z}/\ell^n$ with $s(\zeta_{\ell^{m+2n}}) = \zeta_{\ell^n}^{t} \zeta_{\ell^{m+2n}}$, each logarithmic derivative $\varphi$ of $w_s | g$ mod $\ell^n$ with period $M$, and each $r \in \mathbb{Q}$,
$$\ell^{c_c} \varphi_r \equiv s(\xi_r) - \xi_r + \ell^{c_c} N^3 E_r(g)\, t \pmod{\ell^n A}.$$

Lean: `UpperTheory.Kd.L.one`

*Proof.* Siegel data have $\ell \neq 2$. For part 1: $\ell$ divides neither $g_{11}$ nor $g_{21}$, and $\ell \nmid N$. So the parameters of the two series are prime to $\ell$ in the places where it matters, and the coefficients of each smoothed series of weight one lie in $A$. A product of two such series has coefficients in $A$.

For part 2, take $c_c$ from the edge congruence for a pair of Siegel units. That result takes two Siegel units for $c$ and $d$ with parameters $(A_1, a_2)$ and $(B_1, b_2)$, where $a_2 \equiv N' g'$ and $b_2 \equiv N' h'$ mod $\ell^L$, together with $\ell^n$-th roots of the units, their two Kummer characters, and a cochain $\eta$ whose coboundary is the cup product of the two characters. It gives $\xi$ and the congruence
$$\ell^{c_c}\varphi_r \equiv s^{-1}(\xi_r) - \xi_r - \ell^{c_c}(A_1 h' - g' B_1)\, t\, E'_r,$$
where $E'_r$ is the coefficient of the product of the two smoothed series of weight one at these parameters. It holds for each $s$ that maps $A$ onto $A$ and fixes the base field.

Apply it with $N' = N^3$ and $L = m + n$, to the embedding of the field of level $M$ given by $\mathrm{diag}(N^2, 1)$ followed by $g$. The roots and the cochain come from the construction of $w_s$. The rescaling by $N^2$ turns a logarithmic derivative with period $M$ into one with period $\ell^{m+n}$. After the rescaling, $E'_r$ becomes $E_r(g)$. The result is used with $s^{-1}$ in place of $s$ and $-t$ in place of $t$. Last, $\det g = 1$ gives $A_1 h' - g' B_1 = N^3 + \ell^{m+n} Q$ for an integer $Q$. The term $\ell^{m+n} Q$ dies mod $\ell^n$ because $E'_r$ lies in $A$ by part 1. $\square$

The theorem is local in $g$: it says nothing about the other terms of the class. The sum over the terms needs a choice of representatives and a formula for the class as a product of translates of $w_s$. This is the subject of the next section.

**Remark 5.1.7 (Formalization).** The theorem is in [CoefQCmulMem.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/CoefQCmulMem.lean#L155). It is proved under `set_option maxHeartbeats 2000000` (line 154). The case $\ell = 2$ is a vacuous branch at lines 161 to 162, because `Par` already contains `l ≠ 2`. The name `one` and the file name say little. The tower is the structure `Tower` ([ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L42)); we list only the fields that we use. The logarithmic derivative is `IsDl` and the Siegel data are `Par`. The Kummer element $w_s$ is `wkMu` ([IsZetaTW.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsZetaTW.lean#L59)); we have not unfolded `topW`, through which it is defined, so the words "Kummer element of the edge" only name it. The coefficient $E_r(g)$ is `EE`, and the series are `eisF` and `smF` ([Integral.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/Integral.lean#L24)); we did not unfold the constant term `const0`. The edge congruence for a pair of Siegel units is `GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence`, proved as `GlobalTheory.pair_edge_dlog`; we have not unfolded it. The rescaling is `GlobalTheory.T.isLogDerivQExpansionModPrimePow_rescale`.
