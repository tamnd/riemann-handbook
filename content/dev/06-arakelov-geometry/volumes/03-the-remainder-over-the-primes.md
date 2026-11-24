---
title: The remainder over the primes
decls:
  - GlobalTheory.CompanionTheory.Ar.Top.TestRest.finite_bound
  - GlobalTheory.CompanionTheory.Ar.Top.testRest_bound
  - GlobalTheory.T.test_polynomial_remainder_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The remainder over the primes

The power sum formula (Proposition 6 of the [previous section](/entry/full-intersection-tower-i8-identity/)) moves the top intersection numbers of a tower from one level to another. When the level goes to infinity, a sum over all large primes is left: the remainder. This section proves that the remainder of one special polynomial, the test polynomial, is bounded by $1.6\,(D+1)\delta$, where $D$ is the dimension of the fibres of the Hodge map and $\delta$ is a fibre degree. The bound does not depend on the primes, on the Frobenius labels or on the decomposition of the test polynomial into power sums. It is used in the [next section](/entry/test-height-bound-slope-flat/) to bound the shift constant at the base level from below.

Throughout, $\Psi$ is a finite set, $1 \le j < N$, and $R = \mathbb{R}[x_{\tau, i}]$ with $\deg_{\mathrm{Fl}}$ as in [the first section](/entry/t-flag-degree-polynomial-eval/). The index $j$ cuts each block $\{x_{\tau, 0}, \dots, x_{\tau, N-1}\}$ into a left part $i < j$ of size $j$ and a right part $i \ge j$ of size $N - j$.

**Definition 9.3.1 (Test polynomial).** Put $D = |\Psi|\, j\, (N - j)$. The small class is

$$
\mu = \begin{cases} \displaystyle\sum_\tau \sum_{i \ge j} x_{\tau, i} & \text{if } N - j \le j, \\ \displaystyle -\sum_\tau \sum_{i < j} x_{\tau, i} & \text{otherwise.} \end{cases}
$$

The fibre class is

$$
\mathrm{fib} = \prod_\tau \prod_{\substack{a < b \\ a < j \iff b < j}} (x_{\tau, b} - x_{\tau, a}),
$$

the product over the pairs $a < b$ on the same side of $j$. The test polynomial is $F_T = \mu^{D+1}\,\mathrm{fib}$ and the test degree is $\delta = \deg_{\mathrm{Fl}}(\mu^D\,\mathrm{fib})$.

The flag variety $\mathrm{Fl}(\mathbb{C}^N)$ maps to the Grassmannian of $j$-planes, with fibre a product of two smaller flag varieties. The Grassmannian has dimension $j(N-j)$, so $D$ is the dimension of the product of the Grassmannians. The class $\mathrm{fib}$ is, up to sign, the product of the two Vandermonde products of the fibre, and $\mu$ is a sum of Chern roots of the smaller of the two parts. We read $\delta$ as a degree on the base; this reading is a guide only. The degree of $\mathrm{fib}$ is $|\Psi|(j(j-1)/2 + (N-j)(N-j-1)/2)$. Adding $D$ gives $|\Psi| N(N-1)/2 = d$, so $\mu^D \mathrm{fib}$ has the top degree $d$ and $F_T$ has degree $d + 1$. We also use the computation that $F_T$ is homogeneous of degree $d + 1$ and that $\delta > 0$; it is part of the computation of the shift numbers of $F_T$, which we do not reproduce.

**Definition 9.3.2 (Power sum decomposition).** A power sum decomposition of $F \in R$ is a family $Q_{\tau, k}$, for $\tau \in \Psi$ and $1 \le k \le N$, of homogeneous polynomials of degree $d + 1 - k$ with

$$
F = \sum_\tau \sum_{k=1}^{N} p_k^\tau\, Q_{\tau, k}.
$$

Since $\deg_{\mathrm{Fl}}$ kills every multiple of a power sum $p_k^\tau$ with $k \ge 1$ (a symmetric function of positive degree in the Chern roots of a trivial bundle vanishes), every polynomial of degree $d + 1$ lies in the ideal of the power sums, since the coinvariant algebra of the Weyl group vanishes above degree $d$. We work with the test polynomial and with any of its decompositions.

**Definition 9.3.3 (Remainder terms).** Let $\mathrm{frob}$ give for each prime $p$, each $\tau$ and each $n \ge 0$ a label $\mathrm{frob}_p(\tau, n) \in \Psi \sqcup \Psi$, and let $p^{\mathrm{Lie}}_{k}$ be as in [the tower conditions](/entry/full-intersection-tower-i8-identity/). For a prime $p$, $k \ge 2$ and $Q \in R$ put

$$
r_p(\tau, k, Q) = k \log p \sum_{n \ge 0} p^{-k(n+1)} \deg_{\mathrm{Fl}}\big(p^{\mathrm{Lie}}_{k-1}(\mathrm{frob}_p(\tau, n))\, Q\big),
$$

and $r_p(\tau, 1, Q) = 0$. For a finite set $\mathcal{B}$ of bad primes and $B_0 \ge 0$ the remainder is

$$
\mathrm{Rest}_{B_0}(\tau, k, Q) = \sum_{\substack{p > B_0 \text{ prime} \\ p \notin \mathcal{B}}} r_p(\tau, k, Q).
$$

The term $r_p$ is the part of $\delta_p$ of Proposition 6 that does not involve $1/(p - 1)$. It comes from the Frobenius at $p$ acting on the Lie algebra of the universal abelian scheme: the label $\mathrm{frob}_p(\tau, n)$ records on which side of the Hodge filtration the image of $\tau$ under the $(n+1)$-st power of Frobenius lies. The sum over $n$ converges since $|r_p| \le c \log p / p^2$, and so the sum over $p$ converges too. We use this fact in the form: the sum over the good primes in $(B_0, B]$ tends to $\mathrm{Rest}_{B_0}$ as $B \to \infty$.

The main input is the bound for the rest terms of the [chapter on heights](/entry/rest-bound-full/). There the rest polynomial $F_c = \mu^{fra+1}\Delta_c$ of a small block $c$ is defined on blocks of $r + a$ roots, and the sum over the primes of its rest terms is at most $1.6(fra + 1)|D_c|$, for $B_0 \ge 4fN^2$, for all choices of blocks $s$ and all choices of signs $e$. We first prove the bound for a finite set of primes.

**Theorem 9.3.4 (Remainder over a finite set of primes).** Let $\Psi$ be nonempty, $j, k \ge 1$ and $N = j + k$. Let $B_0 \ge 4|\Psi| N^2$, let $\mathrm{frob}$ be a label map and let $Q$ be a power sum decomposition of $F_T$. Then for every finite set $P$ of primes $p > B_0$

$$
\Big|\sum_{p \in P} \sum_\tau \sum_{m=1}^{N} r_p(\tau, m, Q_{\tau, m})\Big| \le 1.6\,(D + 1)\,\delta.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Top.TestRest.finite_bound`

*Proof.* We translate the problem into the setting of the rest terms. Put $f = |\Psi|$, choose a bijection $e \colon \Psi \to \{0, \dots, f-1\}$ and rename the variables by $x_{\tau, i} \mapsto X_{e(\tau), i}$. Let $I = \deg_{\mathrm{Fl}} \circ e^{-1}$. Then $I$ is a flag integral in the sense of the chapter on heights: it vanishes on multiples of power sums of positive degree, and it is $\pm 1$ on the staircase monomial $\prod X_{\tau, i}^{N-1-i}$.

The small block is chosen by $j$: it is the last block if $k \le j$, and the first block otherwise. With $r$ the size of the small block and $a$ the size of the other, $fra = D$. Under the renaming, $\mu$ goes to the small class of the chapter on heights, and $\mathrm{fib}$ goes to $\pm\Delta_c$, since on each side of $j$ the product $\prod_{a<b}(x_b - x_a)$ is a Vandermonde determinant, equal to $\pm$ the other Vandermonde product, and a change of all signs in a Vandermonde product changes it by a sign. So there is $\varepsilon \in \{1, -1\}$ with $F_T \mapsto \varepsilon F_c$ and $\mu^D \mathrm{fib} \mapsto \varepsilon\, \mu^D \Delta_c$, and $\varepsilon\, e(Q)$ is a power sum decomposition of $F_c$.

A label $\mathrm{frob}_p(\tau, n)$ is a left or right copy of some $\tau'$. It goes to the block $e(\tau')$ with the sign that records the side. The Lie power sum $p^{\mathrm{Lie}}_{m-1}$ then goes to $\pm$ the small power sum $q_{m-1}$ of that block. With these choices of blocks and signs, the prime term $M(p)$ of the chapter on heights, at volume $1$, equals $\varepsilon \sum_\tau \sum_m r_p(\tau, m, Q_{\tau, m})$. The terms with $m = 1$ are $0$ on both sides.

The [theorem on rest terms over the primes](/entry/rest-bound-full/), applied to the set $P$, gives $|\sum_{p \in P} M(p)| \le 1.6\,(D+1)\,|I(\varepsilon \mu^D \Delta_c)| = 1.6\,(D+1)\,|\delta|$. Since $\delta > 0$ and $|\varepsilon| = 1$, this is the claim. $\square$

**Theorem 9.3.5 (Remainder of the test polynomial).** Let $1 \le j < N$, let $\mathcal{B}$ be a finite set, let $\mathrm{frob}$ be a label map, and let $B_0 \ge 4|\Psi| N^2$. Let $Q$ be a power sum decomposition of $F_T$. Then

$$
\Big|\sum_\tau \sum_{k=1}^{N} \mathrm{Rest}_{B_0}(\tau, k, Q_{\tau, k})\Big| \le 1.6\,(D + 1)\,\delta.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Top.testRest_bound` (also `GlobalTheory.T.test_polynomial_remainder_bound`, a second name)

*Proof.* Write $N = j + k$ with $k \ge 1$. If $\Psi$ is empty, the left side is $0$ and the right side is $1.6\,\delta \ge 0$. Let $\Psi$ be nonempty. For each $\tau$ and $m$, the sum of $r_p(\tau, m, Q_{\tau, m})$ over the primes $p \in (B_0, B]$ outside $\mathcal{B}$ tends to $\mathrm{Rest}_{B_0}(\tau, m, Q_{\tau, m})$ as $B \to \infty$. So the left side is the limit of the absolute values of the finite sums

$$
\sum_\tau \sum_{m=1}^{N} \sum_{p \in P_B} r_p(\tau, m, Q_{\tau, m}),
$$

with $P_B$ the set of primes in $(B_0, B]$ outside $\mathcal{B}$. After a change of the order of summation, each of these is bounded by $1.6(D+1)\delta$, by the [remainder over a finite set of primes](/entry/finite-bound/) applied to $P_B$. The bound passes to the limit. $\square$

The bad primes play no role: the bound holds for every set of primes larger than $B_0$. The condition $B_0 \ge 4|\Psi|N^2$ comes from the chapter on heights.

**Remark 9.3.6 (Formalization).** The finite bound is stated with $N$ written as $j + k$, so the second theorem rewrites $N$ first. The infinite sum is an unconditional sum over all natural numbers with the value $0$ off the good primes; such a sum is $0$ when it does not converge, which is why the proof goes through the limit of finite sums, given by a separate convergence statement. The second theorem has no hypothesis that $\Psi$ is nonempty, and its proof treats the empty case apart. The finite bound uses the [Vandermonde sign lemma](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestPolynomialRemainderBound.lean#L53) for the fibre class. We have not unfolded the proof of the bound in the chapter on heights.
