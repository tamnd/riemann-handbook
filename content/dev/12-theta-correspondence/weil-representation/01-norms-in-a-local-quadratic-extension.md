---
title: Norms in a local quadratic extension
decls:
  - GlobalTheory.KSp.NormIndex.mul_mem_range_norm
  - GlobalTheory.T.mul_mem_range_norm_of_not_mem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Norms in a local quadratic extension

This section proves that the product of two elements of a $p$-adic field $F$ that are not norms from a quadratic extension $E$ is a norm. Equivalently, the sign $\eta$ that is $1$ on the norms and $-1$ off them is a character of $F^\times$. The Weil representation of the split unitary group in the next three sections is normalized by a character $\chi$ of $E^\times$ whose restriction to $F^\times$ is $\eta^m$, and the Gauss integral of a Hermitian form in [the next section](/entry/has-gauss-herm/) is a product of values of $\eta$. To split such a product into factors one needs that $\eta$ is multiplicative, and this is the only nontrivial case.

### The setting

Let $F$ be a non-archimedean local field of characteristic $0$, that is, a finite extension of $\mathbb{Q}_p$. Let $E$ be a field that is an $F$-algebra, with an $F$-algebra map $c \colon E \to E$ and an element $\delta \in E$.

**Definition 1.1.1 (Quadratic datum).** The pair $(c, \delta)$ is a *quadratic datum* for $E/F$ if $\delta$ is a unit of $E$, $c(\delta) = -\delta$, and $(1, \delta)$ is a basis of $E$ over $F$.

So $E = F(\delta)$ is a quadratic extension and $c$ is its nontrivial automorphism: $c$ fixes $F$ and moves $\delta$, so $c \neq 1$. Every quadratic extension of $F$ has such a datum, since the characteristic is not $2$: take $\delta$ a square root of a nonsquare. Let $N = N_{E/F} \colon E^\times \to F^\times$ be the norm, so $N(z) = z\, c(z)$, and let $N(E^\times)$ be its image, the norm group.

**Definition 1.1.2 (Norm residue sign).** For $t \in F^\times$ put $\eta(t) = 1$ if $t \in N(E^\times)$ and $\eta(t) = -1$ otherwise.

**Example 1.1.3.** Let $F = \mathbb{Q}_p$ with $p$ odd and $E = \mathbb{Q}_p(\sqrt{u})$ for a unit $u$ that is not a square. Then $E/F$ is unramified, the norm group is the set of $t$ with even valuation, and $\eta(t) = (-1)^{v_p(t)}$.

### The theorem

We take the following result as given.

**Theorem 1.1.4 ([[Local class field theory|SHEN158T3M]]; Hasse, 1930; Lubin and Tate, 1965).** Let $L/F$ be a finite abelian extension. There is a homomorphism $F^\times \to \mathrm{Gal}(L/F)$ that is onto, with kernel $N_{L/F}(L^\times)$. In particular $F^\times / N_{L/F}(L^\times) \cong \mathrm{Gal}(L/F)$.

This is the [local Artin map](/learn/class-field-theory/#local-class-field-theory) of Volume 1, restricted to $L$. See also J.-P. Serre, *Local class field theory*, in Cassels and Fröhlich, *Algebraic Number Theory* (1967), Section 2.

**Lemma 1.1.5.** Let $G$ be a finite group of order $2$, and let $a, b \in G$ with $a \neq 1$ and $b \neq 1$. Then $ab = 1$.

*Proof.* The set $\{1, a, b\}$ has at most two elements and $a, b \neq 1$, so $a = b$. Then $ab = a^2 = 1$, since the order of $a$ divides $2$. $\square$

**Theorem 1.1.6 (Product of two non-norms).** Let $F$ be a non-archimedean local field of characteristic $0$, and let $E$ be an $F$-algebra that is a field, with a quadratic datum $(c, \delta)$. Let $x, y \in F^\times$ with $x \notin N(E^\times)$ and $y \notin N(E^\times)$. Then $xy \in N(E^\times)$.

Lean: `GlobalTheory.KSp.NormIndex.mul_mem_range_norm` (also `GlobalTheory.T.mul_mem_range_norm_of_not_mem`, a second name).

*Proof.* The basis $(1, \delta)$ gives $[E : F] = 2$. A quadratic extension in characteristic $0$ is separable and normal, so $E/F$ is Galois, and its Galois group has order $2$. A group of order $2$ is cyclic, so $E/F$ is abelian. Fix an $F$-embedding of $E$ into an algebraic closure of $F$ and let $L$ be its image. The embedding is an isomorphism $E \cong L$ over $F$, and it carries the norm of $E$ to the norm of $L$, so $N_{E/F}(E^\times) = N_{L/F}(L^\times)$. By local class field theory there is a homomorphism $r \colon F^\times \to \mathrm{Gal}(L/F)$ with kernel $N_{L/F}(L^\times)$. The hypotheses say $r(x) \neq 1$ and $r(y) \neq 1$. The group $\mathrm{Gal}(L/F)$ has order $2$, so the lemma gives $r(xy) = r(x)\,r(y) = 1$, that is, $xy \in N(E^\times)$. $\square$

**Corollary 1.1.7.** The norm residue sign $\eta$ is a character of $F^\times$ of order at most $2$.

*Proof.* Let $x, y \in F^\times$. If both are norms, so is $xy$. If exactly one is a norm, say $x = N(z)$, then $xy$ is not a norm, since otherwise $y = N(z)^{-1} xy = N(z^{-1}w)$ for some $w$. If neither is a norm, the theorem says $xy$ is a norm. In each case $\eta(xy) = \eta(x)\eta(y)$. $\square$

The corollary is how the theorem is used: in [the Gauss integral](/entry/has-gauss-herm/) the sign of a product of diagonal entries of a Hermitian matrix is split into the product of the signs.

**Remark 1.1.8.** The surjectivity in local class field theory gives more: $\eta$ is not trivial, so exactly half of the classes of $F^\times / F^{\times 2}$ are norms. The proof does not need this, only that the kernel of $r$ is the norm group and that the target has order $2$.

**Remark 1.1.9 (Formalization).** Of the quadratic datum, the proof uses only that $(1, \delta)$ is a basis. The conditions that $\delta$ is a unit and that $c(\delta) = -\delta$, the map $c$ itself, and the module topology on $E$ are hypotheses of `GlobalTheory.KSp.NormIndex.mul_mem_range_norm` (MulMemRangeNorm.lean, line 29) that are never used. Class field theory enters as `artin_reciprocity_char_zero` (ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportC.lean, line 155), which is stated for subfields of an algebraic closure; this is why the proof moves $E$ into the algebraic closure. Only the last clause of that result, the kernel of the map to $\mathrm{Gal}(L/F)$, is used. The lemma on groups of order $2$ is `mul_eq_one_of_card_two` (MulMemRangeNorm.lean, line 13). The second name is a `first | exact ...` wrapper (MulMemRangeNormStatement.lean, line 10) under `maxHeartbeats 1000000`. The two callers are `KSp.sgn_mul_of_isQuad` (the corollary) and `gauss_cancel`.
