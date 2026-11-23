---
title: Integral jet moments
decls:
  - GlobalTheory.MomT.jetMoments_of_unitPeriod
  - GlobalTheory.MomTop.jetMoments
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integral jet moments

This section turns the moment statement of the previous section into an integrality statement for the jet sums of the kernels. Fix a prime $T(u)$ of an admissible datum, a place $w$ above it and an embedding $\iota$ into $\mathbb{C}_{T(u)}$ that induces $w$. We show that there are weights $u_\tau$ of absolute value $1$ such that the images under $\iota$ of the jet sums are limits of integral combinations of the point tables, once at the places that see $\bar\pi$ and once, with a factor $T(u)^{-f N_i}$, at the places that see $\pi$. The result is used in the [sharp column valuations](/entry/cm-theta-values/depth-valuations/#sharp-column-valuations-at-level-primes), where it bounds the kernels of the chain at the level primes.

### The setting

Let $D$ be an admissible datum. It has fields $F \subseteq E$ and $K$, a finite set $\mathcal{T}$ of embeddings $\tau : E \to K$ with $f = |\mathcal{T}|$, ranks $N_0, \dots, N_m$, and a family of primes: for each word $u$ a rational prime $T(u)$ and an element $\pi = \pi_u \in \mathcal{O}_E$ with $\pi \bar\pi = T(u)$ and $\pi$, $\bar\pi$ coprime. All ranks $N_i$ are even. Let $V(\pi)$ be the set of primes of $E$ that divide $\pi$.

The analytic data are a tuple $(s, \mathfrak{c}, \delta, B, \chi, c_D)$: a seam $s$ between the host of the theta functions and the fields of $D$, a curve ideal $\mathfrak{c}$, a twelfth root $\delta$ of the discriminant of the ideal lattice, a base $B$ for $(\mathfrak{c}, \delta)$ as in the [section on lattice integrality](/entry/cm-theta-values/depth-valuations/#lattice-integrality-of-theta-translates), an [admissible character](/entry/cm-theta-values/depth-valuations/#normalized-theta-vectors-and-the-finiteness-of-moments) $\chi$, and numbers $c_D(\tau)$. The data are *admissible* if the seam satisfies its conditions, its reference embedding $\sigma_0 : K \to \mathbb{C}$ is the one of $D$, $\mathfrak{c}$ is a curve ideal, $\delta$ is a twelfth root, $\chi$ is admissible, and there is a number field $M \subseteq \mathbb{C}$ that contains the images of all embeddings with $c_D(\tau) \in M$ a generator of a certain ideal $\ell_\tau$ of $\mathcal{O}_M$ for each $\tau$. The data give an ambient object $A$: the normalized theta vectors $e(N, N')$ for the lattices of $D$, an ideal $\mathfrak{A}$ of $E$, a character factor $\chi_F(N, N')$ and the kernel jets.

**Definition 4.10.1.** Let $H$ and $I$ be sets, $t : H \times I \to \mathbb{C}_p$ a table, $\Sigma \subseteq H$ and $R \subseteq I$. A function $J : I \to \mathbb{C}_p$ lies in the *integral closure of $t$ over $\Sigma$ on $R$* if for every finite set $F \subseteq R$ and every $\varepsilon > 0$ there is a finitely supported function $c : H \to \mathbb{C}_p$ with support in $\Sigma$ and $\|c(x)\| \leq 1$ for all $x$, such that
$$\Big\| J(m) - \sum_{x \in H} c(x)\, t(x, m) \Big\| < \varepsilon \quad \text{for all } m \in F.$$

So $J$ lies in the closure, for pointwise convergence on $R$, of the $\mathcal{O}_{\mathbb{C}_p}$-span of the columns $t(x, \cdot)$ with $x \in \Sigma$. Each column $t(x, \cdot)$ with $x \in \Sigma$ lies in it: take $c$ equal to $1$ at $x$ and $0$ elsewhere.

**Definition 4.10.2.** A ring homomorphism $\iota : K \to \mathbb{C}_p$ *induces* the place $w$ of $K$ if for every $y \in \mathcal{O}_K$ we have $y \in w$ if and only if $\|\iota(y)\| < 1$.

The place $w$ *sees $\pi$* if $\tau(\pi) \in w$ for every $\tau \in \mathcal{T}$, and it *sees $\bar\pi$* if $\tau(\bar\pi) \in w$ for every $\tau$.

**Definition 4.10.3.** Let $u = (u_\tau)$ be weights in $\mathbb{C}_p$. For an $E$-linear map $x : E^a \to E^b$ with adjoint $x^*$, the variables are the triples $k = (\tau, j, i)$ with $\tau \in \mathcal{T}$, $j \leq b$ and $i \leq a$. For a finitely supported $m$ from variables to $\mathbb{N}$, the *point table* is
$$\mathrm{pt}(x, m) = \prod_{k = (\tau, j, i)} \big( u_\tau\, \iota(\tau(x^* e_j)_i) \big)^{m(k)}.$$

So $\mathrm{pt}(x, \cdot)$ lists the monomials in the conjugates of the entries of $x^*$, weighted by $u$.

A *decorated lattice* $d$ of rank $a$ at $V(\pi)$ has a lattice $N_d \subseteq E^a$ and, for each $P \in V(\pi)$, a local lattice $d_P$ and a map $f_P$ on $E^a$. It is *standard* at $V(\pi)$ if $d_P$ is the localization at $P$ of the standard lattice for each $P \in V(\pi)$. For decorated lattices $d$ of rank $a$ and $d'$ of rank $b$, the two *supports* are
$$\begin{aligned} \overline{\Sigma}(d, d') &= \{ x : x(y) \in d'_P \text{ and } f'_P(x y) = f_P(y) \text{ for all } P \in V(\pi),\ y \in d_P \},\\ \Sigma_p(d, d') &= \{ x : x^*(y) \in d_P \text{ for all } P \in V(\pi) \text{ and } y \in d'_P \text{ with } f'_P(y) = 0 \}. \end{aligned}$$

For a finite set $S$ of primes of $E$ and lattices $N \subseteq E^a$, $N' \subseteq E^b$, let $H_S(N, N')$ be the set of $x$ with $x(N_P) \subseteq N'_P$ for all $P \in S$. For an integer $c$, write $c^{-1}H$ for the set of $x$ with $c x \in H$.

**Definition 4.10.4.** Let $c_A, c_B$ be positive integers and $S_G$ a finite set of primes. A function $\Xi_0$ on the maps $E^a \to E^b$ with values in $K$ is an *off datum* at $w$ if for every $x \in c_A^{-1} H_{S_G}(N, N')$ we have $|\Xi_0(x)|_w \leq 1$ and $\Xi_0(x + y) = \Xi_0(x)$ for all $y \in c_B H_{S_G}(N, N')$.

For a function $\Xi$ and a finite set $S$, the *jet sum* is
$$J(m) = \sum_{x \in c_A^{-1} H / c_B H} \Xi(x)\, j_A(x, m), \qquad H = H_S(N, N'),$$
summed over one representative of each class, where $j_A(x, m)$ is the kernel jet of $A$ at $x$. The *rational indices* are the $m$ such that for every $x \in c_A^{-1}H$ with $\Xi(x) \neq 0$ the number $\chi_F(N, N')^{-1}$ times the $m$-th jet of the induced theta function at $x$ is $\sigma_0(k)$ for some $k \in K$.

### The theorem

Given row data (a selection $\mathrm{sel}$, a set $S$ of primes, a tuple $\mu$ and local constants), we write $S_G$ for their set of row primes, $c_A$ and $c_B$ for their two constants, $S_{\mathrm{all}}$ for $V(\pi) \cup S_G$, and $\varphi(d, d')$ for the indicator function of $\overline{\Sigma}(d, d')$. The row data are *admissible* if the selection is one, $S$ contains the primes of the host and all $T(u)$, and $N(\mathfrak{c})$ is prime to the residue characteristic $q_P$ of each $P \in S_G$.

**Theorem 4.10.5 (integral jet moments).** Let $D$ be an admissible datum with admissible analytic data. Let $u$ be a word with $T(u)$ prime to $N(\mathfrak{c})$, let $w$ be a place of $K$ and let $\iota : K \to \mathbb{C}_{T(u)}$ induce $w$. Then there are weights $u_\tau$ with $\|u_\tau\| = 1$ for all $\tau$ with the following property. Let the row data be admissible, let $i < m$ and $b = N_{i + 1}$, let $d$ and $d'$ be decorated self-dual lattices of ranks $N_i$ and $b$ at $V(\pi)$, both standard there, let $\Xi_0$ be an off datum at $w$ for $(c_A, c_B, S_G)$, put $\Xi = \varphi(d, d')\, \Xi_0$, and let $J$ and $R$ be the jet sum and the rational indices for $\Xi$ and $S_{\mathrm{all}}$. Then:

1. if $w$ sees $\bar\pi$, then $\iota \circ J$ lies in the integral closure of $\mathrm{pt}$ over $\overline{\Sigma}(d, d')$ on $R$;
2. if $w$ sees $\pi$, then $\iota \circ J$ lies in the integral closure of $T(u)^{-f N_i}\, \mathrm{pt}$ over $\Sigma_p(d, d')$ on $R$.

Lean: `GlobalTheory.MomTop.jetMoments`.

The weights depend on $u$, $w$ and $\iota$ but not on the row data. We prove the theorem from three inputs.

**Theorem 4.10.6 (reduction to the moment statement).** Assume the following.

1. For every datum, curve ideal $\mathfrak{c}$, twelfth root $\delta$, base $B$ and admissible character $\chi$, every prime $p \neq 2$ with $\left(\frac{-d}{p}\right) = 1$ and $N(\mathfrak{c})$ prime to $p$, and every $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$, there is $\Omega$ with $\|\Omega\| = 1$ such that the moment statement holds for $(e_\chi, \lambda, \Omega)$.
2. For the same data, the normalized vectors satisfy the equivariance laws for $\chi$.
3. The lattice facts hold: for all admissible data and all even $a, b$, the ambient object satisfies the lattice hypothesis and the smoothness condition in ranks $a, b$.

Then the integral jet moments hold.

Lean: `GlobalTheory.MomT.jetMoments_of_unitPeriod`.

*Proof.* Fix the data of the theorem and write $p = T(u)$.

Step 1 (the prime). There is $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ with $\lambda(\sigma_0(k)) = \iota(k)$ for all $k \in K$. The prime $p$ is not in the set of small primes of the host and differs from the prime $q$ of the host, so $p \neq 2$. Since $\pi \bar\pi = p$ with $\pi$ and $\bar\pi$ coprime, the prime $p$ is split for $d$. Input 1 gives $\Omega$ with $\|\Omega\| = 1$ and the moment statement for $(e_\chi, \lambda, \Omega)$.

Step 2 (the weights). Put $u_\tau = \lambda(c_D(\tau'))/\Omega$, where $\tau'$ is the embedding of the host that the seam attaches to $\tau$. Since $c_D(\tau')$ generates $\ell_{\tau'}$ and $p$ is not small and differs from $q$, $\|\lambda(c_D(\tau'))\| = 1$. So $\|u_\tau\| = 1$.

Step 3 (units). Fix row data, $i$, $d$, $d'$ and $\Xi_0$. Both $N_i$ and $b$ are even, so input 3 applies in ranks $N_i$, $b$. The ideal $\mathfrak{A}$ is a unit at every prime of $S_{\mathrm{all}}$: at the primes above $p$ because $p$ is prime to $N(\mathfrak{c})$, and at the row primes because they are bad primes of the row with $q_P$ prime to $N(\mathfrak{c})$. The product of the $q_P$ over $S_G$ is prime to $p$. For the self-dual lattices $N_d$ and $N_{d'}$, the values $\chi(\det)$ that enter $\chi_F(N_d, N_{d'})$ are algebraic, and $\lambda$ maps them to units. So $\chi_F$ is algebraic and $\|\lambda(\chi_F)\| = 1$.

Step 4 ($w$ sees $\bar\pi$). Since $\iota$ induces $w$, $\|\iota(\tau(\bar\pi))\| < 1$ for all $\tau$. The moment statement at $\bar\pi$ gives the point moments of $A$ at $\pi/\bar\pi$ for $\lambda$, $\iota$ and the weights $u$. A lemma on cosets turns these point moments into moments of the induced theta functions at each $x \in c_A^{-1}H$ in $\overline{\Sigma}(d, d')$, and adding $c_B H$ does not leave $\overline{\Sigma}(d, d')$. Since the off datum is constant on the cosets of $c_B H$ and $|\Xi_0|_w \leq 1$, while $\|\iota(\varphi)\| \leq 1$, the sum $J$ is an integral combination of point tables in the limit. This gives part 1.

Step 5 ($w$ sees $\pi$). For $P \in V(\pi)$ we have $\pi \notin P^2$, because $|V(\pi)| = [F : \mathbb{Q}] = f$, each $P$ has norm $p$, and $\pi\bar\pi = p$. So there is a self-dual lattice $N''$ with $\pi N_{d'} \subseteq N''$, $\bar\pi N'' \subseteq N_{d'}$ and $N''_P = \{ y \in d'_P : f'_P(y) = 0 \}$ for $P \in V(\pi)$. Then $\chi(\det(N_{d'}, N'')) = \sigma_0(k)$ with
$$k = \prod_{\tau \in \mathcal{T}} \tau(\pi/\bar\pi)^{-1},$$
and $\|\iota(k)\| \leq p^f$, since $\|\iota\tau(\bar\pi/\pi)\| \leq p$ for each $\tau$. Put $\kappa = \sigma_0(k^{N_i/2})$. Then $\|\lambda(\kappa)\|^2 \leq p^{f N_i}$. Input 2 gives the move relation: for a set $R'$ of representatives of the periods for $(N_d, N_{d'})$ modulo those for $(N_d, N'')$,
$$\sum_{y \in R'} W_y\, e(N_d, N_{d'}) = \sqrt{|R'|}\; \kappa\; e(N_d, N''),$$
where we use $\chi(\det)^{-N_i/2} = \sigma_0(k)^{-N_i/2}$. The point moments at $\bar\pi/\pi$ come from the moment statement at $\pi$, as in Step 4. Summing over cosets as in Step 4, with $N''$ in place of $N_{d'}$ and the bound on $\kappa$, gives part 2 with the factor $p^{-f N_i}$. $\square$

*Proof of the integral jet moments.* This is the reduction theorem applied to three results. The equivariance laws hold for every curve ideal ([Theorem](/entry/euler-product-eq-of-curve-ideal/)), and the Taylor coefficients of the translates are algebraic. With these two facts, the [finiteness of moments](/entry/moments-fin/) gives input 1. The equivariance laws are input 2. The lattice facts, proved from the lattice facts of the base and the lattices of the seam, are input 3. $\square$

**Remark 4.10.7 (Formalization).** The second clause of the admissibility of the analytic data, $\sigma_0 = \sigma_0(D)$, is discarded at the start of the proof ([JetMomentsOfUnitPeriod.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/JetMomentsOfUnitPeriod.lean#L25)). The equivariance laws enter twice: inside input 1 and as input 2. The result that gives them is named after an Euler product ([FinalEq.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/SplitPairEquations/FinalEq.lean#L6)), which is not what it states. A second proof of the same statement, from the moment statement in its form with the period condition, sits in [MemSuppBarOfNe.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MemSuppBarOfNe.lean#L349). We did not unfold the kernel jets, the induced theta functions, the point moments, the lattice hypothesis, the smoothness condition or the ideal $\ell_\tau$. The jet sum is a sum over a quotient at representatives chosen by the axiom of choice. Steps 4 and 5 describe lemmas whose statements we read but whose proofs we did not open.
