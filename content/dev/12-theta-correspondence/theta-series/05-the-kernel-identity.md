---
title: The kernel identity
decls:
  - GlobalTheory.SW.KernSum.hasSum_eis
  - GlobalTheory.SW.kernel_identity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The kernel identity

This section proves a reproducing kernel identity for theta series on a unitary period domain. A product of two theta series, one at $x_1$ and the conjugate of one at $x_2$, is a theta series of a doubled test function on the doubled Hermitian space. By [the Siegel-Weil formula](/entry/siegel-weil-definite/) its genus sum equals an Eisenstein series, and the Eisenstein series unfolds into a sum over an arithmetic group $\Delta$. After applying a family of harmonic differential operators, this gives a kernel $K_P(x_1, x_2)$ whose average over $\Delta$ is a finite sum of products of theta series. The [spanning theorem](/entry/theta-span/) of the next section uses this identity to show that each bounded automorphic form is a combination of theta series. This is the method of [theta kernels](/learn/theta/#theta-kernels) and of [the doubling method](/learn/theta/#the-doubling-method).

### Systems of test functions

We keep the notation of [the first section](/entry/is-mu-multiplier-sq-mul-det/): a unitary period datum of rank $r$ with a symplectic basis of $\Lambda$, Hermitian matrix $G$ of signature $(p_0, q_0)$, $p_0 + q_0 = r$, the period domain $\mathcal{D}$, the theta series $\Theta_\varphi(x, z)$ of a Schwartz-Bruhat function $\varphi$ on $M_{n \times g}(\mathbb{Q})$, the inner product $\langle \varphi, \psi \rangle$, the Heisenberg action $\rho$, and the set $V_n(M)$ of self-dual lattices with the class sum $\sum_M$ of [the third section](/entry/swd-invariant-bound/). Let $n$ be even.

A matrix $\gamma \in \mathrm{GL}_r(E)$ is *unitary* if it preserves $h_G$. It acts on frames by $(\gamma x)_\tau = \tau(\gamma) x_\tau$ and on lattices $L \subset E^r$ by $L \mapsto \gamma L$. For unitary $\gamma$, the *global Weil transform* $\omega(\gamma)\varphi$ is a chosen Schwartz-Bruhat function $\psi$ with $\Theta_\psi(\gamma x, z) = \Theta_\varphi(x, z)$ for all $x \in \mathcal{D}$ and all $z$, and $0$ if there is none.

**Definition 3.5.1 (Theta system).** Let $M > 0$, let $\Delta$ be a subgroup of $\mathrm{GL}_r(E)$, let $\mathcal{L}$ be a set of $\mathcal{O}_E$-lattices in $E^r$, let $\Phi_{L, \Lambda}$ be a function on $M_{n \times g}(\mathbb{Q})$ for each $L$ and each $\Lambda \subset E^n$, and let $\mu(\gamma, L) \in \mathbb{C}$. This is a *theta system* of level $M$ if, for $L, L' \in \mathcal{L}$ and $\Lambda \in V_n(M)$:

1. each $\gamma \in \Delta$ is unitary and maps $\mathcal{L}$ to itself, and each $L \in \mathcal{L}$ is finitely generated and spans $E^r$;
2. $\Phi_{L, \Lambda}$ is Schwartz-Bruhat;
3. there are $a > 0$, $\theta < 1$ and $b(L, L') \ge 0$ with $\langle \Phi_{L,\Lambda}, \Phi_{L,\Lambda} \rangle = a$, $|\langle \Phi_{L,\Lambda}, \Phi_{L',\Lambda} \rangle| \le a\, b(L, L')$ and $\sum_{L' \ne L} b(L, L') \le \theta$ (a convergent sum);
4. for $\gamma \in \Delta$: $|\mu(\gamma, L)| = 1$ and $\omega(\gamma)\Phi_{L,\Lambda} = \mu(\gamma, L)\, \Phi_{\gamma L, \Lambda}$;
5. for unitary $\gamma \notin \Delta$: $\langle \Phi_{L,\Lambda}, \omega(\gamma)\Phi_{L',\Lambda} \rangle = 0$;
6. (cuspidality) for each $\xi \ne 0$ in $E^r$ with $h_G(\xi, \xi) = 0$ there are finitely many $v \in E^n$ and $a_v \in \mathbb{C}$ with $\sum_v a_v \ne 0$ and $\sum_v a_v\, \rho(v \xi^T)\Phi_{L,\Lambda} = 0$;
7. the doubled family $\Lambda \mapsto \Phi^{\mathrm{dbl}}_{L, L', \Lambda}$, defined below, is admissible of level $(M, R)$ for some $R$.

Condition 3 says that the vectors $\Phi_{L,\Lambda}$ are almost orthogonal, condition 4 that $\Delta$ permutes them up to phases, and condition 5 that the other unitary matrices move them to orthogonal vectors.

### Doubling

The doubled space is $E^r \oplus E^r$ with the form $h_G \oplus (-h_G)$. A pair of frames $x_1, x_2 \in \mathcal{D}$ gives a point $Z(x_1, x_2)$ of the Hermitian upper half space $\mathcal{H}_r$, and with $z, w \in (\mathbb{C}^g)^n$ it gives vectors $\zeta(x_1, x_2, z, w)$ and $\zeta'(x_1, x_2, z, w)$, and a factor
$$k_0(x_1, x_2, z, w) = \prod_{\tau \in \Psi} \big(\det a_\tau \det \bar a_\tau\big)^{-n/2} \exp\Big(\pi \sum_k \zeta'_{\tau,k}\, (\operatorname{Im} Z_\tau)^{-1} \zeta_{\tau,k}\Big),$$
where $a_\tau, \bar a_\tau$ are explicit matrices built from $x_1$ and $x_2$. We do not unfold these maps. They come from the doubling embedding of $U(G) \times U(G)$ in the unitary group of the doubled space.

**Definition 3.5.2 (Doubled test function).** For Schwartz-Bruhat $\varphi_1, \varphi_2$ on $M_{n \times g}(\mathbb{Q})$, the *doubled test function* $\varphi_1 \boxtimes \varphi_2$ is a chosen Schwartz-Bruhat function $\psi$ on $M_{n \times r}(E)$ with
$$\Theta_{\varphi_1}(x_1, z)\, \overline{\Theta_{\varphi_2}(x_2, \bar w)} = k_0(x_1, x_2, z, w)\, \theta_\psi\big(Z(x_1, x_2), \zeta, \zeta'\big)$$
for all $x_1, x_2 \in \mathcal{D}$ and all $z, w$, where $\theta_\psi$ is the [Hermitian theta series](/entry/bound-high/); it is $0$ if there is none. Put $\Phi^{\mathrm{dbl}}_{L, L', \Lambda} = \Phi_{L,\Lambda} \boxtimes \Phi_{L',\Lambda}$.

**Lemma 3.5.3 (Unfolding the Eisenstein series).** Let $n$ be even with $4r < n$, let $(\Delta, \mathcal{L}, \Phi, \mu)$ be a theta system of level $M$, and let $a \in \mathbb{C}$ with $(\varphi_1 \boxtimes \varphi_2)(0) = a \langle \varphi_1, \varphi_2 \rangle$ for all Schwartz-Bruhat $\varphi_1, \varphi_2$. Let $L_1, L_2 \in \mathcal{L}$, $x_1, x_2 \in \mathcal{D}$, $\Lambda \in V_n(M)$ and $z, w$. Then the series
$$\sum_{\gamma \in \Delta} a\, \langle \Phi_{L_1,\Lambda}, \Phi_{\gamma L_2,\Lambda} \rangle\, \overline{\mu(\gamma, L_2)}\, k_0(x_1, \gamma x_2, z, w)$$
converges, with sum $k_0(x_1, x_2, z, w)\, E_{\Phi_{L_1,\Lambda} \boxtimes \Phi_{L_2,\Lambda}}\big(Z(x_1,x_2), \zeta, \zeta'\big)$.

Lean: `GlobalTheory.SW.KernSum.hasSum_eis`

*Proof.* Put $\psi = \Phi_{L_1,\Lambda} \boxtimes \Phi_{L_2,\Lambda}$. For $4r < n$ the Eisenstein series $E_\psi$ converges absolutely, by a result of the sources, so we may sum it in any order. Its terms are indexed by the Lagrangian subspaces of the doubled space. A result of the sources says that each Lagrangian is either the graph of a unique unitary $\gamma$, or contains a vector $\xi \ne 0$ with $h_G(\xi, \xi) = 0$. For the graph of $\gamma$, the term times $k_0(x_1, x_2, z, w)$ equals $a \langle \Phi_{L_1,\Lambda}, \omega(\gamma)\Phi_{L_2,\Lambda} \rangle\, k_0(x_1, \gamma x_2, z, w)$, by the transformation law of the doubled test function and the choice of $a$. If $\gamma \notin \Delta$ this is $0$ by condition 5. If $\gamma \in \Delta$, condition 4 gives $\langle \Phi_{L_1,\Lambda}, \mu(\gamma, L_2)\Phi_{\gamma L_2,\Lambda} \rangle = \overline{\mu(\gamma, L_2)} \langle \Phi_{L_1,\Lambda}, \Phi_{\gamma L_2,\Lambda} \rangle$, which is the term of the series. For a Lagrangian that contains an isotropic $\xi$, the Weil transform of $\psi$ vanishes at $0$: condition 6 gives a nontrivial relation among the Heisenberg translates of $\Phi_{L_i,\Lambda}$ along $\xi$, and a result of the sources turns it into this vanishing. $\square$

### The identity

The polynomials have one letter $z_{\tau, j, k}$ for each $\tau \in \Psi$, each index $j$ of one of the two blocks of sizes $q_0$ and $p_0$, and each $k \in \{1, \dots, n\}$. The pair $(\tau, j)$ picks a row of $G$ and so a column $i \in \{1, \dots, g\}$, and the letter stands for the coordinate $z_{k, i}$ of $z \in (\mathbb{C}^g)^n$. For a polynomial $P$, write $P(\partial_z)$ for the constant coefficient operator that replaces each letter by the derivative in its coordinate. Put
$$\Theta^P_\varphi(x) = P(\partial_z)\Theta_\varphi(x, z)\big|_{z=0}.$$
For a finite family $P = (P_1, \dots, P_m)$ put
$$K_P(x_1, x_2) = \sum_{j=1}^m P_j(\partial_z)\, \bar P_j(\partial_w)\, k_0(x_1, x_2, z, w)\big|_{z = w = 0},$$
where $\bar P_j$ has the conjugate coefficients. The family is *unitarily invariant* if $\sum_j P_j(u z)\, \overline{P_j(u w)} = \sum_j P_j(z)\overline{P_j(w)}$ for every family $u = (u_\tau)_{\tau \in \Psi}$ of unitary $n \times n$ matrices, where $u_\tau$ acts on the index $k$ of the letters $z_{\tau, j, k}$. For weights $c$ on $\Psi \times \{1, \dots, q_0\}$ and $c'$ on $\Psi \times \{1, \dots, p_0\}$, there is a set of *highest weight harmonic polynomials* of type $(c, c')$. We do not unfold its definition; it plays the role of the highest weight vectors in the harmonic polynomials of Kashiwara and Vergne.

**Theorem 3.5.4 (Kernel identity).** Let $n$ be even with $4r < n$, let $M > 0$, and let $(\Delta, \mathcal{L}, \Phi, \mu)$ be a theta system of level $M$. Then there is $a \ne 0$ such that for all types $(c, c')$, every unitarily invariant family $P_1, \dots, P_m$ of highest weight harmonic polynomials of type $(c, c')$, all $L_1, L_2 \in \mathcal{L}$ and all $x_1, x_2 \in \mathcal{D}$, the series
$$\sum_{\gamma \in \Delta} a \sum\nolimits_M \langle \Phi_{L_1,\Lambda}, \Phi_{\gamma L_2,\Lambda} \rangle\; \overline{\mu(\gamma, L_2)}\; K_P(x_1, \gamma x_2)$$
converges, with sum
$$\sum\nolimits_M \sum_{j=1}^m \Theta^{P_j}_{\Phi_{L_1,\Lambda}}(x_1)\, \overline{\Theta^{P_j}_{\Phi_{L_2,\Lambda}}(x_2)}.$$

Lean: `GlobalTheory.SW.kernel_identity`

*Proof.* A result of the sources gives $a \ne 0$ with $(\varphi_1 \boxtimes \varphi_2)(0) = a \langle \varphi_1, \varphi_2 \rangle$ for all Schwartz-Bruhat $\varphi_1, \varphi_2$; the doubled test function exists for each such pair. Fix $L_1, L_2, x_1, x_2$, and write $p = (z, w)$. Put
$$S(p) = \sum\nolimits_M k_0(x_1, x_2, z, w)\, E_{\Phi^{\mathrm{dbl}}_{L_1, L_2, \Lambda}}\big(Z(x_1, x_2), \zeta, \zeta'\big),$$
$$T(p) = \sum\nolimits_M \Theta_{\Phi_{L_1,\Lambda}}(x_1, z)\, \overline{\Theta_{\Phi_{L_2,\Lambda}}(x_2, \bar w)}.$$

Step 1. Summing the [unfolding lemma](/entry/has-sum-eis/) over the finitely many classes gives, for each $p$, the identity $S(p) = \sum_{\gamma \in \Delta} c_\gamma\, k_0(x_1, \gamma x_2, p)$ with $c_\gamma = a \sum_M \langle \Phi_{L_1,\Lambda}, \Phi_{\gamma L_2,\Lambda} \rangle \overline{\mu(\gamma, L_2)}$. Each $k_0(x_1, \gamma x_2, \cdot)$ is a constant times the exponential of a quadratic form in $p$. For a convergent sum of such Gaussians, the sum is analytic and constant coefficient derivatives may be taken term by term. Applying $\sum_j P_j(\partial_z)\bar P_j(\partial_w)$ at $p = 0$ gives the series of the theorem, with sum $\sum_j P_j(\partial_z)\bar P_j(\partial_w) S(0)$.

Step 2. The theta series are holomorphic in $z$, since the $P_j$ are highest weight harmonic polynomials of type $(c, c')$ and the test functions are Schwartz-Bruhat. The column directions are real, so $P_j(\partial_z)\bar P_j(\partial_w)$ applied to $f(z)\overline{g(\bar w)}$ at $0$ gives $P_j(\partial)f(0)\, \overline{P_j(\partial)g(0)}$. Hence $\sum_j P_j(\partial_z)\bar P_j(\partial_w) T(0)$ is the claimed sum.

Step 3. By the definition of the doubled test function, $T(p) - S(p) = k_0(x_1, x_2, z, w)\, D(Z(x_1, x_2), \zeta, \zeta')$, where $D$ is the Siegel-Weil difference of the doubled family $\Lambda \mapsto \Phi^{\mathrm{dbl}}_{L_1, L_2, \Lambda}$. This family is admissible by condition 7. So $D$ solves the heat equation, by a result of the sources, and $D(Z, 0, 0) = 0$ for all $Z \in \mathcal{H}_r$ by [the Siegel-Weil formula](/entry/siegel-weil-definite/) in rank $n$ and degree $r$, since $4r < n$. A result of the sources says that, for a unitarily invariant family $P$ and $r \le n$, the operator $\sum_j P_j(\partial_z)\bar P_j(\partial_w)$ at $0$ kills $k_0 \cdot D$ for every such $D$. So the two derivatives at $0$ agree, and the theorem follows from Steps 1 and 2. $\square$

**Remark 3.5.5 (Formalization).** We have not unfolded the doubling maps $Z(x_1, x_2)$, $\zeta$, $\zeta'$, the matrices $a_\tau, \bar a_\tau$, or the highest weight condition `Harm.rowHighest`; its role in the proof is to give the holomorphy in Step 2. The doubled test function and the global Weil transform are defined by choice, and are $0$ when no function exists ([IsSystem.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/IsSystem.lean#L34)). In the theorem the types $c, c'$ enter only through the highest weight hypothesis, which gives the holomorphy in Step 2 ([KernelIdentity.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/KernelIdentity.lean#L207)). The convergence of the Eisenstein series, the classification of Lagrangians, the vanishing on isotropic Lagrangians, the heat equation and the killing of heat solutions are results of the sources.
