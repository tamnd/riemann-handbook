---
title: De Rham representations are potentially semistable
decls:
  - GlobalTheory.deRham_potentiallySemistable
status: drafted
drafted_by: writer@claude-opus-5-5
---
## De Rham representations are potentially semistable

This section proves the $p$-adic monodromy theorem: a de Rham representation of $G_K$, for $K$ a finite extension of $\mathbb{Q}_\ell$, becomes semistable on an open subgroup $G_{K'}$. Fontaine stated it as a conjecture, and Berger proved it. The theorem is used by the trunk step [EveryCharacter](/step/every-character/). The proof here reduces the theorem to a statement about matrices, the matrix form of the monodromy theorem. That matrix form is proved in [its own entry](/entry/p-adic-monodromy-theorem-matrix-form/), and the main work is in [the proof of the matrix form](/entry/mat-thm-holds/). The reduction is the content of this section.

We keep the notation of the previous sections. Fix a prime $\ell$ and local period data at $\ell$ that is tied to its $A_{\inf}$ data, so that the abstract rings $B$ and $B_{\mathrm{dR}}$ are identified with Fontaine's rings, with all their structure (see [[Fontaine's period rings|K6HW8YWCQJ]]). The data give the action of $G_{\mathbb{Q}_\ell}$ on $B$ and on $B_{\mathrm{dR}}$, the element $t_B$ of $B$ and the cyclotomic character $\chi$. Let $\mathbb{Q}_\ell^{\mathrm{ur}}$ be the maximal unramified extension of $\mathbb{Q}_\ell$ in $\Omega$, not completed, and $\sigma$ its arithmetic Frobenius. For a finite extension $K$ of $\mathbb{Q}_\ell$, let $K_0 = K \cap \mathbb{Q}_\ell^{\mathrm{ur}}$.

**Definition 6.15.1 (Semistable period ring).** Fix $\ell$-power roots $\ell^{1/\ell^m}$ in $\Omega$ with $\ell^{1/\ell^0} = \ell$ and $(\ell^{1/\ell^{m+1}})^\ell = \ell^{1/\ell^m}$. For $g \in G_{\mathbb{Q}_\ell}$, the *Kummer cocycle* $c(g) \in \mathbb{Z}_\ell$ is chosen so that $g(\ell^{1/\ell^m}) = \zeta_{\ell^m}^{c(g)}\,\ell^{1/\ell^m}$ for all $m$. Put $B_{\mathrm{st}} = B[X]$. The group $G_{\mathbb{Q}_\ell}$ acts on $B_{\mathrm{st}}$ by its action on the coefficients and by
$$g(X) = X + c(g)\,t_B.$$

Lean: `GlobalTheory.Pst.Bst` (also `GlobalTheory.Pst.actSt`, the action).

The relation $g(t_B) = \chi(g)\,t_B$ and the cocycle relation of $c$ make this an action.

**Definition 6.15.2 (De Rham, semistable, potentially semistable).** Let $V$ be a finite dimensional $\mathbb{Q}_\ell$-vector space with a representation $\rho$ of $G_K$.

1. $\rho$ is *de Rham* if $\dim_{\mathbb{Q}_\ell} D_{\mathrm{dR}}(V) = [K : \mathbb{Q}_\ell]\,\dim V$, where $D_{\mathrm{dR}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{dR}})^{G_K}$.
2. $\rho$ is *semistable* if $\dim_{\mathbb{Q}_\ell} D_{\mathrm{st}}(V) = [K_0 : \mathbb{Q}_\ell]\,\dim V$, where $D_{\mathrm{st}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{st}})^{G_K}$.
3. $D_{\mathrm{pst}}(V)$ is the union, over all finite extensions $K' \supseteq K$, of $D_{\mathrm{st}}$ of the restriction of $\rho$ to $G_{K'}$. It is a vector space over $\mathbb{Q}_\ell^{\mathrm{ur}}$ by multiplication in $B_{\mathrm{st}}$. The representation $\rho$ is *potentially semistable* if $\operatorname{rank}_{\mathbb{Q}_\ell^{\mathrm{ur}}} D_{\mathrm{pst}}(V) = \dim V$.

Lean: `Formalism.MainNotions.N.IsDR` (also `GlobalTheory.Pst.IsSst`, semistable; `GlobalTheory.Pst.Dpst`, the union; `GlobalTheory.Pst.IsPst`, potentially semistable).

The matrix form uses representations with coefficients in $\mathbb{Q}_\ell^{\mathrm{ur}}$. Let $n$ be a finite index set and $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ a homomorphism. For a matrix $M$ and a map $f$, write $f(M)$ for $M$ with $f$ applied to its entries, and $g(Q)$ for the Galois action on the entries of $Q$.

**Definition 6.15.3 (Matrix form of the monodromy theorem).** Let $r \geq 0$.

1. $\rho$ is *$r$-rational* if $r > 0$, every $c \in \mathbb{Q}_\ell^{\mathrm{ur}}$ with $\sigma^r(c) = c$ lies in $K$, $\sigma^r$ fixes every entry of every $\rho(g)$, and every entry of $\rho(g)$ is continuous in $g$ as a map to $\Omega$.
2. $\rho$ is *de Rham admissible* if for every $m \geq 0$ there is $Q \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $\sigma^m(\rho(g))\,g(Q) = Q$ for all $g \in G_K$.
3. $\rho$ is *semistable admissible* if there are a finite extension $K' \supseteq K$ and $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ with $\rho(g)\,g(Q) = Q$ for all $g \in G_{K'}$.

The *matrix form of the monodromy theorem* says: for every prime $\ell$, all tied local period data, every $n$, $K$ and $r$, and every $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, if $\rho$ is $r$-rational and de Rham admissible, then $\rho$ is semistable admissible.

Lean: `GlobalTheory.PMon.MatThm` (also `GlobalTheory.PMon.IsRat`, `GlobalTheory.PMon.AdmDR` and `GlobalTheory.PMon.AdmSt`, the three conditions).

The matrix $Q$ in 2 is a period matrix: its columns are a basis of $(V \otimes B_{\mathrm{dR}})^{G_K}$ written in coordinates. The index $m$ and the power $\sigma^m$ allow the $r$ embeddings of an unramified field of degree $r$; for coefficients in $\mathbb{Q}_\ell$ they play no role.

**Theorem 6.15.4 (p-adic monodromy theorem).** Let $\ell$ be a prime, and assume that the local period data at $\ell$ are tied to their $A_{\inf}$ data. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, and $V$ a finite dimensional $\mathbb{Q}_\ell$-vector space with its module topology. Let $\rho$ be a representation of $G_K$ on $V$ such that $g \mapsto \rho(g)v$ is continuous for every $v \in V$. If $\rho$ is de Rham, then $\rho$ is potentially semistable.

Lean: `GlobalTheory.deRham_potentiallySemistable`.

*Proof.* The matrix form of the monodromy theorem holds, by [its entry](/entry/p-adic-monodromy-theorem-matrix-form/). We show that it implies the Theorem.

Choose a basis $b_1, \dots, b_n$ of $V$ over $\mathbb{Q}_\ell$. Let $R(g) \in \mathrm{GL}_n(\mathbb{Q}_\ell)$ be the matrix of $\rho(g)$ in this basis, and let $\rho_b : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ be $R$ followed by the inclusion $\mathbb{Q}_\ell \subset \mathbb{Q}_\ell^{\mathrm{ur}}$. This is a homomorphism, since $\rho$ is.

Step 1: $\rho_b$ is $1$-rational. First, $1 > 0$. If $\sigma(c) = c$, then $c \in \mathbb{Q}_\ell$, since $\mathbb{Q}_\ell$ is the fixed field of $\sigma$ in $\mathbb{Q}_\ell^{\mathrm{ur}}$, and $\mathbb{Q}_\ell \subseteq K$. The entries of $\rho_b(g)$ lie in $\mathbb{Q}_\ell$, so $\sigma$ fixes them. The $(i, j)$ entry of $\rho_b(g)$ is the $i$-th coordinate of $\rho(g)b_j$. The coordinate map is linear on $V$, hence continuous for the module topology, and $g \mapsto \rho(g)b_j$ is continuous by assumption. So each entry is continuous.

Step 2: $\rho_b$ is de Rham admissible. Since $\rho$ is de Rham, a result proved elsewhere in this development gives $Q \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $R(g)\,g(Q) = Q$ for all $g \in G_K$, where the entries of $R(g)$ are mapped into $B_{\mathrm{dR}}$. For every $m$, $\sigma^m$ fixes the entries of $\rho_b(g)$, so $\sigma^m(\rho_b(g)) = R(g)$ in $B_{\mathrm{dR}}$, and the same $Q$ works for every $m$.

Step 3: the matrix form with $r = 1$. It gives a finite extension $K' \supseteq K$ and $Q \in \mathrm{GL}_n(B_{\mathrm{st}})$ with $\rho_b(g)\,g(Q) = Q$ for all $g \in G_{K'}$. Here the entries of $\rho_b(g)$ lie in $\mathbb{Q}_\ell$ and map to constants of $B_{\mathrm{st}} = B[X]$. So $R(g)\,g(Q) = Q$ for $g \in G_{K'}$.

Step 4: the restriction of $\rho$ to $G_{K'}$ is semistable. This is a second result proved elsewhere: if the matrices of a representation in a basis satisfy $R(g)\,g(Q) = Q$ for an invertible $Q$ over $B_{\mathrm{st}}$, then the representation is semistable. Classically, the columns of $Q$ give $n$ invariant vectors of $V \otimes B_{\mathrm{st}}$ that are independent over the invariants of $B_{\mathrm{st}}$.

Step 5: $\rho$ is potentially semistable. A third result proved elsewhere says that if the restriction of $\rho$ to $G_{K'}$ is semistable for some finite $K' \supseteq K$, then $\rho$ is potentially semistable. Classically, $D_{\mathrm{st}}$ of the restriction lies in $D_{\mathrm{pst}}(V)$, and its $\mathbb{Q}_\ell^{\mathrm{ur}}$-span has rank $\dim V$. $\square$

The converse also holds classically, since $B_{\mathrm{st}}$ embeds into $B_{\mathrm{dR}}$ compatibly with the Galois action; the development does not use it here. Berger's proof of the matrix form goes through the $(\varphi, \Gamma)$-module of $V$ and a $p$-adic differential equation attached to it. The de Rham condition makes the equation have a full set of solutions after a finite extension, and the monodromy theorem for $p$-adic differential equations (Crew's conjecture, proved by André, Kedlaya and Mebkhout) then gives the semistable periods.

**Remark 6.15.5 (Formalization).** The statement is the proposition `GlobalTheory.Published.DeRhamPotSemistable` in [DeRhamPotSemistable.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/DeRhamPotSemistable.lean#L13). It lies in the folder `PublishedTheorems`, but it is proved here, not assumed: the proof in [DeRhamPotentiallySemistable.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamPotentiallySemistable.lean#L11) is `GlobalTheory.T.deRham_potSemistable_of_matrix_monodromy` applied to `GlobalTheory.T.pAdicMonodromyTheorem_matrixForm`. Both are `first | exact ...` wrappers under `maxHeartbeats 1000000`, of `GlobalTheory.PMon.FromMat.deRhamPotSemistable_of_matThm` and `GlobalTheory.PMon.matThm_holds`. The reduction is in [DeRhamPotSemistableOfMatrixMonodromy.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamPotSemistableOfMatrixMonodromy.lean#L40); it uses the matrix form only with $r = 1$, at [line 60](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamPotSemistableOfMatrixMonodromy.lean#L60), so the general $r$ is used only inside the proof of the matrix form. The basis is `Module.finBasis`, and $\rho_b$ is `FromMat.matRep`. Steps 2, 4 and 5 are `GlobalTheory.T.exists_invertible_deRhamPeriodMatrix_of_isDR`, `GlobalTheory.T.isSemistable_of_invertible_periodMatrix_semistableRing` and `GlobalTheory.T.isPotentiallySemistable_of_semistable_restrict`, wrappers of `GlobalTheory.DRMat.exists_period_matrix_of_isDR`, `GlobalTheory.PMon.isSst_of_periodMatrix` and `GlobalTheory.PMon.isPst_of_isSst_resTo`; we read their statements, not their proofs. The fact that $\sigma$ fixes only $\mathbb{Q}_\ell$ is `fixed_frob`. The tie enters as `Nonempty (LocTied l P AI)`, and the proof extracts a tie and passes it to every step. The rank in `IsPst` is taken over the uncompleted field `MaximalUnramifiedExtension l`, on the type `DpstUr`, whose module structure is `Module.compHom` along multiplication in $B_{\mathrm{st}}$. The Kummer cocycle is chosen by `Exists.choose`. The file of the statement also contains the namespace `GlobalTheory.PstCoeff`, on representations with coefficients in a field $LL$ over $\mathbb{Q}_\ell$; it is not used in this proof.
