---
title: Algebraization of formal schemes with an ample line bundle
decls:
  - GlobalTheory.CompanionTheory.FormalAlg.tower_sections
  - GlobalTheory.CompanionTheory.FormalAlg.schemes_of_closedProj
  - GlobalTheory.T.formal_algebraisation_schemes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Algebraization of formal schemes with an ample line bundle

This section proves that a formal system of proper schemes with a formal line bundle that is ample on the first member comes from a proper scheme over the complete base ring, with an ample line bundle. The proof embeds the whole system in one projective space by compatible sections, and then applies the existence theorem for closed subschemes of projective space of Section 4. The line bundle on the algebraization is not one of the twists $\mathcal{O}(1)$ directly; it is recovered as a quotient of two roots, from the sections of two consecutive powers. Together with the algebraization of morphisms, which comes from Section 3, this gives the formal algebraization theorem that the [theorem on formal thickenings](/entry/formal-thickening-formal-algebraisation/) states.

We keep the notation of Section 5: $R$ is Noetherian, $I \subseteq R$ an ideal and $R_e = R/I^{e+1}$. For a scheme $X$ over $\operatorname{Spec} R$ let $X_e = X \times_R \operatorname{Spec} R_e$.

**Definition 7.6.1 (Relatively ample line bundle).** Let $Y$ be a scheme over a scheme $S$ and $L$ a line bundle on $Y$. Then $L$ is *relatively ample* if, for each affine open $U \subseteq S$, there are $k \geq 1$ and a very ample family of sections of $L^k$ over the inverse image of $U$ in $Y$.

For $S$ affine, a relatively ample $L$ has a power that defines a closed immersion into a projective space over $S$. This is the [ampleness](/learn/positivity-resolution/#ample-nef-and-big-line-bundles) relative to the base.

**Lemma 7.6.2 (Compatible very ample sections of two consecutive powers).** Let $(Y_e, \beta_e)$ be a formal system of proper schemes and $(N_e, v_e)$ a formal line bundle on it, with $N_0$ relatively ample over $\operatorname{Spec} R_0$. Then there are $n \geq 1$, $p, q \geq 0$, and for each $e$ sections $a_{e,0}, \dots, a_{e,p}$ of $N_e^n$ and $c_{e,0}, \dots, c_{e,q}$ of $N_e^{n+1}$, with these properties.

1. The families $(a_{0,i})$ and $(c_{0,i})$ are very ample on $Y_0$.
2. For each $e$ and $i$, the section $a_{e+1,i}$ maps to $a_{e,i}$, and $c_{e+1,i}$ maps to $c_{e,i}$.

Lean: `GlobalTheory.CompanionTheory.FormalAlg.tower_sections`.

*Proof.* We take as given two facts on very ample families.

1. Since $N_0$ is relatively ample over the affine scheme $\operatorname{Spec} R_0$, there are $d \geq 1$ and very ample families $s$ of sections of $N_0^d$ and $s'$ of sections of $N_0^{d+1}$.
2. Let $s_0, \dots, s_m$ be a very ample family of sections of $L^d$ and $t \geq 1$. Then the monomials $s_{j_1} \cdots s_{j_t}$, for all maps $(j_1, \dots, j_t)$ from $\{1, \dots, t\}$ to $\{0, \dots, m\}$, form a very ample family of sections of $L^{dt}$.

[Theorem 7.5.2](/entry/exists-uniform-lift/) on uniform lifting, applied to $d$ and $s$, gives $t_1$. Applied to $d + 1$ and $s'$, it gives $t_2$. Let $k = \max(t_1, t_2)$ and put
$$t = 1 + (d+1) k, \qquad t' = 1 + d k, \qquad n = d t.$$
Then $t \geq t_1$, $t' \geq t_2$, $t, t' \geq 1$ and $n \geq 1$. The exponents fit: $n + 1 = d + d(d+1)k + 1 = (d+1)(1 + dk) = (d+1) t'$.

Let $(a_{0,i})$ be the monomials of degree $t$ in $s$, indexed by $0, \dots, p$, and let $(c_{0,i})$ be the monomials of degree $t'$ in $s'$, indexed by $0, \dots, q$. These are sections of $N_0^{dt} = N_0^n$ and $N_0^{(d+1)t'} = N_0^{n+1}$. By the second fact both families are very ample. Since $t \geq t_1$, each section of $N_e^n$ lifts to a section of $N_{e+1}^n$ that maps to it, for each $e$. Choose such lifts for each $e$ in turn, by recursion on $e$. This gives the sections $a_{e,i}$ with the second property. The sections $c_{e,i}$ are built in the same way from $t' \geq t_2$. $\square$

**Theorem 7.6.3 (Algebraization of formal schemes).** Assume the existence theorem for closed subschemes of projective space, in the form of [Theorem 7.4.2](/entry/ge-closed-proj/). Let $R$ be Noetherian and $I$-adically complete. Let $(Y_e, \beta_e)$ be a formal system of proper schemes over the rings $R_e$, and let $N_e$ be line bundles on $Y_e$ such that, for each $e$, $N_e$ is isomorphic to $\beta_e^* N_{e+1}$, and $N_0$ is relatively ample over $\operatorname{Spec} R_0$. Then there are a scheme $X$ over $\operatorname{Spec} R$, a line bundle $M$ on $X$ and morphisms $b_e : Y_e \to X$ with these properties.

1. $X$ is proper over $\operatorname{Spec} R$, and $M$ is relatively ample.
2. For each $e$, the square formed by $b_e$, the structure maps and $\operatorname{Spec} R_e \to \operatorname{Spec} R$ is a pullback square, so $Y_e = X_e$.
3. $b_{e+1} \circ \beta_e = b_e$ for each $e$.
4. $N_e \cong b_e^* M$ for each $e$.

Lean: `GlobalTheory.CompanionTheory.FormalAlg.schemes_of_closedProj` (also `GlobalTheory.T.formal_algebraisation_schemes`, a second name).

*Proof.* Choose the isomorphisms $v_e : N_e \cong \beta_e^* N_{e+1}$. Take $n$, $a$ and $c$ from the lemma, and let $D = n(n+1)$. Let $z_e$ be the family of sections of $N_e^D$ formed by the monomials of degree $n+1$ in the $a_{e,i}$ and the monomials of degree $n$ in the $c_{e,i}$. The second fact in the proof of the lemma shows that both parts of $z_0$ are very ample families. We take as given that the union of two very ample families of sections of one line bundle is very ample. So $z_0$ is very ample. The sections $z_{e+1,j}$ map to $z_{e,j}$, since the $a$ and $c$ do. We take as given three inputs.

1. *Compatible system of sections.* Given the existence theorem for closed subschemes of projective space, a formal system of proper schemes with a formal line bundle $L_e$ and compatible sections $z_e$ of $L_e$ that are very ample on $Y_0$ comes from algebraic data. There are $X$ proper over $R$, a line bundle $Q$ on $X$, sections $\zeta_j$ of $Q$ that form a very ample family, morphisms $b_e$ with the pullback squares and the compatibility, and isomorphisms $\omega_e : b_e^* Q \cong L_e$ that send $\zeta_j$ to $z_{e,j}$. A polynomial relation of degree two between the $z_{e,j}$ that holds for each $e$ holds between the $\zeta_j$. If the sets where some of the $z_{0,j}$ do not vanish cover $Y_0$, then the sets where the corresponding $\zeta_j$ do not vanish cover $X$.
2. *Roots from relations.* Let $Q$ be a line bundle on $X$, $k \geq 1$, and $u_w$ sections of $Q$ indexed by the maps $w$ from $\{1, \dots, k\}$ to a finite set $\tau$. Assume that $u_{w_1} u_{w_2} = u_{w_3} u_{w_4}$ whenever the values of $w_1$ and $w_2$ together are the values of $w_3$ and $w_4$ together, counted with multiplicity, and that the sections $u_{(i, \dots, i)}$ for $i \in \tau$ do not vanish together. Then there is a line bundle $A$ on $X$ with $A^{\otimes k} \cong Q$. If $b : Y \to X$ is a morphism with $b^* Q \cong L^D$ such that each $u_w$ goes to the monomial $\prod_l a_{w(l)}$ in sections $a_i$ of $L^{D/k}$, then $b^* A \cong L^{D/k}$.
3. *The difference of two roots.* With $A$ and $C$ the two roots of $Q$ below, the line bundle $C \otimes A^{-1}$ is relatively ample, and its pullbacks are computed from those of $A$ and $C$.

The first input, with $L_e = N_e^D$, gives $X$, $Q$, $\zeta$, $b_e$ and $\omega_e$. This proves the first claim on $X$ and the second and third claims. The diagonal monomials $a_{0,i}^{n+1}$ do not vanish together, since $(a_{0,i})$ is very ample, so the first input shows that the corresponding $\zeta_j$ do not vanish together on $X$. The monomials of degree $n+1$ in the $a_{e,i}$ satisfy the quadratic relations of the second input for each $e$, so the corresponding $\zeta_j$ satisfy them on $X$. The second input with $k = n+1$ gives $A$ with $A^{n+1} \cong Q$ and $b_e^* A \cong N_e^n$. In the same way, from the monomials of degree $n$ in the $c_{e,i}$, the second input with $k = n$ gives $C$ with $C^n \cong Q$ and $b_e^* C \cong N_e^{n+1}$.

Let $M = C \otimes A^{-1}$. It is a line bundle, and the third input shows that it is relatively ample. Last,
$$b_e^* M \cong N_e^{n+1} \otimes N_e^{-n} \cong N_e$$
for each $e$, which is the fourth claim. $\square$

The two consecutive powers are needed because the first input gives a line bundle $Q$ that algebraizes $N_e^D$, not $N_e$. The two roots of $Q$ of orders $n+1$ and $n$ come from the monomial structure of $z$, and their quotient has the pullback $N_e$.

**Remark 7.6.4 (Formalization).** Both results are in [FormalAlgebraisationSchemes.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FormalAlgebraisationSchemes.lean#L32). The statement `FormalAlgebraisation.Schemes` and its partner `FormalAlgebraisation.Morphisms` are in [FormalAlgebraisation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FormalAlgebraisation.lean#L28). The theorem is stated as an implication from `GEClosedProj`; in [Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/Development.lean#L17) it is applied to `T.grothendieck_existence_closed_proj`. The recursion in the lemma is the helper `exists_compatible`, a `Nat.rec`. In the lemma the uniform lifting is called by its second name `T.formal_line_bundle_very_ample_system`. The relative ampleness `RelAmple` is in [NonzeroLocus.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/NonzeroLocus.lean#L33). The name `formal_algebraisation_schemes` is a wrapper that closes with `first | exact ...`.
