---
title: Zeros of residue series
decls:
  - GlobalTheory.T.exists_orthogonal_family_residue_zeros
  - GlobalTheory.CoreOrth.residue_zeros
  - GlobalTheory.CoreOrth.core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Zeros of residue series

An eigenvector $b$ of $\varphi^h$ in $B_{\mathrm{cris}}^+$ can be built from a sequence of elements of $\mathcal{O}_C^\flat$, and the residue of $\iota(\varphi^i b)$ modulo $\mathrm{Fil}^1$ is then given by a series in $\mathbb{C}_\ell$. This section proves that for a suitable family of coefficients $\mu_0, \dots, \mu_{h-1}$ in $\mathbb{C}_\ell$, there are sequences for which the $\mu$-combination of these series vanishes for all $i$, and one of which is not too small. The proof transfers [the window theorem](/entry/frobenius-polydisc-windows-surjective-bounds-zero/) from the tilt $C^\flat$ to $\mathbb{C}_\ell$ and corrects the error by successive approximation. The result is used to construct [a nonzero Frobenius vector with zero residues](/entry/exists-nonzero-frob-vector-residue-zero/).

We keep the notation of the previous sections: $\mathbb{C}_\ell$ is the completion of $\Omega$, $\mathcal{O}_C$ its ring of integers, and $\mathcal{O}_C^\flat$ the tilt of $\mathcal{O}_C$, a perfect ring of characteristic $\ell$. For $x \in \mathcal{O}_C^\flat$ let $x^\sharp \in \mathcal{O}_C \subset \mathbb{C}_\ell$ be its untilt. For $k \in \mathbb{Z}$ let $x \mapsto x^{\ell^k}$ be the $k$-th power of the Frobenius automorphism of $\mathcal{O}_C^\flat$.

We use these facts about the untilt, proved elsewhere in this development: $(xy)^\sharp = x^\sharp y^\sharp$; $|x^\sharp| \leq 1$; every $c \in \mathbb{C}_\ell$ with $|c| \leq 1$ is $x^\sharp$ for some $x$; and $|(x + y)^\sharp - x^\sharp - y^\sharp| \leq |\ell|$.

**Definition 6.18.1 (Residue series).** Let $h \geq 1$ and $j \geq 0$. For $x \in \mathcal{O}_C^\flat$ and for a sequence $y = (y_k)_{k \geq 0}$ in $\mathcal{O}_C^\flat$, put
$$\Lambda_{h,j}(x) = \sum_{n \in \mathbb{Z}} \ell^{-n} \big( x^{\ell^{nh + j}} \big)^\sharp, \qquad A_{h,j}(y) = \sum_{k \geq 0} \ell^k\, \Lambda_{h,j}(y_k),$$
in $\mathbb{C}_\ell$. Each sum is taken to be $0$ if it does not converge.

If $|x^\sharp| \leq R < 1$, the terms of $\Lambda_{h,j}(x)$ tend to $0$ in both directions: for $n \to -\infty$ because of the factor $\ell^{-n}$, and for $n \to +\infty$ because $|x^\sharp|^{\ell^{nh+j}}$ falls faster than $|\ell|^{-n}$ grows. So the series converges, and $|\Lambda_{h,j}(x)|$ is bounded. Then $A_{h,j}(y)$ also converges.

The proof uses the following further facts, proved elsewhere in this development. In all of them, $F$ is a field with a nontrivial ultrametric absolute value, of characteristic $\ell$ and perfect; $\iota : \mathcal{O}_C^\flat \to F$ is a ring homomorphism; and $\theta : F \to \mathbb{C}_\ell$ is a multiplicative map with $\theta(0) = 0$, $|\theta(z)| = |z|$ and $\theta(\iota(x)) = x^\sharp$, such that every $z \in F$ with $|z| \leq 1$ is $\iota(x)$ for some $x$.

1. (Orthogonality.) Let $m \in (\mathcal{O}_C^\flat)^h$ with $|m_i^\sharp| < \ell\, |m_j^\sharp|$ for all $i, j$, and with $|c_j|\,|m_j^\sharp| \leq |\sum_i c_i m_i^\sharp|$ for all $c \in \mathbb{Q}_\ell^h$ and all $j$. Then for $c \in \mathbb{Z}^h$ and $j$ with $\ell \nmid c_j$, $|m_j^\sharp| \leq |(\sum_i c_i m_i)^\sharp|$.
2. (Surjectivity.) $\theta$ is onto $\mathbb{C}_\ell$.
3. (Truncation.) Let $h \geq 1$, $m, x \in (\mathcal{O}_C^\flat)^h$ with $|x_j^\sharp| < 1$, $\varpi \in F$ with $\theta(\varpi) = \ell$, $K \geq 0$, $r < h$ and $\tau_r \in \mathbb{R}$. Assume that the terms $T_{r,j,n}$ of the window rows for the family $\iota(m)$ at the point $\iota(x)$ satisfy $|T_{r,j,n}| \leq \tau_r$ for all $j, n$, and $|T_{r,j,n}| \leq \tau_r/\ell$ for $|n| > K$. Then
$$\Big| \sum_j m_j^\sharp\, \Lambda_{h,r}(x_j) - \theta\big( R_K(\iota(x))_r \big) \Big| \leq |\ell|\, \tau_r.$$
4. (Successive approximation.) Let $X$ and $I$ be sets, $\eta : X \to \mathbb{C}_\ell^I$ a map, $\tau \in \mathbb{R}^I$ and $S \subseteq X$. Assume that for every $t$ with $|t_i| \leq \tau_i$ for all $i$ there is $y \in S$ with $|\eta(y)_i - t_i| \leq |\ell|\,\tau_i$ for all $i$. Then for every $x \in S$ with $|\eta(x)_i| \leq |\ell|\,\tau_i$ for all $i$, there is a sequence $(y_k)_{k \geq 0}$ in $S$ with $y_0 = x$ such that $\sum_{k \geq 0} \ell^k \eta(y_k)_i$ converges to $0$ for every $i$.
5. (Double series.) Let $h \geq 1$, $\rho < 1$, $\mu \in \mathbb{C}_\ell^h$, $i \geq 0$, and $y_{k,j} \in \mathcal{O}_C^\flat$ with $|y_{k,j}^\sharp| \leq \rho$. If $\sum_{k \geq 0} \ell^k \sum_j \mu_j \Lambda_{h,i}(y_{k,j})$ converges to $0$, then $\sum_j \mu_j A_{h,i}(y_{\bullet, j}) = 0$.
6. (The tilt of $\mathbb{C}_\ell$.) The tilt $C^\flat$ of $\mathbb{C}_\ell$ is algebraically closed, and there is a ring homomorphism $\iota : \mathcal{O}_C^\flat \to C^\flat$ onto the unit ball of $C^\flat$ with $\iota(x)^\sharp = x^\sharp$. The sharp map $C^\flat \to \mathbb{C}_\ell$ is multiplicative, sends $0$ to $0$ and preserves absolute values.

Fact 4 is the usual way to pass from an approximate solution to an exact one: solve up to an error of size $|\ell|\tau$, divide the error by $\ell$, and repeat.

**Theorem 6.18.2 (Residue zeros, abstract form).** Let $F$ be a field with a nontrivial ultrametric absolute value, complete, algebraically closed, of characteristic $\ell$ and perfect. Let $\iota : \mathcal{O}_C^\flat \to F$ be a ring homomorphism and $\theta : F \to \mathbb{C}_\ell$ a multiplicative map with $\theta(0) = 0$, such that $|\theta(z)| = |z|$ for all $z$, $\theta(\iota(x)) = x^\sharp$ for all $x$, and every $z \in F$ with $|z| \leq 1$ is $\iota(x)$ for some $x$. Let $h \geq 2$ and $\mu \in \mathbb{C}_\ell^h$, and assume:

1. $\mu_i \neq 0$ and $|\mu_i| \leq 1$ for all $i$, and $|\mu_i|$ is decreasing in $i$;
2. $|\mu_i| < \ell\, |\mu_j|$ for all $i, j$;
3. $|c_j|\,|\mu_j| \leq |\sum_i c_i \mu_i|$ for all $c \in \mathbb{Q}_\ell^h$ and all $j$.

Then there are sequences $y_a = (y_{a,k})_{k \geq 0}$ in $\mathcal{O}_C^\flat$ for $a < h$, an index $j_0 < h$ and real numbers $r, R$ such that $0 \leq r < 1$, $R < 1$, $|y_{a,k}^\sharp| \leq R$ for all $a, k$, $|y_{j_0,k}^\sharp| \leq r$ for all $k$, $r^{\ell^h} < |y_{j_0,0}^\sharp|$, and
$$\sum_{j=0}^{h-1} \mu_j\, A_{h,i}(y_j) = 0 \quad \text{for every } i < h.$$

Lean: `GlobalTheory.CoreOrth.core`.

Condition 3 says that $\mu$ is an orthogonal family over $\mathbb{Q}_\ell$. The sequence $y_{j_0}$ is the one that is not too small: its first term lies outside the disc of radius $r^{\ell^h}$.

*Proof.* Step 1: lifting the data to $F$. Since $|\mu_j| \leq 1$ and $|\ell| \leq 1$, there are $m_j \in \mathcal{O}_C^\flat$ with $m_j^\sharp = \mu_j$ and $w \in \mathcal{O}_C^\flat$ with $w^\sharp = \ell$. Put $\varpi = \iota(w)$ and $\lambda_j = \iota(m_j)$. Then $|\varpi| = |\theta(\varpi)| = |w^\sharp| = 1/\ell$, $\theta(\varpi) = \ell$, and $|\lambda_j| = |\mu_j|$. So $\lambda_j \neq 0$, $|\lambda_j|$ is decreasing, and $|\lambda_i| < \ell\,|\lambda_j|$. The family $\lambda$ is orthogonal modulo $\ell$: for $c \in \mathbb{Z}^h$, $\sum_i c_i \lambda_i = \iota(\sum_i c_i m_i)$, whose absolute value is $|(\sum_i c_i m_i)^\sharp|$, and fact 1 gives the bound.

Step 2: the window. [The window theorem](/entry/frobenius-polydisc-windows-surjective-bounds-zero/), with $p = \ell$, gives $\rho$, $\tau$ and $K$ with its four properties. Let $S$ be the set of $x \in (\mathcal{O}_C^\flat)^h$ with $|x_j^\sharp| \leq \rho_j$ for all $j$, and define
$$\eta(x)_i = \sum_j \mu_j\, \Lambda_{h,i}(x_j).$$
For $x \in S$, the point $\iota(x)$ satisfies $|\iota(x_j)| = |x_j^\sharp| \leq \rho_j < 1$, so part 2 of the window theorem bounds its terms. Fact 3 gives
$$|\eta(x)_i - \theta(R_K(\iota(x))_i)| \leq |\ell|\,\tau_i \quad \text{for } x \in S.$$
Every $z \in F^h$ with $|z_j| \leq \rho_j$ is $\iota(x)$ for some $x \in S$, since $\rho_j < 1$ and $\iota$ is onto the unit ball.

Step 3: approximate solutions. Let $t \in \mathbb{C}_\ell^h$ with $|t_i| \leq \tau_i$. By fact 2 there are $b_i \in F$ with $\theta(b_i) = t_i$, so $|b_i| = |t_i| \leq \tau_i$. Part 3 of the window theorem gives $z$ with $|z_j| \leq \rho_j$ and $R_K(z) = b$. Write $z = \iota(x)$ with $x \in S$. Then $|\eta(x)_i - t_i| \leq |\ell|\,\tau_i$ by step 2.

Step 4: the starting point. Part 4 of the window theorem gives $z^0$ with $|z^0_j| \leq \rho_j$, an index $j_0$ with $|z^0_{j_0}| > \rho_{j_0}^{\ell^h}$, and $R_K(z^0) = 0$. Write $z^0 = \iota(x^0)$ with $x^0 \in S$. Since $\theta(0) = 0$, step 2 gives $|\eta(x^0)_i| \leq |\ell|\,\tau_i$.

Step 5: the exact zero. By steps 3 and 4, fact 4 applies. It gives $y_k \in S$ with $y_0 = x^0$ and $\sum_k \ell^k \eta(y_k)_i = 0$ for every $i$. Write $y_{a,k}$ for the $a$-th entry of $y_k$. Put $R = \max_j \rho_j$ and $r = \rho_{j_0}$. Then $0 \leq r < 1$, $R < 1$, $|y_{a,k}^\sharp| \leq \rho_a \leq R$, and $|y_{j_0,k}^\sharp| \leq r$. Also $|y_{j_0,0}^\sharp| = |\iota(x^0_{j_0})| = |z^0_{j_0}| > r^{\ell^h}$. Finally, fact 5 with $\rho = R$ turns $\sum_k \ell^k \eta(y_k)_i = 0$ into $\sum_j \mu_j A_{h,i}(y_j) = 0$. $\square$

**Theorem 6.18.3 (Residue zeros).** Let $h \geq 2$ and $\mu \in \mathbb{C}_\ell^h$ satisfy conditions 1 to 3 of the [Theorem 6.18.2](/entry/core-orth-core/) above. Then there are sequences $y_a$ in $\mathcal{O}_C^\flat$ for $a < h$, an index $j_0$ and real numbers $r, R$ with the same properties: $0 \leq r < 1$, $R < 1$, $|y_{a,k}^\sharp| \leq R$, $|y_{j_0,k}^\sharp| \leq r$, $r^{\ell^h} < |y_{j_0,0}^\sharp|$, and $\sum_j \mu_j A_{h,i}(y_j) = 0$ for every $i < h$.

Lean: `GlobalTheory.T.exists_orthogonal_family_residue_zeros` (also `GlobalTheory.CoreOrth.residue_zeros`, a second name).

*Proof.* This is the abstract form applied to $F = C^\flat$, with $\iota$ and the sharp map $\theta : C^\flat \to \mathbb{C}_\ell$ of fact 6. $\square$

**Remark 6.18.4 (Formalization).** The series $\Lambda_{h,j}$ and $A_{h,j}$ are the definitions `GlobalTheory.PSer.lam` and `GlobalTheory.PSer.abelian₂` ([ImportsAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ImportsAlt.lean#L17)). They are `tsum`s, so they are $0$ when the series does not converge; the bounds $R < 1$ in the conclusion keep the series in the convergent range. The map $\theta$ is a `MonoidWithZeroHom`, so it is not assumed additive. In the abstract form, the completeness and algebraic closure of $F$ are used only through the window theorem. The six facts are wrappers in the namespace `GlobalTheory.T`, and the untilt facts come from `GlobalTheory.PSer.Laws.sh_laws`.
