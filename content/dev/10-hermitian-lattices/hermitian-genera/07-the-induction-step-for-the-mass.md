---
title: The induction step for the mass
decls:
  - Formalism.HermitianLattices.Ext.L3.tendsto_singS_sum
  - Formalism.HermitianLattices.Ext.L3.Step.tendsto_right
  - Formalism.HermitianLattices.Ext.L3.massConst_succ
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The induction step for the mass

This section proves the induction step of the mass formula for Hermitian lattices over an unramified CM field. If the mass of every integral lattice of rank $m - 1$ is a fixed constant times the product of its local factors, then the same holds in rank $m$, with a new constant that we compute. The method is that of Siegel. One counts the vectors of bounded length in all classes of a genus in two ways. Geometry of numbers gives the count in terms of the mass. Splitting off each vector and using the induction hypothesis gives it in terms of the singular series, and the [local identity](/entry/li-stat/) of the last section computes each local factor. Comparing the two leading terms gives the constant. The result serves the step [theta local matching](/step/theta-local-matching/) of the proof. We keep the notation of the last two sections.

### Masses and the singular series

Let $d$ be the number of infinite places of $K$, so $d = [K^+ : \mathbb{Q}]$, and let $\delta_K = |\operatorname{disc} K|^{1/(2d)}/2$. Let $L$ be a lattice in $(V, h)$. The *genus* of $L$ is the set of lattices $M$ such that, for each maximal ideal $P$ of $\mathcal{O}_K$, there is an isometry $g$ of $(V, h)$ with $g L_P = M_P$. A *set of class representatives* is a finite subset $s$ of the genus such that each lattice of the genus is isometric to exactly one member of $s$.

**Definition 6.7.1 (Mass and representation mass).** Let $s$ be a set of class representatives for the genus of $L$. The *mass* of $L$ and the *representation mass* of $t \in K$ are
$$\mathrm{mass}(L) = \sum_{M \in s} \frac{1}{|\mathrm{Aut}(M)|}, \qquad r(L, t) = \sum_{M \in s} \frac{|\{x \in M : h(x, x) = t\}|}{|\mathrm{Aut}(M)|}.$$
Both are $0$ if no such $s$ exists.

For totally positive definite $h$ the groups $\mathrm{Aut}(M)$ are finite and a set of class representatives exists, by the finiteness of class numbers ([Platonov and Rapinchuk, Chapter 8](/learn/groups/#hermitian-lattices-and-the-mass-formula)).

**Definition 6.7.2 (Global factors).** Let $L$ be an integral lattice and $n \in \mathcal{O}_{K^+}$. Let
$$\lambda(L) = \prod_{\mathfrak{p}} \lambda_{\mathfrak{p}}(h, L), \qquad \mathfrak{S}(L, n) = \prod_{\mathfrak{p}} \frac{\alpha_{\mathfrak{p}}(L, n)}{1 - \eta(\mathfrak{p})^m q^{-m}}, \qquad D(L) = N(\mathfrak{d}(L))^{1/2},$$
where the products run over the maximal ideals $\mathfrak{p}$ of $\mathcal{O}_{K^+}$ and $q = N\mathfrak{p}$. Let $L(m, \eta) = \prod_{\mathfrak{p}} (1 - \eta(\mathfrak{p})^m q^{-m})^{-1}$. For $T > 0$ let $B(T)$ be the set of $n \in \mathcal{O}_{K^+}$ with $0 < \operatorname{Re}\varphi(n) \leq T$ for every embedding $\varphi \colon K \to \mathbb{C}$.

The series $\mathfrak{S}(L, n)$ is the *singular series* of $n$. Its factor at $\mathfrak{p}$ is the local density of $n$, normalized by the factor that a unimodular lattice of rank $m$ would give. The function $L(m, \eta)$ is the $L$-function of the quadratic character $\eta$ of $K/K^+$ at $s = m$, which converges for $m \geq 2$.

**Definition 6.7.3 (Mass constant).** A real number $c$ is a *mass constant* for $K$ in rank $m$ if $\mathrm{mass}(L) = c\, \lambda(L)$ for each totally positive definite Hermitian space $(V, h)$ over $K$ of dimension $m$ and each integral lattice $L \subseteq V$.

### The singular series on average

**Theorem 6.7.4 (Average of the singular series).** Let $K$ be an unramified CM field, $h$ totally positive definite of dimension $m \geq 2$ and $L$ an integral lattice. Then
$$\lim_{j \to \infty} (j^2)^{-dm} \sum_{n \in B(j^2)} N(n)^{m - 1}\, \mathfrak{S}(L, n) = \frac{m^{-d}}{\sqrt{(2\delta_K)^d}}\, L(m, \eta),$$
where $N(n)$ is the norm of the ideal $n \mathcal{O}_{K^+}$.

Lean: `Formalism.HermitianLattices.Ext.L3.tendsto_singS_sum`.

*Proof.* Let $S$ be the finite set of primes $\mathfrak{p}$ with $v_{\mathfrak{p}}(L) \neq 0$. For $\mathfrak{p} \notin S$ the local factor of $\mathfrak{S}(L, n)$ depends only on $v_{\mathfrak{p}}(n)$, so it is $\rho_{\mathfrak{p}}(v_{\mathfrak{p}}(n))$ for a sequence $\rho_{\mathfrak{p}}$, and $|\rho_{\mathfrak{p}}(i + 1) - \rho_{\mathfrak{p}}(i)| \leq 8 (i + 2)^2 / q$. Expand the product of the $\rho_{\mathfrak{p}}$ as a sum over ideals $\mathfrak{b}$ of multiplicative weights given by these differences. Here $\mathfrak{b}$ is prime to $S$. Each weight multiplies the sum of $N(n)^{m-1} \prod_{\mathfrak{p} \in S} \alpha_{\mathfrak{p}}(L, n)(1 - \eta(\mathfrak{p})^m q^{-m})^{-1}$ over the $n \in B(T)$ divisible by $\mathfrak{b}$. That sum, divided by $T^{dm}$, tends to $m^{-d} \prod_{\mathfrak{p} \in S} (1 - \eta(\mathfrak{p})^m q^{-m})^{-1} / (\sqrt{(2\delta_K)^d}\, N(\mathfrak{b}))$. For the main factor $m^{-d}/\sqrt{(2\delta_K)^d}$: the box $B(T)$ is a cube in $K^+ \otimes \mathbb{R} = \mathbb{R}^d$, the integral of $\prod_i x_i^{m-1}$ over $(0, T]^d$ is $(T^m/m)^d$, and $\mathfrak{b}$ has covolume $N(\mathfrak{b}) |\operatorname{disc} K^+|^{1/2}$, which is $N(\mathfrak{b}) \sqrt{(2\delta_K)^d}$ because $K/K^+$ is unramified at all finite primes. The bound $|B(T) \cap \mathfrak{b}| \leq 2^d T^d / N(\mathfrak{b})$ and the bound on the differences give a summable majorant. So a dominated convergence theorem for multiplicative weights moves the limit inside the sum. The limit is an Euler product, which equals $L(m, \eta)$ after the factors at $S$ are put back. $\square$

### The two counts

**Proposition 6.7.5 (Representation side).** Assume, for every unramified CM field $K$, that for all totally positive $a, b, n \in K^+$ there are $s, t \in K$ with $a s \bar s + b t \bar t = n$. Assume the [local identity](/entry/li-stat/). Let $K$ be an unramified CM field, $h$ totally positive definite of dimension $m \geq 2$, $L$ an integral lattice, and $c$ a mass constant for $K$ in rank $m - 1$. Then
$$\lim_{j \to \infty} \frac{\mathrm{mass}(L) + \sum_{n \in B(j^2)} r(L, n)}{j^{2dm}} = 0 + c\, \lambda(L)\, D(L)^{-1}\, \frac{m^{-d}}{\sqrt{(2\delta_K)^d}}\, L(m, \eta).$$

Lean: `Formalism.HermitianLattices.Ext.L3.Step.tendsto_right`.

*Proof.* The constant $\mathrm{mass}(L)$ divided by $j^{2dm}$ tends to $0$. For the sum, fix $n \in B(j^2)$. Since $h$ is totally positive definite and $m \geq 2$, the assumption on binary forms gives $x_0 \in V$ with $h(x_0, x_0) = n$; write $V = K x_0 \oplus x_0^{\perp}$. Each vector $x$ with $h(x, x) = n$ in a class of the genus gives a lattice in the complement of $x$, of rank $m - 1$. Grouping the vectors by the class of this lattice, and using that $c$ is a mass constant in rank $m - 1$, gives $r(L, n) = c \prod_{\mathfrak{p}} \psi_{\mathfrak{p}}(L)$. By the local identity at each $\mathfrak{p}$, and since $\alpha^{\mathrm{std}}_{\mathfrak{p}}(m) = \alpha^{\mathrm{std}}_{\mathfrak{p}}(m-1)(1 - \eta^m q^{-m})$ and $\prod_{\mathfrak{p}} q^{v_{\mathfrak{p}}(L)} = D(L)$,
$$\prod_{\mathfrak{p}} \psi_{\mathfrak{p}}(L) = N(n)^{m-1}\, \lambda(L)\, D(L)^{-1}\, \mathfrak{S}(L, n).$$
So the sum is $c\, \lambda(L) D(L)^{-1} \sum_{n \in B(j^2)} N(n)^{m-1} \mathfrak{S}(L, n)$, a finite sum. The [average of the singular series](/entry/tendsto-sing-s-sum/) gives the limit. $\square$

### The induction step

**Theorem 6.7.6 (Induction step for the mass).** Assume the hypothesis on binary forms of the proposition and the local identity. Let $K$ be an unramified CM field with real subfield $K^+$, $m \geq 2$, and $c > 0$ a mass constant for $K$ in rank $m - 1$. Then $c\, \rho(K, m)$ is a mass constant for $K$ in rank $m$, where
$$\rho(K, m) = \frac{\bigl((m - 1)!\, (\delta_K/\pi)^m\bigr)^d}{\sqrt{(2\delta_K)^d}}\, L_K(m), \qquad L_K(m) = \prod_{P} e_P(m),$$
the product over the maximal ideals $P$ of $\mathcal{O}_K$, with $e_P(m) = (1 - (-1)^m N(P)^{-m/2})^{-1}$ if $\bar P = P$ and $e_P(m) = (1 - N(P)^{-m})^{-1/2}$ if $\bar P \neq P$.

Lean: `Formalism.HermitianLattices.Ext.L3.massConst_succ`.

*Proof.* Let $(V, h)$ be totally positive definite of dimension $m$ and $L$ integral, and let $s$ be a set of class representatives. For $M$ in the genus let $b(M, T)$ be the number of $x \in M$ with $\operatorname{Re}\varphi(h(x, x)) \leq T$ for every $\varphi$. Geometry of numbers gives, for each $M$ in the genus,
$$\lim_{j \to \infty} \frac{b(M, j^2)}{j^{2dm}} = \frac{(\pi^m/m!)^d}{\delta_K^{dm}\, D(M)}:$$
at each complex place the region is a ball for a positive definite Hermitian form on $\mathbb{C}^m$, of volume $\pi^m T^m/m!$ divided by the determinant, and $\delta_K^{dm} D(M)$ is the covolume of $M$ after this normalization. Also $D(M) = D(L)$ on the genus. Summing over $M \in s$ with weights $1/|\mathrm{Aut}(M)|$, the weighted count tends, after division by $j^{2dm}$, to $\mathrm{mass}(L)\, (\pi^m/m!)^d / (\delta_K^{dm} D(L))$. On the other hand, the vector $x = 0$ contributes $\mathrm{mass}(L)$, and each $x \neq 0$ has $h(x, x) = n$ with $n \in B(T)$, since $h(x, x) \in \mathcal{O}_K$ is fixed by the involution. So the weighted count is $\mathrm{mass}(L) + \sum_{n \in B(T)} r(L, n)$. By the [representation side](/entry/tendsto-right/) and the uniqueness of limits,
$$\mathrm{mass}(L)\, \frac{(\pi^m/m!)^d}{\delta_K^{dm} D(L)} = c\, \lambda(L)\, D(L)^{-1} \frac{m^{-d}}{\sqrt{(2\delta_K)^d}}\, L(m, \eta).$$
With $m! = m\,(m-1)!$ this gives $\mathrm{mass}(L) = c\, \lambda(L)\, ((m-1)!/\pi^m)^d\, \delta_K^{dm} \sqrt{(2\delta_K)^d}^{\,-1} L(m, \eta)$. Finally $L_K(m) = L(m, \eta)$. A prime $\mathfrak{p}$ inert in $K$ gives one $P = \bar P$ with $N(P) = q^2$ and factor $(1 - (-1)^m q^{-m})^{-1}$. A split prime gives $P \neq \bar P$ with $N(P) = N(\bar P) = q$ and two factors $(1 - q^{-m})^{-1/2}$. No prime ramifies. So $\mathrm{mass}(L) = c\, \rho(K, m)\, \lambda(L)$. $\square$

**Remark 6.7.7 (Formalization).** The proposition on binary forms is the hypothesis `HermRepUnram` of [MassLandSt.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/MassLandSt.lean#L17); it is not proved here. The local identity enters [MassConstSucc.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/MassConstSucc.lean#L99) as the hypothesis `LIStat`, though the last section proves it. The hypothesis $c > 0$ (line 100) is not used. The limit of $b(M, j^2)$ is the lemma `tendsto_ballCount`, the identity for $r(L, n)$ is `repMass_eq` of FactorIdentity.lean, built from `exists_vec_of_hermRep`, `repMass_eq_prod_psi` and `tprod_localPsi_eq`; for these we read the statements and the way they are used, not all proofs. The abstract convergence theorem is `tendsto_weighted_tprod` of TendstoWeightedTprod.lean. The mass is $0$ when no class representatives exist ([StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L11)); this case does not occur. The constant $\rho(K, m)$ is written with an Euler product over the primes of $K$, with exponent $-1/2$ at split primes ([StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L30)); the proof turns it into $L(m, \eta)$ by the lemma `massRatio_eq_lvalue`. The limits of the sums over $B(T) \cap \mathfrak{b}$ are `tendsto_sum_box_ideal`, of which we read the statement; the covolume argument in the proof above explains its limit. The products $\lambda(L)$, $\mathfrak{S}(L, n)$ and $L(m, \eta)$ are `tprod`, which is $1$ when the product does not converge unconditionally.
