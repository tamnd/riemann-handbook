---
title: Finiteness for unitary groups
decls:
  - PositivityTheory.RgHf.harishChandraFinite
  - GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_constTerm
  - GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_formsOn
  - GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.Rg.finite_cuspOn
  - GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.CoreGL.Rg.finite_slices_glPart
  - GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.UCore.Rg.finite_slices_uPart
  - GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.UCore.Rg.finite_slices_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness for unitary groups

This section proves the finiteness theorem of Harish-Chandra for a unitary group $G = \mathrm{U}(V)$ of a Hermitian space over a CM field. The plan is the one of the previous section, with one more layer. A form is cut into its cuspidal part and its constant terms. The constant terms along a standard parabolic subgroup are forms on that parabolic, and they are handled by downward induction on the parabolic. At the end one must bound the forms on a parabolic $P_T$ that are cuspidal along every larger parabolic. Their restrictions to the Levi subgroup $M_T$ are cut into slices along the factors of $M_T$: general linear groups over the CM field, to which the results for $\mathrm{GL}_d$ over a totally complex field apply, and one smaller unitary group. See [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms) for the background.

### The setting

Let $E/F$ be a CM extension of number fields with conjugation $x \mapsto \bar{x}$, and $V$ a nondegenerate Hermitian space over $E$ of dimension $n$ with Gram matrix $J$. Write $G(\mathbb{A})$ for the unitary group of $V$ over $\mathbb{A}_F$, $G(F)$ for its rational points, $G_f$ for the elements trivial at the infinite places and $G_\infty$ for the elements trivial at the finite places. For each infinite place $\tau$ of $F$, fix a signature $\varepsilon_\tau$ and an invertible matrix $P_\tau$ with $P_\tau^* J_{\varepsilon_\tau} P_\tau = J_\tau$, where $J_{\varepsilon_\tau}$ is the diagonal matrix of signs. Conjugation by $P_\tau$ identifies $G_\tau$ with $\mathrm{U}(p, q)$, and the compact group $K_\tau = \mathrm{U}(p) \times \mathrm{U}(q)$ embeds into $G(\mathbb{A})$ at the place $\tau$ by $k \mapsto P_\tau^{-1} k P_\tau$.

For a matrix $Z \in M_n(\mathbb{C})$, let $R_\tau(Z)$ be the complex linear extension at $\tau$ of the derivative $R(X)\varphi(g) = \frac{d}{dt}\varphi(g \exp tX)|_{t=0}$ from the Lie algebra of $G_\tau$. For $k \ge 0$ put
$$\Delta_{\tau,k} = \sum_{i_0, \dots, i_k} R_\tau(E_{i_0 i_1}) R_\tau(E_{i_1 i_2}) \cdots R_\tau(E_{i_k i_0}),$$
with $E_{ij}$ the matrix units. These are the Gelfand elements of the center of the enveloping algebra.

**Definition 1.5.1 (Smooth automorphic function).** A function $\varphi$ on $G(\mathbb{A})$ is a *smooth automorphic function* if it is left invariant under $G(F)$, continuous, right invariant under $U \cap G_f$ for some open subgroup $U$, smooth along $G_\infty$, lies in a finite-dimensional space stable under all $\Delta_{\tau,k}$, and has moderate growth: there is $N$ such that for every word $D$ in the derivatives and every $x$ there is $C$ with $|D\varphi(x g)| \le C \|g\|^N$ for $g \in G_\infty$.

Let $U \subseteq G(\mathbb{A})$ be open, $\rho_\tau$ a representation of $K_\tau$ on a finite-dimensional space $W_\tau$ for each $\tau$, and $c_\tau(k) \in \mathbb{C}$. Let $\mathcal{A}(U, \rho, c)$ be the set of smooth automorphic functions $\varphi$ with $\varphi(g u) = \varphi(g)$ for $u \in U \cap G_f$, with $k \mapsto \varphi(x k)$ in the coefficient space of $\rho_\tau$ for every $x$ and $\tau$, and with $\Delta_{\tau,k}\varphi = c_\tau(k)\varphi$ for all $\tau$ and $k$.

**Theorem 1.5.2 (Harish-Chandra finiteness for unitary groups).** Assume that each $\rho_\tau$ is continuous. Then $\mathcal{A}(U, \rho, c)$ spans a finite-dimensional space.

Lean: `PositivityTheory.RgHf.harishChandraFinite`.

*Proof.* For each $r \le n$ for which an isotropic frame exists, choose one: a matrix $C$ with $r > 0$ linearly independent columns and $C^* J C = 0$. Let $\Psi$ map $\varphi$ to the family of its constant terms along the unipotent radicals of the flags of these frames. By [the finiteness of constant terms](/entry/finite-const-term/), $\Psi$ takes values in a finite-dimensional space. If $\Psi\varphi = 0$, then $\varphi$ is cuspidal: a function is cuspidal when its constant terms along all isotropic subspaces vanish, and for a left $G(F)$-invariant function the vanishing along one isotropic frame of size $r$ implies it along every frame of size $r$. So $\ker \Psi$ lies in the span of the cuspidal elements of $\mathcal{A}(U, \rho, c)$, which is finite-dimensional by the finiteness theorem for cusp forms. The span is then finite-dimensional, since the kernel and the image of $\Psi$ are. $\square$

### Standard parabolic subgroups

A *Witt frame* is a pair of $n \times m$ matrices $X, Y$ over $E$ with $X^* J X = 0$, $Y^* J Y = 0$, $X^* J Y = 1$, and with the orthogonal complement of the columns anisotropic. For $T \subseteq \{0, \dots, m-1\}$ let $N_T$ be the unipotent radical of the stabilizer of the flag of subspaces spanned by the first $k+1$ columns of $X$, $k \in T$, and let $M_T$ be the stabilizer of the first $k+1$ columns of both $X$ and $Y$ for $k \in T$. Let $\mathcal{A}_T(U, \rho, c)$ be the set of continuous functions $\varphi$ that are smooth of moderate growth, left invariant under $N_T(\mathbb{A})$ and $G(F) \cap M_T(\mathbb{A})$, and satisfy the level, type and eigenvalue conditions of $\mathcal{A}(U, \rho, c)$. A function $c$ is *the constant term of $\varphi$ along $T$* if $c(g) = \int_{\mathcal{F}} \varphi(u g)\, d\mu(u)$ for all Haar measures $\mu$ on $N_T(\mathbb{A})$ and all fundamental domains $\mathcal{F}$ of $N_T(F)$ with $\mu(\mathcal{F}) = 1$.

We use these facts on constant terms. The groups $N_T(F) \backslash N_T(\mathbb{A})$ are compact. If $S \subseteq T$, then $N_S \subseteq N_T$ and $M_T \subseteq M_S$. A constant term is unique, it exists for functions left invariant under $N_T(F)$, and taking constant terms is transitive: if $S \subseteq T$, $c$ is the constant term of $\varphi$ along $S$ and $c'$ that of $c$ along $T$, then $c'$ is the constant term of $\varphi$ along $T$. If $S \subseteq T$ with $T$ nonempty, the constant term along $T$ of an element of $\mathcal{A}_S(U, \rho, c)$ lies in $\mathcal{A}_T(U, \rho, c)$, and $\mathcal{A}(U, \rho, c) \subseteq \mathcal{A}_\emptyset(U, \rho, c)$.

**Theorem 1.5.3 (Finiteness of constant terms).** Assume each $\rho_\tau$ continuous. For each isotropic frame $C$ with $r$ columns, the constant terms along the flag of $C$ of the elements of $\mathcal{A}(U, \rho, c)$ span a finite-dimensional space.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_constTerm`.

*Proof.* Extend $C$ to a Witt frame $(X, Y)$ whose first $r$ columns of $X$ are those of $C$. The constant term along the flag of $C$ is the constant term along $T = \{r-1\}$. It maps $\mathcal{A}(U, \rho, c) \subseteq \mathcal{A}_\emptyset(U, \rho, c)$ into $\mathcal{A}_{\{r-1\}}(U, \rho, c)$, whose span is finite-dimensional by [the finiteness on parabolics](/entry/finite-forms-on/). $\square$

**Theorem 1.5.4 (Finiteness on parabolic subgroups).** Assume each $\rho_\tau$ continuous, and let $(X, Y)$ be a Witt frame. For each nonempty $T$, the span of $\mathcal{A}_T(U, \rho, c)$ is finite-dimensional.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.ConstFin.Rg.finite_formsOn`.

*Proof.* By strong induction on the number $j$ of indices outside $T$. For each $k \notin T$, the constant term along $T \cup \{k\}$ is a linear map $L_k$ from the span of $\mathcal{A}_T(U, \rho, c)$ into the span of $\mathcal{A}_{T \cup \{k\}}(U, \rho, c)$, which is finite-dimensional by the induction hypothesis. Let $\Psi = (L_k)_{k \notin T}$. If $\Psi\varphi = 0$ and $T \subsetneq T'$, choose $k \in T' \setminus T$; the constant term of $\varphi$ along $T \cup \{k\}$ is $0$, so by transitivity the constant term of $\varphi$ along $T'$ is $0$. So $\ker \Psi$ lies in the span of the elements of $\mathcal{A}_T(U, \rho, c)$ whose constant terms along all $T' \supsetneq T$ vanish, which is finite-dimensional by [the cuspidal finiteness on parabolics](/entry/finite-cusp-on/). $\square$

### Cuspidal forms on a parabolic subgroup

Let $\mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ be the set of $\varphi \in \mathcal{A}_T(U, \rho, c)$ whose constant terms along every $T' \supsetneq T$ vanish. The Levi subgroup has the parts $H_0$, the pointwise stabilizer of the columns $X_i, Y_i$ with $i \le \max T$, which is the unitary group of their orthogonal complement, and $H_k$ for $k \in T$, the elements of $M_T$ that fix the orthogonal complement of the columns $X_i, Y_i$ in the block of $k$; these are general linear groups over $E$. For a set $\mathcal{C}$ of functions on a group $G$, subgroups $H \subseteq L$ and $b \in G$, the *slices* of $\mathcal{C}$ are the functions $t \mapsto \varphi(t y b)$ on $H$ with $\varphi \in \mathcal{C}$ and $y \in L$ commuting with $H$.

**Lemma 1.5.5 (Finiteness from parts).** Let $H_i$, $i \in I$ finite, be subgroups of a group $G$ such that elements of different $H_i$ commute, and let $L$ be the subgroup they generate. Let $\mathcal{C}$ be a set of functions and $B \subseteq G$ finite such that each $\varphi$ in the span of $\mathcal{C}$ that vanishes on $L B$ is $0$. If for each $i$ and $b$ the slices of $\mathcal{C}$ along $H_i$, $L$ and $b$ span a finite-dimensional space, then the span of $\mathcal{C}$ is finite-dimensional.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.Rg.finiteDimensional_of_parts`.

*Proof.* The product map $P : \prod_i H_i \to G$ is a homomorphism onto $L$. For $b \in B$ the functions $x \mapsto \varphi(P(x) b)$ on $\prod_i H_i$ have, in each variable, slices among the slices of $\mathcal{C}$ along $H_i$. A space of functions on a finite product whose slices in each variable lie in given finite-dimensional spaces is finite-dimensional; this is the lemma on slices of the previous section for several factors. The map $\varphi \mapsto (x \mapsto \varphi(P(x) b))_{b \in B}$ is injective on the span by the choice of $B$. $\square$

**Theorem 1.5.6 (Cuspidal finiteness on parabolics).** Assume each $\rho_\tau$ continuous, and let $(X, Y)$ be a Witt frame and $T$ nonempty. Then $\mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ spans a finite-dimensional space.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.Rg.finite_cuspOn`.

*Proof.* The parts $H_0$ and $H_k$, $k \in T$, commute with each other and generate $M_T$. There is a finite $B \subseteq G(\mathbb{A})$ such that each $\varphi \in \mathcal{A}_T(U, \rho, c)$ that vanishes on $M_T(\mathbb{A}) B$ is $0$. Apply the lemma on parts. The slices along $H_k$ are finite by [the theorem on general linear parts](/entry/finite-slices-gl-part/), and those along $H_0$ by [the theorem on the unitary part](/entry/finite-slices-u-part/). $\square$

**Theorem 1.5.7 (General linear parts).** In the setting above, for $k \in T$ and $b \in G(\mathbb{A})$, the slices of $\mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ along $H_k$, $M_T$ and $b$ span a finite-dimensional space.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.CoreGL.Rg.finite_slices_glPart`.

*Proof.* The index $k$ ends a block $[l, l+d)$ of indices that contains no other element of $T$. There is a block embedding $\iota : \mathrm{GL}_d(\mathbb{A}_E) \to G(\mathbb{A})$ with image $H_k$. Fix a maximal compact subgroup $K$ of $G_\infty$ that contains the groups $K_\tau$. Write $b = u\, \iota(y_1)\, g_0$ with $u \in N_T(\mathbb{A})$, such that $g_0^{-1} \iota(\kappa) g_0 \in K$ for $\kappa$ in the maximal compact subgroup $K_{\infty,d}$ of $\mathrm{GL}_d(E_\infty)$. There is a finite-dimensional space $S$ of functions on $K$, stable under right translation, that contains $k \mapsto \varphi(x k)$ for every $x$ and every $\varphi$ of type $\rho$; it gives a continuous representation $\rho'$ of $K_{\infty,d}$ through $\kappa \mapsto g_0^{-1}\iota(\kappa) g_0$. Let $L'$ be the preimage of $g_0 U g_0^{-1}$ under $\iota$ on finite adeles; it is open. For each $\tau$ and $u \in \mathbb{C}$ there is a monic polynomial $q_{\tau,u}$ such that $q_{\tau,u}(C_\tau(u))$ kills every function $x \mapsto \varphi(\iota(x) g)$ with $\varphi$ left invariant under $N_T(\mathbb{A})$ and $G(F) \cap M_T$ and with $\Delta_{\tau',k'}\varphi = c_{\tau'}(k')\varphi$. The set $\mathcal{J}$ of the operators $q_{\tau,u}(C_\tau(u))$ has finite codimension in the center: the algebra $\mathcal{Z}$ is the sum of a finite-dimensional space and $\mathcal{Z}\mathcal{J}$.

Now let $\varphi \in \mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ and $y \in M_T$ commute with $H_k$. The function $F(x) = \varphi(\iota(x) y g_0)$ is a cusp form on $\mathrm{GL}_d(\mathbb{A}_E)$ of level $L'$ and type $\rho'$, killed by $\mathcal{J}$. Since $E$ is totally complex, the finiteness of cusp forms on $\mathrm{GL}_d$ killed by a set of finite codimension shows that these $F$ span a finite-dimensional space. The slice is $t \mapsto \varphi(t y b) = F(\iota^{-1}(t) y_1)$, by left invariance under $N_T(\mathbb{A})$, so it lies in the image of this space under a linear map. $\square$

**Theorem 1.5.8 (Unitary part).** In the setting above, for $b \in G(\mathbb{A})$, the slices of $\mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ along $H_0$, $M_T$ and $b$ span a finite-dimensional space.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.UCore.Rg.finite_slices_uPart`.

*Proof.* Write $b = n\, m\, b_0$ with $n \in N_T(\mathbb{A})$, $m \in M_T(\mathbb{A})$, such that the frames $P_\tau$ translated by $b_0$ are adapted to $(X, Y, T)$. Write $m = m_H m_o$ with $m_H \in H_0$ and $m_o$ commuting with $H_0$. For $\varphi \in \mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$, the function $x \mapsto \varphi(x b_0)$ lies in $\mathcal{A}^{\mathrm{c}}_T$ for the level $b_0^{-1} U b_0$ and the translated frames. Since $M_T$ normalizes $N_T$, the slice $t \mapsto \varphi(t y b)$ equals $t \mapsto \varphi(t m_H (y m_o) b_0)$, a right translate by $m_H$ of a slice at $b = 1$ for the new data. The span of the slices at $1$ is finite-dimensional by [the theorem on the unitary core](/entry/finite-slices-core/). $\square$

**Theorem 1.5.9 (Unitary core).** In the setting above, assume the frames $P_\tau$ are adapted to $(X, Y, T)$. Then the slices of $\mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ along $H_0$, $M_T$ and $1$ span a finite-dimensional space.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.UCore.Rg.finite_slices_core`.

*Proof.* Let $V'$ be the orthogonal complement in $V$ of the columns $X_i, Y_i$ with $i \le \max T$, and $s : \mathrm{U}(V')(\mathbb{A}) \to G(\mathbb{A})$ the embedding, which maps onto $H_0$. The adapted frames give frames $P'_\tau$ for $V'$ and maps $j_\tau$ from the compact groups of $V'$ to $K_\tau$. There are lists $A_\tau$ of complex numbers such that $\prod_{a \in A_\tau}(\Delta'_{\tau,1} - a)$ kills each function $h \mapsto \psi(s(h) y)$, for $\psi \in \mathcal{A}_T(U, \rho, c)$ and $y \in M_T$ that commutes with $H_0$. For $\psi \in \mathcal{A}^{\mathrm{c}}_T(U, \rho, c)$ such a function is a smooth automorphic function on $\mathrm{U}(V')$, right invariant under $s^{-1}(U)$, of type $\rho_\tau \circ j_\tau$, and cuspidal. The cusp forms on $\mathrm{U}(V')$ with these properties span a finite-dimensional space. Since $s$ maps onto $H_0$, composition with $s$ is injective on functions on $H_0$, so the slices span a finite-dimensional space. $\square$

**Remark 1.5.10 (Formalization).** The cuspidal input in the main theorem is `GlobalTheory.CompanionTheory.HCCusp.cuspFinite`; we read its statement, not its proof. The main theorem is `GlobalTheory.CompanionTheory.Hypotheses₂.HCF.Rg.finite_of_cusp_of_constTerm` applied to that statement and to the finiteness of constant terms; that lemma does not use that $U$ is open, nor the hypotheses on $\theta$, the frames or $\rho$ (FiniteOfCuspOfConstTerm.lean, line 61). The level condition is imposed only for $u \in U \cap G_f$. We read only the statements of these inputs: the facts on constant terms (`GlobalTheory.StdPar.constAlong_cocompact_unique_stages`, `GlobalTheory.CompanionTheory.ConstTermConj.constTerm_eq_zero_of_frame`), the separating set (`GlobalTheory.T.archimedean_frame_K_type_decomposition`), the parts (`GlobalTheory.T.levi_parts_commute`, `GlobalTheory.T.levi_eq_iSup_parts`), the monic polynomials (`GlobalTheory.CompanionTheory.Hypotheses₂.LeviPart.MonicBlock.monic_block`), the finite codimension (`GlobalTheory.T.cofinite_of_capelli_monic`), the finiteness of cusp forms on $\mathrm{GL}_d$ (`GlobalTheory.CompanionTheory.CuspFinGL.Split.cuspFin`), the decomposition of $b$ (`GlobalTheory.T.langlands_decomposition_unipotent_levi`), and for the unitary core `GlobalTheory.T.constant_term_parabolic_eigenfunction` and `GlobalTheory.T.constant_term_parabolic_finite_type`. The statement files do not match their names: `archimedean_frame_K_type_decomposition` is in LeviPartsCommuteStatement.lean, `levi_parts_commute` in LeviEqISupPartsStatement.lean, `levi_eq_iSup_parts` in AdelicHaarFiniteInfiniteProductStatement.lean, and `constant_term_parabolic_finite_type`, the finiteness of cusp forms on $\mathrm{U}(V')$ killed by polynomials in $\Delta'_{\tau,1}$, in CasimirAnnihilatedCuspFormsFiniteDimensionalStatement.lean. Indices of frames start at $0$.
