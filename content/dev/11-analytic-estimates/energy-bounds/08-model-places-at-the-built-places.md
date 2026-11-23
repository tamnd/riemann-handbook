---
title: Model places at the built places
decls:
  - Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.model_place_built_holds
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_chartEqs
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_jf
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_polyS
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_SSnRep
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_rotK
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_ssnRep
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_bdd
  - Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_hat
  - Formalism.FourierDecayAlt.P.CutMP.JA.jAdjTrQQ_of_three
  - Formalism.FourierDecayAlt.P.CutMP.JA.jAdjTrQQ_of_open
  - Formalism.FourierDecayAlt.P.CutMP.JA.jABddOpQQ_of_ssnRep
  - Formalism.FourierDecayAlt.P.CutMP.JA.second_shift_geometry_holds
  - Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.ssnRep_of_polyS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Model places at the built places

The vector $f$ of the main argument has one component $f_v$ for each infinite place $v$ of a CM field $E$. This section proves that at each such place the energy of $f_v$ is a model energy, in the sense of [the model](/entry/lemma-model/): there are model data $(\mathcal{L}, j, \lambda)$ and constants $C_m, \sigma > 0$ such that the energy of the cut of $f_v$ at $\varepsilon$ is $C_m$ times the model energy at $\sigma\varepsilon$. Then Lemma E in the model gives the limit of the energy at each infinite place. The proof is a chain of reductions. Each step removes one input, and the last inputs are the [polynomial radial relation](/entry/polynomial-radial-holds/) and an elliptic regularity theorem. For the representation theory used here see [representations of real groups](/learn/representations/#representations-of-real-groups) and [unitary groups](/learn/groups/#unitary-groups).

**Definition 3.8.1 (Built place).** Let $E$ be a CM number field, let $S$ be a setting over $E$ with $f$ infinite places $v$, and let $T_v$ be a level tower at $v$ with base data $(z, z', \pi, \pi')$. Let $f_v$ be smooth functions on the real group $G_V$, let $\chi$ be a cutoff, and let $\nu'$, $m_0$, $\mathrm{top}$ and $A_0$ be the auxiliary data of the construction. The data form a *built place* for a constant $C_c$ if: the two weights $g_1, g_2$ of the setting are positive; $E$ is unramified in the required sense; the tower and the vectors are the ones that the construction builds; the level $l$ of the setting satisfies $1 \leq l$ and $l + 2 \leq k$; the grids are admissible; the cut is long with respect to $C_c$, and $C_c$ is at most the constant $C_A$ of the setting; each $f_v$ is smooth on $G_V$; $k \geq 2$; the budget
$$C_c (r + 1)^4 \big(N (2r + k + 1)^2 + (2r + k + 1)^3\big) \leq A_0$$
holds, where $N$ is the top length of the setting; and each $Y$ in the cut interval $[\alpha_v, \beta_v]$ of $v$ lies on the cut of $(u_v, u_v', l + 1)$.

**Definition 3.8.2 (Model place).** Built place data are a *model place* at $v$, with model data $(\mathcal{L}, j, \lambda)$, a cutoff $c$ with $c.\chi = \chi$ and constants $C_m, \sigma > 0$, if the model data satisfy the setting condition of [the model](/entry/lemma-model/) at the level $l + 1$ with the interval $[\alpha_v, \beta_v]$, the conditions of decay and adjoints of order $2N + 2$ and the eigenvalue condition, and if for each admitted word $a$ at $v$:

1. for all $\varepsilon > 0$ the energy of the cut of $f_v$ at $\varepsilon$ on the word $a$ is $C_m\, \mathcal{E}_{\sigma\varepsilon}(a)$, where $\mathcal{E}$ is the model energy of the cutoff $c$;
2. for every box length, $a$ is admitted in the model energy system, and its size there is the size of $a$ at $v$.

**Theorem 3.8.3 (Model places at the built places).** There is a constant $C_c$ with the following property. Let $E$, $S$, $T$, $f$, $\chi$ and the auxiliary data form a built place for $C_c$, assume that each place of the setting is admissible and that the two weight words $d, d'$ of the setting are words, and let $c$ be a cutoff with $c.\chi = \chi$. Then for each infinite place $v$ there are model data and constants $C_m, \sigma$ that make the data a model place at $v$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.model_place_built_holds`.

The proof takes the rest of the section. We first name the inputs. All of them are statements about built place data, and all hold with a constant $C_c$ that one can increase.

- (J) *Smoothness.* The vector $J_f$ attached to $f_v$ lies in the space of smooth functions on the open set $\Omega_+$ with the covariance of $(\pi, \pi')$.
- (G) *Gauge transfer.* At each real place with the standard section there is a frame $e$ of the fibres along $\mu_0$ such that the transfer $\mathrm{tr}_e$ to functions on the model domain carries the operators $\zeta, \zeta^{-1}, \bar\zeta, \bar\zeta^{-1}, G, G^{-1}, \nabla, \dots$ of the level datum to the model operators of the same names.
- (K) *Rotation invariance.* Operators on the radial space that commute with the radial multipliers and act by a rotation in $\zeta$ preserve the frame.
- (H) *Hat operators.* For each frame and gauge and each $X$ in the set $\widehat{\mathcal{A}}$ of the model level datum, the transfer of $X$ is a finite sum $\sum_t b_t\, \mathrm{tr}_e \circ D_t$ with $b_t$ in the monoid of bounded operators and $D_t$ differential operators with smooth coefficients that commute with the group action.
- (B) *Bounded operators.* For each $b$ in the set $\mathcal{B}$ of bounded model operators there is an operator $\Theta$ of order $0$ with cut coefficients bounded by $C_b (r + 1)$ such that $\mathrm{tr}_e(\Theta J) = b(\mathrm{tr}_e J)$, and $\Theta$ and its adjoint preserve the cone of smooth forms.
- (D) and (A) *Transfer of decay and adjoints.* For each frame and gauge, $j = \mathrm{tr}_e(J_f)$ satisfies the decay and the adjoint conditions of order $2N + 2$.
- (S) *Second shift representation.* For each frame and gauge and each level $1 \leq l \leq k - 1$ there are fibre maps $(\Phi, \Phi_a)$ that represent the second shift at the level $l$.
- (P) *Polynomial radial relation*, the [theorem](/entry/polynomial-radial-holds/) of the previous section.
- (C) *Chart equations.* In smooth charts of the real group, a function $u$ that satisfies the equations of the place solves a finite system of differential operators $P_j$ of order at most $2r + k + 1$ with smooth coefficients. A real covector $\xi \neq 0$ at which all principal symbols vanish gives a nonzero nilpotent element $\Xi$ of the Lie algebra that is orthogonal to the Lie algebras of $U_W(z)$, of $U_W(z')$ and of the unipotent radical.

The chain of reductions runs from the bottom of this list to the top: (C) gives (J), (P) gives (S), (S) gives (B), (K) gives (G), and (B) gives (H) and then (A).

**Proposition 3.8.4 (Adjoints from bounded and hat operators).** Assume (H) and (B), the transfer of the star operator, a transfer of group adjoints and a transfer of local classes. Then (A) holds. The last two inputs hold, so (H), (B) and the star transfer give (A).

Lean: `Formalism.FourierDecayAlt.P.CutMP.JA.jAdjTrQQ_of_open` (also `Formalism.FourierDecayAlt.P.CutMP.JA.jAdjTrQQ_of_three`, the form with three inputs).

*Proof.* Let $X \in \widehat{\mathcal{A}}$, let $b$ be in the monoid of $\mathcal{B}$, and let $v, w$ be products of operators of $\widehat{\mathcal{A}}$. By (H) and (B) the functions $\varphi(G)\, b v j$ and $w j$ are transfers of smooth forms $\Theta_b D_v J_f$ and $D_w J_f$, and the transfer of $X$ is a combination of differential operators on the group. On the group, the adjoint of a right invariant differential operator with respect to Haar measure is the formal adjoint, and the star transfer identifies it with the transfer of $X^*$. The cutoff $\varphi(G)$ vanishes near the boundary, so integration by parts has no boundary terms. The local class transfer keeps the forms in the class where the integrals converge, and the stability of smooth forms under the operators closes the argument. $\square$

**Proposition 3.8.5 (Reduction to bounded and hat operators).** (J), (G), (H) and (B) imply the Theorem. With (H) proved, (J), (G) and (B) imply the Theorem.

Lean: `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_hat` (also `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_bdd`, the form with (H) proved).

*Proof.* (H) gives the transfer of decay: each $a_1 \cdots a_n j$ is a finite sum of bounded operators applied to transfers of $D J_f$ with $D$ smooth, and these are square integrable since $J_f$ lies in the smooth class by (J). (H), (B) and the star transfer give (A) by the previous Proposition. Then (J), (G), (D) and (A) give the model place. The gauge (G) provides the frame, the model level datum and the function $j = \mathrm{tr}_e(J_f)$. The energy trace identity writes the energy of the cut of $f_v$ as $C_m$ times the model energy at $\sigma\varepsilon$, and the energy is real. The conditions on admitted words and sizes are identities between the two energy systems. The setting and eigenvalue conditions come from the built place. $\square$

**Lemma 3.8.6 (Second shift geometry).** There is $K \geq 0$ such that for all $C_c, C_b \geq K$ and all built place data with constant $C_c$, each infinite place $v$ has a geometric datum $(a, a', \iota)$ with bound $C_b (r + 1)$.

Lean: `Formalism.FourierDecayAlt.P.CutMP.JA.second_shift_geometry_holds`.

*Proof.* The datum consists of two vector valued functions $a, a'$ on the group and a map $\iota$ of the group to itself. Its conditions are smoothness, equivariance of the first vector, equivariance of the embedding, the value at the level function, a bound at $0$ and a bound for the unipotent part. Each is proved separately, and the bounds have the form $C_b (r + 1)$ since the unipotent part has $r + 1$ blocks. $\square$

**Proposition 3.8.7 (Bounded operators from the second shift).** (S) implies (B). In particular, (J), (G) and (S) imply the Theorem.

Lean: `Formalism.FourierDecayAlt.P.CutMP.JA.jABddOpQQ_of_ssnRep` (also `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_ssnRep`, the form for the Theorem).

*Proof.* The bounded set $\mathcal{B}$ consists of a scalar part, a part given by the quadratic form $\kappa$, and the second shifts and their adjoints. For the scalar part the operator $\Theta$ is multiplication by a bounded function. For $\kappa$ the bound comes from the geometry lemma, the type projections, the gauge lines and the unit norm of the datum. For a second shift at the level $l$, (S) gives fibre maps that represent it, and a chain bound on the geometric datum bounds its cut coefficients by $C_b (r + 1)$; the same holds for the adjoint. The reduction of the previous Proposition then gives the Theorem. $\square$

**Proposition 3.8.8 (Gauge from rotation invariance).** (J), (K) and (S) imply the Theorem. Since (K) holds, (J) and (S) imply the Theorem.

Lean: `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_rotK` (also `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_SSnRep`, the form with (K) proved).

*Proof.* By [the gauge transfer](/entry/gen-transfer-of-rot-k/), (K) gives (G). Its proof builds the gauge function and its connection, shows that the curvature of the connection is the expected one and that its holonomy is trivial on the reference annulus, and moves the gauge to the radial coordinate. Rotation invariance gives the trace of the reference curvature. The previous Proposition ends the proof. $\square$

**Proposition 3.8.9 (Second shift from the radial relation).** (P) implies (S). Hence (J) and (P) imply the Theorem, and (J) alone implies it.

Lean: `Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.ssnRep_of_polyS` (also `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_polyS` and `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_jf`, the forms for the Theorem).

*Proof.* Fix $v$, a frame and gauge, and a level $l$. The fibre maps of (S) send a vector of type $\pi$ to the projection of type $\rho$ of the second shift, where $\rho_i = \pi_i + [i + 1 = l]$. The projection of type $\rho$ exists. A modular constancy statement says that along a line in the fibre the datum is constant up to a unit; it uses that the line does not vanish, that its dimension is at most one, that the datum is transitive, and two identities for the raising operator and the norm at the section. The polynomial radial relation then writes the projected shift as $q(\sqrt{|\zeta|^2 - \tau})(|\zeta|^2 - \tau)^{-n}$ times the projected theta operator, and the fibre maps are read off from this formula. For the last claim, the [polynomial radial relation](/entry/polynomial-radial-holds/) is a theorem. $\square$

**Proposition 3.8.10 (Smoothness from the chart equations).** (C) implies the Theorem.

Lean: `Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_chartEqs`.

*Proof.* We show that (C) gives (J). The function $J_f$ is continuous and, in a chart $\kappa : O \to G_V$, the function $u \circ \kappa$ is a weak solution of the system $P_j(u \circ \kappa) = 0$, since it is a classical solution of class $C^{2r + k + 1}$. The system is elliptic: if all principal symbols vanish at $\xi \neq 0$, then (C) gives a nonzero nilpotent $\Xi$ orthogonal to the Lie algebras of $U_W(z)$, $U_W(z')$ and the unipotent radical, and the structure of the place excludes such an element on $\Omega_+$. Elliptic regularity for systems with smooth coefficients then shows that $u \circ \kappa$ is smooth on $O$. The charts cover $\Omega_+$, so $J_f$ is smooth there, which is (J). The previous Proposition ends the proof. $\square$

*Proof of the Theorem.* The [chart equations](/entry/chart-equations-holds/) hold: they come from the Capelli word identities on the left and on the right of the group. The previous Proposition gives the Theorem. $\square$

The chain shows where the analysis enters: elliptic regularity gives smoothness, and the polynomial radial relation gives the bounds on the second shifts. All other steps are identities between operators on the group and on the model domain.

**Remark 3.8.11 (Formalization).** The statement is `JCT.ModelPlaceBuilt2` ([StatementJCT.lean](lean:Formalism/HermitianCurvature/StatementJCT.lean#L317)), with `IsBuiltPlace` at line 153 and `JC.IsModelPlace` in [StatementJC.lean](lean:Formalism/HermitianCurvature/StatementJC.lean#L117). `model_place_built_holds` is in [TransferSmoothAtBuiltPlace.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TransferSmoothAtBuiltPlace.lean#L9). The chain is `modelPlaceBuilt2_of_chartEqs` (ModelPlaceBuilt2OfChartEqs.lean, line 9), `modelPlaceBuilt2_of_jf` (CutJAPRSSnRep.lean, line 6), `modelPlaceBuilt2_of_polyS` and `ssnRep_of_polyS` (CutJASSnRepDone.lean, lines 27 and 20), `modelPlaceBuilt2_of_SSnRep` (GaugeConstructionHolds.lean, line 12), `modelPlaceBuilt2_of_rotK` (CutGCoreDone.lean, line 43), `modelPlaceBuilt2_of_ssnRep` and `jABddOpQQ_of_ssnRep` (CutJABddDone.lean, lines 26 and 17), `modelPlaceBuilt2_of_bdd` (ModelPlaceBuilt2OfBdd.lean, line 6), `modelPlaceBuilt2_of_hat` (ModelPlaceBuilt2OfHat.lean, line 8), `jAdjTrQQ_of_three` (JAdjTrQQOfThree.lean, line 6), `jAdjTrQQ_of_open` (CutJAQQOpen.lean, line 11) and `second_shift_geometry_holds` (CutJASSnGeom.lean, line 11). The inputs are `JfSmoothDS` (CutRegFF.lean, line 28), `Gauge.GC.GenTransfer`, `GTRRotK`, `JDHatOpQQ`, `JABddOpQQ`, `JDecayTrQQ`, `JAdjTrQQ`, `SSnRep`, `SSnGeom` and `ChartEqs` (JfSmoothBuiltOfLeaves.lean, line 56); the elliptic regularity input is `EllRegW` ([TransferSmoothOfRegularity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TransferSmoothOfRegularity.lean#L37)). We read the statements of the inputs and the top-level term of each reduction, and we did not unfold `IsDatum`, `IsFibreMap`, `IsFrame`, `IsGauge`, `trJ`, `BuiltOW` or `smoothFormsPositiveCone`, so the proofs of the Propositions describe the named parts, not their proofs. The step from (C) to (J) and the step from (H) to (D) are our readings of `jfSmoothBuilt_of_chart` and `jDecayTrQQ_of_open`. `JfSmoothBuilt` is an `abbrev` for `JfSmoothDS` (CutRegFFName.lean, line 5). `modelPlaceBuilt2_of_SSnRep` lives in GaugeConstructionHolds.lean, whose theorem `gauge_construction_holds` is not used in this chain.
