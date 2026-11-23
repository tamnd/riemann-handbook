---
title: Čech cocycles on abelian schemes
decls:
  - GlobalTheory.CechFibre.exists_dlog_add_coboundary_mod
  - GlobalTheory.T.cechCocycle_eq_coboundary_add_logDerivatives_mod
  - GlobalTheory.CechH1Span.exists_dlog_add_coboundary
  - GlobalTheory.T.cechCocycle_eq_coboundary_add_logDerivatives_affine
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Čech cocycles on abelian schemes

This section describes the first cohomology of the structure sheaf of an abelian scheme over an affine base in Čech terms. Each Čech $1$-cocycle on an affine cover is a coboundary plus a combination of the logarithmic derivatives of the transition functions of the polarization, taken along the invariant vector fields. We prove this first modulo a maximal ideal of the base, and then exactly. This is how Kodaira-Spencer matrices in the sense of Section 16 are found. The differences of local lifts of a derivation give a cocycle, and the theorem writes it in the form of item 3 of the definition of a Kodaira-Spencer matrix. The result enters step 3 of [the log Kodaira-Spencer isomorphism on a smooth model](/entry/has-log-ks/), the existence of Kodaira-Spencer matrices on framed affine opens.

We fix the data. Let $E$ and $H$ be as in Section 1, $X$ a scheme and $t$ a semi-abelian datum on $X$, with group $G \to X$ and line bundle $L$ on $G$. The bundle $L$ comes with a cover of $G$ by opens $G_\alpha$ on which it is trivial, and with transition functions $g_{\alpha\beta}$ on $G_\alpha \cap G_\beta$, as in Section 16. We make three assumptions.

1. The map $G \to X$ is proper. So $G$ is an abelian scheme over $X$.
2. The bundle $L$ is relatively ample in the following sense. For each affine open $V$ of $X$ there are $N \ge 1$ and sections $s_0, \dots, s_M$ of $L^N$ on $G_V$ such that the loci $s_i \neq 0$ are affine and cover $G_V$, and on each locus $s_i \neq 0$ the quotients $s_j / s_i$ generate the ring of functions as a $\Gamma(V)$-algebra.
3. Let $R$ be a ring, $\operatorname{Spec} R \to X$ a map and $x$ a point of $G$ over $\operatorname{Spec} R$. Suppose that the bundle $\mu^* L \otimes \mathrm{pr}^* L^{-1}$ on $G_R$, where $\mu(s) = x + s$, is trivial locally over $\operatorname{Spec} R$. Then $x = 0$.

Condition 3 says that the polarization map $x \mapsto t_x^* L \otimes L^{-1}$ has trivial kernel.

Let $U$ be an affine open of $X$ and $v_1, \dots, v_n$ tangent vectors of $G$ along $U$ such that each tangent vector is a unique $\Gamma(U)$-linear combination of them. For each $a$ let $\delta_a$ be a vector field on $G_U$, in the sense of Section 16, with these properties: $\delta_a$ kills the functions pulled back from $U$, and for each translate $w$ of $v_a$ by a point $g_0$, as in Section 16, the value of $\delta_a f$ at $g_0$ is $\partial_w f$. So $\delta_a$ is the invariant vector field of $v_a$. Let $(W_i)_{i \in J}$ be a cover of $G_U$ by affine opens, with each $W_i$ in some $G_{\alpha(i)}$. Write $g_{ii'}$ for $g_{\alpha(i)\alpha(i')}$ on $W_i \cap W_{i'}$, and put
$$\kappa_{b, ii'} = \delta_b(g_{ii'})\, g_{ii'}^{-1}.$$
A *cocycle* is a family $c = (c_{ii'})$ of functions on $W_i \cap W_{i'}$ with $c_{ii'} + c_{i'i''} = c_{ii''}$ on triple intersections.

**Theorem 7.25.1 (Čech cocycles modulo a maximal ideal).** Let the data be as above, let $\mathfrak{m}$ be a maximal ideal of $\Gamma(U)$ and $c$ a cocycle. Then there are $\theta_1, \dots, \theta_n \in \Gamma(U)$, functions $h_i$ on $W_i$, elements $r_1, \dots, r_N \in \mathfrak{m}$ and cocycles $e_1, \dots, e_N$ such that for all $i, i'$
$$c_{ii'} = h_i - h_{i'} + \sum_b \theta_b\, \kappa_{b, ii'} + \sum_k r_k\, e_{k, ii'}.$$

Lean: `GlobalTheory.CechFibre.exists_dlog_add_coboundary_mod` (also `GlobalTheory.T.cechCocycle_eq_coboundary_add_logDerivatives_mod`, a second name).

*Proof.* Let $x_0 : \operatorname{Spec} \Gamma(U)/\mathfrak{m} \to X$ be the closed point of $\mathfrak{m}$, and let $G_0$ be the pullback of $G$ along $x_0$. It is an abelian variety over the field $\Gamma(U)/\mathfrak{m}$.

1. A lemma on the closed fibre uses all the assumptions above. It gives $\theta_1, \dots, \theta_n \in \Gamma(U)$ and functions $h'_i$ on the opens $W_i \cap G_0$ such that the restriction of $c$ to $G_0$ equals $h'_i - h'_{i'} + \sum_b \theta_b\, \kappa_{b, ii'}$ there.
2. Each $\kappa_b$ is a cocycle. The $g_{ii'}$ satisfy $g_{ii'} g_{i'i''} = g_{ii''}$, and $\delta_b$ is a derivation, so $\delta_b(g)\, g^{-1}$ turns products into sums.
3. Put $c^0 = c - \sum_b \theta_b\, \kappa_b$. It is a cocycle by step 2. By step 1 its restriction to $G_0$ is a coboundary.
4. A lemma on cocycles uses that $G$ is proper over $X$ and that the $W_i$ are affine. It states the following. A cocycle whose restriction to $G_0$ is a coboundary is of the form $h_i - h_{i'} + \sum_k r_k\, e_{k, ii'}$ with $r_k \in \mathfrak{m}$ and cocycles $e_k$. We apply it to $c^0$.

Steps 3 and 4 give the identity of the theorem. $\square$

Step 4 is a form of the base change for the first cohomology of $\mathcal{O}_G$. Step 1 is the statement on one abelian variety.

**Theorem 7.25.2 (Čech cocycles on an affine base).** Let the data be as above and let $c$ be a cocycle. Then there are $\theta_1, \dots, \theta_n \in \Gamma(U)$ and functions $h_i$ on $W_i$ such that for all $i, i'$
$$c_{ii'} = h_i - h_{i'} + \sum_b \theta_b\, \kappa_{b, ii'}.$$

Lean: `GlobalTheory.CechH1Span.exists_dlog_add_coboundary` (also `GlobalTheory.T.cechCocycle_eq_coboundary_add_logDerivatives_affine`, a second name).

*Proof.* Let $Z$ be the set of cocycles. It is a $\Gamma(U)$-module, where $\Gamma(U)$ acts through the pullback of functions to $G_U$. Let $S$ be the submodule of $Z$ spanned by the coboundaries $(h_i - h_{i'})$ and the cocycles $\kappa_1, \dots, \kappa_n$. We show that $Z / S = 0$.

1. A lemma on finite generation uses that $G$ is proper over $X$, that $L$ is relatively ample and that the $W_i$ are affine. It gives cocycles $e_1, \dots, e_N$ such that each cocycle is a coboundary plus a $\Gamma(U)$-linear combination of the $e_k$. So the classes of the $e_k$ generate $Z / S$, and $Z / S$ is a finite $\Gamma(U)$-module.
2. Let $\mathfrak{m}$ be a maximal ideal and $z \in Z$. The previous theorem writes $z$ as an element of $S$ plus $\sum_k r_k\, e'_k$ with $r_k \in \mathfrak{m}$ and cocycles $e'_k$. So the class of $z$ lies in $\mathfrak{m}(Z / S)$. Thus $Z / S = \mathfrak{m}(Z / S)$ for each maximal ideal $\mathfrak{m}$.
3. A finite module $M$ with $M = \mathfrak{m} M$ for each maximal ideal $\mathfrak{m}$ is zero, by the lemma of Nakayama applied at each maximal ideal. So $Z / S = 0$.

Thus $c \in S$. An element of $S$ is a coboundary plus $\sum_b \theta_b\, \kappa_b$ for some $\theta_b \in \Gamma(U)$, since the coboundaries form a submodule. $\square$

We read the theorem as follows. The space $H^1(G_U, \mathcal{O})$ is the Lie algebra of the dual abelian scheme. The class of $\kappa_b$ is the image of $v_b$ under the tangent map of the polarization. The theorem says that these classes generate $H^1(G_U, \mathcal{O})$, which uses condition 3. This reading is ours; the formal proof does not state it.

**Remark 7.25.3 (Formalization).** The proofs are in [CechCocycleEqCoboundaryAddLogDerivativesMod.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CechCocycleEqCoboundaryAddLogDerivativesMod.lean#L20) and [CechCocycleEqCoboundaryAddLogDerivativesAffine.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CechCocycleEqCoboundaryAddLogDerivativesAffine.lean#L22). The `T.*` names are wrappers, at line 10 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. Both files have a helper `resG_appLE` (line 11 and line 13) on restrictions of pulled back functions. Conditions 2 and 3 are `Out.RelAmple` and `Out.KTriv` in [NonzeroLocus.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/NonzeroLocus.lean#L33), lines 33 and 53. The bundle of condition 3 is `translDiff`. In the first proof, $x_0$ is defined at line 23, step 1 is `T.closedFibre_cechCocycle_in_tangentSpan` (line 26), step 2 is `T.cech_cocycle_condition_log_derivative_transition` (line 32), step 4 is `T.cechCocycle_mem_coboundary_add_maximal_smul` (line 42), and the last identity is a `linear_combination` (line 47). Only the lemma of step 1 takes conditions 2 and 3 and the fields $\delta_a$; the lemma of step 4 takes none of them. In the second proof, step 1 is `T.cech_h1_finite_generation_affine` (line 70), step 3 is `GlobalTheory.submodule_eq_top_of_sup_maximal_smul_eq_top` (line 91) applied to the zero submodule, the call of the first theorem is at line 96, and $\theta$ and $h$ are read off at lines 125 to 126. These lemmas have no entries in this chapter, and we use only their statements. The second theorem is used in `CechCocycleVerticalFieldsEqCoboundaryAddLogDeriv.lean` (line 51) and `BasisTangentModuleLocalizedAbelianLocus.lean` (line 252), on the way to step 3 of the theorem in Section 16. In the statements the index set $J$ is arbitrary, and the map $i \mapsto \alpha(i)$ is part of the data.
