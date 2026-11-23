---
title: Hyodo's theorem for semistable representations
decls:
  - GlobalTheory.T.hyodo_statement
  - GlobalTheory.PMon.hyodo
  - GlobalTheory.T.hyodo_theorem_matrix_unramifiedCoefficients
  - GlobalTheory.PMon.hyodo_mat
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hyodo's theorem for semistable representations

This section proves that an extension of semistable representations that is de Rham is itself semistable, in the form of a statement about cocycles. Let $V$ be a semistable representation of $G_K$ and $c$ a continuous cocycle with values in $V$. If $c$ becomes a coboundary in $V \otimes B_{\mathrm{dR}}$, then it already becomes a coboundary in $V \otimes B_{\mathrm{st}}$. In the language of Bloch and Kato this says $H^1_g(K, V) = H^1_{\mathrm{st}}(K, V)$. We then prove a matrix form with coefficients in $\mathbb{Q}_\ell^{\mathrm{ur}}$, by restriction of scalars. The matrix form is the input of [the extension step](/entry/de-rham-extension-potentially-semistable/) of the next section.

We keep the notation of sections 15 and 21: tied local period data at $\ell$, the rings $B$, $B_{\mathrm{dR}}$ and $B_{\mathrm{st}} = B[X]$, the Frobenius $\varphi$ of $B$, the field $\mathbb{Q}_\ell^{\mathrm{ur}}$ with its Frobenius $\sigma$, and $r$-rational representations. For background see [de Rham representations](/learn/padic-hodge/#de-rham-representations), [semistable representations](/learn/padic-hodge/#crystalline-and-semistable-representations) and [local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory). Let $V$ be a finite-dimensional $\mathbb{Q}_\ell$-vector space with a continuous representation $\rho$ of $G_K$, and write $Z^1(V)$ for the space of continuous cocycles $c : G_K \to V$, as in [the previous section](/entry/finite-and-finrank-h1-v/). Write $D_{\mathrm{cris}}(V) = (V \otimes B)^{G_K}$.

**Definition 6.24.1 (Bloch-Kato cocycles).** Let $c \in Z^1(V)$.

1. $c$ is *geometric* if there is $b \in V \otimes B_{\mathrm{dR}}$ with $c(g) \otimes 1 = g(b) - b$ for all $g \in G_K$.
2. $c$ is *finite* if there is $x \in V \otimes B$ with $c(g) \otimes 1 = g(x) - x$ for all $g$.
3. $c$ is *exponential* if there is $x \in V \otimes B$ with $\varphi(x) = x$ and $c(g) \otimes 1 = g(x) - x$ for all $g$.

The geometric, finite and exponential cocycles form subspaces $Z^1_g(V)$, $Z^1_f(V)$ and $Z^1_e(V)$ of $Z^1(V)$.

Lean: `GlobalTheory.HyodoDef.geometricCocycles` (also `Formalism.WeaklyAdmissibleFiltrations.finiteCocycles`, the finite cocycles, and `GlobalTheory.HyodoDef.crystallineCocycles`, the exponential cocycles).

Here $g$ acts on $V \otimes B$ by $\rho(g) \otimes g$, and $\varphi$ acts on the second factor. Each of these spaces contains the coboundaries, and its image in $H^1(V)$ is the space $H^1_g$, $H^1_f$ or $H^1_e$ of Bloch and Kato, since $B$ is identified with $B_{\mathrm{cris}}$. We work with the cocycle spaces themselves.

### The statement

**Theorem 6.24.2 (Hyodo's theorem).** Let $\ell$ be a prime, with local period data tied to their $A_{\inf}$ data. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $V$ a finite-dimensional $\mathbb{Q}_\ell$-vector space with its module topology, and $\rho$ a representation of $G_K$ on $V$ with $g \mapsto \rho(g)v$ continuous for each $v$. Assume that $\rho$ is semistable. Let $c : G_K \to V$ be continuous with $c(gh) = c(g) + \rho(g) c(h)$, and assume that there is $b \in V \otimes B_{\mathrm{dR}}$ with $c(g) \otimes 1 = g(b) - b$ for all $g \in G_K$. Then there is $b' \in V \otimes B_{\mathrm{st}}$ with $c(g) \otimes 1 = g(b') - b'$ for all $g \in G_K$.

Lean: `GlobalTheory.T.hyodo_statement` (also `GlobalTheory.PMon.hyodo`, the proof).

Hyodo expected this for de Rham $V$, and Berger deduced it from the $p$-adic monodromy theorem. Here $V$ is semistable, and the proof is a count of dimensions.

### Inputs

We use the following facts, proved elsewhere in this development. In each, $V$ and $\rho$ are as in the Theorem.

1. (Tate dual.) There are a continuous representation $\rho'$ of $G_K$ on $V' = \mathbb{Q}_\ell^d$, $d = \dim V$, and a perfect duality $P : V \times V' \to \mathbb{Q}_\ell$ into $\mathbb{Q}_\ell(1)$, in the sense of [the previous section](/entry/finite-and-finrank-h1-v/).
2. (Semistable implies de Rham.) If $\rho$ is semistable, it is de Rham.
3. (Duality of de Rham representations.) If $V$ is de Rham and $V'$ is in perfect duality with $V$ into $\mathbb{Q}_\ell(1)$, then $V'$ is de Rham.
4. (Finiteness.) $Z^1(V)$ is finite-dimensional. This follows from [the Euler characteristic formula](/entry/finite-and-finrank-h1-v/).
5. (Semistable cocycles.) Let $\rho$ be semistable, $V'$ as in 1, and $Z^1(V)$ finite-dimensional. Then there is a subspace $S$ with $Z^1_f(V) \subseteq S \subseteq Z^1(V)$, such that every $c \in S$ becomes a coboundary in $V \otimes B_{\mathrm{st}}$ and in $V \otimes B_{\mathrm{dR}}$, and
$$\dim Z^1_f(V) + \dim D_{\mathrm{cris}}(V')^{\varphi = 1} \leq \dim S.$$
6. (Duality of Bloch-Kato spaces.) If $V$ and $V'$ are de Rham and in perfect duality into $\mathbb{Q}_\ell(1)$, then
$$\dim Z^1_g(V) + \dim Z^1_e(V') \leq \dim Z^1_f(V) + \dim Z^1_f(V').$$
7. (Finite against exponential.) If $V'$ is de Rham, then
$$\dim Z^1_f(V') \leq \dim Z^1_e(V') + \dim D_{\mathrm{cris}}(V')^{\varphi = 1}.$$

Facts 6 and 7 are the cocycle forms of results of Bloch and Kato: $H^1_f(V)$ and $H^1_f(V')$ are exact annihilators under the cup product, as are $H^1_g(V)$ and $H^1_e(V')$, and $H^1_f / H^1_e$ has dimension $\dim D_{\mathrm{cris}}^{\varphi = 1}$ (S. Bloch and K. Kato, Proposition 3.8 and Corollary 3.8.4).

*Proof of the Theorem.* Take $V'$ and $P$ by fact 1. By fact 2, $V$ is de Rham, and by fact 3, $V'$ is de Rham. By fact 4, $Z^1(V)$ is finite-dimensional, so fact 5 gives $S$. Every $c \in S$ is geometric, so $S \subseteq Z^1_g(V)$, and $Z^1_g(V)$ is finite-dimensional. Facts 6, 7 and 5 give
$$\begin{aligned} \dim Z^1_g(V) &\leq \dim Z^1_f(V) + \dim Z^1_f(V') - \dim Z^1_e(V') \\ &\leq \dim Z^1_f(V) + \dim D_{\mathrm{cris}}(V')^{\varphi = 1} \\ &\leq \dim S. \end{aligned}$$
So $S = Z^1_g(V)$. The cocycle $c$ of the Theorem is geometric, so $c \in S$, and $c$ becomes a coboundary in $V \otimes B_{\mathrm{st}}$. $\square$

### The matrix form

In the matrix form the coefficients lie in $\mathbb{Q}_\ell^{\mathrm{ur}}$. To avoid a clash with the Frobenius $\sigma$, we write $\tau : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ for the representation. As in section 21, $\tau_m(g) = \sigma^m(\tau(g))$ with entries in $B_{\mathrm{dR}}$, and $g(b)$ is the Galois action on the entries of a vector $b$.

**Theorem 6.24.3 (Hyodo's theorem, matrix form).** Let $\ell$ be a prime, with tied local period data. Let $n$ be a finite set, $K$ a finite extension of $\mathbb{Q}_\ell$, $r \geq 0$, and $\tau : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ an $r$-rational homomorphism. Assume:

1. there is $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ with $\tau(g)\, g(Q) = Q$ for all $g \in G_K$;
2. $c : G_K \to (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ has entries fixed by $\sigma^r$ and continuous in $g$, and satisfies $c(gh) = c(g) + \tau(g) c(h)$;
3. for every $m \geq 0$ there is $b_m \in B_{\mathrm{dR}}^n$ with $\sigma^m(c(g)) = \tau_m(g)\, g(b_m) - b_m$ for all $g \in G_K$.

Then there is $b \in B_{\mathrm{st}}^n$ with $c(g) = \tau(g)\, g(b) - b$ for all $g \in G_K$.

Lean: `GlobalTheory.T.hyodo_theorem_matrix_unramifiedCoefficients` (also `GlobalTheory.PMon.hyodo_mat`, the proof).

Hypothesis 1 says that $\tau$ is semistable over $K$ itself, with period matrix $Q$. Hypothesis 3 says that $c$ dies over $B_{\mathrm{dR}}$ for every embedding $\sigma^m$, which is the de Rham condition on the extension of $\tau$ by $c$.

The idea is to view $\tau$ as a representation over $\mathbb{Q}_\ell$ of dimension $nr$ and to apply the Theorem to it. We use the following facts, proved elsewhere in this development.

1. (Coordinates.) Since $r > 0$, there are $\omega_0, \dots, \omega_{r-1} \in \mathbb{Q}_\ell^{\mathrm{ur}}$ fixed by $\sigma^r$ such that the matrix $W = (\sigma^m(\omega_k))_{m,k}$ is invertible and has the following property. For every topological space $X$ and every continuous $x : X \to \mathbb{Q}_\ell^{\mathrm{ur}}$ with values fixed by $\sigma^r$, there is a continuous $a : X \to \mathbb{Q}_\ell^r$ with $\sigma^m(x(t)) = \sum_k W_{mk}\, a_k(t)$ for all $t$ and all $m < r$.
2. (Rational form.) There are $\rho_0 : G_K \to \mathrm{GL}_{n \times r}(\mathbb{Q}_\ell)$ with continuous entries and $p \in \mathrm{GL}_{n \times r}(\mathbb{Q}_\ell^{\mathrm{ur}})$ with entries in $K$ such that
$$p\, \rho_0(g) = \operatorname{blockdiag}_{m < r} \big(\sigma^m(\tau(g))\big)\, p \quad \text{for all } g \in G_K.$$
For every $c$ as in hypothesis 2 there is a continuous $c_0 : G_K \to \mathbb{Q}_\ell^{n \times r}$ with $(p\, c_0(g))_{(i,m)} = \sigma^m(c(g)_i)$, and $c_0$ is a cocycle for $\rho_0$.
3. (Period matrix.) From $Q$ we get $Q_0 \in \mathrm{GL}_{n \times r}(B_{\mathrm{st}})$ with $\rho_0(g)\, g(Q_0) = Q_0$ for all $g \in G_K$. A representation of $G_K$ on $\mathbb{Q}_\ell^{n \times r}$ with such an invertible period matrix is semistable.
4. (De Rham.) Hypothesis 3 gives $\beta \in B_{\mathrm{dR}}^{n \times r}$ with $c_0(g) = \rho_0(g)\, g(\beta) - \beta$ for all $g$, and such a $\beta$ gives an element of $\mathbb{Q}_\ell^{n \times r} \otimes B_{\mathrm{dR}}$ that kills $c_0$.
5. (Back to vectors.) An element of $\mathbb{Q}_\ell^{n \times r} \otimes B_{\mathrm{st}}$ that kills $c_0$ gives $\beta' \in B_{\mathrm{st}}^{n \times r}$ with $c_0(g) = \rho_0(g)\, g(\beta') - \beta'$, and such a $\beta'$ gives a vector $b$ as in the conclusion, through $p$ and the block $m = 0$.

The block diagonal form says that $\rho_0$ is $\tau$ viewed as a representation over $\mathbb{Q}_\ell$ on $F^n$, where $F$ is the field of $\sigma^r$-fixed elements: after extending scalars, it splits into the $r$ conjugates $\sigma^m(\tau)$.

*Proof.* Take the coordinates of fact 1, and then $\rho_0$, $p$ and $c_0$ by fact 2. By fact 3, $\rho_0$ is semistable on $V_0 = \mathbb{Q}_\ell^{n \times r}$. It is continuous, so $g \mapsto \rho_0(g)v$ is continuous for every $v$. By fact 4, $c_0$ dies in $V_0 \otimes B_{\mathrm{dR}}$. Hyodo's theorem gives an element of $V_0 \otimes B_{\mathrm{st}}$ that kills $c_0$, and fact 5 turns it into $b$. $\square$

**Remark 6.24.4 (Formalization).** In the proof of Hyodo's theorem the inclusion $Z^1_f(V) \subseteq S$ of fact 5 is not used (it is bound as `_hfS` in [HyodoStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HyodoStatement.lean#L32)). The space of exponential cocycles is named `crystallineCocycles`, but it is the space of cocycles that die in $V \otimes B^{\varphi = 1}$, that is $H^1_e$, not $H^1_f$. Facts 1 to 7 are `GlobalTheory.T.exists_tateTwistDual_perfectPairing`, `GlobalTheory.T.isDeRham_of_isSemistable`, `GlobalTheory.T.de_rham_filtration_duality`, `GlobalTheory.T.finiteDimensional_continuousCocycles_galoisRep`, `GlobalTheory.T.semistable_cocycles_between_blochKato_and_continuous`, `GlobalTheory.T.finrank_blochKato_g_add_e_le_f_add_f` and `GlobalTheory.T.finrank_finite_le_exponential_cocycles`; we read their statements, not their proofs, and the comparison with Bloch and Kato is ours. In the matrix form the representation is called `σ`, and the de Rham hypothesis is asked for every $m \geq 0$, not only for $m < r$.
