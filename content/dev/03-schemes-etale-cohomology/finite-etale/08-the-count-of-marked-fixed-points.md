---
title: The count of marked fixed points
decls:
  - UpperTheory.Cb.complex_count_regular_marked_points
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The count of marked fixed points

The Lefschetz formula of the last section turns the trace of a Hecke correspondence on the Dolbeault cohomology of a [Shimura variety](/learn/geometry/#shimura-varieties-and-toroidal-compactifications) into a weighted count of fixed points. The Galois row then needs this count as a sum over conjugacy classes in a group, so that it can compare it with an automorphic trace. This section does the first regrouping. It writes the weighted count as a sum over classes of *marked* pairs: an element $\gamma$ of a unitary similitude group, together with the eigenvalue of $\gamma$ on the line that it fixes. The proof only reorders a finite sum, but it needs three finiteness facts and one uniqueness fact. The result (Theorem 5.8.4) feeds [the count over definite pairs](/entry/weighted-count-definite-unitary/), which is the first input of [the theorem that Hecke eigensystems occur in Dolbeault cohomology](/entry/ks-hodge-of-geo/).

**Definition 5.8.1 (Group datum).** A *group datum* $G$ at a prime $p$ consists of a CM field $F$, a central simple $F$-algebra $C$ of dimension $n^2$ with an involution of the second kind, and for each infinite place $v$ of $F$ a map $\psi_v : C \to M_n(\mathbb{C})$ and a hermitian matrix $H_v$ of signature $(1, n - 1)$ or $(0, n)$, with further data at $p$. Let $a(G)$ be the number of places $v$ where $H_v$ has signature $(1, n - 1)$.

When $a(G) = 1$ and $v$ is the place of signature $(1, n - 1)$, the vectors $z \in \mathbb{C}^n$ with $z^* H_v z > 0$ form a complex ball, and the Shimura variety of $G$ is a union of quotients of this ball. A point of the variety is given by an adelic coset and a line of positive norm.

**Definition 5.8.2 (Weighted fixed-point count).** Let $G$ be a group datum with $a(G) = 1$ and let $v$ be the place of signature $(1, n - 1)$. Let $c : F[x] \times \mathbb{C} \to \mathbb{C}$ be a function, the *weight*. Let $f$ be a test function on the finite adeles at a level $L$, and $f'$ a test function at $p$. For a form $\beta$ in $C^\times$ fixed by the involution, let $\mathrm{Pts}(\beta)$ be the set of classes of points $(g, g_p, z)$, with $z$ a vector of positive norm for the form of $\beta$ at $v$, and let $\mathrm{Stab}(q)$ be the stabilizer of a point $q$. An element $y$ of the similitude group of $\beta$ *fixes the line* of $z$ if $\psi_v(y) z = \mu z$ for some $\mu \in \mathbb{C}$, and then $\mu_y = \mu$. The *weighted count* is
$$
\begin{aligned}
\mathrm{cxTotal}(c, f, f') = \sum_{[\beta]} \sum_{q \in \mathrm{Pts}(\beta)} \frac{1}{|\mathrm{Stab}(q)|} \sum_{y \text{ fixes } z_q} &f\bigl(g_q^{-1} y g_q\bigr) f'\bigl(g_{p,q}^{-1} y g_{p,q}\bigr) \\
&\cdot c\bigl(P_y, \mu_y\bigr),
\end{aligned}
$$
where $[\beta]$ runs over the classes of forms and $P_y$ is the minimal polynomial of $y$ over $F$.

**Definition 5.8.3 (Marked pair).** A *pair* $P = (\beta, \gamma, \lambda)$ is a form $\beta$ and an element $\gamma \in C^\times$ that is a similitude of $\beta$ with factor $\lambda \in \mathbb{Q}^\times$, with local conditions. Its polynomial $P_\gamma$ is the minimal polynomial of $\gamma$ over $F$, and its term $\mathrm{term}(P)$ is a sum of values of $f$ and $f'$ over the points of the pair. A *mark* of $P$ is a $\mu \in \mathbb{C}$ such that, for some infinite place $w$ of signature $(1, n - 1)$, $\mu$ is an eigenvalue of $\psi_w(\gamma)$ with an eigenvector of positive norm for the form $H_w \psi_w(\beta^{-1})$.

**Theorem 5.8.4 (Weighted count as a sum over marked pairs).** Let $G$ be a group datum with $a(G) = 1$, and let $v$ be the place of signature $(1, n - 1)$. Let $c$ be any weight, let $f$ be a test function at a level $L$ such that $f(g) \neq 0$ only for regular elements $g$, and let $f'$ be a test function at $p$. Then
$$
\mathrm{cxTotal}(c, f, f') = \sum_{[P] \text{ marked by } \mu} c(P_\gamma, \mu) \, \mathrm{term}(P),
$$
where the sum runs over the classes of pairs that have a mark $\mu$.

Lean: `UpperTheory.Cb.complex_count_regular_marked_points`.

*Proof.* We give the proof in three steps.

First, three facts make the sums finite and the eigenvalues well defined.
1. For each line of positive norm, only finitely many $y$ fix it with $f \cdot f' \neq 0$.
2. Only finitely many classes of points give a nonzero contribution. This uses that $f$ has regular support.
3. An element $y$ in the support fixes at most one line of positive norm. This follows from the separability of $P_y$, which follows from the regular support of $f$, and from the signature $(1, n - 1)$ of $H_v$.

By the third fact, $\mu_y$ depends only on $y$, not on the point. If $y$ comes from a marked pair, $\mu_y$ is the mark.

Second, we write the left side by conjugacy classes. Fix a form $\beta$. The sum over points is a sum over orbits of the similitude group of $\beta$. The summand does not change when $y$ is replaced by a conjugate and the point is moved with it. So the sum over points and elements regroups as a sum over conjugacy classes $[y]$ of sums over orbits of the centralizer of $y$. For one class $[y]$, this inner sum is a class weight $w(y)$: a weight of the centralizer times a point sum of Kottwitz type for $y$, multiplied by $c(P_y, \mu_y)$.

Third, we write the right side by forms. A marked pair has similitude factor $\lambda > 0$, and its mark is unique. A class of pairs with $\lambda > 0$ gives a class of forms $\beta$ and a conjugacy class in the similitude group of $\beta$, and on each fibre over a class of forms this is a bijection. On each fibre the summand $c(P_\gamma, \mu) \mathrm{term}(P)$ equals the class weight $w(y)$ of a representative. So both sides equal $\sum_{[\beta]} \sum_{[y]} w(y)$. $\square$

**Remark 5.8.5.** A mark asks for some place of signature $(1, n - 1)$, not for the place $v$ of the count. Since $a(G) = 1$, there is only one such place, so this is the same. The theorem holds for every weight $c$, and it does not need $n$ odd or any condition on pairs with reducible polynomial. Those conditions enter only in the next step, which moves the marked sum to a sum over definite pairs, in [the count over definite pairs](/entry/weighted-count-definite-unitary/).

**Remark 5.8.6 (Formalization).** The sum on the right picks the mark by a choice function, which is harmless because the mark is unique. The eigenvalue $\mu_y$ in the count is also defined by a choice, and it is set to $0$ when $y$ fixes no line, a case that the count never uses. The three facts of the first step were read as statements, not proofs. We have not unfolded the term of a pair, the point sum, or the set of points.

## Notes and references

The chapter feeds three parts of the Galois row. The scheme of subgroups of the torsion of an abelian scheme is used in the first step of [the representability of isogenies of type $T_j$](/entry/isogeny-rep/), and the isogenies with a given kernel are used for the quotient objects in the chapter on Galois representations. The neighbourhood lemma is an input to [the finiteness of étale cohomology](/entry/etale-topology-top/) of proper schemes, and the projective bundle formula is an input to [the formula on discrete spaces](/entry/pbf-disc/). The holomorphic Lefschetz formula and the count of marked fixed points are the two inputs of [the theorem that Hecke eigensystems occur in Dolbeault cohomology](/entry/ks-hodge-of-geo/), in [the geometric realization of weight one](/entry/geometric-realization-of-weight-one/). This is the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/), which builds the Galois representations of weight one from the cohomology of a tower of unitary Shimura varieties.

A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, for the Hilbert scheme in the proof of Theorem 5.1.4.

S. Bosch, W. Lütkebohmert and M. Raynaud, *Néron Models*, §7.6, for the Weil restriction. It gives the scheme of clopen subsets without the noetherian hypothesis.

M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Ann. of Math. Stud. 151, Chapter III, for the moduli problem of Section 5.3 and its isogenies.

J. S. Milne, *Étale Cohomology*, Chapter I, §4, for henselian rings and the strict henselization; Chapter III, §1, for the continuity of étale cohomology; Chapter VI, §10, for the projective bundle formula.

SGA 5, Exposé VII, for the projective bundle formula and Chern classes in étale cohomology.

M. F. Atiyah and R. Bott, *A Lefschetz fixed point formula for elliptic complexes. II. Applications*, Ann. of Math. 88 (1968), §4, for the holomorphic Lefschetz formula. Their formula is for a holomorphic map with nondegenerate fixed points. Theorem 5.7.3 is an algebraic form for a correspondence, and it takes the finite set of fixed points and the cotangent matrices as inputs.
