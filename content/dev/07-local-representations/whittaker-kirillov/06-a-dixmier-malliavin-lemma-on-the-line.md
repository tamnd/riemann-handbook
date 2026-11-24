---
title: A Dixmier-Malliavin lemma on the line
decls:
  - GroundTheory.Automorphic.exists_dixmierMalliavin_line
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Dixmier-Malliavin lemma on the line

The archimedean Kirillov theory of the next two sections builds functions as integrals of translates against kernels of rapid decay. The basic tool for such constructions is the factorization theorem of Dixmier and Malliavin: a smooth vector of a representation of a Lie group is a finite sum of smoothed vectors. This section proves its one-variable core. The value of a smooth function at $0$ is a convergent series of integrals of its derivatives against one fixed smooth kernel, plus one more integral against a second smooth kernel. The result is used below the step [EveryCharacter from the Galois row](/step/every-character/). For smooth functions and the Fourier transform, see [continuity and smooth functions](/learn/analysis/#continuity-and-smooth-functions) and [the Fourier transform](/learn/analysis/#the-fourier-transform).

**Theorem 4.6.1 (Dixmier-Malliavin on the line).** Let $(M_p)_{p \geq 0}$ be a sequence of real numbers and let $\varepsilon > 0$. There are real numbers $c_p$ and smooth functions $g, h \colon \mathbb{R} \to \mathbb{C}$ with supports in $[-\varepsilon, \varepsilon]$, with $\sum_p |c_p|\, M_p$ convergent, such that the following holds. For each smooth $F \colon \mathbb{R} \to \mathbb{C}$ with $|F^{(p)}(t)| \leq M_p$ for all $p \geq 0$ and $t \in [-\varepsilon, \varepsilon]$,
$$F(0) = \sum_{p \geq 0} c_p \int_{\mathbb{R}} F^{(p)}(t)\, g(t)\, dt + \int_{\mathbb{R}} F(t)\, h(t)\, dt.$$

Lean: `GroundTheory.Automorphic.exists_dixmierMalliavin_line`.

The kernels do not depend on $F$; only the bounds $M_p$ enter. In the proof the supports of $g$ and $h$ are even in $[0, \varepsilon/2]$.

### One step of integration by parts

Fix a smooth function $s$ on $\mathbb{R}$ that is $0$ on $(-\infty, 0]$ and $1$ on $[1, \infty)$. For $r > 0$ put $\chi_r(t) = 1 - s(t/r - 1)$. Then $\chi_r = 1$ on $(-\infty, r]$ and $\chi_r = 0$ on $[2r, \infty)$.

**Definition 4.6.2 (Elementary kernel).** For $a, r > 0$ put
$$k_{a,r}(t) = \begin{cases} a e^{-at}\chi_r(t) & t \geq 0, \\ 0 & t < 0, \end{cases} \qquad \eta_{a,r}(t) = -e^{-at}\chi_r'(t).$$

The kernel $k_{a,r}$ is nonnegative with support in $[0, 2r]$ and total mass at most $1$. The function $\eta_{a,r}$ is smooth with support in $[r, 2r]$.

**Lemma 4.6.3 (One step).** For smooth $F$,
$$F(0) = \int (F - a^{-1}F')\, k_{a,r} + \int F\, \eta_{a,r}.$$

*Proof.* Integrate the derivative of $e^{-at}\chi_r(t)F(t)$ over $[0, \infty)$. The boundary terms are $-F(0)$ at $0$ and $0$ at $2r$. The derivative is $-ae^{-at}\chi_r F + e^{-at}\chi_r' F + e^{-at}\chi_r F'$. Divide the identity into its three terms and rearrange. $\square$

### Iteration

Choose numbers $a_0, a_1, \ldots > 0$ (below) and radii $r_j = \varepsilon/2^{j+3}$. Let $K_n = k_{a_0, r_0} * \cdots * k_{a_n, r_n}$. It is nonnegative, of mass at most $1$, with support in $[0, \sum_{j \leq n} 2r_j] \subset [0, \varepsilon/2]$. Define the numbers $c_n(p)$ by $c_0(p) = \delta_{p0}$, $c_{n+1}(0) = c_n(0)$ and
$$c_{n+1}(p+1) = c_n(p+1) + c_n(p)/a_n.$$
So $\sum_p c_n(p) X^p = \prod_{j < n}(1 + a_j^{-1}X)$, and the operator $T_n F = \sum_p (-1)^p c_n(p) F^{(p)}$ is the product of the operators $1 - a_j^{-1}\frac{d}{dt}$ for $j < n$. The numbers $c_n(p)$ are nonnegative, they are $0$ for $p > n$, and they increase with $n$.

**Lemma 4.6.4 (Stage identity).** There are smooth functions $\rho_j$ with compact support in $[0, \varepsilon/2]$, built from $K_{j-1} * \eta_{a_j, r_j}$ and its derivatives, such that for smooth $F$ and each $n$,
$$F(0) = \int T_{n+1}F \cdot K_n + \sum_{j \leq n} \int F \rho_j.$$

*Proof.* Induction on $n$. The case $n = 0$ is the one step lemma. For the step from $n$ to $n + 1$, apply the one step lemma to the function $T_{n+1}F$ translated along the kernel $K_n$, with $a = a_{n+1}$ and $r = r_{n+1}$. The recursion for $c_n(p)$ is the identity $T_{n+2} = (1 - a_{n+1}^{-1}\frac{d}{dt}) T_{n+1}$. The new remainder is the integral of $T_{n+1}F$ against $K_n * \eta_{a_{n+1}, r_{n+1}}$; integration by parts moves the derivatives of $T_{n+1}$ onto the kernel and gives $\rho_{n+1}$. $\square$

### Choice of the constants

Put $w(0) = 1$ and $w(p) = 2^{-p}/\max(1, |M_p|)$ for $p \geq 1$. Then $w(p)|M_p| \leq 2^{-p}\max(1, |M_0|)$. We choose $a_j$ so large that:

1. $a_j^{-1} w(p - 1) \leq 2^{-(j+1)} w(p)$ for $1 \leq p \leq j + 1$;
2. the derivatives of $\eta_{a_j, r_j}$ of order at most $2j + 2$ are bounded by $2^{-j}/(j + 2)$;
3. $e^{-a_j r_j} \leq 2^{-j}$.

Each condition holds for all large $a_j$, so such a choice exists. Condition 1 and the recursion give $c_n(p) \leq w(p)$ for all $n$ by induction. Condition 2 gives bounds on the derivatives of $\rho_j$ that are summable in $j$. Condition 3 controls the difference of the Fourier transforms of $K_n$ and $K_{n+1}$.

*Proof of the theorem.* The sequence $c_n(p)$ is increasing and bounded by $w(p)$, so it has a limit $c(p) \leq w(p)$. Put $c_p = (-1)^p c(p)$. Then $\sum_p |c_p| M_p$ converges, since $|c_p| |M_p| \leq w(p) |M_p|$.

By condition 2, the series $h = \sum_j \rho_j$ converges with all its derivatives, so $h$ is smooth with support in $[0, \varepsilon/2]$. For $F$ as in the theorem, $\sum_{j \leq n} \int F \rho_j \to \int F h$.

The Fourier transforms $\hat K_n(\xi)$ form a Cauchy sequence for each $\xi$: by condition 3 and the form of $\hat k_{a,r}$, $|\hat K_{n+1}(\xi) - \hat K_n(\xi)|$ is bounded by $C|\xi| 2^{-n} + 2^{-(n+1)}$. They also decay like $(1 + |\xi|)^{-m}$ for each $m$, uniformly in large $n$. A sequence of nonnegative kernels of mass at most $1$ with support in a fixed interval and with these two properties converges weakly to a smooth function: there is a smooth $g$ with support in $[0, \varepsilon/2]$ and $\int \phi K_n \to \int \phi g$ for every continuous $\phi$.

Now write $\int T_{n+1}F \cdot K_n = \sum_p (-1)^p c_{n+1}(p) \int F^{(p)} K_n$. The $p$-th term converges to $c_p \int F^{(p)} g$. It is bounded by $w(p)|M_p|$, since $|F^{(p)}| \leq M_p$ on the support of $K_n$ and $K_n$ has mass at most $1$. The bounds are summable, so by dominated convergence the sum converges to $\sum_p c_p \int F^{(p)} g$. The stage identity has the constant left side $F(0)$, and its right side converges to the right side of the theorem. $\square$

**Remark 4.6.5.** In the theorem of Dixmier and Malliavin, a smooth function $F$ on a Lie group (or a smooth vector of a representation) is written as a finite sum of convolutions $\sum_i f_i * F_i$ with $f_i$ smooth of compact support. The one-variable lemma is the main analytic step: the series $\sum_p c_p \frac{d^p}{dt^p}$ is applied to $F$ and the kernel $g$ is moved to the other side. Here the bounds $M_p$ are given first and the kernels are chosen for them.

**Remark 4.6.6 (Formalization).** The statement allows any real sequence $M_p$. If some $M_p$ is negative, no $F$ satisfies the bounds and the identity is vacuous. The supports of the kernels are in $[0, \varepsilon/2]$, which is stronger than the stated $[-\varepsilon, \varepsilon]$. The bounds on $F$ are only used on $[0, \varepsilon/2]$.
