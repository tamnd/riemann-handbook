---
title: Column data and link conditions
decls:
  - GlobalTheory.T.true_geometry_family_column_data_alt
  - GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt
  - GlobalTheory.T.cls_pin_d_of_true_family
  - GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW
  - GlobalTheory.T.nonzero_scalars_roots_of_unity_alt
  - GlobalTheory.StepVacForm.main_alt_alt
  - GlobalTheory.T.exists_ne_zero_scalars_gVec
  - GlobalTheory.GVecAt.main_alt_alt
  - GlobalTheory.T.type_data_unit_shift_relation_alt
  - GlobalTheory.MiTop.linkComm_of_laws_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Column data and link conditions

This section proves that a good and true geometric family with a good row choice has a column choice for which the family character satisfies the laws, the chart condition at zero, the link tail condition, the link commutation and the ratio condition. These are five of the conclusions of [the Theorem on family conditions](/entry/fam-all-q-of-all-true-alt/), and the theorem here is its step 5. The column choice comes from [the column side](/entry/col-side-alt/) at family constants that we choose first. Before the main theorem we prove four supporting results: the class data of the family, two results on the scalars of the vector data, and the link commutation.

We keep the notation of [the column side](/entry/col-side-alt/): $a$ is a geometric family for $W$ and $u$, $f = a(\mathrm{row}, \mathrm{col})$, $v$ the commuting vector data, $o$ the type data over $k$, and $m$ the top level.

**Definition 4.10.1 (Conditions on a family character).** Let $f$ be a family character for $W$ and $u$.

1. *Class data* for $f$ are a good real datum $\rho$ for the commutation datum of $f$ such that for each $t$ there are good kernel classes and good top classes for $\rho$ and the tuple $f_t$.
2. The *laws* of $f$ are nine conditions: the commutation datum is good, each tuple is good and locally finite, and the real, value, last value, kernel, period and reading laws hold. We do not unfold the last six.
3. The *chart condition at zero* says that for each $t$ there is $\alpha_0$ with $\mathrm{Ch}_t(0) = \{\alpha_0\}$ and $e_t(0, \alpha_0)$ the point mass at $b_0$, that for each $\varphi$ the column vector $c_t(\varphi)$ at level $0$ of $\varphi$ is ramified and its readings at $\alpha_0$ are those of $\varphi$ in the chart at zero, and that every ramified vector at level $0$ is some $c_t(\varphi)$.
4. The *link tail condition* says that for $2n = m$ the tail of the column at level $2n$ of $c_t(\varphi)$ at a leading linear map $G$ of $F$ equals the period of $u$ at $\varphi$ and the vector $j_A(r_t F)$.
5. *Link commutation* says that for each $n$ with $2n = m$ there are a linear automorphism $S$ of the space of $\varphi$, a real $r > 0$ with $\|S\varphi\| = r \|\varphi\|$ for all $\varphi$, and $s \neq 0$, such that for all $t$, $\varphi$ and $F$,
$$\mathrm{tail}_t\bigl(\mathrm{up}_n\, c_t(\varphi)\bigr)(F) = s \cdot \mathrm{tail}_t\bigl(\mathrm{col}_{2n}\, c_t(S\varphi)\bigr)(F).$$
6. The *ratio condition* says that for $2n = m$ and every $t$, the top constant $c_{\mathrm{Top}}(t, n)$ is nonzero and $c_{\mathrm{Top}}(t, n)/c_{\mathrm{Bot}}(t)$ and $c_{\mathrm{Top}}(\mu_0, n)/c_{\mathrm{Bot}}(\mu_0)$ are $q_t$-unit ratios, where $q_t(p)$ says that $p$ lies in a place of $Q(t)$.

**Theorem 4.10.2 (Class data of a true family).** Let $W$ be a valid real package with standard twists, and let $f$ have a leading reading, good rows and the family column condition. Then $f$ has class data.

Lean: `GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW` (also `GlobalTheory.T.cls_pin_d_of_true_family`, a second name).

*Proof.* Let $c_0$ be the sequence of the family column condition. From the validity of $W$ and its pins, results of another chapter give nonzero jet scales $s$ of the true columns and translates $J$ of the values on frames. The top pin at $\mu_0$ gives the embedding of the top level. The real datum is built from $u$, $f$, $s$ and $J$, and is good by the specification of true columns. For each $t$, the kernel classes come from [the kernel part laws of column pins](/entry/kernel-part-laws-of-column-pins/), using the column pin at $t$ and the lattices of the rows. For the top classes, we read the last space at the level condition of $t$: if $t = \mu_0$ we use the class forms of $u$, and otherwise the standard twist of $W$ at $t$. In both cases the tail coefficient of $f$ is the period of a reading, and the last period gives the top classes with the top pin $(U_T, \varepsilon)$. $\square$

Let $v$ be good commuting vector data tied to $f$, with local groups $G_1, \dots, G_n$ pinned and placed by a bijection $\mathrm{pl}$ onto the places $P_g$ of the package, such that $f$ reads the $G_i$. The *G-vector condition* for scalars $s_j$ says: for $j + 1 < m$, every global divisor $d$ at level $j$, every $P$ and all $a, a'$ in the archimedean group,
$$\omega_Y(\mu_0, j)(a b_j, a' b_{j+1})\, \mathrm{comb}(d)\bigl(\mathrm{vac}_j(P)\bigr) = s_j\, \mathrm{comb}(e_G(j))\bigl(\Psi_j(P, a, a')\bigr),$$
and the same at the top, with $\omega_T$, $(b_{j+1}, b_T)$, $\Psi_T$ and $s_{j+1}$, when $j + 2 = m$. For a tuple $w$ at $t$, the *vector function condition* with scalars $\mathrm{sc}_j$ is the same identity with the operator $\omega_t(j)$ of $f_t$ on the left and $\mathrm{comb}(e_G(j)) \circ \mathrm{comb}(w.eQ_j)$ on the right.

**Theorem 4.10.3 (Scalars of the G-vectors).** Assume the package hypotheses, good rows, and $v$ and $G_i$ as above. Then there are $s_j \neq 0$ satisfying the G-vector condition.

Lean: `GlobalTheory.GVecAt.main_alt_alt` (also `GlobalTheory.T.exists_ne_zero_scalars_gVec`, a second name).

*Proof.* We find for each level a constant $c_j \neq 0$; take $j + 1 < m$, the top case being the same.

1. If there is no global divisor at level $j$, then $c_j = 1$ works, as the condition is empty.
2. Otherwise fix one divisor $d_0$. A local result gives lattices $M, M'$, a combination $o'$ and $\kappa \neq 0$ with $\omega(b_j, b_{j+1})\, \mathrm{comb}(d)(\mathrm{vac}_j) = \kappa\, \mathrm{comb}(o')(g_0)$ for every divisor $d$, where $g_0$ is a vacuum vector.
3. The tie gives $o$ with $\Psi_j(1, 1, 1) = \mathrm{comb}(o)\bigl(\omega(b_j, b_{j+1})\, \mathrm{vac}_j\bigr)$, a vacuum vector at the places of $v$, and nonzero since $v$ does not vanish.
4. Two vacuum vectors for the same lattices are proportional, so $\mathrm{comb}(o')(g_0) = c\, \mathrm{comb}(o)(\dots)$ with $c \neq 0$. Take $c_j = \kappa / c$.
5. The Fock model passes from $P = 1$, $a = a' = 1$ to all $P$, $a$, $a'$.

Set $s_j = c_j$ when $j + 1 < m$, $s_{j+1} = c^T_j$ when $j + 2 = m$, and $s = 1$ otherwise. $\square$

**Theorem 4.10.4 (Vector scalars up to roots of unity).** Under the same hypotheses there are $s_j \neq 0$ such that for each $t$ there are roots of unity $\zeta_t(j)$ with the following property: every tuple $w$ at $t$ whose primes are those under the places of $Q(t)$, whose combinations are supported at these primes, and which satisfies the rational vector condition, satisfies the vector function condition with scalars $s_j \zeta_t(j)$.

Lean: `GlobalTheory.StepVacForm.main_alt_alt` (also `GlobalTheory.T.nonzero_scalars_roots_of_unity_alt`, a second name).

*Proof.* Take $s$ from the previous theorem. A result of another chapter gives descent data along the chain: for each $j$ a global combination $d_G$ and for each $t$ a combination $d_Q$ that realize $\Psi_j$. A second result gives, for each $t$, roots of unity $\zeta_t(j)$ for the Weil tuple at $t$. The primes under $P_g$ and those under $Q(t)$ are disjoint, since the level of the character separates them. A step lemma on the Fock model then combines the factor $s_j$ at the primes of $v$ with the factor $\zeta_t(j)$ at the primes of $w$, giving the scalar $s_j \zeta_t(j)$ at level $j$, and $s_{j+1} \zeta_t(j + 1)$ at the top. $\square$

**Theorem 4.10.5 (Link commutation).** Let $o$ be type data over a local field $k$ with index set $\iota$, let $\varepsilon_j(i)$ be units of the residue field, and let $S_0(t)$ be operators on the columns at level $0$. Assume that the ramified groups are unitary, that the commutation datum is good, and that each $f_t$ is good, has kernel back and tail readings, and lifts and reads $S_0(t)$ for $o$ and $\varepsilon$. Assume that the indices of $o$ have no repetition, that the places of $o$ are distinct, that each $\mathrm{Ch}_t(0)$ is nonempty, that the readings of $c_t(\varphi)$ are those of the chart at zero, and that every ramified vector at level $0$ is some $c_t(\varphi)$. Then $f$ has link commutation.

Lean: `GlobalTheory.MiTop.linkComm_of_laws_alt` (also `GlobalTheory.T.type_data_unit_shift_relation_alt`, a second name).

*Proof.* Fix $n$ with $2n = m$.

1. For each $\eta \colon \iota \to k^\times$ of units, [the scaling of norms by level prime operators at step zero](/entry/level-prime-operators-step-zero-scale-norms/) gives $S_\eta$ and $r_\eta > 0$ with $\|S_\eta \varphi\| = r_\eta \|\varphi\|$, such that the chart readings of $S_\eta \varphi$ are those of $\varphi$ moved by $o.S$ at $\eta$. Its inputs at $\mu_0$ are the readings of $f_{\mu_0}$.
2. For every $t$, $S_0(t, \eta)\, c_t(\varphi) = c_t(S_\eta \varphi)$: the left side is ramified, hence some $c_t(\varphi')$, and the chart at zero is injective.
3. Iterating along $\varepsilon$ gives $S$ and $r > 0$ with $\|S\varphi\| = r\|\varphi\|$. Take $s = o.c_S(n)$, a product of positive real powers of cardinals, so $s \neq 0$.
4. The kernel chain identity of another chapter turns $\mathrm{tail}_t(\mathrm{up}_n\, c_t(\varphi))$ into $s$ times the tail of the column of the iterated $S_0(t)$ at $c_t(\varphi)$, which is $c_t(S\varphi)$ by step 2. $\square$

**Theorem 4.10.6 (Column data).** Assume the discrete series cover, the Harish-Chandra modules and strong approximation for the special unitary group. Let $W$ satisfy the family conditions on a package, $a$ be good and true, and $\mathrm{row}$ be good with all rows of the same shape. Assume that for all family constants $\kappa$ the conclusion of [the column side](/entry/col-side-alt/) holds. Then there is a column choice $\mathrm{col}$ such that $f = a(\mathrm{row}, \mathrm{col})$ has good rows, satisfies the laws, the chart condition at zero and the link tail condition, has link commutation and satisfies the ratio condition.

Lean: `GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt` (also `GlobalTheory.T.true_geometry_family_column_data_alt`, a second name).

*Proof.* We take the steps in order.

1. Every $a(\mathrm{row}, \mathrm{col})$ has good rows. Applying the column hypothesis at trivial constants gives some $\mathrm{col}_0$, and the commutation datum is good by step 1 of [the place laws](/entry/laws-resc-alt/).
2. [The lattice frame pins](/entry/see-saw-lattice-frame-pins-finite-integral-laws/) give $\varepsilon$, $\mathrm{op}$, $r_j$, $e_j$, $c_G$ such that $v_\kappa$ is good, the values of $o$ at $(r_j, e_j)$ are unit ratios, and the value laws follow from a list of conditions on tuples.
3. The previous theorem gives $s_j$ and $\zeta_t(j)$. Let $\kappa$ have these $\varepsilon, \dots, c_G$ and $\mathrm{sc}(t, j) = s_j \zeta_t(j)$, and take $\mathrm{col}$, $w_0$, $w$, $F$ from the column side at $\kappa$.
4. The primes of $w(t)$ are those under the places of $Q(t)$, by the pins and levels of $F(t)$. The vector function condition for $w(t)$ with $\mathrm{sc}(t)$ follows from step 3, applied to the tuple with the primes and combinations of $w_0(t)$.
5. The tuples are good, $w(t)$ satisfies the Weil condition by the rank one Gram result, the $G_i$ read $f_t$, and the rows satisfy the quadratic family level identity. With step 4 and the column output, $w(t)$ satisfies the ten conditions of the vector form for $v_\kappa$.
6. Step 2 gives local finiteness, the value laws and the last value laws. The class data come from the theorem above. The real law holds by the good columns, and the kernel, period and reading laws follow from the class data. So the laws hold.
7. The chart condition at zero is part of the column output. The link tail condition follows from the leading reading of $a$, since the reference tuple at $\mu_0$ is the identity.
8. Link commutation is the previous theorem with the type data of $a$ and $S_0$ from the readings of the column output. Kernel back comes from the kernel classes, as $c_K(t, j) \neq 0$ (a unit ratio has nonzero terms); tail readings come from the top classes, as $c_P(t) \neq 0$; the lift comes from the type data local relation and the shape of $a$. The conditions at level $0$ come from the chart condition at zero.
9. Ratio condition. For $j < m$, $\mathrm{sc}(t, j)/\mathrm{sc}(\mu_0, j)$ is a unit ratio: if $\zeta_t(j)^{n_1} = 1$ and $\zeta_{\mu_0}(j)^{n_2} = 1$, then both $s_j \zeta_t(j)$ and $s_j \zeta_{\mu_0}(j)$ have $n_1 n_2$-th power $s_j^{n_1 n_2}$. The ratio of $c_K$ is a unit ratio by the column output. When $j + 2(\sigma + 1) = m$, the constants $c_I(t, j) \neq 0$ by the measures of $a$, and the identity $c_I(t, j) \prod_i \mathrm{idx}_i(j) = c_I(\mu_0, j)$ gives
$$\frac{w(t).c_Q(j)}{c_I(t, j)\, c_I(t, j + 1)} = \bigl(c_I(\mu_0, j)\, c_I(\mu_0, j + 1)\bigr)^{-1},$$
so this ratio does not depend on $t$. The ratio of $c_T$ is a unit ratio, as $c_T$ is a value of $o$ at a root of unity of the theta twist. A result on factor ratios then gives $c_{\mathrm{Top}}(t, n) \neq 0$ and the unit ratio of $c_{\mathrm{Top}}/c_{\mathrm{Bot}}$. $\square$

**Remark 4.10.7 (Formalization).** The theorems are at [LawsLinksOfGeoRowsCols.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsLinksOfGeoRowsCols.lean#L36), [ClsPinDOfFamCol.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClsPinDOfFamCol.lean#L22), [ExistsIsWeilDatumOOmTAtLast.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsWeilDatumOOmTAtLast.lean#L43), [ImportsBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsBis.lean#L25) and [LinkCommOfLaws.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkCommOfLaws.lean#L29). The second names are relays at [LawsLinksOfGeoRowsColsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsLinksOfGeoRowsColsStatement.lean#L22), [ClsPinDOfFamColStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClsPinDOfFamColStatement.lean#L16), [ExistsIsWeilDatumOOmTAtLastStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsWeilDatumOOmTAtLastStatement.lean#L18), [ImportsBisStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsBisStatement.lean#L18) and [LinkCommOfLawsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkCommOfLawsStatement.lean#L21); the names "type data unit shift relation" and "imports" do not describe the statements. The conditions are `ClsPinD`, `LawsX`, `ChartAtZeroCondition` at [ChartZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ChartZero.lean#L48), `LinkTailCondition` and `LinkCommutes` at [NotMemQBase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NotMemQBase.lean#L29), `FamilyRatioCondition` at [FamAllQ.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQ.lean#L24), and `VectorFunctionCondition` and `GVectorCondition` at [GVec.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GVec.lean#L27). In `lawsLinks_of_geo_rows_cols_alt` strong approximation and the truth of $a$ are taken but not used, the column hypothesis is first applied at dummy constants only to get $\mathrm{col}_0$, and the chart condition at zero is copied from the hypothesis. In `clsPinD_of_famCol_of_trueW` only the lattice field of the good rows is used. In `GVecAt.main_alt_alt` the case with no divisor takes $c = 1$, and the top level is written `j + 2 * 0 + 2`. In `linkComm_of_laws_alt` the hypothesis that every index lies in `o.I` is introduced as `_` and not used. We did not unfold the real, value, last value, kernel, period and reading laws, `ClsK`, `ClsT`, `RealD`, `IsDivisorGlobal`, `RationalVectorCondition`, `LiftS`, `ReadS`, `TDat.cS` or `VForm`.
