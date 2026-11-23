---
title: Bounds for the Siegel-Weil difference
decls:
  - GlobalTheory.SW.InvBound.bound_high
  - GlobalTheory.SW.swd_invariant_bound
  - GlobalTheory.T.siegelWeil_difference_invariant_norm_bounded
  - GlobalTheory.SW.twist_swd_bounded
  - GlobalTheory.T.twisted_siegelWeil_difference_bounded
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bounds for the Siegel-Weil difference

The Siegel-Weil formula says that a weighted sum of theta series over the classes of a genus of Hermitian lattices equals an Eisenstein series. The next section proves it for definite Hermitian lattices of rank $n$ and degree $N$ with $4N < n$, by induction on $N$. The difference $D_\varphi$ between the two sides is a holomorphic function on a Hermitian upper half space. This section proves that, if the formula holds in degree $N$, then $|D_\varphi(Z)| \det(\operatorname{Im} Z)^{n/2}$ is bounded in degree $N + 1$, with a bound that is uniform in the test functions and in a family of twists. The induction step of the next section turns this bound into the vanishing of $D_\varphi$.

### Hermitian theta and Eisenstein series

Let $E$ be a CM field with complex conjugation $a \mapsto \bar a$, and $\Psi$ a CM type of $E$: for each embedding $\tau \colon E \to \mathbb{C}$, exactly one of $\tau$ and $\bar\tau$ lies in $\Psi$. For a matrix $g$ over $E$ write $g^* = \bar g^T$. For a complex square matrix $Z$ put $\operatorname{Im} Z = (2i)^{-1}(Z - Z^*)$.

**Definition 3.3.1 (Hermitian upper half space).** The *Hermitian upper half space* of degree $N$ is the set $\mathcal{H}_N$ of families $Z = (Z_\tau)_{\tau \in \Psi}$ of complex $N \times N$ matrices with $\operatorname{Im} Z_\tau$ positive definite for each $\tau$. For $\delta > 0$, $\mathcal{H}_N(\delta)$ is the subset where $\operatorname{Im} Z_\tau - \delta$ is positive semidefinite for each $\tau$. Put $\Delta(Z) = \prod_{\tau \in \Psi} \det \operatorname{Im} Z_\tau$.

**Definition 3.3.2 (Hermitian theta series).** Let $\varphi$ be a function on $M_{n \times N}(E)$. For $Z \in \mathcal{H}_N$ and families $z = (z_\tau)$, $z' = (z'_\tau)$ of complex $n \times N$ matrices, put
$$\theta_\varphi(Z, z, z') = \sum_{x \in M_{n \times N}(E)} \varphi(x)\, e\Big(\sum_{\tau \in \Psi} \sum_{k=1}^n \big(\tau(x_k) Z_\tau \tau(x_k)^* + \tau(x_k) \cdot z_{\tau,k} + z'_{\tau, k} \cdot \overline{\tau(x_k)}\big)\Big),$$
with $e(w) = e^{2\pi i w}$ and $x_k$ the $k$-th row of $x$.

This is the [[theta series|2F5CYQJVAF]] of the [[Hermitian form|8NJ7XY6F1S]] $\operatorname{tr}(x Z x^*)$, with two variables for the linear terms. For $\varphi$ the characteristic function of $L^n$ for an $\mathcal{O}_E$-lattice $L$, it counts the vectors of $L$ by their Gram matrices, as in [theta series of lattices](/learn/theta-functions-cm/#theta-series-of-lattices).

Let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ in $M_{2N}(E)$, and let $U(N,N)$ be the group of $\gamma \in M_{2N}(E)$ with $\gamma^* J \gamma = J$. Write $\gamma = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$. It acts on $\mathcal{H}_N$ by $\gamma Z = \big((A_\tau Z_\tau + B_\tau)(C_\tau Z_\tau + D_\tau)^{-1}\big)_\tau$, where $A_\tau$ is $A$ with $\tau$ applied to the entries. The automorphy factor is
$$j(\gamma, Z, z, z') = \prod_{\tau \in \Psi} \det(C_\tau Z_\tau + D_\tau)^n \, e\Big(\sum_k z'_{\tau,k} (C_\tau Z_\tau + D_\tau)^{-1} C_\tau\, z_{\tau,k}\Big).$$

**Definition 3.3.3 (Weil transform).** A function $\varphi$ on $M_{n \times N}(E)$ is *Schwartz-Bruhat* if there is $R > 0$ such that $\varphi(x) \ne 0$ implies $R x$ integral, and $\varphi(x + R y) = \varphi(x)$ for integral $y$. For $\gamma \in U(N,N)$, a *Weil transform* of $\varphi$ is a Schwartz-Bruhat function $\psi$ with
$$\theta_\psi\big(\gamma Z, (Z C^* + D^*)^{-1} z, z' (CZ + D)^{-1}\big) = j(\gamma, Z, z, z')\, \theta_\varphi(Z, z, z')$$
for all $Z, z, z'$, with the matrices acting through $\tau$ in each component. We write $\omega(\gamma)\varphi$ for a chosen Weil transform when one exists, and $\omega(\gamma)\varphi = 0$ when none exists.

This is the [[Weil representation|H3Q2703KKV]] of $U(N,N)$ in the form of [the transformation formula](/learn/theta-functions-cm/#the-transformation-formula): it is defined by the theta series that it transforms.

**Definition 3.3.4 (Hermitian Eisenstein series).** Let $\mathcal{L}_N$ be the set of subspaces of $E^{2N}$ that are spanned by the last $N$ columns of some $\gamma \in U(N,N)$, and for each $U \in \mathcal{L}_N$ choose such a $\gamma_U$. The *Eisenstein series* of $\varphi$ is
$$E_\varphi(Z, z, z') = \sum_{U \in \mathcal{L}_N} (\omega(\gamma_U)\varphi)(0)\, j(\gamma_U, Z, z, z')^{-1}.$$

This is the Siegel [[Eisenstein series|3NZBZXYWAJ]] of $U(N,N)$ attached to the section $\gamma \mapsto (\omega(\gamma)\varphi)(0)$, as in [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

### Genus sums and the difference

Let $\mathcal{O}_E^m$ be the standard lattice. Two $\mathcal{O}_E$-submodules $\Lambda, \Lambda'$ of $E^m$ *agree away from* $M$ if there is $s > 0$ prime to $M$ with $s\Lambda \subset \Lambda'$ and $s\Lambda' \subset \Lambda$. Let $V_n(M)$ be the set of finitely generated $\Lambda \subset E^n$ that are self-dual for $\sum_k u_k \bar v_k$ and agree with $\mathcal{O}_E^n$ away from $M$. Let $\Gamma_n(M)$ be the set of unitary $h \in M_n(E)$ with $s(h - 1) \in M \cdot M_n(\mathcal{O}_E)$ for some $s > 0$ prime to $M$. A *class* is an orbit of $\Gamma_n(M)$ on $V_n(M)$. The set of classes is finite, by [the theory of the genus](/learn/hermitian-lattices/#genus-class-and-spinor-genus).

**Definition 3.3.5 (Class sum).** For a function $f$ on lattices put
$$\sum\nolimits_M f = \sum_{c} \frac{f(\Lambda_c)}{|\mathrm{Stab}(\Lambda_c)|},$$
over the classes $c$, with $\Lambda_c$ a chosen lattice of the class $c$ and $\mathrm{Stab}(\Lambda_c)$ its stabilizer in $\Gamma_n(M)$.

**Definition 3.3.6 (Admissible family).** Let $M, R > 0$. A family $\varphi = (\varphi_\Lambda)$ of functions on $M_{n \times N}(E)$, one for each lattice $\Lambda \subset E^n$, is *admissible of level* $(M, R)$ if, for $\Lambda, \Lambda' \in V_n(M)$:

1. $\varphi_{\Lambda'}(h x) = \varphi_\Lambda(x)$ when $h \in \Gamma_n(M)$ and $h\Lambda = \Lambda'$;
2. $\varphi_\Lambda(x) \ne 0$ implies that the columns of $R x$ lie in $\Lambda$;
3. $\varphi_\Lambda(x + R y) = \varphi_\Lambda(x)$ when the columns of $y$ lie in $\Lambda$;
4. $\varphi_\Lambda(x) = \varphi_{\Lambda'}(x)$ when $\Lambda$ and $\Lambda'$ agree away from $RM$ and the columns of $Rx$ lie in both.

**Definition 3.3.7 (Siegel-Weil difference).** For an admissible family $\varphi$ put
$$D_\varphi(Z, z, z') = \sum\nolimits_M \big(\theta_{\varphi_\Lambda}(Z, z, z') - E_{\varphi_\Lambda}(Z, z, z')\big),$$
and $D_\varphi(Z) = D_\varphi(Z, 0, 0)$. We say that the *Siegel-Weil formula holds in rank* $n$ *and degree* $N$, and write $\mathrm{SW}(n, N)$, if $D_\varphi(Z) = 0$ for all $M, R$, all admissible $\varphi$ of level $(M, R)$ and all $Z \in \mathcal{H}_N$.

### The bound on a Siegel set

**Lemma 3.3.8 (Bound high in the half space).** Let $\Psi$ be a CM type, let $n$ be even with $4(N+1) < n$, and assume $\mathrm{SW}(n, N)$. Let $M, R \ge 0$ and $\delta > 0$. Then there is $C$ such that for every admissible $\varphi$ of level $(M, R)$ and degree $N+1$, every $B$ with $|\varphi_\Lambda(x)| \le B$ for all $\Lambda \in V_n(M)$ and all $x$, and every $Z \in \mathcal{H}_{N+1}(\delta)$,
$$|D_\varphi(Z)|\, \Delta(Z)^{n/2} \le C B.$$

Lean: `GlobalTheory.SW.InvBound.bound_high`

*Proof.* If $M = 0$ or $R = 0$ there is no admissible family, and any $C$ works. Otherwise we use four results of the sources.

1. There is a common $R_0$ such that every $\varphi_\Lambda$, $\Lambda \in V_n(M)$, is a Schwartz-Bruhat function of level $R_0$ in a uniform sense.
2. For $4(N+1) < n$ the theta and Eisenstein series of a function of level $R_0$ bounded by $B$ converge, and are bounded by $C_1 B$ on $\mathcal{H}_{N+1}(\delta/4)$.
3. A *decay principle*: there is $C_2$ such that every function $f$ on $\mathcal{H}_{N+1}$ that is holomorphic, invariant under $Z \mapsto Z + 2R_0^2\, y$ for Hermitian integral $y$, bounded by $B'$ on $\mathcal{H}_{N+1}(\delta/4)$, and tends to $0$ along each ray $Z + i t\, v v^*$ ($t \to \infty$, $v \ne 0$), satisfies $|f(Z)| \Delta(Z)^{n/2} \le C_2 B'$ on $\mathcal{H}_{N+1}(\delta)$.
4. Along a ray $Z + i t\, v v^*$, the difference $D_\varphi$ tends to $0$. Its proof uses $\mathrm{SW}(n, N)$.

We apply the decay principle to $f = D_\varphi$. It is holomorphic: a result of the sources shows that $D_\varphi(Z, z, z')$ is holomorphic in all variables and solves the heat equation $2\pi i\, \partial_{Z_{ab}} D = \sum_k \partial_{z_{ka}} \partial_{z'_{kb}} D$ in each component $\tau$. It is invariant under the translations, since a translation by $2R_0^2 y$ multiplies $\varphi_\Lambda(x)$ by $e\big(\sum_\tau \tau(\operatorname{tr}(x \cdot 2R_0^2 y \cdot x^*))\big)$, which is $1$ on the support of $\varphi_\Lambda$. On $\mathcal{H}_{N+1}(\delta/4)$ each term of the class sum is bounded by $2 C_1 B$, so $|D_\varphi| \le C_3 B$ with $C_3 = 2C_1 \sum_c |\mathrm{Stab}(\Lambda_c)|^{-1}$. Item 4 gives the decay along rays. $\square$

### The bound on the whole half space

**Theorem 3.3.9 (Invariant bound).** Let $\Psi$ be a CM type, let $n$ be even with $4(N+1) < n$, and assume $\mathrm{SW}(n, N)$. For all $M, R$ there is $C$ such that for every admissible $\varphi$ of level $(M, R)$ and degree $N + 1$, every $B$ with $|\varphi_\Lambda| \le B$ on $V_n(M)$, and every $Z \in \mathcal{H}_{N+1}$,
$$|D_\varphi(Z)|\, \Delta(Z)^{n/2} \le C B.$$

Lean: `GlobalTheory.SW.swd_invariant_bound` (also `GlobalTheory.T.siegelWeil_difference_invariant_norm_bounded`, a second name)

*Proof.* Assume $M, R > 0$. A reduction theory result of the sources gives $c > 0$ and $\delta > 0$ such that for each $Z \in \mathcal{H}_{N+1}$ there is $\gamma \in U(N+1, N+1)$ with $c\gamma$ integral and $\gamma Z \in \mathcal{H}_{N+1}(\delta)$. For such $\gamma$, the Weil transforms $(\omega(\gamma)\varphi_\Lambda)_\Lambda$ form an admissible family of a level $(M, R')$ with $R'$ depending only on $c$ and $R$, and they are bounded by $C_1 B$ with $C_1$ depending only on $c$ and $R$. The difference has the automorphy
$$D_{\omega(\gamma)\varphi}(\gamma Z) = j(\gamma, Z, 0, 0)\, D_\varphi(Z),$$
by a result of the sources; for the theta series it is the definition of $\omega(\gamma)$. By the [previous lemma](/entry/bound-high/), applied to $\omega(\gamma)\varphi$ at $\gamma Z$,
$$|j(\gamma, Z, 0, 0)|\, |D_\varphi(Z)|\, \Delta(\gamma Z)^{n/2} \le C_2 C_1 B.$$
Now $|j(\gamma, Z, 0, 0)| = \big(\prod_\tau |\det(C_\tau Z_\tau + D_\tau)|^2\big)^{n/2}$ and $\Delta(\gamma Z) = \Delta(Z) \prod_\tau |\det(C_\tau Z_\tau + D_\tau)|^{-2}$. So the two factors cancel, and $C = C_2 C_1$ works. $\square$

### Twists by lattices

The induction step moves the test functions by Hecke operators, and these change the lattice $\mathcal{O}_E^{N}$ on the side of the degree. For an $\mathcal{O}_E$-submodule $\mathfrak{X} \subset E^N$ put
$$\iota(\mathfrak{X}) = \frac{[\mathfrak{X} : \mathfrak{X} \cap \mathcal{O}_E^N]}{[\mathcal{O}_E^N : \mathfrak{X} \cap \mathcal{O}_E^N]},$$
the generalized index of $\mathcal{O}_E^N$ in $\mathfrak{X}$, so that $\iota(\mathcal{O}_E^N) = 1$.

**Definition 3.3.10 (Twist).** Let $\varphi$ be a family and $R > 0$. The *twist* $\varphi^{\mathfrak{X}}$ of $\varphi$ by $\mathfrak{X}$ is the family with $\varphi^{\mathfrak{X}}_\Lambda(x) = \varphi_\Lambda(s x)$ if $R\, x\xi \in \Lambda$ for all $\xi \in \mathfrak{X}$ and there is $s \equiv 1 \bmod R^2$ with $s \mathcal{O}_E^N \subset \mathfrak{X}$ (we use a chosen such $s$), and $\varphi^{\mathfrak{X}}_\Lambda(x) = 0$ otherwise.

**Theorem 3.3.11 (Twisted bound).** Let $\Psi$ be a CM type, let $n$ be even with $4(N+1) < n$, assume $\mathrm{SW}(n, N)$, and let $\varphi$ be admissible of level $(M, R)$ and degree $N + 1$. Then there is $C$ such that for every finitely generated $\mathfrak{X} \subset E^{N+1}$ that agrees with $\mathcal{O}_E^{N+1}$ away from $RM$, and every $Z \in \mathcal{H}_{N+1}$,
$$\iota(\mathfrak{X})^{n/2}\, |D_{\varphi^{\mathfrak{X}}}(Z)|\, \Delta(Z)^{n/2} \le C.$$

Lean: `GlobalTheory.SW.twist_swd_bounded` (also `GlobalTheory.T.twisted_siegelWeil_difference_bounded`, a second name)

*Proof.* An admissible family is bounded, say by $B$, and so is each of its twists. A result of the sources gives $c > 0$ and $C_1$, independent of $\varphi$ and $\mathfrak{X}$, and for each $\mathfrak{X}$ an invertible $a \in M_{N+1}(E)$ with
$$\iota(\mathfrak{X}) \le C_1 |N_{E/\mathbb{Q}}(\det a)|$$
such that $x \mapsto \varphi^{\mathfrak{X}}_\Lambda(x a)$ is an admissible family of level $(M, Rc)$. A change of variables $x \mapsto x a$ in the theta and Eisenstein series gives, for each $Z \in \mathcal{H}_{N+1}$, a point $Z' \in \mathcal{H}_{N+1}$ with
$$D_{\varphi^{\mathfrak{X}}(\cdot\, a)}(Z') = D_{\varphi^{\mathfrak{X}}}(Z), \qquad \Delta(Z') = |N_{E/\mathbb{Q}}(\det a)|\, \Delta(Z).$$
The [invariant bound](/entry/swd-invariant-bound/) at level $(M, Rc)$ gives $C_2$ with
$$|D_{\varphi^{\mathfrak{X}}}(Z)|\, |N_{E/\mathbb{Q}}(\det a)|^{n/2}\, \Delta(Z)^{n/2} \le C_2 B.$$
Multiply by $\iota(\mathfrak{X})^{n/2} \le C_1^{n/2} |N_{E/\mathbb{Q}}(\det a)|^{n/2}$ and divide by the norm: $C = C_1^{n/2} C_2 B$ works. $\square$

**Remark 3.3.12 (Formalization).** The decay principle, the convergence bound, the reduction step, the heat equation for $D_\varphi$ and the limit along rays are results of the sources, cited in [SiegelWeilDifferenceInvariantNormBounded.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilDifferenceInvariantNormBounded.lean#L111). The Weil transform and the Eisenstein series are defined by choice; the Weil transform is $0$ when no transform exists. The lemma `detIm_nonneg` is proved twice, at line 162 of that file and at line 127 of TwistedSiegelWeilDifferenceBounded.lean. The second names are wrappers proved by `first | exact ...`. In the lemma, the case $M = 0$ or $R = 0$ is vacuous.
