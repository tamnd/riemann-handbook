---
title: Orthogonal sums and Kronecker images
decls:
  - Formalism.L2.Col.hlat_orth_sum
  - Formalism.L2.Col.T2.kron_mu
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.majorant_kronecker_map
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_eq_of_isometric_sum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orthogonal sums and Kronecker images

This section computes slopes of two kinds of lattices built from simpler ones. The first is a sum of mutually orthogonal sublattices: its slope is the mean of the slopes when the ranks agree, and its maximal slope is at most the largest maximal slope of a summand. The second is the image of a power $L^\beta$ of a lattice under a linear map whose metric is given by an integer Gram matrix $g$: its slope is the slope of $L$ minus $\log\det g / |\beta|$. The first result bounds the maximal slope of the level-zero lattice in Section 7 class by class. The second gives the exact slope of the ramified sublattice in Sections 3 and 5.

We keep the notation of Section 1: $K$ is a number field, a hermitian lattice datum is $A = (V, b, X, L)$ with majorants $\langle\cdot,\cdot\rangle_v$, and $A[L']$ is the datum with the lattice $L'$ in place of $L$. For an $\mathcal{O}_K$-submodule $N \subseteq V$ we write $\operatorname{rk}_K N = \dim_K(KN)$.

### Orthogonal sums

**Definition 1.2.1 (Orthogonal family).** Let $A = (V, b, X, L)$ be a hermitian lattice datum and $(N_c)_{c \in \Gamma}$ a family of $\mathcal{O}_K$-submodules of $V$. The family is *orthogonal* if $\langle x, y \rangle_v = 0$ for every $v \in S_\infty$, every $c \neq c'$, every $x \in N_c$ and every $y \in N_{c'}$.

Orthogonality for all majorants means that the realizations $\rho_A(N_c)$ are mutually orthogonal in the Euclidean space of the realization, since $(\rho_A x, \rho_A y) = \sum_v \operatorname{Re}\langle x, y \rangle_v$.

**Theorem 1.2.2 (Slopes of an orthogonal sum).** Let $A$ be a hermitian lattice datum with invertible frames. Let $\Gamma$ be a nonempty finite set and $(N_c)_{c \in \Gamma}$ an orthogonal family of finitely generated nonzero $\mathcal{O}_K$-submodules of $V$. Let $r > 0$ be an integer with $\operatorname{rk}_K N_c = r$ for all $c$ and $\operatorname{rk}_K \sum_c N_c = |\Gamma|\, r$. Put $N = \sum_c N_c$. Then
$$
\mu(A[N]) = \frac{1}{|\Gamma|} \sum_{c \in \Gamma} \mu(A[N_c]),
$$
and there is a $c \in \Gamma$ with $\mu_{\max}(A[N]) \leq \mu_{\max}(A[N_c])$.

Lean: `Formalism.L2.Col.hlat_orth_sum` (also `Formalism.L2.Col.hlat_orth_fin`, the form for a finite subfamily).

*Proof.* All the modules are finitely generated and the frames are invertible, so their realizations are discrete subgroups, of $\mathbb{Z}$-rank $[K:\mathbb{Q}]$ times their $K$-rank. Since the realizations of the $N_c$ are mutually orthogonal, the realization of $N$ is their orthogonal direct sum. The covolume of an orthogonal direct sum is the product of the covolumes, so $\deg \rho(N) = \sum_c \deg \rho(N_c)$. Dividing by $\operatorname{rk}\rho(N) = [K:\mathbb{Q}]\,|\Gamma|\,r$ gives that $s(\rho(N))$ is the mean of the $s(\rho(N_c))$, and the first claim follows from the definition of $\mu$, which is affine in $s$.

For the second claim it suffices to show, for two orthogonal discrete subgroups $\Lambda_1, \Lambda_2$ of a Euclidean space, that every nonzero subgroup $\Lambda' \subseteq \Lambda_1 \oplus \Lambda_2$ has $s(\Lambda') \leq \max(\mu_{\max}(\Lambda_1), \mu_{\max}(\Lambda_2))$, where here $\mu_{\max}$ is the maximal Euclidean slope; then induction on $|\Gamma|$ gives $\mu_{\max}(A[N]) \leq \max_c \mu_{\max}(A[N_c])$, and we take for $c$ an index where the maximum is attained. Let $p_2$ be the orthogonal projection onto the span of $\Lambda_2$. The kernel of $p_2$ on $\Lambda'$ is $\Lambda'_1 = \Lambda' \cap \Lambda_1$, which is saturated in $\Lambda'$, and its real span is the kernel of $p_2$ on the span of $\Lambda'$. So $p_2$ induces a bijection from the quotient $\Lambda'/\Lambda'_1$ onto $p_2(\Lambda') \subseteq \Lambda_2$ that does not increase lengths, and hence $\deg(\Lambda'/\Lambda'_1) \leq \deg p_2(\Lambda')$. With the additivity of $\deg$ in Section 1,
$$
\deg \Lambda' \leq \deg \Lambda'_1 + \deg p_2(\Lambda') \leq \mu_{\max}(\Lambda_1) \operatorname{rk}\Lambda'_1 + \mu_{\max}(\Lambda_2) \operatorname{rk} p_2(\Lambda'),
$$
where a term with rank zero is zero. The ranks add up to $\operatorname{rk}\Lambda'$, which gives the claim. $\square$

The equal rank condition is needed only for the mean. Without it the slope of $N$ is the mean of the slopes weighted by the ranks.

### Kronecker images

Let $W$ be a hermitian lattice datum $(V_W, b_W, X_W, L_W)$ and $\beta$ a finite set. The power $L_W^\beta$ is the $\mathcal{O}_K$-module of functions $F : \beta \to V_W$ with all values in $L_W$. An integer matrix $g \in M_\beta(\mathbb{Z})$ defines a hermitian form on $V_W^\beta$ at each place,
$$
\langle F, F' \rangle_{g, v} = \sum_{b, c \in \beta} g_{bc} \langle F_b, F'_c \rangle_v .
$$
For $g$ the identity this is the orthogonal sum of $|\beta|$ copies of $W$.

**Theorem 1.2.3 (Slope of a Kronecker image).** Let $K$ be totally complex. Let $B = (V, b, X, L)$ be a hermitian lattice datum with invertible frames, and $W$ a good datum with $L_W \neq 0$. Let $\beta$ be a nonempty finite set, $\Psi : V_W^\beta \to V$ an injective $K$-linear map, and $g \in M_\beta(\mathbb{Z})$ with $\det g > 0$ such that
$$
\langle \Psi F, \Psi F' \rangle_v = \sum_{b, c \in \beta} g_{bc} \langle F_b, F'_c \rangle_v \qquad \text{for all } v \in S_\infty \text{ and } F, F' \in V_W^\beta.
$$
Then
$$
\mu\big(B[\Psi(L_W^\beta)]\big) = \mu(W) - \frac{\log \det g}{|\beta|}.
$$

Lean: `Formalism.L2.Col.T2.kron_mu`

*Proof.* Let $m = [K:\mathbb{Q}] \operatorname{rk}_K L_W$, and let $w_1, \dots, w_m \in L_W$ have realizations that form a $\mathbb{Z}$-basis of $\rho_W(L_W)$, with real Gram matrix $\Gamma$. The vectors $\Psi(\delta_b w_k)$, for $b \in \beta$ and $1 \leq k \leq m$, where $\delta_b w_k$ is the function with value $w_k$ at $b$ and $0$ elsewhere, generate $\Psi(L_W^\beta)$ over $\mathbb{Z}$ and are independent because $\Psi$ is injective. The real inner product of the realization is $\sum_v \operatorname{Re} \langle\cdot,\cdot\rangle_v$, and $g$ has real entries, so by the hypothesis their real Gram matrix is the Kronecker product $g \otimes \Gamma$. Since $\det(g \otimes \Gamma) = (\det g)^m (\det\Gamma)^{|\beta|}$,
$$
\operatorname{covol} \rho_B(\Psi(L_W^\beta)) = (\det g)^{m/2} \operatorname{covol}(\rho_W(L_W))^{|\beta|}.
$$
The rank is $|\beta|\, m$, so $s(\rho_B(\Psi(L_W^\beta))) = s(\rho_W(L_W)) - \log\det g/(2|\beta|)$. Doubling and adding $\kappa_K$ gives the formula. $\square$

**Corollary 1.2.4 (Isometric sums).** Let $K$, $B$, $W$ be as in the theorem, $\alpha$ a nonempty finite set, and $\Psi : V_W^\alpha \to V$ injective and $K$-linear with $\langle \Psi F, \Psi F' \rangle_v = \sum_{a \in \alpha} \langle F_a, F'_a \rangle_v$ for all $v$, $F$, $F'$. If $L = \Psi(L_W^\alpha)$, then $\mu(B) = \mu(W)$.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_eq_of_isometric_sum`

*Proof.* This is the theorem with $\beta = \alpha$ and $g$ the identity matrix, whose determinant is $1$. $\square$

The Kronecker images that occur below are images of an isometric sum under an integer change of variables. For a matrix $t \in M_{\beta \times \alpha}(\mathbb{Z})$ let $t_* : V_W^\beta \to V_W^\alpha$ be the $K$-linear map
$$
(t_* F)_a = \sum_{b \in \beta} t_{ba} F_b .
$$

**Lemma 1.2.5 (Gram matrix of an integer change of variables).** Let $\Psi : V_W^\alpha \to V$ be $K$-linear with $\langle \Psi F, \Psi F' \rangle_v = \sum_{a \in \alpha} \langle F_a, F'_a \rangle_v$ for all $v$, and let $t \in M_{\beta \times \alpha}(\mathbb{Z})$. Then for all $v$ and $F, F' \in V_W^\beta$,
$$
\langle \Psi t_* F, \Psi t_* F' \rangle_v = \sum_{b, c \in \beta} (t\, t^{\mathsf{T}})_{bc} \langle F_b, F'_c \rangle_v .
$$

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.majorant_kronecker_map`

*Proof.* The left side is $\sum_a \langle \sum_b t_{ba} F_b, \sum_c t_{ca} F'_c \rangle_v$. The form is additive in each variable and the coefficients are integers, so it equals $\sum_{b, c} \big(\sum_a t_{ba} t_{ca}\big) \langle F_b, F'_c \rangle_v$, and $\sum_a t_{ba} t_{ca} = (t\,t^{\mathsf{T}})_{bc}$. $\square$

So if $\Psi$ is an isometric sum and $t_*$ is injective, the theorem applies to $\Psi \circ t_*$ with $g = t\,t^{\mathsf{T}}$, as soon as $\det(t\,t^{\mathsf{T}}) > 0$. In Section 3 the matrix $t$ is the matrix of the basic ramified functions on a product of finite groups.

**Example 1.2.6.** Let $\alpha = \{1, 2\}$, $\beta = \{1\}$ and $t = (1\ \ {-1})$, so that $t_* x = (x, -x)$. Then $t\,t^{\mathsf{T}} = (2)$, and the antidiagonal $\{(x, -x) : x \in L_W\}$ of the orthogonal sum $W \oplus W$ has slope $\mu(W) - \log 2$. In the normalization of Volume 1 this is the familiar fact that the vectors $(x, -x)$ are longer than $x$ by the factor $\sqrt 2$.

**Remark 1.2.7 (Formalization).** The orthogonal sum theorem has no assumption that $K$ is totally complex, while the Kronecker image theorem and its corollary do. The Kronecker image theorem asks only for invertible frames on $B$, not that $B$ be good: its lattice is replaced by the image $\Psi(L_W^\beta)$. The second part of the orthogonal sum theorem comes from a general result on orthogonal sums of Euclidean lattices, which we did not unfold; the argument above is the classical one.
