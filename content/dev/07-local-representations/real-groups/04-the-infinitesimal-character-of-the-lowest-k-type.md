---
title: The infinitesimal character of the lowest K-type
decls:
  - CompanionTheory.D.DSIC.hAlgCore
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The infinitesimal character of the lowest K-type

A discrete series representation of $U(p,q)$ with Harish-Chandra parameter $\lambda$ has infinitesimal character $\lambda$. This section proves an algebraic form of that fact. We start from a unitary module over the Lie algebra $\mathfrak{gl}_n$ and a vector $v$ of the lowest $K$-type, and we show that the Capelli (quantum) determinant acts on $v$ by the scalar that $\lambda$ predicts. The tools are the Koszul complex of the abelian subalgebra $\mathfrak{p}^+$, the theorem of Casselman and Osborne, and a norm inequality that singles out one term of the complex. The result is used in the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/), where it identifies the central character of a discrete series.

Background: [representations of real groups](/learn/representations/#representations-of-real-groups), [discrete series](/learn/representations/#discrete-series), [[Harish-Chandra module|2MKHH636C3]].

### Unitary modules and the quantum determinant

Fix $n \geq 0$ and a sign vector $\varepsilon \in \{+, -\}^n$, with $p$ plus signs and $q$ minus signs. As in [the Weyl dimension formula](/entry/weyl-for-k-closed/), two indices are in the same block if they have the same sign.

**Definition 2.4.1 (Unitary $\mathfrak{gl}_n$-module of type $\varepsilon$).** Let $V$ be a complex inner product space and $E_{ab}$, for $a, b < n$, linear operators on $V$ with
$$[E_{ab}, E_{cd}] = \delta_{bc} E_{ad} - \delta_{da} E_{cb}.$$
The module is *unitary of type $\varepsilon$* if $\langle E_{ab} x, y \rangle = s_{ab} \langle x, E_{ba} y \rangle$ for all $x, y$, where $s_{ab} = 1$ if $a, b$ are in the same block and $s_{ab} = -1$ otherwise.

This is the derivative of a unitary representation of $U(p,q)$ on its smooth vectors, written in the basis $E_{ab}$ of the complexified Lie algebra $\mathfrak{gl}_n(\mathbb{C})$. The compact part $\mathfrak{k}$ is spanned by the $E_{ab}$ with $a, b$ in the same block; the rest, $\mathfrak{p}$, has the sign $-1$.

**Definition 2.4.2 ($K$-highest vectors).** A vector $w$ is *$K$-highest of weight $\mu \in \mathbb{R}^n$* if $E_{aa} w = \mu_a w$ for all $a$ and $E_{ab} w = 0$ for all $a < b$ in the same block.

Let $\rho_c$ be the compact half sum of [the Weyl dimension formula](/entry/weyl-for-k-closed/), and $\rho_n(a) = \tfrac12(\#\{b > a\text{ in the other block}\} - \#\{b < a\text{ in the other block}\})$ the noncompact one.

**Definition 2.4.3 (Harish-Chandra parameter, lowest $K$-type, Vogan norm).** A *Harish-Chandra parameter* is $\lambda \in \mathbb{R}^n$, strictly decreasing, with $\lambda_a - \tfrac{n-1}{2} \in \mathbb{Z}$ for all $a$. Its *lowest $K$-type weight* is $\Lambda = \lambda + \rho_n - \rho_c$. The *Vogan norm* of a weight $\mu$ is $\|\mu\|_V^2 = |\mu + 2\rho_c|^2$, the Euclidean norm.

For the discrete series with parameter $\lambda$, $\Lambda$ is the highest weight of the lowest $K$-type, the $K$-type of least Vogan norm; this is part of Blattner's formula, proved by H. Hecht and W. Schmid (Invent. Math. 31 (1975)).

**Definition 2.4.4 (Quantum determinant).** For $u \in \mathbb{C}$ let $T(u)_{ab} = u\,\delta_{ab} + E_{ab}$. For sequences $a, b$ of $t$ indices, the *quantum minor* is
$$C_{a,b}(u) = \sum_{\sigma \in S_t} \mathrm{sgn}(\sigma)\, T(u)_{a_{\sigma 0}, b_0}\, T(u - 1)_{a_{\sigma 1}, b_1} \cdots T(u - t + 1)_{a_{\sigma(t-1)}, b_{t-1}},$$
an ordered product. The *quantum determinant* is $\mathrm{qdet}(u) = C_{\mathrm{id}, \mathrm{id}}(u)$, with $t = n$.

The coefficients of $\mathrm{qdet}(u)$, as a polynomial in $u$, are central in the enveloping algebra; they are the Capelli elements. On a vector $w$ of weight $\mu$ killed by all $E_{ab}$ with $a < b$, the rightmost factor acts first and only the identity permutation survives, so $\mathrm{qdet}(u) w = \prod_k (u - k + \mu_k) w$. With $u = Y + \tfrac{n-1}{2}$ this is $\prod_k (Y + (\mu + \rho)_k) w$, where $\rho_k = \tfrac{n-1}{2} - k$. So the conclusion of the theorem below says that $v$ has infinitesimal character $\lambda$ in the usual $\rho$-shifted normalisation.

### The theorem

Harish-Chandra proved that a discrete series representation with parameter $\lambda$ has infinitesimal character $\chi_\lambda$ (Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966)). We prove the following algebraic form for $U(p,q)$, in which the group does not appear.

**Theorem 2.4.5 (Infinitesimal character of the lowest $K$-type).** Let $\lambda$ be a Harish-Chandra parameter and $\Lambda = \lambda + \rho_n - \rho_c$. Let $V$ be a unitary $\mathfrak{gl}_n$-module of type $\varepsilon$, let $v \in V$ be $K$-highest of weight $\Lambda$, and let $S \subseteq V$ be a finite-dimensional subspace with $v \in S$ and $E_{ab} S \subseteq S$ for all $a, b$ in the same block. Assume that $\|\Lambda\|_V \leq \|\mu\|_V$ whenever some nonzero $x \in V$ is $K$-highest of weight $\mu$. Then for all $Y \in \mathbb{C}$,
$$\mathrm{qdet}\Big(Y + \frac{n-1}{2}\Big) v = \prod_{s < n} (Y + \lambda_s)\, v.$$

Lean: `CompanionTheory.D.DSIC.hAlgCore`.

The vector $v$ is not assumed to be nonzero; for $v = 0$ the statement is empty.

### The Koszul complex of $\mathfrak{p}^+$

Let $P$ be the set of pairs $i = (a, b)$ with $\varepsilon_a = +$ and $\varepsilon_b = -$. The operators $E_i = E_{ab}$, $i \in P$, commute with each other: they span the abelian subalgebra $\mathfrak{p}^+$. Order $P$ by $(a, b) \mapsto a n + b$.

**Definition 2.4.6 (Chains).** A *chain* is a function $x$ from the finite subsets of $P$ to $V$; it is a model of $\Lambda(\mathfrak{p}^+) \otimes V$. It has *degree $j$* if $x(A) = 0$ whenever $|A| \neq j$. For $i \in P$ let $\mathrm{sg}(i, A) = (-1)^{\#\{j \in A : j < i\}}$, and define
$$(\mathrm{ann}_i x)(A) = \begin{cases} \mathrm{sg}(i, A)\, x(A \cup \{i\}) & i \notin A, \\ 0 & i \in A, \end{cases} \qquad (\mathrm{cre}_i x)(A) = \begin{cases} \mathrm{sg}(i, A)\, x(A \smallsetminus \{i\}) & i \in A, \\ 0 & i \notin A. \end{cases}$$
The *boundary* is $\partial = \sum_{i \in P} E_i\, \mathrm{ann}_i$ and the *coboundary* is $\delta = \sum_{(a,b) \in P} E_{ba}\, \mathrm{cre}_{(a,b)}$. Let $F_{cd} = E_{cd} + G_{cd}$, where $G_{cd}$ is the action of $E_{cd}$ on the exterior factor (a combination of $\mathrm{cre}_i\, \mathrm{ann}_j$). Put $\langle x, y \rangle = \sum_A \langle x(A), y(A) \rangle$.

So $\partial$ is the Koszul differential computing the homology of $\mathfrak{p}^+$ with coefficients in $V$, and the $F_{cd}$ with $c, d$ in one block give the diagonal action of $\mathfrak{k}$ on chains. For $A \subseteq P$ let $\mathrm{wt}(A)_c = \#\{(a,b) \in A : a = c\} - \#\{(a,b) \in A : b = c\}$, the weight of $\bigwedge_{i \in A} E_i$. Let $A_1 = \{(a, b) \in P : b < a\}$ and $\gamma = \Lambda + \mathrm{wt}(A_1)$. Finally let $\zeta(u) = C^-(u)\, C^+(u - q)$, where $C^\pm$ is the quantum minor of the operators $F$ on the indices of the $\pm$ block, in increasing order.

**Lemma 2.4.7 (Ingredients).** Let $V$ be a $\mathfrak{gl}_n$-module as above.

1. (Casselman-Osborne.) If $x$ has degree $j$ and $\partial x = 0$, then for every $u$ there is $w$ of degree $j + 1$ with $\mathrm{qdet}(u)\, x - \zeta(u)\, x = \partial w$.
2. If $x$ is a chain that is $K$-highest of weight $\gamma$ for the operators $F$, then $\zeta(Y + \tfrac{n-1}{2})\, x = \prod_s (Y + \lambda_s)\, x$.
3. If $x \neq 0$ is $K$-highest of weight $\gamma'$ for the $F$, then some $A$ has $x(A) \neq 0$ and $x(A)$ is $K$-highest of weight $\gamma' - \mathrm{wt}(A)$ for the $E$.
4. If $\lambda$ is strictly decreasing and $A \neq A_1$, then $\|\gamma - \mathrm{wt}(A)\|_V < \|\Lambda\|_V$.
5. If $V$ is unitary of type $\varepsilon$, then $\langle \partial w, x \rangle = -\langle w, \delta x \rangle$.
6. Under the hypotheses of the theorem except the norm condition, there is a chain $c$ of degree $|A_1|$, $K$-highest of weight $\gamma$ for the $F$, with $c(A_1) = v$.

Lean: `CompanionTheory.D.DSIC.hCO`, `CompanionTheory.D.DSIC.hZetaHW`, `CompanionTheory.D.DSIC.hWLem`, `CompanionTheory.D.DSIC.hNormLt`, `CompanionTheory.D.DSIC.hAdj`, `CompanionTheory.D.DSIC.hPRV`.

*Proof.* Part 1 is the theorem of Casselman and Osborne for $\mathfrak{p}^+$ in the form of a chain homotopy: modulo the ideal generated by $\mathfrak{p}^+$, the quantum determinant equals the product of the block Capelli determinants (the Harish-Chandra projection of a central element to $\mathfrak{k}$), and this congruence is lifted to chains with the exactness of the Koszul complex and a Verma module argument. Part 2 is the computation of the block determinants on a highest weight vector, done as for $\mathrm{qdet}$ above; the shift by $q$ in $\zeta$ and the shift $\gamma = \Lambda + \mathrm{wt}(A_1)$ combine to give $\lambda$. Part 3 follows from $F = E + G$ and the formulas for $G$: the diagonal operator $G_{cc}$ multiplies the component at $A$ by $\mathrm{wt}(A)_c$, and one takes a nonzero component that is maximal for the order of weights. Part 4 is an inequality between explicit vectors in $\mathbb{R}^n$. Part 5 is the unitarity: $E_{ab}^* = -E_{ba}$ for $(a,b) \in P$, and $\mathrm{ann}_i$ and $\mathrm{cre}_i$ are adjoint. Part 6 is a Parthasarathy-Ranga Rao-Varadarajan type construction: the tensor product of the $K$-type of $v$ with $\bigwedge^{|A_1|} \mathfrak{p}^+$ contains a highest weight vector of weight $\gamma$ whose $A_1$-component is $v$. $\square$

### The proof

*Proof of the theorem.* Fix $Y$, put $u = Y + \tfrac{n-1}{2}$ and $s = \prod_s (Y + \lambda_s)$.

First, a vanishing lemma: a chain $y$ that is $K$-highest of weight $\gamma$ for the $F$ and has $y(A_1) = 0$ is zero. Otherwise part 3 gives $A$ with $y(A) \neq 0$ and $y(A)$ $K$-highest of weight $\gamma - \mathrm{wt}(A)$. Then $A \neq A_1$, and the norm hypothesis gives $\|\Lambda\|_V \leq \|\gamma - \mathrm{wt}(A)\|_V$. This contradicts part 4, since a Harish-Chandra parameter is strictly decreasing.

Second, take $c$ from part 6. The boundary $\partial$ commutes with the action of $\mathfrak{k}$, so $\partial c$ is $K$-highest of weight $\gamma$; it has degree $|A_1| - 1$, so $(\partial c)(A_1) = 0$. By the vanishing lemma, $\partial c = 0$.

Third, part 1 gives $w$ with $\mathrm{qdet}(u) c - \zeta(u) c = \partial w$, and part 2 gives $\zeta(u) c = s\, c$. So $T c = \partial w$, where $T = \mathrm{qdet}(u) - s$ acts on each component.

Fourth, $T$ commutes with the $F$, because $\mathrm{qdet}(u)$ is central and the $G$ act only on the exterior factor. So $\delta T c$ is $K$-highest of weight $\gamma$ (the coboundary also commutes with $\mathfrak{k}$), and it has degree $|A_1| + 1$. By the vanishing lemma, $\delta T c = 0$. Part 5 gives
$$\langle T c, T c \rangle = \langle \partial w, T c \rangle = -\langle w, \delta T c \rangle = 0.$$
So $T c = 0$, and its component at $A_1$ is $(\mathrm{qdet}(u) - s) v = 0$. $\square$

**Remark 2.4.8 (Formalization).** The statement is about an abstract inner product space with operators, not about a group. It is used through a second form, restricted to a $\mathfrak{gl}_n$-stable subspace, and then for the $K$-finite smooth vectors of a discrete series in [DiscreteSeriesInfinitesimalCharacter.lean](lean:CompanionTheory/HarishChandraModules/LowKTypeMultiplicity/DiscreteSeriesCharacters/DiscreteSeriesInfinitesimalCharacter.lean#L54). The finite-dimensional subspace $S$ only serves part 6. The proofs of the six ingredients sit in other modules; we have read their statements and the assembly, not every proof, so the proof sketches of the lemma describe the mathematics of the statements rather than the formal proofs. The weights $\rho_c$, $\Lambda$ and the Vogan norm are defined in [UpqRep.lean](lean:Formalism/PeriodIntegrals/UpqRep.lean#L201), and $\rho_c$ has a second copy elsewhere.
