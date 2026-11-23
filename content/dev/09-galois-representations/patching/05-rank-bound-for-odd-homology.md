---
title: A rank bound for odd-degree homology
decls:
  - PositivityTheory.KB.bStarOdd
  - PositivityTheory.KB.bOdd_zk
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A rank bound for odd-degree homology

Let $L$ be a totally complex number field with $r_2$ complex places. This section proves that a certain subgroup of $H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L); \mathbb{Z})$, for $k$ even, has rank at most $r_2$. The subgroup is cut out by an operator built from block sums, which kills every part of the homology of weight $2$ to $k + 1$. What remains has weight $1$, and the classes of weight $1$ are detected by $r_2$ functionals, one for each complex place. The result is the [rank input](/entry/b-odd/) of [Lemma K](/entry/lemma-k-lit-n-alt/), which the [window bound](/proof/vwin/) uses in step 5. The proof combines the [stability theorem](/entry/k-stability-main/), the [Hecke vanishing theorem](/entry/s-hecke/) and the analytic estimates of the [previous section](/entry/s-gap-of/).

### Block sums and weights

For $d \ge 1$ and a commutative ring $R$, let $\psi_d \colon \mathrm{GL}_n(R) \to \mathrm{GL}_{dn}(R)$ send $A$ to $1_d \otimes A$, the block diagonal matrix with $d$ copies of $A$. Let $\iota_{n,n'}$ be the [stabilization map](/entry/k-stability-main/). On homology, $\psi_d$ behaves like multiplication by $d$ on primitive classes. Precisely, if a real cycle $z$ of $\mathrm{GL}_n(R)$ is primitive, then $(\psi_{d})_* z - d\, (\iota_{n,dn})_* z$ is a boundary. This follows from the fact that the $d$ diagonal blocks commute and are conjugate to the upper left block.

**Definition 7.5.1 (Weight system).** Let $j \ge 0$. A *weight system of weight $j$* in degree $k + 1$ for $R$ is a family $a = (a_n)_{n \ge 0}$ of real linear maps from real $(k+1)$-chains of $\mathrm{GL}_n(R)$ to $\mathbb{R}$ such that:

1. $a_n(z) = 0$ for each boundary $z$;
2. $a_{n'}\big((\iota_{n,n'})_* z\big) = a_n(z)$ for each cycle $z$ and $n \le n'$;
3. $a_{dn}\big((\psi_d)_* z\big) = d^j a_n(z)$ for each cycle $z$ and $d \ge 1$.

A weight system is a stable homology functional on which the block sum $\psi_d$ acts by the scalar $d^j$. On a product of $j$ primitive classes, $\psi_d$ acts by $d^j$; so weights separate the primitive part (weight $1$) from products.

**Definition 7.5.2 (The weight filter).** Let $\ell \ge 1$ and $n \ge 0$. Put $n_0 = n$ and $n_{t+1} = \ell\, n_t$, so $n_t = \ell^t n$. For $x \in H_m(\mathrm{GL}_n(R); \mathbb{Z})$ define $z_t(x) \in H_m(\mathrm{GL}_{n_t}(R); \mathbb{Z})$ by $z_0(x) = x$ and
$$z_{t+1}(x) = (\psi_\ell)_*\, z_t(x) - \ell^{t+2}\, (\iota_{n_t, n_{t+1}})_*\, z_t(x).$$

The step from $t$ to $t + 1$ multiplies a weight system of weight $j$ by $\ell^j - \ell^{t+2}$: by properties 2 and 3, $a(z_{t+1}) = (\ell^j - \ell^{t+2})\, a(z_t)$. So $a(z_k(x)) = \prod_{t=0}^{k-1} (\ell^j - \ell^{t+2})\, a(x)$, and this is $0$ for $2 \le j \le k + 1$. A weight system of weight $1$ is multiplied by the nonzero numbers $\ell - \ell^{t+2}$ when $\ell \ge 2$.

### Two inputs

**Theorem 7.5.3 (Cocycles are represented by invariant forms).** Let $L$ be totally complex and $k + 1 < r_2(L)$. For each $n_0$ there is $N \ge n_0$ with the following property. For each real cocycle $c$ of degree $k + 1$ of $\Gamma_N = \mathrm{GL}_N(\mathcal{O}_L)$, invariant under $\Gamma_N$, there is a $(k+1)$-form $\omega$ on $\mathcal{H}$, invariant under all of $G_\infty$, with
$$\mathrm{ev}(c, 1, z) = \mathrm{ev}(I_\omega, 1, z) \quad \text{for every cycle } z.$$

Lean: `PositivityTheory.KB.sSurj_of`.

The notation $\mathcal{H}$, $G_\infty$, $I_\omega$ and $\mathrm{fr}_\omega$ is that of the [previous section](/entry/s-gap-of/).

*Proof.* Fix a prime $\pi$ of $\mathcal{O}_L$ with $N(\pi) \ge 25$; such a prime exists, since the prime ideals that split completely in the Hilbert class field of $L$ are principal, and there are infinitely many of them by the Chebotarev density theorem. Let $a$ be the exponent of the [partition of unity theorem](/entry/s-pu/), $N_0$ the bound of the [Hecke vanishing theorem](/entry/s-hecke/), and $N_1$ the bound of the [moment theorem](/entry/s-mom/) for $A = 2a(k + 1)$. Take $N = \max(N_0, N_1, n_0, 3)$, and a fundamental domain datum $(\mu, D)$ with $\int_D \mathrm{ht}^{2a(k+1)} \, d\mu < \infty$.

1. A form for $c$. Spreading $c$ over the partition of unity gives a good form $\omega'$, invariant under $\Gamma_N$ and under scalars, with $\mathrm{ev}(I_{\omega'}, 1, z) = \mathrm{ev}(c, 1, z)$ on cycles and $\|\mathrm{fr}_{\omega'}\| \le K\, \mathrm{ht}^{a(k+1)}$ for some $K$. So $\|\mathrm{fr}_{\omega'}\|^2$ is integrable on $D$.
2. The mean. There is a $G_\infty$-invariant form $\bar\omega$ whose frame is the constant $\mu(D)^{-1} \int_D \mathrm{fr}_{\omega'} \, d\mu$. Invariant forms are good, and $\omega' - \bar\omega$ has frame of mean zero.
3. Decay. Let $F$ be the cocycle $y \mapsto I_{\omega' - \bar\omega}(y \cdot 1)$ on $\mathrm{GL}_N(L)$. The Hecke operator acts on $F$ through the frame. By the [spectral gap](/entry/s-gap-of/), applied to the coordinates of the frame, $\| \mathrm{fr} \|_{L^2(D)}$ decreases by the factor $3/5$ at each application of $T$. By [localization](/entry/s-loc/), $|\mathrm{ev}(T^r F, 1, z)| \le C (3/5)^r$ for each cycle $z$.
4. Vanishing. The [Hecke vanishing theorem](/entry/s-hecke/) gives $\mathrm{ev}(F, 1, z) = 0$ on cycles.

So $c$ and $I_{\bar\omega}$ have the same evaluations on cycles, and $\omega = \bar\omega$ works. $\square$

**Proposition 7.5.4 (Weight decomposition for $k$ even).** Let $L$ be a number field and $k$ even. There are weight systems $\tau_w$ of weight $1$ in degree $k + 1$ for $\mathcal{O}_L$, one for each infinite place $w$ of $L$, with the following property. For each $N$ and each $G_\infty$-invariant $(k+1)$-form $\omega$, there are real numbers $c_w$ and weight systems $a_j$ of weight $j$, $2 \le j \le k + 1$, with
$$\mathrm{ev}(I_\omega, 1, z) = \sum_{w} c_w\, \tau_{w,N}(z) + \sum_{j=2}^{k+1} a_{j,N}(z)$$
for every cycle $z$ of $\Gamma_N$.

Lean: `PositivityTheory.KB.sWtOdd_of`.

We do not reproduce the proof. It uses Stokes's theorem for the simplex integrals, the block sum rule above, and the decomposition of $G_\infty$-invariant forms place by place.

### The rank bound

**Theorem 7.5.5 (Rank bound).** Let $L$ be a totally complex number field, $k$ an even integer with $k + 1 < r_2(L)$, $\ell \ge 1$, and $n \ge 2(k+1) + 4$. Then the subgroup of $H_{k+1}(\mathrm{GL}_{\ell^k n}(\mathcal{O}_L); \mathbb{Z})$ generated by the classes $z_k(x)$, $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L); \mathbb{Z})$, has rank at most $r_2(L)$.

Lean: `PositivityTheory.KB.bStarOdd` (also `PositivityTheory.KB.bOdd_zk`, the same statement for a second copy of the definitions of $n_t$, $z_t$ and $\psi_d$).

*Proof.* Put $M = \ell^k n \ge n \ge 2(k + 1) + 4$. Let $C$ be the real span of the cycles $z_k(z_0)$, where $z_0$ runs over real cycles of $\mathrm{GL}_n(\mathcal{O}_L)$ and $z_k$ is defined on chains by the same recursion. Let $\theta$ be the isomorphism of part 4 of the [bar complex proposition](/entry/s-aff/), from cycles modulo boundaries to $\mathbb{R} \otimes H_{k+1}$. Let $\tau \colon C \to \mathbb{R}^{r_2}$ be the map $z \mapsto (\tau_{w,M}(z))_w$, with the weight systems of the weight decomposition. There are $r_2$ infinite places, since $L$ is totally complex.

We claim that $\tau(z) = 0$ implies $\theta(z) = 0$ for $z \in C$. Suppose $\tau(z) = 0$ and $z$ is not a boundary. Take $N \ge M$ from the representation theorem with $n_0 = M$. By the [stability theorem](/entry/k-stability-main/) for the Dedekind ring $\mathcal{O}_L$, which applies since $M \ge 2(k+1) + 4$, the cycle $\iota_{M,N\,*} z$ is not a boundary. Part 3 of the bar complex proposition gives an invariant cocycle $c$ of $\Gamma_N$ with $\mathrm{ev}(c, 1, \iota_* z) \neq 0$. The representation theorem gives a $G_\infty$-invariant form $\omega$ with the same evaluations. The weight decomposition writes $\mathrm{ev}(I_\omega, 1, \iota_* z)$ as $\sum_w c_w \tau_{w,N}(\iota_* z) + \sum_j a_{j,N}(\iota_* z)$. By property 2 of weight systems, $\tau_{w,N}(\iota_* z) = \tau_{w,M}(z) = 0$ and $a_{j,N}(\iota_* z) = a_{j,M}(z)$. Since $z$ is a combination of the $z_k(z_0)$ and $2 \le j \le k + 1$, the computation after the weight filter gives $a_{j,M}(z) = 0$. So the evaluation is $0$, a contradiction.

The claim says that $\theta(C)$ is a quotient of $\tau(C) \subset \mathbb{R}^{r_2}$, so $\dim_{\mathbb{R}} \theta(C) \le r_2$. The image of the subgroup of the theorem in $\mathbb{R} \otimes H_{k+1}$ lies in $\theta(C)$, by naturality of $\theta$. For a subgroup $A \subseteq H_{k+1}$, the map $\mathbb{R} \otimes A \to \mathbb{R} \otimes H_{k+1}$ is injective, since $\mathbb{R}$ is flat over $\mathbb{Z}$, and the rank of $A$ is $\dim_{\mathbb{R}} (\mathbb{R} \otimes A)$. So the rank is at most $r_2$. $\square$

**Remark 7.5.6.** For $\ell = 1$ the recursion gives $z_{t+1} = (1 - 1)\, z_t = 0$, and the bound is trivial. For $\ell \ge 2$ the filter keeps the weight $1$ part, which is the primitive part of the stable homology. By Borel's theorem, for $L$ totally complex and $m \ge 2$, the group $K_{2m-1}(\mathcal{O}_L)$ has rank $r_2$, and $K_{2m-1}(\mathcal{O}_L) \otimes \mathbb{Q}$ is the primitive part of $H_{2m-1}(\mathrm{GL}(\mathcal{O}_L); \mathbb{Q})$. The theorem gives the upper bound of this form, without the computation of the regulator.

**Remark 7.5.7 (Formalization).** The theorem is assembled in [FinalOdd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/FinalOdd.lean#L8) from the bar complex facts, stability, the representation theorem and the weight decomposition. The second name `bOdd_zk` ([Bridge.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/TorsionIntegers/Bridge.lean#L34)) exists only because the definitions of $n_t$, $z_t$ and $\psi_d$ are duplicated in the namespaces `UpperTheory.V.ZK` and `PositivityTheory.KB`; it proves that the two copies agree and transports the bound. The representation theorem is proved in `JoinReconstruction.key`; its steps 1 and 2 use the statements `SWhit`, `SCen`, `SMean` and `SInv`, which we have read but not unfolded. We have not unfolded the proof of the weight decomposition. The theorem allows $\ell = 1$, where it is trivial.
