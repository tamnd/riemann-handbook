---
title: The special unitary group of a plane
decls:
  - GlobalTheory.T.specialUnitary_fixing_plane_complement_mem_closure
  - GlobalTheory.PlaneSU.plane_closure
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The special unitary group of a plane

Let $E/F$ be a CM extension and $P$ a plane in a Hermitian space over $E$ on which the form is nondegenerate. The special unitary group of $P$ is the norm-one group of a quaternion algebra over $F$ that contains $E$. This section makes this identification explicit by a matrix embedding and uses it to carry the [theorem on quaternions split at $S$](/entry/strong-approximation-quaternion-norm-one-split/) over to the elements of a special unitary group that act on $P$ and fix its orthogonal complement. The next section builds strong approximation for the whole special unitary group from these elements.

### The special unitary group

We now use the notation of the earlier sections: $(F, E, \sigma)$ is a CM extension, $J \in M_M(E)$ is nondegenerate Hermitian with form $h(x, y) = \sigma(x)^{\mathsf T} J y$, $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$, and $U_J(\mathbb{A}_F)$ is the unitary group over $\mathbb{A}_F$ with its rational subgroup $U_J(F)$. From the last section we keep the reduced norm $\mathrm{nrm}$, the algebras $(a, b)_R$, the embedding $\gamma \mapsto \hat\gamma$ of $(a, b)_F$ into $(a, b)_{\mathbb{A}_F}$, place idempotents $\varepsilon$ for a set $S = S_1 \cup S_2$ of places, and the set $H_0(\varepsilon)$.

**Definition 1.12.1 (Special unitary groups).** Let $\mathrm{SU}_J(\mathbb{A}_F)$ be the subgroup of $g \in U_J(\mathbb{A}_F)$ with $\det g = 1$. Let $\mathrm{SU}_J(F) = \mathrm{SU}_J(\mathbb{A}_F) \cap U_J(F)$. For $\varepsilon \in \mathbb{A}_F$ let $\mathrm{SU}_J(\varepsilon)$ be the set of $g \in \mathrm{SU}_J(\mathbb{A}_F)$ with $\varepsilon (g - 1) = g - 1$, entry by entry.

Lean: `GlobalTheory.Published.SUAdelic` (also `GlobalTheory.Published.SURat`, `GlobalTheory.Published.SUSupp`).

For a place idempotent $\varepsilon$ of $S$ the set $\mathrm{SU}_J(\varepsilon)$ is $\mathrm{SU}_J(F_S)$, and the closure of $\mathrm{SU}_J(F) \, \mathrm{SU}_J(\varepsilon)$ is what strong approximation is about.

### Strong approximation for a plane

**Theorem 1.12.2 (Strong approximation for a plane).** Let $(F, E, \sigma)$ be a CM extension and $J \in M_M(E)$ nondegenerate Hermitian. Let $\varepsilon$ be a place idempotent for $(S_1, S_2)$ with $S_1 \cup S_2$ nonempty. Let $e_1, e_2 \in E^M$ with $h(e_1, e_2) = 0$, $h(e_1, e_1) \neq 0$ and $h(e_2, e_2) \neq 0$. Assume that there is $t \in \mathbb{A}_E$ with
$$\varepsilon \Bigl( t \, \sigma(t) + \frac{h(e_1, e_1)}{h(e_2, e_2)} \Bigr) = 0.$$
Let $g \in \mathrm{SU}_J(\mathbb{A}_F)$ fix the image in $\mathbb{A}_E^M$ of every $v \in E^M$ with $h(e_1, v) = h(e_2, v) = 0$. Then $g$ lies in the closure of $\{ \gamma h : \gamma \in \mathrm{SU}_J(F), \ h \in \mathrm{SU}_J(\varepsilon) \}$.

Lean: `GlobalTheory.T.specialUnitary_fixing_plane_complement_mem_closure` (also `GlobalTheory.PlaneSU.plane_closure`).

The element $g$ acts on the plane $P = E e_1 + E e_2$ and fixes its orthogonal complement. The condition on $t$ says that $-h(e_1, e_1)/h(e_2, e_2)$ is a norm from $E_v$ at each $v \in S$.

*Proof.* We use the following facts from another part of the development, whose statements we have opened.

1. $\sigma^2 = 1$, and an element of $E$ fixed by $\sigma$ lies in $F$.
2. Let $A \in M_{M \times 2}(E)$ have columns $e_1, e_2$, let $H = \mathrm{diag}(h(e_1, e_1), h(e_2, e_2))$ and $B = H^{-1} \sigma(A)^{\mathsf T} J$. Then $h(e_1, e_1)$ and $h(e_2, e_2)$ are fixed by $\sigma$, $B A = 1$, $\sigma(A)^{\mathsf T} J = H B$, $J A = \sigma(B)^{\mathsf T} H$, and $B v = 0$ if and only if $h(e_1, v) = h(e_2, v) = 0$.
3. There is a basis $1, \theta$ of $E$ over $F$ with $\sigma(\theta) = -\theta$ and $\theta^2 = \delta \in F$.
4. If a matrix $G$ over $\mathbb{A}_E$ fixes every rational $v$ with $B v = 0$, then $G (1 - A B) = 1 - A B$.
5. If also $\sigma(G)^{\mathsf T} J G = J$, then $G = 1 + A (X - 1) B$ with $X = B G A$, and $\sigma(X)^{\mathsf T} H X = H$.
6. Let $f_1, f_2 \in F^\times$ and $H = \mathrm{diag}(f_1, f_2)$. A matrix $X \in M_2(\mathbb{A}_E)$ with $\sigma(X)^{\mathsf T} H X = H$ and $\det X = 1$ is $X = Q(x)$ for some $x$ in $(\delta, -f_2/f_1)_{\mathbb{A}_F}$, where
$$Q(x) = \begin{pmatrix} x_0 + x_1 \theta & b (x_2 + x_3 \theta) \\ x_2 - x_3 \theta & x_0 - x_1 \theta \end{pmatrix}, \qquad b = -f_2/f_1.$$
7. If $\varepsilon \bigl(t \sigma(t) + f_1/f_2\bigr) = 0$ for some $t \in \mathbb{A}_E$, there are $p, q \in \mathbb{A}_F$ with $\varepsilon \bigl(-f_2/f_1 - (p^2 - \delta q^2)\bigr) = 0$.
8. The map $y \mapsto 1 + A (Q(y) - 1) B$ from $(\delta, -f_2/f_1)_{\mathbb{A}_F}$ to $M_M(\mathbb{A}_E)$ is continuous.

The map $Q$ is the usual embedding of a quaternion algebra that contains $E = F(\theta)$ into $M_2(E)$. A direct computation shows that $Q$ is multiplicative, $\det Q(x) = \mathrm{nrm}(x)$, and $\sigma(Q(x))^{\mathsf T} H Q(x) = H$ when $\mathrm{nrm}(x) = 1$ and $b f_1 = -f_2$. Also $\det (1 + A(X - 1)B) = \det X$ when $B A = 1$, and $X \mapsto 1 + A(X - 1)B$ is multiplicative.

By facts 1 and 2, $f_1 = h(e_1, e_1)$ and $f_2 = h(e_2, e_2)$ lie in $F^\times$. Take $\theta$ and $\delta$ from fact 3; $\delta \neq 0$. Let $G$ be the matrix of $g$. By hypothesis $G$ fixes the rational vectors $v$ with $B v = 0$, so facts 4 and 5 give $G = 1 + A (X - 1) B$ with $\sigma(X)^{\mathsf T} H X = H$. Then $\det X = \det G = 1$, and fact 6 gives $x$ with $Q(x) = X$. From $\mathrm{nrm}(x) = \det Q(x) = 1$, and the injectivity of $\mathbb{A}_F \to \mathbb{A}_E$, $x$ has norm one. Fact 7, applied to $t$, gives $p$ and $q$, and the theorem on quaternions split at $S$, applied to $a = \delta$ and $b = -f_2/f_1$, gives $x$ in the closure of $H_0(\varepsilon)$.

Let $\Phi(y) = 1 + A (Q(y) - 1) B$ for $y$ of norm one. Then $\Phi(y)$ lies in $\mathrm{SU}_J(\mathbb{A}_F)$, $\Phi$ is multiplicative, and $\Phi(y)^{-1} = \Phi(\bar y)$. By fact 8 and the continuity of conjugation, $\Phi$ is continuous on the norm-one elements. Also $\Phi(x) = G$, so $\Phi(x) = g$.

Let $\hat\gamma h \in H_0(\varepsilon)$. Then $\Phi(\hat\gamma h) = \Phi(\hat\gamma) \Phi(h)$. The matrix $\Phi(\hat\gamma)$ is the image of the matrix $1 + A (Q(\gamma) - 1) B$ over $E$, which lies in $U_J(F)$ and has determinant $1$, so $\Phi(\hat\gamma) \in \mathrm{SU}_J(F)$. Since $Q$ is linear over $\mathbb{A}_F$, $Q(h) - 1 = \varepsilon \, Q(h - 1)$, so $\Phi(h) - 1 = \varepsilon A Q(h - 1) B$, and $\varepsilon^2 = \varepsilon$ gives $\Phi(h) \in \mathrm{SU}_J(\varepsilon)$. So $\Phi$ maps $H_0(\varepsilon)$ into the target set. By continuity, $g = \Phi(x)$ lies in the closure of $\Phi(H_0(\varepsilon))$, hence in the closure of the target set. $\square$

**Remark 1.12.3 (Classical form).** For a nondegenerate binary Hermitian space $P$ over a quadratic extension $E = F(\theta)$, with an orthogonal basis of lengths $f_1, f_2$, the group $\mathrm{SU}(P)$ is the norm-one group of the quaternion algebra $(\delta, -f_2/f_1)_F$, $\theta^2 = \delta$; the map $\Phi$ of the proof is this isomorphism, made explicit. With it, strong approximation for $\mathrm{SU}(P)$ is a case of strong approximation for $D^1$ (V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Chapter 7). The theorem here asks that $-f_1/f_2$ be a norm from $E_v$ at every $v \in S$, which makes $D$ split at every place of $S$; the classical theorem needs a single place of $S$ where $\mathrm{SU}(P)(F_v)$ is not compact.

**Remark 1.12.4 (Formalization).** The special unitary groups are defined in [NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L19). They use the namespace `Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes` for `IsCMExt`, `IsHermND`, `hE` and `HA`, whose definitions are the same as those of the earlier sections. The matrices $A$, $B$, $H$, the map $Q$ and the map $X \mapsto 1 + A(X - 1)B$ are `planeA`, `planeB`, `planeH`, `qm` and `emb` in [EmbUnitary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EmbUnitary.lean#L20), with the computations `det_qm`, `qm_mul`, `qm_unitary`, `det_emb`, `emb_mul` and `emb_unitary`. The facts of the proof are `GlobalTheory.CMConjInvol.cm_conj_invol_fixed`, `GlobalTheory.T.orthogonalAnisotropicPair_planeMatrices_facts`, `GlobalTheory.QuadNormBase.exists_basis`, `GlobalTheory.T.matrix_fixes_lowRankProjector_of_fixes_rationalKernel`, `GlobalTheory.T.unitary_fixing_kernel_eq_oneAddLowRank_of_unitary`, `GlobalTheory.T.exists_quaternionMatrix_eq_of_unitary_det_one`, `GlobalTheory.T.neg_inv_ratio_isNorm_of_neg_ratio_isNorm` and `GlobalTheory.T.continuous_oneAddLowRankEmbedding_quaternionMatrix`. The fact $\varepsilon^2 = \varepsilon$ for a place idempotent, proved twice in the last section, is proved a third time inline at [line 178](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpecialUnitaryFixingPlaneComplementMemClosure.lean#L178). The wrapper `GlobalTheory.T.specialUnitary_fixing_plane_complement_mem_closure` restates `GlobalTheory.PlaneSU.plane_closure` without change.
