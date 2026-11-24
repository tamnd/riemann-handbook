---
title: Volumes and weights
decls:
  - GlobalTheory.T.true_geometry_exists_volume_data_alt
  - GlobalTheory.Fam.vol_level_wt_const_alt
  - GlobalTheory.T.true_geometry_chain_step_value_alt
  - GlobalTheory.PenVol.pen_vol_alt
  - GlobalTheory.T.true_geometry_step_relation_alt
  - GlobalTheory.PenBridge.pen_bridge_alt
  - GlobalTheory.T.true_geometry_chain_step_identity_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Volumes and weights

This section proves that the volume of a level subgroup of a quadratic extension datum, multiplied by the weight of its characters, does not depend on the twist index, on the datum or on the characters. Together with the constants $C_j$ of [the previous section](/entry/dat-exists/), these volume constants $V_j$ and $V_T$ enter the column constants of [the Theorem on the column side](/entry/true-geometry-family-invariance-alt/). The proof at the level $m - 1$ writes each level subgroup as the preimage of a product of local stabilizers under a reduction map, and reads the weights as indices.

We keep the notation of [the section on quadratic extension data](/entry/exists-quadratic-extension-reads-low/). Let $a$ be a geometric family for $W$ and $u$, with lattices $L_j$ in the spaces $X_j$, and with Haar measures $\mathrm{vol}_j$ on $G(X_j)$ and $\mathrm{vol}_T$ on $G(X')$. For a compact open subgroup $U$ we write $\mathrm{vol}_j(U)$ for its level volume, computed with a [[Haar measure|VY0HXD3GC4]], as in [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups). For subgroups $U \leq U_0$ we write $[U_0 : U]$ for the index.

**Definition 4.8.1 (Volume constants).** Let $J$ be a quadratic extension datum for $(a, t)$, with level subgroups $A.U_j(\beta)$ of $G(X_j)$. Let $V_j$ ($j \geq 0$) and $V_T$ be complex numbers. We say that $J$ has *level volumes* $V$ if

$$\mathrm{vol}_j\bigl(A.U_j(\iota_j \alpha)\bigr) \cdot \mathrm{wt}_j(\alpha) = V_j \quad \text{for all } j < m \text{ and } \alpha \in \mathrm{Ch}(j).$$

We say that $J$ has *top volume* $V_T$ if the subgroup $U_T$ of $h \in G(X')$ with $b_T^{-1} h b_T$ in the top level subgroup of the package satisfies $\mathrm{vol}_T(U_T) \cdot \mathrm{wt}_m(\beta) = V_T$ for all $\beta \in \mathrm{Ch}(m)$.

All the theorems of this section assume that $W$ satisfies the family conditions on a package and that $a$ is good and true.

Fix $j$ with $j + 1 = m$, and a datum $J$ that reads. Each local group $G_i$ of $J$ has level $s_i = m - 2$, so $j = s_i + 1$. At this level $G_i$ has a level subgroup $K_i$ of $\mathrm{GL}_N(k_i)$ and the maximal compact subgroup $K_{O, i} = \mathrm{GL}_N(\mathcal{O}_{k_i})$, and $E_i$ gives a coset $E_i.\cos(\alpha_i)$ for each $\alpha_i \in E_i.\mathrm{Ch}(j)$. Let $\mathrm{St}_i(\alpha_i) \leq K_i$ be the stabilizer of this coset in $K_i$, for the block element built from $\varpi^{M}$, where $\varpi$ is the uniformizer of $k_i$ and $M$ the matrix size of $E_i$. A result of the theory of the local data gives

$$[K_{O, i} : \mathrm{St}_i(\alpha_i)] = E_i.\mathrm{wt}_j(\alpha_i),$$

so the local weight at the level $s_i + 1$ is an index.

**Theorem 4.8.2 (The level subgroup as a preimage).** Let $j + 1 = m$. There is a compact subgroup $U_0 \leq G_f(X_j)$ such that for every $t$, every $J$ for $(a, t)$ that reads and every $\alpha \in \mathrm{Ch}(j)$, we have $A.U_j(\iota_j \alpha) \leq U_0$ and

$$[U_0 : A.U_j(\iota_j \alpha)] = \prod_{i = 1}^{r} [K_{O, i} : \mathrm{St}_i(\alpha_i)].$$

Lean: `GlobalTheory.PenBridge.pen_bridge_alt` (also `GlobalTheory.T.true_geometry_step_relation_alt`, a second name).

*Proof.* A relaxed lattice result, proved elsewhere in the development, gives a compact $U_0 \leq G_f(X_j)$ with three properties, for every $J$ that reads. (a) Each $g \in U_0$ moves $L_j$ to itself at the finite places outside the places of $J$. (b) Each $\kappa$ that keeps $L_j$ at those places lies in $U_0$. (c) For each $\alpha$ there are $c_i \in K_i$ such that $g \in A.U_j(\iota_j \alpha)$ if and only if $g \in U_0$ and

$$c_i \, \rho_i(g) \, c_i^{-1} \in \mathrm{St}_i(\alpha_i) \quad \text{for all } i,$$

where $\rho_i : U_0 \to \mathrm{GL}_N(k_i)$ is the reduction at the last level, the matrix of $g$ at the place of $G_i$ in the frame of $L_j$. By (c), $A.U_j(\iota_j \alpha) \leq U_0$. Let $\rho = (\rho_i)_i : U_0 \to \prod_i \mathrm{GL}_N(k_i)$. Then $A.U_j(\iota_j \alpha) = \rho^{-1}\bigl(\prod_i c_i^{-1} \mathrm{St}_i(\alpha_i) c_i\bigr)$. Each $c_i^{-1} \mathrm{St}_i(\alpha_i) c_i$ lies in $K_{O, i}$, since $\mathrm{St}_i(\alpha_i) \leq K_i \leq K_{O, i}$ and $c_i \in K_{O, i}$. We check two properties of $\rho$.

1. $\rho(U_0) \subset \prod_i K_{O, i}$. Since $g \in U_0$ carries the completion of $L_j$ at the place of $G_i$ to itself, its matrix in the frame of $L_j$ at that place is integral and invertible.
2. $\rho : U_0 \to \prod_i K_{O, i}$ is onto. The places of the groups $G_i$ are distinct, since the places $P_i$ of $J$ are distinct. The lattice $L_j$ is self-dual because $a$ is good. Then a result on self-dual lattices gives, for prescribed matrices $x_i \in K_{O, i}$, an element $g$ of the stabilizer of $L_j$ with these matrices at the places of the $G_i$ in the frames of $L_j$. By (b), $g \in U_0$, and $\rho(g) = (x_i)_i$.

For a surjective homomorphism $\rho : U_0 \to \prod_i K_{O, i}$ and subgroups $H_i \leq K_{O, i}$, the index of $\rho^{-1}(\prod_i H_i)$ in $U_0$ is $\prod_i [K_{O, i} : H_i]$. With $H_i = c_i^{-1} \mathrm{St}_i(\alpha_i) c_i$ and $[K_{O, i} : c_i^{-1} \mathrm{St}_i(\alpha_i) c_i] = [K_{O, i} : \mathrm{St}_i(\alpha_i)]$, since $c_i \in K_{O, i}$, this is the claim. $\square$

**Theorem 4.8.3 (Volume at the level below the top).** Let $j + 1 = m$. There is $v \neq 0$ such that for every $t$, every $J$ for $(a, t)$ that reads and every $\alpha \in \mathrm{Ch}(j)$,

$$\mathrm{vol}_j\bigl(A.U_j(\iota_j \alpha)\bigr) \cdot \mathrm{wt}_j(\alpha) = v.$$

Lean: `GlobalTheory.PenVol.pen_vol_alt` (also `GlobalTheory.T.true_geometry_chain_step_value_alt`, a second name).

*Proof.* Take $U_0$ from the previous theorem. Fix $t$, $J$ that reads and $\alpha$, and write $U = A.U_j(\iota_j \alpha)$.

1. By the goodness of the tuple data $A$, the representatives of the chart levels represent the unitary double cosets; in particular $U$ is open. Since $U \leq U_0 \leq G_f(X_j)$ and $U_0$ is compact, the index $[U_0 : U]$ is finite and nonzero, and $\mathrm{vol}_j(U) \cdot [U_0 : U] = \mathrm{vol}_j(U_0)$.
2. By the previous theorem and the index formula for the local weights,
$$[U_0 : U] = \prod_i [K_{O, i} : \mathrm{St}_i(\alpha_i)] = \prod_i E_i.\mathrm{wt}_j(\alpha_i) = \mathrm{wt}_j(\alpha).$$
3. Since $a$ is true, its pin at infinity gives $\mathrm{vol}_j(U) \neq 0$.

By steps 1 and 2, $\mathrm{vol}_j(U)\, \mathrm{wt}_j(\alpha) = \mathrm{vol}_j(U_0)$, which does not depend on $t$, $J$ or $\alpha$. If some $t$ has a datum $J$ that reads with $\mathrm{Ch}(j)$ nonempty, put $v = \mathrm{vol}_j(U_0)$; it is nonzero by step 1 and step 3, as the product of two nonzero numbers. Otherwise put $v = 1$; then there is nothing to prove. $\square$

**Theorem 4.8.4 (Volume constants).** There are complex numbers $V_j$, with $V_j \neq 0$ for $j < m$, and $V_T \neq 0$, such that for every $t$, every datum $J$ for $(a, t)$ that reads has level volumes $V$ and top volume $V_T$.

Lean: `GlobalTheory.Fam.vol_level_wt_const_alt` (also `GlobalTheory.T.true_geometry_exists_volume_data_alt`, a second name).

*Proof.* A volume constant result for true geometries, proved elsewhere in the development, gives $V_T \neq 0$ such that every $J$ that reads has top volume $V_T$. For the levels we take three cases.

1. If $j + 2 \leq m$, a chain step identity at the middle levels gives $V_j \neq 0$ with $\mathrm{vol}_j(A.U_j(\iota_j \alpha))\, \mathrm{wt}_j(\alpha) = V_j$ for every $t$, every $J$ that reads and every $\alpha$. This is stated below.
2. If $j + 1 = m$, the previous theorem gives $V_j = v$.
3. If $j \geq m$, put $V_j = 1$; the condition asks nothing at these levels.

Since every $j < m$ falls in case 1 or 2, $V_j \neq 0$ for $j < m$, and every $J$ that reads has level volumes $V$. $\square$

**Theorem 4.8.5 (Chain step identity).** Let $j + 2 \leq m$. There is $v \neq 0$ such that for every $t$, every $J$ for $(a, t)$ that reads and every $\alpha \in \mathrm{Ch}(j)$,

$$\mathrm{vol}_j\bigl(A.U_j(\iota_j \alpha)\bigr) \cdot \mathrm{wt}_j(\alpha) = v.$$

Lean: `GlobalTheory.T.true_geometry_chain_step_identity_alt`.

*Proof.* This is a result of the middle levels, proved elsewhere in the development; the statement here passes its hypotheses on to it. $\square$

So at the level $m - 1$ the volumes of the level subgroups change with $\alpha$, and the weights compensate exactly.

**Remark 4.8.6 (Formalization).** The theorems are at [VolLevelWtConst.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/VolLevelWtConst.lean#L20), [PenVol.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PenVol.lean#L22) and [PenBridge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PenBridge.lean#L24); the volume conditions `Vol` and `VolT` are at lines 72 and 80 of [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L72). The four second names, at [VolLevelWtConstStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/VolLevelWtConstStatement.lean#L17), [PenVolStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PenVolStatement.lean#L18), [PenBridgeStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PenBridgeStatement.lean#L18) and [VolLevMulWtMidStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/VolLevMulWtMidStatement.lean#L18), only pass the hypotheses on, each under `maxHeartbeats 1000000`; the chain step identity relays `volLev_mul_wt_mid_alt`, which we did not open. `pen_vol_alt` runs under `maxHeartbeats 4000000`. The names "chain step value", "step relation" and "pen" do not describe the statements. In `pen_vol_alt` the case with no datum is `absurd`, with $v = 1$, as in the proof above; in `vol_level_wt_const_alt` the value $V_j = 1$ for $j \geq m$ is a default of a `dite`. The index is Mathlib's `Subgroup.relIndex`, so $[U_0 : U]$ is `U.relIndex U0`. The steps are `true_geometry_lattice_relaxed_alt`, `relIndex_eq_prod_relIndex_of_surjective_pi`, `mem_integralGL_split_place_of_carries_latticeCompletion`, `exists_selfDual_stabilizer_with_prescribed_splitPlace_matrices`, `injective_q_v_of_reads`, `relIndex_comap_conj`, `chartLevels_reps_represent_unitaryDoubleCosets`, `archimedeanLevelVolume_mul_relIndex`, `PinInhab.volLev_ne_zero`, `relIndex_couplingCosetStabilizer_eq_chartWeight` and `exists_volume_constant_of_true_geometry`. We did not unfold `volLev`, `cosStab`, `StepData.box`, `KO`, `reductionHomAtLastLevel`, `Moves` or `InK`.
