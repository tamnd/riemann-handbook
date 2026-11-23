---
title: Uniformized members of the eighth power
decls:
  - GlobalTheory.Mum.PowData.exists_tens
  - GlobalTheory.T.degenerationData_eighthPower_via_characterMaps
  - GlobalTheory.Mum.PowData.sharpRef_of_characters
  - GlobalTheory.T.eighthPowerDegData_latticeIso_equivariant
  - GlobalTheory.Poinc.Sep.sharpRef_equivariant_of_unif_pow
  - GlobalTheory.T.uniformisation_eighthPower_data_equivariant
  - GlobalTheory.Poinc.Sep.unif_pow_equivariant
  - GlobalTheory.T.exists_uniformised_member_of_refined_uniformisation
  - GlobalTheory.Poinc.Sep.MkMember.exists_uMem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniformized members of the eighth power

Theta functions on the Siegel family are built from the eighth power of the universal abelian scheme, with the bundle twisted by a form $W$ of type $E_8$. This section proves that a uniformization of a refinement of Mumford data $Q$ gives a uniformization of the eighth power, with degeneration data that are a sharp refinement of $Q$ and with a lattice isomorphism that intertwines the action of integer matrices. Such a uniformization at a point of a theta setup is a *uniformized member*. Members are the input of the [Fourier term systems](/entry/exists-v-pre-traits-chart/) used for [separation at the centre](/entry/sep-st/).

We keep the notation of the previous sections. $W$ is an $8 \times 8$ integer matrix with $W + W^{T}$ positive definite of determinant $1$, so $W + W^{T}$ is the $E_8$ form. For $a \in M_8(\mathbb{Z})$ and $\mu \in Y^8$ we write $(a\mu)_u = \sum_v a_{uv}\mu_v$. For a family $\mathrm{pr}_1, \dots, \mathrm{pr}_8$ of homomorphisms $P \to C$ of commutative group schemes, the family is a *product* if each $\mathrm{pr}_a$ is a homomorphism and $P \to C^8$ is an isomorphism.

**Definition 9.11.1 (Sharp refinement).** Let $\rho : V \to V_1$ be a ring map of domains, $Q$ Mumford data over $V$, $D$ degeneration data over $V_1$ and $e : Y_Q^8 \cong Y_D$. Then $(D, e)$ is a *sharp refinement* of $Q$ along $\rho$ for $W$ if there are a product $\mathrm{pr}_1, \dots, \mathrm{pr}_8 : B_D \to \rho^* B_Q$ and a generating isomorphism $w$ of $L_D$ with the combination of the bundles $(\mathrm{pr}_a, \mathrm{pr}_b)^*\Lambda(M_Q)$ with weights $W_{ab}$, such that $\mathrm{pr}_a \circ c_D(e\mu) = \rho^* c_Q(\mu_a)$ and
$$\psi_D(e\mu) = w \cdot \prod_{a, b} \tau_Q(\mu_a, \mu_b)^{W_{ab}}.$$

Lean: `GlobalTheory.Poinc.Sep.SharpRef`.

So $B_D$ is the eighth power of $B_Q$, and the data of $D$ are those of $Q$ twisted by $W$. The *tensor data* $T$ of degeneration data $D$ over $D_0$ with matrix $W$ are the hypotheses of the theorem on factors of unimodular tensors, with $D_0$ in place of $Q$: a product $\mathrm{pr}_i : B_D \to B_{D_0}$, an isomorphism $x_T : Y_D \cong Y_{D_0}^{r}$ with $c_D(z) \circ \mathrm{pr}_i = c_{D_0}(x_T(z)_i)$, and a generating $w$ with the formula for $\psi_D$ (Lean: `GlobalTheory.Mum.Tens`).

**Theorem 9.11.2 (Tensor data from a power).** Let $R$ be a local domain that is an admissible base of characteristic $0$. Let $U, U_0$ be uniformizations of semi-abelian groups $G, G_0$ by $D, A$ and $D_0, A_0$. Let $W, N$ be integer $r \times r$ matrices with $(W + W^{T}) N = 1$, and let $q_1, \dots, q_r : G \to G_0$ be a product such that
$$[L_U] = \sum_{a, b} W_{ab}\,(q_a, q_b)^*[\Lambda(L_{U_0})].$$
Let $h_u : Y_{D_0} \to Y_D$ be additive maps such that $q_u$ acts on the tori by $h_u$ on characters, and let $x : Y_D \cong Y_{D_0}^{r}$ with $x^{-1}(\mu) = \sum_u h_u\big(((W + W^{T})\mu)_u\big)$. Then there are tensor data $T$ of $D$ over $D_0$ with matrix $W$ and $x_T = x$.

Lean: `GlobalTheory.Mum.PowData.exists_tens`.

*Proof.* The matrix $N$ is symmetric, as it is the inverse of a symmetric matrix. From the $q_u$ and $N$ build the inclusions $j_u : G_0 \to G$ and the maps that split $G$ as a product, and show that they are adjoint in pairs for the classes of $L_U$ and $L_{U_0}$. A lemma on abelian homomorphisms gives the maps of abelian parts $B_D \to B_{D_0}$ and back, and a lemma on characters shows that the lattice maps are constant along the uniformization. Two lemmas on adjoint retracts give the periods and the abelian parts of the split. A lemma on power data then gives the isomorphism $w$ and the formula for $\psi_D$. The product property of the maps of abelian parts comes from the inclusions. $\square$

**Theorem 9.11.3 (Sharp refinement from characters).** Let $V$ be a local domain, $Q$ Mumford data over $V$, $V_1$ a local CN domain and $\rho : V \to V_1$ injective and finite. Let $D_0$ refine $Q$ along $\rho$ and $e_0 : Y_{D_0} \cong Y_Q$, and let $U_0$ be a uniformization of a semi-abelian group $G_0$ by $D_0$ and $A_0$, where $A_0$ is the group pullback of $A$ along $y : \operatorname{Spec} K_{V_1} \to X$ by $\alpha$, with bundles. Let $c$ be a Siegel datum over $K_{V_1}$ that is the group pullback of $(A, P, \ell)$ along $y$ by $\varphi_c$, with bundles and level structures. Let $P_1$ be a polarized abelian scheme over $K_{V_1}$ with a product $\mathrm{pr}_1, \dots, \mathrm{pr}_8 : P_1 \to c$ and bundle isomorphic to the combination of $(\mathrm{pr}_a, \mathrm{pr}_b)^*\Lambda$ with weights $W_{ab}$. Let $U$ be a uniformization of a semi-abelian group $G$ by $D$ and $P_1$, and $q_1, \dots, q_8 : G \to G_0$ a product with $\alpha \circ q_u = \varphi_c \circ \mathrm{pr}_u$ on generic fibres. Let $h_u : Y_{D_0} \to Y_D$ match $q_u$ on the tori, and let
$$e(\mu) = \sum_u h_u\Big(e_0^{-1}\big(((W + W^{T})\mu)_u\big)\Big).$$
Then $(D, e)$ is a sharp refinement of $Q$ along $\rho$ for $W$.

Lean: `GlobalTheory.Mum.PowData.sharpRef_of_characters` (also `GlobalTheory.T.degenerationData_eighthPower_via_characterMaps`, a wrapper).

*Proof.* As $V_1$ is a CN domain, it is an admissible base of characteristic $0$. A lemma on bundle classes gives the class of $L_U$ as $\sum_{a, b} W_{ab}\,(q_a, q_b)^*[\Lambda(L_{U_0})]$. By uniqueness of torus maps and a lemma on toric matches, each $q_u$ acts on the tori by $h_u$. The previous theorem with $N = (W + W^{T})^{-1}$ gives tensor data of $D$ over $D_0$ with $x_T = e^{-1}$ up to $e_0$. A lemma on refinements of tensors turns tensor data over a refinement of $Q$ into a sharp refinement of $Q$. $\square$

**Theorem 9.11.4 (Equivariant sharp refinement).** In the setting of the previous theorem, without the maps $h_u$ and $e$, there is $e : Y_Q^8 \cong Y_D$ such that $(D, e)$ is a sharp refinement of $Q$ along $\rho$ for $W$, and for all $a, a' \in M_8(\mathbb{Z})$ with $(W + W^{T}) a' = a^{T} (W + W^{T})$ and each endomorphism $E$ of $U$ with $q_u \circ E_G = \prod_v q_v^{a_{uv}}$, the lattice map of $E$ satisfies $E_h(e\mu) = e(a'\mu)$.

Lean: `GlobalTheory.Poinc.Sep.sharpRef_equivariant_of_unif_pow` (also `GlobalTheory.T.eighthPowerDegData_latticeIso_equivariant`, a wrapper).

Here an *endomorphism* $E$ of a uniformization consists of endomorphisms $E_G$, $E_A$, $E_B$ of $G$, $A$, $B_D$ and an additive $E_h : Y_D \to Y_D$ such that $E_G$ is linear over $(E_B, E_h)$ and agrees with $E_A$ on the generic fibre (Lean: `GlobalTheory.UT.EndU`).

*Proof.* A lemma on eightfold products gives character maps $h_u : Y_{D_0} \to Y_D$ that match the $q_u$ on the tori, with $\mu \mapsto \sum_u h_u(\mu_u)$ bijective. Define $e$ by the formula of the previous theorem. It is bijective, as $W + W^{T}$ has determinant $1$ and so is invertible over $\mathbb{Z}$. The previous theorem gives the sharp refinement. For $E$ as in the statement, a lemma on closed fibres shows that $E_G$ acts on the torus through $E_h$, and a lemma on integral matrix actions gives $E_h(h_v(x)) = \sum_u h_u(a_{uv} x)$. Then
$$\begin{aligned} E_h(e\mu) &= \sum_u h_u\Big(e_0^{-1}\big((a^{T}(W + W^{T})\mu)_u\big)\Big) \\ &= \sum_u h_u\Big(e_0^{-1}\big(((W + W^{T}) a'\mu)_u\big)\Big) = e(a'\mu). \end{aligned}$$
$\square$

**Theorem 9.11.5 (Uniformized eighth power).** In the setting of the previous theorem, without the maps $q_u$: there is $e : Y_Q^8 \cong Y_D$ such that $(D, e)$ is a sharp refinement of $Q$ along $\rho$ for $W$, and for all $a, a'$ with $(W + W^{T}) a' = a^{T} (W + W^{T})$ and each endomorphism $a_A$ of $P_1$ with $\mathrm{pr}_u \circ a_A = \prod_v \mathrm{pr}_v^{a_{uv}}$, there is an endomorphism $E$ of $U$ with $E_A = a_A$ and $E_h(e\mu) = e(a'\mu)$.

Lean: `GlobalTheory.Poinc.Sep.unif_pow_equivariant` (also `GlobalTheory.T.uniformisation_eighthPower_data_equivariant`, a wrapper).

*Proof.* A lemma on power models gives a product $q_1, \dots, q_8 : G \to G_0$ with $\alpha \circ q_u = \varphi_c \circ \mathrm{pr}_u$ on generic fibres. The previous theorem gives $e$. Given $a_A$, it is a homomorphism, as the $\mathrm{pr}_u$ form a product. Extend $a_A$ from the generic fibre to an endomorphism of $G$ by the extension theorem for homomorphisms of semi-abelian schemes, and a lemma on degeneration endomorphisms over an admissible base makes it an endomorphism $E$ of $U$ with $E_A = a_A$. A lemma on eighth powers shows that $q_u \circ E_G = \prod_v q_v^{a_{uv}}$, so the previous theorem gives $E_h(e\mu) = e(a'\mu)$. $\square$

**Definition 9.11.6 (Theta setup and members).** A *theta setup* $X_1$ for $(F, W, i)$ consists of a theta system $S$ over an arithmetic base with ring $S_R$, a polarized abelian scheme $P_X$ over $S_R$ and $u : \operatorname{Spec} S_R \to X$ such that $P_X$ is the eighth power of the pullback of $(A, P)$ along $u$ twisted by $W$, with generic image, and a normal rational model $Z_1$ with a finite map $\pi_1 : Z_1 \to Z$ compatible with $u$ and $i$ (Lean: `GlobalTheory.Poinc.Setup`). An *action* is a map $a \mapsto \mathrm{act}(a)$ from $M_8(\mathbb{Z})$ to endomorphisms of $P_X$ with $\mathrm{pr}_u \circ \mathrm{act}(a) = \prod_v \mathrm{pr}_v^{a_{uv}}$ for a product as above.

Let $z_1 \in Z_1$, $\mathrm{ev} : \mathcal{O}_{Z_1, z_1} \to V$, $t_1, \dots, t_m \in V$ and forms $\delta_k$ on a lattice $Y$. A *uniformized member* at $(z_1, \mathrm{ev})$ consists of degeneration data $D$ over $V$, $e_8 : Y^8 \cong Y_D$, a uniformization $U$ of a semi-abelian group $G$ by $D$ and $A_1$, and $\phi$ with $A_1$ the group pullback of $P_X$ by $\phi$ with bundles, such that:

1. $V$ is a CN domain, $\mathrm{ev}$ is local and regular at $z_1$, and the generic point of $V$ maps to $S_R$ by a map $y_K$ given by values on $Z_1$;
2. for $a, a'$ with $(W + W^{T}) a' = a^{T} (W + W^{T})$ there is an endomorphism $E$ of $U$ with $\phi \circ E_A = \mathrm{act}(a) \circ \phi$ and $E_h(e_8\mu) = e_8(a'\mu)$;
3. each $\psi_D(e_8\mu)$ has coordinate a unit times $\prod_k t_k^{q_W(\delta_k)(\mu)}$.

Lean: `GlobalTheory.Poinc.Sep.UMem` (also `GlobalTheory.Poinc.Sep.IsAct`, `GlobalTheory.Poinc.Sep.RegAt`).

**Theorem 9.11.7 (Uniformized members exist).** Let $(Z, z, i)$ be a theta compactification of $F$ with matrix $W$, $X_1$ a theta setup with an action, and $Q$ Mumford data over a local domain $V$ with monomial periods $t^\delta$, where $t_k \ne 0$ and the $\delta_k$ are symmetric with $\delta_k(y, y) \ge 0$. Let $V_1$ be a local CN domain, $\rho : V \to V_1$ finite and injective, $D_0$ refine $Q$ along $\rho$, and $U_0$ a uniformization of a semi-abelian $G_0$ by $D_0$ and $A_0$, where $A_0$ is the group pullback of $A$ along $y$ with bundles. Let $\mathrm{ev} : \mathcal{O}_{Z_1, z_1} \to V_1$ be local and regular at $z_1$, compatible with $y$. Then there is a uniformized member $\mathfrak{m}$ at $(z_1, \mathrm{ev})$ for $\rho \circ t$ and $\delta$ such that $(\mathfrak{m}.D, \mathfrak{m}.e_8)$ is a sharp refinement of $Q$ along $\rho$ for $W$.

Lean: `GlobalTheory.Poinc.Sep.MkMember.exists_uMem` (also `GlobalTheory.T.exists_uniformised_member_of_refined_uniformisation`, a wrapper).

*Proof.* A lemma on theta values gives $y_K$, lying over the moduli point $y$. A lemma on polarized fibres gives $A_1$ with $\phi$, the pullback of $P_X$ along $\operatorname{Spec} y_K$. As the action exists, a lemma on endomorphisms of the eighth power shows that $A_1$ is again an eighth power of a Siegel datum twisted by $W$. A lemma on eighth powers gives $D$ and $U$ on the eighth power $G_0^8$, which is semi-abelian. The previous theorem gives $e$, the sharp refinement and clause 2. A lemma on trivializations of the eighth power gives clause 3. $\square$

**Remark 9.11.8 (Formalization).** The theorem `sharpRef_of_characters` discards five hypotheses: that $\rho$ is injective and finite, the compatibility of level structures, and that the $\mathrm{pr}_a$ are homomorphisms forming a product ([DegenerationDataEighthPowerViaCharacterMaps.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationDataEighthPowerViaCharacterMaps.lean#L213)). The theorem `exists_uMem` names the hypotheses `hg`, `hn`, `hodd`, `hproj`, `hnorm`, `hiz`, `hdense` and `hTI` but does not use them ([ExistsUniformisedMemberOfRefinedUniformisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniformisedMemberOfRefinedUniformisation.lean#L24)). The extension of $a_A$ is the helper `PowEq.endU_exists`, which calls `SemiAbelianHomExtension.fractionField` ([UniformisationEighthPowerDataEquivariant.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisationEighthPowerDataEquivariant.lean#L20)). The bundle combinations `LinComb`, the predicates `OnTorus`, `TorMatch`, `PsiCoord`, `Refines` and `IsDiagEnd`, and the structures `ThetaSys` and `RatModel` are not unfolded here. The lemmas cited in the proofs have no entries in this part; we use only their statements.
