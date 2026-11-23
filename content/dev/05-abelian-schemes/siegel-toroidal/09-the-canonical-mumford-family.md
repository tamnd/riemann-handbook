---
title: The canonical Mumford family
decls:
  - GlobalTheory.T.exists_mumford_family
  - GlobalTheory.TChart.Taut.exists_family
  - GlobalTheory.T.exists_canonical_mumford_family_monomial_periods
  - GlobalTheory.Mum.exists_canonOn_of_isMonomialTau
  - GlobalTheory.T.nonempty_of_tensorData_posDef_unimodular
  - GlobalTheory.Mum.PFactor.nonempty_of_tens
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The canonical Mumford family

This section proves that Mumford data with monomial periods over a CN domain carry a semi-abelian group $G$ with a bundle $P$ on $G \times G$ that is a Mumford polarization and is canonical where the periods are units. The group is the image of an idempotent in the uniformized group of a tensor construction, as in the section on [the image of an idempotent](/entry/image-unif/); the tensor uses a form of type $E_8$. For a tautological chart this gives the Mumford family of Step 5 in the proof of the [theorem on tautological charts](/entry/exists-chart-at/), with abelian locus and rational torsion.

We keep the notation of the previous sections. $R$ is a local domain, $K = K_R$, and $Q$ is Mumford data over $R$ with abelian scheme $B_Q$, bundle $M_Q$, lattice $Y_Q$, map $c_Q$ and periods $\tau_Q$. For $a, b \in Y_Q$ and $k \in K^\times$ we say that $\tau_Q(a, b)$ *has coordinate* $k$ if $\tau_Q(a, b)$ is $k$ times a generating section of the bundle on $\operatorname{Spec} K$ in which $\tau_Q(a, b)$ lies. The data $Q$ are *positive* if for each $y \ne 0$ the period $\tau_Q(y, y)$ has coordinate $r$ for some $r \in \mathfrak{m}_R$. For $t_1, \dots, t_m \in R$ and bilinear forms $\beta_1, \dots, \beta_m$ on $Y_Q$, the data $Q$ have *monomial periods* $t^\beta$ if each $\tau_Q(a, b)$ has coordinate $\prod_i t_i^{\beta_i(a, b)}$. If the $t_i$ lie in $\mathfrak{m}_R$, the $\beta_i(y, y)$ are $\ge 0$, and for each $y \ne 0$ some $\beta_i(y, y) > 0$, then monomial periods $t^\beta$ make $Q$ positive.

**Definition 9.9.1 (Factor with a Mumford model).** Let $D'$ be degeneration data over $R$. A *factor* of $D'$ with Mumford model $Q$ consists of the same objects as a factor in the previous sections, with $Q$ in place of $D$: a ring $O$ with involution acting on $D'$, elements $e, f \in O$ with $e^2 = e$, homomorphisms $\mathrm{inc} : B_Q \to B_{D'}$, $\mathrm{pr} : B_{D'} \to B_Q$, additive maps $\xi : Y_Q \to Y'$, $\xi_p : Y' \to Y_Q$, and a generating isomorphism $w : \Lambda(M_Q) \cong (\mathrm{inc} \times \mathrm{act}(f)\,\mathrm{inc})^* \Lambda(L_{D'})$, with clauses 1 to 3 of a factor, $\tau_Q(a, b) = w \cdot \tau_{D'}(\xi(a), f\xi(b))$, and the three conditions of algebraicity.

Lean: `GlobalTheory.Mum.PFactor`.

**Definition 9.9.2 (Mumford polarization).** Let $G$ be a commutative group scheme over $R$ and $P$ a line bundle on $G \times_R G$. Then $(Q, G, P)$ is a *Mumford polarization* if $R$ is a CN domain, $Q$ is positive, $G$ is semi-abelian, $P$ is birigidified, and for each local CN domain $R'$ with an injective finite map $\rho : R \to R'$ and all degeneration data $D$ over $R'$ that refine $Q$ along $\rho$ and some $Y_D \cong Y_Q$, there are a group scheme $G'$ over $R'$, a polarized abelian scheme $A'$ over $K_{R'}$, a uniformization $U$ of $G'$ by $D$ and $A'$, and $\pi : G' \to G$ such that $G'$ is the group pullback of $G$ along $\operatorname{Spec}\rho$ by $\pi$ and $\Lambda(L_U) \cong (\pi \times \pi)^* P$.

Lean: `GlobalTheory.TChart.IsMumPol`.

**Definition 9.9.3 (Canonical bundle).** Let $W \subseteq \operatorname{Spec} R$ be open. A line bundle $P$ on $G \times_R G$ is *canonical* for $Q$ over $W$ if there are degeneration data $D'$ over $R$, a factor $F$ of $D'$ with Mumford model $Q$, ring $O$ and elements $e, f$, a uniformization $U'$ of a semi-abelian group $G'$ by $D'$ and $A'$, Rosati compatible actions of $O$ on $A'$ and $G'$ for which $U'$ is $O$-linear, and homomorphisms $\mathrm{inc} : G \to G'$, $\mathrm{pr} : G' \to G$, such that:

1. the trivializations $\psi_{D'}(y)$ are units over each affine open in $W$, for all $y \in Y'$;
2. $\mathrm{pr} \circ \mathrm{inc} = 1$ and $\mathrm{inc} \circ \mathrm{pr} = \mathrm{act}(e)$;
3. $P \cong (\mathrm{inc} \times \mathrm{act}(f)\,\mathrm{inc})^* \Lambda(L_{U'})$.

Lean: `GlobalTheory.Mum.CanonOn` (also `GlobalTheory.Mum.Canon`, the same without clause 1).

**Definition 9.9.4 (Rational torsion).** A group scheme $G$ over a domain $R$ has *rational $n$-torsion* if for each algebraically closed field $k$ with a map $\kappa : K \to k$, each point $x$ of $G$ over $\operatorname{Spec} k$ with $x^n = 1$ is the image under $\operatorname{Spec}\kappa$ of a point of $G$ over $\operatorname{Spec} K$.

Lean: `GlobalTheory.TChart.TorsRat`.

**Theorem 9.9.5 (Factor of a unimodular tensor).** Let $R$ be a CN domain, $D'$ degeneration data over $R$, and $W$ an integer $r \times r$ matrix with $r \ge 1$ such that $S = W + W^{T}$ is positive definite and $\det S$ is a unit. Let $\mathrm{pr}_1, \dots, \mathrm{pr}_r : B_{D'} \to B_Q$ be homomorphisms that make $B_{D'}$ the product of $r$ copies of $B_Q$, and $x : Y' \cong Y_Q^{r}$ an isomorphism with $c'(z) \circ \mathrm{pr}_i = c_Q(x(z)_i)$. Let $w$ be a generating isomorphism of $L_{D'}$ with the tensor combination of $M_Q$ along the $\mathrm{pr}_i$ with weights from $W$, such that for all $y \in Y'$
$$\psi_{D'}(y) = w \cdot \prod_{i, j} \tau_Q\big(x(y)_i, x(y)_j\big)^{W_{ij}}.$$
Then $D'$ has a factor with Mumford model $Q$.

Lean: `GlobalTheory.Mum.PFactor.nonempty_of_tens` (also `GlobalTheory.T.nonempty_of_tensorData_posDef_unimodular`, a wrapper).

*Proof.* Let $O$ be the ring of integer $r \times r$ matrices with the involution $a^* = S^{-1} a^{T} S$, which is defined as $\det S$ is a unit. A matrix $a$ acts on $B_{D'} = B_Q^{r}$ through the $\mathrm{pr}_i$, and on $Y' \cong Y_Q^{r}$ through $x$. A lemma on Rosati adjoints shows that the action on $B_{D'}$ is Rosati compatible, and $c'$ is $O$-linear. A lemma on integral matrices shows that $\tau_{D'}$ is balanced. Fix the index $i_0 = 1$ and put
$$e = E_{i_0 i_0}, \qquad f = S^{-1},$$
where $E_{i_0 i_0}$ is the matrix unit. Let $\mathrm{inc}$ be the inclusion of $B_Q$ as the factor $i_0$, $\mathrm{pr} = \mathrm{pr}_{i_0}$, and let $\xi, \xi_p$ be the inclusion and the projection of $Y_Q$ at $i_0$, transported by $x$. Then clause 1 of a factor holds. A lemma on factors of tensors gives the isomorphism $w$ of clause 3 with the formula for $\tau_Q$, and a lemma on lattices of factors gives clause 2. For algebraicity, $f^* = f$ because $S$ is symmetric, and $e^* f e = S^{-1} E^{T}_{i_0 i_0} S S^{-1} E_{i_0 i_0} = S^{-1} E_{i_0 i_0}$. So $e^* f e = e^* f^* e$, and $S \cdot e^* f e = e$. Also $e^* e = S^{-1} E_{i_0 i_0} S E_{i_0 i_0} = S_{i_0 i_0} \, e^* f e$, and $S_{i_0 i_0} > 0$ because $S$ is positive definite. $\square$

**Theorem 9.9.6 (Canonical Mumford family).** Let $R$ be a CN domain and $Q$ positive Mumford data over $R$ with monomial periods $t^\beta$, where $t_1, \dots, t_m \ne 0$ and the $\beta_i$ are symmetric, $\beta_i(y, y) \ge 0$, and for each $y \ne 0$ some $\beta_i(y, y) > 0$. Then there are a commutative group scheme $G$ over $R$ and a line bundle $P$ on $G \times_R G$ such that $(Q, G, P)$ is a Mumford polarization and $P$ is canonical for $Q$ over $D(\prod_i t_i)$.

Lean: `GlobalTheory.Mum.exists_canonOn_of_isMonomialTau` (also `GlobalTheory.T.exists_canonical_mumford_family_monomial_periods`, a wrapper).

*Proof.* Let $W_8$ be the integer $8 \times 8$ matrix with $W_8 + W_8^{T} = E_8$. The $E_8$ form is positive definite with determinant $1$. A lemma on tensor data gives degeneration data $D'$ over $R$ with maps $\mathrm{pr}_i$, $x$ and $w$ as in the previous theorem, for $W = W_8$ and $r = 8$. The previous theorem gives a factor $F$ of $D'$ with Mumford model $Q$. A lemma on tensor powers gives forms $\beta'$ such that $D'$ has monomial trivializations in $t$; in particular each $\psi_{D'}(y)$ is a unit over $D(\prod_i t_i)$. As $R$ is a CN domain of characteristic $0$, a lemma on complete normal bases gives a semi-abelian group $G'$ with a uniformization $U'$ by $D'$ and some $A'$. A lemma on ring actions extends the action of $O$ on $D'$ to Rosati compatible actions on $A'$ and $G'$ for which $U'$ is $O$-linear. Since $\mathrm{act}(e)$ is an idempotent homomorphism, a lemma on images of idempotents gives a semi-abelian group $G$ with $\mathrm{inc}$, $\mathrm{pr}$ as in the definition of a canonical bundle. Let
$$P = (\mathrm{inc} \times \mathrm{act}(f)\,\mathrm{inc})^* \Lambda(L_{U'}).$$
Then $P$ is canonical for $Q$ over $D(\prod_i t_i)$, with the identity as the isomorphism of clause 3. A lemma on canonical families shows that $P$ is birigidified, and a second lemma shows that $(G, P)$ is uniformized after each finite refinement. So $(Q, G, P)$ is a Mumford polarization. $\square$

**Theorem 9.9.7 (Mumford family of a chart).** Let $n \ge 3$ be odd and let $C$ be a tautological chart of genus $g$ and level $n$ for $\varphi$, with ring $R$, elements $t_1, \dots, t_m$, data $Q$ and forms $\delta_k$ on $Y_Q$, the pullbacks of the $\varepsilon_k$ along $e$. Then there are a commutative group scheme $G_1$ over $R$ and a line bundle $P$ on $G_1 \times_R G_1$ such that $(Q, G_1, P)$ is a Mumford polarization, $P$ is canonical for $Q$ over $D(\prod_k t_k)$, a prime $\mathfrak{p}$ lies in the abelian locus of $G_1$ if and only if $\prod_k t_k \notin \mathfrak{p}$, and $G_1$ has rational $n$-torsion.

Lean: `GlobalTheory.TChart.Taut.exists_family` (also `GlobalTheory.T.exists_mumford_family`, a wrapper).

*Proof.* A lemma on tautological charts shows that $R$ is a regular local ring of characteristic $0$ and that $b_C$ is injective. A regular local ring is an integrally closed domain, and $R$ is noetherian and complete, so $R$ is a CN domain. A second lemma shows that $Q$ has monomial periods $t^{n\delta}$, that the $\delta_k$ are a cone for $\varphi$, that for each $y \ne 0$ some $\delta_k(y, y) > 0$, and that each $t_k \ne 0$. So the forms $n\delta_k$ are symmetric with $n\delta_k(y, y) \ge 0$, and for each $y \ne 0$ some $n\delta_k(y, y) > 0$. As $t_k \in \mathfrak{m}_R$, $Q$ is positive. The previous theorem gives $G_1$ and $P$. Each $n\delta_k$ is nonzero, as $\varepsilon$ is a basis, and a lemma on monomial periods then gives the abelian locus. For the torsion, $\zeta_n$ is a primitive $n$th root of unity, so $b_C(\zeta_n)$ is a primitive $n$th root of unity in $R$. The abelian scheme $B_Q$ is a group pullback of a Siegel datum of level $n$, so it has rational $n$-torsion, and a lemma on canonical families gives rational $n$-torsion for $G_1$. $\square$

**Remark 9.9.8 (Formalization).** The theorem `Taut.exists_family` assumes that $n$ is odd but does not use it ([ExistsMumfordFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMumfordFamily.lean#L56)). In `exists_canonOn_of_isMonomialTau` the instance `IsCommMonObj` on the image group is bound to the name `cutoffSecondDeriv` ([ExistsCanonicalMumfordFamilyMonomialPeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCanonicalMumfordFamilyMonomialPeriods.lean#L41)). The factor in `nonempty_of_tens` is always taken at the first index `⟨0, hr⟩`, which is why $r \ge 1$ is assumed ([NonemptyOfTensorDataPosDefUnimodular.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NonemptyOfTensorDataPosDefUnimodular.lean#L139)); the algebraicity is `PowLim.alg_idem_binv` with $b = S_{i_0 i_0}$ and $g = S$ ([AlgIdemBinv.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AlgIdemBinv.lean#L336)). The tensor combination `LinComb Q.M.L (tensφ pr) (tensε W)` and the predicates `IsBiRig`, `Refines`, `PsiUnitOn` and `IsGrpPullback` are not unfolded here. The lemmas on tensor data, tensor powers, complete normal bases, ring actions, images of idempotents, canonical families and monomial periods have no entries in this part; we use only their statements.
