---
title: Class numbers for an open level
decls:
  - GlobalTheory.classNumberFinite_holds
  - GlobalTheory.T.isCompact_integralPoints_finiteAdelic_algebraicGroup
  - GlobalTheory.T.compact_meets_finitely_many_leftCosets_open
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Class numbers for an open level

This section proves the finiteness of class numbers in the form that the rest of the proof uses. For a linear algebraic group $G$ over a number field $F$ and an open subgroup $U$ of $G(\mathbb{A}_{F,f})$, the set of double cosets $G(F) \backslash G(\mathbb{A}_{F,f}) / U$ is finite. The last section proved this for the group of integral points in place of $U$. The integral points form a compact set, and a compact set meets only finitely many cosets of an open subgroup. This gives the general case.

### Two topological facts

Give $\mathbb{A}_{F,f}$ its restricted product topology ([adeles](/learn/number-fields/#adeles-and-ideles)), and $M_n(\mathbb{A}_{F,f})$ the product topology. Give $\mathrm{GL}_n(\mathbb{A}_{F,f})$ the topology for which $u \mapsto (u, u^{-1})$ is a homeomorphism onto its image in $M_n(\mathbb{A}_{F,f}) \times M_n(\mathbb{A}_{F,f})$. This is the topology of the [[adelic points|M07YRPQPX4]] of $\mathrm{GL}_n$ ([adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups)); it makes $\mathrm{GL}_n(\mathbb{A}_{F,f})$ a [topological group](/learn/analysis/#topological-groups-and-covering-maps). A subgroup of it has the subspace topology. Recall from the last section the sets $G_S(B)$ and the notion of an integral matrix.

**Lemma 1.6.1 (Integral points are compact).** Let $F$ be a number field, $S \subseteq F[x_{ij}]$ a set of polynomials, and $H \subseteq \mathrm{GL}_n(\mathbb{A}_{F,f})$ a subgroup with $H = G_S(\mathbb{A}_{F,f})$. Then the set of integral $u \in H$ is compact in $H$.

Lean: `GlobalTheory.T.isCompact_integralPoints_finiteAdelic_algebraicGroup`.

*Proof.* The ring $\widehat{\mathcal{O}} = \prod_v \mathcal{O}_v$ is compact, by Tychonoff's theorem, and closed in $\mathbb{A}_{F,f}$. The integral elements of $\mathrm{GL}_n(\mathbb{A}_{F,f})$ map under $u \mapsto (u, u^{-1})$ onto the pairs $(a, a')$ of matrices over $\widehat{\mathcal{O}}$ with $aa' = a'a = 1$. This is a closed subset of the compact space $M_n(\widehat{\mathcal{O}})^2$, so $\mathrm{GL}_n(\widehat{\mathcal{O}})$ is compact. Each $P \in S$ gives a continuous map $g \mapsto P(g)$ to the Hausdorff space $\mathbb{A}_{F,f}$, so $H$ is closed in $\mathrm{GL}_n(\mathbb{A}_{F,f})$. The set of integral $u \in H$ is $H \cap \mathrm{GL}_n(\widehat{\mathcal{O}})$, a closed subset of a compact set. A subset of $H$ that is compact in $\mathrm{GL}_n(\mathbb{A}_{F,f})$ is compact in $H$. $\square$

**Lemma 1.6.2 (A compact set meets finitely many cosets).** Let $G$ be a topological group, $U \subseteq G$ an open subgroup, and $K \subseteq G$ a compact set. Then there is a finite set $T \subseteq G$ such that every $k \in K$ is $k = tu$ with $t \in T$ and $u \in U$.

Lean: `GlobalTheory.T.compact_meets_finitely_many_leftCosets_open`.

*Proof.* The cosets $kU$, $k \in K$, are open and cover $K$. Choose finitely many, $t_1 U, \dots, t_m U$, that cover $K$, and let $T = \{t_1, \dots, t_m\}$. $\square$

### The theorem

**Theorem 1.6.3 (Finiteness of class numbers).** Let $F$ be a number field, $n \geq 0$, and $S \subseteq F[x_{ij}]$ a group locus. Let $H = G_S(\mathbb{A}_{F,f})$, and let $U \subseteq H$ be a subgroup that is open and compact in $H$. Then there is a finite set $T \subseteq H$ such that every $x \in H$ is
$$x = \gamma\, s\, u, \qquad \gamma \in G_S(F),\ s \in T,\ u \in U.$$

Lean: `GlobalTheory.classNumberFinite_holds`.

So $G_S(F) \backslash H / U$ is finite. For $G = \mathrm{GL}_1$ and $U = \widehat{\mathcal{O}}^\times$, the double cosets are the ideal classes of $F$ ([class group](/learn/number-fields/#adeles-and-ideles)), and the theorem is the finiteness of the class number of $F$.

*Proof.* By the [Theorem 1.5.8](/entry/class-finite-integral-level/) (class finiteness at the integral level), applied to $F$, $n$ and $S$, there is a finite set $T_0 \subseteq H$ such that every $x \in H$ is $x = \gamma s k$ with $\gamma \in G_S(F)$, $s \in T_0$ and $k \in H$ integral. Let $K$ be the set of integral elements of $H$. It is compact by the first lemma. Since $U$ is open in $H$, the second lemma, applied to the topological group $H$, gives a finite set $T_1 \subseteq H$ such that every $k \in K$ is $k = tu$ with $t \in T_1$ and $u \in U$. Let $T = \{ st : s \in T_0, t \in T_1 \}$. It is finite and lies in $H$. For $x \in H$ write $x = \gamma s k$ and $k = tu$. Then $x = \gamma\, (st)\, u$. $\square$

The proof does not use that $U$ is compact. It uses only that $U$ is an open subgroup.

**Remark 1.6.4 (Formalization).** In [ClassNumberFiniteHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ClassNumberFiniteHolds.lean#L13) the hypothesis that $U$ is compact is introduced with the name `_` and is not used. The statement proved is the proposition `HeckeCharacterZeroLocus.ClassNumberFinite`, whose group locus is `HeckeCharacterZeroLocus.IsGroupLocus` and whose group $H$ is `HeckeCharacterZeroLocus.locusSubgroup`; its topology is the one that Mathlib puts on the units of the topological ring $M_n(\mathbb{A}_{F,f})$, restricted to $H$. We have not checked the topology that Mathlib puts on $\mathbb{A}_{F,f}$; the text uses the restricted product topology. The two lemmas of this section are proved in the same folder by `GlobalTheory.IntegralPointsCompact.isCompact_integral_points` and `GlobalTheory.ClassFin.compact_subset_finite_leftCosets`; we have opened their statements, not their proofs, and the proofs given here are ours. The compactness lemma assumes only that $S$ cuts out $H$, not that $S$ is a group locus.

## Notes and references

This chapter proves the finiteness of class numbers of linear algebraic groups over number fields. The theorem of this section is used by the [theorem on the geometric realization of weight one](/entry/geometric-realization-of-weight-one/), which serves the step [GeoOne](/step/geo-one-def/) of [the Galois row](/proof/galois-row/). It is also used to show that the centraliser torus of a similitude group has finitely many classes.

The theorem is due to Borel. In its classical form: let $G$ be a linear algebraic group over a number field $F$ and $U$ an open compact subgroup of $G(\mathbb{A}_{F,f})$; then $G(F) \backslash G(\mathbb{A}_{F,f}) / U$ is finite. The form here is the same, with $G$ given by equations inside $\mathrm{GL}_n$. The treatment of a reductive group, by a rational tensor with a closed orbit and the reduction theory of $\mathrm{SL}_I$, is the method of Borel and Harish-Chandra. The treatment here differs in three points. All results over $\mathbb{Q}$ are proved over an arbitrary adelic pair $(R, R_0)$, of which $(\mathbb{A}_{\mathbb{Q},f}, \widehat{\mathbb{Z}})$ is the main example. A group is given by its complex points and its rational ideal, not as a scheme; the hypothesis on a reductive group is replaced by the complete reducibility of the natural representation. The unipotent part is removed by an induction on the dimension of the linear span of the group, with the block-diagonal part for a rational flag, and not by a Levi decomposition.

- A. Borel, "Some finiteness properties of adele groups over number fields", *Publ. Math. IHÉS* 16 (1963), Theorem 5.1.
- A. Borel and Harish-Chandra, "Arithmetic subgroups of algebraic groups", *Ann. of Math.* 75 (1962).
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*: Chapter 2, §2.1 (restriction of scalars), Chapter 4 (reduction theory and Siegel sets), Chapter 5, §5.1 (Theorem 5.1, finiteness of the class number), Chapter 8 (class numbers).
- J. E. Humphreys, *Linear Algebraic Groups*, §11.2 (Chevalley's theorem: a closed subgroup is the stabiliser of a line in a representation).
