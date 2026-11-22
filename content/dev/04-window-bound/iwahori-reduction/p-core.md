---
id: p-core
title: A power series for a norm-compatible system of Kummer cocycles
kind: theorem
decl: UpperTheory.Kd.C7.pCore
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.LangPolynomials.MemOfMulMem
covers: 463
status: drafted
drafted_by: writer@claude
---
To a norm-compatible system $(Z_m)$ of Kummer cocycles on inertia at a place $A$ over $\ell$, this theorem attaches a power series $G$ with integral coefficients ($\mathrm{SCore}$). Its twisted sums match the log-derivative sums of $(Z_m)$, and its moments vanish when those of $(Z_m)$ do. [`LocalUnitsRoots.main`](/entry/local-units-roots-main/) uses it with $d_0 = 2$. The shape is that of Coleman's power series for norm-compatible units (R. Coleman, Division values in local fields, Invent. Math. 53, 1979); the Lean code does not cite it.

## Statement

As in [`LocalUnitsRoots.main`](/entry/local-units-roots-main/), $x \equiv_n x'$ means $|x-x'| \le |\ell^n|$, and $I_r(G)$ is the moment of $G$ against $\varphi(x)x^k$. $H_m$ is the part of inertia at $A$ where the cyclotomic character mod $\ell^m$ is trivial.

Let $\ell \neq 2$, let $A$ lie over $\ell$, and suppose:

1. ($\mathrm{IwI}$) on inertia, $Z_r(s)$ is an integral function on $(\mathbb{Z}/\ell^r)^\times$, $Z_r$ is a cocycle for the shift by $\chi_r(s)^{-1}$, and the $Z_r$ are norm compatible;
2. $|a| = 1$, and $Z_m(\sigma s\sigma^{-1})(1) = a\,Z_m(s)(1)$ for every Frobenius $\sigma$ with $\bar\chi(\sigma) = 1$ and $s \in H_m$;
3. $j\colon \Omega \to \overline{\mathbb{Q}}_\ell$ is integral on $A$, $\ell \nmid d_0$, and $(\zeta_m)$ is a compatible system of primitive $\ell^m$-th roots of unity;
4. for $m \ge m_0$, $Z_m$ has a Kummer presentation (`KumPres`): polynomials $P_i$ over $A$ with inertia-fixed coefficients, and integral $o_i$, with, on $H_m$, $Z_m(s)(1) \equiv \sum_i o_i k_i(s)$ mod $\ell^{m-e_0}$, where $k_i$ is the Kummer character of the unit $P_i(\zeta_m)$.

**Theorem.** There are $G$ with integral coefficients, units $v_m$ with $v_{m+1} \equiv_m v_m$, and $c_1, m_1$ with two properties. Write $\zeta = \zeta_m$ and $\mathrm{tval}(G)(z) = \sum_{n<\ell^{3m}} G_n (z-1)^n$.

1. For $m \ge m_1$, every presentation as in 4 and every character $\psi$ mod $\ell^m$, the congruence $(\ast)$ below holds.
2. For each $\varphi$, $k \ge 1$ and $n$, $\mathrm{SpZero}(\varphi, k, Z)$ implies $I_r(G) \equiv_{n+r} 0$ for $r$ large.

$$\bigl(1 - d_0\psi^{-1}(d_0)\bigr)\sum_b \psi(b)\sum_i o_i\, j\Bigl(\tfrac{\zeta^b P_i'(\zeta^b)}{P_i(\zeta^b)}\Bigr) \equiv_{m-c_1} v_m a^m \sum_b \psi(b)\,\mathrm{tval}(G)\bigl(j(\zeta)^b\bigr). \qquad (\ast)$$

## Proof

1. **Frame.** `pFrEx3` gives a ring $R$ with a Frobenius lift and a Frobenius $\mathrm{fr}$; `pBasEx` gives a $\mathbb{Z}_\ell$-basis $\beta$ of the coefficient ring. `pToBasis` writes each presentation in $\beta$.
2. **Coleman vector.** Through `pContOf`, `pIwOps` and `pKumEx`, `pRepEx` gives power series $D_i$ over $R$ for the system $Z^\sharp = Z - d_0\,\mathrm{tr}_{d_0}Z$. Their $m$-th Frobenius twists agree, at level $m$ and to precision $m - c$, with the logarithmic derivative of $P_i(1+X)$.
3. **Eigenvector.** `sharp_eig` moves the Frobenius law to $Z^\sharp$. Then `pack` gives $G$ and a unit $v \in \mathbb{C}_\ell$ with $\sum_i \beta_i D_{i,n} = v\,G_n$, and $\mathrm{fr}$ acting on $D$ by $a$, or $G = 0$. `exists_approx` approximates $v$ by algebraic units $v_m$.
4. **Clause 1** is `pClause1` with `sum_step`; the factor $1 - d_0\psi^{-1}(d_0)$ comes from $Z^\sharp$.
5. **Clause 2.** `pDiv` gives $g$ prime to $\ell$, $c_2$ and a system $Z'$ with $\ell^{c_2}Z = \mathrm{tr}_g Z' - \theta Z'$ on $H_m$, where $\theta = \varphi(g)g^k$. If $\theta$ is integral, `pRepSmul`, `pRepAdd`, `pRepTr` and `pRepUniq` carry this relation to $D$, and `pClause2` concludes. If not, `mem_of_mul_mem` forces $Z'^\sharp = 0$. Then $Z^\sharp = 0$ on $H_m$, so $D = 0$, $G = 0$ and the moments vanish.

## In the Lean code

The theorem is at [MemOfMulMem.lean, line 253](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/MemOfMulMem.lean#L253). $\mathrm{SCore}$ is in [FixedIntegersIsUnitOfNotMemPrimeSpan.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/FixedIntegersIsUnitOfNotMemPrimeSpan.lean#L126). The file is named after the helper `mem_of_mul_mem` (line 92). We have not unfolded `pRepEx`, `pDiv`, `pClause1`, `pClause2` or the level-$m$ evaluation. In clause 1, $\psi$ need not be primitive.
