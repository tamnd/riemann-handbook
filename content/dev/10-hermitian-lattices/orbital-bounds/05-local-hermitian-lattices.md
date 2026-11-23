---
title: Local facts on Hermitian lattices
decls:
  - local_density_corank
  - square_pair_local
  - split_pair_generation
  - unimodular_local_standard
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local facts on Hermitian lattices

This section proves four facts about Hermitian lattices that are local at a prime. The first computes the local density of a form $A^* \operatorname{diag}(a) A$ against a self-dual lattice, at both inert and split places. The second and third build an approximate idempotent that is compatible with two self-dual lattices at once, first at one prime and then globally. The fourth moves a self-dual lattice of a CM elliptic type by an isometry so that its index relative to the standard lattice is prime to a given prime. These facts are used in the [standard frame at a place](/entry/local-standard/) and in the steps that need [nonempty hypotheses](/step/nonempty-hyps/). For the background see [rings, ideals and modules](/learn/algebra/#rings-ideals-and-modules) and [number fields and their integers](/learn/number-fields/#number-fields-and-their-integers).

### Local densities

We use the setting of the section on [local densities and the local mass of a type](/entry/local-mass-type-of-parts/). So $F$ is a nonarchimedean local field with residue field of order $q$, and $E$ is a commutative $F$-algebra of rank $2$ with an involution $x \mapsto \bar x$ whose fixed ring is $F$, unramified in the sense used there. Then $V$ is a free $E$-module of rank $n$ with a nondegenerate Hermitian form, $\Lambda \subseteq V$ is a lattice, $\delta_\Lambda(G)$ is the local density of an $I \times I$ matrix $G$, and $P_\eta(q; n, m, c)$ is the product of local factors.

**Theorem 4.5.1 (Local density by corank).** Let $F$ have characteristic $0$. Let $\Lambda$ be a self-dual lattice in $V$, let $\varpi \in \mathcal{O}_F$ be irreducible, let $I$ be a finite set with $|I| \leq n$, let $A$ be an $I \times I$ matrix with entries in $\mathcal{O}_E$ and with $\det A$ a unit of $\mathcal{O}_E$, and let $a = (a_i)_{i \in I}$ be a family in $\mathcal{O}_F$. Put $\eta = -1$ if every nonzero element of $E$ is a unit, and $\eta = 1$ otherwise. Let $c$ be the number of $i$ with $\varpi \mid a_i$. Then
$$\delta_\Lambda\big(\bar A^{\mathsf T} \operatorname{diag}(a) A\big) = P_\eta(q; n, |I|, c).$$

Lean: `local_density_corank`.

Here $\eta = -1$ is the case where $E$ is the unramified quadratic field extension of $F$, and $\eta = 1$ is the case where $E$ is not a field. Since $\det A$ is a unit, $c$ is the corank modulo $\varpi$ of the form $\bar A^{\mathsf T} \operatorname{diag}(a) A$.

*Proof.* This is a reduction lemma applied to two proved counts. The first is the theorem on the [local density of a diagonal form](/entry/field-count-holds/) at an inert place, which gives the case $\eta = -1$. The second is the same count at a split place, which gives the case $\eta = 1$. The reduction lemma derives the theorem from the two counts; we did not unfold how it passes from $\operatorname{diag}(a)$ to $\bar A^{\mathsf T} \operatorname{diag}(a) A$. $\square$

**Example 4.5.2.** Let $|I| = 1$, $a = (1)$ and $A = (1)$. Then $c = 0$, and the product has the single factor $i = n$. So $\delta_\Lambda(1) = 1 - \eta^n q^{-n}$. At an inert place this is $1 - (-1)^n q^{-n}$, which is the proportion of vectors of norm $1$ among the $q^{2n - 1}$ that the denominator counts.

### Square pairs

Let $E$ be a number field with an involution $x \mapsto \bar x$. Let $E$ be *CM and unramified*, as in the section on [approximate Lagrangian projections](/entry/sq-pair-local-of/). On $E^N$ we use the form $h(x, y) = \sum_i \bar x_i y_i$. A *self-dual lattice* $L \subseteq E^N$ is a finitely generated $\mathcal{O}_E$-submodule that spans $E^N$ and satisfies $y \in L$ exactly when $h(x, y) \in \mathcal{O}_E$ for all $x \in L$. For a matrix $e$ write $e^* = \bar e^{\mathsf T}$.

**Theorem 4.5.3 (Square pairs at every prime).** Let $E$ be CM and unramified, let $N$ be even, let $L'$ and $L''$ be self-dual lattices in $E^N$, let $n \in \mathcal{O}_E$ be nonzero, and let $p$ be a prime. Then there is $e \in M_N(E)$ with $e L' \subseteq L'$ and $e L'' \subseteq L''$ such that, for every
$$M \in \{\, e^2 - e,\ e^* e,\ (1 - e)^*(1 - e) \,\}$$
and every $y \in L' \cup L''$, there are $s \in \mathbb{Z}$ with $p \nmid s$ and $m \in L' \cap L''$ with $s \cdot M y = n \cdot m$.

Lean: `square_pair_local`.

*Proof.* This is [square pairs at a prime](/entry/sq-pair-local-of/) applied to the local Cartan pair theorem. That theorem, which is proved, says the following. Let $R$ be a commutative ring with an involutive automorphism $\sigma$ whose fixed ring $R_0$ is a Henselian discrete valuation ring with finite residue field, and let $\theta - \sigma\theta$ be a unit for some $\theta \in R$. Let $\varpi \in R_0$ be irreducible, $N$ even, and $h \in M_N(R)$ with $\sigma(h)^{\mathsf T} h = \varpi^{2k}$. Then there are $e, f \in M_N(R)$ with $e^2 = e$, $\sigma(e)^{\mathsf T} = 1 - e$ and $e h = h f$. $\square$

**Theorem 4.5.4 (Square pairs).** Let $E$ be CM and unramified, let $N$ be even, let $L'$ and $L''$ be self-dual lattices in $E^N$, and let $n \in \mathcal{O}_E$ be nonzero. Then there is $e \in M_N(E)$ with $e L' \subseteq L'$ and $e L'' \subseteq L''$ such that, for every $M \in \{ e^2 - e, e^* e, (1 - e)^*(1 - e) \}$ and every $y \in L' \cup L''$, there is $m \in L' \cap L''$ with $M y = n \cdot m$.

Lean: `split_pair_generation`.

*Proof.* This is a gluing lemma applied to the theorem on square pairs at every prime. The gluing lemma is proved; it derives the global statement, with no factor $s$, from the statement at every prime $p$. We did not unfold its proof. $\square$

The matrix $e$ is close to an orthogonal projection onto a Lagrangian subspace: $e^2 - e$, $e^* e$ and $(1-e)^*(1-e)$ all vanish modulo $n$ on both lattices. So $e$ and $1 - e$ behave modulo $n$ like complementary isotropic projections, for $L'$ and for $L''$ at the same time.

### A standard lattice of CM type

Let $a \geq 1$, $b, c \in \mathbb{Z}$ and $d \geq 1$ with
$$4ac = b^2 + d, \qquad a \text{ odd}, \qquad d \equiv 7 \pmod 8, \qquad d \text{ prime}.$$
Put $\theta = (b + i \sqrt{d})/2$. For $\lambda \in \mathbb{C}^\times$ let $L = \lambda(a \mathbb{Z} + \theta \mathbb{Z})$, a lattice in $\mathbb{C}$, and let $A(L)$ be the area of a fundamental parallelogram. Let $m$ be a finite set. On $\mathbb{C}^m$ put the Hermitian form
$$H(z, w) = \frac{1}{A(L)} \sum_{i \in m} z_i \bar w_i.$$
For an additive subgroup $\Lambda \subseteq \mathbb{C}^m$ let $\Lambda^\vee$ be the set of $x$ with $\operatorname{Im} H(x, y) \in \mathbb{Z}$ for all $y \in \Lambda$, and call $\Lambda$ *self-dual* if $\Lambda^\vee = \Lambda$. For subgroups $\Lambda_1, \Lambda_2$ let $[\Lambda_2 : \Lambda_1 \cap \Lambda_2]$ be the index, read as $0$ when it is infinite. Two subgroups are *commensurable* if both indices $[\Lambda_2 : \Lambda_1 \cap \Lambda_2]$ and $[\Lambda_1 : \Lambda_1 \cap \Lambda_2]$ are nonzero.

**Theorem 4.5.5 (Unimodular local standard).** Let $a, b, c, d$ and $\lambda$ be as above, and let $\Lambda_a \subseteq \mathbb{C}^m$ be a self-dual subgroup with $\theta \Lambda_a \subseteq \Lambda_a$ that is commensurable with $L^m$. Then for every prime $l$ there is a $\mathbb{C}$-linear isometry $\delta$ of $(\mathbb{C}^m, H)$ with no nonzero fixed vector, such that $\delta \Lambda_a$ is commensurable with $L^m$ and
$$l \nmid [\delta \Lambda_a : L^m \cap \delta \Lambda_a].$$

Lean: `unimodular_local_standard`.

*Proof.* This is a reduction to a representation statement. A reduction lemma derives the conclusion from a key representation property at the prime $l$. That property is derived from its form at the ramified prime, and that form from the existence of a suitable unit vector at the ramified prime. All three lemmas are proved. The key property asks, roughly, for a saturated vector that vanishes on a given sublattice and on which a quadratic form takes a value prime to $l$. We did not unfold how the isometry $\delta$ is built from it. $\square$

The condition $d \equiv 7 \pmod 8$ says that $2$ splits in $\mathbb{Q}(\sqrt{-d})$, since $-d \equiv 1 \pmod 8$. Since $d$ is odd, $b$ is odd, and $\mathbb{Z}[\theta]$ is the ring of integers of $\mathbb{Q}(\sqrt{-d})$. The lattice $a\mathbb{Z} + \theta\mathbb{Z}$ is an ideal of it, because $\theta^2 = b\theta - ac$ by $4ac = b^2 + d$.

**Remark 4.5.6 (Formalization).** In the density theorem the hypothesis $|I| \leq n$ is part of the statement. The section on local densities notes that the proof of the inert count does not use it; we did not check whether the split count does. The index of the unimodular theorem is the relative index of subgroups, which is $0$ when it is infinite; this is why commensurability is stated by nonzero indices, see [UnimodLocStd.lean](lean:Formalism/PeriodIntegrals/UnimodLocStd.lean#L112). The reduction lemma for densities, the gluing lemma for square pairs and the three lemmas on the CM lattice were not unfolded beyond their statements, and the key representation property only in part. The four theorems are in [LocDensCorank.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LocDensCorank.lean#L7), [SqPairLocal.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/SqPairLocal.lean#L6), [SplitPairGen.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/SplitPairGen.lean#L5) and [UnimodLocStd.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnimodLocStd.lean#L6).
