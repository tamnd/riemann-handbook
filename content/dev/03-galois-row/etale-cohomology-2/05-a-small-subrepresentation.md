---
title: A small subrepresentation of a compact group
decls:
  - LateralTheory.DivDb.goal_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A small subrepresentation of a compact group

Let $\rho$ be a continuous semisimple representation of a compact group $\Gamma$ of dimension $N$. Assume that on a dense set of elements $s$, the matrix $\rho(s)$ is killed by a monic polynomial $P_s$ of degree $n$, and that the Lie algebra of the Zariski closure of the image contains an element with $n$ lacunary eigenvalues. This section shows that $\rho$ then comes from a representation $r$ of dimension $n$: $r$ is a subrepresentation of $\rho$, $\rho$ is a subrepresentation of a sum of copies of $r$, and $r(s)$ has characteristic polynomial $P_s$ in good cases. The proof applies [the key criterion](/entry/etale-divisibility-key-criterion-of-components/) and then builds $r$ from matrix units. It is used for [Galois representations](/entry/div-set-holds/), with $\Gamma$ a Galois group.

We keep the notation of the previous section: $\overline{S}$ is the Zariski closure, $T(S)$ the tangent space at $1$, and a family is lacunary when averages over disjoint sets differ. Let $\Gamma$ be a [[topological group|92700QAB5Y]] that is [[compact|0TVJZYB6SH]], see [topological groups](/learn/analysis/#topological-groups-and-covering-maps). Let $K$ be an algebraically closed field of characteristic $0$ with a Hausdorff topology that makes it a topological ring, and let $K'$ be an algebraically closed field that contains $K$.

**Definition 4.5.1 (Semisimple, Lie element, generic product).** A homomorphism $\rho : \Gamma \to \mathrm{GL}_N(K)$ is *semisimple* if each $\rho$-invariant subspace of $K^N$ has a $\rho$-invariant complement. A matrix $X \in M_N(K')$ is in the *Lie algebra of* $\rho$ if $df_1(X) = 0$ for each polynomial $f$ over $K$ that vanishes on $\rho(\Gamma)$. A monic polynomial $P$ of degree $n$ has *generic products* if it is [[separable|0RZ89QWTSJ]] and, for each multiset $M$ of $n$ roots of $P$ other than the multiset of all roots, the product of $M$ differs from the product of all roots.

**Theorem 4.5.2 (Small subrepresentation).** Let $\Gamma$, $K$ and $K'$ be as above. Let $\rho : \Gamma \to \mathrm{GL}_N(K)$ be continuous and semisimple. Let $S \subseteq \Gamma$ be [[dense|0BSJSX7ME2]], and for $s \in S$ let $P_s$ be a monic polynomial of degree $n$ with $P_s(\rho(s)) = 0$. Let $X \in M_N(K')$ be in the Lie algebra of $\rho$, and let the characteristic polynomial of $X$ have $n$ distinct roots $e_1, \dots, e_n$ that form a lacunary family. Let $\psi : \Gamma \to K^\times$ be a continuous character with $\psi(s) = (-1)^n P_s(0)$ for $s \in S$. Then there is a continuous semisimple $r : \Gamma \to \mathrm{GL}_n(K)$ with the following properties.

1. There is $A \in M_{N \times n}(K)$ of rank $n$ with $\rho(g) A = A\, r(g)$ for all $g$.
2. There are $k \ge 0$ and $B \in M_{nk \times N}(K)$ of rank $N$ with $(r(g) \otimes 1_k) B = B \rho(g)$ for all $g$.
3. The characteristic polynomial of $r(g)$ kills $\rho(g)$, for all $g$.
4. $P_s(r(s)) = 0$ and $\det r(s) = \psi(s)$, for all $s \in S$, and $\det r = \psi$ on $\Gamma$.
5. The set of $g$ such that the characteristic polynomial of $r(g)$ is separable is open and dense.
6. For $s \in S$, the characteristic polynomial of $r(s)$ is $P_s$ if it is separable, or if $P_s$ has generic products.

Lean: `LateralTheory.DivDb.goal_holds`.

The proof uses the key criterion, the matrix units lemma of the previous section, and eleven more statements, which the code proves in other files. We state them; we opened their statements but not their proofs, except where we give an argument.

**Definition 4.5.3 (Subrepresentation datum).** Let $\rho$ be as above and $r : \Gamma \to \mathrm{GL}_n(K)$ a homomorphism. A *subrepresentation datum* is a pair of matrices $A \in M_{N \times n}(K)$ and $B \in M_{n \times N}(K)$ with $BA = 1$ and $\rho(g) A = A\, r(g)$ for all $g$, such that each $Z \in M_N(K)$ with $Z T = 0$ for all intertwiners $T$ (all $T$ with $\rho(g) T = T r(g)$) is zero.

**Lemma 4.5.4 (Inputs).** Let $\rho : \Gamma \to \mathrm{GL}_N(K)$.

1. (Descent of the Lie element.) Let $X$ and $e$ be as in the theorem. Then there are $X_0 \in M_N(K)$ in the Lie algebra of $\rho$ and a lacunary family $e^0$ of $n$ roots of the characteristic polynomial of $X_0$.
2. (Degree everywhere.) If $\rho$ is continuous and $\rho(s)$ has degree at most $n$ for all $s$ in a dense set, then $\rho(g)$ has degree at most $n$ for all $g$.
3. (Structure.) If $\rho$ is semisimple, each $\rho(g)$ has degree at most $n$, $X_0$ is in the Lie algebra and $e^0$ is a lacunary family of roots of its characteristic polynomial, then there is a system $p$ with $(\rho, e^0, p)$ good.
4. (Big corner.) Let $A$ be a subalgebra with a corner system $p$, normalized by $\rho$, that keeps the $\rho$-invariant subspaces. Assume the conclusion of part 2 of the key criterion for all $g$. Then there is a subalgebra $R$ that contains $\rho(\Gamma)$, has $p$ as a corner system, is normalized by $\rho$, and keeps the $\rho$-invariant subspaces.
5. (Semisimplicity.) If $\rho$ is semisimple and a subalgebra $R$ is normalized by $\rho$ and keeps the invariant subspaces, then $R$ has no nil ideal.
6. (Representation.) If $p$ is a system, $R$ contains $\rho(\Gamma)$ and has matrix units adapted to $p$, then there is a homomorphism $r : \Gamma \to \mathrm{GL}_n(K)$ with a subrepresentation datum.
7. (Finite subrepresentation.) Given a datum and $\rho$ semisimple: $r$ is semisimple, $A$ has rank $n$, $r(g) = B \rho(g) A$, and a polynomial kills $\rho(g)$ if and only if it kills $r(g)$.
8. (Dense separability, algebraic part.) Given a datum, let $U$ be a subgroup and $g \in \Gamma$. If $\rho(g) m$ has $n$ distinct eigenvalues for some $m \in \overline{\rho(U)}$, then $r(gu)$ has separable characteristic polynomial for some $u \in U$.
9. (Dense separability, topological part.) Let $\Gamma$ be compact and $r$ continuous. If each coset $gU$ of each normal subgroup $U$ of finite index contains an element with separable characteristic polynomial, then the set of such elements is open and dense.
10. (Characteristic polynomial.) Let $x \in M_n(K)$ and let $P$ be monic of degree $n$ with $P(x) = 0$. If the characteristic polynomial $\chi_x$ is separable, then $\chi_x = P$. If $P$ has generic products and $\det x = (-1)^n P(0)$, then $\chi_x = P$.
11. (Embedding.) Given a datum with $\rho$ and $r$ semisimple, there are $k$ and matrices $T_j \in M_{n \times N}(K)$, $T'_j \in M_{N \times n}(K)$ for $j = 1, \dots, k$, with $T_j \rho(g) = r(g) T_j$, $\rho(g) T'_j = T'_j r(g)$ and $\sum_j T'_j T_j = 1$.

Lean: `LateralTheory.DivDb.SpecLie` (also `LateralTheory.DivDb.DegAll`, `LateralTheory.DivDb.Struct`, `LateralTheory.DivDb.BigCorner`, `LateralTheory.DivDb.Semis`, `LateralTheory.DivDb.Rep`, `LateralTheory.DivDb.FinSub`, `LateralTheory.DivDb.DenseAlg`, `LateralTheory.DivDb.FinDense`, `LateralTheory.DivDb.FinPoly`, `LateralTheory.DivDb.FinEmbed`, the eleven statements).

*Proof.* We give the argument for 2 and 10. For 2: a matrix $x$ has degree at most $n$ if and only if $1, x, \dots, x^n$ are linearly dependent, that is, if all minors of size $n + 1$ of the $N^2 \times (n + 1)$ matrix of their entries vanish. These minors are polynomials in $x$. So the set of $g$ with $\rho(g)$ of degree at most $n$ is closed, as $\rho$ is continuous and $K$ is Hausdorff. It contains a dense set, so it is $\Gamma$. For 10: the eigenvalues of $x$ are roots of $P$, since $P(x) = 0$. If $\chi_x$ is separable, it is the minimal polynomial of $x$, so it divides $P$, and both are monic of degree $n$. In the second case, the multiset $M$ of the eigenvalues of $x$ consists of $n$ roots of $P$, and its product is $\det x = (-1)^n P(0)$, the product of all roots of $P$. Generic products force $M$ to be the multiset of roots of $P$, so $\chi_x = P$. $\square$

*Proof of the theorem.* By descent of the Lie element we replace $X$ and $e$ by $X_0 \in M_N(K)$ and a lacunary $e^0$. Since $P_s(\rho(s)) = 0$, each $\rho(s)$ with $s \in S$ has degree at most $n$, so each $\rho(g)$ has degree at most $n$ by degree everywhere. Structure gives a system $p$ with $(\rho, e^0, p)$ good. Let $A$ be the envelope.

The [key criterion](/entry/etale-divisibility-key-criterion-of-components/) holds for $(\rho, e^0, p)$. Its part 2 with $U = \Gamma$ is the hypothesis of the big corner, since goodness gives the corner system, the normalization and the invariant subspaces. So there is a subalgebra $R \supseteq \rho(\Gamma)$ with $p$ as a corner system. By semisimplicity $R$ has no nil ideal, so $R$ has matrix units adapted to $p$ by [the matrix units lemma](/entry/etale-divisibility-key-criterion-of-components/) of the previous section. Representation gives $r$ with a subrepresentation datum $(A, B)$, and the finite subrepresentation statement gives that $r$ is semisimple, $A$ has rank $n$, and $r(g) = B \rho(g) A$. So $r$ is continuous, and claim 1 holds. Since $\chi_{r(g)}$ kills $r(g)$, it kills $\rho(g)$, which is claim 3. Since $P_s$ kills $\rho(s)$, it kills $r(s)$.

For claim 5, let $U$ be normal of finite index and $g \in \Gamma$. Part 1 of the key criterion gives $m \in \overline{\rho(U)}$ with $\rho(g) m$ of $n$ distinct eigenvalues. The algebraic part of dense separability gives $u \in U$ with $\chi_{r(gu)}$ separable. The topological part gives that the separable set $D$ is open and dense.

By the characteristic polynomial statement, $\chi_{r(s)} = P_s$ for $s \in S \cap D$. So $\det r(s) = (-1)^n P_s(0) = \psi(s)$ on $S \cap D$. This set is dense, as $S$ is dense and $D$ is open and dense. Both $\det r$ and $\psi$ are continuous into the Hausdorff space $K$, so $\det r = \psi$ on $\Gamma$. This gives claim 4. Claim 6 follows from the characteristic polynomial statement, with $\det r(s) = \psi(s) = (-1)^n P_s(0)$ in the case of generic products.

For claim 2, the embedding gives matrices $T_j$ and $T'_j$. Let $B$ be the matrix with the $T_j$ stacked as its blocks of rows, so $B \in M_{nk \times N}(K)$, and let $B'$ be the matrix with the $T'_j$ as its blocks of columns. Then $B' B = \sum_j T'_j T_j = 1$, so $B$ has rank $N$, and $(r(g) \otimes 1_k) B = B \rho(g)$ because each $T_j$ is an intertwiner. $\square$

**Remark 4.5.5.** The theorem asks that the roots $e_i$ be distinct and lacunary. A lacunary family is always injective: take $O = \{i\}$ and $O' = \{j\}$. So the first condition is redundant; see [OpenCoset.lean](lean:Development/EtaleCohomology/DivisorCycles/OpenCoset.lean#L12). The proof in the code drops it at once, in [DivPlus.lean](lean:Development/EtaleCohomology/DivisorCycles/DivPlus.lean#L41).

**Remark 4.5.6.** The Lean statement is a single proposition, and its proof applies one lemma to thirteen inputs. Each input is passed under the name `intersectionNumber_baseChange` of its own namespace; see [GoalHolds.lean](lean:Development/EtaleCohomology/DivisorCycles/GoalHolds.lean#L19). These names do not describe the statements, which are about matrices and compact groups. We did not open the proofs of the inputs, apart from the arguments given in this chapter; the proof above uses only their statements.

## Notes and references

The chapter feeds three parts of [the Galois row](/proof/galois-row/). The continuity of cohomology is an input to [the theorem that classes are killed on an étale neighbourhood](/entry/cont-of/), and through it to [the finiteness of étale cohomology](/entry/etale-topology-top/) in the step [GeoOne holds](/step/geo-one-holds/). The tensor product with flat complexes and the Kummer class are inputs to [the ring laws of the cup product](/entry/s41/) and [the naturality of the Kummer class](/entry/nat-kum/). Both lead to [the power-sum classes of vector bundles](/entry/s57/). The small subrepresentation is used in [the division of a Galois representation](/entry/div-set-holds/), which leads to [the odd finite seed](/entry/seed-fin-odd-of-geo-one/) and to the step [local-global compatibility from a geometric lift](/step/galois-local-global-strong-of-geometry-lift/).

J. S. Milne, *Étale Cohomology*, Chapter II, §2, for the Kummer sequence; Chapter III, §1, for the continuity of étale cohomology.

C. A. Weibel, *An Introduction to Homological Algebra*, Corollary 1.5.4, for the mapping cone and quasi-isomorphisms.

H. Matsumura, *Commutative Ring Theory*, Theorem 7.6, for the equational criterion of flatness.

A. Borel, *Linear Algebraic Groups*, Chapter I, §3, for the Lie algebra of an algebraic group.
