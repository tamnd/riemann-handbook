---
title: Injectivity of the top class
decls:
  - GlobalTheory.T.injective_unipotent_of_restriction
  - GlobalTheory.CompanionTheory.LvChain.injUU_of_injRL
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Injectivity of the top class

Let $V$ be a pair module with a lowest $K$-type, as in the previous section, and let $u$ be a highest weight vector of that $K$-type. The real descent of Volume 8 needs to know that the top compact class $e_{\omega_U} \otimes u$ does not die in the homology $H_*(\mathfrak{u}, V)$: if it is a boundary, then $u = 0$. This section reduces this statement for the nilradical $\mathfrak{u}$ of a block parabolic to the same statement for a larger nilpotent algebra $\mathfrak{r}$, which also contains the compact part of the Levi. The reduction is one of the inputs of [Theorem 7.2 of Volume 8](/entry/injective-decomposition-action-holds/), and through it of the step [EveryCharacter](/step/every-character/). We keep the notation of [Theorem 1.1.7](/entry/gen-cou2/): pair modules, letters, chains, the boundary $\partial_S$, a level function and the set $\mathfrak{u}$.

### Weights and admissible modules

Let $\rho_a = \frac{n-1}{2} - a$. For a level function $\mathrm{lev}$, put
$$\rho^U_a = \tfrac{1}{2}\bigl(\#\{b : \mathrm{lev}(a) < \mathrm{lev}(b)\} - \#\{b : \mathrm{lev}(b) < \mathrm{lev}(a)\}\bigr),$$
the $a$-th coordinate of half the sum of the roots $e_a - e_b$ with $\mathrm{lev}(a) < \mathrm{lev}(b)$. Let $\lambda \in \mathbb{Z}^n$. We say that $(\lambda, \mathrm{lev})$ is *adapted* if $\mathrm{lev}$ is monotone and $\lambda$ is constant on each block. Put $\mu_Q = 2\lambda + 2\rho^U$.

**Definition 1.2.1 (Highest weight space).** For $\mu \in \mathbb{R}^n$ and a pair module $V$, let $V^{\mathrm{hw}}(\mu)$ be the space of $v \in V$ with $k_{aa} v = \mu_a v$ for all $a$ and $k_{ab} v = 0$ for all $a < b$.

**Definition 1.2.2 (Admissible for $(\lambda, \mathrm{lev})$).** Let $V$ be a complex inner product space with a pair module structure. We say $V$ is *admissible for $(\lambda, \mathrm{lev})$* if:

1. $\langle k_{ab} x, y \rangle = \langle x, k_{ba} y \rangle$ for all $a, b, x, y$ (the compact part acts unitarily);
2. every vector lies in a finite-dimensional subspace stable under all $k_{ab}$ (local finiteness);
3. for every $m \geq 0$, the Gelfand invariant $\sum_a (E^m)_{aa}$ of the first copy $E = E^1$ acts by the scalar attached to the parameter $\gamma_a = \lambda_a + \frac{n-1}{2} - a$, and the Gelfand invariant of the second copy, written as $E'_{ab} = -E^2_{ba}$, acts by the scalar attached to $-\gamma$ (the infinitesimal characters);
4. $V^{\mathrm{hw}}(\nu) = 0$ for every weight $\nu$ of *second type*: $\nu$ such that $\nu + \rho$ is strictly decreasing and $\nu + \rho = (\mu_Q + \rho - \mathrm{wt}(B)) \circ w$ for a permutation $w$ and a nonempty set $B$ of pairs $(a, b)$ with $\mathrm{lev}(a) < \mathrm{lev}(b)$, where $\mathrm{wt}(B) = \sum_{(a, b) \in B} (e_a - e_b)$.

Condition 4 says that no $K$-type occurs whose highest weight is obtained from $\mu_Q$ by subtracting a nonempty sum of distinct roots of $\mathfrak{u}$ and moving the result to the dominant chamber.

Let $\mathfrak{r}$ be the set of letters that are either $k$-letters or letters of $\mathfrak{u}$. It is closed under the bracket. Let $\omega_N$ be the set of all $k$-letters, so that $e_{\omega_N}$ spans the top exterior power of the compact part of $\mathfrak{r}$.

**Definition 1.2.3 (Injectivity for $\mathfrak{u}$ and for $\mathfrak{r}$).** We say *injectivity holds for $\mathfrak{u}$* if for every $n$, every decreasing $\lambda \in \mathbb{Z}^n$, every level function $\mathrm{lev}$ with $(\lambda, \mathrm{lev})$ adapted, every $V$ admissible for $(\lambda, \mathrm{lev})$, every $u \in V^{\mathrm{hw}}(\mu_Q)$ and every $\mathfrak{u}$-supported chain $y$ of degree $|\omega_U| + 1$:
$$\partial_{\mathfrak{u}} y = e_{\omega_U} \otimes u \implies u = 0 .$$
*Injectivity holds for $\mathfrak{r}$* if the same holds with $\mathfrak{r}$, $\omega_N$ and $\partial_{\mathfrak{r}}$ in place of $\mathfrak{u}$, $\omega_U$ and $\partial_{\mathfrak{u}}$.

### The compact Levi on chains

For $a, b$ in the same block, let $L_{ab}$ be the operator on chains that acts by $k_{ab}$ on the coefficients and by the adjoint action of $k_{ab}$ on the letters. This is the action of the compact part of the Levi on $\Lambda \mathfrak{u} \otimes V$. We take the following four facts as given; each is an input statement of the proof.

1. Every $\mathfrak{u}$-supported chain of a fixed degree lies in a finite-dimensional space $T$ of such chains that is stable under all $L_{ab}$ with $\mathrm{lev}(a) = \mathrm{lev}(b)$. This uses local finiteness.
2. Each $L_{ab}$ with $\mathrm{lev}(a) = \mathrm{lev}(b)$ commutes with $\partial_{\mathfrak{u}}$.
3. If $k_{ab} u = 0$ for all $a < b$, then $L_{ab}(e_{\omega_U} \otimes u) = 0$ for all $a < b$ in the same block.
4. With the inner product $\langle x, z \rangle = \sum_A \langle x_A, z_A \rangle$ on chains, $L_{ab}$ is adjoint to $L_{ba}$. This uses unitarity.

**Lemma 1.2.4 (Highest preimage).** Let $T$ be a finite-dimensional subspace of an inner product space, $(a_i)$ and $(b_i)$ families of operators with $\langle a_i x, z \rangle = \langle x, b_i z \rangle$, both preserving $T$, and $D$ an operator commuting with every $a_i$ and $b_i$ on $T$. Let $y \in T$ with $a_i D y = 0$ for all $i$. Then there is $y' \in T$ with $a_i y' = 0$ for all $i$ and $D y' = D y$.

*Proof.* Let $S \subseteq T$ be the span of all $b_i t$ with $t \in T$. Write $y = s + w$ with $s \in S$ and $w \perp S$, which is possible because $S$ is finite-dimensional. Then $w \in T$ and $\| a_i w \|^2 = \langle w, b_i a_i w \rangle = 0$, so $a_i w = 0$. Hence $a_i D s = a_i D y - D a_i w = 0$. For $z = b_i t \in S$ we get $\langle D s, D z \rangle = \langle D s, b_i D t \rangle = \langle a_i D s, D t \rangle = 0$, and so $D s \perp D S$. Since $s \in S$, $D s = 0$. Take $y' = w$. $\square$

### The reduction

**Theorem 1.2.5 (Injectivity for $\mathfrak{u}$ from injectivity for $\mathfrak{r}$).** If injectivity holds for $\mathfrak{r}$, then it holds for $\mathfrak{u}$.

Lean: `GlobalTheory.CompanionTheory.LvChain.injUU_of_injRL` (also `GlobalTheory.T.injective_unipotent_of_restriction`, the same statement).

*Proof.* Fix $\lambda$, $\mathrm{lev}$, $V$, $u \in V^{\mathrm{hw}}(\mu_Q)$ and a $\mathfrak{u}$-supported chain $y$ of degree $|\omega_U| + 1$ with $\partial_{\mathfrak{u}} y = e_{\omega_U} \otimes u$. Since $u$ is a highest weight vector, $k_{ab} u = 0$ for $a < b$.

Step 1. By fact 1 there is a finite-dimensional space $T$ of $\mathfrak{u}$-supported chains of degree $|\omega_U| + 1$ that contains $y$ and is stable under the compact Levi. Apply the lemma with the raising operators $a_i = L_{ab}$ ($a < b$ in one block), the lowering operators $b_i = L_{ba}$, and $D = \partial_{\mathfrak{u}}$. The hypotheses hold by facts 2 and 4, and $a_i D y = L_{ab}(e_{\omega_U} \otimes u) = 0$ by fact 3. We get $y' \in T$, killed by the raising operators of the compact Levi, with $\partial_{\mathfrak{u}} y' = e_{\omega_U} \otimes u$.

Step 2. Let $\ell_1, \dots, \ell_r$ be the $k$-letters $k_{ab}$ with $a < b$ in the same block, listed in a suitable order. These are exactly the $k$-letters that lie in $\mathfrak{r}$ but not in $\mathfrak{u}$, so $\omega_N = \omega_U \cup \{\ell_1, \dots, \ell_r\}$. Put $C = \varepsilon_{\ell_1} \cdots \varepsilon_{\ell_r} y'$. It is an $\mathfrak{r}$-supported chain of degree $|\omega_U| + 1 + r = |\omega_N| + 1$. We use the following input: for a $\mathfrak{u}$-supported chain $y'$ killed by the raising operators of the compact Levi, and for a suitable order of the letters,
$$\partial_{\mathfrak{r}}(\varepsilon_{\ell_1} \cdots \varepsilon_{\ell_r} y') = (-1)^r \varepsilon_{\ell_1} \cdots \varepsilon_{\ell_r}\, \partial_{\mathfrak{r}} y' .$$
On $\mathfrak{u}$-supported chains, $\partial_{\mathfrak{r}} = \partial_{\mathfrak{u}}$: every term of $\partial_{\mathfrak{r}}$ that involves a letter outside $\mathfrak{u}$ contracts with a letter that does not occur. So $\partial_{\mathfrak{r}} C = (-1)^r \varepsilon_{\ell_1} \cdots \varepsilon_{\ell_r}(e_{\omega_U} \otimes u)$.

Step 3. The letters $\ell_i$ are distinct and none lies in $\omega_U$. So $\varepsilon_{\ell_1} \cdots \varepsilon_{\ell_r} e_{\omega_U} = c\, e_{\omega_N}$ for a sign $c \neq 0$. Therefore $\partial_{\mathfrak{r}}\bigl(c^{-1}(-1)^r C\bigr) = e_{\omega_N} \otimes u$. Injectivity for $\mathfrak{r}$ gives $u = 0$. $\square$

The idea is the classical one: the compact Levi $\mathfrak{l} \cap \mathfrak{k}$ is reductive, the class of $e_{\omega_U} \otimes u$ is a highest weight vector for it, and multiplying by the top wedge of $\mathfrak{n} \cap \mathfrak{l} \cap \mathfrak{k}$ moves the question from $\mathfrak{u}$ to $\mathfrak{u} + (\mathfrak{n} \cap \mathfrak{l} \cap \mathfrak{k})$. The highest preimage is needed because the product formula of Step 2 holds only for chains killed by the raising operators.

**Remark 1.2.6 (Formalization).** The four facts on the compact Levi and the product formula of Step 2 are input statements (`exists_finite_levi_stable_chains`, `levi_commute_unipotent_boundary`, `levi_raising_kills_top_chain`, `levi_adjoint_on_chains`, `boundary_prod_creation_levi_chains`); the order of the letters comes from `exists_inside_order`. The highest preimage lemma is `highest_preimage` in [InjectiveUnipotentOfRestriction.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/InjectiveUnipotentOfRestriction.lean#L124), which transports `highest_preimage_inner` to chains. The equality $\partial_{\mathfrak{r}} = \partial_{\mathfrak{u}}$ on $\mathfrak{u}$-chains is `bdL_inRR_eq` (L22). The infinitesimal character in condition 3 is written with `gelfVal`, which we did not unfold; the proof here uses only conditions 1 and 2 of admissibility directly and passes the whole structure to the hypothesis for $\mathfrak{r}$. The file of the input `levi_commute_unipotent_boundary` imports `Mathlib` twice (lines 1 and 3).
