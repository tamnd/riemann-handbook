---
title: Row lattices and the orbit count
decls:
  - GlobalTheory.T.rowLattice_of_locally_standard_frame
  - GlobalTheory.RowLatAdapt.row_lattice_of_local_standard
  - GlobalTheory.T.exists_rowTerm_of_local_completions_terms
  - GlobalTheory.RowTermReal.exists_term_of_locOver
  - GlobalTheory.T.orbitCount_rows_doubleCosets_innerDatum_class
  - GlobalTheory.OrbitCount.orbit_count
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row lattices and the orbit count

This section connects the lattices of the last section with the terms of the double coset sum. The first result shows that a lattice which is locally a translate of a standard lattice is, after an adapted isometry, a row lattice. The second result builds a term of the double coset sum over every lattice that lies over a family of local data. The third result, the orbit count, is the core of the mass identity: the keys of the terms over one rational class of lattices are finite in number, all have the same weight, and their number times the squared weight is the inverse order of the stabilizer. The three results are used in the [mass identity](/entry/weights-add-up-to-mass-of/) of the next section.

We keep the [standing assumptions](/entry/gdat-eq-iff/) of the last section, with the frames $F$ and $F'$ attached to two words $u$ and $u'$: their parameters are the primes $T_u$ and $T_{u'}$ of the words. Let $F_u$ be the standard flag of $u$, and recall the [row weight](/entry/per-row-c/) $w(\Lambda') = 1/\#A(\Lambda')$ of a row lattice.

**Definition 2.14.1 (Row lattice).** Let $F_0$ be a flag with parameter $T$, with isotropic span $X$ and dual vectors $e_0, \dots, e_{r-1}$. Let $X_S$ be the standard lattice of $X$: the $\mathcal{O}_E$-module of the $x e_a$ with $x \in \mathfrak{d}^{-(r-a)}$, for the fixed ideal $\mathfrak{d}$ of the setting. An $\mathcal{O}_E$-lattice $\Lambda$ in $V$ is a *row lattice* for $F_0$ if:

1. $\Lambda$ lies in the genus of the base lattice $L_0$;
2. $\Lambda$ is unimodular, it lifts the flag $F_0$, and it satisfies the fixed convolution condition at level $g$;
3. $\Lambda \cap X = X_S$.

**Definition 2.14.2 (Terms over a lattice and keys).** A term $t$ of the double coset sum for $(u, u')$ has a lattice $\lambda_t$, a frame $F_t$, a row $\operatorname{row}(t)$ and a rational double coset $\nu(t)$. Its *key* is $\kappa(t) = (\operatorname{row}(t), \nu(t))$ and its *weight* is
$$\mathrm{wt}(t) = \sqrt{w(\lambda_t)\, w(\lambda'_t)},$$
the geometric mean of the row weights of its two lattices. The term $t$ *lies over* a lattice $\Lambda$ if there is an isometry $\gamma$, adapted from $F_u$ to $F$ and from $F_t$ to $F'$, with $\Lambda = \gamma \lambda_t$.

**Theorem 2.14.3 (Row lattices from locally standard lattices).** Let $T \ne 0$ be an integer. Let $F_0$ be a flag and $G$ a frame, both with parameter $T$. At each finite place $p$ let $A_p$ be a local frame whose vectors are the images of the frame vectors of $G$, scaled by the fixed factors. Let $\Lambda$ be a lattice in $V$ such that, at every $p$,
$$\Lambda_p = n_p \operatorname{std}(A_p, L_p)$$
for some $n_p \in N(A_p)$ and some inner lattice $L_p$ of $A_p$. Then there is an isometry $\gamma$, adapted from $F_0$ to $G$, such that $\gamma^{-1} \Lambda$ is a row lattice for $F_0$.

Lean: `GlobalTheory.RowLatAdapt.row_lattice_of_local_standard` (also `GlobalTheory.T.rowLattice_of_locally_standard_frame`, a second name).

*Proof.* The proof has four steps. First, unimodularity is a local property, and each standard lattice $\operatorname{std}(A_p, L_p)$ is self-dual, so its unipotent translate $\Lambda_p$ is self-dual; hence $\Lambda$ is unimodular. Second, the isotropic part $\Lambda \cap X_G$ is computed place by place. At $p$ it is $n_p$ applied to the span of the scaled frame vectors, and $n_p$ is unitriangular on the flag. This gives a unitriangular change $e'_a$ of the frame vectors of $G$ with $\Lambda \cap X_G$ equal to the span of the scaled $e'_a$. Third, the anisotropic frame vector $z$ of $G$ can be shifted by an isotropic vector $x \in X_G$ so that $z + x \in \Lambda$, and a multiple $c z$ that lies in the inner preimage has $c \in \mathcal{O}_E$; that is, the shifted vector is primitive in the inner lattice. The vectors $e'_a$ and $z + x$ form a new flag $G'$ with the same span and the same parameter. Fourth, Witt's theorem for flags gives an isometry $\gamma$ that maps $F_0$ to $G'$, because two flags with the same parameter $T \ne 0$ have the same Gram matrix. The row lattice conditions are transported by $\gamma^{-1}$: unimodularity, the genus, the lift of the flag, and $\Lambda \cap X = X_S$ follow from the first three steps, and the fixed convolution condition holds for any lattice that is integral along the flag. Finally $\gamma f_a(F_0) - f_a(G)$ is $e'_a - e_a$ or $x$, which lies in the $a$-th step of the flag of $G$. So $\gamma$ is adapted from $F_0$ to $G$. $\square$

**Theorem 2.14.4 (A term over each glued lattice).** Under the standing assumptions, let $\Lambda$ lie over a family $y$ of local data. Then some term $t$ of the double coset sum for $(u, u')$ lies over $\Lambda$.

Lean: `GlobalTheory.RowTermReal.exists_term_of_locOver` (also `GlobalTheory.T.exists_rowTerm_of_local_completions_terms`, a second name).

*Proof.* At each place, a local term with lattice $\Lambda_p$ is a unipotent translate of a standard lattice for $A_p$ and for $B_p$. The [Theorem 2.14.3](/entry/row-lattice-of-local-standard/) above, applied at $F$ and at $F'$, gives isometries adapted from the two base flags such that the two pulled back lattices are row lattices. Choose representatives of the row lattices up to frame adapted isometries; this replaces the pulled back lattices by fixed representatives, at the cost of a further adapted isometry. The two isometries together define a frame for the second word, and the pair (row lattice, frame) is a candidate term. The glued local terms show that this frame is admissible and integral at every place. The point of the pair is rational, because the Gram matrix of $(F, F')$ is the matrix of $w$. So the candidate is a term $t$ of the double coset sum, and the composite isometry is adapted from $F_u$ to $F$ and from $F_t$ to $F'$ and moves $\lambda_t$ to $\Lambda$. $\square$

**Theorem 2.14.5 (Orbit count).** Under the [standing assumptions](/entry/gdat-eq-iff/) without the local frames, let $t_0$ be a term that lies over a lattice $\Lambda_0$. Let
$$K = \{\kappa(t) : t \text{ lies over some } \Lambda_1 \text{ with } \Lambda_0 \sim \Lambda_1\}$$
be the set of keys of terms over the rational class of $\Lambda_0$. Then:

1. $K$ is finite;
2. every key in $K$ is the key of a term that lies over $\Lambda_0$ itself;
3. $\mathrm{wt}(t) = \mathrm{wt}(t_0)$ for every term $t$ that lies over a lattice $\Lambda_1 \sim \Lambda_0$;
4. in $[0, \infty]$,
$$\#K \cdot \mathrm{wt}(t_0)^2 = \frac{1}{\#\operatorname{Stab}(\Lambda_0)}.$$

Lean: `GlobalTheory.OrbitCount.orbit_count` (also `GlobalTheory.T.orbitCount_rows_doubleCosets_innerDatum_class`, a second name).

*Proof.* Let $\gamma_0$ be the isometry that puts $t_0$ over $\Lambda_0$. If $t$ lies over $\Lambda_1 = \eta \Lambda_0$ for some $\eta$ in the stabilizer of the frames, then composing with $\eta^{-1}$ puts $t$ over $\Lambda_0$ with the same key. This gives (2). A term over $\Lambda_0$ has row lattices that are moved to those of $t_0$ by adapted isometries, and the row weight depends only on the orbit, so (3) holds. For (1) and (4), let $A$ and $A'$ be the groups of adapted automorphisms of the two row lattices of $t_0$, and let $U \le A$ and $U' \le A'$ be their normal unipotent subgroups. The index $[A : U]$ is the order of the group $A(\lambda_{t_0})$ of induced maps on the quotient, so $[A : U] = 1/w(\lambda_{t_0})$, and the same for $A'$. Put $P = A \times A'$ and let $B \le P$ be the subgroup of pairs that keep the rational double coset of $t_0$; then $U \times U' \le B \le P$. The group $P$ acts transitively on the terms over $\Lambda_0$ with the row of $t_0$, so the keys form the image of $P$, and
$$\#K = [P : B].$$
The stabilizer of $\Lambda_0$ in $H_0(F, F')$ corresponds to the pairs that keep the double coset and the inner datum, modulo the unipotent pairs, so $\#\operatorname{Stab}(\Lambda_0) = [B : U \times U']$. Multiplying,
$$\#K \cdot \#\operatorname{Stab}(\Lambda_0) = [P : U \times U'] = \frac{1}{w(\lambda_{t_0})\, w(\lambda'_{t_0})} = \frac{1}{\mathrm{wt}(t_0)^2}.$$
All indices are finite, so $K$ is finite, and dividing gives (4). $\square$

**Remark 2.14.6 (Formalization).** In the orbit count, the key set $K$ is a hypothesis of the form `K = {κ | ...}` and the weight is `wt`, defined as a square root of a product of `wRow` values ([TermOp.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean#L341)). The term in the second theorem is built by hand as `Quot.mk _ p` from a carrier element ([ExistsRowTermOfLocalCompletionsTerms.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsRowTermOfLocalCompletionsTerms.lean#L111)). The orbit count does not involve the local frame pairs. The conditions "lifts the flag" and "fixed convolution" are `IsLift` and `IsFixedConv`, which are not unfolded here.
