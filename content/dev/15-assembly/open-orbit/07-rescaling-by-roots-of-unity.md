---
title: Rescaling by roots of unity
decls:
  - GlobalTheory.T.true_geometry_row_pair_relation_alt_alt_alt
  - GlobalTheory.Fam.QuadraticExtensionData.dat_exists
  - GlobalTheory.T.true_geometry_row_pair_relation_alt_alt
  - GlobalTheory.Fam.ratDatum_xiOff_common_alt
  - GlobalTheory.T.true_geometry_row_pair_symmetry_alt
  - GlobalTheory.Fam.LocLev.xiLev_eq_const_mul_locFac_alt
  - GlobalTheory.Fam.LocLev.loc_all_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rescaling by roots of unity

This section proves that the level functions $\xi_j$ of a quadratic extension datum that reads become rational after we multiply them by constants $C_j$ that do not depend on the twist index, and after we rescale the characters by roots of unity. The result is the datum condition of [the Theorem on the column side](/entry/true-geometry-family-invariance-alt/), where the constants $C_j$ enter the column constants. The proof has three layers: local factors at the places of the set $P_g$, a rational datum for the part of $\xi_j$ away from the twist places, and the rescaling at the twist places.

We keep the notation of [the previous section](/entry/exists-quadratic-extension-reads-low/). Let $a$ be a geometric family for $W$ and $u$ with local groups $G_1, \dots, G_n$ at the places $v_1, \dots, v_n$ of $P_g$, and let $J$ be a quadratic extension datum for $(a, t)$. For $j + 1 \leq m$, $\beta \in \mathrm{Ch}_0(j)$, $\gamma \in \mathrm{Ch}_0(j + 1)$ and a matrix $z$ over $E$ of size $\mathrm{rk}\, X_{j+1} \times \mathrm{rk}\, X_j$, the function $\xi_j(\beta, \gamma)(z)$ of the tuple data is a product of local terms. At each bad prime $P$ of the tuple there is a local term $\xi_{j, P}(\beta, \gamma)(z)$, and there is a term $\phi_T(\beta, \gamma)(z)$ from the decorations of the base points. Write

$$\xi^{\mathrm{off}}_j(\beta, \gamma)(z) = \phi_T(\beta, \gamma)(z) \prod_{P \in v_G} \xi_{j, P}(\beta, \gamma)(z),$$

where $P$ runs over the bad primes that lie in the set $v_G$ of places of the base data. Then, for a datum that reads,

$$\xi_j(\beta, \gamma)(z) = \xi^{\mathrm{off}}_j(\beta, \gamma)(z) \prod_{i = 1}^{r} \xi_{j, P_i}(\beta, \gamma)(z),$$

with the product over the twist places $P_1, \dots, P_r$ of $Q(t)$. This splitting is proved in another chapter. The places of $v_G$ are exactly the places $v_1, \dots, v_n$ of $P_g$, by the level condition of $W$.

A function $\Xi$ of $z$ is a *local factor* at $v_k$ for a group $H$ if it is a local function at $v_k$ of the kind given by $H$. A pair $(\Xi, f)$ of a function and a finite combination $f$ of Weil vectors is a *rational datum* at an idempotent $e$ of the adeles, relative to the character $\psi$ of $W$ and the vacuum vector $\mathrm{vac}_j$ of $a$; we do not unfold this condition. We say that $e$ is an *idempotent sum* over a set $S$ of places if $e$ is the sum of the idempotents of the places of $S$.

We say that the top matrix of $a$ is the identity if $i_A(r, s) = 1$ for $r = s$ and $0$ otherwise. All the theorems of this section assume this, together with: $W$ satisfies the family conditions on a package, and $a$ is good and true.

**Theorem 4.7.1 (Local factors with uniform constants).** For each place $v_k$ of $P_g$ and each $j$ with $j + 1 \leq m$, there is $c \neq 0$ such that for every twist index $t$, every datum $J$ for $(a, t)$ that reads and all $\alpha \in \mathrm{Ch}(j)$, $\gamma \in \mathrm{Ch}(j + 1)$, there is a local factor $\Xi$ at $v_k$ for the group $G_k$ at level $j$ with

$$\xi_{j, P}(\iota_j \alpha, \iota_{j+1} \gamma)(z) = c \, \Xi(z)$$

for every bad prime $P$ over $v_k$ and every $z$.

Lean: `GlobalTheory.Fam.LocLev.loc_all_alt`.

*Proof.* There are three cases. If $j + 2 < m$ or $j + 2 = m$, two results of another chapter on the finite index of the level subgroups give $c$. If $j + 1 = m$, a row pair identity, proved there as well, gives $c$; this is the only case that uses that the top matrix is the identity. $\square$

The point is that $c$ depends only on $v_k$ and $j$, and not on $t$, $J$, $\alpha$ or $\gamma$.

**Theorem 4.7.2 (Constant times local factors).** There are constants $C'_j$, with $C'_j \neq 0$ for $j < m$, such that for every $t$, every $J$ that reads, every $j$ with $j + 1 \leq m$ and all $\alpha$, $\gamma$, there are local factors $\Xi_k$ at $v_k$ for $G_k$ at level $j$, $k = 1, \dots, n$, with

$$\prod_{P \in v_G} \xi_{j, P}(\iota_j \alpha, \iota_{j+1} \gamma)(z) = C'_j \prod_{k = 1}^{n} \Xi_k(z) \quad \text{for all } z.$$

Lean: `GlobalTheory.Fam.LocLev.xiLev_eq_const_mul_locFac_alt` (also `GlobalTheory.T.true_geometry_row_pair_symmetry_alt`, a second name).

*Proof.* Let $c(k, j)$ be the constants of the previous theorem, and put $C'_j = \prod_{k} c(k, j)$ for $j + 1 \leq m$ and $C'_j = 1$ otherwise. Each $c(k, j)$ is nonzero, so $C'_j \neq 0$ for $j < m$. Given $t$, $J$, $\alpha$ and $\gamma$, take the local factors $\Xi_k$ of the previous theorem. The bad primes of the tuple that lie in $v_G$ are in bijection with the places $v_1, \dots, v_n$ of $P_g$, since a place lies in $v_G$ if and only if it lies in $P_g$, and the places $v_k$ are distinct. Under this bijection the local term at $P$ is $c(k, j)\, \Xi_k(z)$. So the product over $P \in v_G$ is $\prod_k c(k, j) \Xi_k(z) = C'_j \prod_k \Xi_k(z)$. $\square$

**Theorem 4.7.3 (A common rational datum away from the twist places).** There are constants $C_j$, with $C_j \neq 0$ for $j < m$, such that for every $t$, every $J$ that reads, every idempotent sum $e$ over $v_T(u) \cup v_G$, every $j$ with $j + 1 \leq m$ and all $\alpha$, $\gamma$, the pair

$$\Bigl( C_j \, \xi^{\mathrm{off}}_j(\iota_j \alpha, \iota_{j+1} \gamma), \ \mathrm{comb}(d_G(j))\, \mathrm{comb}(d_T(j))\, \mathrm{vac}_j \Bigr)$$

is a rational datum at $e$. Here $v_T(u)$ is the set of type places of $u$, and $d_G(j)$, $d_T(j)$ are the combinations of the commuting vector data of $a$ at the places of $P_g$ and at the type places.

Lean: `GlobalTheory.Fam.ratDatum_xiOff_common_alt` (also `GlobalTheory.T.true_geometry_row_pair_relation_alt_alt`, a second name).

*Proof.* Let $C'_j$ be the constants of the previous theorem and $C_j = (C'_j)^{-1}$. Fix $t$, $J$, $e$, $j$, $\alpha$, $\gamma$ and take the local factors $\Xi_k$.

1. A chain descent result of another chapter gives three properties of the vacuum vectors of $a$ at level $j$: a condition at zero, a local condition and a type condition.
2. Since $a$ is good and true, the lattices $L_j$ and $L_{j+1}$ of $a$ are self-dual and equal to the integral vectors.
3. The type places of $u$ and the places of $P_g$ are disjoint.
4. A twist reduction result of another chapter treats the term $\phi_T$ at each idempotent sum over the type places.
5. With steps 1 to 4 and the standard pin of $a$, a result on rational data and local combinations gives that the pair $\bigl(\phi_T \prod_k \Xi_k, \ \mathrm{comb}(d)\, \mathrm{comb}(d_T(j))\, \mathrm{vac}_j\bigr)$ is a rational datum at $e$, for a combination $d$ built from the local groups $G_k$. The pin of the commuting vector data of $a$ identifies $\mathrm{comb}(d)$ with $\mathrm{comb}(d_G(j))$ on this vector.
6. By the previous theorem, $C_j \xi^{\mathrm{off}}_j = C_j \phi_T \cdot C'_j \prod_k \Xi_k = \phi_T \prod_k \Xi_k$.

So the pair of the theorem is the pair of step 5. $\square$

Now we rescale. For a datum $J$ that reads, recall the local level vectors $E_i.dL_j$ and the weights $\mathrm{wt}_j$, and for a function $s_j$ on $\mathrm{Ch}(j)$ the rescaled level combination

$$dQ_s(j, \alpha, \gamma) = s_j(\alpha)\, s_{j+1}(\gamma)^{-1}\, \mathrm{wt}_j(\alpha) \cdot \mathrm{aconv}\bigl(E_1.dL_j(\alpha_1, \gamma_1), \dots, E_r.dL_j(\alpha_r, \gamma_r)\bigr).$$

For $\beta \in \mathrm{Ch}_0(j)$ let $x_r(j, \beta)$ be the real point of $A$ at $\beta$, so that $\chi_{j+1}(x_r(j, \beta))$ is a complex number of absolute value one, where $\chi_{j+1} = A.\mathrm{chr}(j + 1)$.

**Definition 4.7.4 (Rescaling datum).** Let $C_j$ be constants and $J$ a datum that reads. A *rescaling datum* for $C$ on $J$ is a triple $(s, \zeta, \rho)$ of functions $s_j$ on $\mathrm{Ch}(j)$, $\zeta_j$ on $\mathrm{Ch}(j) \times \mathrm{Ch}(j + 1)$ and numbers $\rho_j$ such that:

1. every $s_j(\alpha)$ and every $\rho_j$ is a root of unity, and $s_0 = 1$;
2. for $j + 1 \leq m$ and all $\alpha$, $\gamma$, the pair
$$\Bigl( C_j \, \mathrm{wt}_j(\alpha)\, \zeta_j(\alpha, \gamma)\, \xi_j(\iota_j \alpha, \iota_{j+1} \gamma), \ \mathrm{comb}(dQ_s(j, \alpha, \gamma))\, \mathrm{comb}(d_G(j))\, \mathrm{comb}(d_T(j))\, \mathrm{vac}_j \Bigr)$$
is a rational datum at the idempotent of $A$;
3. for $j + 1 \leq m$ and all $\alpha$, $\gamma$,
$$\zeta_j(\alpha, \gamma)\, \chi_{j+1}(x_r(j, \iota_j \alpha))\, \chi_{j+1}(x_r(j+1, \iota_{j+1} \gamma))^{-1} = \rho_j.$$

**Theorem 4.7.5 (Rescaling by roots of unity).** There are constants $C_j$, with $C_j \neq 0$ for $j < m$, such that for every $t$ and every datum $J$ for $(a, t)$ that reads, there is a rescaling datum $(s, \zeta, \rho)$ for $C$ on $J$. One can take $\rho = 1$.

Lean: `GlobalTheory.Fam.QuadraticExtensionData.dat_exists` (also `GlobalTheory.T.true_geometry_row_pair_relation_alt_alt_alt`, a second name).

*Proof.* Let $C_j$ be the constants of the previous theorem. Fix $t$ and $J$, and write $\chi_\alpha = \chi_{j+1}(x_r(j, \iota_j \alpha))$ and $\chi'_\gamma = \chi_{j+1}(x_r(j + 1, \iota_{j+1} \gamma))$.

1. By results of another chapter, the idempotent of $A$ is $e_0 + \sum_i e_i$, where $e_0$ is an idempotent sum over $v_T(u) \cup v_G$ and $e_i$ is the idempotent of the place of $G_i$; and $\xi_j$ splits as in the display at the start of the section.
2. A result on the twist places, also proved in another chapter, gives functions $p_j$ on $\mathrm{Ch}(j)$ and $q_j$ on $\mathrm{Ch}(j + 1)$ with the following properties. The numbers $A_j(\alpha) = p_j(\alpha) \chi_\alpha$ and $B_j(\gamma) = q_j(\gamma) (\chi'_\gamma)^{-1}$ are roots of unity for $j < m$. There is a root of unity $c_0$ with $A_0(\alpha) = c_0$ for all $\alpha$. For $j + 1 < m$ there is a root of unity $k_j$ with $B_j(\gamma) A_{j+1}(\gamma) = k_j$ for all $\gamma$. Finally, if $(\Xi, f)$ is a rational datum at $e_0$, then
$$\Bigl( \Xi \cdot p_j(\alpha) q_j(\gamma) \prod_i \xi_{j, P_i}(\iota_j \alpha, \iota_{j+1} \gamma), \ \mathrm{comb}\bigl(\mathrm{aconv}(E_i.dL_j(\alpha_i, \gamma_i))_i\bigr) f \Bigr)$$
is a rational datum at $e_0 + \sum_i e_i$.
3. Put $k_j = 1$ for $j + 1 \geq m$, and $\tilde{c}_j = c_0 \prod_{i < j} k_i$, a root of unity. Define $s_0 = 1$, $s_{j+1}(\gamma) = \tilde{c}_j B_j(\gamma)$ for $j < m$, and $s_{j+1} = 1$ for $j \geq m$. Each $s_j(\alpha)$ is a root of unity.
4. We claim $s_j(\alpha) A_j(\alpha) = \tilde{c}_j$ for $j < m$. For $j = 0$ this is $A_0 = c_0$. If it holds at $j$ and $j + 1 < m$, then
$$s_{j+1}(\gamma) A_{j+1}(\gamma) = \tilde{c}_j B_j(\gamma) A_{j+1}(\gamma) = \tilde{c}_j k_j = \tilde{c}_{j+1}.$$
5. Put $\rho_j = 1$ and $\zeta_j(\alpha, \gamma) = s_j(\alpha) s_{j+1}(\gamma)^{-1} p_j(\alpha) q_j(\gamma)$. For condition 3, let $j + 1 \leq m$; by step 4,
$$\begin{aligned} \zeta_j(\alpha, \gamma)\, \chi_\alpha (\chi'_\gamma)^{-1} &= s_j(\alpha) A_j(\alpha) \cdot B_j(\gamma) \cdot (\tilde{c}_j B_j(\gamma))^{-1} \\ &= \tilde{c}_j B_j(\gamma) (\tilde{c}_j B_j(\gamma))^{-1} = 1. \end{aligned}$$
6. For condition 2, apply step 2 to the rational datum of the previous theorem at $e_0$, with $f = \mathrm{comb}(d_G(j)) \mathrm{comb}(d_T(j)) \mathrm{vac}_j$. By step 1 the first entry is $C_j\, p_j q_j\, \xi_j$. Multiply by the constant $s_j(\alpha) s_{j+1}(\gamma)^{-1} \mathrm{wt}_j(\alpha)$; a rational datum stays rational, and $\mathrm{comb}$ is linear in the combination, so the second entry becomes $\mathrm{comb}(dQ_s(j, \alpha, \gamma)) f$. The first entry becomes $C_j\, \mathrm{wt}_j(\alpha)\, \zeta_j(\alpha, \gamma)\, \xi_j$. $\square$

So the rescaling absorbs the phases $\chi_\alpha$ and $\chi'_\gamma$ of the twist places into the roots of unity $s_j$, and what is left is the uniform constant $C_j$.

**Remark 4.7.6 (Formalization).** The theorems are at [DatExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DatExists.lean#L22), [RatDatumXiOffCommon.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RatDatumXiOffCommon.lean#L22) and [XiLevEqConstMulLocFac.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/XiLevEqConstMulLocFac.lean#L41), with `loc_all_alt` at line 35 and the bijection `prod_bij_alt` at line 21 of the same file. The rescaling datum is `QuadraticExtensionData.Dat` in [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L74) and $\xi^{\mathrm{off}}$ is `xiOff` in [XiEqXiOffMul.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/XiEqXiOffMul.lean#L106). The three second names, in [DatExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DatExistsStatement.lean#L17), [RatDatumXiOffCommonStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RatDatumXiOffCommonStatement.lean#L18) and [XiLevEqConstMulLocFacStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/XiLevEqConstMulLocFacStatement.lean#L18), only pass the hypotheses on; the words "row pair relation" and "row pair symmetry" do not describe the statements. In `dat_exists` the number $\rho_j$ is the constant `fun _ => 1`, so the existence of $\rho$ adds nothing; the rescaling is `chartRescale`. In `loc_all_alt` the case split is `lt_trichotomy (j + 2) B.R.m`, and only the third case, `true_geometry_row_pair_identity_alt`, uses the hypothesis on $i_A$; the other two cases are `true_geometry_finite_index_alt_alt` and `true_geometry_finite_index_alt_alt_alt`. The steps of the proofs above are `true_geometry_twist_quadratic_level_alt`, `true_geometry_twist_quadratic_value_alt`, `true_geometry_row_pair_property_alt`, `true_geometry_chain_descent_alt`, `true_geometry_twist_reduction_alt`, `type_primes_disjoint'` and `rationalDatum_foldr_local_combinations`; we did not open them. We did not unfold `IsRatDatum`, `IsLocFac`, `IsIdemSum`, `comb`, `aconv`, `locXi`, `phiT` or `homOf`.
