---
title: Translates
decls:
  - GlobalTheory.MiTop.exists_isAt_alt
  - GlobalTheory.T.exists_central_stab_of_transport_correction
  - GlobalTheory.LevZero.StabMatch.exists_center_stab_at_of_transport_correction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Translates

This section proves [the Theorem on translates](/entry/exists-is-at-alt/), which [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/) uses in its first step. The theorem says that a Bessel datum that is placed and framed has a translate. A translate is a pair $(a_0, a)$ with $a_0$ a transport adelic correction and $a$ a central element of $G_f(X_0)$, such that the translation element matches the level set of the package with its character. The correction $a_0$ comes from the transport data of the package and needs no choice. The central element $a$ is the real work. We build it place by place and glue the local elements with a central glueing result. Then we compare the stabiliser of a frame with the level set of the row side, and the matching follows.

We keep the notation of [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/). $W$ is a real package over $D$ with the level set $J_W$ and its character $\chi_W$. The row side has the level set $J_{\mathrm{row}}$ with the character $\chi_{\mathrm{row}}$ and the compact open subgroup $K_2$. For a word $u$ the base point is $x_u$, and for a family character $f$ for $u$ the base point of $f$ is $b_0 = f.g.b_0$. For $a_0, a \in G(X_0)$ the translation element is $\tau = \tau_{f, \mathcal B}(a_0, a) = x_u^{-1} \iota_{\mathcal B}(a_0 a) b_0$.

**Definition 4.11.1 (Frame at a translate).** The package gives a self-dual lattice $\Lambda_Y$ of $Y_0$ with a frame $\beta_Y$. For $g \in G_f(Y_0)$ write $\mathrm{St}(\beta)$ for the stabiliser of a frame $\beta$ in the finite adelic points, and $g_f$ for the finite part of $g$. The *frame at the translate* $(a_0, a)$ is $\beta_\tau = \tau_f \cdot \beta_Y$.

**Definition 4.11.2 (Stabiliser condition).** The pair $(a_0, a)$ satisfies the *stabiliser condition* for $(f, \mathcal B)$ if for every $\kappa \in G(Y_0)$,

$$\bigl(\kappa \in G_f(Y_0) \text{ and } \kappa_f \in \mathrm{St}(\beta_\tau)\bigr) \iff \kappa \in J_{\mathrm{row}}.$$

Here $\kappa \in J_{\mathrm{row}}$ means that the image of $\kappa$ in the row group has trivial first component and second component in $K_2$. So the condition says that the stabiliser of the frame at the translate is the level set of the row side.

**Theorem 4.11.3 (Central stabiliser from a transport correction).** Let $W$ satisfy the package hypotheses. Let $u$ be a word, $f$ a family character for $u$ and $\mathcal B$ a Bessel datum for $u$ that is placed for $f$ and framed. Let $a_0$ be a transport adelic correction for $u$. Then there is $a \in G_f(X_0)$, central in $G(X_0)$, such that $(a_0, a)$ satisfies the stabiliser condition for $(f, \mathcal B)$.

Lean: `GlobalTheory.LevZero.StabMatch.exists_center_stab_at_of_transport_correction` (also `GlobalTheory.T.exists_central_stab_of_transport_correction`, a second name).

*Proof.* The proof makes the lattice $\tau_f \Lambda_Y$ equal, at each finite place, to the lattice of the row side, up to a central factor.

1. A placed datum satisfies the local bottom compatibility. So $\mathcal B$ has the level of the row side and is adapted to the standard character $\psi$. The framing gives $\mu$ and $\lambda = \pm g$ as in the definition of a framed datum.
2. The bottom hypotheses of $W$ give $0 + 2 r_S + 2 = m$, the identity condition, and the second hypothesis at $u$. With these, a result of another chapter on images of lattices gives a self-dual lattice $L_m$ of $Y_0$ and the moves of $b_0$: at each finite place, $b_0$ carries $\Lambda_Y$ to $L_m$.
3. Fix a finite place $p$. We find a central element $a_p$ of the local group at $p$ and a scalar $c_p$ of norm one, with $c_p \bar c_p = 1$ and $c_p - 1$ in the level ideal at $p$, such that $c_p \tau_p$ carries $L_m$ to the lattice of the row side at $p$. There are three cases.
   - If $p$ is a type place, so $p$ lies over a place of $P_g$, the level of $\mathcal B$ at $p$ is given by a uniformizer, and we read $a_p$ off the valuation of that uniformizer.
   - If $p$ is a twist place, so $p$ divides $T_u$, the glued cores of the row side are homothetic at $p$. The trace condition of $\mathcal B$ and the chain level at $p$ show that the column level keeps the row lattice. The Witt core embedding stabilises the lattice exactly when the core does. This gives $a_p$.
   - Otherwise the orthogonal sum of the cores is homothetic to the lattice off the level, and the self-dual lattice splits off the line of the unit norm vector at $p$. This gives $a_p$.
4. A result of another chapter glues local homotheties. From the data $(a_p, c_p)$ at all finite places it gives $a \in G_f(X_0)$, central in $G(X_0)$, and a central $z$ such that $z \cdot \iota_{\mathcal B}(a)$ moves $L_m$ to the lattice of the row side at every place.
5. Then $\tau_f$ carries $\Lambda_Y$ to the lattice of the row side, so $\beta_\tau$ is a frame of that lattice. The stabiliser of such a frame is the set of $\kappa \in G_f(Y_0)$ whose image has trivial first component and second component in $K_2$. This is the stabiliser condition. $\square$

The framing enters only in step 1. It fixes the shape of the vectors $i_0 v_{\mathcal B}$ and $e(k, a)$, and so the shape of the frame of $\mathcal B$.

**Theorem 4.11.4 (Translates).** Let $W$ satisfy the package hypotheses. Let $u$ be a word, $f$ a family character for $u$ and $\mathcal B$ a Bessel datum for $u$ that is placed for $f$ and framed. Then there are $a_0$ and $a$ such that $(a_0, a)$ is a translate for $(f, \mathcal B)$.

Lean: `GlobalTheory.MiTop.exists_isAt_alt`.

*Proof.* We take $a_0$ from the transport data and $a$ from the previous theorem. Then we check that $\tau$ matches.

1. The transport data of $W$ at $u$ give a transport adelic correction $a_0$: an element of $G_f(X_0)$ whose finite part is the first entry of the transport datum.
2. The previous theorem gives $a \in G_f(X_0)$, central, such that $(a_0, a)$ satisfies the stabiliser condition. So the first two conditions of a translate hold.
3. Results of another chapter describe the central elements adapted to the frame. Let $\kappa \in G_f(Y_0)$ with $\kappa_f \in \mathrm{St}(\beta_\tau)$. Then $\kappa \in J_{\mathrm{row}}$ exactly when the tuple of $\kappa$ lies in the group $H$ of the level data at zero. For such $\kappa$, $\chi_{\mathrm{row}}(\kappa)$ is the first extension of the character of the level data.
4. The base point $b_0$ lies in $G_f(Y_0)$, by the first clauses of the placed data. The base point $x_u$ lies in $G_f(Y_0)$, since its image in the row group has first component $1$. So $\tau \in G_f(Y_0)$.
5. The rank of $Y_0$ is at most $r$. Conjugation by $\tau$ carries the level group of the frame $\beta_Y$ to the level group of $\beta_\tau = \tau_f \beta_Y$.
6. The level data at zero have one block, with no shift and no extra places. So for $k \in G(Y_0)$, $k$ lies in $J_W$ exactly when $k \in G_f(Y_0)$ and $k_f$ lies in the level group of $\beta_Y$ with its tuple in $H$, and $\chi_W(k)$ is the first extension of the character at that tuple.
7. Put $\kappa = \tau k \tau^{-1}$. By step 5, $k_f$ lies in the level group of $\beta_Y$ exactly when $\kappa_f$ lies in the level group of $\beta_\tau$. By step 2, this gives the first clause of the stabiliser condition at $\kappa$. Steps 3 and 6 then give $k \in J_W \iff \kappa \in J_{\mathrm{row}}$ and $\chi_{\mathrm{row}}(\kappa) = \chi_W(k)$.

So $\tau$ matches $(J_W, \chi_W)$, and $(a_0, a)$ is a translate. $\square$

The previous theorem is the only place where the placed and framed data are used in a nontrivial way. The rest of the proof is a comparison of two level sets through conjugation by $\tau$.

**Remark 4.11.5 (Formalization).** The theorem on translates is at [ExistsIsAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAt.lean#L32). Step 1 is the call at line 34 and step 2 the call at line 35. Step 5 is the lemma at line 51 and step 6 is the lemma at line 54, applied at line 55 with the two hypotheses on the level data (no shift, no extra places) closed by `rfl`. The final assembly is at lines 61 to 65. The central stabiliser theorem is at [StabMatch.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StabMatch.lean#L33), with the glueing at line 106 and the stabiliser at line 109. Its second name is a relay at [StabMatchStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StabMatchStatement.lean#L24). The stabiliser condition is `StabiliserCondition` and the frame at a translate is `frameAtTranslate`, both in [PlacedBy.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacedBy.lean#L51). The framing hypothesis is used only to build the frame of $\mathcal B$ (step 1). The name `exists_center_stab_at_of_transport_correction` says "stab at", but the conclusion is the stabiliser condition for the frame at the translate, not a stabiliser at one place. We have not opened the three local lemmas of step 3, the glueing lemma `exists_central_glue_localHomotheties`, or the two results on adapted central elements of step 3 of the second proof (`central_adapted_element_property_alt` in MemRowJIffRTupStatement.lean and `central_adapted_element_value_alt` in RowCharacterEqExtensionStatement.lean).
