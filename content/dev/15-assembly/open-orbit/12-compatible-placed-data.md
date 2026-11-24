---
title: Compatible placed data
decls:
  - GlobalTheory.T.matching_translates_bottom_alt
  - GlobalTheory.MiTop.matches_differ_central_alt
  - GlobalTheory.T.placed_bessel_pair_character_alt
  - GlobalTheory.MiTop.centralRatio_stab_atT_alt
  - GlobalTheory.T.placed_bessel_pair_relation_alt
  - GlobalTheory.MiTop.finE_centralRatio_mem_St_alt
  - GlobalTheory.T.placed_bessel_compatibility_alt
  - GlobalTheory.MiTop.matching_coset_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Compatible placed data

This section proves [the Theorem on compatible placed data](/entry/placed-bessel-compatibility-alt/) and [the Theorem on matching translates](/entry/matching-translates-bottom-alt/). Both are used in [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/). There, one triple $(u_0, f_0, \mathcal B_0)$ is fixed, and every other strongly placed framed datum is compared with it. The comparison says that two translation elements differ, on the right, by an element of the level set $J_W$, after we change the central part of one translate. The proof has three parts. First, two matching elements differ by central elements and an element of $J_W$. Second, the central element $z$ of $G_f(Y_0)$ that appears there stabilises the frame $\beta_Y$. We check this place by place, and the twist places need a separate argument. Third, a reduction criterion puts $z$ in $J_W$.

We keep the notation of [the section on translates](/entry/exists-is-at-alt/). For a word $u$, a family character $f$ for $u$ and a Bessel datum $\mathcal B$, $\tau_{f, \mathcal B}(a_0, a) = x_u^{-1} \iota_{\mathcal B}(a_0 a) b_0$ is the translation element. $\Lambda_Y$ is the self-dual lattice of $Y_0$ of the package and $\beta_Y$ its frame. For a place $v$ of the base field $F$, $\mathrm{St}_v(\Lambda_Y)$ is the stabiliser of the completion of $\Lambda_Y$ at $v$, and $z_v$ is the component of $z$ at $v$. The places of $P_g$ are the type places of the package, and $T_u$ is the twist number of $u$.

**Theorem 4.12.1 (Matching translates).** Let $W$ satisfy the bottom hypotheses, with $r_S \geq 1$. Let $u$ be a word, $\mathcal B$ a Bessel datum for $u$, and $t, t' \in G_f(Y_0)$ two elements that match $(J_W, \chi_W)$. Then there are $z \in G_f(Y_0)$ central in $G(Y_0)$, $c \in G_f(X_0)$ central in $G(X_0)$ and $k \in J_W$ with

$$t = x_u^{-1} \, \iota_{\mathcal B}(c) \, x_u \; z \; t' \; k.$$

Lean: `GlobalTheory.MiTop.matches_differ_central_alt` (also `GlobalTheory.T.matching_translates_bottom_alt`, a second name).

*Proof.* This is [the Theorem on matching translates that differ by the centre](/entry/matches-differ/) of the volume on the doubling scalar, applied to the row side of $W$, the word $u$ and $\mathcal B$. Its only hypothesis on the row side is $r_S \geq 1$. $\square$

The bottom hypotheses and the conditions $t, t' \in G_f(Y_0)$ are not needed. Matching already contains $t \in G_f(Y_0)$.

For the next two results we fix the following data. Let $W$ satisfy the package hypotheses, with $r_S \geq 1$. Let $u, u'$ be words, $f, f'$ family characters for $u, u'$, and $\mathcal B, \mathcal B'$ Bessel data that are strongly placed for $f$ and $f'$. Let $(a_0, a)$ be a translate for $(f, \mathcal B)$ and $(a_0', a')$ a translate for $(f', \mathcal B')$, with translation elements $\tau$ and $\tau'$. Let $z \in G_f(Y_0)$ be central and $k \in J_W$ with

$$\tau = z \, \tau' \, k.$$

**Theorem 4.12.2 (Central ratio at the twist places).** In this situation, let $v$ be a place of $F$ that does not lie under a place of $P_g$, and such that $T_u \in v$ or $T_{u'} \in v$. Then $z_v \in \mathrm{St}_v(\Lambda_Y)$.

Lean: `GlobalTheory.MiTop.centralRatio_stab_atT_alt` (also `GlobalTheory.T.placed_bessel_pair_character_alt`, a second name).

*Proof.* The idea is that $z$ is a scalar, and a scalar that keeps one good vector in the lattice keeps the lattice.

1. Since $k \in J_W$, the component $k_v$ lies in the level group of $\beta_Y$, so $k_v$ stabilises the completion of $\Lambda_Y$ at $v$.
2. Since $z$ is central, $z_v^{-1}$ acts on $Y_0$ at $v$ as a scalar $c$.
3. Results of another chapter on the vectors of a placed translate apply to $(a_0, a)$ and to $(a_0', a')$ at $v$. A third result of another chapter, on the vectors of the pair, combines them with the relation $z^{-1} \tau = \tau' k$. Together they say that $c$ carries a line vector $w$ of the lattice at $v$ into the lattice, and that $c^{-1}$ does the same. The vector $w$ is built from the first row vector $e_R(0)$.
4. The first isotropic coordinate of $e_R(0)$ is not zero. So $w$ spans a line that meets the lattice in a primitive vector, and a scalar that keeps the lattice on this line keeps the whole lattice.
5. So $c$ and $c^{-1}$ keep the completion of $\Lambda_Y$ at $v$, and $z_v$ lies in its stabiliser. $\square$

**Theorem 4.12.3 (Central ratio stabilises the frame).** In the same situation, the finite part $z_f$ of $z$ lies in $\mathrm{St}(\beta_Y)$.

Lean: `GlobalTheory.MiTop.finE_centralRatio_mem_St_alt` (also `GlobalTheory.T.placed_bessel_pair_relation_alt`, a second name).

*Proof.* The frame $\beta_Y$ is a frame of the self-dual lattice $\Lambda_Y$. A result of another chapter on such frames says that $z_f \in \mathrm{St}(\beta_Y)$ exactly when $z_v \in \mathrm{St}_v(\Lambda_Y)$ at every finite place $v$. Fix $v$. There are three cases.

1. If $v$ lies under a place of $P_g$, a result of another chapter on the scalars of a placed pair gives $z_v \in \mathrm{St}_v(\Lambda_Y)$.
2. If $v$ does not lie under $P_g$ and $T_u \in v$ or $T_{u'} \in v$, the previous theorem applies.
3. Otherwise $v$ lies under no place of $P_g$ and contains neither $T_u$ nor $T_{u'}$. A result of another chapter on the translates of a placed pair gives $z_v \in \mathrm{St}_v(\Lambda_Y)$ at such places. $\square$

**Lemma 4.12.4 (Matching under central factors).** Let $t$ match $(J_W, \chi_W)$, let $z \in G_f(Y_0)$ be central and let $k \in J_W$. Then $z t k$ matches $(J_W, \chi_W)$.

*Proof.* By [the Lemma that matching is stable under the level set](/entry/exists-bot-dat-pin-of-placed-of-framed/), $t k$ matches. Since $z$ is central, conjugation by $z t k$ is conjugation by $t k$, and $z t k \in G_f(Y_0)$. $\square$

**Theorem 4.12.5 (Compatible placed data).** Let $W$ satisfy the package hypotheses, with $r_S \geq 1$. Let $u, u'$ be words, $f, f'$ family characters for $u, u'$, and $\mathcal B, \mathcal B'$ Bessel data that are strongly placed for $f$ and $f'$ and framed. Let $(a_0, a)$ be a translate for $(f, \mathcal B)$ and $(a_0', a')$ a translate for $(f', \mathcal B')$. Then there is $a_1$ such that $(a_0, a_1)$ is a translate for $(f, \mathcal B)$, and there is $k \in J_W$ with

$$\tau_{f, \mathcal B}(a_0, a_1) = \tau_{f', \mathcal B'}(a_0', a') \, k.$$

Lean: `GlobalTheory.MiTop.matching_coset_alt` (also `GlobalTheory.T.placed_bessel_compatibility_alt`, a second name).

*Proof.* Write $\tau = \tau_{f, \mathcal B}(a_0, a)$ and $\tau' = \tau_{f', \mathcal B'}(a_0', a')$.

1. Both $\tau$ and $\tau'$ match. The package hypotheses contain the bottom hypotheses. By the Theorem on matching translates, at the word $u$ and the datum $\mathcal B$, there are central $z$, $c$ and $k \in J_W$ with $\tau = x_u^{-1} \iota_{\mathcal B}(c) x_u \, z \tau' k$.
2. Put $a_1 = a c^{-1}$. Since $c$ is central in $G(X_0)$, $a_0 a c^{-1} = c^{-1} a_0 a$, and $\iota_{\mathcal B}$ is a homomorphism. So

$$\begin{aligned} \tau_{f, \mathcal B}(a_0, a_1) &= x_u^{-1} \iota_{\mathcal B}(c)^{-1} x_u \, \tau \\ &= z \, \tau' \, k. \end{aligned}$$

3. The element $a_1$ lies in $G_f(X_0)$ and is central, as $a$ and $c$ are. By the Lemma on central factors, $z \tau' k$ matches. So $(a_0, a_1)$ is a translate.
4. Now the relation of step 2 has the form of the fixed data above, with $a_1$ in place of $a$. By the Theorem that the central ratio stabilises the frame, $z_f \in \mathrm{St}(\beta_Y)$.
5. A result of another chapter on the pair gives the reductions of $z$: at each place of $P_g$ the reduction of $z$ in the local group is $1$.
6. A reduction criterion says that an element $z \in G_f(Y_0)$ with $z_f \in \mathrm{St}(\beta_Y)$ and trivial reductions at the places of $P_g$ lies in $J_W$. So $z \in J_W$.
7. Put $k' = z k \in J_W$. Since $z$ is central, $z \tau' k = \tau' z k = \tau' k'$. $\square$

The reduction criterion of step 6 is the description of $J_W$ by level groups. The level group of $\beta_Y$ at the type places is cut out by a reduction map to the local groups $G_i$, and off these places it is the stabiliser.

**Remark 4.12.6 (Formalization).** The theorems are at [MatchesDifferCentral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MatchesDifferCentral.lean#L22), [CentralRatioStabAtT.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CentralRatioStabAtT.lean#L27), [FinECentralRatioMemSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinECentralRatioMemSt.lean#L28) and [MatchingCoset.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MatchingCoset.lean#L66). The second names are relays at [MatchesDifferCentralStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MatchesDifferCentralStatement.lean#L20), [CentralRatioStabAtTStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CentralRatioStabAtTStatement.lean#L24), [FinECentralRatioMemStStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinECentralRatioMemStStatement.lean#L24) and [MatchingCosetStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MatchingCosetStatement.lean#L24). The reduction criterion is `mem_rJ_of_red_alt` (line 32) and the Lemma on central factors is `matches_mul_of_mem_rJ` (line 53), both in MatchingCoset.lean. Some details:

- In `matches_differ_central_alt` (line 23) the bottom hypotheses and the two proofs of $t, t' \in G_f(Y_0)$ are bound as `_` and not used. The body is one call to `LevNorm.matches_differ`. Lines 19 to 21 of the same file open and close an empty namespace `GlobalTheory.LevNorm`.
- The framing hypotheses of `matching_coset_alt` are not used. At lines 87 to 92 the calls to `placed_bessel_pair_relation_alt` and `placed_bessel_pair_identity_alt` are wrapped in `first`, and the first branch passes the framing proofs, which these results do not take. The second branch, without them, is the one that elaborates. So the theorem holds for strongly placed data without the framing, and so does its relay.
- The name `placed_bessel_pair_character_alt` speaks of a character, but the conclusion is a stabiliser condition at one place. The name `placed_bessel_pair_relation_alt` hides that the conclusion is the stabiliser of $\beta_Y$.
- We have not opened the three local results of the second proof (`placed_bessel_pair_scalar_alt`, `placed_bessel_pair_translate_alt`, and the vector results `placed_bessel_translate_vector_alt` and `placed_bessel_pair_vector_alt`), nor `placed_bessel_pair_identity_alt` of step 5.
