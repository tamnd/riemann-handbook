---
title: Chern classes and power sums
decls:
  - LateralTheory.Fix.EtaleChapterDTwo.s42
  - LateralTheory.Fix.EtaleChapterDTwo.s54
  - LateralTheory.Fix.EtaleChapterDTwo.s57
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern classes and power sums

This section proves the axiom D2 of the chapter from the axiom D1, the projective bundle formula. D2 asks, for each $k > 0$, for a class $s_k(V) \in H^{2k}(E, \mathbb{Z}/q(k))$ of each vector bundle $V$. The class must commute with pullback, be additive on direct sums, and equal $c_1(L)^k$ on a line bundle $L$. If $V$ has Chern roots $x_1, \ldots, x_N$, then $s_k(V) = x_1^k + \cdots + x_N^k$ is the $k$-th power sum of the roots. It is $k!$ times the degree $k$ part of the Chern character.

The construction is Grothendieck's. The projective bundle formula defines Chern classes. A splitting argument gives the Whitney sum formula. Newton's formulas turn Chern classes into power sums (A. Grothendieck, "La théorie des classes de Chern", Bull. Soc. Math. France 86 (1958), 137 to 154; for étale cohomology, J. S. Milne, *Étale Cohomology*, Chapter VI, §10). The code follows this plan, with no splitting principle. It uses a ring in which the even cohomology classes multiply, and it works with sequences of classes in that ring.

We use the vector bundles, line bundles and first Chern classes of [the previous section](/entry/s0/). For a class $x$ of degree $2$, $x^k$ is the $k$-th cup power: $x^0 = 1_E$ and $x^{k+1} = x^k \cup x$.

**Definition (Direct sum).** Let $V : E \to B\mathrm{GL}_a$ and $W : E \to B\mathrm{GL}_b$ be vector bundles. Their *direct sum* $V \oplus W : E \to B\mathrm{GL}_{a+b}$ sends a simplex $x$ to the block diagonal matrices with blocks $V(x)$ and $W(x)$.

**Definition (Projective bundle).** Let $N \geq 1$. The space $P_N$ has as objects over $U$ the vectors $v \in \Gamma(U, \mathcal{O}_U)^N$ whose coordinates generate the unit ideal. A morphism $v \to w$ is a pair $(g, \lambda)$ with $g \in \mathrm{GL}_N$, $\lambda$ a unit and $g v = \lambda w$. The $N'$-simplices of $P_N$ are the strings of $N'$ composable morphisms. The map $\mathrm{pr} : P_N \to B\mathrm{GL}_N$ keeps $g$, and the map $\mathrm{line} : P_N \to B\mathrm{GL}_1$ keeps $\lambda$. For a vector bundle $V$ of rank $N$ on $E$, the *projective bundle* $P(V)$ is the pullback of $\mathrm{pr}$ along $V$, with projection $\pi : P(V) \to E$. Its *tautological class* is $\xi = c_1(\mathrm{line}) \in H^2(P(V), \mathbb{Z}/q(1))$.

For a scheme, $P_N$ is a model of projective space $\mathbb{P}^{N-1}$ with its group of symmetries: a point is a line spanned by a unimodular vector, up to scaling.

**Axiom D1 (Projective bundle formula).** If $q$ is invertible on $E$ and $V$ has rank $N$, then for all $n$ and $i$ the map
$$
\begin{aligned}
\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) &\to H^n(P(V), \mathbb{Z}/q(i)), \\
(a_j)_j &\mapsto \sum_{j=0}^{N-1} \pi^* a_j \cup \xi^j
\end{aligned}
$$
is bijective. In this chapter D1 is a hypothesis. It is proved in [the projective bundle formula for any space](/entry/projective-bundle-formula-vector-bundle-any-space/).

**Theorem (The even cohomology ring).** Let $q \geq 1$. For each space $E$ on which $q$ is invertible there is a commutative ring $R(E)$ with additive maps $\iota_k : H^{2k}(E, \mathbb{Z}/q(k)) \to R(E)$ and $\pi_k : R(E) \to H^{2k}(E, \mathbb{Z}/q(k))$, such that:

1. $\pi_k \circ \iota_k$ is the identity, and $\iota_0(1_E) = 1$;
2. $\iota_{k+l}(a \cup b) = \iota_k(a)\, \iota_l(b)$, and so $\iota_k(x^k) = \iota_1(x)^k$ for $x$ of degree $2$;
3. each map $f : E \to E'$ gives a ring map $f^* : R(E') \to R(E)$ with $f^* \circ \iota_k = \iota_k \circ f^*$ and $\pi_k \circ f^* = f^* \circ \pi_k$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s42`.

*Proof.* Let $R(E) = \bigoplus_{k \geq 0} H^{2k}(E, \mathbb{Z}/q(k))$, with $\iota_k$ the inclusion and $\pi_k$ the projection. The product of $a$ of degree $2k$ and $b$ of degree $2l$ is $a \cup b$. This makes $R(E)$ a graded ring in the sense of [[GradedRing|8KB4SQGC0C]]. [The ring laws](/entry/s41/) give the axioms. Associativity is the second law. The left unit law is the first law, which needs $q$ invertible on $E$. Graded commutativity gives $a \cup b = (-1)^{2k \cdot 2l} b \cup a = b \cup a$, so $R(E)$ is commutative, and the right unit law follows from the left one. The ring maps $f^*$ act in each degree. They are ring maps by [the naturality theorem](/entry/s0/): pullback commutes with the cup product and with $1_E$. $\square$

**Definition (Chern family).** Let $q$ be invertible on $E$ and let $V$ be a vector bundle of rank $N$ on $E$. A *Chern family* of $V$ is a sequence $c_j \in H^{2j}(E, \mathbb{Z}/q(j))$, $j \geq 0$, such that $c_0 = 1_E$, $c_j = 0$ for $j > N$, and
$$
\sum_{j=0}^{N} \pi^*(c_j)\, \xi^{N-j} = 0 \quad \text{in } R(P(V)).
$$

**Lemma (Chern families exist and are unique).** Assume D1. If $q$ is invertible on $E$, each vector bundle $V$ on $E$ has exactly one Chern family.

Lean: `LateralTheory.E.D2.LeafChern_of` (also `LateralTheory.Fix.EtaleChapterDTwo.s43`, a second name).

*Proof.* Let $N$ be the rank of $V$. Since $c_0 = 1_E$, the relation reads
$$
\sum_{m=0}^{N-1} \pi^*(c_{N-m}) \cup \xi^m = -\xi^N \quad \text{in } H^{2N}(P(V), \mathbb{Z}/q(N)).
$$
Put $a_m = c_{N-m}$. By D1 with $n = 2N$ and $i = N$, there is exactly one family $(a_m)_{m < N}$ with this property. It determines $c_1, \ldots, c_N$, and the other $c_j$ are fixed by the definition. $\square$

The code also proves that Chern families commute with pullback. If $c$ is the Chern family of $V$ on $E'$ and $f : E \to E'$, then $(f^* c_j)_j$ is the Chern family of $V \circ f$. This follows from the naturality theorem, since $P(V \circ f)$ maps to $P(V)$ over $f$.

**Theorem (Whitney sum formula).** Let $q$ be invertible on $E$, and let $V$ and $W$ be vector bundles of ranks $a$ and $b$ on $E$ with Chern families $c$ and $d$. Then $V \oplus W$ has a Chern family $e$ with
$$
\iota_k(e_k) = \sum_{p + r = k} \iota_p(c_p)\, \iota_r(d_r) \quad \text{for all } k \geq 0.
$$

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s54`.

*Proof.* Let $e_k = \sum_{p+r=k} c_p \cup d_r$. Then $e_0 = 1_E$, and $e_k = 0$ for $k > a + b$ because one of $c_p$ and $d_r$ is $0$. We must prove the relation on $P = P(V \oplus W)$. Write $\xi$ for its tautological class and put
$$
\begin{aligned}
y_c &= \sum_{i=0}^{a} \pi^*(c_i)\, \xi^{a-i}, \\
y_d &= \sum_{j=0}^{b} \pi^*(d_j)\, \xi^{b-j}.
\end{aligned}
$$
A computation with polynomials shows that $y_c\, y_d = \sum_{k=0}^{a+b} \pi^*(e_k)\, \xi^{a+b-k}$ in $R(P)$. So it is enough to show $y_c \cup y_d = 0$.

Let $U_1 \subset P$ be the part where the first $a$ coordinates of the vector at the first vertex generate the unit ideal. Let $U_2$ be the part where the last $b$ coordinates do. The code builds maps $U_1 \to P(V)$ and $U_2 \to P(W)$ that keep the first or the last coordinates. They are compatible with the projections to $E$ and with the line bundles. So the pullback of $y_c$ to $U_1$ is the pullback of the Chern relation of $V$, and it is $0$. In the same way, $y_d$ pulls back to $0$ on $U_2$.

The $a + b$ coordinates of a vector generate the unit ideal. So, locally, the first $a$ coordinates or the last $b$ coordinates generate the unit ideal. Hence each simplex of $P$ lies in $U_1$ or in $U_2$ after restriction to the members of an étale covering. The code proves that such a covering makes the two free complexes of $U_1$ and $U_2$ map onto that of $P$. The support condition of cup products then applies: if $y_c$ vanishes on $U_1$ and $y_d$ vanishes on $U_2$, then $y_c \cup y_d = 0$. $\square$

This is the topological argument for the Whitney formula in Grothendieck's setting. $P(V \oplus W)$ is covered by the complements of $P(W)$ and of $P(V)$, and these retract onto $P(V)$ and $P(W)$.

**Lemma (Chern family of a line bundle).** Let $q$ be invertible on $E$, and let $c$ be the Chern family of a line bundle $L$. Then $c_1 = -c_1(L)$.

Lean: `LateralTheory.E.D2.LeafLine_of` (also `LateralTheory.Fix.EtaleChapterDTwo.s55`, a second name).

*Proof.* For $N = 1$ the vector $(1)$ gives a section $\sigma : E \to P(L)$ with $\pi \circ \sigma = \mathrm{id}$ and $\mathrm{line} \circ \sigma = L$. The relation of the Chern family is $\xi + \pi^*(c_1) = 0$. Pull it back along $\sigma$, with the naturality of $c_1$: $c_1(L) + c_1 = 0$. $\square$

**Definition (Newton power sums).** Let $A$ be a commutative ring and let $c = (c_j)_{j \geq 0}$ be a sequence in $A$ with $c_0 = 1$. Put $c(T) = \sum_j c_j T^j$, a unit in the [formal power series](/learn/algebra/#polynomials-and-power-series) ring $A[[T]]$. The $k$-th *Newton power sum* $\mathrm{nw}_k(c)$ is the coefficient of $T^k$ in $-T\, c'(T)\, c(T)^{-1}$.

If $c(T) = \prod_i (1 - x_i T)$, then $-T c'(T)/c(T) = \sum_i x_i T / (1 - x_i T)$, so $\mathrm{nw}_k(c) = \sum_i x_i^k$ for $k \geq 1$. These are Newton's formulas (I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I, §2). The code proves three facts. A ring map $\varphi$ gives $\varphi(\mathrm{nw}_k(c)) = \mathrm{nw}_k(\varphi(c))$. If $e(T) = c(T)\, d(T)$, then $\mathrm{nw}_k(e) = \mathrm{nw}_k(c) + \mathrm{nw}_k(d)$, since $-T e'/e$ is the sum of the two logarithmic derivatives. If $c(T) = 1 - xT$, then $\mathrm{nw}_k(c) = x^k$ for $k \geq 1$.

**Theorem (Power sum classes).** Assume the axioms A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5 and D1. Let $q \geq 1$ and $k \geq 1$. For each space $E$ and each vector bundle $V$ on $E$ there is a class $s_k(V) \in H^{2k}(E, \mathbb{Z}/q(k))$ such that:

1. $f^* s_k(V) = s_k(V \circ f)$ for each map $f : E \to E'$ and bundle $V$ on $E'$, when $q$ is invertible on $E'$;
2. $s_k(V \oplus W) = s_k(V) + s_k(W)$, when $q$ is invertible on $E$;
3. $s_k(L) = c_1(L)^k$ for each line bundle $L$, when $q$ is invertible on $E$.

So the axiom D2 holds.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s57`.

*Proof.* If $q$ is invertible on $E$, let $c$ be the Chern family of $V$ and put
$$
s_k(V) = \pi_k\big( \mathrm{nw}_k(\iota_j(c_j))_j \big),
$$
the Newton power sum computed in the ring $R(E)$. If $q$ is not invertible on $E$, put $s_k(V) = 0$.

Part 1. The pullbacks $f^* c_j$ form the Chern family of $V \circ f$, by the naturality of Chern families and the uniqueness lemma. The ring map $f^*$ commutes with $\iota$, with $\pi_k$ and with Newton power sums. So $f^* s_k(V) = s_k(V \circ f)$.

Part 2. Let $c$ and $d$ be the Chern families of $V$ and $W$. [The Whitney sum formula](/entry/s54/) and uniqueness show that the Chern family $e$ of $V \oplus W$ satisfies $e(T) = c(T)\, d(T)$ in $R(E)[[T]]$, after $\iota$. Newton power sums are additive for products, and $\pi_k$ is additive.

Part 3. By the lemma on line bundles, $c(T) = 1 - \iota_1(c_1(L))\, T$ in $R(E)[[T]]$. So the Newton power sum is $\iota_1(c_1(L))^k = \iota_k(c_1(L)^k)$, and $\pi_k$ of it is $c_1(L)^k$. $\square$

**Remark.** The theorem `s57` is the term `D2.goal_of s42 s43 s44 s54 s55 s56`. Its type `EtaleChapterDTwo` has $22$ hypotheses, the axioms A1 to C5 and D1, and the conclusion D2. The proof of `D2.goal_of` ([InstCommRingR.lean](lean:Development/EtaleCohomology/EtaleSheaves/InstCommRingR.lean#L85)) binds $21$ of them without a name and uses only D1. So the theorem is really "D1 implies D2". The list of other axioms only makes the type fit the place where it is used.

**Remark.** The classes $s_k(V)$ are $0$ when $q$ is not invertible on $E$. The three properties make no claim in that case, so this value is a convention. The Chern family of the code has $c_1 = -c_1(L)$ for a line bundle. So it differs from the usual Chern classes by signs. The theorem does not depend on this convention: the lemma on line bundles gives $c(T) = 1 - x T$ with $x = c_1(L)$, and the Newton power sums of $1 - xT$ are the powers $x^k$.

**Remark.** Some Lean names here mislead. The space $P_N$ is `PGL N` ([BlockGLMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/BlockGLMap.lean#L42)), but it is not the group $\mathrm{PGL}_N$. It is the space of unimodular vectors. The support condition is `LeafA6supp`, a second name of `DivisorSupportCondition`. The theorem `s57` has a second name `intersectionNumber_baseChange` ([AwSpec.lean](lean:Development/EtaleCohomology/EtaleSheaves/AwSpec.lean#L127)), and it says nothing about intersection numbers or base change.

## Notes and references

The chapter feeds two parts of the Galois row. The last theorem is copied without change into [the chapter on étale cohomology](/entry/a0/), with [a second name](/entry/d2-intersection-number-base-change/). There [the theorem on the trace isomorphism](/entry/etale-duality-trace-isomorphism/) supplies the $22$ hypotheses, so D2 holds outright, and D2 is used for [the finiteness of duality](/entry/etale-finiteness-of-duality/). From there it reaches [the finiteness of the representation](/entry/v-fin-holds/), which is used in the step [geometric realization of weight one](/step/geo-one-holds/) of [the proof](/proof/galois-row/). The Kummer sequence of the first section goes to [the top theorem of the étale topology](/entry/etale-topology-top/), which feeds the same finiteness result.

J. S. Milne, *Étale Cohomology*, Princeton University Press, 1980: Chapter II, §2 for the Kummer sequence; Chapter III, Proposition 4.9 for $H^1(X, \mathbb{G}_m) = \mathrm{Pic}(X)$; Chapter VI, §10 for Chern classes.

A. Grothendieck, "La théorie des classes de Chern", Bull. Soc. Math. France 86 (1958), 137 to 154.

A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Section 3.2, Theorem 3.11, for graded commutativity of the cup product.

N. E. Steenrod, "Products of cocycles and extensions of mappings", Ann. of Math. 48 (1947), 290 to 320, for the cup-$1$ product.

I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Oxford University Press, Chapter I, §2, for Newton's formulas.
