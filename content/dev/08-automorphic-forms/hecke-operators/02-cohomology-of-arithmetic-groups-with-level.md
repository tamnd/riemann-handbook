---
title: Cohomology of arithmetic groups with level
decls:
  - UpperTheory.V.Af.bddArith
  - cohBound_of
  - UpperTheory.V.Af.cohBoundFree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cohomology of arithmetic groups with level

This section proves a polynomial bound for the total cohomology of $\mathrm{GL}_n$ over a number field with coefficients in functions of level $3M$. The bound is linear in the dimension of the coefficient system and polynomial in $M$, with constants that do not depend on the coefficients. It is used in [the window of the hypotheses](/entry/vwin-of-hypotheses-h-e-alt/), where the size of a space of automorphic forms of high level must be controlled. The proof has two parts: a uniform bound for the cohomology of one arithmetic group, and the passage from adelic level to arithmetic groups by double cosets and Shapiro's lemma.

### Bounded cohomology dimension

For a group $\Gamma$ and a complex representation $A$ of $\Gamma$, let
$$h(\Gamma, A) = \sum_{q \ge 0} \dim_{\mathbb{C}} H^q(\Gamma, A),$$
a cardinal number. We say that $\Gamma$ has *bounded cohomology dimension* if there is an integer $c$ with $h(\Gamma, A) \le c \dim A$ for every representation $A$.

**Example 6.2.1.** A finite group has bounded cohomology dimension with $c = 1$: over $\mathbb{C}$ the higher cohomology vanishes and $H^0$ is a subspace of $A$. A free group of rank $r$ has $c = r + 1$, since $\dim H^1(\Gamma, A) \le r \dim A$ and the higher groups vanish.

The property says that the cohomology is computed by a resolution whose terms are finite sums of induced modules from finite groups, of bounded length. This is the case for arithmetic groups. Two subgroups $\Gamma, \Gamma'$ of a group are *commensurable* if $\Gamma \cap \Gamma'$ has finite index in both. A subgroup of $\mathrm{GL}_n(F)$ commensurable with $\mathrm{GL}_n(\mathcal{O}_F)$ is an arithmetic subgroup in the sense of the Background ([arithmetic subgroups](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets)).

**Theorem 6.2.2 (Arithmetic groups).** Let $F$ be a number field that is totally complex or totally real, $n \ge 0$, and let $\Gamma \le \mathrm{GL}_n(F)$ be commensurable with $\mathrm{GL}_n(\mathcal{O}_F)$. Then $\Gamma$ has bounded cohomology dimension.

Lean: `UpperTheory.V.Af.bddArith`.

The classical source is Borel-Serre: an arithmetic group has a torsion-free subgroup of finite index that is the fundamental group of a compact manifold with corners (the Borel-Serre compactification of the locally symmetric space), so its cohomology with coefficients in $A$ is computed by a finite complex of free modules.

*Proof.* First let $\Gamma = \mathrm{GL}_n(\mathcal{O}_F)$. Assume $F$ is totally complex. We use a criterion for a group $\Gamma$ acting on a cell complex $K$: if the augmented cellular chain complex of $K$ is exact over $\mathbb{Z}$, $K$ has finitely many cells in each degree modulo $\Gamma$ and only finitely many nonzero degrees, and the stabilizers of cells are finite, then $\Gamma$ has bounded cohomology dimension. Indeed, the chain complex tensored with $\mathbb{C}$ is a resolution of $\mathbb{C}$ by finite sums of permutation modules $\mathbb{C}[\Gamma/\Gamma_\sigma]$ with $\Gamma_\sigma$ finite. Each such module is projective over $\mathbb{C}[\Gamma]$. So $H^q(\Gamma, A)$ is a subquotient of $\bigoplus_\sigma \mathrm{Hom}_{\Gamma}(\mathbb{C}[\Gamma/\Gamma_\sigma], A) = \bigoplus_\sigma A^{\Gamma_\sigma}$, the sum over the $q$-cells modulo $\Gamma$, and it vanishes above the top degree. The group $\mathrm{GL}_n(\mathcal{O}_F)$ acts on such a complex. Now assume $F$ is totally real. Choose a CM extension $L/F$ with complex conjugation $\sigma$. Then $\mathrm{GL}_n(\mathcal{O}_F)$ is identified with the fixed points of $\sigma$ in $\mathrm{GL}_n(\mathcal{O}_L)$, and the fixed points of $\sigma$ on the complex of $\mathrm{GL}_n(\mathcal{O}_L)$ give a complex for $\mathrm{GL}_n(\mathcal{O}_F)$ with the same three properties. Finally, bounded cohomology dimension passes to commensurable groups: for a subgroup $\Gamma'$ of finite index $m$ in $\Gamma$, Shapiro's lemma gives $h(\Gamma', A) = h(\Gamma, \mathrm{Ind}_{\Gamma'}^{\Gamma} A)$ and $\dim \mathrm{Ind}\, A = m \dim A$; and in the other direction $H^q(\Gamma, A)$ is a direct summand of $H^q(\Gamma', A)$ over $\mathbb{C}$, by restriction and corestriction. $\square$

### Functions of level $M$

Let $\hat{\mathcal{O}} = \prod_w \mathcal{O}_w$ and, for $M \ge 1$, let
$$K(M) = \ker\bigl(\mathrm{GL}_n(\hat{\mathcal{O}}) \to \mathrm{GL}_n(\hat{\mathcal{O}}/M\hat{\mathcal{O}})\bigr),$$
the principal congruence subgroup of level $M$ in $\mathrm{GL}_n(\mathbb{A}_{F,f})$. Let $\Gamma \le \mathrm{GL}_n(F)$ and let $\xi : \mathrm{GL}_n(F) \to M_d(\mathbb{C})$ be a homomorphism of monoids. Let $\mathcal{C}(K(M), \xi)$ be the space of all functions $f : \mathrm{GL}_n(\mathbb{A}_{F,f})/K(M) \to \mathbb{C}^d$, with $\Gamma$ acting by
$$(\gamma f)(x) = \xi(\gamma)\, f(\gamma^{-1} x).$$
The group $H^q(\Gamma, \mathcal{C}(K(M), \xi))$ is the cohomology of the locally symmetric space of level $K(M)$ with coefficients in the local system of $\xi$, when $\Gamma = \mathrm{GL}_n(F)$. For each $g$, the stabilizer of the coset $gK(M)$ in $\Gamma$ is the group of $\gamma \in \Gamma$ with $g^{-1}\gamma g \in K(M)$.

**Lemma 6.2.3 (Uniform bound for a family of levels).** Let $H \to G$ be a homomorphism of groups, $\Gamma \le H$, and $U \le G$. Assume that $\Gamma \backslash G / U$ is finite and that the stabilizer of each coset $gU$ in $\Gamma$ has bounded cohomology dimension. Then there is $c$ such that for every subgroup $U' \le U$ of index at most $D$, every $d$ and every $\xi$, the total cohomology of $\Gamma$ in the functions on $G/U'$ with values in $\mathbb{C}^d$ is at most $c D d$.

Lean: `cohBound_of`.

*Proof.* Choose representatives $g_1, \dots, g_r$ of $\Gamma \backslash G / U$. The $\Gamma$-set $G/U'$ is the disjoint union of the $\Gamma$-orbits of the cosets $g_i u U'$ with $u \in U$, and each orbit $\Gamma \cdot x$ is $\Gamma / \Gamma_x$. The functions on $G/U'$ are therefore a product of coinduced modules, and Shapiro's lemma gives
$$h\bigl(\Gamma, \mathcal{C}(U', \xi)\bigr) = \sum_{x} h\bigl(\Gamma_x, \mathbb{C}^d\bigr),$$
the sum over the orbits. Each $\Gamma_x$ is a subgroup of finite index in the stabilizer of $g_i U$, so each term is at most $c_i [\Gamma_{g_iU} : \Gamma_x]\, d$ by the transfer argument above. The number of orbits above $g_i U$, weighted by these indices, is the number of cosets of $U'$ in $U$, at most $D$. Take $c = \max_i c_i$. $\square$

**Theorem 6.2.4 (Polynomial bound in the level).** Let $F$ be totally complex or totally real, $n \ge 0$, and let $\Gamma$ be a subgroup of finite index in $\mathrm{GL}_n(F)$. Then there are integers $c$ and $A$ such that for all $M \ge 1$, all $d$ and all monoid homomorphisms $\xi : \mathrm{GL}_n(F) \to M_d(\mathbb{C})$,
$$\sum_{q \ge 0} \dim H^q\bigl(\Gamma, \mathcal{C}(K(3M), \xi)\bigr) \le c\, M^A d.$$

Lean: `UpperTheory.V.Af.cohBoundFree`.

*Proof.* Apply the lemma with $G = \mathrm{GL}_n(\mathbb{A}_{F,f})$ and $U = K(3)$. The double coset space $\mathrm{GL}_n(F) \backslash G / K(3)$ is finite, by the finiteness of the class number and strong approximation for $\mathrm{SL}_n$ ([strong approximation](/learn/groups/#strong-approximation)); since $\Gamma$ has finite index, $\Gamma \backslash G / K(3)$ is finite as well. The stabilizer of $gK(3)$ is $\Gamma \cap gK(3)g^{-1}$, which is commensurable with $\mathrm{GL}_n(\mathcal{O}_F)$, so it has bounded cohomology dimension by the theorem on arithmetic groups. The index of $K(N)$ in $K(1)$ is at most $N^{[F:\mathbb{Q}]\, n^2}$, since $K(1)/K(N)$ embeds in $M_n(\mathcal{O}_F/N)$, of order $N^{[F:\mathbb{Q}] n^2}$. With $N = 3M$ this gives $[K(3) : K(3M)] \le 3^{[F:\mathbb{Q}] n^2} M^{[F:\mathbb{Q}] n^2}$. So the bound holds with $A = [F:\mathbb{Q}]\, n^2$ and $c$ the constant of the lemma times $3^{[F:\mathbb{Q}] n^2}$. $\square$

**Remark 6.2.5 (Formalization).** The lemma is private and is the name `cohBound_of` without a namespace ([CohBoundFree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/TemperedLocalComponents/CohBoundFree.lean#L69)). Dimensions are cardinals (`Module.rank`), so an infinite-dimensional cohomology group is not counted as $0$. The group $\Gamma$ is assumed of finite index in $\mathrm{GL}_n(F)$, not in an arithmetic group; the arithmetic groups enter only as stabilizers. The map $\xi$ is only a monoid homomorphism to matrices; on the group $\Gamma$ it takes invertible values. In the theorem on arithmetic groups, the complex for $\mathrm{GL}_n(\mathcal{O}_F)$ and the fixed-point identification are inputs whose construction we did not unfold ([BddArith.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/TemperedLocalComponents/BddArith.lean#L59)). The finiteness of double cosets and the index bound are also inputs of the lemma.
