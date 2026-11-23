---
title: Archimedean Siegel-Weil integrals
decls:
  - GlobalTheory.CompanionTheory.SiegelND.Integ.Arch.core_integrable
  - GlobalTheory.CompanionTheory.SiegelND.Integ.Arch.integrable_starLoc_inf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Archimedean Siegel-Weil integrals

The Siegel-Weil formula compares a theta integral with an Eisenstein series. On the Eisenstein side, each Fourier coefficient is a product of local integrals. The archimedean factor is the Fourier transform, on the space of Hermitian matrices, of the push forward of a Schwartz function under the moment map $X \mapsto$ (Gram matrix of $X$). This section proves that this archimedean factor is an integrable function of the Hermitian matrix, under Weil's condition $M > 2n$ that relates the size $M$ of the Hermitian space to the size $n$ of the matrices. Integrability means that the push forward has a continuous density, by Fourier inversion. It is used to bound the archimedean density of the Gram map on compact sets, in the convergent range of the Siegel-Weil formula. The background is in [the Weil representation](/learn/theta/#the-weil-representation), [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms) and [the Fourier transform](/learn/analysis/#the-fourier-transform).

### The integral in complex coordinates

Let $W$ be a finite set, the set of archimedean places. Fix $M, n \ge 1$ and, for each $w \in W$, a Hermitian matrix $J_w \in M_M(\mathbb{C})$ with $\det J_w \neq 0$. For $X \in M_{n \times M}(\mathbb{C})$, with rows $X_1, \dots, X_n$, the Gram matrix is the Hermitian $n \times n$ matrix
$$\operatorname{gram}_{J}(X)_{ac} = \sum_{i,j} \overline{X_{ai}}\, J_{ij}\, X_{cj}.$$
Let $\mathcal{H}_n$ be the real vector space of Hermitian $n \times n$ complex matrices.

**Definition 3.7.1 (Archimedean core integral).** Let $\mu$ be a Haar measure on $\prod_{w \in W} M_{n\times M}(\mathbb{C})$ and $g$ an integrable function there. For $b = (b_w) \in \mathcal{H}_n^W$ put
$$\operatorname{core}(g)(b) = \int g(X) \exp\Bigl( 2\pi i \sum_{w \in W} \operatorname{Re} \operatorname{tr}\bigl( b_w \operatorname{gram}_{J_w}(X_w) \bigr) \Bigr) \, d\mu(X).$$

Up to the identification of $\mathcal{H}_n^W$ with its dual by the trace form, $\operatorname{core}(g)$ is the Fourier transform of the push forward of $g\,\mu$ under $X \mapsto (\operatorname{gram}_{J_w}(X_w))_w$.

We say that $g$ is Schwartz if $g = f \circ e$ for a Schwartz function $f$ on $\mathbb{R}^N$ and an additive homeomorphism $e$ from $\prod_w M_{n \times M}(\mathbb{C})$ to $\mathbb{R}^N$.

For a Hermitian matrix $b$ write $\Delta(b) = \det(1 + b^2)$. It is real and at least $1$, since the eigenvalues of $1 + b^2$ are $1 + \beta^2$ for the real eigenvalues $\beta$ of $b$.

We use three facts, taken as given.

- (Hua bound.) If $g$ is Schwartz, there is $C$ with
$$|\operatorname{core}(g)(b)| \le C \prod_{w \in W} \Delta(b_w)^{-M/2} \qquad \text{for all } b.$$
- (Continuity.) If $g$ is Schwartz, $\operatorname{core}(g)$ is continuous.
- (Hua integral.) For every Haar measure $\nu$ on $\mathcal{H}_n^W$ and every real $s > n - \tfrac12$, the function $b \mapsto \prod_w \Delta(b_w)^{-s}$ is integrable.

The Hua bound is the statement for a Gaussian, $g(X) = \exp(-\pi \sum_w \operatorname{tr} X_w X_w^*)$, extended to all Schwartz functions. For a Gaussian the integral is a product of one dimensional Gaussian integrals after diagonalizing $J_w$ and $b_w$, and each entry contributes a factor $(1 - 2i\alpha\beta)^{-1}$ for an eigenvalue $\beta$ of $b_w$ and an eigenvalue $\alpha$ of $J_w$. Since every $\alpha$ is nonzero, the product over the $M$ eigenvalues of $J_w$ is at most a constant times $(1 + \beta^2)^{-M/2}$ in absolute value. The Hua integral is a classical computation of L. K. Hua on the space of Hermitian matrices.

**Theorem 3.7.2 (Integrability of the core integral).** Let $W$ be finite, $2n < M$, and $J_w \in M_M(\mathbb{C})$ Hermitian with $\det J_w \neq 0$ for each $w$. Let $g$ be Schwartz, $\mu$ a Haar measure on $\prod_w M_{n \times M}(\mathbb{C})$ and $\nu$ a Haar measure on $\mathcal{H}_n^W$. Then $\operatorname{core}(g)$ is $\nu$-integrable.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.Arch.core_integrable`.

*Proof.* Put $s = M/2$. From $2n < M$ we get $2n + 1 \le M$, so $s \ge n + \tfrac12 > n - \tfrac12$. By the Hua integral, $C \prod_w \Delta(b_w)^{-M/2}$ is integrable. By the Hua bound it dominates $|\operatorname{core}(g)|$. By continuity, $\operatorname{core}(g)$ is measurable. So $\operatorname{core}(g)$ is integrable. $\square$

The condition $2n < M$ is stronger than the condition $s > n - \tfrac12$ needs, which is $M > 2n - 1$. The integer form $2n < M$ is the usual form of Weil's condition for absolute convergence.

### The adelic form

Now let $E/F$ be a CM extension, $J \in M_M(E)$ Hermitian and nondegenerate, and $\mathbb{A}_\infty = F \otimes \mathbb{R}$. Let $\mathcal{H}_n(\mathbb{A}_\infty)$ be the space of Hermitian $n \times n$ matrices over $\mathbb{A}_\infty \otimes_F E$. Let $\psi$ be a nontrivial character of $\mathbb{A}_F$ trivial on $F$ and $\psi_\infty$ its archimedean component.

**Definition 3.7.3 (Local Siegel-Weil integral at infinity).** For a Haar measure $\mu$ on $M_{n \times M}(\mathbb{A}_\infty \otimes E)$, a Schwartz function $P$ there and $b \in \mathcal{H}_n(\mathbb{A}_\infty)$, put
$$W_\infty(P)(b) = \int P(X)\, \psi_\infty\Bigl( \tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}\bigl( b \operatorname{gram}_J(X) \bigr) \Bigr)\, d\mu(X).$$

The function $P$ is Schwartz in the same sense as above, through an additive homeomorphism with some $\mathbb{R}^N$.

We use the following facts about coordinates, taken as given.

- (Archimedean character.) Identify $\mathbb{A}_\infty$ with $\mathbb{R}^W$ through the real places $\rho_w$ of $F$. There is $a \in F^\times$ with $\psi_\infty(x) = \exp\bigl(2\pi i \sum_w \rho_w(a x)\bigr)$.
- (Complex coordinates.) For each $w$ choose a complex embedding $\tau_w$ of $E$ above $\rho_w$. It gives an isomorphism $\mathbb{A}_\infty \otimes_F E \cong \mathbb{C}^W$, under which $\sigma$ becomes complex conjugation. It induces linear homeomorphisms $\Psi$ from $\mathcal{H}_n(\mathbb{A}_\infty)$ to $\mathcal{H}_n^W$ and $\Phi$ from $M_{n \times M}(\mathbb{A}_\infty \otimes E)$ to $\prod_w M_{n\times M}(\mathbb{C})$. These maps carry Haar measures to Haar measures and preserve integrability and integrals.
- (Character in coordinates.) Under these maps, the phase $\psi_\infty(\tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}(b \operatorname{gram}_J(X)))$ is the phase of the core integral for the matrices $J_w = \rho_w(a)\, \tau_w(J)$.

The factor $\tfrac12 \operatorname{Tr}_{E/F}$ becomes the real part, since $\tfrac12 \operatorname{Tr}_{\mathbb{C}/\mathbb{R}}(z) = \operatorname{Re} z$.

**Theorem 3.7.4 (Integrability at infinity).** Let $E/F$ be a CM extension, $J \in M_M(E)$ Hermitian and nondegenerate, and $2n < M$. Let $\psi$ be a character of $\mathbb{A}_F$ as above, $\mu$ a Haar measure on $M_{n \times M}(\mathbb{A}_\infty \otimes E)$, $\nu$ a Haar measure on $\mathcal{H}_n(\mathbb{A}_\infty)$, and $P$ a Schwartz function. Then $W_\infty(P)$ is $\nu$-integrable.

Lean: `GlobalTheory.CompanionTheory.SiegelND.Integ.Arch.integrable_starLoc_inf`.

*Proof.* Take $a$, $\tau_w$, $\Psi$ and $\Phi$ as in the facts. Put $J_w = \rho_w(a) \tau_w(J)$. Each $J_w$ is Hermitian: $\rho_w(a)$ is real, and $\tau_w(\overline{J_{ji}}) = \overline{\tau_w(J_{ji})}$ because $\tau_w$ turns $\sigma$ into complex conjugation. Each $J_w$ is invertible, since $\det J_w = \rho_w(a)^M \tau_w(\det J)$ and both factors are nonzero.

Write $P = f \circ e_0$ with $f$ Schwartz on $\mathbb{R}^N$, and put $e_2 = e_0 \circ \Phi^{-1}$, an additive homeomorphism. Then $g = f \circ e_2$ is Schwartz on $\prod_w M_{n\times M}(\mathbb{C})$, and $g \circ \Phi = P$. By the [theorem above](/entry/core-integrable/) applied to $J_w$, $g$, $\Phi_*\mu$ and $\Psi_*\nu$, the function $\operatorname{core}(g)$ is $\Psi_*\nu$-integrable. So $\operatorname{core}(g) \circ \Psi$ is $\nu$-integrable.

It remains to see that $\operatorname{core}(g)(\Psi b) = W_\infty(P)(b)$. Change variables $X \mapsto \Phi X$ in the core integral. The integrand becomes $f(e_0(X))$ times the phase of the core integral at $(\Phi X, \Psi b)$. The first factor is $P(X)$. By the fact on the character in coordinates, the second is $\psi_\infty(\tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}(b \operatorname{gram}_J(X)))$. $\square$

**Example 3.7.5.** Let $F = \mathbb{Q}$, $n = 1$ and $J = 1_M$. Then $\mathcal{H}_1 = \mathbb{R}$, the Gram matrix of a row $X$ is $|X|^2$, and for the Gaussian $P(X) = e^{-\pi |X|^2}$ on $\mathbb{C}^M$,
$$W_\infty(P)(b) = \int_{\mathbb{C}^M} e^{-\pi |X|^2 (1 - 2i b)}\, dX = (1 - 2i b)^{-M}$$
for $\psi_\infty(x) = e^{2\pi i x}$ and Lebesgue measure on $\mathbb{C}^M = \mathbb{R}^{2M}$. Here $\tfrac12 \operatorname{Tr}_{E/F}(b|X|^2) = b|X|^2$. The absolute value is $(1 + 4b^2)^{-M/2} \le (1 + b^2)^{-M/2}$, which is the Hua bound with $C = 1$. It is integrable on $\mathbb{R}$ exactly when $M > 1$, in accordance with $2n < M$.

**Remark 3.7.6 (Formalization).** The three facts before the first theorem are the statements `GlobalTheory.T.archimedean_orbital_integral_hua_bound`, `archimedean_orbital_integral_continuous` and `product_hua_determinant_integrable`. The weight is written as the real part of $\det(1 + b\,b)$. The coordinate facts are `infinite_adele_haar_map_eq_scaled_volume`, `adelic_character_archimedean_form`, `complex_coordinates_exist_at_infinity`, `hermitian_archimedean_complex_coordinates`, `tuple_archimedean_complex_coordinates` and `archimedean_character_in_coordinates`. Two components of the Haar measure statement and three components of the character statement are discarded with `-` at lines 50 and 51 of [ArchimedeanSiegelWeilIntegralIdentity.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArchimedeanSiegelWeilIntegralIdentity.lean#L42). The core theorem is at line 26 of the same file. The second theorem is also stated as `GlobalTheory.T.archimedean_siegel_weil_integral_identity`; despite the name, that statement asserts integrability, not an identity.
