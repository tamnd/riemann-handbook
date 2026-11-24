---
title: The archimedean mass bound
decls:
  - GlobalTheory.CovTop.VolUp.MassLow.massLow
  - GlobalTheory.T.archimedean_mass_product_lower_bound_unitary_pq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The archimedean mass bound

The previous section measured the real special unitary group with the Riemannian Haar measure. The adelic volume computations of the next sections use instead a product of fixed Haar measures on the unitary groups $U(p_\rho, q_\rho)$, one for each archimedean place. This section compares the two. It shows that the Riemannian measure of a set, times $(1/16)^{d r^2}$, is at most the product measure of its preimage, cut down to the half where one determinant has positive imaginary part. The bound is used in [the tube estimate](/entry/tube/).

We keep the notation of [the previous section](/entry/riem-haar-eq-smul/): a CM field $E$, a CM type $\Psi$ with $|\Psi| = d$, a hermitian matrix $G \in M_r(E)$, the group $\mathrm{SU}_\Psi$ of families $(g_\tau)_{\tau \in \Psi}$ of special unitary matrices for the forms $h_\tau$, a frame $x$ and the Riemannian Haar measure $\mathrm{vol}_x$.

**Definition 3.18.1 (Standard unitary groups and their measures).** For $p, q \in \mathbb{N}$ let $J_{p,q}$ be the diagonal matrix with $p$ entries $1$ and $q$ entries $-1$, and let $U(p, q)$ be the group of complex matrices $u$ of size $p + q$ with $u^* J_{p,q} u = J_{p,q}$. A measure $m$ on $U(p, q)$ is *standard* if it is a Haar measure and, near the identity, its ratio to a fixed Lebesgue measure on the Lie algebra, transported by the exponential map, tends to
$$2^{-N(N-1)/2}, \qquad N = p + q.$$
For $a_0 \in \{1, \dots, p + q\}$ and $u \in U(p, q)$ put
$$s_{a_0}(u) = u \cdot \mathrm{diag}(1, \dots, (\det u)^{-1}, \dots, 1),$$
with $(\det u)^{-1}$ at position $a_0$. Then $\det s_{a_0}(u) = 1$.

**Definition 3.18.2 (Identification and projection).** Let $\kappa$ be a finite set with a bijection $\sigma : \kappa \to \Psi$, and let $p, q : \kappa \to \mathbb{N}$. An *identification* of $(G, x)$ with the standard forms is a family of matrices $A_\rho$ of size $(p_\rho + q_\rho) \times r$ and bijections $e_\rho : \{1, \dots, p_\rho + q_\rho\} \to \{1, \dots, r\}$ such that for each $\rho \in \kappa$:

1. $A_\rho^* J_{p_\rho, q_\rho} A_\rho = -\,\sigma_\rho(G)^{T}$;
2. $A_\rho\, x_{\sigma_\rho} = P_\rho$, the permutation matrix of $e_\rho$.

A map $\pi : \prod_\rho U(p_\rho, q_\rho) \to \mathrm{SU}_\Psi$ is a *projection* for the identification and points $a_{0, \rho}$ if
$$A_\rho\, \pi(b)_{\sigma_\rho} = s_{a_{0,\rho}}(b_\rho)\, A_\rho \quad \text{for all } b \text{ and } \rho.$$
It is *equivariant* if for every $s \in \mathrm{SU}_\Psi$ and every $b_0$ with $b_{0, \rho} A_\rho = A_\rho\, s_{\sigma_\rho}$ for all $\rho$, we have $\pi(b_0 b) = s\, \pi(b)$ for all $b$.

So $A_\rho$ carries the form $-\sigma_\rho(G)^T$ to the standard form, and $\pi$ reads off the special unitary part of a family of unitary matrices in these coordinates.

**Theorem 3.18.3 (Archimedean mass bound).** Let $r \ge 1$. Let $(A, e)$ be an identification of $(G, x)$ with the standard forms, $\pi$ a continuous equivariant projection for $(A, a_0)$, and $m_\rho$ a standard measure on $U(p_\rho, q_\rho)$ for each $\rho \in \kappa$. Fix $\rho_0 \in \kappa$. Then for every measurable $S \subset \mathrm{SU}_\Psi$,
$$\Bigl(\tfrac1{16}\Bigr)^{d r^2} \mathrm{vol}_x(S) \le \Bigl(\prod_\rho m_\rho\Bigr)\bigl(\pi^{-1}(S) \cap T\bigr),$$
where $T = \{ b : \mathrm{Im} \det b_{\rho_0} > 0 \}$.

Lean: `GlobalTheory.CovTop.VolUp.MassLow.massLow` (also `GlobalTheory.T.archimedean_mass_product_lower_bound_unitary_pq`, a second name).

*Proof.* Write $\mu = \prod_\rho m_\rho$ and let $\nu$ be the image under $\pi$ of the restriction of $\mu$ to $T$, so that $\nu(S) = \mu(\pi^{-1}(S) \cap T)$. We show that $\nu$ is a Haar measure, compare it with $\mathrm{vol}_x$ by a constant $c$, and bound $c$ from below on a small ball.

*First facts.* Since $\sigma$ is a bijection, $|\kappa| = d$, and $d \ge 1$ since $\rho_0 \in \kappa$. Part 2 of the identification shows that $x_\tau$ is invertible for all $\tau$, and the bijection $e_\rho$ shows $p_\rho + q_\rho = r$.

*Left invariance.* Let $s \in \mathrm{SU}_\Psi$. An input lemma gives $b_0$ with $b_{0, \rho} A_\rho = A_\rho\, s_{\sigma_\rho}$ for all $\rho$. Then $b_{0, \rho_0} = P\, M\, P^{T}$ with $P$ the permutation matrix of $e_{\rho_0}$ and $M$ conjugate to $s_{\sigma_{\rho_0}}$, so
$$\det b_{0, \rho_0} = \det s_{\sigma_{\rho_0}} = 1.$$
Hence left multiplication by $b_0$ maps $T$ onto $T$. Since $\pi(b_0 b) = s \pi(b)$ and $\mu$ is left invariant, the image of $\nu$ under left multiplication by $s$ is $\nu$.

*Finiteness on compact sets.* An input upper bound for the product measure gives, for every compact $K \subset \mathrm{SU}_\Psi$, a bound of $\mu(\pi^{-1}(K))$ by a constant times $\mathrm{vol}_x(K)$, which is finite. So $\nu(K) < \infty$.

*The constant.* The Riemannian Haar measure is a Haar measure. By uniqueness of Haar measures, $\nu = c\, \mathrm{vol}_x$ for a constant $c \ge 0$. It is sufficient to show
$$c \ge \Bigl(\tfrac1{16}\Bigr)^{d r^2}.$$

*Two estimates on a ball.* For $\varepsilon > 0$ let $W_\varepsilon$ be the set of $s \in \mathrm{SU}_\Psi$ with
$$\bigl| (x_\tau^{-1} s_\tau x_\tau - 1)_{a b} \bigr| < \varepsilon \quad \text{for all } \tau, a, b.$$
Two input lemmas give $\varepsilon_0 > 0$ such that for $0 < \varepsilon < \varepsilon_0$:

1. at each place, the $m_\rho$-measure of the set of $u$ with $|s_{a_0}(u) - 1|_{ab} < \varepsilon$ for all entries and $\mathrm{Im} \det u > 0$ is at least $L = \varepsilon^{r^2 - 1} / r^{r - 1}$;
2. $\mathrm{vol}_x(W_\varepsilon) \le U = (8\varepsilon)^{d (r^2 - 1)}$.

Fix such an $\varepsilon$. The product of the sets in 1 lies in $\pi^{-1}(W_\varepsilon) \cap T$, by the projection property and part 2 of the identification. So
$$L^{d} \le \nu(W_\varepsilon) = c\, \mathrm{vol}_x(W_\varepsilon) \le c\, U.$$

*Arithmetic.* We have $r \le 2^r$, so $r^{r-1} \le 2^{r^2}$, and $8^{r^2 - 1} \le 8^{r^2}$. Hence
$$\Bigl(\tfrac1{16}\Bigr)^{r^2} (8\varepsilon)^{r^2 - 1} \le \Bigl(\tfrac{1 \cdot 8 \cdot 2}{16}\Bigr)^{r^2} \frac{\varepsilon^{r^2 - 1}}{r^{r-1}} = \frac{\varepsilon^{r^2-1}}{r^{r-1}}.$$
Raise this to the power $d$: $(1/16)^{d r^2}\, U \le L^d \le c\, U$. Since $U > 0$, we get $c \ge (1/16)^{d r^2}$.

*Conclusion.* For measurable $S$,
$$\Bigl(\tfrac1{16}\Bigr)^{d r^2} \mathrm{vol}_x(S) \le c\, \mathrm{vol}_x(S) = \nu(S) = \mu(\pi^{-1}(S) \cap T). \qquad \square$$

The constant $1/16$ is not sharp. It comes from the factor $8$ in the upper bound for the Riemannian ball, the factor $r^{r-1}$ in the lower bound for the unitary balls, and the crude bound $r^{r-1} \le 2^{r^2}$.

The left invariance needs the lift $b_0$ to have determinant $1$ at $\rho_0$, so that $T$ is kept.

**Remark 3.18.4 (Formalization).** The lower bound at each place is stated with the condition $\mathrm{Im} \det u > 0$ at every place, while $T$ needs it only at $\rho_0$; the product set is still contained in $\pi^{-1}(W_\varepsilon) \cap T$ ([ArchimedeanMassProductLowerBoundUnitaryPq.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArchimedeanMassProductLowerBoundUnitaryPq.lean#L66)). The identification, the projection and the ball $W_\varepsilon$ are defined in [PermMMulTranspose.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PermMMulTranspose.lean#L27). We have not unfolded the fixed Lebesgue measure on the Lie algebra of $U(p, q)$ in the definition of a standard measure, nor the three input estimates. The second name is a wrapper.
