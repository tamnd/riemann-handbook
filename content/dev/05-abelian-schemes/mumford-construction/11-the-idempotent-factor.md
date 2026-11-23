---
title: The idempotent factor
decls:
  - GlobalTheory.Mum.TraitTwist.exists_bundle_data_at_traits
  - GlobalTheory.T.semiabelian_uniformization_linear_action_descent
  - GlobalTheory.Mum.FactorTrait.factor_unif_at_trait
  - GlobalTheory.T.semiabelian_uniformization_linear_action_transfer
  - GlobalTheory.Mum.factor_unif
  - GlobalTheory.T.idempotentFactor_uniformised_of_degData_factor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The idempotent factor

This section proves the last geometric step of [Mumford's construction](/entry/has-of-base/). Let $D$ be an algebraic factor of realised data $D'$, and let $G$ be the image of the idempotent $[e]$ on the semi-abelian scheme $G'$ that realises $D'$. Then, after a finite extension of the base, a group pullback of $G$ is uniformised by a pullback of $D$, and the Mumford bundle of its line bundle is the restriction of the Mumford bundle of $G'$. Since a group pullback of a semi-abelian scheme is semi-abelian, $D$ is then realised after a finite extension, and the Galois descent of [the next section](/entry/has-of-has-fin/) finishes the proof.

The proof has three steps. [The section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/) gives a line bundle $P$ on a group pullback of $G$ that is even on the torus. Such a line bundle gives degeneration data, but not the data $D$: it gives data with the same polarisation as a pullback of $D$. [The theorem on data with the same polarisation](/entry/same-pol-unif-fin-ext/) replaces these data by a pullback of $D$. Finally, a uniformisation at one complete discrete valuation ring spreads out to the base after a finite extension.

We work in the factor situation of [the section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/): a base $R$, data $D$ and $D'$, a factor $F$ of $D'$ onto $D$ with elements $e, f$, a uniformisation $U'$ of $(A', G')$ by $D'$ with line bundle $L'$ that is linear for actions of the ring of $F$, and a semi-abelian $G$ with $i : G \to G'$ and $p : G' \to G$, $p \circ i = 1$, $i \circ p = [e]$. We put $\Lambda_F = (i \times [f] \circ i)^* \Lambda(L')$. A *trait* over a base $R_0$ is a complete discrete valuation ring $W$ of characteristic $0$ with an injective local map $\varphi : R_0 \to W$.

We use two facts on uniformisations, which this chapter takes as inputs.

(U1) Let $R_0$ be an admissible base, $G_0$ a commutative semi-abelian scheme over $R_0$ and $U_0$ a uniformisation of $(A_0, G_0)$ by data $D_0$. Then the line bundle of $U_0$ is a cubical symmetric line bundle that is even on the torus.

(U2) Conversely, let $G_0$ be semi-abelian over a base $R_0$, $P$ a cubical symmetric line bundle on $G_0$ that is even on the torus, and $\gamma_0 : (G_0)_{K_0} \to A_0$ an isomorphism of group schemes with a polarised abelian variety, with $\gamma_0^* L_{A_0} \cong P|_{(G_0)_{K_0}}$. Then there are data $D_0$ and a uniformisation of $(A_0, G_0)$ by $D_0$ with line bundle $P$.

**Theorem 4.11.1 (Data for the factor).** In the factor situation, let $\rho_9 : R \to R_9$ be a finite extension, $\beta_9 : G_9 \to G$ a group pullback along $\rho_9$ with a square $\beta_{92}$, $P_9$ a cubical symmetric line bundle on $G_9$, $A_9$ a polarised abelian variety over the fraction field $K_9$ of $R_9$, and $\gamma_9 : (G_9)_{K_9} \to A_9$ an isomorphism of group schemes. Assume that $G_9$ is semi-abelian, that $\Lambda(P_9) \cong \beta_{92}^* \Lambda_F$, that $P_9$ is even on the torus, and that $\gamma_9^* L_{A_9} \cong P_9|_{(G_9)_{K_9}}$, all by generating isomorphisms. Then there are a finite extension $\rho_0 : R \to R_0$, a pullback $D_0$ of $D$ along $\rho_0$, a group pullback $\beta_0 : G_0 \to G$ along $\rho_0$ with a square $\beta_{02}$, a cubical symmetric line bundle $P$ on $G_0$, a polarised abelian variety $A_0$ over $K_0$ and an isomorphism of group schemes $\gamma_0 : (G_0)_{K_0} \to A_0$, with these properties:

1. $G_0$ is semi-abelian, $\Lambda(P) \cong \beta_{02}^* \Lambda_F$, $P$ is even on the torus, and $\gamma_0^* L_{A_0} \cong P|_{(G_0)_{K_0}}$;
2. for every trait $\varphi : R_0 \to W$, every group pullback $\beta : G_W \to G_0$ along $\varphi$, all data $D_W$ over $W$ and every uniformisation $U_W$ of $(A_W, G_W)$ by $D_W$ with $L_{U_W} \cong \beta^* P$, the data $D_W$ are a pullback of $D_0$ along $\varphi$.

Lean: `GlobalTheory.Mum.TraitTwist.exists_bundle_data_at_traits` (also `GlobalTheory.T.semiabelian_uniformization_linear_action_descent`, a second name).

*Proof.* The ring $R_9$ is an admissible base, and it has characteristic $0$ since $\rho_9$ is injective; so $R_9$ is a base. By (U2) there are data $D_9'$ and a uniformisation $U_9$ of $(A_9, G_9)$ by $D_9'$ with line bundle $P_9$.

We compare $D_9'$ with $D$, using one more input: there is a pullback $D_9$ of $D$ along $\rho_9$ with the same polarisation as $D_9'$. The idea is the condition $\Lambda(P_9) \cong \beta_{92}^* \Lambda_F$: the factor identifies $\Lambda(L)$ with the restriction of $\Lambda(L')$ along $(i, [f] i)$, with the matching values of $\tau$, so the Mumford bundle and the periods of $D_9'$ agree with those of the pullback of $D$.

[The theorem on data with the same polarisation](/entry/same-pol-unif-fin-ext/), applied to $D_9$, $D_9'$ and $U_9$, gives a finite extension $\rho : R_9 \to R_0$, a pullback $D_0$ of $D_9$ along $\rho$, a group pullback $\beta : G_0 \to G_9$ along $\rho$ with a square $\beta_2$, and a uniformisation $U_0$ of $(A_0, G_0)$ by $D_0$ with $\Lambda(L_{U_0}) \cong \beta_2^* \Lambda(P_9)$. As a group pullback of a semi-abelian scheme, $G_0$ is semi-abelian. By (U1), $P = L_{U_0}$ is cubical symmetric and even on the torus, and we take for $\gamma_0$ the generic isomorphism of $U_0$, which respects the polarisation bundles.

Put $\rho_0 = \rho \circ \rho_9$, $\beta_0 = \beta_9 \circ \beta$ and $\beta_{02} = \beta_{92} \circ \beta_2$. The composite of finite extensions is a finite extension, and $D_0$ is a pullback of $D$ along $\rho_0$ as a pullback of a pullback. A composite of group pullbacks is a group pullback and a composite of squares is a square. Then
$$\begin{aligned} \Lambda(P) &= \Lambda(L_{U_0}) \cong \beta_2^* \Lambda(P_9) \\ &\cong \beta_2^* \beta_{92}^* \Lambda_F = \beta_{02}^* \Lambda_F. \end{aligned}$$
This proves property 1.

For property 2, we use the uniqueness of data under base change to a trait. Let $R_0$ be an admissible base, $G_0$ semi-abelian with a uniformisation $U_0$ by $D_0$, $\varphi : R_0 \to W$ a trait, and $U_W$ a uniformisation of a group pullback $G_W$ of $G_0$ along $\varphi$ by data $D_W$, with $L_{U_W} \cong \beta^* L_{U_0}$. Then $D_W$ is a pullback of $D_0$ along $\varphi$. Since $P = L_{U_0}$, this is property 2. $\square$

The trait property says that the data $D_0$ are determined by the pair $(G_0, P)$ after every base change to a trait. It is the form in which the next theorem passes the data to a trait.

**Theorem 4.11.2 (The factor at a trait).** In the factor situation, assume that the factor $F$ is algebraic. Then there are:

1. a finite extension $\rho_0 : R \to R_0$, a pullback $D_0$ of $D$ along $\rho_0$, a semi-abelian group pullback $\beta_0 : G_0 \to G$ along $\rho_0$ with a square $\beta_{02}$, and a cubical symmetric line bundle $P$ on $G_0$ with $\Lambda(P) \cong \beta_{02}^* \Lambda_F$;
2. a trait $\varphi : R_0 \to W$, a group pullback $\beta : G_W \to G_0$ along $\varphi$, a pullback $D_W$ of $D_0$ along $\varphi$, a polarised abelian variety $A_W$ over the fraction field of $W$, and a uniformisation $U_W$ of $(A_W, G_W)$ by $D_W$ with $L_{U_W} \cong \beta^* P$.

Lean: `GlobalTheory.Mum.FactorTrait.factor_unif_at_trait` (also `GlobalTheory.T.semiabelian_uniformization_linear_action_transfer`, a second name).

*Proof.* Since $F$ is algebraic, [the theorem on even cubical structures](/entry/exists-fin-ext-cp-factor-even/) gives the hypotheses of the previous theorem. The previous theorem gives $\rho_0$, $D_0$, $\beta_0$, $\beta_{02}$, $P$, $A_0$ and $\gamma_0$ with properties 1 and 2. The ring $R_0$ is a base. By (U2) there are data $D''$ and a uniformisation $U''$ of $(A_0, G_0)$ by $D''$ with line bundle $P$.

Now we choose a trait. There is a complete discrete valuation ring $W$ of characteristic $0$ with an injective local map $\varphi : R_0 \to W$. The base change of $U''$ along $\varphi$ is a uniformisation $U_W$ of $(A_W, G_W)$ by a pullback $D_W$ of $D''$, where $G_W = G_0 \otimes_{R_0} W$ with its projection $\beta$, a group pullback, and $L_{U_W} \cong \beta^* P$. Property 2 of the previous theorem shows that $D_W$ is a pullback of $D_0$ along $\varphi$. $\square$

**Theorem 4.11.3 (The idempotent factor).** In the factor situation, assume that the factor $F$ is algebraic. Then there are a finite extension $\rho : R \to R_1$, a pullback $D_1$ of $D$ along $\rho$, a group scheme $G_1$ over $R_1$ with a morphism $\beta : G_1 \to G$ that makes it the group pullback of $G$ along $\rho$, a square $\beta_2$ over $\beta$, a polarised abelian variety $A_1$ over the fraction field of $R_1$ and a uniformisation $U_1$ of $(A_1, G_1)$ by $D_1$, with a generating isomorphism
$$\Lambda(L_{U_1}) \cong \beta_2^* \Lambda_F.$$

Lean: `GlobalTheory.Mum.factor_unif` (also `GlobalTheory.T.idempotentFactor_uniformised_of_degData_factor`, a second name).

*Proof.* The previous theorem gives $\rho_0 : R \to R_0$, $D_0$, $\beta_0 : G_0 \to G$, $\beta_{02}$, $P$ and a uniformised trait $(W, \varphi, G_W, D_W, U_W)$. The ring $R_0$ is a base.

We spread the uniformisation out from the trait. Let $R_0$ be a base, $D_0$ data over $R_0$, $G_0$ a semi-abelian scheme with a cubical symmetric line bundle $P$, and $(W, \varphi, \beta : G_W \to G_0, D_W, U_W)$ a uniformised trait with $D_W$ a pullback of $D_0$ and $L_{U_W} \cong \beta^* P$. Then there are a finite extension $\rho_1 : R_0 \to R_1$, a pullback $D_1$ of $D_0$ along $\rho_1$, a group pullback $\beta_1 : G_1 \to G_0$ along $\rho_1$, a polarised abelian variety $A_1$ and a uniformisation $U_1$ of $(A_1, G_1)$ by $D_1$ with $L_{U_1} \cong \beta_1^* P$. This is the last input of the section: the passage from a complete discrete valuation ring to the base.

Put $\rho = \rho_1 \circ \rho_0$ and $\beta = \beta_0 \circ \beta_1$. Then $\rho$ is a finite extension, $D_1$ is a pullback of $D$ along $\rho$, and $\beta$ is a group pullback. The group pullback $\beta_1$ has a square $\beta_{12}$ such that $L \cong \beta_1^* M$ implies $\Lambda(L) \cong \beta_{12}^* \Lambda(M)$. With $\beta_2 = \beta_{02} \circ \beta_{12}$,
$$\begin{aligned} \Lambda(L_{U_1}) &\cong \beta_{12}^* \Lambda(P) \\ &\cong \beta_{12}^* \beta_{02}^* \Lambda_F = \beta_2^* \Lambda_F. \end{aligned}$$
$\square$

**Remark 4.11.4 (Formalization).** The second names are wrappers, proved by a `first | exact` tactic. Their names say "linear action", but neither conclusion mentions the action of the ring of the factor; the linearity of $U'$ is only passed on. The first theorem does not assume the factor algebraic; the other two pass the algebraic condition on, and in the last theorem it is used only through the second ([IdempotentFactorUniformisedOfDegDataFactor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentFactorUniformisedOfDegDataFactor.lean#L21)). The inputs are: (U1) `GlobalTheory.Mum.unif_evenOn`; (U2) `GlobalTheory.T.exists_uniformisation_completeLocal_evenOnTorus`, whose clause that the generic isomorphism is $\gamma_0$ is dropped at [SemiabelianUniformizationLinearActionDescent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiabelianUniformizationLinearActionDescent.lean#L29) and at [SemiabelianUniformizationLinearActionTransfer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiabelianUniformizationLinearActionTransfer.lean#L51); the comparison with $D$ is `GlobalTheory.T.uniformisation_pulledBackFactor_samePolarisation`, whose proof we did not open, so the reason given for it above is only a sketch; the uniqueness at a trait is `GlobalTheory.T.uniformization_base_change_complete_dvr`; the trait is chosen by the helper `GlobalTheory.Mum.FactorTrait.exists_trait_of_unif` through `GlobalTheory.PrimeUnif.exists_cdvr`, and the last output of the helper is dropped at line 52; the spreading out is `GlobalTheory.T.exists_finiteExtension_uniformisation_of_trait_unif`, and the squares come from `GlobalTheory.Mum.lbIso_lam_pull_of_isGrpPullback`. None of these is in the outline of this chapter.
