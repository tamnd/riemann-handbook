---
title: Highest weights and twisted traces
decls:
  - GlobalTheory.CompanionTheory.RealCountG.CharDec.main
  - GlobalTheory.T.dual_weight_trace_formula
  - GlobalTheory.CompanionTheory.RealCountG.dualtr
  - GlobalTheory.CompanionTheory.RealCountG.countG
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Highest weights and twisted traces

Twisted Lefschetz numbers of $(\mathfrak{g}, K)$-modules are traces of an involution on spaces of $K$-equivariant maps $\operatorname{Hom}_K(E', V)$, where $E$ is a finite dimensional representation of the maximal compact subgroup $K = U(n)$. This section computes such a trace for a unitary representation $V$ of $GL_n(\mathbb{C})$ with the infinitesimal character of a dominant weight $\lambda$. The answer is $2^n$ times a sum of traces on highest weight spaces of $V$, over an explicit finite set of weights. The proof has three steps: a twisted Weyl character formula for $E'$, the identification of the coefficients by comparing characters, and a factorization of $\operatorname{Hom}_K(E', V)$ along highest weight spaces. The result is used in the [count of twisted traces](/entry/count-g-holds/). The background is in [compact groups](/learn/representations/#compact-groups), [highest weights and branching](/learn/representations/#highest-weights-and-branching) and [representations of real groups](/learn/representations/#representations-of-real-groups).

### Notation

Let $K = U(n)$. For $z \in \mathbb{C}^n$ write $\operatorname{diag}(z)$ for the diagonal matrix. A weight is a vector $\nu \in \mathbb{Z}^n$; it is dominant if $\nu_1 \ge \nu_2 \ge \dots \ge \nu_n$. The Weyl character of $\nu$ is the Schur function
$$s_\nu(z) = \frac{\det\bigl(z_i^{\nu_j + n - j}\bigr)}{\det\bigl(z_i^{n - j}\bigr)},$$
with indices $i, j$ from $1$ to $n$. For weights $\nu, m \in \mathbb{R}^n$, $\nu \preceq m$ means $\sum_{a \le k} \nu_a \le \sum_{a \le k} m_a$ for all $k$, with equality for $k = n$.

A $K$-module is a finite dimensional Hilbert space $E$ with a continuous unitary representation $\rho$ of $K$. Its dual $E'$ carries the representation $k \cdot \xi = \xi \circ \rho(k^{-1})$. A dual Lie family is a family $(G_{ab})$ of operators on $E'$ that satisfies the commutation relations of the basis $e_{ab}$ of $\mathfrak{gl}_n$ and gives the derivative of the $K$-action: for $X$ skew-Hermitian and $\gamma(t) = \exp(tX)$, the derivative of $\gamma(t)\cdot\xi$ at $t = 0$ is $\sum_{a,b} X_{ab} G_{ab}\xi$. A highest weight vector of weight $\mu$ is a vector $v$ with $G_{aa} v = \mu_a v$ for all $a$ and $G_{ab} v = 0$ for $a < b$. Write $\operatorname{hw}_\mu(E')$ for the space of these vectors. For an operator $T$ on $E$, its transpose is $T^t \xi = \xi \circ T$.

For a subspace $W$ and an operator $S$ that preserves it, $\operatorname{tr}_W S$ is the trace of the restriction; it is $0$ if $S$ does not preserve $W$.

### The twisted character of the dual

**Theorem 3.9.1 (Twisted characters by highest weights).** Let $E$ be a $K$-module, $T$ an operator on $E$ commuting with $\rho$, and $(G_{ab})$ a dual Lie family. There is a finite set $F$ of dominant weights such that $\operatorname{hw}_\nu(E') = 0$ for dominant $\nu \notin F$, and for every $k = \operatorname{diag}(z) \in K$ with distinct $z_a$,
$$\operatorname{tr}_{E'}\bigl( k \cdot T^t \bigr) = \sum_{\nu \in F} \operatorname{tr}_{\operatorname{hw}_\nu(E')}(T^t)\; s_\nu(z).$$

Lean: `GlobalTheory.CompanionTheory.RealCountG.CharDec.main` (also `GlobalTheory.T.dual_weight_trace_formula`, a second name).

The left side is written in Lean as the trace of the transpose of $\rho(k^{-1})T$, which is the same operator.

We use the following facts about a finite dimensional unitary representation $H$ of $K$ with its Lie family $G$, taken as given.

- (Isotypic projectors.) For each dominant $\nu$ there is an operator $p_\nu$ on $H$ that commutes with all $G_{ab}$, is the identity on $\operatorname{hw}_\nu(H)$, kills highest weight vectors of every other weight, and satisfies $\operatorname{tr}_H(\rho(k)\, S\, p_\nu) = \operatorname{tr}_{\operatorname{hw}_\nu(H)}(S)\, s_\nu(z)$ for every $S$ commuting with all $G_{ab}$ and every $k = \operatorname{diag}(z)$ with distinct $z_a$.
- (Weights of highest weight vectors.) Every highest weight vector has an integral dominant weight.
- (Vanishing.) An operator that commutes with all $G_{ab}$ and kills every highest weight vector is $0$.
- (Euclidean model.) The dual $E'$, with its representation, is isomorphic to a unitary representation on a Euclidean space, and the dual Lie family corresponds to the Lie family of that representation.

The isotypic projector is the projection onto the $\nu$-isotypic part, given by integrating against the character; its trace formula is the Weyl character formula for the irreducible representation of highest weight $\nu$.

*Proof.* By the Euclidean model we may work with a unitary representation $H$ and its Lie family. The operator $S = T^t$ commutes with all $G_{ab}$, because $T$ commutes with $\rho$.

The set $F$ of dominant $\nu$ with $\operatorname{hw}_\nu(H) \neq 0$ is finite. Pick $v_\nu \neq 0$ in each of these spaces. If $\sum c_\nu v_\nu = 0$, apply $p_\mu$: it fixes $v_\mu$ and kills $v_\nu$ for $\nu \neq \mu$, so $c_\mu = 0$. So the $v_\nu$ are linearly independent in the finite dimensional space $H$.

Now $1 - \sum_{\nu \in F} p_\nu$ commutes with all $G_{ab}$. It kills every highest weight vector $v$: the weight $\nu_0$ of $v$ is integral and dominant, so $\nu_0 \in F$ if $v \neq 0$, and then $p_{\nu_0} v = v$ while $p_\nu v = 0$ for $\nu \neq \nu_0$. By vanishing, $\sum_{\nu \in F} p_\nu = 1$. Hence
$$\operatorname{tr}_H(\rho(k) S) = \sum_{\nu \in F} \operatorname{tr}_H(\rho(k)\, S\, p_\nu) = \sum_{\nu \in F} \operatorname{tr}_{\operatorname{hw}_\nu(H)}(S)\, s_\nu(z). \qquad \square$$

### Lefschetz $K$-types and harmonic weights

**Definition 3.9.2 (Lefschetz $K$-type).** Let $\lambda$ be dominant. A Lefschetz $K$-type for $\lambda$ is a $K$-module $E$ with an operator $T$ such that $T$ commutes with $\rho$, $T^2 = 1$, and for every $k = \operatorname{diag}(z) \in K$ with distinct $z_a^2$:
$$\operatorname{tr}_E \rho(k) = \prod_{a,b} \Bigl(1 + \frac{z_a}{z_b}\Bigr)\, \overline{s_\lambda(z)}^{\,2}, \qquad \operatorname{tr}_E\bigl(\rho(k) T\bigr) = \prod_{a,b} \Bigl(1 + \frac{z_a}{z_b}\Bigr)\, \overline{s_\lambda(z^2)}.$$

The product runs over all pairs $(a, b)$, including $a = b$; it is the character of the exterior algebra of the adjoint representation of $K$ on $\mathfrak{gl}_n$. Its diagonal factors contribute $2^n$.

**Definition 3.9.3 (Harmonic weights).** Let $\lambda$ be dominant. A level function is a nondecreasing map $\ell : \{1, \dots, n\} \to \{1, \dots, n\}$ such that $\ell(a) = \ell(b)$ implies $\lambda_a = \lambda_b$. Its weight is
$$\mu_a = 2\lambda_a + \#\{b : \ell(b) > \ell(a)\} - \#\{b : \ell(b) < \ell(a)\}.$$
The set $\operatorname{Harm}(\lambda)$ of harmonic weights is the set of these $\mu$. Put $m_0(\lambda)_a = 2\lambda_a + n + 1 - 2a$.

For an injective level function, $\mu = m_0(\lambda)$, which is $2\lambda + 2\rho$ in the usual notation. Level functions that are constant on blocks give the other harmonic weights. If $\lambda$ is regular in the sense that $\lambda_a > \lambda_{a+1}$ for all $a$, then $m_0(\lambda)$ is the only harmonic weight.

We use two facts, taken as given.

- (Twisted trace of a Lefschetz $K$-type.) If $(E, T)$ is a Lefschetz $K$-type for $\lambda$, then for $k = \operatorname{diag}(z) \in K$ with distinct $z_a^2$,
$$\operatorname{tr}_{E'}(k \cdot T^t) = \prod_{a,b}\Bigl(1 + \frac{z_a}{z_b}\Bigr)\, s_\lambda(z^2).$$
- (Coefficients.) Let $F$ be a finite set of dominant weights and $c$ a function on $F$ such that $\sum_{\nu \in F} c_\nu s_\nu(z) = \prod_{a,b}(1 + z_a/z_b)\, s_\lambda(z^2)$ for all $z$ with $|z_a| = 1$ and distinct $z_a^2$. Then $\operatorname{Harm}(\lambda) \subseteq F$ and $c_\mu = 2^n$ for every $\mu \in \operatorname{Harm}(\lambda)$.

**Theorem 3.9.4 (Traces on harmonic highest weight spaces).** Let $\lambda$ be dominant, $(E, T)$ a Lefschetz $K$-type for $\lambda$, and $(G_{ab})$ a dual Lie family. Then for every $\mu \in \operatorname{Harm}(\lambda)$,
$$\operatorname{tr}_{\operatorname{hw}_\mu(E')}(T^t) = 2^n.$$

Lean: `GlobalTheory.CompanionTheory.RealCountG.dualtr`.

*Proof.* Take $F$ from the [theorem on twisted characters](/entry/char-dec-main/), and put $c_\nu = \operatorname{tr}_{\operatorname{hw}_\nu(E')}(T^t)$. Let $|z_a| = 1$ with distinct $z_a^2$. Then the $z_a$ are distinct, and $\operatorname{diag}(z)$ is unitary. So the theorem on twisted characters and the twisted trace of the Lefschetz $K$-type give the same left side, and
$$\sum_{\nu \in F} c_\nu\, s_\nu(z) = \prod_{a,b}\Bigl(1 + \frac{z_a}{z_b}\Bigr)\, s_\lambda(z^2).$$
The fact on coefficients gives $c_\mu = 2^n$ for $\mu \in \operatorname{Harm}(\lambda)$. $\square$

### The twisted count

Now let $V$ be a Hilbert space with two commuting families $(E^1_{ab})$, $(E^2_{ab})$ of operators satisfying the relations of $\mathfrak{gl}_n$, so that $V$ is a module over the complexified Lie algebra $\mathfrak{gl}_n \oplus \mathfrak{gl}_n$ of $GL_n(\mathbb{C})$. Let $\sigma$ be a unitary representation of $K$ on $V$ and $A$ an operator.

**Definition 3.9.5 (Core module).** The quadruple $(V, E^1, E^2, \sigma, A)$ is a core module for $\lambda$ if: the centres of the two enveloping algebras act by the infinitesimal characters with parameters $\pm(\lambda_a + \tfrac{n+1}{2} - a)$, $1 \le a \le n$; $V \neq 0$ and the algebra generated by the $E^i_{ab}$ acts transitively on nonzero vectors; every vector lies in a finite dimensional $K$-stable subspace on which the derivative of $\sigma$ is $E^1 + E^2$; $A^2 = 1$, $A E^1_{ab} = E^2_{ab} A$, and $A$ commutes with $\sigma$.

Write $\operatorname{hw}_\mu(V)$ for the highest weight vectors of weight $\mu$ for the $K$-action, with Lie family $E^1 + E^2$. Let $\operatorname{Hom}_K(E', V)$ be the space of linear maps $t : E' \to V$ with $t(k\cdot\xi) = \sigma(k) t(\xi)$, and define the flip $\Phi(t) = A \circ t \circ T^t$.

We use the following facts, taken as given.

- (Weights of the dual.) If $(E, T)$ is a Lefschetz $K$-type for $\lambda$, then $E'$ is the sum of its weight spaces, and every weight $\mu$ of $E'$ satisfies $\mu \preceq m_0(\lambda)$.
- (Derivatives.) Every $t \in \operatorname{Hom}_K(E', V)$ carries $G_{ab}$ to $E^1_{ab} + E^2_{ab}$. So $t$ maps $\operatorname{hw}_\mu(E')$ into $\operatorname{hw}_\mu(V)$.
- (Restriction is injective.) Let $M$ be a finite set of weights containing every $\nu$ for which $\nu$ is a weight of $E'$ and $\operatorname{hw}_\nu(V) \neq 0$. If $t \in \operatorname{Hom}_K(E', V)$ vanishes on $\operatorname{hw}_\mu(E')$ for all $\mu \in M$, then $t = 0$.
- (Extension.) For every finite $M$ and every family of linear maps $f_\mu : \operatorname{hw}_\mu(E') \to \operatorname{hw}_\mu(V)$, there is $t \in \operatorname{Hom}_K(E', V)$ that restricts to $f_\mu$ for $\mu \in M$.
- (Parthasarathy's inequality.) If $v \neq 0$ is in $\operatorname{hw}_\nu(V)$, the Parthasarathy, Ranga Rao and Varadarajan construction gives a nonzero highest weight vector in $V$ tensored with a Clifford module, of weight $w\nu - w\rho$ for some permutation $w$; and for such a vector of weight $\tau$, $|m_0(\lambda)|^2 \le |\tau + \rho|^2$.
- (Harmonic from the norm bound.) If $\nu$ is dominant, $\nu \preceq m_0(\lambda)$, and $|m_0(\lambda)|^2 \le |w\nu - w\rho + \rho|^2$ for such a $w$, then $\nu \in \operatorname{Harm}(\lambda)$.
- (Traces on spaces of maps.) If $I \cong \prod_i \operatorname{Hom}(W_i, H_i)$ with $I$ and all $W_i \neq 0$ finite dimensional, and $\Phi$ acts by $f_i \mapsto a_i f_i b_i$, then each $H_i$ is finite dimensional and $\operatorname{tr}_I \Phi = \sum_i \operatorname{tr}(b_i) \operatorname{tr}(a_i)$.

Parthasarathy's inequality is the Dirac inequality for unitary representations: the square of the Dirac operator is a difference of Casimir eigenvalues, and it is nonnegative on a unitary module.

**Lemma 3.9.6 (Highest weights below $m_0$ are harmonic).** Let $V$ be a core module for $\lambda$. If $\operatorname{hw}_\nu(V) \neq 0$ and $\nu \preceq m_0(\lambda)$, then $\nu \in \operatorname{Harm}(\lambda)$.

*Proof.* A nonzero highest weight vector lies in a finite dimensional $K$-stable subspace, so its weight $\nu$ is dominant. Parthasarathy's inequality gives $w$ and the norm bound, and the last fact gives $\nu \in \operatorname{Harm}(\lambda)$. $\square$

**Theorem 3.9.7 (Twisted count).** Let $\lambda$ be dominant, $(E, T)$ a Lefschetz $K$-type for $\lambda$, and $(V, E^1, E^2, \sigma, A)$ a core module for $\lambda$, with $\operatorname{Hom}_K(E', V)$ finite dimensional. Then:

1. for $\mu \in \operatorname{Harm}(\lambda)$, $A$ preserves $\operatorname{hw}_\mu(V)$ and this space is finite dimensional;
2. if $\operatorname{Hom}_K(E', V) \neq 0$, then $\operatorname{hw}_\mu(V) \neq 0$ for some $\mu \in \operatorname{Harm}(\lambda)$;
3. $\displaystyle \operatorname{tr}_{\operatorname{Hom}_K(E', V)} \Phi = 2^n \sum_{\mu \in \operatorname{Harm}(\lambda)} \operatorname{tr}_{\operatorname{hw}_\mu(V)} A.$

Lean: `GlobalTheory.CompanionTheory.RealCountG.countG`.

*Proof.* Take a dual Lie family $(G_{ab})$ on $E'$. By the facts on weights of the dual and the lemma, every $\nu$ that is a weight of $E'$ with $\operatorname{hw}_\nu(V) \neq 0$ lies in $\operatorname{Harm}(\lambda)$. So restriction to the spaces $\operatorname{hw}_\mu(E')$, $\mu \in \operatorname{Harm}(\lambda)$, is injective on $\operatorname{Hom}_K(E', V)$, and by extension it is onto. This gives an isomorphism
$$R : \operatorname{Hom}_K(E', V) \xrightarrow{\ \sim\ } \prod_{\mu \in \operatorname{Harm}(\lambda)} \operatorname{Hom}\bigl(\operatorname{hw}_\mu(E'), \operatorname{hw}_\mu(V)\bigr).$$
The operator $A$ preserves each $\operatorname{hw}_\mu(V)$, since $A$ exchanges $E^1$ and $E^2$ and so commutes with $E^1 + E^2$. The flip $\Phi$ preserves $\operatorname{Hom}_K(E', V)$, since $A$ commutes with $\sigma$ and $T$ commutes with $\rho$. The transpose $T^t$ preserves each $\operatorname{hw}_\mu(E')$, since it commutes with the dual Lie family. Under $R$, $\Phi$ acts by $f_\mu \mapsto A f_\mu T^t$.

By the [theorem on harmonic traces](/entry/dualtr/), $\operatorname{tr}_{\operatorname{hw}_\mu(E')} T^t = 2^n \neq 0$, so each $\operatorname{hw}_\mu(E')$ is nonzero. The fact on traces on spaces of maps now gives that each $\operatorname{hw}_\mu(V)$ is finite dimensional, which is part 1, and
$$\operatorname{tr} \Phi = \sum_{\mu} \operatorname{tr}_{\operatorname{hw}_\mu(E')}(T^t)\, \operatorname{tr}_{\operatorname{hw}_\mu(V)}(A) = 2^n \sum_{\mu} \operatorname{tr}_{\operatorname{hw}_\mu(V)}(A),$$
which is part 3. For part 2, if every $\operatorname{hw}_\mu(V)$ with $\mu \in \operatorname{Harm}(\lambda)$ is $0$, then every $t$ restricts to $0$ on these spaces, so $t = 0$ by injectivity. $\square$

**Remark 3.9.8 (Formalization).** The facts used are statements of the form `GlobalTheory.T.*`: `highest_weight_integral_of_unitary`, `highest_weight_of_unitary_derivative`, `intertwiner_eq_zero_of_vanish_on_highest`, `unitary_euclidean_model` and `exists_compact_lie_action` for the first theorem; `twisted_trace_weyl_character` and `harmonic_weights_coefficient` for the second; and `dual_weights_dominated`, `exists_dual_lie_family`, `invariant_intertwines_dual`, `finite_weights_invariant_hom`, `exists_invariant_extending`, `parthasarathy_rao_varadarajan`, `clifford_highest_weight_vector`, `harmonic_of_norm_bound` and `trace_factor_tensor_decomp` for the third. The weights of the twisted count are stated in real form, as the image of the integral harmonic weights. The module [DiagonalMemUnitary.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DiagonalMemUnitary.lean#L112) is named after a helper lemma at line 90, which says that a diagonal matrix with entries of modulus $1$ is unitary; the second and third theorems are at lines 100 and 112. The first theorem is at line 154 of [DualWeightTraceFormula.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/DualWeightTraceFormula.lean#L154).
