---
title: Transfer of nonvanishing between power series
decls:
  - GlobalTheory.T.nonvanishing_transfer_characterSums_powerSeries
  - GlobalTheory.KZ.Cmp.nonvanishing_transfer
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Transfer of nonvanishing between power series

Two power series with integral coefficients define two measures on $\mathbb{Z}_\ell^\times$. Assume that their twisted character sums agree at all levels, up to units, a constant and a smoothing factor. This section proves that, if the moments of the first measure do not vanish, then neither do the moments of the second. The proof passes to the Mellin transforms of the two measures, uses the character sums to compare their values at roots of unity, and concludes with the Weierstrass preparation theorem. The result is the transfer hypothesis of [the theorem on nonvanishing on inertia](/entry/p-locu/): there the second series is the Coleman series of an Euler system and the first is a known series with nonzero moments.

### Notation

Let $\ell$ be an odd prime and $\mathcal{O} \subseteq \overline{\mathbb{Q}}_\ell$ the ring of a coefficient datum. For $x, x' \in \overline{\mathbb{Q}}_\ell$ write $x \equiv_n x'$ if $|x - x'| \leq |\ell^n|$. For a power series $F = \sum_n F_n X^n$ over $\overline{\mathbb{Q}}_\ell$ and $N \geq 0$ put
$$
\mathrm{tv}_N(F)(z) = \sum_{n < N} F_n (z - 1)^n,
$$
the value of $F$ at $z - 1$, truncated at degree $N$. For $|z - 1| < 1$ and $F$ integral, $\mathrm{tv}_N(F)(z)$ converges to $F(z - 1)$ as $N \to \infty$. We write $\mathrm{tv}_m(F)$ for $\mathrm{tv}_{\ell^{3m}}(F)$ when the argument is a root of unity of order $\ell^m$.

**Definition 6.19.1 (Character sums and moments).** Let $m \geq 1$, $z$ a primitive $\ell^m$-th root of unity and $\psi$ a [[Dirichlet character|JR4QSEFXWF]] modulo $\ell^m$. Put
$$
S_m(F; z, \psi) = \sum_{b \in (\mathbb{Z}/\ell^m)^\times}\psi(b)\,\mathrm{tv}_m(F)(z^b), \qquad g_m(z, \psi) = \sum_{b \in (\mathbb{Z}/\ell^m)^\times}\psi(b)\,z^b,
$$
with $b$ read as its least nonnegative representative. Let $\varphi$ be a character modulo $\ell$ and $e \geq 1$. For $r \geq 1$ and a primitive $\ell^r$-th root of unity $\xi$, the *moment* of $F$ is
$$
I_r(F; \xi) = \sum_{\substack{0 < x < \ell^r \\ \ell \nmid x}} \varphi(x)\,x^e \sum_{k < \ell^r}\xi^{-kx}\,\mathrm{tv}_r(F)(\xi^k).
$$

The series $F(X)$ is the Amice transform of a measure $\mu_F$ on $\mathbb{Z}_\ell$: $F(z - 1) = \int z^x\,d\mu_F(x)$. Then $S_m(F; z, \psi)$ is the integral of $\psi(b)z^b$ in $b$, a twisted value. The inner sum in $I_r$ is $\ell^r$ times the mass of $\mu_F$ on $x + \ell^r\mathbb{Z}_\ell$, up to truncation. So $I_r(F; \xi)$ is $\ell^r$ times a Riemann sum for $\int_{\mathbb{Z}_\ell^\times}\varphi(x)x^e\,d\mu_F$. For measures and their transforms, see L. C. Washington, *Introduction to Cyclotomic Fields*, Chapter 12.

### The theorem

**Theorem 6.19.2 (Transfer of nonvanishing).** Let $e \geq 1$, $m_0 \geq 2$, $c_1, n_0 \geq 0$, and $c_0 \geq 2$ with $\ell \nmid c_0$. Let $G$ and $L$ be power series with coefficients in $\mathcal{O}$, $a, a' \in \overline{\mathbb{Q}}_\ell$ with $|a| = |a'| = 1$, $\kappa \neq 0$, and $v_m, v'_m$ with $|v_m| = |v'_m| = 1$, $v_{m+1} \equiv_m v_m$ and $v'_{m+1} \equiv_m v'_m$. Let $\varphi$ be a character modulo $\ell$. Assume:

1. for each $m \geq m_0$ there is a primitive $\ell^m$-th root of unity $z$ such that, for each primitive character $\psi$ modulo $\ell^m$,
$$
\bigl(1 - c_0\psi^{-1}(c_0)\bigr)\,v'_m\,\kappa\,a'^m\,S_m(L; z, \psi) \equiv_{m - c_1} v_m\,a^m\,S_m(G; z, \psi);
$$
2. there is $r_1$ such that $I_r(L; \xi) \not\equiv_{n_0 + r} 0$ for all $r \geq \max(r_1, 1)$ and all primitive $\ell^r$-th roots of unity $\xi$.

Then there are $n_1$ and $r_2$ such that $I_r(G; \xi) \not\equiv_{n_1 + r} 0$ for all $r \geq r_2$ and all primitive $\ell^r$-th roots of unity $\xi$.

Lean: `GlobalTheory.KZ.Cmp.nonvanishing_transfer` (also `GlobalTheory.T.nonvanishing_transfer_characterSums_powerSeries`, a second name).

The factor $1 - c_0\psi^{-1}(c_0)$ comes from the smoothing of a zeta class by $c_0$, as in [the Hodge-Tate law for smoothed zeta classes](/entry/k5-top/). The conclusion is "$\ell^{-r}I_r(G; \xi)$ stays away from $0$".

We use three lemmas on power series over $\mathcal{O}$.

**Lemma 6.19.3 (Mellin transform).** Assume that $\mathcal{O}$ contains the $(\ell - 1)$-th roots of unity. Let $F$ have coefficients in $\mathcal{O}$ and $d \geq 1$. There is a power series $A$ with coefficients in $\mathcal{O}$ such that:

1. for $r \geq 1$ and each primitive $\ell^r$-th root of unity $\xi$, $d^e\varphi(d)\,I_r(F; \xi) \equiv_{2r} \ell^r\,\mathrm{tv}_r(A)\bigl((1 + \ell)^e\bigr)$;
2. for $k \geq 1$, a primitive $\ell^{k+1}$-th root of unity $z$, and a primitive character $\psi$ modulo $\ell^{k+1}$ with $\psi^{-1}(b)$ congruent to $b^e\varphi(b)$ modulo the maximal ideal for each $b$ with $b^{\ell-1} = 1$: if $\zeta = \psi^{-1}(1 + \ell)$ and $\zeta^{\ell^k} = 1$, then
$$
\psi^{-1}(d)\,S_{k+1}(F; z, \psi) \equiv_{k+1} g_{k+1}(z, \psi)\,\mathrm{tv}_{\ell^{3k}}(A)(\zeta).
$$

Here $\mathrm{tv}_r$ in part 1 is the truncation at degree $r$. The series $A$ is the Mellin transform of the restriction of $\mu_F$ to $\mathbb{Z}_\ell^\times$, twisted by $\varphi$ and by $x^e$, with the factor $d$ inserted: $A((1+\ell)^s - 1)$ is the integral of $\varphi(x)\,x^e\,\langle x\rangle^{s}$, roughly, where $\langle x\rangle$ is the projection of $x$ to $1 + \ell\mathbb{Z}_\ell$. Part 1 is the value at $s = e$ (more precisely at $(1 + \ell)^e$), and part 2 is the value at a character of finite order of $1 + \ell\mathbb{Z}_\ell$.

**Lemma 6.19.4 (Identity from values at roots of unity).** Let $A$ and $B \neq 0$ have coefficients in $\mathcal{O}$, $|u| = 1$, and $w_m$ with $|w_m| = 1$ and $w_{m+1} \equiv_m w_m$. Let $c, m_0 \geq 0$, and assume that for $m \geq m_0$ and each primitive $\ell^m$-th root of unity $z$,
$$
\mathrm{tv}_m(A)(z) \equiv_{\lfloor m/2\rfloor - c} w_m\,u^m\,\mathrm{tv}_m(B)(z).
$$
Then $u = 1$, and for each $k$ there is $m_1$ such that $A_n \equiv_k w_m B_n$ for all $m \geq m_1$ and all $n$.

This is a uniqueness statement for power series over $\mathcal{O}$ that rests on the Weierstrass preparation theorem: a nonzero series over $\mathcal{O}$ has only finitely many zeros in the open unit disc. See Washington, *Introduction to Cyclotomic Fields*, §7.1.

**Lemma 6.19.5 (Comparison of values).** If $A_n \equiv_k w_m B_n$ for all $n$, for each $k$ and all large $m$, with $|w_m| = 1$, then $|\mathrm{tv}_N(B)(y)| \leq |\mathrm{tv}_N(A)(y)|$ for every $N$ and every $y$ with $|y - 1| \leq 1$.

Indeed $\mathrm{tv}_N(A)(y) - w_m\mathrm{tv}_N(B)(y)$ is a finite sum of terms of size at most $|\ell^k|$, for every $k$.

*Proof of the theorem.* Choose $N$ with $|\ell^N\kappa| \leq 1$ and put $p = \ell^N$. Enlarge $\mathcal{O}$ to the ring of a coefficient datum that contains $p\kappa$ and the $(\ell - 1)$-th roots of unity.

*Step 1: transforms.* Let $A_G$ be the Mellin transform of $G$ with $d = 1$, and $A_1$, $A_2$ those of $L$ with $d = 1$ and $d = c_0$. Put $A_L = A_1 - c_0A_2$. By part 1 of the Mellin lemma,
$$
f\,I_r(L; \xi) \equiv_{2r} \ell^r\,\mathrm{tv}_r(A_L)\bigl((1 + \ell)^e\bigr), \qquad f = 1 - c_0\cdot c_0^e\varphi(c_0),
$$
and by part 2, for $\psi$ and $\zeta$ as there,
$$
\bigl(1 - c_0\psi^{-1}(c_0)\bigr)\,S_{k+1}(L; z, \psi) \equiv_{k+1} g_{k+1}(z, \psi)\,\mathrm{tv}_{\ell^{3k}}(A_L)(\zeta).
$$
So $A_L$ is the transform of the measure of $L$ smoothed by $c_0$. We have $f \neq 0$, since $c_0^{e+1}\varphi(c_0) = 1$ would make the root of unity $\varphi(c_0)$ equal to the rational number $c_0^{-e-1}$, which has absolute value less than $1$ in $\mathbb{C}$.

*Step 2: a lower bound for $A_L$.* Fix a primitive $\ell^r$-th root of unity $\xi_r$ for each $r$. By hypothesis 2, $|f\,I_r(L; \xi_r)| > |f|\,|\ell^{n_0 + r}|$. Compare with the congruence of Step 1: for large $r$ the error $|\ell^{2r}|$ is smaller, so $|\ell^r\,\mathrm{tv}_r(A_L)((1+\ell)^e)| > |f|\,|\ell^{n_0 + r}|$. Hence there are $\delta > 0$ and $R$ with $|\mathrm{tv}_r(A_L)((1 + \ell)^e)| > \delta$ for $r \geq R$. In particular $A_L \neq 0$.

*Step 3: values at roots of unity.* Let $k \geq m_0 + 2c_1$ and let $\zeta$ be a primitive $\ell^k$-th root of unity. There is a primitive character $\psi$ modulo $\ell^{k+1}$ with $\psi^{-1}(1 + \ell) = \zeta$ and in the component of part 2. Take $z$ from hypothesis 1 at $m = k + 1$. Part 2 of the Mellin lemma for $G$ and Step 1 for $L$ express $S_{k+1}(G; z, \psi)$ and $(1 - c_0\psi^{-1}(c_0))S_{k+1}(L; z, \psi)$ as the Gauss sum $g_{k+1}(z, \psi)$ times values of $A_G$ and $A_L$ at $\zeta$. The Gauss sum satisfies $g_{k+1}(z, \psi)\,g_{k+1}(z^{-1}, \psi^{-1}) = \ell^{k+1}$, and the second factor has absolute value at most $|\ell|^{(k+1)/2}$. So we can divide hypothesis 1 by $g_{k+1}(z, \psi)$ and lose at most half of the precision. The result is
$$
p\,\mathrm{tv}(A_G)(\zeta) \equiv_{\lfloor k/2\rfloor - c_1} \frac{v'_{k+1}}{v_{k+1}}\cdot\frac{a'}{a}\cdot\Bigl(\frac{a'}{a}\Bigr)^k\,p\kappa\,\mathrm{tv}(A_L)(\zeta).
$$
The factors $w_k = (v'_{k+1}/v_{k+1})(a'/a)$ are units with $w_{k+1} \equiv_k w_k$.

*Step 4: conclusion.* The identity lemma, applied to $pA_G$, $p\kappa A_L \neq 0$, $u = a'/a$ and $w$, gives $p(A_G)_n \equiv_k w_m\,p\kappa(A_L)_n$ for all $n$ and all large $m$. The comparison lemma at $y = (1 + \ell)^e$, where $|y - 1| \leq 1$, gives
$$
|p\kappa|\,\delta < |p\kappa|\,\bigl|\mathrm{tv}_r(A_L)(y)\bigr| \leq |p|\,\bigl|\mathrm{tv}_r(A_G)(y)\bigr| \leq \bigl|\mathrm{tv}_r(A_G)(y)\bigr|
$$
for $r \geq R$. By part 1 of the Mellin lemma for $G$ with $d = 1$, $I_r(G; \xi) \equiv_{2r} \ell^r\,\mathrm{tv}_r(A_G)(y)$ for each primitive $\xi$. Since $|\ell^r\,\mathrm{tv}_r(A_G)(y)| > |\ell^r|\,|p\kappa|\,\delta$ and the error is at most $|\ell^{2r}|$, there is $n_1$ with $I_r(G; \xi) \not\equiv_{n_1 + r} 0$ for all large $r$. $\square$

The identity lemma also gives $a = a'$. So the hypothesis can hold only with equal units $a$ and $a'$, once $A_L \neq 0$.

**Remark 6.19.6 (Formalization).** The second name is a wrapper of the form `first | exact @… | …`. The three lemmas are `GlobalTheory.KZ.Cmp.mellin_comp`, `GlobalTheory.T.powerSeries_eq_of_congruent_values_at_primitiveRoots` (a wrapper of `GlobalTheory.KZ.autoPin_congr`) and `GlobalTheory.KZ.Cmp.norm_tval_le_of_coeff_cg`. The Gauss sum facts are `GlobalTheory.T.gaussSumModPrimePower_mul_inv_eq_prime_pow` and `GlobalTheory.T.norm_gaussSumModPrimePower_le_half_power`, and the choice of $\psi$ in Step 3 is `GlobalTheory.T.exists_primitive_character_twist`. We read the Mellin lemma, the identity lemma and these facts as statements; the description of $A$ as a Mellin transform is ours. In the moments, the power $\xi^{-kx}$ is written as $\xi^{\ell^r - (kx \bmod \ell^r)}$ (the definition `mass`). In part 1 of the Mellin lemma the truncation is at degree $r$, while the character sums use degree $\ell^{3m}$ ([NonvanishingTransferCharacterSumsPowerSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/NonvanishingTransferCharacterSumsPowerSeries.lean#L199)).
