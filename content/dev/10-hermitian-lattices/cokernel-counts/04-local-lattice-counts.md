---
title: Local lattice counts by cokernels
decls:
  - Formalism.L2.SG.LocalCountModules.AlgGSplit.stepSplit_holds
  - Formalism.L2.SG.LocalCountModules.UnitaryGroupMassFormula.LocCntUG.locCntUG_holds
  - Formalism.L2.SG.LocalCountModules.localCountUnitGlobal_holds
  - Formalism.L2.SG.LsDatumA.modSideUG
  - Formalism.L2.SG.LsDatumA.localCount_of_module
  - Formalism.L2.SG.LsDatumA.globalCount_of_module
  - Formalism.L2.SG.LsDatumA.globalCount_of_split_mode
  - Formalism.L2.SG.LsDatumA.integralClosureRank_and_residueTrdegLe
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local lattice counts by cokernels

This section gives the local count that names the chapter. Over a local field, fix two flags in a Hermitian space and the cross Gram matrices of the two flags. The lattices that are compatible with both flags are then counted by the isomorphisms between two finite modules: the cokernels of the two Gram matrices, with a marked element and a linear form. The count depends only on the classes of the Gram matrices under $\mathrm{GL}_{r+1}$ of the local integers. The main result is the Theorem (Family local model), which proves this count for every admissible local model. It is used in the [Theorem 8.5.3](/entry/partner-count-holds-all/) that counts the partners of a term.

Let $F$ be a nonarchimedean local field with ring of integers $\mathcal{O}_F$, and let $E$ be a quadratic étale $F$-algebra with involution $x \mapsto \bar{x}$: either a field, or $E \cong F \times F$ with the involution that swaps the factors. Let $R \subseteq E$ be the lattice ring of a local model, with the additive character of the [previous section](/entry/local-model-at-holds/). In the split case the model comes with a splitting $E \cong F \times F$ and a parameter $q \in \mathcal{O}_F$.

**Definition 8.4.1 (Cokernel of a matrix).** For $m \geq 1$ let $\mathrm{Mat}_m(R)$ be the set of $m \times m$ matrices $Z$ with entries in $R$ and $\det Z \in E^\times$. The *cokernel* of $Z$ is the finite $R$-module $\mathrm{cok}(Z) = R^m / Z R^m$. For $Z \in \mathrm{Mat}_{m+1}(R)$, the *marked element* $e(Z) \in \mathrm{cok}(Z)$ is the class of the last basis vector, and the *linear form* $\lambda_Z \colon \mathrm{cok}(Z) \to E/R$ is
$$\lambda_Z(v) = \bigl(Z^{-1} v\bigr)_{m+1} \bmod R.$$
It is well defined, since $(Z^{-1} Z w)_{m+1} = w_{m+1} \in R$.

**Definition 8.4.2 (Isomorphism count).** For $Z, Z' \in \mathrm{Mat}_{m+1}(R)$ let $\mathrm{Iso}(Z, Z')$ be the set of $R$-linear isomorphisms $\varphi \colon \mathrm{cok}(Z) \to \mathrm{cok}(Z')$ with $\varphi(e(Z)) = e(Z')$ and $\lambda_{Z'} \circ \varphi = \lambda_Z$. Put $n(Z, Z') = |\mathrm{Iso}(Z, Z')|$. The relation $\mathrm{Iso}(Z, Z') \neq \emptyset$ is an equivalence relation, and its classes are the *cokernel classes* of rank $m+1$. For a class $c$, $n(c) = n(Z, Z)$ for any $Z$ in $c$ is the number of automorphisms of the marked cokernel. More generally, for $Z, Z' \in \mathrm{Mat}_m(R)$ and vectors $\beta, \beta', \alpha, \alpha' \in R^m$, let $n^{\beta,\alpha}(Z, Z'; \beta', \alpha')$ be the number of $R$-linear isomorphisms $\varphi \colon \mathrm{cok}(Z) \to \mathrm{cok}(Z')$ that send the class of $\beta$ to the class of $\beta'$ and satisfy $\mu' \circ \varphi = \mu$, where $\mu(v) = \alpha^{T} Z^{-1} v \bmod R$ and $\mu'$ is defined in the same way from $Z'$ and $\alpha'$.

Two matrices $Z$ and $gZh$ with $g, h \in \mathrm{GL}_{m+1}(R)$ have isomorphic cokernels, and when $g$ has last column $e_{m+1}$ and $h$ has last row $e_{m+1}^T$, the isomorphism induced by $g$ respects the marked element and the form. So the count depends on $Z$ through a double coset. For example, if $Z$ is invertible over $R$, then $\mathrm{cok}(Z) = 0$ and $n(Z, Z') = 1$ if $Z'$ is invertible too.

**Definition 8.4.3 (Terms and their Gram matrices).** Let $(V, h)$ be a Hermitian space of dimension $n$ over $E$. A *term* of rank $r$ is a tuple $t = (\Lambda, f, f', T, T')$ with $\Lambda$ an $R$-lattice in $V$, $f, f' \colon \{1, \dots, r+1\} \to V$ two flags, and $T, T' \in F$. The *cross Gram matrix* is $\hat{Z}(f, f')_{ab} = h(f'_b, f_a)$, and $D_l(f, f')$ is its leading $l \times l$ minor. The *modified Gram matrix* $Z^+(t)$ is $\hat{Z}(f, f')$ if $E$ is a field. In the split case it is obtained from $\hat{Z}$ by dividing the two components by $q$ and correcting by $T$ and $T'$. A flag $f_2$ is a *frame for $T$* if $h(f_{2,a}, f_{2,b}) = 0$ unless $a = b = r + 1$, and $h(f_{2,r+1}, f_{2,r+1}) = -T$.

**Definition 8.4.4 (Family local model).** The local model $M$ is a *family local model* in rank $r$ and dimension $n$ if the following holds. Let $(V, h)$ have dimension $n$, let $t_1 = (\Lambda_1, f, f', T, T')$ be a generic term, let $f_2, f'_2$ be frames for $T$ and $T'$, and let $\varphi, \varphi'$ be isomorphisms from the spaces attached to $f, f'$ to those attached to $f_2, f'_2$ that match $t_1$ with $(0, f_2, f'_2, T, T')$ and send the last vectors to the last vectors. Let $\mathcal{S}$ be the set of lattices $\Lambda_2$ such that $t_2 = (\Lambda_2, f_2, f'_2, T, T')$ is generic and respects $\varphi, \varphi'$. Let $P_1 = Z^+(t_1)$ and $P_2$ the modified Gram matrix of $\hat{Z}(f_2, f'_2)$. Then:

1. if $D_r(f, f') = 0$, then $|\mathcal{S}| = n(Z_1, Z_2)$ for all $Z_1, Z_2 \in \mathrm{Mat}_{r+1}(R)$ with $Z_1 = P_1$ and $Z_2 = P_2$;
2. if $D_r(f, f')$ is a unit, then $|\mathcal{S}| = n^{\beta,\alpha}(Y_1, Y_2; \beta_2, \alpha_2)$, where $Y_i$ is the upper left $r \times r$ block of $P_i$, $\beta_i$ its last column without the last entry and $\alpha_i$ its last row without the last entry.

We call part 1 the *zero side* and part 2 the *unit side*. A global datum satisfies the *local count* if every admissible local model is a family local model in rank $r$ and dimension $n$ fixed by the datum.

In the unit case the count drops by one rank: the last row and column are recorded by the vector $\beta$ and the form $\alpha$. The proof of the two sides is different over a split place, where $E = F \times F$ and the Hermitian space is a pair of dual vector spaces.

**Theorem 8.4.5 (Splitting the count).** Let $M$ be split, with parameter $q$. Let $T, T' \in \mathcal{O}_F^\times$ with $T \equiv T' \pmod{q^2}$. For $i = 1, 2$ let $\hat{Z}_i$ be a matrix over $E$ with unit determinant, such that $\det \hat{Z}_i \overline{\det \hat{Z}_i} - T T' \, D_r(\hat Z_i) \overline{D_r(\hat Z_i)}$ is a unit, and let $Z_i, Z^\sigma_i$ be the modified Gram matrices of $\hat Z_i$ and of $\overline{\hat Z_i}$. Assume $\det \hat Z_1 \, D_r(\hat Z_2) = \det \hat Z_2 \, D_r(\hat Z_1)$. Then the number of local theta isomorphisms from $\hat Z_1$ to $\hat Z_2$ equals the number of pairs $(\theta_1, \theta_2)$ of $\mathcal{O}$-linear isomorphisms $\theta_1$ between the components of $Z_1$ and $Z_2$ and $\theta_2$ between those of $Z^\sigma_1$ and $Z^\sigma_2$, that match the first columns and satisfy the gluing condition between the two components.

Lean: `Formalism.L2.SG.LocalCountModules.AlgGSplit.stepSplit_holds`.

*Proof.* Over $E = F \times F$, every module splits into its two components, and a theta isomorphism is the same as an isomorphism on each component. The first component carries the matrix $Z_i$, and the second carries the matrix built from the conjugate $\overline{\hat Z_i}$, which is $Z^\sigma_i$. The condition $T \equiv T' \pmod{q^2}$ and the determinant identity make the matching of the last columns compatible on the two sides. The proof combines two steps: one identifies the gamma parts (by a sub and a sup inclusion), and one identifies the forms. $\square$

The Theorem (Splitting the count) is used on both sides of the split case: on the zero side, and on the unit side through the first isometry statements.

**Theorem 8.4.6 (Unit side at split places).** Every admissible split local model satisfies the unit side of the family local model condition, in every rank and dimension.

Lean: `Formalism.L2.SG.LocalCountModules.UnitaryGroupMassFormula.LocCntUG.locCntUG_holds` (also `Formalism.L2.SG.LocalCountModules.localCountUnitGlobal_holds` and `Formalism.L2.SG.LsDatumA.modSideUG`, the same statement under two more names).

*Proof.* The unit side at split places follows from a single algebraic statement: in the split case, with $T, T'$ units, $T \equiv T' \pmod{q^2}$, unit determinants of $\hat Z_i$ and of their leading $r \times r$ minors, the identity $\det \hat Z_1 \, D_r(\hat Z_2) = \det \hat Z_2 \, D_r(\hat Z_1)$ and the unit condition above, the number of local theta isomorphisms is the count $n^{\beta, \alpha}$. That statement follows from the [Theorem (Splitting the count)](/entry/step-split-holds/) together with the first isometry statements (forward, backward and uniqueness). $\square$

**Theorem 8.4.7 (Family local model).** Let $M$ be an admissible local model and $r, n \geq 0$. Assume the zero side and the unit side for $M$ in the split case. Then $M$ is a family local model in rank $r$ and dimension $n$.

Lean: `Formalism.L2.SG.LsDatumA.localCount_of_module`.

*Proof.* In the case $E$ a field, both sides are proved directly. In general, the lattices $\Lambda_2$ in $\mathcal{S}$ are glued from their parts along the flags. Three results describe the gluing: the gluing of the $\eta$ parts, the convexity of the gluing and the generation of a lattice by primitive vectors. With them, the set $\mathcal{S}$ is in bijection with a set of module isomorphisms, by a statement that holds in the field case and in the split case separately. In the split case the hypotheses give the two sides. $\square$

**Corollary 8.4.8 (Local count from both sides).** Assume the zero side and the unit side for every admissible split local model. Then the global datum satisfies the local count.

Lean: `Formalism.L2.SG.LsDatumA.globalCount_of_module`.

*Proof.* This is the [Theorem (Family local model)](/entry/local-count-of-module/) applied to each admissible local model. $\square$

**Corollary 8.4.9 (Local count from the split mode).** Assume the zero side and the unit side for every admissible local model in the split mode. Then the global datum satisfies the local count.

Lean: `Formalism.L2.SG.LsDatumA.globalCount_of_split_mode`.

*Proof.* For a model that is not split, the two sides hold by the field case. For a split model they hold by hypothesis. Then apply the [Corollary (Local count from both sides)](/entry/global-count-of-module/). $\square$

**Corollary 8.4.10 (Local count).** Every global datum satisfies the local count.

Lean: `Formalism.L2.SG.LsDatumA.integralClosureRank_and_residueTrdegLe`.

*Proof.* This is the [Corollary (Local count from the split mode)](/entry/global-count-of-split-mode/) applied to the zero side at split places, which follows from the Theorem (Splitting the count), and to the [Theorem (Unit side at split places)](/entry/loc-cnt-ug-holds/). $\square$

**Remark 8.4.11 (Formalization).** The last corollary carries a name about integral closures and residue transcendence degrees ([IntegralClosureRankAndResidueTrdegLe.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/IntegralClosureRankAndResidueTrdegLe.lean#L11)). The name is taken from an unrelated statement in ReciprocityTheory/SemistableReduction and says nothing about the local count. The statement it proves, `T2 D`, is one of three different definitions named `T2` (ThinScalesBound.lean:199, ChainLength.lean:195, LocalBesselAndTopKernel.lean:162). The unit side at split places has three names (`locCntUG_holds`, `localCountUnitGlobal_holds`, `modSideUG`), each a one-line restatement of the previous one. In the names, the suffix `G` means the split case and `L` the field case. The proofs in the field case and the gluing results (`glueEta_holds`, `glueConv_holds`, `genOfPrim_holds`) were not opened in detail; the proof of the Theorem (Family local model) gives their role, not their content. We did not unfold the theta isomorphism count `ThetaGC`, the components `DD1`, or the matching conditions `Match1` and `IsoB` in the Theorem (Splitting the count).
