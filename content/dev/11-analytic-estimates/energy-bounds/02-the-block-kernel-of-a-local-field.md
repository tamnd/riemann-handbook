---
title: The block kernel of a local field
decls:
  - Formalism.FourierDecayAlt.P.second_gram_and_vanishing
  - Formalism.FourierDecayAlt.Final.gram_determinant_dual_bound_a
  - Formalism.FourierDecayAlt.P.lattice_average_identity
  - Formalism.FourierDecayAlt.P.A5x9.bad_zero
  - Formalism.FourierDecayAlt.P.first_kernel_explicit_formula
  - Formalism.FourierDecayAlt.P.A5x8.first_kernel_formula_proof
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The block kernel of a local field

At a finite place the energy of a word is a sum over double cosets of unipotent groups, weighted by counts of isomorphisms of finite modules and by values of an additive character. This section defines that sum, the block kernel, and proves its two main properties: it is positive semidefinite on points of equal size, and it vanishes unless the last blocks of its two arguments are congruent modulo the ring of integers. It also proves the averaging identity behind the second property and an explicit formula for blocks of size one. Both properties enter [the local cores](/entry/local-cores/) of Section 1.

**Definition 3.2.1 (Local datum).** A *local datum* is a triple $(K, R, \psi)$ with the following properties. $K$ is a Hausdorff topological ring that is Artinian and reduced. $R \subseteq K$ is an open compact subring with an element $\varpi \in R$ such that for each $x \in K$ some $\varpi^m x$ lies in $R$. For each $x \in K$ there is $r \in R$ with $x + r$ a unit. The map $\psi : K \to \mathbb{C}^\times$ is an additive character with $\overline{\psi(x)} = \psi(-x)$, and it is self-dual: $\psi(aR) = 1$ if and only if $a \in R$.

A [[local field|J85FZEQG38]] with its ring of integers and a character of conductor $R$ is the main example. A finite product of local fields with the product ring and character is another one. Self-duality makes the Pontryagin dual of $K/R$ equal to $R$, which is what the finite Fourier analysis below uses.

**Definition 3.2.2 (Modulus).** For $x \in K$ let $|x|_K = [R : xR]/[xR : R]$, where $[A : B]$ is the relative index $[A : A \cap B]$ of two compact open subgroups. For a unit $x$ this is the normalized absolute value: $|x|_K = |R/xR|$ when $x \in R$.

**Definition 3.2.3 (Points, blocks and cosets).** A *point* of size $n$ is a pair $(s, t)$ with $s = (s_1, \dots, s_m)$ a list of positive integers with sum $n$ and $t_1, \dots, t_m \in K^\times$. Its matrix $\mathrm{pt}(s, t) \in \mathrm{GL}_n(K)$ is block diagonal, and block $i$ is $t_i$ times the antidiagonal permutation matrix of size $s_i$. For a point $(h, u)$ and $s \geq 1$, $t \in K^\times$, let $(h, u) \oplus (s, t)$ be the point with one more block, of size $s$ and value $t$. Let $N^-$ and $N^+$ be the lower and upper unipotent groups of $\mathrm{GL}_n(K)$, and $N^\pm(R)$ their integral points. For a point $w$ let $N^-_w$ be the group of $g \in N^-$ with $g\, \mathrm{pt}(w) = \mathrm{pt}(w)\, h$ for some $h \in N^-$. The *cosets* of $w$ are the pairs $q = (p_1, p_2)$ with $p_1 \in N^-_w / N^-_w(R)$ and $p_2 \in N^+ / N^+(R)$. The *orbit matrix* is $Z_q = p_1\, \mathrm{pt}(w)\, p_2$, and the *phase* is $\theta(q) = \psi(\sigma^-(p_1) + \sigma^+(p_2))$, where $\sigma^-$ and $\sigma^+$ are the sums of the entries just below and just above the diagonal.

**Definition 3.2.4 (Cokernel data).** For $Z \in \mathrm{GL}_n(K)$ with $Z \in M_n(R)$ let $C(Z) = R^n / Z R^n$, a finite $R$-module. Let $e_Z \in C(Z)$ be the class of the last basis vector, and let $\lambda_Z : C(Z) \to K/R$ send the class of $v$ to the last coordinate of $Z^{-1} v$ modulo $R$. For two such matrices let $I(Z, Z')$ be the set of $R$-isomorphisms $\varphi : C(Z) \to C(Z')$ with $\varphi(e_Z) = e_{Z'}$ and $\lambda_{Z'} \circ \varphi = \lambda_Z$.

**Definition 3.2.5 (Block kernel).** For points $w, w'$ of the same size $n$ let
$$\mathcal{K}(w, w') = \sum_{q,\, q'} \big[Z_q, Z_{q'} \in M_n(R)\big]\; |I(Z_q, Z_{q'})|\; \theta(q)\, \overline{\theta(q')},$$
a finite sum over the cosets of $w$ and of $w'$. For points $(h, u)$, $(h', u')$, a size $s \geq 1$ and $t, t' \in K^\times$ the *normalized kernel* is
$$N_s\big((h, u, t), (h', u', t')\big) = |t t'|_K^{s(s-1)/2}\; \mathcal{K}\big((h, u) \oplus (s, t),\; (h', u') \oplus (s, t')\big).$$

The count $|I(Z, Z')|$ is the number of ways to identify two cokernels with their marked vector and their last coordinate. It is the local analogue of an inner product of two lattice vectors. The factor $|tt'|^{s(s-1)/2}$ is the modulus of the last block on both sides.

**Theorem 3.2.6 (Gram and support property).** Let $(K, R, \psi)$ be a local datum.

1. Let $s \geq 1$ and let $F$ be a finite set of triples $(h, u, t)$ whose points $(h, u)$ have equal size. Then $N_s$ is positive semidefinite on $F$.
2. If $(h, u)$ and $(h', u')$ have equal size and $N_s((h, u, t), (h', u', t')) \neq 0$, then $t^{-1} - t'^{-1} \in R$.

Lean: `Formalism.FourierDecayAlt.P.second_gram_and_vanishing` (also `Formalism.FourierDecayAlt.Final.gram_determinant_dual_bound_a`, a second name).

The proof uses five facts. (G) The kernel $\mathcal{K}$ is positive semidefinite on each finite set of points. (M) $|x|_K > 0$ and $|xy|_K = |x|_K |y|_K$ for units. (T) For points of size $k + 1$, $\mathcal{K}$ equals the truncated kernel $\mathcal{K}_k$ defined below with $k$. (A) The averaging identity of the Lemma below. (E) If an isomorphism satisfies the truncation condition at level $\ell = |h|$ for the points $(h, u) \oplus (s, t)$ and $(h', u') \oplus (s, t')$, then $t^{-1} - t'^{-1} \in R$.

**Definition 3.2.7 (Truncated kernel).** For $v \in C(Z)$ and $j < n$ let $\lambda_{Z, j}(v)$ be coordinate $j$ of $Z^{-1}v$ modulo $R$. An isomorphism $\varphi : C(Z) \to C(Z')$ satisfies the *truncation condition at level $k$* if for each $j$ with $k \leq j < n$ there are $a_l \in R$ with
$$\lambda_{Z', j}(\varphi v) = \lambda_{Z, j}(v) + \sum_{j < l < n} a_l\, \lambda_{Z, l}(v) \quad \text{for all } v.$$
The *truncated kernel* $\mathcal{K}_k$ is $\mathcal{K}$ with $|I(Z, Z')|$ replaced by the number of $\varphi \in I(Z, Z')$ that satisfy the truncation condition at level $k$.

**Lemma 3.2.8 (Averaging identity).** Let $(h, u)$ and $(h', u')$ have the same size $\ell$, let $s \geq 1$ and $t, t' \in K^\times$, and let $k$ satisfy $\ell \leq k$ and $k + 2 \leq \ell + s$. Then $\mathcal{K}_{k + 1} = \mathcal{K}_k$ at the pair of points $(h, u) \oplus (s, t)$ and $(h', u') \oplus (s, t')$.

Lean: `Formalism.FourierDecayAlt.P.lattice_average_identity`.

*Proof.* For each pair of cosets, the condition at level $k$ is the condition at level $k + 1$ together with one more row, row $k$. So the count at level $k + 1$ is the count at level $k$ plus a correction $b(q, q')$, the number of isomorphisms that satisfy the condition at level $k + 1$ but not at level $k$. It is enough to show
$$\sum_{q, q'} \big[Z_q, Z_{q'} \text{ integral}\big]\; b(q, q')\; \theta(q)\, \overline{\theta(q')} = 0.$$
Since $k$ lies inside the last block ($\ell \leq k < \ell + s - 1$), the coset map $q \mapsto \kappa(q)$ to a coarser quotient of the upper unipotent group forgets exactly the entry that row $k$ sees. On each fibre of $\kappa$ the integrality conditions and the correction $b$ are constant, while the phase runs through a nontrivial character of a finite group $R$-module. By self-duality of $\psi$ the sum of the phases over the fibre is zero. Adding over the fibres gives the claim. $\square$

**Lemma 3.2.9 (Vanishing of the correction).** In the setting of the Lemma above, the phase weighted sum of the correction $b$ over all pairs of cosets is zero.

Lean: `Formalism.FourierDecayAlt.P.A5x9.bad_zero`.

*Proof.* This is the fibrewise argument in the proof of the Lemma above: the sum over each fibre of $\kappa$ vanishes, and the total is the sum over the fibres. $\square$

*Proof of the Theorem.* For part 1, put $a(h, u, t) = |t|_K^{s(s-1)/2}$. By (M), $a$ is real and $|t t'|_K^{s(s-1)/2} = a(h, u, t)\, a(h', u', t')$. So $N_s$ is the kernel $\mathcal{K}$ on the points $(h, u) \oplus (s, t)$, scaled by $a(x) a(y)$. By (G) and the real scaling rule of [the closure rules](/entry/local-cores/), $N_s$ is positive semidefinite. For part 2, the two points $(h, u) \oplus (s, t)$ and $(h', u') \oplus (s, t')$ have size $\ell + s$, where $\ell$ is the common size of $h$ and $h'$. By (T) with $k = \ell + s - 1$, $\mathcal{K} = \mathcal{K}_{\ell + s - 1}$ there. The averaging identity, applied for $k = \ell + s - 2, \ell + s - 3, \dots, \ell$, gives $\mathcal{K}_{\ell + s - 1} = \mathcal{K}_\ell$. If $N_s \neq 0$, then $\mathcal{K}_\ell \neq 0$, so some isomorphism satisfies the truncation condition at level $\ell$. By (E), $t^{-1} - t'^{-1} \in R$. $\square$

For blocks of size one the kernel has a closed form. This form feeds the Parseval identity for one block in [the local cores](/entry/local-cores/).

**Theorem 3.2.10 (Single block formula).** Let $(K, R, \psi)$ be a local datum, let $(h, u)$ and $(h', u')$ be points, and let $c \in K^\times$. Then $N_1((h, u, c), (h', u', c))$ equals
$$\sum_{q, q'} \big[Z_q, Z_{q'} \text{ integral}\big]\; S(Z_q, Z_{q'}, c)\; \theta(q)\, \overline{\theta(q')},$$
where the cosets are those of $(h, u) \oplus (1, c)$ and $(h', u') \oplus (1, c)$, and
$$\begin{aligned} S(Z, Z', c) = \sum_{\vartheta} \sum_{\alpha} \sum_{\beta} \psi\big(&\alpha(e_Z - \vartheta^{-1} e_{Z'}) \\ &+ \lambda_Z(\beta) - \lambda_{Z'}(\vartheta \beta)\big). \end{aligned}$$
Here $\vartheta$ runs over all $R$-isomorphisms $C(Z) \to C(Z')$, $\alpha$ over $\mathrm{Hom}_R(C(Z), K/R)$, and $\beta$ over the $\beta \in C(Z)$ with $\alpha(\beta) = -[c]$, the class of $-c$ in $K/R$ read through the identification of $K/R$ with its dual.

Lean: `Formalism.FourierDecayAlt.P.A5x8.first_kernel_formula_proof` (also `Formalism.FourierDecayAlt.P.first_kernel_explicit_formula`, a second name).

*Proof (outline).* For $s = 1$ the scaling factor is $|c^2|_K^0 = 1$, so $N_1$ is the block kernel itself. One fixes a section of the coset projection for the points with last block $(1, c)$ and writes the block kernel as a sum over that section. The count $|I(Z, Z')|$ is then expanded by finite Fourier analysis on $C(Z)$. The condition $\varphi(e_Z) = e_{Z'}$ is detected by the sum over $\alpha$ of $\psi(\alpha(e_Z - \vartheta^{-1}e_{Z'}))$, and the condition $\lambda_{Z'} \circ \vartheta = \lambda_Z$ by the sum over $\beta$ of $\psi(\lambda_Z(\beta) - \lambda_{Z'}(\vartheta\beta))$. The constraint $\alpha(\beta) = -[c]$ records the last block, whose coordinate is $c$. This is why $\vartheta$ runs over all isomorphisms: the characters cut out the subset $I(Z, Z')$. $\square$

**Remark 3.2.11 (Formalization).** The statements are `A5.A2`, `A5.AvgClaim` and `A5.SingleBlockFormula` in [BlockKernelPropertiesOfSteps.lean](lean:Formalism/HermitianCurvature/BlockKernelPropertiesOfSteps.lean#L345). `second_gram_and_vanishing` ([SecondVanishingOffRing.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SecondVanishingOffRing.lean#L11)) applies `second_gram_vanishing_of_parts` to `kernel_gram_property`, `modulus_positive_multiplicative`, `tripleForm`, `lattice_average_identity` and `triple_form_end_identity`, which are facts (G), (M), (T), (A) and (E). We opened the statements of these five facts, not the proofs of (G), (T) and (E). The second name `gram_determinant_dual_bound_a` sits at line 1007 of HeisenbergConjugationMeasurePreserving.lean, a file whose name does not describe its content. `lattice_average_identity` is at [LatticeAverageIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/LatticeAverageIdentity.lean#L1824); it uses `bad_zero` (line 1741), which is proved fibre by fibre by `fibre_zero` (line 1700) over the map `kap` to `upUniG/PPsub`. The correction count is `badN`; we describe it by its role and did not unfold it. `first_kernel_formula_proof` is at [FirstKernelExplicitFormula.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/FirstKernelExplicitFormula.lean#L1892) and goes through `Kp_eq_section`; we give its proof in outline only, and the identification of $K/R$ with its dual in the constraint on $\beta$ is our reading of `singleBlockInner`.
