---
title: The period identity from the family conditions
decls:
  - GlobalTheory.MiTop.miStar2_of_bot_lev_fam_served_puNZ
  - GlobalTheory.T.mi_star2_of_pu_nz
  - GlobalTheory.MiTop.miStar2_at_realisation_alt
  - GlobalTheory.T.joint_star_product_nonvanishing_alt
  - GlobalTheory.MiTop.botRel_of_pin_of_mem_center
  - GlobalTheory.T.botRel_of_botHyp_of_pin_central
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The period identity from the family conditions

This section proves [the Theorem on the period identity from the family conditions](/entry/mi-star2-of-pu-nz/), which is step 4 of the proof in [the section on the period identity for a true package](/entry/mi-star2-of-all-true-alt-alt/). Its input is the conditions $\mathrm{FAC}(W)$ of [the Theorem on family conditions](/entry/fam-all-q-of-all-true-alt/), proved in sections 4 to 15, together with the served condition and the nonzero projection. Its output is the period identity $\mathrm{MI}^*_2$ of [the section on rows](/entry/fam-mi-star-row-alt-alt/). The proof has three layers. The family conditions and the served condition give a joint condition: one central pin $z$ and, for each word, a bottom datum pinned at $z$ with a unitary change of coordinates. A pinned bottom datum satisfies a bottom relation, which turns a linear relation between periods into the same relation between pairings. The bottom relation and the joint condition then give the period datum.

We keep the notation of [the section on the family conditions](/entry/mi-star2-of-all-true-alt-alt/). $W$ is a real package over $D$, $u$ a word, $M_u$ the space of row vectors of $u$ with its norm, $t$ a twist index and $\mu_0$ the base one. $x_u$ is the base point of $u$, $t_S$ the translation element of $W$ and $J_W, \chi_W$ the level set and its character. For a bottom datum $d$, $d.\mathrm{per}(\varphi, T, y, v)$ is its period map, at a row vector $\varphi$, a row form $T$ in the base row space of $W$, a point $y$ and a vector $v$. A *column form* of $\varphi$ is a cusp form $C$ attached to $\varphi$ by the column dictionary, and a *pairing* of a row form $T(v)$ at $g$ with $C$ is a number $b$ given by the pairing of the evaluation of $T(v)$ at $g$ with $C$.

**Definition 4.16.1 (Joint condition).** $W$ satisfies the *joint condition* if there is $z \in G_f(Y_0)$, central in $G(Y_0)$, such that for each word $u$ there are a bottom datum $d$ pinned at $z$, a linear map $U$ of $M_u$, a real $r > 0$ with $\|U\varphi\| = r\|\varphi\|$ for all $\varphi$, and unit coefficients $c$, with $d.\mathrm{Rel}(U, c)$. Here $c$ is a family of *unit coefficients* if $c_t \neq 0$ for all $t$ and $v(w, k) = 0$ whenever $c_{\mu(w)} / c_{\mu_0}$ is the image of $k$, and $d.\mathrm{Rel}(U, c)$ says that for each $T$ in the base row space there is $p$ with $c_t \, \mathrm{per}_{\mathrm{col}}(\varphi, t, F) \, d.\mathrm{per}(\varphi', T, y, v)$ equal to $p(\varphi')$ times the period of $U \varphi$ at the row form of $F$, for all $\varphi, \varphi', t, F, y, v$.

**Definition 4.16.2 (Bottom relation).** Let $z \in G(Y_0)$ and let $d$ be a bottom datum for $u$. The *bottom relation* for $(z, d)$ says: there is a linear isometry $R$ of $M_u$ such that for all $\varphi, \varphi'$, all $T, T'$ in the base row space and all $\alpha, \alpha' \in \mathbb C$ with

$$\alpha \, d.\mathrm{per}(\varphi, T, y, v) + \alpha' \, d.\mathrm{per}(\varphi', T', y, v) = 0 \quad \text{for all } y, v,$$

and for all column forms $C$ of $R\varphi$ and $C'$ of $R\varphi'$ and pairings $b$ of $T(v)$ and $b'$ of $T'(v)$ at $z t_S$ with $C$ and $C'$, we have $\alpha b + \alpha' b' = 0$.

**Theorem 4.16.3 (Bottom relation from a central pin).** Assume the rapid decay of cusp forms. Let $W$ satisfy the bottom hypotheses, let $z \in G_f(Y_0)$ be central in $G(Y_0)$, and let $d$ be a bottom datum for $u$ pinned at $z$. Then the bottom relation holds for $(z, d)$.

Lean: `GlobalTheory.MiTop.botRel_of_pin_of_mem_center` (also `GlobalTheory.T.botRel_of_botHyp_of_pin_central`, a second name).

*Proof.* We write both the periods and the pairings through one Bessel period, and move the relation from the first to the second.

1. A result of another chapter on the bottom hypotheses gives the infinity type $\theta$, the standard character $\psi$, the matching of $z t_S$ with $(J_W, \chi_W)$ for central $z \in G_f(Y_0)$, and that the character of the level of $\mathcal B = d.\mathcal B$ does not vanish.
2. A result of another chapter on pins gives the isometry $R$: the column forms of $R\varphi$ are the right translates by $t_S$ of the column forms of $\varphi$.
3. A result of another chapter on the column dictionary gives a family $\xi(y)$ of column scalars, whose span is the whole space, such that the column scalar form at $\xi(y)$ is the trace column form.
4. A result of another chapter on Poincaré series and Bessel periods gives a weight $c$ such that each pairing of a row form at $z t_S$ with a column form is the integral over the real points of $c$ times the Bessel period of the column form against the row form translated by $x_u^{-1} z t_S$.
5. *Periods through the Bessel period.* Let $C$ be a column form of $R\varphi$. Then for all $y, v$,
   $$\begin{aligned} d.\mathrm{per}(\varphi, T, y, v) &= \chi_W(d.k) \cdot \mathcal P_{\mathcal B}(C, \xi(y), \tau T(v)), \\ \tau &= x_u^{-1} z t_S, \end{aligned}$$
   where $\mathcal P_{\mathcal B}$ is the Bessel period of the level of $\mathcal B$ and $\tau$ acts by right translation. The proof writes out the pin $\iota_{\mathcal B}(a_0 a) b = x_u z t_S k$, moves the central factor $a$ through, and uses the character of $k \in J_W$.
6. Insert step 5 in the relation. The factor $\chi_W(d.k)$ is common, and it is nonzero by step 1. So $\alpha \mathcal P_{\mathcal B}(C, \xi(y), \tau T(v)) + \alpha' \mathcal P_{\mathcal B}(C', \xi(y), \tau T'(v)) = 0$ for all $y$ and $v$.
7. Both terms are linear in the column scalar. Since the $\xi(y)$ span, the relation of step 6 holds for every column scalar $\xi'$ in place of $\xi(y)$.
8. A real translation acts on the base row space as a linear map $\sigma_y$. The evaluation of $T(v)$ at a translate by $y$ is then the right translate by $\tau$ of $T(\sigma_y v)$. This uses that $z t_S$ has trivial real part, which comes from the matching of step 1.
9. By step 4 and the rapid decay of cusp forms, $b$ and $b'$ are integrals of $c$ against the Bessel periods of step 7, at the vectors $\sigma_y v$. The integrand of $\alpha b + \alpha' b'$ vanishes at every $y$ by steps 7 and 8, so $\alpha b + \alpha' b' = 0$. $\square$

**Theorem 4.16.4 (Period identity at a realisation).** Assume the classification of discrete series and the rapid decay of cusp forms. Let $W$ satisfy the bottom hypotheses, assume that every theta vector $\Theta_t(j_R(e_V(t, F)))$ lies in the level part of the coefficient space, that $W$ satisfies the joint condition, and that $D$ has nonzero projection. Then $\mathrm{MI}^*_2$ holds for the coefficient space of $W$.

Lean: `GlobalTheory.MiTop.miStar2_at_realisation_alt` (also `GlobalTheory.T.joint_star_product_nonvanishing_alt`, a second name).

*Proof.* We build the period datum from the joint condition.

1. The joint condition gives $z$ and, for each $u$, $d_u$, $U_u$, $r_u$ and $c_u$.
2. A result of another chapter on central shifts gives a linear map $V_0$ of the coefficient space from $z$: this is the map $V$ of the period datum.
3. From the classification of discrete series, a result of another chapter gives a conjugate vector $v$ of the real representation at level zero. A second result gives $\kappa \neq 0$ such that the pairing form at $v$ is $\kappa$ times the inner product.
4. A result of another chapter on the real package gives the column coordinates: a bijection of coordinate vectors with $M_u$ that is a multiple of an isometry.
5. A result of another chapter on conjugate vectors, using the nonzero projection, gives for each $u$ a row vector $\varphi_1$, a column form $C_0$ of $\varphi_1$ and a pairing $b_0 \neq 0$ of a row form $T_0$ at $z t_S$ with $C_0$.
6. *Anchor.* Fix $u$, and let $R$ be the isometry of the Theorem on bottom relations for $(z, d_u)$. Since $\|U\varphi\| = r\|\varphi\|$ with $r > 0$, $U$ is injective, hence onto, so $R U \varphi_0 = \varphi_1$ for some $\varphi_0$. The relation $d.\mathrm{Rel}(U, c)$ at $T_0$ gives $p$. Feeding the relation into the bottom relation gives $p(\varphi_0) \neq 0$, and for all $t, \varphi, F$ and all pairings $b$ with a column form of $R U \varphi$,
   $$c_t \, \mathrm{per}_{\mathrm{col}}(\varphi, t, F) \, b_0 = p(\varphi_0) \, b.$$
7. Put $A = r^{-1} R U$. It preserves the norm. Through the bijection of step 4 and the conjugation $\mathrm{cj}$ of the twist, $A$ becomes a unitary matrix $U'_u$. Put $c'_t = \mathrm{cj}(c_t)$, $p' = \mathrm{cj}(p(\varphi_0))$ and $b' = \mathrm{cj}(\kappa r^{-1} b_0)$. These are nonzero, and the unit condition on $c$ passes to $c'$ since the embedding of $k$ is $\mathrm{cj}$ of the embedding into $\mathbb C$.
8. Step 6, read through step 3, is the identity of the period datum at $u$ with the constants $c'$, $p'$ and $b'$. Every member of the coefficient space comes from a word, so this holds for all members.
9. A result of another chapter collects anchored data of this form into a unitary period datum with $a_u \neq 0$. $\square$

**Theorem 4.16.5 (Period identity from the family conditions).** Assume the classification of discrete series, the rapid decay of cusp forms and the Harish-Chandra modules. Let $W$ satisfy the bottom hypotheses, the level hypothesis, the conditions $\mathrm{FAC}(W)$ and the served condition, and let $D$ have nonzero projection. Then $\mathrm{MI}^*_2$ holds for the coefficient space of $W$.

Lean: `GlobalTheory.MiTop.miStar2_of_bot_lev_fam_served_puNZ` (also `GlobalTheory.T.mi_star2_of_pu_nz`, a second name).

*Proof.* A result of another chapter on descent gives, from the bottom hypotheses and the level hypothesis, that every theta vector $\Theta_t(j_R(e_V(t, F)))$ lies in the level part. A second result gives the joint condition from $\mathrm{FAC}(W)$ and the served condition, with the rapid decay of cusp forms and the Harish-Chandra modules. The Theorem on the period identity at a realisation finishes the proof. $\square$

The pin $z$ is chosen once for all words in [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/). This is what makes $V_0$ in step 2 independent of $u$, and so the map $V$ of the period datum is one map.

**Remark 4.16.6 (Formalization).** The theorems are at [MiStar2OfFamilies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamilies.lean#L23), [MiStar2AtRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2AtRealisation.lean#L84) and [BotRelTwo.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BotRelTwo.lean#L32). The second names are relays at [MiStar2OfFamiliesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamiliesStatement.lean#L20), [MiStar2AtRealisationStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2AtRealisationStatement.lean#L19) and [BotRelTwoStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BotRelTwoStatement.lean#L18). The joint condition is `JointCondition` and the bottom relation `BottomRelation` in [FormsAtZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FormsAtZero.lean#L67). Some details:

- The name `joint_star_product_nonvanishing_alt` speaks of a nonvanishing product, but the statement is the period identity at a realisation, with the joint condition as a hypothesis.
- In BotRelTwo.lean the classification of discrete series is a hypothesis of the bottom relation theorem but is bound as `_` at line 33 and not used. Lines 27 to 29 open and close an empty namespace `MiTop.BotTwo`.
- Step 5 of the first proof is the local claim `L1` at lines 49 to 79; the central factor is moved at line 61. Step 6 cancels the character at line 89, step 7 is at lines 91 to 111, and the integral is closed by `comb_integral` at line 133.
- The anchor of step 6 of the second proof is the lemma `anchor_word_alt` at line 48 of MiStar2AtRealisation.lean. The helpers `dc_heq_alt`, `df1_fc_eq_side3` and `exists_word_heq_of_mem_dc` (lines 36 to 40) identify the members of the coefficient space with words, through casts of dependent types. Lines 31 to 33 open and close an empty `section Gen`.
- In the anchor lemma, the first two parts of the conjugate vector data of step 5 are discarded with `-`.
- We have not opened `exists_isShift_of_center_alt`, `exists_conjVec`, `pairForm_of_conjVec_of_botHyp`, `conjugate_vector_central_twist_alt`, `miStar2_of_anchored`, `descent_eV_mem_level_alt` and `joint_of_famAllQ_of_servedQ`, nor the results of steps 2 to 4 of the first proof.
