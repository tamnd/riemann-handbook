---
title: Frobenius windows on polydiscs
decls:
  - GlobalTheory.T.frobenius_polydisc_windows_surjective_bounds_zero
  - GlobalTheory.PMonE.winThm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frobenius windows on polydiscs

The lattice lemma of the monodromy theorem needs eigenvectors $b$ of $\varphi^h$ in $B_{\mathrm{cris}}^+$ whose images in $B_{\mathrm{dR}}$ satisfy linear conditions modulo $\mathrm{Fil}^1$. Such eigenvectors are built from series of the form $\sum_{n \in \mathbb{Z}} \ell^{-n} x^{\ell^{nh+j}}$ in a perfect field of characteristic $\ell$, and the conditions become equations in these series. This section proves the analytic result behind those equations, in a field $F$ of characteristic $p$. It says that a finite part (a *window*) of such a system of series is onto a polydisc of the right size, that its terms obey explicit bounds, and that it has a zero which is not too small. The result is used in [the construction of residue zeros](/entry/exists-orthogonal-family-residue-zeros/), where $p = \ell$ and $F$ is the tilt $C^\flat$.

Throughout, $p$ is a prime and $F$ is a field with a nontrivial absolute value $|\cdot|$ that is ultrametric. We assume that $F$ is complete, algebraically closed, of characteristic $p$ and perfect. Vectors are indexed by $\{0, \dots, h-1\}$, and $|x| \leq \rho$ for vectors means $|x_j| \leq \rho_j$ for all $j$.

**Definition 6.17.1 (Frobenius powers).** For $k \in \mathbb{Z}$ and $x \in F$, write $x^{p^k}$ for $x$ raised to the power $p^k$ if $k \geq 0$, and for the image of $x$ under the $(-k)$-th power of the inverse of Frobenius if $k < 0$. Since $F$ is perfect, $x \mapsto x^{p^k}$ is an automorphism of $F$ for every $k$, and $|x^{p^k}| = |x|^{p^k}$.

**Definition 6.17.2 (Orthogonal family).** A family $\lambda = (\lambda_0, \dots, \lambda_{h-1})$ in $F$ is *orthogonal modulo $p$* if for every $c \in \mathbb{Z}^h$ and every $j$ with $p \nmid c_j$,
$$|\lambda_j| \leq \Big| \sum_{i} c_i \lambda_i \Big|.$$

For example, if the $|\lambda_i|$ are distinct, then $\lambda$ is orthogonal modulo $p$. An integer prime to $p$ has absolute value $1$ in $F$ and a multiple of $p$ is $0$, so the absolute value of the sum is the largest $|\lambda_i|$ with $p \nmid c_i$.

**Definition 6.17.3 (Window rows).** Let $\varpi \in F$, let $\lambda \in F^h$ and $x \in F^h$. For $r, j \in \{0, \dots, h-1\}$ and $n \in \mathbb{Z}$, the *term* is
$$T_{r,j,n}(x) = \lambda_j\, \varpi^{-n}\, x_j^{p^{r + nh}}.$$
For integers $L, U \geq 0$, the *window row* with bounds $L$ and $U$ is
$$S_{L,U}(x)_r = \sum_{j=0}^{h-1} \sum_{n=-L}^{U} T_{r,j,n}(x).$$
For $K \geq 0$ write $R_K = S_{K,K}$, the symmetric window.

If $\varpi$ is a uniformizer of absolute value $1/p$, then $R_K(x)_r$ is a truncation of $\sum_j \lambda_j \sum_{n \in \mathbb{Z}} \varpi^{-n} x_j^{p^{r+nh}}$, which is the shape of the series in the opening paragraph.

**Definition 6.17.4 (Additive system).** Let $m$ be a finite index set. A vector $x \in F^m$ is *integral* if $|x_i| \leq 1$ for all $i$. Let $q$ be a power of $p$, let $D \geq 0$, and let $M_0, M_1, \dots$ be $m \times m$ matrices over $F$. The *additive system* is the map
$$G_{q,D,M}(x) = \sum_{n=0}^{D} M_n\, x^{q^n}, \qquad x \in F^m,$$
where $x^{q^n}$ is taken entry by entry. For $N \geq 0$, the sequence $M$ is *normal of order $N$* if every entry of every $M_n$ has absolute value at most $1$, $M_N$ is the identity matrix, and every entry of $M_n$ has absolute value less than $1$ for $n > N$.

Since $x \mapsto x^{q^n}$ is additive in characteristic $p$, the map $G_{q,D,M}$ is additive. Its zeros form a group.

We use the following facts, proved elsewhere in this development.

1. (The general lemma.) Let $F$ be a field with a nontrivial ultrametric absolute value, complete, algebraically closed and of characteristic $p$. Let $q = p^e$ with $e > 0$, let $N \leq D$, and let $M$ be normal of order $N$. Then for every integral $b \in F^m$ there is an integral $x$ with $G_{q,D,M}(x) = b$. If also $\det M_0 \neq 0$, the number of integral $x$ with $G_{q,D,M}(x) = 0$ is $q^{|m| N}$.
2. (Radii.) Let $h = k + 1$, $|\varpi| = 1/p$, $\lambda_j \neq 0$ for all $j$, $|\lambda_j|$ decreasing in $j$, and $|\lambda_i| < p\,|\lambda_j|$ for all $i, j$. Then there is $\pi \in F^h$ with $\pi_j \neq 0$ and $|\pi_j| < 1$ for all $j$, with $|\lambda_{j+1}|\,|\pi_{j+1}|^{p^j} = |\lambda_j|\,|\pi_j|^{p^j}$ for $j < k$, and with $(|\lambda_0|/p)^p\,|\pi_0| = (|\lambda_k|\,|\pi_k|^{p^k})^p$.
3. (Bounds at the radii.) Under the hypotheses and conclusion of 2, put $c_r = \lambda_r \pi_r^{p^r}$. Then $|T_{r,j,n}(\pi)| \leq |c_r|$ for all $r, j, n$; the inequality is strict for $n > 0$; and $|T_{r,j,n}(\pi)| \leq |c_r|/p$ for $|n| > 2$.
4. (Monotonicity.) If $|x| \leq |\pi|$, then $|T_{r,j,n}(x)| \leq |T_{r,j,n}(\pi)|$ for all $r, j, n$.
5. (Determinants.) For $L, U \geq 0$ and $\pi$ with nonzero entries, let $C_0, C_1, \dots$ be the matrices with entries
$$(C_m)_{r,j} = \Big( \frac{T_{r,j,m-L}(\pi)}{c_r} \Big)^{p^{h-r}} \ \text{ for } m \leq L + U, \qquad C_m = 0 \ \text{ for } m > L + U.$$
If $\varpi \neq 0$, all $\lambda_j \neq 0$, $|\lambda_j|$ is decreasing, and $\lambda$ is orthogonal modulo $p$, then $|\det C_L| = 1$ and $\det C_0 \neq 0$.
6. (Normalization.) If the entries of all $C_n$ have absolute value at most $1$, those of $C_n$ for $n > L$ less than $1$, and $|\det C_L| = 1$, then $(C_L^{-1} C_n)_n$ is normal of order $L$ and the entries of $C_L^{-1}$ have absolute value at most $1$.
7. (Window identity.) Let $q = p^h$, $L \geq 1$, and put $w(z)_j = \pi_j z_j^{q^{L-1}}$ for $z \in F^h$. Then
$$\Big( \frac{S_{L,U}(w(z))_r}{c_r} \Big)^{p^{h-r}} = G_{q, L+U, C}(z)_r.$$
8. (Counting zeros.) Let $L \geq 1$ and let $M$ be a sequence of matrices with $G_{q,L+U,M}(z) = 0$ if and only if $S_{L,U}(w(z)) = 0$. Then the number of $x$ with $|x| \leq |\pi|$ and $S_{L,U}(x) = 0$ equals the number of integral $z$ with $G_{q,L+U,M}(z) = 0$.
9. (Inner disc.) For $K \geq 1$ and $\varpi \neq 0$, the number of $x$ with $|x_j| \leq |\pi_j|^{p^h}$ for all $j$ and $R_K(x) = 0$ equals the number of $x$ with $|x| \leq |\pi|$ and $S_{K-1,K+1}(x) = 0$.

Fact 7 is a direct computation: $T_{r,j,n}(w(z)) = T_{r,j,n}(\pi)\, z_j^{p^{r+nh} q^{L-1}}$, and the power $p^{h-r}$ is additive and turns the exponent into $q^{n+L}$. Fact 9 comes from the shift $n \mapsto n + 1$ in the window, which moves $x_j$ to $x_j^{p^h}$.

**Theorem 6.17.5 (Frobenius windows).** Let $F$ be as above. Let $h > 0$, let $\varpi \in F$ with $|\varpi| = 1/p$, and let $\lambda \in F^h$ with $\lambda_j \neq 0$ for all $j$. Assume that $|\lambda_j|$ is decreasing in $j$, that $\lambda$ is orthogonal modulo $p$, and that $|\lambda_i| < p\,|\lambda_j|$ for all $i, j$. Then there are real numbers $\rho_0, \dots, \rho_{h-1}$ and $\tau_0, \dots, \tau_{h-1}$ and an integer $K \geq 0$ such that:

1. $0 < \rho_j < 1$ and $\tau_r > 0$ for all $j$ and $r$;
2. for every $x$ with $|x| \leq \rho$ and all $r, j, n$, $|T_{r,j,n}(x)| \leq \tau_r$, and $|T_{r,j,n}(x)| \leq \tau_r/p$ if $|n| > K$;
3. for every $b \in F^h$ with $|b_r| \leq \tau_r$ for all $r$, there is $x$ with $|x| \leq \rho$ and $R_K(x) = b$;
4. there is $x$ with $|x| \leq \rho$, with $|x_j| > \rho_j^{p^h}$ for some $j$, and with $R_K(x) = 0$.

Lean: `GlobalTheory.T.frobenius_polydisc_windows_surjective_bounds_zero` (also `GlobalTheory.PMonE.winThm`, a second name).

Part 2 says that the terms outside the window are smaller than the size $\tau$ of the target by a factor $p$. Part 3 says that the window is onto the polydisc of radii $\tau$. Part 4 gives a zero of the window that does not lie in the inner polydisc of radii $\rho^{p^h}$. In the application, part 4 produces a nontrivial solution, and parts 2 and 3 let one correct the error made by the truncation.

*Proof.* Write $h = k + 1$. Fact 2 gives $\pi \in F^h$ with $\pi_j \neq 0$, $|\pi_j| < 1$, and the two relations between radii. Put
$$\rho_j = |\pi_j|, \qquad \tau_r = |c_r| = |\lambda_r|\,|\pi_r|^{p^r}, \qquad K = 2.$$
Then $0 < \rho_j < 1$ and $\tau_r > 0$, since $\lambda_r \neq 0$ and $\pi_r \neq 0$. Also $\varpi \neq 0$, since $|\varpi| = 1/p > 0$. This gives part 1.

Part 2. Let $|x| \leq \rho = |\pi|$. By fact 4 and fact 3, $|T_{r,j,n}(x)| \leq |T_{r,j,n}(\pi)| \leq \tau_r$, and for $|n| > 2$ also $|T_{r,j,n}(x)| \leq |T_{r,j,n}(\pi)| \leq \tau_r/p$.

Normalization. Fix $L \geq 1$ and $U \geq 0$, and let $C_m$ be the matrices of fact 5. By fact 3, every entry of $C_m$ has absolute value at most $1$, and for $m > L$, that is for $n = m - L > 0$, less than $1$. Fact 5 gives $|\det C_L| = 1$ and $\det C_0 \neq 0$. By fact 6, $M_n = C_L^{-1} C_n$ is normal of order $L$, and $C_L^{-1}$ has entries of absolute value at most $1$. Also $\det M_0 = \det(C_L)^{-1} \det C_0 \neq 0$. For $b \in F^h$ define
$$\nu(b)_r = \Big( \frac{b_r}{c_r} \Big)^{p^{h-r}}, \qquad \Phi(b) = C_L^{-1}\, \nu(b).$$
If $|b_r| \leq \tau_r$ for all $r$, then $\nu(b)$ is integral, and so is $\Phi(b)$ by the ultrametric inequality. Clearly $\Phi(0) = 0$. Since $G_{q,L+U,M}(z) = C_L^{-1} G_{q,L+U,C}(z)$, fact 7 shows that $G_{q,L+U,M}(z) = \Phi(b)$ holds if and only if $(S_{L,U}(w(z))_r / c_r)^{p^{h-r}} = (b_r/c_r)^{p^{h-r}}$ for all $r$. Since $y \mapsto y^{p^{h-r}}$ is injective and $c_r \neq 0$, this holds if and only if $S_{L,U}(w(z)) = b$.

Part 3. Let $|b_r| \leq \tau_r$ for all $r$. Normalize with $L = U = 2$, so that $S_{2,2} = R_2$. By the first half of fact 1, with $e = h$, $N = 2$ and $D = 4$, there is an integral $z$ with $G_{q,4,M}(z) = \Phi(b)$. Put $x = w(z)$. Then $|x_j| = |\pi_j|\,|z_j|^{q} \leq |\pi_j| = \rho_j$, and $R_2(x) = S_{2,2}(w(z)) = b$ by the normalization.

Part 4. Normalize twice: with $(L, U) = (2, 2)$, which gives $M$, and with $(L, U) = (1, 3)$, which gives $M'$. Both normalizations satisfy the hypothesis of fact 8, since $\Phi(0) = 0$. Let $Z_{\mathrm{out}}$ be the set of $x$ with $|x| \leq |\pi|$ and $R_2(x) = 0$, and $Z_{\mathrm{in}}$ the set of $x$ with $|x_j| \leq |\pi_j|^{p^h}$ for all $j$ and $R_2(x) = 0$. By fact 8 and the second half of fact 1, with $N = 2$,
$$|Z_{\mathrm{out}}| = q^{2h} = (p^h)^{2h}.$$
By fact 9, $|Z_{\mathrm{in}}|$ equals the number of zeros of $S_{1,3}$ in $|x| \leq |\pi|$. By fact 8 for $M'$ and fact 1 with $N = 1$, this number is $(p^h)^h$. Now suppose that part 4 fails. Then every $x \in Z_{\mathrm{out}}$ has $|x_j| \leq \rho_j^{p^h} = |\pi_j|^{p^h}$ for all $j$, so $Z_{\mathrm{out}} \subseteq Z_{\mathrm{in}}$. The set $Z_{\mathrm{in}}$ is finite, since its number of elements is not zero. So $(p^h)^{2h} \leq (p^h)^h$. This is false, since $p^h > 1$ and $2h > h$. $\square$

**Remark 6.17.6 (Formalization).** The window size is fixed at $K = 2$ ([FrobeniusPolydiscWindowsSurjectiveBoundsZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FrobeniusPolydiscWindowsSurjectiveBoundsZero.lean#L116)). The element $\varpi$ enters the proof only through $|\varpi| = 1/p$ and $\varpi \neq 0$; no relation between $\varpi$ and $p$ is assumed. Facts 3 to 9 are wrappers of lemmas in the namespace `GlobalTheory.PMonE`, and fact 1 is `GlobalTheory.T.additiveSystem_generalLemma_all_orders`, which gives the two properties for every order $N$. Fact 2 is `GlobalTheory.PMonE.exists_window_radii` ([ExistsWindowRadii.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsWindowRadii.lean#L13)); in its first relation the exponent $p^j$ is the same on both sides. The proposition `GlobalTheory.PMonE.MooreNorm` is defined in the same file as the theorem but is not used here. The counts are cardinalities in `Nat.card`, which is $0$ for an infinite set; the proof gets the finiteness of the inner zero set from the fact that its count is positive.
