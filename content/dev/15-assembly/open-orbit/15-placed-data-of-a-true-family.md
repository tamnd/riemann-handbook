---
title: Placed data of a true family
decls:
  - GlobalTheory.FamPlaced.placedP_of_allTrue
  - GlobalTheory.T.placed_p_of_true_geometry
  - GlobalTheory.FamTrace.levTrace_mem_alt
  - GlobalTheory.T.true_geometry_local_data_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Placed data of a true family

This section proves [the Theorem on placed data](/entry/placed-p-of-true-geometry/), which step 5 of the proof in [the section on the family conditions](/entry/mi-star2-of-all-true-alt-alt/) uses. A geometric family $a$ that is good and true carries the Bessel datum $a.\mathcal B$ of its bottom datum. The theorem says that this datum is strongly placed for each family character $f = a(\mathrm{row}, \mathrm{col})$ whose commutation datum is good. Most of the eight clauses of a strongly placed datum are fields of the good family, read off directly. Two need an argument: the primitivity of the top vector, which uses the twist number $T_u$ and the element $\pi_T$ of norm $T_u$, and the trace condition, which compares the level group at zero with the level set $J_W$ after conjugation by the base point $b_0$.

We keep the notation of [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/) and of [the section on the family conditions](/entry/mi-star2-of-all-true-alt-alt/). $W$ is a real package over $D$ that satisfies the family conditions on a package. $u$ is a word with twist number $T_u$, and $\pi_T \in \mathcal O_E$ is the element with $\pi_T \overline{\pi_T} = T_u$ fixed by the package. $a$ is a geometric family for $W$ and $u$, with local field $k$, commuting vector data $v$, type data $o$ with line vector $\zeta_0$, local groups $G_1, \dots, G_n$ and the bijection with $P_g$. Its bottom datum has the Bessel datum $\mathcal B = a.\mathcal B$ with embedding $\iota_{\mathcal B}$. For a row and a column, $f = a(\mathrm{row}, \mathrm{col})$ and $b_0 = a.g.b_0$ is the base point at level zero. The level group at zero of the forms at zero is $U_0$ with the character $\chi_0$. $P_T$ is the set of twist places of $v$.

**Definition 4.15.1 (Primitive top vector).** Let $\zeta_0$ be the line vector of $o$ and $w = o_T(\zeta_0)$ its image in the top space $X_m$, with the lattice $L_m$. The top vector is *primitive* off $P_T$ if for each finite place $p \notin P_T$ and each $\alpha$ in the local completion at $p$,

$$\alpha w \in L_{m, p} \iff \alpha \text{ is integral at } p.$$

**Definition 4.15.2 (Trace condition).** $\mathcal B$ satisfies the *trace condition* for $f$ if for each $\kappa \in G_f(X_0)$ and each $y$ in the finite adelic unitary group of the Gram matrix at zero with finite part equal to that of $\kappa$,

$$y \in U_0 \iff b_0^{-1} \, \iota_{\mathcal B}(\kappa) \, b_0 \in J_W,$$

and for $y \in U_0$, $\chi_0(y) \cdot \chi_W\bigl(b_0^{-1} \iota_{\mathcal B}(\kappa) b_0\bigr) = 1$.

The local bottom compatibility of [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/) has six parts: the level of $\mathcal B$ is the Bessel datum of the commutation datum at $(0, r_S)$; $\mathcal B$ is adapted to the weight of the twist of $u$; there are $\mu, \lambda$ with $\mu \lambda = -\xi_0^{m/2}$, the vector $i_0 v_{\mathcal B}$ is $\mu$ times the vector $z_R(u)$, and the twist $\tau$ of $v$ sends $\zeta_0$ to $\lambda$ times the Bessel vector; the last vector of each $G_i$ is the projection of $\zeta_0$; the lattice of $X_0$ is the lattice of the level group at zero at each place $p \notin P_T$; and the trace condition.

**Theorem 4.15.3 (Level groups by conjugation).** Let $a$ be good and true, and let $f = a(\mathrm{row}, \mathrm{col})$ have a good commutation datum. Then for each $\kappa \in G_f(X_0)$ and $y$ as above,

$$y \in U_0 \iff b_0^{-1} \, \iota_{\mathcal B}(\kappa) \, b_0 \in J_W.$$

Lean: `GlobalTheory.FamTrace.levTrace_mem_alt` (also `GlobalTheory.T.true_geometry_local_data_alt`, a second name).

*Proof.* We turn both sides into conditions on lattices, place by place.

1. The embedding $\iota_{\mathcal B}$ maps $G_f(X_0)$ into $G_f(Y_0)$, so $g = b_0^{-1} \iota_{\mathcal B}(\kappa) b_0$ lies in $G_f(Y_0)$.
2. A result of another chapter rewrites $y \in U_0$, through the finite part of $\kappa$, as the condition that $\kappa$ lies in the level group of the lattice $L_0$ of $X_0$.
3. A second result of another chapter rewrites $g \in J_W$, for $g \in G_f(Y_0)$, as the condition that $g$ lies in the level group of the frame of $Y_0$.
4. Two more results of another chapter turn both level groups into lattice conditions. The first says that $\kappa$ carries the completion of $L_0$ to itself at the places of $P_g$, and also off them. The second says the same of $\iota_{\mathcal B}(\kappa)$ and the lattice $b_0 \Lambda_Y$ moved by the base point. The hypotheses that $a$ is good and true enter only through these results.
5. A lattice is carried to itself at all finite places exactly when it is so at the places of $P_g$ and at the places outside $P_g$. Split both sides of steps 2 and 3 at $P_g$ in this way. The two sides become the same conjunction, and the equivalence follows. $\square$

**Theorem 4.15.4 (Placed data).** Let $W$ satisfy the family conditions on a package. Let $u$ be a word, $a$ a geometric family for $W$ and $u$ that is good and true, and $f = a(\mathrm{row}, \mathrm{col})$ a family character of $a$ whose commutation datum is good. Then $a.\mathcal B$ is strongly placed for $f$.

Lean: `GlobalTheory.FamPlaced.placedP_of_allTrue` (also `GlobalTheory.T.placed_p_of_true_geometry`, a second name).

*Proof.* We take the local field $k$, the data $v$ and $o$, the groups $G_i$ and the bijection of $a$, and check the clauses.

1. The commutation datum of $f$ is good by hypothesis. That $v$ is good, the commuting vector tie, the shape of $o$, the pins of the $G_i$ and the reading of the local groups of $f$ are fields of the good family $a$: the first part of the tie at $(\mathrm{row}, \mathrm{col})$ gives the vector tie, and its second part gives the reading.
2. *Primitive top vector.* Let $p \notin P_T$. The twist places of $v$ are the places that divide $T_u$, by the tie of $a$, so $T_u \notin p$. The true family gives the vector of the top decomposition at $\zeta_0$ through the point $z_0(u)$, whose coordinates are integral: all are $0$ except the last, which is $\pi_T$. The last coordinate satisfies
   $$\begin{aligned} z_0(u)_{N-1} \cdot \overline{\pi_T} &= \pi_T \overline{\pi_T} \\ &= T_u. \end{aligned}$$
   A result of another chapter on primitive vectors says: if a vector has integral coordinates, and one coordinate times an integral element is an integer not in $p$, then $\alpha w \in L_{m, p}$ exactly when $\alpha$ is integral at $p$. Apply it with the last coordinate and $\overline{\pi_T}$. The lattice $L_m$ is the right one by the pin condition of the true family at level $m$.
3. *Level.* The level clause of the bottom datum of $a$ gives that the level of $\mathcal B$ is the Bessel datum of the commutation datum at $(0, r_S)$, whenever $0 + 2 r_S + 2 = m$.
4. *Adapted.* This is the next clause of the bottom datum of $a$.
5. *Norm.* Take $\mu = 1$ and $\lambda = -\xi_0^{m/2}$, so $\mu \lambda = -\xi_0^{m/2}$. With $\mu = 1$, the condition on $i_0 v_{\mathcal B}$ is the last clause of the bottom datum of $a$. The condition on $\tau \zeta_0$ is the norm condition of the good family.
6. *Last vectors.* The standard condition on the local groups of $a$ gives that the last vector of each $G_i$ is the projection of $\zeta_0$.
7. *Lattice.* A result of another chapter, on the lattice off the twist, gives that at each $p \notin P_T$ the lattice of $X_0$ is the lattice of the level group at zero.
8. *Trace.* The first part is the Theorem on level groups by conjugation. The second part, the character identity, is a result of another chapter on the reduction of the level, with the same hypotheses. $\square$

The clause on $\tau\zeta_0$ fixes $\lambda$, and with it $\mu = 1$. This is why the framing of [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/) is not used here: the vector $i_0 v_{\mathcal B}$ is already $z_R(u)$.

**Remark 4.15.5 (Formalization).** The theorem on placed data is at [PlacedOfTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacedOfTrue.lean#L32), with the primitivity at lines 37 to 57 and the local bottom compatibility at lines 62 to 72. The theorem on level groups is at [LevTraceMem.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevTraceMem.lean#L25). The second names are relays at [PlacedOfTrueStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacedOfTrueStatement.lean#L19) and [LevTraceMemStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevTraceMemStatement.lean#L20). The strongly placed condition is `PlacedConditions` in [PlacedP.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacedP.lean#L27), and the local bottom compatibility and the trace condition are `LocalBottomCompatibility` and `LevTraceAlt` in [ChartZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ChartZero.lean#L28). Some details:

- The primitive top vector is `PrimTop`, in Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlacedP.lean at line 20. The lemma `PlacedConditions.placed` (PlacedP.lean, line 31) forgets it, with a `-` in its pattern, to get `PlacedAlt`. So step 2 is needed only for the strongly placed form used in [the section on one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/).
- Lines 29 to 31 of PlacedOfTrue.lean open and close an empty `section Prim`.
- The name `true_geometry_local_data_alt` speaks of local data, but the statement is the first half of the trace condition.
- The four results of steps 2 to 4 of the first proof are `true_geometry_final_identity_alt`, `true_geometry_final_value_alt`, `true_geometry_final_relation_alt` and `true_geometry_final_property_alt`; step 5 is `carriesLatticeCompletion_on_off_iff_all_finitePlaces` with the predicate "in $a.v.g_P$", followed by `tauto`. We describe them by their use and have not opened their proofs, nor `prim_std`, `lattice_eq_base_off_twist_alt` and `true_geometry_reduction_level_alt`.
