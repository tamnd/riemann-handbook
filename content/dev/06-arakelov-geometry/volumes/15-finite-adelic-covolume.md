---
title: Finite adelic covolume
decls:
  - GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_remaining
  - GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_open
  - GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_covolume
  - GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicLatticeDictionary.full
  - GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicLatticeDictionary.proof
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finite adelic covolume

This section proves that the rational points of a unitary group are a lattice of finite covolume in its adelic points. The proof passes from the adelic group to the arithmetic groups of integral lattices, through a dictionary between finite adelic points and lattices, and then uses the finiteness of the covolume of each arithmetic group. It is used by the [finiteness of the adelic covolume](/entry/adelic-covolume-finite/), which removes the last hypotheses. Finite covolume is what makes the Haar measure of a fundamental domain of the rational points a finite number, as in the volume statement of the previous section. The lattices here are [hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes) over a CM field.

Let $F$ be a totally real number field and $E$ a totally complex quadratic extension of $F$. Let $W$ be a finite dimensional vector space over $E$ with a nondegenerate hermitian form $h$ and a basis $v$. We write $U_h$ for the unitary group of $h$ over $F$, $U_h(\mathbb{A})$, $U_h(\mathbb{A}_\infty)$ and $U_h(\mathbb{A}_f)$ for its points over the adeles, the infinite adeles and the finite adeles of $F$, in the matrix form given by the Gram matrix of $v$. The group $U_h(F)$ embeds diagonally in $U_h(\mathbb{A})$. The group $U_h(\mathbb{R})$ is the product over the infinite places $w$ of $E$ of the unitary groups of the Gram matrix at $w$, and $U_h(F)$ maps into it by the embeddings of $E$.

**Definition 9.15.1 (Integral lattices).** For an integer $D \ge 1$, a subgroup $\Lambda$ of $W$ is $D$-integral if it is a lattice of $W$, the form $h$ takes integral values on $\Lambda$, and the index of $\Lambda$ in its dual lattice is nonzero and at most $D$. For such $\Lambda$ the arithmetic group $\Gamma_\Lambda$ is the image in $U_h(\mathbb{R})$ of the stabilizer of $\Lambda$ in $U_h(F)$.

**Definition 9.15.2 (The covolume statements).** The arithmetic covolume statement says: for every Haar measure on $U_h(\mathbb{R})$, every $D$ and every $D$-integral $\Lambda$, the group $\Gamma_\Lambda$ has a fundamental domain of finite measure. The adelic covolume statement says: for every Haar measure on $U_h(\mathbb{A})$, the diagonal image of $U_h(F)$ has a fundamental domain of finite measure.

**Definition 9.15.3 (The lattice dictionary).** The adelic lattice dictionary for $h$ and $v$ says: there are a compact open subgroup $K$ of $U_h(\mathbb{A}_f)$, an integer $D$ and a map $g \mapsto L(g)$ from $U_h(\mathbb{A}_f)$ to the subgroups of $W$ such that

1. every $L(g)$ is $D$-integral;
2. $L(\gamma_f\, g) = \gamma\, L(g)$ for $\gamma \in U_h(F)$, where $\gamma_f$ is the finite part of $\gamma$;
3. $L(g) = L(g')$ if and only if $g^{-1} g' \in K$.

The dictionary is the familiar bijection between $U_h(\mathbb{A}_f)/K$ and the lattices in the genus of a fixed lattice, written so that the action of the rational points is visible.

**Theorem 9.15.4 (The lattice dictionary).** The adelic lattice dictionary holds for every $h$ and $v$.

Lean: `GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicLatticeDictionary.proof` (also `GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicLatticeDictionary.full`, a second name)

*Proof.* Fix a basis of $E$ over $F$. It defines an integral core in the finite adelic vectors: the vectors $u$ such that $\beta u$ lies in the standard integral lattice for every integer $\beta$ of $E$. Let $K$ be the set of $g \in U_h(\mathbb{A}_f)$ such that $g$ and $g^{-1}$ map the integral core into itself. This is an open subgroup, and it is compact; the compactness uses that the Gram matrix has a unit determinant. For $g \in U_h(\mathbb{A}_f)$, the core lattice of $g$ is the set of rational vectors $x$ with $g^{-1} x$ in the integral core.

There is a nonzero integer $d$ such that $d$ times the hermitian pairing of two vectors of any core lattice is integral, and a nonzero integer $m$ such that $m y$ lies in the core lattice of $g$ whenever $y$ pairs integrally with that core lattice. Put

$$
L(g) = \{ x \in W : \text{the coordinates of } d^{-1} x \text{ lie in the core lattice of } g \}.
$$

Then $L(g)$ is a finitely generated subgroup that spans $W$, since a multiple of each basis vector lies in it. The pairing is integral on $L(g)$ by the choice of $d$. The dual of $L(g)$ is contained in a fixed multiple of $L(g)$ by the choice of $m$, so the index of $L(g)$ in its dual is nonzero and at most

$$
D = |m d^2|^{N}
$$

where $N$ is the rank over $\mathbb{Z}$ of $\mathcal{O}_F^{\iota \times \kappa}$, with $\iota$ indexing $v$ and $\kappa$ indexing the basis of $E$ over $F$. So every $L(g)$ is $D$-integral. The core lattice of $\gamma_f g$ is $\gamma$ applied to the core lattice of $g$, which gives the second property. Two core lattices are equal exactly when $g^{-1} g'$ lies in $K$, and the coordinate map is a bijection, which gives the third. $\square$

**Theorem 9.15.5 (Adelic covolume from the arithmetic covolume).** If the arithmetic covolume statement holds for $h$ and $v$, then the adelic covolume statement holds for $h$ and $v$.

Lean: `GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_covolume`

*Proof.* We use four further facts, all proved: there are finitely many $U_h(F)$-orbits of $D$-integral lattices for each $D$; there is a topological isomorphism $\psi$ from $U_h(\mathbb{A}_\infty)$ to $U_h(\mathbb{R})$ that carries the infinite part of $\gamma$ to the image of $\gamma$; the lattice dictionary; and the double coset lemma below.

The double coset lemma says: let $G \cong G_1 \times G_2$ be topological groups with $G_1$ locally compact, Hausdorff and second countable, let $\Gamma$ be a countable subgroup of $G$, $K$ a compact open subgroup of $G_2$ and $S$ a finite subset of $G_2$. Assume that an element of $\Gamma$ with trivial first component is trivial, that $G_2 = \Gamma_2 S K$, where $\Gamma_2$ is the set of second components of $\Gamma$, and that for every $s \in S$ the slice group

$$
\Gamma_s = \{ \gamma_1 : \gamma \in \Gamma,\ s^{-1} \gamma_2 s \in K \}
$$

has a fundamental domain of finite Haar measure in $G_1$. Then $\Gamma$ has a fundamental domain of finite Haar measure in $G$.

Apply it with $G = U_h(\mathbb{A})$, $G_1 = U_h(\mathbb{R})$ and $G_2 = U_h(\mathbb{A}_f)$, through the splitting of the adeles and $\psi$, and with $\Gamma = U_h(F)$. The group $U_h(F)$ is countable, since $E$ is countable and $U_h(F)$ is a set of matrices over $E$. An element of $U_h(F)$ whose image at one infinite place of $E$ is the identity is the identity, since the embedding is injective. Take $K$ and $L$ from the dictionary, and a finite set $S_0$ of representatives of the orbits of $D$-integral lattices. For each lattice in $S_0$ of the form $L(y)$ choose such a $y$, and let $S$ be the set of these choices.

Every $y \in U_h(\mathbb{A}_f)$ lies in $U_h(F)\, S\, K$. Indeed, $L(y)$ is $D$-integral, so $L(y) = g\, L_0$ for some $g \in U_h(F)$ and $L_0 \in S_0$. Then $L_0 = L(g_f^{-1} y)$, so $L_0 = L(s)$ for the chosen $s \in S$, and $L(g_f s) = g L_0 = L(y)$, which gives $(g_f s)^{-1} y \in K$.

For $s \in S$, the element $\gamma$ stabilizes $L(s)$ if and only if $L(\gamma_f s) = L(s)$, that is, $s^{-1} \gamma_f s \in K$. So the slice group $\Gamma_s$ is the arithmetic group $\Gamma_{L(s)}$, which has finite covolume by hypothesis. The double coset lemma gives the claim. $\square$

**Theorem 9.15.6 (Adelic covolume from the open statements).** Assume, for all hermitian spaces over $E$ with bases indexed by $\{1, \ldots, n\}$ and for the given $h$ and $v$, the archimedean unimodularity, the compactness of the stabilizer of a majorant, the Haar measure of a line stabilizer, the covering by the semidirect product, the Levi decomposition of a stabilizer, the modulus of the unipotent radical and its cocompactness, and, for all hermitian spaces, the congruence lift statement. Then the adelic covolume statement holds for $h$ and $v$.

Lean: `GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_open`

*Proof.* These hypotheses give the arithmetic covolume statement. The argument is reduction theory by induction on the dimension: the stabilizer covolume statement follows from the Levi decomposition, the semidirect covering, the modulus and the cocompactness of the unipotent radical and the congruence lift, the Haar measure in parabolic coordinates unfolds the covolume along that stabilizer, and the reduced basis bound with the finiteness of lattice points below a bound controls the rest. The previous theorem then gives the adelic statement. $\square$

**Theorem 9.15.7 (Adelic covolume from the remaining statements).** Assume, in the same two forms, the torus embedding, line eigenvalue, torus modulus, semidirect Haar, unipotent properness, unipotent horizontal and unipotent central statements, and the invariance of Haar measure under units. Then the adelic covolume statement holds for $h$ and $v$.

Lean: `GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_remaining`

*Proof.* The archimedean unimodularity, the compactness of the majorant stabilizer, the covering by the semidirect product, the Levi decomposition, the modulus of the unipotent radical and the congruence lift are proved outright. The Haar measure of a line stabilizer follows from the torus embedding, line eigenvalue, torus modulus, semidirect Haar and unit invariance statements, with the existence of a Witt partner of an isotropic vector and the existence of a coordinate that does not vanish. The cocompactness of the unipotent radical follows from the three unipotent statements. The previous theorem applies. $\square$

The finiteness theorem with no hypotheses is the parent result; it supplies the eight remaining statements, each of which is proved in the development. The result is a case of the theorem of Borel and Harish-Chandra on arithmetic subgroups of reductive groups, proved here for unitary groups of hermitian spaces over a CM field by a reduction to integral lattices.

**Remark 9.15.8 (Formalization).** The four theorems on the adelic statement are reductions; the actual argument is `AdelicCovolumeFinite.proof` in [PAdelicCovolumeFinite.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/PAdelicCovolumeFinite.lean#L44), called through `AdelicCovolumeFinite.full_of`, which is a second name for it ([Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/Assembly.lean#L337)). `AdelicLatticeDictionary.full` is a second name for `AdelicLatticeDictionary.proof` ([OfUnfolding.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/OfUnfolding.lean#L74)). In [MainOf.lean](lean:GroundTheory/HeightsAndTheta/Heights/FiniteCovolume/MainOf.lean#L24) each remaining statement is a hypothesis twice, once for all spaces in the universe with bases indexed by $\mathrm{Fin}\ n$ and once for the given $h$ and $v$, whose basis has an arbitrary finite index type; the body of `AdelicCovolumeFinite.of_remaining` repeats the same fifteen line term as the three other theorems of that file, and the same pattern of two forms appears in `AdelicCovolumeFinite.of_open`. The names of the hypotheses in the last two theorems are our reading of the statement names; we have not unfolded those statements, the reduction theory in `ArithmeticCovolumeFinite.of_open` or the double coset lemma.
