---
title: The log Kodaira-Spencer isomorphism
decls:
  - GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts
  - GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan
  - GlobalTheory.T.logKodairaSpencer_iso_smooth_snc_toroidalModel
  - GlobalTheory.LogKSAssembly.hasLogKS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The log Kodaira-Spencer isomorphism

This section proves the logarithmic Kodaira-Spencer isomorphism of Section 1 on a smooth model with a strict normal crossings boundary and rigid charts. Section 1 uses the result in the proof of [the toroidal compactification for a fan](/entry/toroidal-for-fan-ks/), and it adds the isomorphism to the output of [the theorem on rigid charts for a fan](/entry/rigid-for-fan-holds/). The argument is linear algebra over the ring of an affine open. The log derivations and the balanced matrices are finite projective modules with the same fibre ranks. The Kodaira-Spencer matrix gives a linear map from the first module to the second, and a map of this type is an isomorphism if it is injective modulo each maximal ideal. Injectivity modulo a maximal ideal is the part that uses the rigid charts. We use the notation of Section 1. In particular, $Y$ is a model of $X_F$ over $\mathrm{id}_F$ with semi-abelian datum $t$, group $G \to Y$ and line bundle $L$ on $G$, and $j(X_F)$ is the open subset of $Y$ where $G$ is abelian.

We first define the Kodaira-Spencer matrix of Section 1. The line bundle $L$ comes with a cover of $G$ by opens $G_\alpha$ on which $L$ is trivial, and with transition functions $g_{\alpha\beta}$, which are units on $G_\alpha \cap G_\beta$. A *vector field* on an open $W$ of $G$ is a family of maps $\Gamma(W', \mathcal{O}_G) \to \Gamma(W', \mathcal{O}_G)$ for opens $W' \subseteq W$ that are additive, satisfy the Leibniz rule and commute with restriction. Let $U$ be an affine open of $Y$ and $v_1, \dots, v_n$ tangent vectors of $G$ along $U$, that is, points of $G$ over $\operatorname{Spec} \Gamma(U)[\varepsilon]$ that lie over the constant map to $U$ and reduce to the zero section modulo $\varepsilon$. Let $\varphi : \Gamma(U) \to A$ be a ring map and $g_0$ a point of $G$ over $\operatorname{Spec} A$ that lies over $\operatorname{Spec} \varphi$. The *translate* of $v_a$ by $g_0$ is the point $w_a = g_0 \cdot \varphi(v_a)$ of $G$ over $\operatorname{Spec} A[\varepsilon]$, the product in the group $G$ of the constant point $g_0$ and the pullback of $v_a$ along $\varphi$. For a function $f$ near $g_0$, write $\partial_{w} f$ for the $\varepsilon$-part of $w^* f$.

**Definition 7.16.1 (Kodaira-Spencer matrix).** Let $V$ be an open subset of $Y$, $U$ an affine open, $v_1, \dots, v_n$ tangent vectors of $G$ along $U$, $D : \Gamma(U) \to \Gamma(U)$ a map and $\Theta$ an $n \times n$ matrix over $\Gamma(U)$. Then $\Theta$ is a *Kodaira-Spencer matrix* of $D$ along $V$ if there are opens $W_i$ of $G$ and vector fields $d_i$ on $W_i$, for $i$ in an index set, such that:

1. the $W_i$ cover the preimage of $U \cap V$ in $G$, and each $W_i$ lies in some $G_{\alpha(i)}$;
2. each $d_i$ lifts $D$: $d_i$ of the pullback of $r \in \Gamma(U)$ is the pullback of $D r$;
3. for $i, i'$, an open $O \subseteq W_i \cap W_{i'}$, a function $f$ on $O$, a ring map $\varphi : \Gamma(U) \to A$, a point $g_0$ of $G$ over $\operatorname{Spec} A$ that lies over $\operatorname{Spec} \varphi$ and lands in $O$, and the translates $w_a$ of $v_a$ by $g_0$, we have
$$g_0^*(d_i f - d_{i'} f) = \sum_{a, b} \varphi(\Theta_{ab})\, \bigl(\partial_{w_b} g_{\alpha(i)\alpha(i')}\bigr)\, g_0^* g_{\alpha(i)\alpha(i')}^{-1}\, \partial_{w_a} f.$$

Lean: `GlobalTheory.LogKS.IsKS` (also `GlobalTheory.LogKS.IsField`, `GlobalTheory.LogKS.IsTranslate`).

The factor in the middle is the derivative of $\log g_{\alpha(i)\alpha(i')}$ along $w_b$. So item 3 says that the differences $d_i - d_{i'}$ are given by $\Theta$ and the logarithmic derivatives of the transition functions. This is a Čech form of the Kodaira-Spencer class of $D$. The zero map has the zero matrix as a Kodaira-Spencer matrix.

**Lemma 7.16.2 (Isomorphism from a relation).** Let $A$ be a ring, $M$ a finite projective $A$-module and $N$ a submodule of the $n \times n$ matrices over $A$ that is finite projective. Let $K$ be a relation between elements $D$ of $M$ and matrices $\Theta$ such that:

1. each $D$ has a matrix $\Theta$ with $K(D, \Theta)$, and it is unique;
2. if $K(D, \Theta)$ and $K(D', \Theta')$, then $K(D + D', \Theta + \Theta')$ and $K(r D, r \Theta)$ for $r \in A$;
3. if $K(D, \Theta)$, then $\Theta \in N$;
4. for each maximal ideal $\mathfrak{m}$, the fibres $M / \mathfrak{m} M$ and $N / \mathfrak{m} N$ have the same dimension over $A / \mathfrak{m}$;
5. if $K(D, \Theta)$ and all entries of $\Theta$ lie in a maximal ideal $\mathfrak{m}$, then $D \in \mathfrak{m} M$.

Then there is a linear isomorphism $e : M \to N$ such that $K(D, \Theta)$ holds if and only if $\Theta = e(D)$.

Lean: `GlobalTheory.LogKSAssembly.exists_equiv` (also `GlobalTheory.ProjBij.bijective_of_injective_mod_maximal`).

*Proof.* By item 1 there is a map $f : M \to N$ with $K(D, f(D))$ for each $D$, and $f(D) \in N$ by item 3. By items 1 and 2, $f(D + D')$ and $f(D) + f(D')$ both satisfy the relation with $D + D'$, so they are equal, and in the same way $f(r D) = r f(D)$. So $f$ is linear. Let $\mathfrak{m}$ be a maximal ideal and suppose $f(D) \in \mathfrak{m} N$. Each entry of an element of $\mathfrak{m} N$ is a sum of products of an element of $\mathfrak{m}$ and an entry of a matrix, so the entries of $f(D)$ lie in $\mathfrak{m}$. By item 5, $D \in \mathfrak{m} M$. So $f$ is injective modulo each maximal ideal. A lemma on finite projective modules states that a linear map between finite projective modules with equal fibre dimensions at each maximal ideal, which is injective modulo each maximal ideal, is bijective. With item 4 it applies to $f$. Let $e$ be the isomorphism $f$. If $K(D, \Theta)$, then $\Theta = e(D)$ by uniqueness. If $\Theta = e(D)$, then $K(D, \Theta)$ by the choice of $f$. $\square$

**Theorem 7.16.3 (Log Kodaira-Spencer isomorphism on a smooth model).** Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, and let $Y$ be a model of $X_F$ over $\mathrm{id}_F$. Suppose that $Y_F$ is smooth over $F$ of relative dimension $n_D$, that $\partial Y_F$ is a strict normal crossings divisor, and that each closed point of $\partial Y_F$ has a rigid chart. Then the datum of $Y$ has the logarithmic Kodaira-Spencer isomorphism along $j(X_F)$.

Lean: `GlobalTheory.LogKSAssembly.hasLogKS` (also `GlobalTheory.T.logKodairaSpencer_iso_smooth_snc_toroidalModel`, a second name).

*Proof.* Let $U$ be an affine open of $Y$, let $v_1, \dots, v_n$ be a basis of the tangent vectors of $G$ along $U$, and let $A(a)$ be the matrices of the action of $a \in \mathcal{O}_E$ in this basis. We apply the previous lemma with $M = \operatorname{Der}^{\log}(U)$, $N$ the module of balanced matrices for $A$, and $K(D, \Theta)$ the condition that $\Theta$ is a Kodaira-Spencer matrix of $D$ along $j(X_F)$. The inputs are the following lemmas, each for this $U$ and this basis.

1. A lemma on log derivations of a smooth model with a strict normal crossings boundary gives that $\operatorname{Der}^{\log}(U)$ is finite projective with fibre dimension $n_D$ at each maximal ideal.
2. A lemma on balanced matrices gives that $N$ is finite projective with fibre dimension $n_D$ at each maximal ideal. With step 1, this gives item 4 of the lemma.
3. A lemma on framed affine opens gives a Kodaira-Spencer matrix for each $D \in \operatorname{Der}^{\log}(U)$.
4. A uniqueness lemma on models gives that two Kodaira-Spencer matrices of the same $D$ are equal. With step 3, this gives item 1 of the lemma.
5. A linearity lemma gives item 2. It uses only the basis and the matrices $A(a)$, and none of the hypotheses on $Y$.
6. A lemma on Kodaira-Spencer classes gives that each Kodaira-Spencer matrix is balanced. This is item 3 of the lemma.
7. [The theorem on injectivity modulo a maximal ideal](/entry/log-kodaira-spencer-injective-mod-maximal-ideal/) gives item 5 of the lemma.

The previous lemma now gives the isomorphism $e : \operatorname{Der}^{\log}(U) \to N$ with the property of Section 1. $\square$

The rigid charts enter in steps 3, 4, 6 and 7. Steps 1 and 2 use only smoothness, the boundary and $p + q \ge 1$.

**Theorem 7.16.4 (Log Kodaira-Spencer isomorphism from rigid charts).** Suppose that the statement of [the theorem on rigid charts for a fan](/entry/rigid-for-fan-holds/) holds. Then the statement of [the toroidal compactification for a fan](/entry/toroidal-for-fan-ks/) holds.

Lean: `GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan` (also `GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts`, a second name).

*Proof.* Let $E$, $H$, $D$, $\varphi$, $l$, $X$ and $F$ be as in Section 1. The hypothesis gives a model $Y$ of $X_F$ over $\mathrm{id}_F$, an effective Cartier divisor $B$ and integers $d, k \ge 1$ with conditions 1 to 5. We keep $Y$, $B$, $d$, $k$ and conditions 1 to 4. Condition 1 says that $Y_F$ is smooth over $F$ of relative dimension $n_D$ and that $\partial Y_F$ is a strict normal crossings divisor, and condition 5 gives a rigid chart at each closed point of $\partial Y_F$. With $p + q \ge 1$, these are the hypotheses of the previous theorem, so the datum of $Y$ has the logarithmic Kodaira-Spencer isomorphism along $j(X_F)$. $\square$

**Remark 7.16.5 (Formalization).** The proofs are in [ToroidalFanKodairaSpencerOfRigidBoundaryCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalFanKodairaSpencerOfRigidBoundaryCharts.lean#L16) and [LogKodairaSpencerIsoSmoothSncToroidalModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerIsoSmoothSncToroidalModel.lean#L57). The `T.*` names are wrappers, at line 16 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The definitions `IsField`, `IsTranslate`, `IsKS` and `HasLogKS` are in [DenseInterior.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/DenseInterior.lean#L76), at lines 16, 55, 76 and 99. In `IsKS` the map $D$ is any function $\Gamma(U) \to \Gamma(U)$, not a derivation; `HasLogKS` applies it to log derivations only. The tangent vectors $v_a$ in `IsKS` are not asked to be a basis, but `HasLogKS` asks it through `IsTanAtG` and the unique combinations `IsCombAtG`. We have not unfolded `IsCombAtG`. The zero case is `isKS_zero` (line 92). In `toroidalForFanKS_of_rigidForFan` the proof destructures the output of `RigidForFan` into eight parts and replaces only the last one, the rigid charts, by the conclusion of `hasLogKS` (line 19). The step from an element of $\mathfrak{m} N$ to entries in $\mathfrak{m}$ is `entry_mem_of_mem_smul_top` (line 25). Both fibre dimensions in steps 1 and 2 are `Dw.dim`, and item 4 is their composite `(hLr m hm).trans (hBr m hm).symm` (line 68). The lemma of step 1, `GlobalTheory.LogDerProj.main`, is in [IsLocalizedModuleRes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsLocalizedModuleRes.lean#L58), a file whose name does not match its content. The linearity lemma `LogKSLin.isKS_linear` (TranslateUnique.lean, line 319) is the only input that takes none of $p + q \ge 1$, smoothness, the boundary condition or the rigid charts. The proof applies `ProjBij.bijective_of_injective_mod_maximal`, `LogDerProj.main`, `T.symmetric_balanced_tensors_finite_projective_rank_dim`, `T.exists_kodairaSpencer_regular_framed_affine`, `KSUniq.isKS_unique_model`, `LogKSLin.isKS_linear` and `LogKSBal.ksClass_mem_balanced`. They have no entries in this chapter, and we use only their statements. The lemma `T.logKodairaSpencer_injective_mod_maximalIdeal` is proved in a later part of this chapter.
