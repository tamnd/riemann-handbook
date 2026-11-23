---
title: The Weyl dimension formula for the maximal compact subgroup of U(p, q)
decls:
  - weylForK_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Weyl dimension formula for the maximal compact subgroup of $U(p, q)$

This section proves the Weyl dimension formula for the maximal compact subgroup $K = U(p) \times U(q)$ of an indefinite unitary group $U(p, q)$, from the same formula for $U(N)$. The $K$-types of a representation of $U(p, q)$ have dimensions given by a product over the compact positive roots. The formula is used to [close the dimension formula for $K$](/entry/weyl-for-k-closed/), and through it in the dimension counts of the later chapters. For the background see [unitary groups](/learn/groups/#unitary-groups) and [highest weights and branching](/learn/representations/#highest-weights-and-branching).

### The group $K$ and its weights

Fix $N \geq 0$ and a sign vector $\varepsilon : \{0, \dots, N-1\} \to \{+, -\}$. Let $J_\varepsilon$ be the diagonal matrix with entry $1$ at the indices $a$ with $\varepsilon_a = +$ and $-1$ at the others. Let $p$ and $q$ be the numbers of plus and minus signs, so $p + q = N$.

**Definition 4.2.1 (The compact group $K_\varepsilon$).** $K_\varepsilon$ is the set of unitary $N \times N$ complex matrices $g$ with $g J_\varepsilon = J_\varepsilon g$.

So $K_\varepsilon$ is the group of unitary matrices that preserve the two coordinate subspaces given by the signs. It is isomorphic to $U(p) \times U(q)$, and it is the maximal compact subgroup of the unitary group of $J_\varepsilon$. The signs need not come in two blocks; the indices of each sign can be interleaved.

Let $H$ be a complex inner product space, and let $\sigma$ be a map from $N \times N$ complex matrices to bounded operators on $H$.

**Definition 4.2.2 (Unitary representation on a set).** $\sigma$ is a *unitary representation on* a set $G$ of matrices if $\sigma(1) = 1$, $\sigma(ab) = \sigma(a) \sigma(b)$ for $a, b \in G$, $\|\sigma(g) v\| = \|v\|$ for $g \in G$ and $v \in H$, and $g \mapsto \sigma(g) v$ is continuous on $G$ for each $v \in H$.

For $\theta \in \mathbb{R}^N$ write $t(\theta)$ for the diagonal matrix with entries $e^{i \theta_a}$. It lies in $K_\varepsilon$.

**Definition 4.2.3 (Weight vector).** Let $\mu \in \mathbb{R}^N$. A vector $v \in H$ has *weight* $\mu$ if $\sigma(t(\theta)) v = e^{i \langle \mu, \theta \rangle} v$ for all $\theta \in \mathbb{R}^N$, where $\langle \mu, \theta \rangle = \sum_a \mu_a \theta_a$.

Let $e_a$ be the standard basis of $\mathbb{R}^N$. A pair $a < b$ with $\varepsilon_a = \varepsilon_b$ is a *compact positive root*, with root vector $e_a - e_b$.

**Definition 4.2.4 (Compact dominance).** For $\mu, \Lambda \in \mathbb{R}^N$, $\mu$ is *below* $\Lambda$ if
$$\Lambda - \mu = \sum_{a, b} c_{ab}\, (e_a - e_b)$$
with $c_{ab} \in \mathbb{Z}_{\geq 0}$ and $c_{ab} = 0$ unless $a < b$ and $\varepsilon_a = \varepsilon_b$.

**Definition 4.2.5 ($K$-type of highest weight $\Lambda$).** A subspace $S \subseteq H$ is a *$K$-type of highest weight* $\Lambda$ if

1. $S$ is finite-dimensional and $\sigma(g) S \subseteq S$ for every $g \in K_\varepsilon$;
2. the only $K_\varepsilon$-stable subspaces of $S$ are $0$ and $S$;
3. $S$ contains a nonzero vector of weight $\Lambda$;
4. every weight $\mu$ of a nonzero vector of $S$ is below $\Lambda$.

**Definition 4.2.6 (Half sum of compact roots).** Put
$$\rho_c(a) = \tfrac{1}{2} \big( \#\{ b > a : \varepsilon_b = \varepsilon_a \} - \#\{ b < a : \varepsilon_b = \varepsilon_a \} \big).$$

For the all-plus sign vector, $\rho_c(a) = (N - 1)/2 - a$, and $\rho_c(a) - \rho_c(b) = b - a$.

### The formula for $U(N)$

**Definition 4.2.7 (Weyl formula for $U(N)$).** The *Weyl formula for $U(N)$* is the statement: for every $N$, every $\Lambda \in \mathbb{R}^N$, every inner product space $H$ and every $\sigma$ that is a unitary representation on $K_+ = U(N)$, every $K$-type $S$ of highest weight $\Lambda$ for the all-plus sign vector has
$$\dim S = \frac{\prod_{a < b} (\Lambda_a - \Lambda_b + b - a)}{\prod_{i=0}^{N-1} i!}.$$

This is the classical Weyl dimension formula, as in Goodman and Wallach, Chapter 7.

### The theorem

**Theorem 4.2.8 (Weyl formula for $K$).** Assume the Weyl formula for $U(N)$. Let $N \geq 0$, let $\varepsilon$ be a sign vector with $p$ plus signs and $q$ minus signs, let $\Lambda \in \mathbb{R}^N$, let $H$ be a complex inner product space, and let $\sigma$ be a unitary representation on $K_\varepsilon$. Then every $K$-type $S$ of highest weight $\Lambda$ has
$$\dim S = \frac{\prod_{a < b,\ \varepsilon_a = \varepsilon_b} \big( (\Lambda + \rho_c)_a - (\Lambda + \rho_c)_b \big)}{\prod_{i=0}^{p-1} i! \cdot \prod_{i=0}^{q-1} i!}.$$

Lean: `weylForK_of`.

*Proof.* This is a reduction of $K_\varepsilon$ to a product of two unitary groups, followed by the formula for each factor. Let $i_+ : U(p) \to K_\varepsilon$ and $i_- : U(q) \to K_\varepsilon$ be the embeddings through the plus indices and the minus indices, each taken in increasing order. The proof applies an assembly lemma to eight proved results. In order, they say the following.

1. The images of $i_+$ and $i_-$ lie in $K_\varepsilon$ and commute, every $g \in K_\varepsilon$ is a product $i_+(h)\, i_-(h')$, and a unitary representation on $K_\varepsilon$ restricts to unitary representations of $U(p)$ and $U(q)$ through $i_+$ and $i_-$.
2. A sum over all indices is the sum over the plus indices plus the sum over the minus indices, and $i_+$ and $i_-$ send diagonal matrices $t(\theta)$ to diagonal matrices $t(\theta')$, with $\theta'$ equal to $\theta$ on the indices of that sign and $0$ on the others.
3. A nonzero finite-dimensional subspace that is stable under the diagonal matrices contains a nonzero weight vector.
4. For $U(n)$, a nonzero vector has at most one weight.
5. For $U(p)$, a finite-dimensional stable subspace $S$ with a nonzero vector of weight $\mu$ contains an irreducible stable subspace $X$ that has a nonzero vector of weight $\mu$.
6. If $\mu$ is below $\Lambda$ for $\varepsilon$, then the restriction of $\mu$ to the plus indices is below the restriction of $\Lambda$ for $U(p)$, and the same holds for the minus indices and $U(q)$.
7. Let $U(p)$ and $U(q)$ act on $S$ by commuting unitary representations, and let $S$ be finite-dimensional and irreducible for the two actions together. If $X \subseteq S$ is a nonzero irreducible stable subspace for $U(p)$ and $Y \subseteq S$ is one for $U(q)$, then $\dim S = \dim X \cdot \dim Y$.
8. The right side of the theorem is the product of the right side of the formula for $U(p)$ at the restriction of $\Lambda$ to the plus indices and the right side of the formula for $U(q)$ at the restriction to the minus indices.

The first six results show that $S$ contains a $K$-type $X$ of $U(p)$ whose highest weight is the restriction of $\Lambda$ to the plus indices, and a $K$-type $Y$ of $U(q)$ whose highest weight is the restriction to the minus indices. Result 7 gives $\dim S = \dim X \cdot \dim Y$. The formula for $U(N)$, at $N = p$ and at $N = q$, gives $\dim X$ and $\dim Y$. Result 8 identifies the product with the right side. $\square$

**Example 4.2.9.** Take $N = 2$ with $\varepsilon = (+, -)$. There is no compact positive root, so both products in the numerator are empty, and the denominator is $0! \cdot 0! = 1$. The formula gives $\dim S = 1$. This is right: $K_\varepsilon$ is the diagonal torus $U(1) \times U(1)$, and its irreducible representations are characters.

**Example 4.2.10.** Take $N = 3$ with $\varepsilon = (+, -, +)$. The only compact positive root is $(0, 2)$. Here $\rho_c(0) = 1/2$ and $\rho_c(2) = -1/2$, and $\rho_c(1) = 0$. The formula gives $\dim S = \Lambda_0 - \Lambda_2 + 1$. This is the dimension of the representation of $U(2)$ on the indices $0$ and $2$ with highest weight $(\Lambda_0, \Lambda_2)$, tensored with a character of the $U(1)$ on index $1$.

**Remark 4.2.11.** The weight $\Lambda$ is a real vector, not an integral one. The hypotheses force $\Lambda$ to be integral and dominant for the compact roots, since it is the weight of a nonzero vector in a finite-dimensional representation of the torus and is the highest weight. The theorem does not state this.

**Remark 4.2.12 (Formalization).** The weight $\Lambda$ is taken in $\mathbb{R}^N$, and the space $H$ is an inner product space that need not be complete; see [WeylForK.lean](lean:Formalism/PeriodIntegrals/WeylForK.lean#L13). Neither matters for the conclusion, since $S$ is finite-dimensional. The dimension is the rank of $S$ as a complex vector space, read as a real number. The eight proved results of the proof were not unfolded beyond their statements, which the text gives in mathematical terms. The theorem is in [WeylForK.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/WeylForK.lean#L7).
