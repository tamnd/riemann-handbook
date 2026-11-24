---
title: Lie algebra homology and the theorem of Casselman and Osborne
decls:
  - GlobalTheory.T.pair_multiplicity_generic_unitary
  - GlobalTheory.CompanionTheory.PairMult.COU.genCOU2
  - GlobalTheory.T.action_unipotent_radical_real
  - GlobalTheory.CompanionTheory.PairBridge.actUU
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lie algebra homology and the theorem of Casselman and Osborne

Let $\mathfrak{q} = \mathfrak{l} + \mathfrak{u}$ be a parabolic subalgebra of a reductive Lie algebra $\mathfrak{g}$ and $V$ a $\mathfrak{g}$-module. The center of $U(\mathfrak{g})$ acts on the homology $H_*(\mathfrak{u}, V)$, and the theorem of Casselman and Osborne says that it acts there through the Harish-Chandra projection to $U(\mathfrak{l})$. This section proves the form of this theorem that the real descent of Volume 8 uses. The group is $\mathrm{GL}_n(\mathbb{C})$ seen as a real group, the parabolic is a block upper triangular parabolic, and the homology class is the top class of the compact part of $\mathfrak{u}$. The result is one of the three parts of [Theorem 7.1.10 of Volume 8](/entry/injective-decomposition-action-holds/), which serves the step [EveryCharacter](/step/every-character/). For background see [representations of real groups](/learn/representations/#representations-of-real-groups).

### Pair modules and chains

Fix $n \geq 0$. Indices $a, b, c$ run over $\{0, \dots, n-1\}$.

**Definition 1.1.1 (Pair module).** A *pair module* is a complex vector space $V$ with two families of operators $E^1_{ab}$ and $E^2_{ab}$ such that each family satisfies the relations of $\mathfrak{gl}_n$,
$$[E_{ab}, E_{cd}] = \delta_{bc} E_{ad} - \delta_{da} E_{cb},$$
and every $E^1_{ab}$ commutes with every $E^2_{cd}$. We put $k_{ab} = E^1_{ab} + E^2_{ab}$ and $p_{ab} = E^1_{ab} - E^2_{ab}$.

A pair module is a module over $\mathfrak{gl}_n \oplus \mathfrak{gl}_n$, the complexified Lie algebra of $\mathrm{GL}_n(\mathbb{C})$ as a real group. The $k_{ab}$ span the diagonal copy of $\mathfrak{gl}_n$, which plays the part of the complexified Lie algebra of the maximal compact subgroup $U(n)$, and the $p_{ab}$ span its complement.

**Definition 1.1.2 (Letters and chains).** A *letter* is a triple $l = (s, a, b)$ with $s \in \{k, p\}$ and $a < b$. Its operator on a pair module is $x_l = k_{ab}$ if $s = k$ and $x_l = p_{ab}$ if $s = p$. A *chain* of degree $j$ with coefficients in $V$ is a finite sum $\sum_A e_A \otimes v_A$ over sets $A$ of $j$ letters, where $e_A$ is the wedge product of the letters of $A$ in a fixed order. For a letter $l$ we write $\iota_l$ for the contraction with $l$ and $\varepsilon_l$ for the exterior product with $l$.

The letters form a basis of $\mathfrak{n} \oplus \mathfrak{n}$, where $\mathfrak{n}$ is the algebra of strictly upper triangular matrices, and the chains are $\Lambda(\mathfrak{n} \oplus \mathfrak{n}) \otimes V$. Two letters $l = (s, a, b)$ and $m = (s', b, c)$ have the bracket $l * m = (s \oplus s', a, c)$, where $k \oplus k = p \oplus p = k$ and $k \oplus p = p \oplus k = p$. This is the bracket of $\mathfrak{gl}_n \oplus \mathfrak{gl}_n$: for example $[p_{ab}, p_{bc}] = E^1_{ac} + E^2_{ac} = k_{ac}$.

**Definition 1.1.3 (Boundary).** Let $S$ be a set of letters that is closed under the bracket. The *boundary* on $S$-chains is
$$\partial_S = \sum_{l \in S} x_l \, \iota_l + \sum_{l, m \in S,\ l * m \text{ defined}} \varepsilon_{l * m} \, \iota_m \, \iota_l .$$
A chain is *$S$-supported* if every letter in it lies in $S$.

This is the Chevalley-Eilenberg boundary of the Lie algebra spanned by $S$, with coefficients in $V$. Its homology is the Lie algebra homology $H_*(\mathfrak{s}, V)$.

**Definition 1.1.4 (Levels).** A *level function* is a monotone map $\mathrm{lev} : \{0, \dots, n-1\} \to \mathbb{N}$. Its fibres are intervals, the *blocks*. The set $\mathfrak{u}$ of letters $(s, a, b)$ with $\mathrm{lev}(a) < \mathrm{lev}(b)$ is closed under the bracket. We write $\omega_U$ for the set of $k$-letters in $\mathfrak{u}$, and $e_{\omega_U}$ for their wedge product.

So $\mathfrak{u}$ is the nilradical of the block upper triangular parabolic in both copies of $\mathfrak{gl}_n$, the $k$-letters of $\mathfrak{u}$ span its intersection with the compact part, and $e_{\omega_U}$ spans the top exterior power of that intersection.

**Definition 1.1.5 (Levi evaluation).** Let $\mathcal{A}$ be the free algebra on symbols $(s, a, b)$, with $s \in \{k, p\}$ and $a, b$ arbitrary. For $\alpha \in \mathcal{A}$ and a pair module $V$, $\mathrm{ev}(\alpha)$ is the operator obtained by sending $(k, a, b)$ to $k_{ab}$ and $(p, a, b)$ to $p_{ab}$. The *Levi evaluation* $\mathrm{ev}_{\mathfrak{l}}(\alpha)$ does the same, except that a symbol with $\mathrm{lev}(a) \neq \mathrm{lev}(b)$ goes to $0$. On chains, $\mathrm{ev}^C_{\mathfrak{l}}(\alpha)$ lets each symbol of the Levi act by the tensor product of its adjoint action on $\Lambda \mathfrak{u}$ and its action on $V$.

The Levi $\mathfrak{l}$ normalizes $\mathfrak{u}$, so $\mathfrak{l}$ acts on $\mathfrak{u}$-chains, and this action commutes with $\partial_{\mathfrak{u}}$.

### The theorem

The classical statement is as follows.

**Theorem 1.1.6 (Casselman and Osborne).** Let $\mathfrak{g}$ be a complex reductive Lie algebra, $\mathfrak{q} = \mathfrak{l} + \mathfrak{u}$ a parabolic subalgebra and $V$ a $\mathfrak{g}$-module. Let $z$ lie in the center of $U(\mathfrak{g})$ and write $z = z_{\mathfrak{l}} + y$ with $z_{\mathfrak{l}} \in U(\mathfrak{l})$ and $y \in \mathfrak{u}\, U(\mathfrak{g})$. Then $z$ and $z_{\mathfrak{l}}$ act in the same way on $H_*(\mathfrak{u}, V)$.

Casselman and Osborne prove this for $\mathfrak{n}$-cohomology (W. Casselman and M. S. Osborne, *The n-cohomology of representations with an infinitesimal character*, Compositio Math. 31 (1975), §2). The homology form is the same argument with arrows reversed. We need a version in which $z$ is only assumed to commute with a subalgebra, and the decomposition $z = z_{\mathfrak{l}} + y$ is replaced by a statement about every pair module.

**Theorem 1.1.7 (Casselman and Osborne for a closed subset).** Let $\mathrm{lev}$ be a level function and $S \subseteq \mathfrak{u}$ a set of letters closed under the bracket. Let $\alpha, \beta \in \mathcal{A}$. Assume that in every pair module:

1. $\mathrm{ev}(\alpha)$ commutes with $x_l$ for every $l \in S$;
2. for every $v \in V$, $\mathrm{ev}(\alpha) v - \mathrm{ev}_{\mathfrak{l}}(\beta) v$ lies in $\sum_{l \in \mathfrak{u}} x_l V$.

Then in every pair module $V$, for every $j \geq 0$ and every $S$-supported cycle $x$ of degree $j$, there is a $\mathfrak{u}$-supported chain $w$ of degree $j + 1$ with
$$\mathrm{ev}(\alpha)\, x - \mathrm{ev}^C_{\mathfrak{l}}(\beta)\, x = \partial_{\mathfrak{u}} w .$$
Here $\mathrm{ev}(\alpha)$ acts on the coefficients of $x$ only.

Lean: `GlobalTheory.CompanionTheory.PairMult.COU.genCOU2` (also `GlobalTheory.T.pair_multiplicity_generic_unitary`, the same statement).

The proof uses two facts. The first is that the Levi action commutes with the boundary: for $\beta \in \mathcal{A}$, $\mathrm{ev}^C_{\mathfrak{l}}(\beta)$ preserves support and degree of $\mathfrak{u}$-chains and commutes with $\partial_{\mathfrak{u}}$. The second is a free cover.

**Lemma 1.1.8 (Free cover).** For every pair module $V$ there are a pair module $Y$ and a surjective map of pair modules $\pi : Y \to V$ such that every $\mathfrak{u}$-supported cycle of degree at least $1$ in $Y$ is the boundary of a $\mathfrak{u}$-supported chain.

*Proof.* There is a pair module $W$ with a linear form $\chi$ and a vector $w_0$ such that $\chi(w_0) = 1$ and $\chi$ vanishes on the image of every $E^1_{ab}$ and every $E^2_{ab}$. The module $W$ carries operators $a_l$ and $d_l$, one pair for each letter, with $[d_l, a_m] = \delta_{lm}$, and an exhaustive filtration on which $x_l - a_l$ and $d_l$ lower the degree. Put $Y = V \otimes W$ with the diagonal action and $\pi(v \otimes w) = \chi(w) v$. Since $\chi$ kills the image of the operators, $\pi$ is a map of pair modules, and $\pi(v \otimes w_0) = v$. The operator $\sum_{l \in \mathfrak{u}} d_l\, \varepsilon_l$ is a contracting homotopy for $\partial_{\mathfrak{u}}$ up to terms of lower filtration degree, and an induction on the filtration shows that every $\mathfrak{u}$-cycle of positive degree in $Y$ is a boundary. $\square$

*Proof of the theorem.* We argue by induction on $j$, for all pair modules at once.

Let $j = 0$. Then $x = e_\emptyset \otimes v$, and the Levi action on degree $0$ is $\mathrm{ev}_{\mathfrak{l}}(\beta)$ on $V$. By hypothesis 2, $\mathrm{ev}(\alpha) v - \mathrm{ev}_{\mathfrak{l}}(\beta) v = \sum_{l \in \mathfrak{u}} x_l w_l$. The right side is $\partial_{\mathfrak{u}}(\sum_{l \in \mathfrak{u}} e_l \otimes w_l)$, since chains of degree $1$ have no bracket term.

Let $j \geq 1$ and let $x$ be an $S$-supported cycle of degree $j$ in $V$. Take the free cover $\pi : Y \to V$ of the lemma, and lift $x$ coefficient by coefficient to an $S$-supported chain $x'$ of degree $j$ in $Y$. Put $z' = \partial_{\mathfrak{u}} x'$. Since $S$ is closed under the bracket, $z'$ is $S$-supported of degree $j - 1$. It is a cycle, and its coefficients lie in the pair submodule $\ker \pi$, because $\pi(z') = \partial_{\mathfrak{u}} x = 0$. The induction hypothesis, applied in the pair module $\ker \pi$, gives a $\mathfrak{u}$-supported chain $w'$ of degree $j$ with coefficients in $\ker \pi$ and
$$\mathrm{ev}(\alpha) z' - \mathrm{ev}^C_{\mathfrak{l}}(\beta) z' = \partial_{\mathfrak{u}} w' .$$
Now put $u = \mathrm{ev}(\alpha) x' - \mathrm{ev}^C_{\mathfrak{l}}(\beta) x' - w'$. On $S$-supported chains, $\mathrm{ev}(\alpha)$ commutes with $\partial_{\mathfrak{u}}$: the boundary only applies the operators $x_l$ with $l \in S$ to the coefficients, and these commute with $\mathrm{ev}(\alpha)$ by hypothesis 1. The Levi action commutes with $\partial_{\mathfrak{u}}$. So $\partial_{\mathfrak{u}} u = \mathrm{ev}(\alpha) z' - \mathrm{ev}^C_{\mathfrak{l}}(\beta) z' - \partial_{\mathfrak{u}} w' = 0$. Thus $u$ is a $\mathfrak{u}$-supported cycle of degree $j \geq 1$ in $Y$, and by the lemma $u = \partial_{\mathfrak{u}} t$. Apply $\pi$. Since $\pi(w') = 0$ and $\pi$ commutes with all operators, $\mathrm{ev}(\alpha) x - \mathrm{ev}^C_{\mathfrak{l}}(\beta) x = \partial_{\mathfrak{u}}(\pi t)$. $\square$

The proof needs the hypotheses in every pair module, and not only in $V$: the induction runs through the submodule $\ker \pi$ of the cover.

### The top compact class

Now take $S$ to be the set $\omega_U$ of $k$-letters of $\mathfrak{u}$. It is closed under the bracket, because $[k_{ab}, k_{bc}] = k_{ac}$.

**Lemma 1.1.9 (The top compact chain is a cycle).** Let $v \in V$ with $k_{ab} v = 0$ for all $a < b$ with $\mathrm{lev}(a) < \mathrm{lev}(b)$. Then $e_{\omega_U} \otimes v$ is a cycle for $\partial_{\mathfrak{u}}$.

*Proof.* The first sum in $\partial_{\mathfrak{u}}$ applies some $x_l$ with $l \in \omega_U$ to $v$, which gives $0$. In the second sum, both $l$ and $m$ lie in $\omega_U$, so $l * m$ is again a $k$-letter of $\mathfrak{u}$, and it lies in $\omega_U \setminus \{l, m\}$. Then $\varepsilon_{l * m}$ meets a wedge that already contains $l * m$, and the term is $0$. $\square$

**Theorem 1.1.10 (Casselman and Osborne for the top compact class).** Let $\mathrm{lev}$ be a level function and $\alpha, \beta \in \mathcal{A}$. Assume that in every pair module:

1. $\mathrm{ev}(\alpha)$ commutes with every $k_{cd}$;
2. for every $v \in V$, $\mathrm{ev}(\alpha) v - \mathrm{ev}_{\mathfrak{l}}(\beta) v$ lies in $\sum_{l \in \mathfrak{u}} x_l V$.

Let $V$ be a pair module and $v \in V$ with $k_{ab} v = 0$ whenever $a < b$ and $\mathrm{lev}(a) < \mathrm{lev}(b)$. Then there is a $\mathfrak{u}$-supported chain $w$ of degree $|\omega_U| + 1$ with
$$e_{\omega_U} \otimes \mathrm{ev}(\alpha) v - \mathrm{ev}^C_{\mathfrak{l}}(\beta)(e_{\omega_U} \otimes v) = \partial_{\mathfrak{u}} w .$$

Lean: `GlobalTheory.CompanionTheory.PairBridge.actUU` (also `GlobalTheory.T.action_unipotent_radical_real`, the same statement).

*Proof.* By the lemma, $e_{\omega_U} \otimes v$ is an $\omega_U$-supported cycle of degree $|\omega_U|$. Hypothesis 1 gives hypothesis 1 of [Theorem 1.1.7](/entry/gen-cou2/) for $S = \omega_U$, and hypothesis 2 is the same in both theorems. So [Theorem 1.1.7](/entry/gen-cou2/) applies with $j = |\omega_U|$ and gives $w$. The two theorems use different names for the letters and for the evaluation of $\mathcal{A}$; we pass from one to the other by exchanging the two kinds of letters and by the matching substitution in the free algebra, and back. $\square$

In words: if $\alpha$ commutes with $\mathfrak{k}$ and $\beta$ is its projection to the Levi modulo $\mathfrak{u}$, then $\alpha$ and $\beta$ act in the same way on the class of $e_{\omega_U} \otimes v$ in $H_{|\omega_U|}(\mathfrak{u}, V)$. Hypothesis 1 asks more than the proof uses: only the $k$-letters of $\mathfrak{u}$ need to commute with $\mathrm{ev}(\alpha)$.

**Remark 1.1.11 (Formalization).** The two theorems use opposite conventions for the Boolean label of a letter: in [ActionUnipotentRadicalReal.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ActionUnipotentRadicalReal.lean#L507) the label `true` means a $p$-letter, while in the general theorem `true` means a $k$-letter, and the free algebra is evaluated at $E^1, E^2$ instead of $k, p$. The proof `actUU_of` (L507) translates by the Boolean swap and a substitution; it uses only the commutation with the $k$-letters of $\mathfrak{u}$, although `ActUU` assumes commutation with all $k_{cd}$. The fact that the top compact chain is a cycle is the input `pair_multiplicity_top_cycle`. The name `pair_multiplicity_generic_unitary` of the input statement says nothing about its content, which is the Casselman-Osborne argument above. The free cover is `coverQ` in [CreAnnApply.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CreAnnApply.lean#L264); the module $W$ comes from `freeQ` (L226), which rewrites an earlier `freeR`, and we did not read the construction of `freeR`. The file of the input statement imports `Mathlib` twice (lines 1 and 3).
