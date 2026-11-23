---
title: The formula on constant spaces
decls:
  - GlobalTheory.T.exists_injective_cochainModel_trivialProjectiveBundle
  - GlobalTheory.EtC.pbf_disc_model
  - GlobalTheory.EtC.pbf_disc
  - GlobalTheory.T.projectiveBundleFormula_discrete_space
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The formula on constant spaces

This section extends the projective bundle formula from a scheme $U$, that is from the constant space $\mathrm{sch}(U)$, to an arbitrary constant space $\mathrm{disc}(F)$ on which $q$ is invertible. A presheaf $F$ is glued from representable presheaves, so the extension is a local to global argument. The proof writes both sides of the formula map as cohomology of $\mathrm{disc}(F)$ with values in fixed complexes of injective sheaves, and then shows that a map of such complexes that is a bijection on every scheme is a bijection on every constant space. The spaces, the groups $H^n(E, \mathbb{Z}/q(i))$ and the formula map $\Phi_V$ are defined in the first section of this chapter.

For complexes $K$ and $L$ of sheaves of $\mathbb{Z}/q$-modules, write $H^n(K, L)$ for the group of homotopy classes of maps $K \to L$ of degree $n$. So $H^n(E, F) = H^n(C_\bullet(E), I^\bullet(F))$. A cocycle $\psi$ of degree $d$ from $L$ to $C$ gives a map $\psi_* : H^{n-d}(K, L) \to H^n(K, C)$ by composition.

**Lemma 2.2.1 (Comparison on constant spaces).** Let $q \geq 1$. Let $L_1, \dots, L_r$ and $C$ be complexes of injective étale sheaves of $\mathbb{Z}/q$-modules, all zero below a fixed degree. Let $\psi_j$ be a cocycle of degree $d_j$ from $L_j$ to $C$. Suppose that for every scheme $U$ on which $q$ is a unit and every $n$ the map
$$
\Psi_K : \bigoplus_{j} H^{n-d_j}(K, L_j) \to H^n(K, C), \qquad (a_j) \mapsto \sum_j \psi_{j*} a_j,
$$
is bijective for $K = C_\bullet(\mathrm{sch}(U))$. Then $\Psi_K$ is bijective for $K = C_\bullet(\mathrm{disc}(F))$, for every presheaf $F$ such that $q$ is invertible on $\mathrm{disc}(F)$.

Lean: `GlobalTheory.T.injectiveComplexMap_quasiIso_of_unit_schemes` (also `GlobalTheory.EtC.DiscSupp.bijective_disc`).

*Proof.* First replace each cocycle $\psi_j$ by a map of complexes. After a shift by $d_j$ and a change of $L_j$ within its homotopy class, the sum of the $\psi_j$ becomes one map of complexes $f : D \to C$, with $D$ again bounded below and made of injective sheaves, and with $\Psi_K = f_* \circ e_K$ for a bijection $e_K$ that is natural in $K$. So $\Psi_K$ is bijective in all degrees if and only if $f_*$ is, and by the long exact sequence of the mapping cone this holds if and only if $H^n(K, \mathrm{cone}(f)) = 0$ for all $n$. The hypothesis on schemes says that the complex $\mathrm{cone}(f)(U)$ of sections is exact for every scheme $U$ on which $q$ is a unit, in the étale local sense that every cocycle of sections becomes a coboundary after an étale cover. Each section of $F$ lives over such a scheme, because $q$ is invertible on $\mathrm{disc}(F)$. A complex of injective sheaves, bounded below, whose sections are exact in this local sense on every scheme over which $\mathrm{disc}(F)$ has a point has no cohomology on $C_\bullet(\mathrm{disc}(F))$, so $H^n(C_\bullet(\mathrm{disc}(F)), \mathrm{cone}(f)) = 0$. We take these three steps (the cone criterion, the local exactness on schemes, and the vanishing on a constant space) as given. $\square$

The second input is a model of the projective bundle as a complex. Let $\mathrm{Inv}_q$ be the presheaf with one point over $U$ when $q$ is a unit on $U$ and no point otherwise. Let $Q_N$ be the projective bundle of the trivial bundle of rank $N$ on $\mathrm{disc}(\mathrm{Inv}_q)$, and let $L_Q$ be its tautological line bundle. Then $q$ is invertible on $Q_N$. If $q$ is invertible on $\mathrm{disc}(F)$, then $F$ maps to $\mathrm{Inv}_q$, and the projective bundle of $\mathrm{triv}_N$ on $\mathrm{disc}(F)$ is isomorphic to the product $\mathrm{disc}(F) \times Q_N$, with the tautological line bundle on the second factor.

**Lemma 2.2.2 (Cochain model of the trivial projective bundle).** Let $q \geq 1$, $N \geq 0$ and $i \in \mathbb{Z}$. There are a complex $J$ of injective sheaves, zero in negative degrees, and cocycles $\psi_j$ of degree $2j$ from $I^\bullet(\mathbb{Z}/q(i-j))$ to $J$ for $0 \leq j < N$, with the following property. For every presheaf $F$ such that $q$ is invertible on $\mathrm{disc}(F)$ and every $n$ there is an isomorphism
$$
e : H^n(C_\bullet(\mathrm{disc}(F)), J) \xrightarrow{\ \sim\ } H^n(\mathbb{P}(\mathrm{triv}_N), \mathbb{Z}/q(i))
$$
such that $e \circ \Psi = \Phi_{\mathrm{triv}_N}$, where $\Psi(a) = \sum_j \psi_{j*} a_j$ and $\Phi$ is the formula map.

Lean: `GlobalTheory.T.exists_injective_cochainModel_trivialProjectiveBundle` (also `GlobalTheory.EtC.pbf_disc_model`).

*Proof.* For each $j < N$ choose a cocycle $z_j$ on $Q_N$ that represents $c_1(L_Q)^j \in H^{2j}(Q_N, \mathbb{Z}/q(j))$. The complex $J$ is a complex built from $Q_N$ and the resolution $I^\bullet(\mathbb{Z}/q(i))$, and the pairing of a class with $z_j$ is a cocycle $\psi_j$ into $J$. For a constant space $\mathrm{disc}(F)$, we take as given an isomorphism $e_0$ from $H^n(C_\bullet(\mathrm{disc}(F)), J)$ to $H^n(\mathrm{disc}(F) \times Q_N, \mathbb{Z}/q(i))$, which sends a cocycle that vanishes in positive simplicial degree to the class of its pairing with the fibre. Compose $e_0$ with the isomorphism $\mathbb{P}(\mathrm{triv}_N) \cong \mathrm{disc}(F) \times Q_N$. Under this isomorphism $\pi$ becomes the first projection and $L_V$ becomes the pullback of $L_Q$, so by naturality of cup products and of $c_1$ the formula map becomes $(a_j) \mapsto \sum_j \mathrm{pr}_1^* a_j \cup \mathrm{pr}_2^* c_1(L_Q)^j$. Each class $a_j$ on the constant space has a representative that is zero in positive simplicial degree. For such a representative, the cup product with $\mathrm{pr}_2^* z_j$ is the pairing that defines $\psi_j$. So $e \circ \Psi$ and $\Phi$ agree on all classes. $\square$

**Theorem 2.2.3 (Projective bundle formula on constant spaces).** Let $q \geq 1$, let $F$ be a presheaf such that $q$ is invertible on $\mathrm{disc}(F)$, and let $V$ be a vector bundle of rank $N$ on $\mathrm{disc}(F)$. Then the projective bundle formula holds for $V$.

Lean: `GlobalTheory.T.projectiveBundleFormula_discrete_space` (also `GlobalTheory.EtC.pbf_disc`).

*Proof.* Fix the weight $i$. Take $J$ and the $\psi_j$ from the cochain model, and apply the comparison lemma to $L_j = I^\bullet(\mathbb{Z}/q(i-j))$, $C = J$ and $d_j = 2j$. Its hypothesis on schemes holds: for a scheme $U$ on which $q$ is a unit, $q$ is invertible on $\mathrm{sch}(U)$, and the cochain model for $F = \mathrm{Hom}(-, U)$ gives $e \circ \Psi = \Phi_{\mathrm{triv}_N}$. Here $\Phi_{\mathrm{triv}_N}$ is bijective by the [projective bundle formula on a scheme](/entry/t-etale-cohomology-projective-bundle-formula/), and $e$ is bijective, so $\Psi$ is bijective. The comparison lemma now gives that $\Psi$ is bijective on $\mathrm{disc}(F)$. By the lemma of the first section on bundles over constant spaces, $V = \mathrm{triv}_N$, and the cochain model gives $\Phi_V = e \circ \Psi$. So $\Phi_V$ is bijective. $\square$

**Remark 2.2.4.** The formula for the trivial bundle of rank $N$ on every space on which $q$ is invertible is already proved in the chapter on étale clopen descent, in [the lemma on trivial bundles](/entry/pbf-all/). With the lemma that bundles on constant spaces are trivial, that would give the theorem at once. Only its case $E = \mathrm{sch}(U)$ is available here, so the proof takes the longer route through the comparison lemma.

**Remark 2.2.5 (Formalization).** The lemma on trivial bundles of the chapter on étale clopen descent is private to its module, and only its case $E = \mathrm{sch}(U)$ is exported. The cochain model is restated in [ExistsInjectiveCochainModelTrivialProjectiveBundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsInjectiveCochainModelTrivialProjectiveBundStatement.lean#L8), which tries the target name in three ways, raises the heartbeat limit to $10^6$ and imports Mathlib twice. We opened the statements of the three lemmas in the proof of the comparison lemma but not their proofs. We did not open the complex $J$, the space $Q_N$ beyond its definition as a fibre product, or the line bundle $L_Q$; the cochain model uses only the properties stated.
