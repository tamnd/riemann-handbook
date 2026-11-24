---
title: The coefficient as an Euler product integral
decls:
  - GlobalTheory.CompanionTheory.WhitFree.pure_identity
  - GlobalTheory.CompanionTheory.WhitFree.coefN_eq_integral
  - GlobalTheory.CompanionTheory.WhitFree.whit_eq_integral
  - GlobalTheory.T.block_coefficient_local_global_factor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The coefficient as an Euler product integral

The Fourier coefficient of a Siegel Eisenstein series at a Hermitian matrix $T$ is a Whittaker integral: a double Fourier transform of a Schwartz function along the Gram map. This section proves that this Whittaker integral equals the integral of the Schwartz function against any Euler product measure with constant 1 at $T$, as defined in [the singular case](/entry/sw-free-singular/). The proof goes from pure functions to all Schwartz-Bruhat functions and then to the form of the coefficient that the next section uses. With the measure form of the Siegel-Weil formula, this gives the convergent formula for frames in [the theorem on frames](/entry/siegel-frame/).

We keep the setting of the previous sections. Let $\psi$ be a character of $\mathbb{A}$. We call $\psi$ a standard character if it is continuous, has absolute value 1, is trivial on $F$, and is not trivial. For an adelic Hermitian matrix $b$ and an adelic tuple $X$ we write
$$\langle b, X \rangle = \tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}\bigl(b \operatorname{gr}(X)\bigr),$$
where the trace $\operatorname{Tr}_{E/F}$ is the trace of $\mathbb{A}_E = \mathbb{A} \otimes_F E$ over $\mathbb{A}$, see [Fourier coefficients](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions).

**Definition 4.3.1 (Whittaker integral).** Let $dx$ be a measure on adelic $n$-tuples in $\mathbb{A}_E^M$ and $db$ a measure on adelic Hermitian $n \times n$ matrices. For a function $\Phi$ on adelic tuples, put
$$\Phi^\ast(b) = \int \Phi(X) \, \psi(\langle b, X \rangle) \, dx.$$
For a Hermitian matrix $T$ over $E$, the Whittaker integral of $\Phi$ at $T$ is
$$W_T(\Phi) = \int \Phi^\ast(b) \, \psi\bigl(-\tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}(T b)\bigr) \, db.$$

So $\Phi^\ast$ is the integral of $\Phi$ against the character of the Gram map, and $W_T$ is its Fourier transform at $T$. Formally $W_T(\Phi)$ is the integral of $\Phi$ over the fibre $\operatorname{gr}^{-1}(T)$. The theorems below make this precise.

**Definition 4.3.2 (Self-dual measures).** The measure $dx$ is self-dual if it is self-dual for the pairing $\psi(B(X, Y))$, where $B(X, Y) = \tfrac12 \operatorname{Tr}_{E/F}\sum_a h_J(x_a, y_a)$ up to the symmetrisation fixed by the trace form. The measure $db$ is self-dual if it is self-dual for the pairing $\psi(\tfrac12 \operatorname{Tr}_{E/F}\operatorname{tr}(S T))$ on Hermitian matrices. See [the Fourier transform](/learn/analysis/#the-fourier-transform).

**Definition 4.3.3 (Schwartz-Bruhat functions).** A function $\varphi$ on archimedean tuples is Schwartz if it is a [[Schwartz function|GE020MY43M]] in real coordinates: there is an additive homeomorphism with some $\mathbb{R}^N$ that carries $\varphi$ to an element of $\mathcal{S}(\mathbb{R}^N)$. A function $\Phi$ on adelic tuples is Schwartz-Bruhat if it is a finite sum $\sum_i \Phi_{\infty,i}(X_\infty) \Phi_{f,i}(X_f)$ with each $\Phi_{\infty,i}$ Schwartz and each $\Phi_{f,i}$ a Schwartz-Bruhat function on the finite adeles.

For a Schwartz function $\varphi$ and compact open sets $A_v$ of tuples at the finite places, with $A_v = L_v$ for almost all $v$, the pure function is
$$\Phi_{\varphi, A}(X) = \varphi(X_\infty) \cdot \mathbf{1}[X_v \in A_v \text{ for all } v].$$

**Proposition 4.3.4 (Pure functions).** Let $E/F$ be CM and $J$ Hermitian and nondegenerate of size $M$. Let $0 < n$ with $2n < M$, let $\psi$ be a standard character, and let $dx$ and $db$ be self-dual. Let $b$ be a basis of $E/F$, $(\lambda_\infty, \lambda_v)$ a standard system, and $m_\infty$, $m_v$ free Gram fibre families in rank $n$ for the coordinate measures. Let $T$ be Hermitian of size $n$, and let $I$ be the Euler product of $(m_\infty(T), m_v(T))$ with constant 1. Let $\varphi$ be Schwartz, and let $A_v$ be compact open sets with $A_v = L_v$ for $v$ outside a finite set $S_0$. Then $\Phi_{\varphi, A}$ is $I$-integrable and
$$W_T(\Phi_{\varphi, A}) = \int \Phi_{\varphi, A} \, dI.$$

Lean: `GlobalTheory.CompanionTheory.WhitFree.pure_identity`.

*Proof.* Choose a finite set $S$ of places that contains $S_0$, the set beyond which $I$ is standard, and the set beyond which the coefficient factors. For such $S$ the Whittaker integral of a function that is standard outside $S$ is the limit of finite products: the coefficient at $T$ of $\Phi_{\varphi, A}$, truncated to $S$, equals
$$c_S = \int \varphi \, dm_\infty(T) \prod_{v \in S} m_v(T)(A_v)$$
times the product of the local unramified factors $m_v(T)(L_v)$ over the places of a finite set outside $S$. This uses three local facts. At the archimedean place the fibre measure $m_\infty(T)$ integrates a Schwartz function to the archimedean Whittaker integral, and $\varphi$ is integrable for it. At each finite place the fibre measure of $A_v$ is the local Whittaker integral of its indicator, and at an unramified place the local integral of $\mathbf{1}_{L_v}$ is $m_v(T)(L_v)$. In the convergent range $2n < M$ the function $\Phi^\ast$ is integrable, so $W_T$ is the limit of its truncations as the finite set grows. The tail product $\prod_{v \notin S'} m_v(T)(L_v)$ tends to 1 since $\sum_v |m_v(T)(L_v) - 1|$ converges. Condition 3 of the Euler product computes $\int \Phi_{\varphi, A} \, dI$ as the same product with the full tail. The two limits agree, and limits are unique. Integrability follows from the same factorization applied to $|\varphi|$. $\square$

**Theorem 4.3.5 (Whittaker integral of a Schwartz-Bruhat function).** In the setting of the proposition on pure functions, let $\Phi$ be a Schwartz-Bruhat function. Then
$$W_T(\Phi) = \int \Phi \, dI.$$

Lean: `GlobalTheory.CompanionTheory.WhitFree.coefN_eq_integral`.

*Proof.* A Schwartz-Bruhat function on the finite adeles is a finite linear combination of indicators of products $\prod_v A_v$ of compact open sets with $A_v = L_v$ for almost all $v$. So $\Phi$ is a finite linear combination of pure functions. Both sides of the formula are linear in $\Phi$, and each pure function is integrable for $I$ by [the proposition on pure functions](/entry/pure-identity/), which also gives the formula for each pure term. $\square$

The next form of the theorem uses the notation of the convergent Siegel-Weil formula. A Hermitian space $V$ of rank $m$ over $E$ is $E^m$ with a nondegenerate Hermitian Gram matrix. For $r \ge 1$ let $\mathrm{Mat}_{m \times r}(\mathbb{A}_E)$ carry a measure $\mu$, and let the adelic Hermitian $r \times r$ matrices carry a measure $\lambda$. For an $m \times r$ matrix $y$ write $\langle y, y \rangle = {}^t y^\sigma G_V y$.

**Definition 4.3.6 (Convergent coefficient).** For $\varphi$ on $\mathrm{Mat}_{m \times r}(\mathbb{A}_E)$ and an adelic Hermitian $b$ put
$$J_\varphi(b) = \int \varphi(y) \, \psi\bigl(\tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}(b \langle y, y \rangle)\bigr) \, d\mu(y),$$
and for a rational Hermitian $\beta$,
$$W_\beta(\varphi) = \int J_\varphi(b) \, \psi\bigl(-\tfrac12 \operatorname{Tr}_{E/F} \operatorname{tr}(\beta b)\bigr) \, d\lambda(b).$$

**Definition 4.3.7 (Convergent hypotheses).** We say that the convergent hypotheses hold for $(r, V, \psi, \mu, \lambda, \nu, \varphi)$ if: $2r < m$; $\psi$ is a standard character; the archimedean data are fixed; $\mu$ is a Haar measure of covolume 1 for the rational matrices; $\lambda$ is an additive Haar measure with a fundamental domain for the rational Hermitian matrices of measure 1; $\nu$ is a Haar measure on $U_V(\mathbb{A})$; $\varphi$ is an adelic Schwartz function of the given archimedean type; and the absolute theta integral $\int_{[U_V]} \sum_x |\varphi(h^{-1} x)| \, dh$ is finite.

A Hermitian matrix is in block normal form of rank $t$ if it is in block form of rank $t$ as in the [block case](/entry/sw-free-block/).

**Theorem 4.3.8 (Whittaker integral as an Euler product integral).** Assume the convergent hypotheses for $(r, V, \psi, \mu, \lambda, \nu, \varphi)$. Let $\beta$ be a rational Hermitian matrix in block normal form of some rank $t$. Let $b$ be a basis of $E/F$, $(\lambda_\infty, \lambda_v)$ a standard system, $m_\infty$, $m_v$ free Gram fibre families for $V$ in rank $r$, and $I$ the Euler product of $(m_\infty(\beta), m_v(\beta))$ with constant 1. If $X \mapsto \varphi({}^t X)$ is $I$-integrable, then
$$W_\beta(\varphi) = \int \varphi({}^t X) \, dI(X).$$

Lean: `GlobalTheory.CompanionTheory.WhitFree.whit_eq_integral` (also `GlobalTheory.T.block_coefficient_local_global_factor`, a second name).

*Proof.* The Gram matrix of $V$ is Hermitian and nondegenerate, and $E/F$ is CM. The block normal form gives $t < r$, so $r > 0$. There are self-dual measures $dx$ and $db$ such that $W_\beta(\varphi)$ equals the Whittaker integral $W_\beta$ of $X \mapsto \varphi({}^t X)$ for these measures; this is the comparison of the covolume one measures $\mu$ and $\lambda$ with the self-dual ones. An adelic Schwartz function of the given type is Schwartz-Bruhat. Now apply [the theorem on Schwartz-Bruhat functions](/entry/coef-n-eq-integral/). $\square$

**Remark 4.3.9 (Formalization).** The last theorem never uses its integrability hypothesis, which is left unnamed. It uses the block normal form only for $t < r$, and it discards the Haar measure $\nu$ and the finiteness of the absolute theta integral ([BlockCoefficientLocalGlobalFactor.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/BlockCoefficientLocalGlobalFactor.lean#L118)). So the theorem holds for each $\beta$ of size $r \ge 1$. The second name is stated with `first | exact`, and its name speaks of a block coefficient, though the statement is the Whittaker integral identity. The adelic Schwartz space of the given archimedean type and the self-dual pairing on tuples are not unfolded here.
