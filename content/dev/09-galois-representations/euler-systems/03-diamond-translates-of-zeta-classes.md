---
title: Diamond translates of zeta classes
decls:
  - UpperTheory.Kd.L.twist
  - UpperTheory.Kd.L.thcocd
  - UpperTheory.Kd.L.thdiam
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Diamond translates of zeta classes

This section extends [the coefficient law](/entry/law/) from a zeta class to its translates by the diamond operators $\langle \delta \rangle$, with $\delta$ a unit mod $N$. The method is a change of the matrices of the Siegel data: a diamond translate of the class for $g_m$ is the class for $g_m \sigma_\delta$, and the Eisenstein piece changes by a factor $\delta^{-1}$ in its parameters. We then state the result for elements of an inertia group, with values in $\overline{\mathbb{Q}}_\ell$ through an embedding over a place above $\ell$. This is the form that [the coefficient law of the zeta argument](/entry/hco/) uses in the [window bound](/proof/vwin/). It averages the result over $\delta$. The local background is in [local fields](/learn/galois-cohomology/#local-fields) and [decomposition groups and inertia](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius).

### The diamond operators

We keep the notation of [the previous section](/entry/mackey/): a tower $K$ over $\Omega$, the space $\mathcal{F}$ of maps $\mathbb{Z}_\ell^2 \to \widehat{K}_\ell$ with its action of matrices, the space $B_{N,\ell}(w)$, the twisted Galois action $\ast$, the lifts $b$ of zeta classes, the fibre sums $b^{\mathrm{bot}}(s, y)$, the logarithmic derivatives of a class mod $\ell^n$, and the Eisenstein pieces $P^{(k)}_i(u, v; \zeta)$.

**Definition 5.3.1.** Let $N, \ell \geq 1$ and $\delta \in \mathbb{N}$. Fix a matrix $\sigma_\delta \in \mathrm{SL}_2(\mathbb{Z})$ with $\sigma_\delta \in \Gamma_0(N) \cap \Gamma_0(\ell)$ and $(\sigma_\delta)_{22} \equiv \delta \bmod N$, if there is one. The *diamond operator* $\langle \delta \rangle$ on $\mathcal{F}$ is the action of $\sigma_\delta$.

If $\delta$ is prime to $N$, such a matrix exists. Then $(\sigma_\delta)_{21} \equiv 0 \bmod N$ and $\det \sigma_\delta = 1$ give $(\sigma_\delta)_{11} \equiv \delta^{-1} \bmod N$.

### The law for a diamond translate

**Theorem 5.3.2 (coefficient law for a diamond translate).** Let $\ell$ be a prime, $N \geq 1$ and $w$ odd. There are $c_1 \in \mathbb{N}$ and $\kappa \in \mathbb{Q}$, $\kappa \neq 0$, with the following property. Take a tower $K$ and Siegel data $c, d, g_m$ with $g_m(r_0) \in \Gamma_1(N)$ for each $r_0$. Take a valuation ring $A$ of $\Omega$ with $\ell$ in its maximal ideal, $x \in \mathbb{Z}/N$, $1 \leq m \leq n$, $c_0 \in \mathbb{N}$, a lift $b$ with exponent $c_0$ in weight $w$, $y \in (\mathbb{Z}/\ell^m)^\times$ and $\delta \in (\mathbb{Z}/N)^\times$. Then there is a series $g$ with coefficients in $A$ such that the following holds. Let $s$ map $A$ onto $A$, act trivially on the residue field of $A$ and fix $\zeta_{\ell^m}$. Let $\varphi$ be a logarithmic derivative of $\langle \delta \rangle b^{\mathrm{bot}}(s, y)$ mod $\ell^n$, where $\delta$ is taken as its least residue. Let $t_t \in \mathbb{Z}/\ell^n$ with $s^{\ell^{n-m}}(\zeta_{\ell^{2n}}) = \zeta_{\ell^n}^{t_t} \zeta_{\ell^{2n}}$. Let $\beta \in \mathbb{N}$ and $t \in \mathbb{Z}$ with $\beta \equiv y \bmod \ell^m$, $\beta \equiv 1 \bmod N$ and $\ell^m t \equiv 1 \bmod N$. Let $\bar\delta$ be the least residue of $\delta^{-1}$. Then for each $i \in \mathbb{N}$,
$$\begin{aligned} \ell^{c_1} \varphi_i \equiv \ell^{c_1} \Bigl( &\ell^{c_0+m} \kappa\, t_t\, P^{(w+2)}_i\bigl(x t \bar\delta, t \bar\delta; \zeta_{N\ell^m}^{\beta}\bigr) \\ &+ s(g_i) - g_i \Bigr) \pmod{\ell^n A}. \end{aligned}$$

Lean: `UpperTheory.Kd.L.twist`

*Proof.* Take $c_1$ and $\kappa$ from the coefficient law for $\ell$, $N$ and $w$. Let $\sigma_\delta$ be the matrix of $\langle \delta \rangle$. It exists because $\delta$ is prime to $N$.

1. The map $r_0 \mapsto g_m(r_0) \sigma_\delta$ is again Siegel data. The conditions on the first column hold because $\sigma_\delta \in \Gamma_0(N) \cap \Gamma_0(\ell)$. The family $\sigma_\delta b$ is a lift with exponent $c_0$ in weight $w$ of the zeta classes for these new data, because the action of $\sigma_\delta$ permutes the image of $\Gamma$ by conjugation.
2. Apply the coefficient law to the new data and to the lift $\sigma_\delta b$, with $a = \bar\delta$.
3. The twisted Galois action commutes with $\sigma_\delta$ on $B_{N,\ell}(w)$. This is a form of the Shimura reciprocity law. So the fibre sum built from $\sigma_\delta b$ is $\langle \delta \rangle b^{\mathrm{bot}}(s, y)$, and $\varphi$ is a logarithmic derivative of it.
4. The law asks $a \equiv (g_m(1)\sigma_\delta)_{11} \bmod N$. Since $g_m(1) \in \Gamma_1(N)$, this entry is $(\sigma_\delta)_{11} \bmod N$, which is $\delta^{-1}$. So $a = \bar\delta$ is allowed.

The parameters $(x a t, a t)$ of the law are then $(x t \bar\delta, t \bar\delta)$. $\square$

### The law on inertia

Let $\overline{\mathbb{Q}}_\ell$ be an algebraic closure of $\mathbb{Q}_\ell$ with its absolute value. Let $j \colon \Omega \to \overline{\mathbb{Q}}_\ell$ be an embedding, and let $A = \{ z \in \Omega : |j(z)| \leq 1 \}$. We say $A$ *lies over $\ell$* if $A$ lies over a place of $\mathbb{Q}$ that contains $\ell$. For $a, b \in \overline{\mathbb{Q}}_\ell$, write $a \equiv b \pmod{\ell^n}$ when $|a - b| \leq |\ell^n|$.

**Definition 5.3.3.** Let $e \geq 1$, $N \in \mathbb{N}$ and $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$. Let $\mathrm{pr} \colon \mathcal{F} \to \overline{\mathbb{Q}}_\ell^2$ be a map and $\alpha \in \overline{\mathbb{Q}}_\ell$. The data are *admissible for zeta classes of weight $2e+1$* if:

1. $N \geq 5$ and $\ell \nmid N$;
2. each $g_m(r_0)$ lies in $\Gamma_1(N)$, and $g_m(r_0)_{21} \equiv -r_0\, g_m(r_0)_{11} \bmod \ell$;
3. $|\alpha| = 1$ and $\mathrm{pr}(U_\ell b) = \alpha\, \mathrm{pr}(b)$ for each $b \in B_{N,\ell}(2e-1)$, where $U_\ell$ is the Hecke operator at $\ell$.

The level $N = 4$ is not admissible, by clause 1.

**Theorem 5.3.4 (coefficient law on inertia).** Let $\ell$ be an odd prime and $K$ a tower over $\Omega$ whose modular invariant is holomorphic on $\mathbb{H}$. Let $j \colon \Omega \to \overline{\mathbb{Q}}_\ell$ be an embedding with $A = \{|j| \leq 1\}$ lying over $\ell$. Let $N \geq 1$ with $\ell \nmid N$. Let $c, d > 1$ be prime to $6\ell N$, let $e \geq 1$, and let $g_m \colon (\mathbb{Z}/\ell)^\times \to \mathrm{SL}_2(\mathbb{Z})$ be such that for each $r_0$ there is a unit $u$ mod $\ell$ with $(g_m(r_0)_{21}, g_m(r_0)_{22}) \equiv u\,(r_0, -1) \bmod \ell$, and $N \mid g_m(r_0)_{21}$. Let $\mathrm{pr}$ and $\alpha$ make the data admissible for zeta classes of weight $2e+1$. Then there are $c_1 \in \mathbb{N}$ and $\kappa_0 \in \overline{\mathbb{Q}}_\ell$, $\kappa_0 \neq 0$, with the following property. Take $x \in \mathbb{Z}/N$, $\delta \in \mathbb{N}$ prime to $N$, $1 \leq m \leq n$, $c_0 \in \mathbb{N}$, a lift $b$ with exponent $c_0$ in weight $2e-1$, and $y \in (\mathbb{Z}/\ell^m)^\times$. Then there is a series $g$ with coefficients in $A$ such that the following holds. Let $s$ be in the inertia group of $A$, with $\chi(s) \equiv 1 \bmod \ell^m$. Let $\varphi$ be a logarithmic derivative of $\langle \delta \rangle b^{\mathrm{bot}}(s, y)$ mod $\ell^n$. Let $t_t$, $\beta$ and $t$ be as in the previous theorem, and let $\bar\delta$ be the least residue of $\delta^{-1} \bmod N$. Then for each $i \in \mathbb{N}$,
$$\begin{aligned} \ell^{c_1} j(\varphi_i) \equiv \ell^{c_1} \Bigl( &\ell^{c_0 + m} \kappa_0\, t_t\, j\bigl(P^{(2e+1)}_i(x t \bar\delta, t \bar\delta; \zeta_{N\ell^m}^{\beta})\bigr) \\ &+ j(s(g_i)) - j(g_i) \Bigr) \pmod{\ell^n}. \end{aligned}$$

Lean: `UpperTheory.Kd.L.thcocd`

*Proof.* Put $w = 2e - 1$. It is odd, and $w + 2 = 2e+1$. Take $c_1$ and $\kappa$ from the previous theorem for $\ell$, $N$ and $w$, and put $\kappa_0 = \kappa$. The data $c, d, g_m$ are Siegel data:

1. $\ell \neq 2$, $N \geq 5$ and $\ell \nmid N$ come from the hypotheses and from admissibility;
2. the conditions on $c$ and $d$ are hypotheses;
3. $g_m(r_0) \in \Gamma_1(N)$ gives $g_m(r_0) \in \Gamma_0(N)$ and $g_m(r_0)_{11} \equiv 1 \equiv g_m(1)_{11} \bmod N$;
4. the congruence mod $\ell$ is clause 2 of admissibility.

Because $A$ lies over $\ell$, $\ell$ is in the maximal ideal of $A$. An element $s$ of the inertia group maps $A$ onto $A$ and acts trivially on its residue field. The condition $\chi(s) \equiv 1 \bmod \ell^m$ means that $s$ fixes $\zeta_{\ell^m}$. Apply the previous theorem to the unit $\delta$ mod $N$. It gives $a - b = \ell^n z$ with $z \in A$, so $|j(a) - j(b)| = |\ell^n|\,|j(z)| \leq |\ell^n|$. $\square$

**Theorem 5.3.5 (coefficient law on inertia, unit index).** Under the hypotheses of the previous theorem there are $c_1 \in \mathbb{N}$ and $\kappa_0 \in \overline{\mathbb{Q}}_\ell$, $\kappa_0 \neq 0$, with the same property, where now $\delta$ runs over $(\mathbb{Z}/N)^\times$, the diamond operator uses the least residue of $\delta$, and $\bar\delta$ is the least residue of the inverse unit $\delta^{-1}$.

Lean: `UpperTheory.Kd.L.thdiam`

*Proof.* Take $c_1$ and $\kappa_0$ from the previous theorem. For a unit $\delta$, its least residue is a natural number prime to $N$. Apply the previous theorem to it. The inverse of the residue of the least residue of $\delta$ is $\delta^{-1}$, so the two Eisenstein pieces agree. $\square$

The constants $c_1$ and $\kappa_0$ do not depend on $\delta$. This is what allows the average over $\delta$ in the coefficient law of the zeta argument.

**Remark 5.3.6 (Formalization).** The law for a diamond translate is in [Imports.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Imports.lean#L13). The file name does not say what the file holds. The hypothesis $g_m(r_0) \in \Gamma_1(N)$ is used only at $r_0 = 1$, in step 4. The matrix $\sigma_\delta$ is `sgD`, a choice by `Classical.epsilon` ([Letter.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/Letter.lean#L62)); for $\delta$ not prime to $N$ the operator `Tower.diam` is still defined, but on an unspecified matrix. Step 1 is `actcls` in [Actcls.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Actcls.lean#L161), and step 3 is `GlobalTheory.T.galB_act_comm_gamma0CapGamma0Level_shimuraReciprocity`, whose proof we have not unfolded. The law on inertia is in [Thcocd.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thcocd.lean#L13). Its row condition and its condition $N \mid g_m(r_0)_{21}$ are bound as `_hrow` and `_hN10` at [line 42](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thcocd.lean#L42) and never used; the second also follows from $\Gamma_1(N)$. The hypothesis that the modular invariant is holomorphic repeats the field `j_hol` of `Tower`, and it is cleared unused at line 96. The proof uses only clauses 1 and 2 of admissibility (`AdmissibleHodgeTateZetaClassParams`, [AdmissibleHodgeTateZetaClassParams.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/AdmissibleHodgeTateZetaClassParams.lean#L15)), so $\mathrm{pr}$, $\alpha$ and the eigenvalue condition play no role. We have not unfolded `heckeU`. The `example` at line 22 of that file shows that $N = 4$ fails. The unit-index form is in [Thdiam.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thdiam.lean#L12); it only reindexes the law on inertia, and passes the unused hypotheses on. The coefficients $j(\varphi_i)$ appear in the Lean statement as `seqN 1 j φ i`, and the congruence in $\overline{\mathbb{Q}}_\ell$ is `Cg`.
