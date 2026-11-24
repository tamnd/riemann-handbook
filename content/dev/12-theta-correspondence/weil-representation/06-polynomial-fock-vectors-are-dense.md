---
title: Polynomial Fock vectors are dense
decls:
  - GlobalTheory.PolDense.pol_dense
  - GlobalTheory.T.polynomialFock_dense_archimedeanSchwartz
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Polynomial Fock vectors are dense

This section proves that the space of polynomial Fock vectors is dense in the archimedean Schwartz space of a global unitary dual pair. The polynomial Fock vectors are the vectors obtained from the Gaussian vacuum vectors by repeated Heisenberg derivatives; in the [Fock model](/learn/theta/#the-fock-model) they are the polynomials. Density lets one pass from statements about the algebraic Fock space, such as [Howe duality](/entry/howe-duality-real-holds/), to statements about all Schwartz functions. It is used in [the existence of an algebraic vector with nonzero definite theta lift](/entry/exists-algebraic-vector-definite-theta-ne/): a continuous functional that is not zero on the Schwartz space is not zero on some polynomial Fock vector.

### The setting

Let $F$ be a number field and $E/F$ a quadratic extension with involution $\sigma$. Let $X$ be a Hermitian space of dimension $n$ and $W$ a skew-Hermitian space of dimension $d$ over $E$, with a model of the Weil representation $\omega$ of $\mathrm{U}(X) \times \mathrm{U}(W)$ on Schwartz functions of $(\mathbb{A}_F)^{n \times d}$, a standard additive character $\psi$ of $\mathbb{A}_F/F$, and embeddings $\tau_w$ of $E$ over each infinite place $w$. Write $F_\infty = F \otimes_{\mathbb{Q}} \mathbb{R}$ and let
$$V_\infty = F_\infty^{\,n \times d}, \qquad S_\infty = \mathcal{S}(V_\infty),$$
the space of [[Schwartz functions|GE020MY43M]] on the real vector space $V_\infty$, with its usual Fréchet topology.

For $u \in M_{n \times d}(\mathbb{A}_E)$ supported at the infinite places, the Heisenberg group element of $u$ acts on $S_\infty$, and $t \mapsto \omega(tu)$ for $t \in \mathbb{R}$ is a one-parameter group. Its derivative at $t = 0$ is the *Heisenberg derivative* $D_u$. In coordinates, for $u = (v, a)$ with $v, a \in V_\infty$,
$$D_u f(y) = \partial_v f(y) - 2\pi i\, \operatorname{tr}\langle y, a\rangle\, f(y),$$
where $\operatorname{tr}\langle y, a \rangle$ is the trace pairing on $V_\infty$.

**Definition 1.6.1 (Gaussian vacuum).** A vector $f_0 \in S_\infty$ is a *Gaussian vacuum* if there are signs $\varepsilon_w \in \{\pm 1\}$ such that for all $u$ supported at infinity, with $u'$ defined at each $w$ by $u'_w = \varepsilon_w\, i\, \theta_{X,w}\, u_w\, {}^t\theta_{W,w}$, one has $D_{u'} f_0 = i\, D_u f_0$.

Here $\theta_{X,w}$ and $\theta_{W,w}$ are the Cartan involutions at $w$. The condition says that $f_0$ is killed by the annihilation operators $D_{u'} - iD_u$, which defines the vacuum of the Fock model.

**Definition 1.6.2 (Polynomial Fock vectors).** The space $\mathcal{P}_\infty \subset S_\infty$ of *polynomial Fock vectors* is the smallest complex subspace that contains each Gaussian vacuum and is stable under each Heisenberg derivative $D_u$.

### The theorem

We use one fact from analysis, with a short proof.

**Lemma 1.6.3 (Gaussian density).** Let $V$ be a finite dimensional real vector space with a norm, and $N \subset \mathcal{S}(V)$ a complex subspace. Let $Q$ be a complex bilinear form on $V$ with $\operatorname{Re} Q(x,x) \geq c|x|^2$ for some $c > 0$, and suppose that $g(x) = e^{-Q(x,x)}$ lies in $N$. If $N$ is stable under each derivative $\partial_v$ and under multiplication by each real linear form $\ell$, then $N$ is dense in $\mathcal{S}(V)$.

*Proof.* By stability under multiplication, $N$ contains $p\,g$ for each polynomial $p$. Let $T$ be a tempered distribution with $T(p\,g) = 0$ for all $p$. The distribution $gT$ decays like $e^{-c|x|^2}$, so its [[Fourier transform|DPVM34ADZV]] is an entire function on $V \otimes \mathbb{C}$. Its derivatives at $0$ are the values $T(p\,g)$, up to constants, so they all vanish, and the Fourier transform of $gT$ is $0$. So $gT = 0$. For a test function $\phi$ with compact support, $\phi / g$ is again such a function, so $T(\phi) = (gT)(\phi/g) = 0$. Test functions with compact support are dense in $\mathcal{S}(V)$, so $T = 0$. By the Hahn-Banach theorem the closure of $N$ is $\mathcal{S}(V)$. $\square$

For $Q$ real and positive definite this is the density of the Hermite functions; see M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (1980), Theorem V.13. The argument above does not use the stability under derivatives.

**Theorem 1.6.4 (Density of polynomial Fock vectors).** Let $(X, W)$ be a unitary dual pair with a model of the Weil representation as above, and with the base data of a standard additive character and of the embeddings $\tau_w$. Then $\mathcal{P}_\infty$ is dense in $S_\infty$.

Lean: `GlobalTheory.PolDense.pol_dense` (also `GlobalTheory.T.polynomialFock_dense_archimedeanSchwartz`, a second name).

*Proof.* There is a Gaussian vacuum $g \in S_\infty$ of the form $g(x) = e^{-Q(x,x)}$, where $Q$ is a complex bilinear form on $V_\infty$ with $\operatorname{Re} Q(x,x) \geq c|x|^2$ for some $c > 0$. This is the classical vacuum vector: at each infinite place it is $e^{-\pi \operatorname{tr}(x^* \theta x \theta')}$ for the Cartan involutions, and its real part is positive definite since the forms are nondegenerate. So $g \in \mathcal{P}_\infty$.

The space $\mathcal{P}_\infty$ is stable under each operator $f \mapsto \partial_v f - 2\pi i \operatorname{tr}\langle\cdot, a\rangle f$, since this is $D_u$ for $u = (v, a)$. Taking $a = 0$ gives stability under $\partial_v$. Taking $v = 0$ gives stability under multiplication by $-2\pi i\operatorname{tr}\langle\cdot, a\rangle$, and so under multiplication by $\operatorname{tr}\langle \cdot, a\rangle$, since $-2\pi i \neq 0$. The trace pairing on $V_\infty$ is nondegenerate, so each real linear form $\ell$ on $V_\infty$ is $\operatorname{tr}\langle\cdot, a\rangle$ for some $a$. The lemma on Gaussian density, with $N = \mathcal{P}_\infty$, gives the claim. $\square$

**Example 1.6.5.** Let $F = \mathbb{Q}$, $n = d = 1$, and let the archimedean space be $\mathbb{C} = \mathbb{R}^2$ with $Q(x, x) = \pi|x|^2$. Then the vacuum is $e^{-\pi|x|^2}$, and $\mathcal{P}_\infty$ is the space of $p(x, \bar x)\, e^{-\pi |x|^2}$ with $p$ a polynomial. These functions span the Hermite functions of two variables, and they are dense in $\mathcal{S}(\mathbb{R}^2)$.

**Remark 1.6.6.** The theorem is the topological link between the two models of the [Weil representation](/learn/theta/#the-weil-representation) at infinity: the Fock model is the space $\mathcal{P}_\infty$ with the Lie algebra action, and the Schrödinger model is its completion $S_\infty$. A continuous linear map on $S_\infty$ is fixed by its values on $\mathcal{P}_\infty$.

**Remark 1.6.7 (Formalization).** The theorem is `GlobalTheory.PolDense.pol_dense` (PolynomialFockDenseArchimedeanSchwartz.lean, line 42). The space $\mathcal{P}_\infty$ is `Model.Pol` and the vacuum condition is `Model.IsGauss` (BlockTheory/DivisorBase/WeilTensorModels.lean, lines 253 and 247). The stability step is `pol_stable` (line 29 of the same file as the theorem), which rewrites the Heisenberg derivative in coordinates through `exists_heisLine_actsD_eq`. The Gaussian vacuum comes from `exists_gaussVacuum_nondegenerate_gaussian_dualPair`, and the lemma on Gaussian density is `schwartzSubmodule_eq_top_of_gaussian_mem_derivStable`, a wrapper of `GlobalTheory.SchwartzGaussDense.dense_of_gaussian_mem`; we have not opened these two proofs, so the proofs of the lemma and of the existence of $g$ above are ours. Of the hypothesis `IsPair`, the proof uses only the standard character (`hP.base.std`, line 46) directly, and passes the whole hypothesis to the vacuum lemma. The Lean lemma asks for stability under derivatives, which our proof of it does not need. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (PolynomialFockDenseArchimedeanSchwartzStatement.lean, line 8).
