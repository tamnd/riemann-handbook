---
title: Injectivity modulo a maximal ideal
decls:
  - GlobalTheory.ChartDer.logKS_inj_mod_boundary
  - GlobalTheory.T.logKodairaSpencer_injective_mod_maximal_boundary
  - GlobalTheory.logKS_inj_mod_maximal
  - GlobalTheory.T.logKodairaSpencer_injective_mod_maximalIdeal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Injectivity modulo a maximal ideal

This section proves item 5 of the lemma in Section 16. Let $D$ be a log derivation on an affine open $U$ of a model, and suppose that its Kodaira-Spencer matrix has all entries in a maximal ideal $\mathfrak{m}$. Then $D$ lies in $\mathfrak{m}$ times the module of log derivations. This is the step of [the log Kodaira-Spencer isomorphism on a smooth model](/entry/has-log-ks/) that uses the rigid charts. The proof splits by the position of the point of $\mathfrak{m}$. At a point of the abelian locus it is the injectivity of the classical Kodaira-Spencer map. At a boundary point we move to a rigid chart. There, Section 23 shows that the degeneration data are constant along the tangent vector of $D$ at the closed point, and the rigidity gives that this tangent vector is zero. The rigid charts come from [the theorem on rigid charts for a fan](/entry/rigid-for-fan-holds/).

We use the notation of Sections 1 and 16. Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, and let $Y$ be a model of $X_F$ over $\mathrm{id}_F$, with semi-abelian datum $t_Y$, group $G \to Y$ and abelian locus $j(X_F)$. Suppose that $Y_F$ is smooth over $F$ of relative dimension $n_D$, that $\partial Y_F$ is a strict normal crossings divisor, and that each closed point of $\partial Y_F$ has a rigid chart. Let $U$ be an affine open of $Y$, let $v_1, \dots, v_n$ be a basis of the tangent vectors of $G$ along $U$, and let $A(a)$ be the matrices of the action of $a \in \mathcal{O}_E$ in this basis. Write $\operatorname{Der}^{\log}(U)$ for the module of log derivations of $\Gamma(U)$, that is, the derivations that preserve the ideal of the complement of $j(X_F)$.

For a field $k$ and a derivation $\delta$ of the chart ring $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$, let $\rho_\delta : R \to k[\varepsilon]$ be the map $\rho_\delta(r) = r(0) + \varepsilon\, (\delta r)(0)$. It is a ring map: the Leibniz rule gives $(\delta(rs))(0) = r(0)\, (\delta s)(0) + s(0)\, (\delta r)(0)$. It is the tangent vector of $\delta$ at the closed point. Its reduction modulo $\varepsilon$ is $r \mapsto r(0)$, which kills $\mathfrak{m}_R$.

**Theorem 7.24.1 (Injectivity modulo a maximal ideal at the boundary).** Let the data be as above. Let $D \in \operatorname{Der}^{\log}(U)$, let $\Theta$ be a Kodaira-Spencer matrix of $D$ along $j(X_F)$, and let $\mathfrak{m}$ be a maximal ideal of $\Gamma(U)$ that contains all entries of $\Theta$. Suppose that there is a point $x \in U$ off $j(X_F)$ at which each element of $\mathfrak{m}$ vanishes. Then $D \in \mathfrak{m} \operatorname{Der}^{\log}(U)$.

Lean: `GlobalTheory.ChartDer.logKS_inj_mod_boundary` (also `GlobalTheory.T.logKodairaSpencer_injective_mod_maximal_boundary`, a second name).

*Proof.* We pass to a rigid chart at a closed point over $x$.

1. A lemma on boundary points uses the smoothness of $Y_F$. It gives a closed point $x'$ of $\partial Y_F$ that maps to $x$.
2. By hypothesis $x'$ has a rigid chart. This gives a field $k$, the chart ring $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$, a map $\xi : \operatorname{Spec} R \to Y_F$ that sends the closed point to $x'$, and data $t$, $P$ and $\gamma_1, \dots, \gamma_m$ with conditions 1 to 3 of a fan chart and the rigidity. The $\gamma_i$ are part of a basis of the forms.
3. The closed point of $\operatorname{Spec} R$ maps into $U$. Each open subset of a local scheme that contains the closed point is the whole scheme. So $\xi$ maps $\operatorname{Spec} R$ into $U$.
4. A lemma on log derivations of charts uses condition 1 of a fan chart. It gives a derivation $D_R$ of $R$ with $D_R(\xi^* r) = \xi^*(D r)$ for $r \in \Gamma(U)$ and $D_R(u_i) \in (u_i)$ for each $i$. We choose $a_i \in R$ with $D_R(u_i) = a_i u_i$.
5. Let $\rho = \rho_{D_R}$. [The theorem on constant data at a boundary point](/entry/degeneration-constant-of-log-kodaira-spencer-mem/) of Section 23 applies. It gives a rational $c_0 \neq 0$ such that $(t, P)$ is constant along $\rho$ with rates $c_0\, a_i(0)$.
6. The reduction of $\rho$ modulo $\varepsilon$ kills $\mathfrak{m}_R$. Since $u_i(0) = 0$, we have $\rho(u_i) = u_i(0) + \varepsilon\, a_i(0)\, u_i(0) = 0$. So the rigidity of the chart applies to $\rho$ and the rates of step 5. It gives that the $\varepsilon$-part of $\rho(r)$ is zero for each $r$, that is, $(D_R r)(0) = 0$ for each $r \in R$.
7. The field $k$ has characteristic $0$, since $F$ maps into $k$ by the constant coefficient of $\xi$. The $\gamma_i$ are linearly independent, since they are part of a basis.
8. A lemma on constant points uses that $P$ is monomial in the $u_i$ with exponents $\gamma_i$, that the $\gamma_i$ are symmetric and linearly independent, and that the $u_i$ lie in $\mathfrak{m}_R$. It states the following. If $\rho$ has no $\varepsilon$-part and $(t, P)$ is constant along $\rho$ with rates $b$, then $b = 0$. With step 6 it gives $c_0\, a_i(0) = 0$. Since $c_0 \neq 0$, we get $a_i(0) = 0$ for each $i$.
9. A lemma on log vector fields uses smoothness, the normal crossings condition and conditions 1 and 2 of a fan chart. It states the following. If $D_R$ lifts $D$, $(D_R r)(0) = 0$ for each $r \in R$, and $a_i(0) = 0$ for each $i$, then $D \in \mathfrak{m} \operatorname{Der}^{\log}(U)$. Steps 6 and 8 give its hypotheses. $\square$

We give the idea of the last step. On the chart, the log derivations form a free module with basis $u_i \partial/\partial u_i$ and $\partial/\partial v_j$. In this basis $D_R$ has the coordinates $a_i$ and $D_R(v_j)$. Steps 6 and 8 say that all these coordinates lie in $\mathfrak{m}_R$. The stalk map of $\xi$ is an étale completion, so this condition on the chart gives the condition on $U$ at $x$.

**Theorem 7.24.2 (Injectivity modulo a maximal ideal).** Let the data be as above. Let $D \in \operatorname{Der}^{\log}(U)$, let $\Theta$ be a Kodaira-Spencer matrix of $D$ along $j(X_F)$, and let $\mathfrak{m}$ be a maximal ideal of $\Gamma(U)$ that contains all entries of $\Theta$. Then $D \in \mathfrak{m} \operatorname{Der}^{\log}(U)$.

Lean: `GlobalTheory.logKS_inj_mod_maximal` (also `GlobalTheory.T.logKodairaSpencer_injective_mod_maximalIdeal`, a second name).

*Proof.* The isomorphism $\operatorname{Spec} \Gamma(U) \cong U$ sends the prime $\mathfrak{m}$ to a point $x \in U$. Each element of $\mathfrak{m}$ lies in the prime of $x$, so it vanishes at $x$. There are two cases.

1. Suppose that $x \in j(X_F)$. Over $j(X_F)$ the scheme $G$ is abelian. A lemma on interior points gives $D \in \mathfrak{m} \operatorname{Der}^{\log}(U)$. It takes the hypotheses of the theorem and the point $x$.
2. Suppose that $x \notin j(X_F)$. Then the previous theorem applies with this $x$, and it gives $D \in \mathfrak{m} \operatorname{Der}^{\log}(U)$. $\square$

In the first case the statement is the injectivity of the Kodaira-Spencer map of an abelian scheme modulo a maximal ideal. There $\operatorname{Der}^{\log}(U)$ is the module of all derivations near $x$. This is the classical part. In the second case the boundary enters, and the log structure and the rigid charts are needed.

**Remark 7.24.3 (Formalization).** The proofs are in [LogKodairaSpencerInjectiveModMaximalBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalBoundary.lean#L47) and [LogKodairaSpencerInjectiveModMaximalIdeal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalIdeal.lean#L31). The `T.*` names are wrappers, at line 16 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The map $\rho_\delta$ is `GlobalTheory.ChartDer.constEps` (line 29 of the first file), with `constEps_apply` (line 37) and `residue_eq_zero_iff_constantCoeff` (line 42). The rigid chart is `GlobalTheory.RigChart.HasRigidChart`, not the definition of the same short name in the namespace `GlobalTheory.LogKSChart`. In the first proof, step 1 is `T.exists_closedBoundaryPoint_maximalIdeal` (line 50), step 3 is `top_le_preimage_of_closedPoint` (line 58), step 4 is `ChartDer.logDer_extend_chartRing` (line 59), step 5 is at line 77, step 6 is at lines 81 to 88, step 8 is `ConstPointCone.dir_eq_zero_of_const` (line 97) and step 9 is `T.logVectorField_mem_maxIdeal_smul_of_vanishing` (line 105). In the second proof, the point $x$ comes from `exists_point_vanishing_of_isMaximal` (line 19 of the second file), the case split is at line 35, and the lemma of step 1 is `T.kodairaSpencer_injective_closed_interior_point` (line 36). The lemmas without links have no entries in this chapter, and we use only their statements. The explanation after the first proof is not a reading of the proof of step 9. The name of the interior lemma says "closed", but its hypotheses do not ask that $x$ is a closed point. The boundary case is called through `first | exact key hb hKS hΘ | exact key hKS hΘ` (lines 40 to 42). This fallback accepts two forms of the lemma; the first form matches the statement file. In the first proof, the hypothesis $p + q \ge 1$ and the matrices $A(a)$ go only to the theorem of step 5, which does not use them.
