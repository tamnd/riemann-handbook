---
title: Hecke parameters along the chain
decls:
  - GlobalTheory.T.chainThetaLiftUpLowerBlockParameter_proof
  - GlobalTheory.ChainTw.upQ_holds
  - GlobalTheory.T.lowerBlockParameter_transfer_invariantPairing
  - GlobalTheory.ParHeckeTransfer.transfer
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke parameters along the chain

The local factor at a twist place in [the section on the local factor](/entry/local-factor/) needs one input: the first form of the step must be a generic vector of the twisted type, with known parameters, at each twist place. This section proves that the theta lift keeps this property along the chain, and it gives the rule for the parameters. At each step the old parameters are multiplied by a ratio of two splitting characters, and a segment of length $t$ is added. The proof is local: a pairing that is equivariant for the [Weil representation](/learn/theta/#the-weil-representation) carries generic vectors to generic vectors. The result is used in [the proof of the step scalars](/entry/scalars-of-given-all/), where it gives the hypothesis of the local factor at every stage.

We use the notation of [the section on the doubling integral](/entry/local-zeta-twisted/): a nonarchimedean local field $k$ with ring of integers $\mathcal{O}$, residue field of $q$ elements and a uniformizer $\varpi$; the parahoric $J$ of $\mathrm{GL}_{r+N}(k)$; the type space $V^{J,\xi}$; the twisted Hecke operators; and the numbers $\gamma^r_n(B)$. A character of $k^\times$ is *tame* if it is trivial on $1 + \mathfrak{p}$, and *unramified* if it is trivial on $\mathcal{O}^\times$. See [depth zero types](/learn/representations/#depth-zero-representations-and-types).

**Definition 2.5.1 (Segment).** For $z \in \mathbb{C}^\times$ and $t \geq 0$, the *segment* of length $t$ at $z$ is the multiset
$$\mathrm{seg}(z, t) = \{\, z\, |\varpi|^{\,n - (t-1)/2} : n = 0, 1, \dots, t-1 \,\}.$$

**Definition 2.5.2 (The two character Weil action).** Let $a, b \geq 0$ and let $\mu_S, \mu_T$ be characters of $k^\times$. For a function $u$ on $M_{b \times a}(k)$, $g \in \mathrm{GL}_a(k)$ and $h \in \mathrm{GL}_b(k)$ put
$$\omega_{\mu_S, \mu_T}(g, h) u = (\mu_S \mu_T^{-1})(\det h)\, \omega_{\mu_T^{-1}}(g, h) u,$$
with $\omega_\mu$ as in the section on the doubling integral. So $\omega_{\mu_S, \mu_T}(g, h)u(x) = \mu_T(\det g)^{-1} \mu_S(\det h)\, |\det g|^{b/2} |\det h|^{-a/2}\, u(h^{-1} x g)$. For $\mu_S = \mu_T = \mu$ this is $\omega_{\mu^{-1}}$.

Below, $\Phi_\xi$ is the test function of the section on the doubling integral, formed on matrices of size $(r + N') \times (r + N)$.

**Theorem 2.5.3 (Parameter transfer).** Let $r, N, t \geq 0$ and $N' = N + t$. Let $\xi, \mu_S, \mu_T$ be characters of $k^\times$ such that $\xi$ is tame and $\mu_S \xi^{-1}$, $\mu_T \xi^{-1}$ are unramified. Let $W$ be a space of functions on $M_{(r+N') \times (r+N)}(k)$ that is stable under $\omega_{\mu_S, \mu_T}$ and contains $\Phi_{\xi}$. Let $\pi$ be a representation of $\mathrm{GL}_{r+N}(k)$ on $X$, and let $x \in X$ be generic of type $\xi$ with parameters $B$. Let $\pi'$ be a representation of $\mathrm{GL}_{r+N'}(k)$ on $X'$, and let $b \colon W \times X \to X'$ be bilinear with
$$b(\omega_{\mu_S, \mu_T}(g, h) u,\ \pi(g) y) = \pi'(h)\, b(u, y)$$
for all $g, h, u, y$. Then $b(\Phi_\xi, x)$ is generic of type $\xi$ with parameters
$$B' = B \cdot \mu_S(\varpi) \mu_T(\varpi)^{-1} + \mathrm{seg}(\mu_S(\varpi), t).$$

Lean: `GlobalTheory.ParHeckeTransfer.transfer` (also `GlobalTheory.T.lowerBlockParameter_transfer_invariantPairing`, a second name).

*Proof.* Put $x' = b(\Phi_\xi, x)$. There are three things to prove.

*The type.* Let $j$ be in the parahoric of $\mathrm{GL}_{r+N'}(k)$, with $d = \det j_{22}$. The equivariance at $g = 1$ gives $\pi'(j) x' = b(\omega_{\mu_S, \mu_T}(1, j)\Phi_\xi, x)$. Since $\xi$ is tame and $\mu_S \xi^{-1}$ is unramified, $\omega_{\mu_S, \mu_T}(1, j)\Phi_\xi = \xi(d)\, \Phi_\xi$. So $\pi'(j)x' = \xi(d)\, x'$, and $x'$ is in the type space.

*The number of parameters.* $B'$ has $N + t = N'$ elements.

*The Hecke eigenvalues.* Fix a subset $s$ of the lower block of size $N'$ and let $m = |s|$. For each $0 \leq n \leq N$ choose a subset $s_n$ of the lower block of size $N$ with $n$ elements. Put
$$\begin{aligned} C &= \mu_S(\varpi)^m\, q^{m(r+N)/2}, \qquad \delta_n = \mu_T(\varpi)^n\, q^{n(r+N')/2}, \\ c_n &= q^{\,n(t - m + n)} \binom{t}{m-n}_q \quad (n \leq m), \qquad c_n = 0 \quad (n > m), \end{aligned}$$
where $\binom{t}{i}_q$ is the Gaussian binomial coefficient. The first and main step is an identity of functions in $W$:
$$\sum_{j \in R'} \xi(d_j)^{-1}\, \omega_{\mu_S,\mu_T}(1, j t_{1_s}) \Phi_\xi = C \sum_{n=0}^{N} \frac{c_n}{\delta_n} \sum_{j \in R_n} \xi(d_j)\, \omega_{\mu_S,\mu_T}(j t_{-1_{s_n}}, 1) \Phi_\xi,$$
where $R'$ and $R_n$ are systems of representatives for the twisted Hecke operators at $t_{1_s}$ and at $t_{-1_{s_n}}$. To prove it, evaluate both sides at a matrix $y$. The torus parts act through $\mu_S(\varpi)$ on the right and $\mu_T(\varpi)$ on the left, which gives the constants $C$ and $\delta_n$. After this, both sides are $\Phi_\xi(y)$ times a sum of indicator functions of integral matrices, evaluated at translates of the Schur complement $y_{22} - y_{21} y_{11}^{-1} y_{12}$. The two sums of indicator functions are equal by a Hecke identity for the indicator function of integral $N \times N'$ matrices, with the coefficients $c_n$.

Now apply $b(\cdot, x)$ to this identity. The left side becomes $\sum_{j \in R'} \xi(d_j)^{-1} \pi'(j t_{1_s}) x'$, by the equivariance at $g = 1$. On the right side, the equivariance at $h = 1$ moves $\omega_{\mu_S,\mu_T}(j t_{-1_{s_n}}, 1)$ to the vector $x$, and the inner sum becomes $b(\Phi_\xi, \cdot)$ of a twisted Hecke operator on $x$. Since $x$ is generic with parameters $B$, the inner sum is $\gamma^r_n(B)\, x'$. So $x'$ is an eigenvector of the twisted Hecke operator at $t_{1_s}$ with the eigenvalue
$$C \sum_{n=0}^{N} \frac{c_n}{\delta_n}\, \gamma^r_n(B).$$
The last step is an identity of symmetric functions: this sum equals $\gamma^r_m(B')$. It comes from $e_m(B') = \sum_n e_n(B \cdot \mu_S(\varpi)\mu_T(\varpi)^{-1})\, e_{m-n}(\mathrm{seg}(\mu_S(\varpi), t))$ and the evaluation of the elementary symmetric functions of a segment by Gaussian binomial coefficients. $\square$

For $r = 0$, trivial $\xi$ and $\mu_S = \mu_T$, this is the classical statement that the theta lift of an unramified representation of $\mathrm{GL}_N$ to $\mathrm{GL}_{N+t}$ has the Satake parameters of the source together with a segment.

Now return to the chain, in the setting of [the section on the local factor](/entry/local-factor/). Let $\mathfrak{P}$ be a twist place over $v$, let $\varpi$ be a uniformizer of $F_v$, and let $x$ be the idele of $E$ that is $\varpi$ at the factor of $\mathfrak{P}$ and $1$ at the other places. For $q$ the size of the residue field at $\mathfrak{P}$, which is also the size at $v$, the segment above is formed with $|\varpi| = q^{-1}$.

**Definition 2.5.4 (Parameters of the chain).** The *parameters of the chain at the index $k$* are the multisets $B_k$ given by $B_0 = \emptyset$ and
$$B_{i+1} = B_i \cdot \chi_{S,i+1}(x)\, \chi_{T,i+1}(x)^{-1} + \mathrm{seg}(\chi_{S,i+1}(x), t).$$
So $B_k$ has $kt$ elements, the number of rows of the lower block at the stage $V_k$. A function $F$ on $U(V_k)(\mathbb{A})$ *has the twisted type of the chain at the index $k$* if at every twist place, for every lift $\xi_l$ of $\xi_{\mathfrak{P}}$, every uniformizer and every chart $\iota$, the function $\overline{F}$ is generic of type $\xi_l$ with parameters $B_k$ for the representation $y \mapsto R(\iota(y))$, where $R$ is right translation. A form of the stage has the twisted type if each of its automorphic functions has it.

At the index $0$ the lower block is empty, and the condition says only that $\overline{F}$ has type $\xi_l$ for $\mathrm{GL}_r$.

**Theorem 2.5.5 (Hecke parameters along the chain).** Assume the rapid decay of cusp forms and the node gap condition. Let $k < m$, and take a step from $V_k$ to $V_{k+1}$ of a twisted theta chain. Let $u$ be a form of the stage $V_k$ with the twisted type of the chain at the index $k$, let $\varphi$ be a polynomial, and let $v$ be a $K$-finite vector. Then the theta lift of the automorphic function of $u$ at $v$, for the test function attached to $\varphi$, has the twisted type of the chain at the index $k+1$.

Lean: `GlobalTheory.ChainTw.upQ_holds` (also `GlobalTheory.T.chainThetaLiftUpLowerBlockParameter_proof`, a second name).

*Proof.* Let $F$ be the automorphic function, and fix a twist place $\mathfrak{P}$ over $v$, a uniformizer $\varpi$, a lift $\xi_l$ of $\xi_{\mathfrak{P}}$ and a chart $\iota'$ at the stage $V_{k+1}$. We must show that the conjugate of the lift of $F$ is generic of type $\xi_l$ with parameters $B_{k+1}$.

1. *Charts and characters.* By [the theorem on charts](/entry/split-place-chart-parahoric-level-stabiliser-height/) there are a chart $\iota$ at the stage $V_k$ and characters $\mu_S, \mu_T$ of $F_v^\times$ that match $\chi_{S,k+1}$ and $\chi_{T,k+1}$ at $v$. Then $\mu_S(\varpi) = \chi_{S,k+1}(x)$ and $\mu_T(\varpi) = \chi_{T,k+1}(x)$.
2. *The linear model.* A lemma on the linear model at a twist place gives a space $W$ of functions on $M_{(r+(k+1)t) \times (r+kt)}(F_v)$, stable under $\omega_{\mu_S, \mu_T}$ and containing $\Phi_{\xi_l}$, and a linear map $T$ from $W$ to the test functions of the global Weil representation. The map $T$ sends $\Phi_{\xi_l}$ to the test function of the step, and it carries $\omega_{\mu_S,\mu_T}(g, h)$ to the global Weil action of $(\iota(g), \iota'(h))$.
3. *The characters.* The lift $\xi_l$ is tame. The residue characters of $\chi_{S,k+1}$ and $\chi_{T,k+1}$ at $\mathfrak{P}$ are $\xi_{\mathfrak{P}}$, so $\mu_S$ and $\mu_T$ also lift $\xi_{\mathfrak{P}}$. Two lifts $\mu, \mu'$ of the same character differ by an unramified character. Indeed, for $y \in \mathcal{O}_v^\times$ choose an integer $a_0$ of $F$ with $y - a_0 \in \mathfrak{p}_v$. Then $a_0$ is not in $\mathfrak{P}$, its residue class $\kappa$ is a unit, and $\mu(y) = \xi_{\mathfrak{P}}(\kappa) = \mu'(y)$. So $\mu_S \xi_l^{-1}$ and $\mu_T \xi_l^{-1}$ are unramified.
4. *The source space.* Let $X$ be the span of the right translates $R(\iota(a))\overline{F}$, with $\mathrm{GL}_{r+kt}(F_v)$ acting by $\rho(a) = R(\iota(a))$. Every element of $X$ is invariant on the left under the rational points, and its product with a theta kernel is integrable on the fundamental domain. By hypothesis, $\overline{F}$ is generic of type $\xi_l$ with parameters $B_k$ for right translation on all functions. Since the inclusion of $X$ is injective and equivariant, $\overline{F}$ is generic with the same parameters in $X$.
5. *The pairing.* For $u \in W$ and $f \in X$ let $b(u, f)(y) = \int_{\mathcal{F}} \theta(g, y; T u)\, f(g)\, dg$, where $\mathcal{F}$ is the fundamental domain and $\theta(g, y; \cdot)$ is the theta kernel. This is bilinear. By step 2, $b(\omega_{\mu_S,\mu_T}(g,h)u, \rho(g)f)$ is the integral of $\theta(g'\iota(g), y\iota'(h); Tu)\, f(g'\iota(g))$ over $g' \in \mathcal{F}$. The integrand is invariant on the left under the rational points, so right translation by $\iota(g)$ does not change the integral. This gives the equivariance $b(\omega_{\mu_S,\mu_T}(g,h)u, \rho(g)f) = R(\iota'(h))\, b(u, f)$.
6. *Transfer.* The theorem on parameter transfer, with $N = kt$ and $N' = (k+1)t$, shows that $b(\Phi_{\xi_l}, \overline{F})$ is generic of type $\xi_l$ with parameters $B_k \cdot \mu_S(\varpi)\mu_T(\varpi)^{-1} + \mathrm{seg}(\mu_S(\varpi), t)$. By step 1 these are the parameters $B_{k+1}$.
7. *The lift.* Since $T\Phi_{\xi_l}$ is the test function of the step,
$$b(\Phi_{\xi_l}, \overline{F})(y) = \int_{\mathcal{F}} \theta(g, y; T\Phi_{\xi_l})\, \overline{F(g)}\, dg = \overline{\int_{\mathcal{F}} \overline{\theta(g, y; T\Phi_{\xi_l})}\, F(g)\, dg},$$
which is the conjugate of the theta lift of $F$ at $y$.

Steps 6 and 7 prove the claim. $\square$

The parameters $B_k$ do not depend on the form, only on the chain. This is what makes the local factor at the index $k$ a function of the chain alone.

**Remark 2.5.6 (Formalization).** The transfer theorem is at [LowerBlockParameterTransferInvariantPairing.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LowerBlockParameterTransferInvariantPairing.lean#L19), and the chain theorem at [ChainThetaLiftUpLowerBlockParameterProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainThetaLiftUpLowerBlockParameterProof.lean#L96), with the helper lemmas for step 4, step 3 and the segment at lines 32, 64 and 48. The genericity, the segment and the two character Weil action are defined in [IsCoType.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsCoType.lean#L26), and the parameters of the chain and the twisted type in [IsLevMeas.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsLevMeas.lean#L73). In the formal statement the chain parameters are formed with a segment at the place $\mathfrak{P}$, and a lemma (line 48) identifies it with the local segment, using the size of the residue field. We have not unfolded the test function $\Phi_\xi$, the parahoric at the new size or the power of the absolute value in the segment, and we have read only the statements of these lemmas: the action of the parahoric on $\Phi_\xi$, the two evaluations of the sums over representatives, the Hecke identity for integral matrices, the reduction to the eigenvalues $\gamma^r_n(B)$, the identity of symmetric functions, the charts at a twist place, the linear model, the residue characters of the splitting characters, the integrability against theta kernels and the invariance of the integral over the fundamental domain. In the chain theorem the hypothesis that $v$ is $K$-finite is not used.
