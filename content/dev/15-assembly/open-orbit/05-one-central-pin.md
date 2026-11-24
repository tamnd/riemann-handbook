---
title: One central pin
decls:
  - GlobalTheory.T.exists_botDat_of_placedP_framed
  - GlobalTheory.MiTop.exists_botDat_pin_of_placed_of_framed
  - GlobalTheory.T.exists_isAt_of_placed_framed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## One central pin

This section proves step 1 of [the Theorem on family conditions](/entry/fam-all-q-of-all-true-alt/). The pin condition on a bottom datum involves a central element $z$ of $G_f(Y_0)$, and the family conditions ask for one $z$ that works for all words $u$ at once. We find such a $z$ by comparing every placed framed Bessel datum with one fixed datum. The comparison uses two results proved in the second part of the chapter: each placed framed Bessel datum has a translate, and two translates differ by an element of the level set.

We keep the notation of [the previous section](/entry/fam-all-q-of-all-true-alt/). Let $W$ be a real package over $D$. It gives a level set $J_W \subset G(Y_0)$, which is a subgroup, and a character $\chi_W$ on $J_W$. The row side gives a second level set $J_{\mathrm{row}}$, the set of $k \in G(Y_0)$ whose image in the row group has trivial first component and second component in a fixed compact open subgroup $K_2$, with a character $\chi_{\mathrm{row}}$.

**Definition 4.5.1 (Matching element).** An element $t \in G(Y_0)$ *matches* $(J_W, \chi_W)$ if $t \in G_f(Y_0)$ and for each $k \in G(Y_0)$,

$$k \in J_W \iff t k t^{-1} \in J_{\mathrm{row}},$$

and $\chi_{\mathrm{row}}(t k t^{-1}) = \chi_W(k)$ for $k \in J_W$.

So $t$ matches when conjugation by $t$ carries the level set of the package with its character onto the level set of the row side with its character.

**Definition 4.5.2 (Framed Bessel datum).** Let $u$ be a word and $\mathcal{B}$ a Bessel datum on $X_0$ for $u$, with a vector $i_0 v_{\mathcal{B}}$ and frame vectors $e(k, a)$ and $e'(k, a)$ for $a = 0, \dots, r_S - 1$. Let $g$ be the generator of the row side, and let $z_R(u)$, $e_R(a)$ and $f_R(a)$ be the vectors of the row side, read in $E$. Then $\mathcal{B}$ is *framed* if there are $\mu, \lambda \in E$ with $\mu \neq 0$ and $\lambda = \pm g$ such that, in each coordinate $k$,

$$\begin{aligned} i_0 v_{\mathcal{B}} &= \mu \, z_R(u), \\ e(k, a) &= \mu \lambda^{r_S - a} \, e_R(a), \\ e'(k, a) &= \overline{\mu \lambda^{r_S - a}}^{\,-1} \, f_R(a). \end{aligned}$$

**Definition 4.5.3 (Placed Bessel datum).** Let $f$ be a family character for $u$. The datum $\mathcal{B}$ is *placed* for $f$ if there are a nonarchimedean local field $k$, commuting vector data $v$, type data $o$, local groups $G_1, \dots, G_n$ and a bijection of $\{1, \dots, n\}$ with the set $P_g$ such that: the commutation datum of $f$ is good, $v$ is good, $f$ and $v$ satisfy the commuting vector tie, $o$ has the right shape, the groups $G_i$ are pinned, they read the local groups of $f$, and $\mathcal{B}$ satisfies the local bottom compatibility with $f$, $v$, $o$ and the $G_i$. The datum is *strongly placed* if in addition the top vector of $v$ is primitive for $o$.

The local bottom compatibility contains the condition that $\mathcal{B}$ is adapted to the weight of the twist of $u$, which is the first clause of the pin.

**Definition 4.5.4 (Translate).** Let $f$ be a family character for $u$ with base point $b_0 = f.g.b_0$, let $\mathcal{B}$ be a Bessel datum for $u$ and $a_0, a \in G(X_0)$. The *translation element* is

$$\tau_{f, \mathcal{B}}(a_0, a) = x_u^{-1} \, \iota_{\mathcal{B}}(a_0 a) \, b_0 \in G(Y_0).$$

The pair $(a_0, a)$ is a *translate* for $(f, \mathcal{B})$ if $a_0$ is a transport adelic correction for $u$, $a \in G_f(X_0)$ is central in $G(X_0)$, and $\tau_{f, \mathcal{B}}(a_0, a)$ matches $(J_W, \chi_W)$.

By the definition of the pin in [the previous section](/entry/fam-all-q-of-all-true-alt/), a bottom datum $(\mathcal{B}, b_0, a_0, a, k)$ is pinned at $z$ exactly when $\mathcal{B}$ is adapted, $(a_0, a)$ satisfies the first two conditions of a translate, $k \in J_W$, and $\tau_{f, \mathcal{B}}(a_0, a) = z \, t_S \, k$.

**Theorem 4.5.5 (Translates exist).** Let $W$ be a real package that satisfies the package hypotheses. Let $u$ be a word, $f$ a family character for $u$ and $\mathcal{B}$ a Bessel datum that is placed for $f$ and framed. Then there is a translate $(a_0, a)$ for $(f, \mathcal{B})$.

Lean: `GlobalTheory.T.exists_isAt_of_placed_framed`.

This theorem is [the Theorem on translates](/entry/exists-is-at-alt/) of the second part of the chapter, and the statement here only passes the hypotheses to it. We first need a lemma on matching elements.

**Lemma 4.5.6 (Matching is stable under the level set).** If $t$ matches $(J_W, \chi_W)$ and $k \in J_W$, then $tk$ matches $(J_W, \chi_W)$.

*Proof.* Since $J_W \subset G_f(Y_0)$ is a subgroup, $tk \in G_f(Y_0)$. The character $\chi_W$ is multiplicative on $J_W$ and has no zeros, so for $j \in G(Y_0)$ we have $j \in J_W$ if and only if $k j k^{-1} \in J_W$, and then $\chi_W(k j k^{-1}) = \chi_W(j)$. Apply the matching of $t$ to $k j k^{-1}$:

$$j \in J_W \iff k j k^{-1} \in J_W \iff (tk)\, j\, (tk)^{-1} \in J_{\mathrm{row}},$$

and for $j \in J_W$, $\chi_{\mathrm{row}}((tk) j (tk)^{-1}) = \chi_W(k j k^{-1}) = \chi_W(j)$. $\square$

**Theorem 4.5.7 (One central pin).** Let $W$ be a real package that satisfies the package hypotheses, with $r_S \geq 1$. Then there is $z \in G_f(Y_0)$, central in $G(Y_0)$, with the following property. For each word $u$, each family character $f$ for $u$ and each Bessel datum $\mathcal{B}$ that is strongly placed for $f$ and framed, there is a bottom datum $d$ with $d.\mathcal{B} = \mathcal{B}$ and $d.b = f.g.b_0$ that is pinned at $z$.

Lean: `GlobalTheory.MiTop.exists_botDat_pin_of_placed_of_framed` (also `GlobalTheory.T.exists_botDat_of_placedP_framed`, a second name).

*Proof.* If there is no triple $(u, f, \mathcal{B})$ with $\mathcal{B}$ strongly placed for $f$ and framed, take $z = 1$; the property holds since it concerns no triple. Otherwise fix one such triple $(u_0, f_0, \mathcal{B}_0)$ and write $x_0 = x_{u_0}$.

1. A strongly placed datum is placed. By the Theorem on translates there is a translate $(a_0, a)$ for $(f_0, \mathcal{B}_0)$. Write $\tau_0 = \tau_{f_0, \mathcal{B}_0}(a_0, a)$.
2. The package hypotheses contain the bottom hypotheses. These give that $z' t_S$ matches $(J_W, \chi_W)$ for every central $z' \in G_f(Y_0)$, by a lemma of the second part. With $z' = 1$, the translation element $t_S$ of $W$ matches.
3. Since $\tau_0$ and $t_S$ both match and $r_S \geq 1$, [the Theorem on matching translates](/entry/matching-translates-bottom-alt/) gives $z \in G_f(Y_0)$ central in $G(Y_0)$, $c \in G_f(X_0)$ central in $G(X_0)$ and $k_0 \in J_W$ with

$$\tau_0 = x_0^{-1} \iota_{\mathcal{B}_0}(c)\, x_0 \, z \, t_S \, k_0.$$

4. We replace $a$ by $c^{-1} a$. Since $c$ is central, $a_0 c^{-1} a = c^{-1} a_0 a$, and since $\iota_{\mathcal{B}_0}$ is a homomorphism,

$$\begin{aligned} \tau_{f_0, \mathcal{B}_0}(a_0, c^{-1} a) &= x_0^{-1} \iota_{\mathcal{B}_0}(c)^{-1} \iota_{\mathcal{B}_0}(a_0 a)\, b_0 \\ &= \bigl(x_0^{-1} \iota_{\mathcal{B}_0}(c)\, x_0\bigr)^{-1} \tau_0 \\ &= z \, t_S \, k_0. \end{aligned}$$

The element $c^{-1} a$ lies in $G_f(X_0)$ and is central. By step 2, $z t_S$ matches, and by the Lemma, so does $z t_S k_0$. Hence $(a_0, c^{-1} a)$ is a translate for $(f_0, \mathcal{B}_0)$ with translation element $z t_S k_0$.

We show that this $z$ has the property. Let $(u, f, \mathcal{B})$ be a triple with $\mathcal{B}$ strongly placed for $f$ and framed.

5. By the Theorem on translates there is a translate $(b_0', b)$ for $(f, \mathcal{B})$.
6. By [the Theorem on compatible placed data](/entry/placed-bessel-compatibility-alt/), applied to the two translates $(b_0', b)$ for $(f, \mathcal{B})$ and $(a_0, c^{-1} a)$ for $(f_0, \mathcal{B}_0)$, there is $a_1$ such that $(b_0', a_1)$ is a translate for $(f, \mathcal{B})$ and $k \in J_W$ with

$$\tau_{f, \mathcal{B}}(b_0', a_1) = \tau_{f_0, \mathcal{B}_0}(a_0, c^{-1} a)\, k = z \, t_S \, k_0 k.$$

7. Let $d = (\mathcal{B}, f.g.b_0, b_0', a_1, k_0 k)$. Then $\mathcal{B}$ is adapted, as part of the local bottom compatibility; $b_0'$ is a transport correction and $a_1 \in G_f(X_0)$ is central, since $(b_0', a_1)$ is a translate; $k_0 k \in J_W$ since $J_W$ is a subgroup; and multiplying the identity of step 6 on the left by $x_u$ gives

$$\iota_{\mathcal{B}}(b_0' a_1)\, f.g.b_0 = x_u \, z \, t_S \, k_0 k.$$

So $d$ is pinned at $z$. $\square$

The element $z$ depends on the fixed triple of the proof. The point of the theorem is that it does not depend on $u$: all words are compared with the same $(u_0, f_0, \mathcal{B}_0)$.

**Remark 4.5.8 (Formalization).** The theorem is at [OneCentralPin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OneCentralPin.lean#L41), with the Lemma `matches_mul_of_mem_rJ'` at line 30; the second name is at [OneCentralPinStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OneCentralPinStatement.lean#L23), and the Theorem on translates at [ExistsIsAtStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAtStatement.lean#L22). Both statement files only pass the hypotheses on. The translate is `IsTranslate'` and the translation element `translationElement` of [Placed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Placed.lean#L33); "placed" is `PlacedAlt` there and "strongly placed" is `PlacedConditions` of [PlacedP.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacedP.lean#L27), which adds `PrimTop`. `Matches` is in [ThetaIdentityOfMapsAll.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L72), written with `ConjLevel t⁻¹`, and `Framed` is in [Framed.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/Framed.lean#L15). Step 2 is `botHyp_match_alt`, which returns six facts, of which only the fourth is used; step 3 is `matching_translates_bottom_alt` and step 6 is `placed_bessel_compatibility_alt`. The empty case with $z = 1$ is a `by_cases` at the start of the proof. The invariance of $J_W$ and $\chi_W$ under conjugation by $k$ in the Lemma is `conj_in_level`, with `levChi_mul_lev` and `levChi_ne_zero`. We did not unfold `rJ_z`, `realCharacter`, `IsTransportAdelicCorrection`, `LocalBottomCompatibility` beyond its field `adapted`, or the embedding `embA`.
