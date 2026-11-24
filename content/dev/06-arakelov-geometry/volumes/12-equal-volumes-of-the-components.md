---
title: Equal volumes of the components
decls:
  - SheetDecomposition.arithIdx
  - SheetDecomposition.famVol
  - SheetDecomposition.ballVolEq
  - SheetDecomposition.degPush
  - SheetDecomposition.volEq_of_degPush
  - SheetDecomposition.volEq_of_isFullIntersectionSystem
  - GlobalTheory.CompanionTheory.Relay.good_tower_intersection_extra
  - GlobalTheory.T.good_tower_intersection_extra
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Equal volumes of the components

The volume theorem needs that all components of a good tower have the same volume. This section proves it when $q \ge 1$ and $3q + 1 \le p + q$. The proof computes one geometric degree in two ways. On the complex side, the base uniformization of [the previous section](/entry/base-unif-ex2/) writes the degree as a constant times the number of embeddings of the coefficient field times a ball volume, and the ball volumes of all pieces agree by an arithmetic statement on hermitian forms. On the tower side, a push forward formula writes the same degree as a nonzero constant times the volume of the component. Comparing the two gives the result. It is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/).

We keep the setting of [the previous section](/entry/base-unif-ex2/). Recall from [the tower conditions](/entry/full-intersection-tower-i8-identity/) that the volume of a component $c$ of a root tower $T$ is

$$
\operatorname{vol}(c) = \frac{\mathrm{geo}_{M_{2, c}}\big(\ell_\rho^{\,d}\big)}{\deg_{\mathrm{Fl}}(\rho)},
$$

the geometric number of a power of the linear root of the weight $\rho$ at the first level, divided by its flag degree. The tower has equal volumes if $\operatorname{vol}(c) = \operatorname{vol}(c')$ for all components $c, c'$. For a set $S \subseteq \mathcal{B}_q$ the ball measure is the integral of the ball density $\rho_q$ over $S$.

### Equal ball volumes

Let $G$ be an invertible hermitian matrix of size $j + j'$ over $E$, $L$ a lattice in $E^{j + j'}$, $\xi \in E$ nonzero with $\bar\xi = -\xi$, and $\mathfrak{a}$ a nonzero ideal of $\mathcal{O}_E$. We say that $L$ is self-dual for $\xi G$ if it is self-dual for the trace form of $\xi G$. The level group of $(G, L, \mathfrak{a})$ is a congruence subgroup of the unitary group of $G$ attached to $L$ and $\mathfrak{a}$. Two subgroups $A$, $B$ have equal index if the index of $A \cap B$ in $B$ equals the index of $A \cap B$ in $A$ and is finite. We also use a neatness condition on $\mathfrak{a}$ for complex conjugation. We do not unfold self-duality, the level groups or neatness.

**Theorem 9.12.1 (Hermitian forms of the same signature).** Let $E$ be a CM field, unramified over its maximal real subfield, and let $s$ be a family of embeddings of $E$ that meets every pair of conjugate embeddings. Let $0 < j$, $0 < j'$ and $j + j' \ge 3$. Let $G$, $G'$ be invertible hermitian matrices that both have signature $(j, j')$ at every $s_\tau$, let $L$, $L'$ be lattices, let $\xi \ne 0$ with $\bar\xi = -\xi$ be such that $L$ is self-dual for $\xi G$ and $L'$ for $\xi G'$, and let $\mathfrak{a} \ne 0$ be neat. Then there is $a \in \mathrm{GL}_{j+j'}(E)$ with

$$
a^{\mathsf{T}} G\, \bar a = G',
$$

such that $a$ conjugates the level group of $(G', L', \mathfrak{a})$ into the unitary group of $G$, and the level group of $(G, L, \mathfrak{a})$ and the conjugate of the level group of $(G', L', \mathfrak{a})$ have equal index.

Lean: `SheetDecomposition.arithIdx`

*Proof.* At each $s_\tau$ both forms are diagonalised to the same sign matrix. So $G$ and $G'$ have the same signature at every infinite place. Self-dual lattices for $\xi G$ and $\xi G'$ lie in one genus; with Landherr's theorem and the Hasse norm theorem for the quadratic extension $E$ over its real subfield, this gives a matrix $P$ with $P^{\mathsf{T}} G \bar P = G'$, and we take $a = P$.

Transport $L'$ by $a$ to a lattice $aL'$, self-dual for $\xi G$. The two self-dual lattices $L$ and $aL'$ for the same form lie in one genus, so they are locally conjugate at every prime, and the local conjugations give an adelic one. Conjugation by $a$ sends the level group of $(G', L', \mathfrak{a})$ to the level group of $(G, aL', \mathfrak{a})$, which lies in the unitary group of $G$. Since $0 < j < j + j'$ and $j + j' \ge 3$, the form $G$ has a nonzero isotropic vector, so $G$ is in the isotropic setting. In this setting the level groups of two lattices that are adelically conjugate, for a neat ideal, have equal index. $\square$

**Theorem 9.12.2 (Equal volumes of fundamental sets).** Let $D$, $D'$ be data, let $F$, $F'$ be universal families on their lattices with the same embeddings $\sigma$ and forms $\pm$ the forms of the data, with $0 < j$, $0 < j'$, $j + j' \ge 3$, and $\sigma_\tau(\sqrt{-d_H}) = i c_0$ with $c_0 > 0$ for all $\tau$. Let $\Gamma$, $\Gamma'$ be the level subgroups and $FF$, $FF'$ fundamental sets for them. Then $FF$ and $FF'$ have the same ball measure.

Lean: `SheetDecomposition.famVol`

*Proof.* The standard model statement writes each universal family, up to a measure preserving bijection of $\mathcal{B}_q$, as the ball model of a hermitian matrix $G$ over $E$ with a lattice $L$: the form of the family is the trace form of $-\xi G$, and the equivalence of $R(t)$ and $R(t')$ through an automorphism becomes the action of the corresponding unitary matrix by Möbius transformations on the ball. The level dictionary identifies the level group of the datum with the level group of $(G, L, \mathfrak{a})$ for the level ideal, and shows that $L$ is self-dual. The theorem on hermitian forms of the same signature gives $a$ relating the two forms, with level groups of equal index. A Möbius transformation preserves the ball measure, and fundamental sets of two groups of equal index, related by a conjugation, have the same measure. $\square$

**Theorem 9.12.3 (Equal ball volumes).** Assume the top level inputs. Let $E$ be abelian over $\mathbb{Q}$, let $B$ be a base uniformization of $Y$ for the right labels and $(j, j') = (p, q)$, and let $FF_k$ be fundamental sets for the pieces. If $q \ge 1$ and $3q + 1 \le p + q$, then

$$
\int_{FF_k} \rho_q(t)\, dt = \int_{FF_{k'}} \rho_q(t)\, dt
$$

for all pieces $k, k'$.

Lean: `SheetDecomposition.ballVolEq`

*Proof.* Fix two pieces $k$, $k'$. Normalise each universal family, replacing the form by its negative if needed, so that every embedding of the family sends $\sqrt{-d_H}$ to $i\sqrt{d_H}$; the fundamental sets and their ball measures do not change. A permutation $\pi$ of the CM types then makes the embeddings of the two normalised families equal, and permuting the coordinates by $\pi$ preserves fundamental sets and ball measures. The conditions give $0 < p$, $0 < q$ and $p + q \ge 3$, and $\sqrt{d_H} > 0$ since $d_H$ is prime. The theorem on fundamental sets applies to the two families, and the ball measure of a fundamental set is the integral of $\rho_q$ over it. $\square$

### The two degree formulas

Let $\mathrm{II}$ be a full intersection system and let $\mathrm{Or}$ be a component origin for component data $\mathrm{Dc}$ with Hodge data $\mathrm{Hd}$. Write $\deg_\mu(\mathrm{Hd})$ for the geometric degree of the reference line $\mu$ of the Hodge data, and $\deg(\mathrm{Or})$ for the degree of the origin.

**Theorem 9.12.4 (Push forward degree).** There is a function $c_0(f, p, q)$, nonzero for all arguments, with the following property. Assume the positivity of agreement, proportionality, the comparison input, the top level inputs and the integrability of points. Let $E$ be abelian over $\mathbb{Q}$, let $T$ have a good origin $o$ over a global model $Y$, let $o$ satisfy the extra conditions, let $\mathrm{II}$ be full, and let $1 \le q \le p$. For a component $a$ of $T$ and a component origin $\mathrm{Or}$ with base labels on the left, side labels on the right, Hodge-Tate free Hodge component, good, over the empty set of primes, and with the same generic point as the component $a$ of the tower,

$$
\deg_\mu(\mathrm{Hd}) = c_0(|\Psi|, p, q) \cdot \deg(\mathrm{Or}) \cdot [F : \mathbb{Q}] \cdot \operatorname{vol}(a).
$$

Lean: `SheetDecomposition.degPush`

*Proof.* The proof assembles statements on the push forward of geometric numbers along the map from the component data to the tower model: an equality of numbers obtained from point dimensions and pull backs, a geometric push forward formula, a fibre number formula, the transcendence degree of the universal family, a relabeling of tests, a formula for numbers of maps, the mass of $\mu$, a join of fields, a generic isomorphism, and two links through chart values, centres and coordinate lattices. Together they express $\deg_\mu$ as a product of a constant depending only on $(|\Psi|, p, q)$, the degree of the origin, the degree of the coefficient field and the geometric number that defines $\operatorname{vol}(a)$. $\square$

The complex side gives a second formula. There is a function $\kappa(f, j, j')$ such that for a locally constant base uniformization whose fundamental sets all have ball volume $v$, and a component origin of the same type as the uniformization with $1 \le j'$ and $3j' + 1 \le j + j'$,

$$
\deg_\mu(\mathrm{Hd}) = \kappa(|\Psi|, j, j') \cdot \deg(\mathrm{Or}) \cdot [F : \mathbb{Q}] \cdot v.
$$

Its proof cuts the complex points into sheets over the pieces, writes the degree as a sum over pieces of the number of sheets times the ball volume, and uses that for each embedding of $F$ exactly one piece meets a fixed open set around the generic point. So the number of pieces that meet it is $[F : \mathbb{Q}]$.

**Theorem 9.12.5 (Equal volumes from the push forward).** Assume the push forward degree statement. Assume the comparison input and the top level inputs. Let $E$ be abelian over $\mathbb{Q}$, let $T$ be a root tower with a good origin $o$ over $Y$, and let $\mathrm{II}$ be an intersection system. If $Y$ is global, $o$ satisfies the extra conditions, $\mathrm{II}$ is full, $q \ge 1$ and $3q + 1 \le p + q$, then $T$ has equal volumes.

Lean: `SheetDecomposition.volEq_of_degPush`

*Proof.* Take a locally constant base uniformization $B$ of $Y$ for the right labels and $(j, j') = (p, q)$. Each piece has a fundamental set for its group, and by the theorem on equal ball volumes all of them have the same ball volume $v$.

Fix a component $a$. The generic bound for full intersection systems gives component data, Hodge data and a component origin $\mathrm{Or}$ over the bad primes, with base labels on the left, $j = p$, $j' = q$, a Hodge-Tate free Hodge component, good, over the empty set, and with the generic point of the origin of $o$ at level $2$ and component $a$. The side labels of $\mathrm{Or}$ are on the right, since $\Psi$ is nonempty. The complex formula gives $\deg_\mu = \kappa\, \deg(\mathrm{Or})\, [F : \mathbb{Q}]\, v$. The push forward formula, with $1 \le p$ and $q \le p$ from $3q + 1 \le p + q$, gives $\deg_\mu = c_0\, \deg(\mathrm{Or})\, [F : \mathbb{Q}] \operatorname{vol}(a)$. The degree of the origin is positive and $[F : \mathbb{Q}] > 0$, so

$$
c_0(|\Psi|, p, q) \operatorname{vol}(a) = \kappa(|\Psi|, p, q)\, v.
$$

The right side does not depend on $a$, and $c_0 \ne 0$. So $\operatorname{vol}(a) = \operatorname{vol}(a')$ for all $a, a'$. $\square$

**Theorem 9.12.6 (Good towers have equal volumes).** Assume the comparison input and the top level inputs. Under the hypotheses of the previous theorem, $T$ has equal volumes.

Lean: `SheetDecomposition.volEq_of_isFullIntersectionSystem` (also `GlobalTheory.CompanionTheory.Relay.good_tower_intersection_extra` and `GlobalTheory.T.good_tower_intersection_extra`, second names)

*Proof.* Apply the previous theorem to the push forward degree statement. $\square$

The condition $3q + 1 \le p + q$, that is $p \ge 2q + 1$, enters through the complex formula and through $q \le p$ in the push forward formula. The arithmetic theorem is where the classical inputs sit: Landherr's theorem says that a hermitian form over a CM field is determined by its local invariants and its signatures, and the genus argument with the isotropic vector controls the index of the level groups.

**Remark 9.12.7 (Formalization).** The push forward theorem takes the positivity of agreement, proportionality and the integrability of points as hypotheses, but the proof of equal volumes discharges them with theorems of the development: `GlobalTheory.T.agreement_positive`, `GlobalTheory.T.proportional'`, and a theorem that derives integrability from the resolution statement in the top level inputs ([VolEqOf.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/VolEqOf.lean#L92)). Elsewhere in the chapter the positivity of agreement is a hypothesis of the theorem on [good towers being linked](/entry/good-origin-linked/). The theorem on equal volumes is a second name for the one from the push forward, and the two relays add nothing. The statement of the push forward theorem fixes $c_0$ before all other data, so the constant depends only on $(|\Psi|, p, q)$. We have not unfolded the definition of self-duality, of neat ideals, of the genus statement, of the sheets, or of the inputs of the push forward theorem; the proofs of the arithmetic theorem and of the push forward theorem are described by the names of the steps. The reading of the arithmetic theorem through Landherr's theorem follows the names `GlobalTheory.QNorm.landherr_and_landherrSt` and `GlobalTheory.T.hasse_norm_theorem_quadratic_extension` used in its proof ([BallVolArith.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/BallVolArith.lean#L113)).
