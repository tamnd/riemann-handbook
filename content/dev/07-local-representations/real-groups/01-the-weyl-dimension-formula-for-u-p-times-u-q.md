---
title: The Weyl dimension formula for U(p) x U(q)
decls:
  - weylForK_closed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Weyl dimension formula for U(p) x U(q)

The maximal compact subgroup of the unitary group $U(p,q)$ is $U(p) \times U(q)$. Its irreducible representations, the $K$-types, organise every representation of $U(p,q)$ that we meet later in this chapter: the discrete series are found through their lowest $K$-type, and the formal degree is computed by an integral over $K$. This section proves the Weyl dimension formula for the $K$-types of $U(p) \times U(q)$. The result is used in the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), where the dimension of a $K$-type enters the normalisation of the formal degree.

For background on compact groups and highest weights, see [compact groups](/learn/representations/#compact-groups), [highest weights and branching](/learn/representations/#highest-weights-and-branching) and [unitary groups](/learn/groups/#unitary-groups).

### The group and its representations

Let $N \geq 1$ and let $\varepsilon : \{0, \dots, N-1\} \to \{+, -\}$ be a sign vector. Put $J_\varepsilon = \mathrm{diag}(\pm 1)$, with the sign $\varepsilon_a$ in position $a$. Let $p$ be the number of indices with $\varepsilon_a = +$ and $q = N - p$. Two indices $a, b$ are in the *same block* if $\varepsilon_a = \varepsilon_b$.

**Definition 2.1.1 (The compact group $K_\varepsilon$).** $K_\varepsilon$ is the group of unitary $N \times N$ matrices $g$ with $g J_\varepsilon = J_\varepsilon g$.

A matrix commutes with $J_\varepsilon$ exactly when its entries $g_{ab}$ vanish for $a, b$ in different blocks. So $K_\varepsilon$ is $U(p) \times U(q)$, embedded along the two blocks of indices. The blocks need not be intervals: for $\varepsilon = (+, -, +)$ the group is $U(2) \times U(1)$ acting on the coordinates $\{0, 2\}$ and $\{1\}$.

**Definition 2.1.2 (Unitary representation on a subset).** Let $H$ be a complex Hilbert space and $\sigma$ a map from $N \times N$ matrices to bounded operators on $H$. We say that $\sigma$ is a *unitary representation of $K_\varepsilon$* if $\sigma(1) = 1$, $\sigma(gh) = \sigma(g)\sigma(h)$ for $g, h \in K_\varepsilon$, each $\sigma(g)$ with $g \in K_\varepsilon$ is an isometry, and $g \mapsto \sigma(g)v$ is continuous on $K_\varepsilon$ for each $v \in H$.

The map $\sigma$ is defined on all matrices, but only its values on $K_\varepsilon$ matter. This form lets the same $\sigma$ serve for $U(p,q)$ and for its compact subgroup.

**Definition 2.1.3 (Weights and $K$-types).** Let $\mu \in \mathbb{R}^N$. A vector $v \in H$ is a *weight vector of weight $\mu$* if
$$\sigma(\mathrm{diag}(e^{i\theta_0}, \dots, e^{i\theta_{N-1}}))\, v = e^{i \sum_a \mu_a \theta_a}\, v \quad \text{for all } \theta \in \mathbb{R}^N.$$
Write $\mu \preceq \Lambda$ if $\Lambda - \mu$ is a sum, with coefficients in $\mathbb{N}$, of vectors $e_a - e_b$ with $a < b$ in the same block. A subspace $S \subseteq H$ is a *$K$-type of highest weight $\Lambda$* if: $S$ is finite-dimensional; $S$ is stable under $\sigma(K_\varepsilon)$ and has no stable subspace other than $0$ and $S$; $S$ contains a nonzero weight vector of weight $\Lambda$; and every weight $\mu$ of a nonzero weight vector in $S$ satisfies $\mu \preceq \Lambda$.

The order $\preceq$ uses only the roots of $K_\varepsilon$, the $e_a - e_b$ inside one block. So $\Lambda$ is the highest weight in the usual sense for the positive system $\{e_a - e_b : a < b \text{ in the same block}\}$.

**Definition 2.1.4 (Compact half sum).** For an index $a$ put
$$\rho_c(a) = \tfrac{1}{2}\big(\#\{b > a : \varepsilon_b = \varepsilon_a\} - \#\{b < a : \varepsilon_b = \varepsilon_a\}\big).$$

This is the half sum of the positive roots of $K_\varepsilon$. If $a < b$ are in the same block and $a', b'$ are their positions inside that block, then $\rho_c(a) - \rho_c(b) = b' - a'$.

### The theorem

We recall the classical formula. For a dominant integral weight $\Lambda$ of $U(N)$, that is $\Lambda \in \mathbb{Z}^N$ with $\Lambda_0 \geq \dots \geq \Lambda_{N-1}$, the irreducible representation of highest weight $\Lambda$ has dimension
$$\prod_{0 \leq a < b < N} \frac{\Lambda_a - \Lambda_b + b - a}{b - a}$$
(J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, §24.3). The denominator is $\prod_{a<b}(b-a) = \prod_{i < N} i!$.

**Theorem 2.1.5 (Weyl dimension formula for $K_\varepsilon$).** Let $\sigma$ be a unitary representation of $K_\varepsilon$ on a Hilbert space $H$, and let $S \subseteq H$ be a $K$-type of highest weight $\Lambda \in \mathbb{R}^N$. Then
$$\dim S = \frac{\displaystyle\prod_{a < b,\ \varepsilon_a = \varepsilon_b} \big((\Lambda + \rho_c)_a - (\Lambda + \rho_c)_b\big)}{\displaystyle\prod_{i < p} i! \ \prod_{i < q} i!}.$$

Lean: `weylForK_closed`.

The numerator runs over the pairs of indices in the same block. By the remark on $\rho_c$, the factor for a pair $a < b$ in one block is $\Lambda_a - \Lambda_b + (b' - a')$, so the formula is the product of the Weyl formula for $U(p)$ and the Weyl formula for $U(q)$. We do not assume that $\Lambda$ is integral or dominant: this follows from the hypotheses, as the proof shows.

We first state the case of one block.

**Theorem 2.1.6 (Weyl dimension formula for $U(N)$).** Let $\sigma$ be a unitary representation of $U(N)$ on a Hilbert space and $S$ a $K$-type of highest weight $\Lambda$ for $\varepsilon = (+, \dots, +)$. Then $\Lambda$ is integral and dominant, and $\dim S = \prod_{a<b} (\Lambda_a - \Lambda_b + b - a) / \prod_{i<N} i!$.

Lean: `weylForU_closed`.

*Proof.* There are two steps. First, the matrix coefficients of $S$ are polynomials in the entries of $g$ and in $\det g^{-1}$, and $U(N)$ is dense in $\mathrm{GL}_N(\mathbb{C})$ for the Zariski topology. So $S$ extends to a rational representation of $\mathrm{GL}_N(\mathbb{C})$ that is still irreducible. An irreducible rational representation with a highest weight vector of weight $\Lambda$ has $\Lambda$ integral and dominant, and it is isomorphic to the dual Weyl module $\nabla(\Lambda)$ twisted by a power of the determinant: the space of polynomials $f$ in an $N \times N$ matrix of variables that are homogeneous of degree $\Lambda_j - \Lambda_{N-1}$ in column $j$ and invariant under adding multiples of a column to a later column. So $\dim S = \dim \nabla(\Lambda - \Lambda_{N-1})$. Second, for a dominant $\nu \in \mathbb{N}^N$ one has
$$\dim \nabla(\nu) = \prod_{i<j} \frac{\nu_i - \nu_j + j - i}{j - i},$$
the Weyl formula for the dual Weyl module (J. C. Jantzen, *Representations of Algebraic Groups*, Part II, Chapter 2). The shift by $\Lambda_{N-1}$ does not change the differences $\Lambda_i - \Lambda_j$. $\square$

*Proof of the Weyl dimension formula for $K_\varepsilon$.* We reorder the indices so that the plus block comes first. This conjugates $K_\varepsilon$ to the block diagonal group $U(p) \times U(q)$ and permutes the weights; it changes neither $\dim S$ nor the formula, since the formula only uses pairs inside a block and their relative order. The diagonal torus of $K_\varepsilon$ is the product of the diagonal tori of $U(p)$ and $U(q)$, and a weight vector of weight $\Lambda$ is a weight vector for each factor, of weight $\Lambda^+ = (\Lambda_a)_{\varepsilon_a = +}$ and $\Lambda^- = (\Lambda_a)_{\varepsilon_a = -}$.

Next, $S$ contains an irreducible $U(p)$-subspace $X$ of highest weight $\Lambda^+$ and an irreducible $U(q)$-subspace $Y$ of highest weight $\Lambda^-$. To see this, take the $U(p)$-subspace generated by the highest weight vector and a minimal stable subspace in it that contains a vector of weight $\Lambda^+$; the order $\preceq$ restricted to the plus block shows that $\Lambda^+$ is its highest weight. The same holds for the minus block.

The actions of $U(p)$ and $U(q)$ on $S$ commute, and $S$ is irreducible for their product. By Schur's lemma, $S$ is isomorphic to $X \otimes Y$ as a representation of $U(p) \times U(q)$, so $\dim S = \dim X \cdot \dim Y$. Theorem (Weyl dimension formula for $U(N)$), applied to $U(p)$ and to $U(q)$, gives $\dim X$ and $\dim Y$. Their product is the stated formula, because for $a < b$ in one block $(\Lambda + \rho_c)_a - (\Lambda + \rho_c)_b = \Lambda_a - \Lambda_b + b' - a'$. $\square$

The general assembly from these steps is [Theorem](/entry/weyl-for-k-of/).

**Example 2.1.7.** Let $\varepsilon = (+, +, -)$, so $K_\varepsilon = U(2) \times U(1)$ and $\rho_c = (\tfrac12, -\tfrac12, 0)$. For $\Lambda = (3, 0, 5)$ the only pair in one block is $(0, 1)$, and $\dim S = (3 + \tfrac12 - 0 + \tfrac12)/(0! \cdot 1! \cdot 0!) = 4$. This is $\mathrm{Sym}^3 \mathbb{C}^2 \otimes \det^5$ of $U(2) \times U(1)$.

**Remark 2.1.8 (Formalization).** The statement is the unconditional form of an implication whose inputs (block reindexing, torus weights, uniqueness of weights, a minimal irreducible subspace, restriction of the order, and the two dimension steps) are all proved; the assembly is in WeylFormulaCompact/Assemble.lean. The half sum $\rho_c$ is defined twice, with the same text, in [StatementA.lean](lean:Formalism/RealPlaceAnalysis/StatementA.lean#L34) and [UpqRep.lean](lean:Formalism/PeriodIntegrals/UpqRep.lean#L201). The representation is a map on all matrices with conditions only on $K_\varepsilon$.
