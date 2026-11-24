---
title: Good reduction from torsion points
decls:
  - GlobalTheory.ManyTorsionProper.isProper_of_many_torsion_charZero
  - GlobalTheory.properOfInfinitelyManyLargeTorsionCounts
  - GlobalTheory.GoodRedTorsion.hasGoodReduction_of_torsion
  - GlobalTheory.T.isProper_of_many_torsion_points_charZero
  - GlobalTheory.T.isProper_of_infinitely_many_large_torsion
  - GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good reduction from torsion points

An abelian variety over the fraction field of a strictly henselian discrete valuation ring has good reduction if it has all its $m$-torsion points rational for infinitely many $m$ prime to the residue characteristic. This is a form of the criterion of Néron, Ogg and Shafarevich, in the version of Serre and Tate. The proof goes through a smooth connected group scheme over the base: such a group is proper if its fibre has many torsion points. The result is used in the proof of [Theorem 3.4.7 of Volume 5](/entry/has-good-reduction-of-infinite-torsion-unramified/). For abelian schemes, see [abelian schemes](/learn/abelian-varieties/#abelian-schemes) and [abelian varieties over a field](/learn/abelian-varieties/#abelian-varieties-over-a-field).

### Definitions

**Definition 4.11.1 (Strictly henselian base).** A pair $(R, K)$ is a *strictly henselian base* if $R$ is a henselian discrete valuation ring with algebraically closed residue field $k$ and $K$ is the fraction field of $R$.

**Definition 4.11.2 (Smooth connected group).** A group scheme $G$ over a base $S$ is a *smooth connected group* if it is commutative, smooth, separated and quasi-compact over $S$, with geometrically connected fibres.

An abelian scheme over $S$ is a smooth connected group that is proper over $S$. Over a field, a smooth connected group of dimension $g$ is an extension of an abelian variety by a linear group. Its $m$-torsion, for $m$ invertible, has at most $m^{2g}$ points over an algebraically closed field, and exactly $m^{2g}$ if and only if the group is an abelian variety. The results below turn this count into properness.

**Definition 4.11.3 (Good reduction).** An abelian variety $A$ over $K$ has *good reduction* over $R$ if there is an abelian scheme $\mathcal{A}$ over $R$ with an isomorphism of group schemes $\mathcal{A}_K \cong A$.

### Properness from torsion

**Theorem 4.11.4 (Properness in characteristic zero).** Let $k$ be an algebraically closed field of characteristic $0$ and $G$ a smooth connected group over $k$ of relative dimension $g$. Assume that there are infinitely many $m \in \mathbb{N}$ with a finite set $s$ of $m$-torsion points of $G(k)$ such that $m^{2g} < m \cdot \# s$. Then $G$ is proper over $k$.

Lean: `GlobalTheory.ManyTorsionProper.isProper_of_many_torsion_charZero` (also `GlobalTheory.T.isProper_of_many_torsion_points_charZero`, a second name).

*Proof.* Assume that $G$ is not proper.

1. A smooth connected group over $k$ that is not proper contains a rational curve: there is a nonconstant morphism from a nonempty open subset of $\mathbb{A}^1_k$ to $G$. Indeed its linear part is nontrivial, and it contains $\mathbb{G}_a$ or $\mathbb{G}_m$.
2. Spread out $G$, the curve and the finite set $s$ over a finitely generated $\mathbb{Z}$-algebra, and specialize to an algebraically closed field $k'$ of characteristic $p$ with $p \nmid m$. We get a smooth connected group $G'$ over $k'$ of relative dimension $g$, a nonconstant morphism from an open subset of $\mathbb{A}^1_{k'}$ to $G'$, and $m$-torsion sets $s'$ with $\# s' = \# s$. Specialization is injective on the torsion of order prime to $p$.
3. The characteristic $p$ form of the theorem (the same statement with $(m : k') \neq 0$) gives that $G'$ is proper. A proper smooth connected group over a field is an abelian variety.
4. Every morphism from an open subset of $\mathbb{A}^1$ to an abelian variety is constant. This contradicts step 2.

$\square$

**Theorem 4.11.5 (Properness from large torsion counts).** Let $k$ be an algebraically closed field and $G$ a smooth connected group over $k$ of relative dimension $g$. Let $C \in \mathbb{N}$. Assume that there are infinitely many $m \in \mathbb{N}$ with $(m : k) \neq 0$ and a finite set $s$ of $m$-torsion points of $G(k)$ such that $m^{2g} \leq C \cdot \# s$. Then $G$ is proper over $k$.

Lean: `GlobalTheory.properOfInfinitelyManyLargeTorsionCounts` (also `GlobalTheory.T.isProper_of_infinitely_many_large_torsion`, a second name).

*Proof.* Among the infinitely many $m$, all but finitely many satisfy $m > C$, and then $m^{2g} \leq C\#s < m\#s$ (here $\#s \geq 1$, since $m \geq 1$ and $m^{2g} \leq C\#s$). In characteristic $p$, the characteristic $p$ result applies to these $m$. In characteristic $0$, apply [Theorem 4.11.4](/entry/is-proper-of-many-torsion-char-zero/). $\square$

### Good reduction

**Theorem 4.11.6 (Good reduction from torsion points).** Let $(R, K)$ be a strictly henselian base with residue field $k$. Let $A$ be an abelian variety over $K$, smooth of relative dimension $g$. Assume that there are infinitely many $m \in \mathbb{N}$ with $(m : k) \neq 0$ and $\# A(K)[m] = m^{2g}$. Then $A$ has good reduction over $R$.

Lean: `GlobalTheory.GoodRedTorsion.hasGoodReduction_of_torsion` (also `GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points`, a second name).

*Proof.*

1. *A model.* Since $A$ is projective, there are a smooth connected group $\mathcal{G}$ over $R$ with $\mathcal{G}_K \cong A$ and an integer $c \geq 1$ such that, for each $a \in A(K)$, the point $ca$ extends to an $R$-point of $\mathcal{G}$. (This is the identity component of a Néron-type model; the multiple $c$ kills the component group.)
2. *Injectivity.* Since $\mathcal{G}$ is separated, the map $\mathcal{G}(R) \to \mathcal{G}(K) = A(K)$ is injective.
3. *No torsion in the kernel of reduction.* Since $R$ is henselian and $\mathcal{G}$ is smooth, an $R$-point of order prime to the residue characteristic that reduces to the identity is the identity. So reduction $\mathcal{G}(R) \to \mathcal{G}_k(k)$ is injective on $m$-torsion for $m$ invertible in $k$.
4. *Counting.* Let $m$ be one of the given numbers and $T = A(K)[m]$. The map $a \mapsto$ (reduction of the extension of $ca$) sends $T$ into the $m$-torsion of $\mathcal{G}_k(k)$. Its fibres are cosets of the kernel of multiplication by $c$ on $T$, which lies in $A(K)[\gcd(m, c)]$ and so has at most $\gcd(m,c)^{2g} \leq c^{2g}$ elements. With steps 2 and 3, $m^{2g} = \#T \leq c^{2g}\, \# s$, where $s$ is the image, a finite set of $m$-torsion points of $\mathcal{G}_k(k)$.
5. *Properness.* By [Theorem 4.11.5](/entry/proper-of-infinitely-many-large-torsion-counts/) with $C = c^{2g}$, the special fibre $\mathcal{G}_k$ is proper. A smooth connected group over a discrete valuation ring with proper fibres is proper. So $\mathcal{G}$ is an abelian scheme with generic fibre $A$.

$\square$

**Remark 4.11.7.** The criterion of Serre and Tate says more: for an abelian variety $A$ over the fraction field of any discrete valuation ring, $A$ has good reduction if and only if the inertia group acts trivially on the $\ell$-adic Tate module for one (or all) $\ell$ prime to the residue characteristic. Over a strictly henselian base the inertia group is the full Galois group, so unramified means that all $\ell$-power torsion is rational. The form here asks for rational $m$-torsion for infinitely many $m$, which is weaker than an $\ell$-adic condition but enough for the counting argument.

**Remark 4.11.8 (Formalization).** The characteristic $0$ theorem has no hypothesis that $m$ is invertible in $k$; it is automatic in characteristic $0$, and $m \geq 1$ follows from the strict inequality ([IsProperOfManyTorsionPointsCharZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProperOfManyTorsionPointsCharZero.lean)). The model of step 1, the rational curve of step 1 of the characteristic $0$ theorem, the specialization of step 2 and the characteristic $p$ result are separate theorems; we have used their statements and not unfolded their proofs. The parenthetical explanation in step 1 of the last proof is ours and is not part of the statement used.
