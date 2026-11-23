---
title: Canonical families and tautological charts
decls:
  - GlobalTheory.T.degeneratingFamily_data_from_base_algClosed_residue
  - GlobalTheory.VData.exists_divFrom
  - GlobalTheory.T.exists_canonical_family_through_degenerating_family
  - GlobalTheory.UCanon.exists_canon_through
  - GlobalTheory.T.exists_tautological_chart_versality
  - GlobalTheory.UCanon.exists_taut_through
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Canonical families and tautological charts

This section puts each monomial family through a *tautological chart*: a monomial family over a chart ring $k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ of Section 1 whose parameters are the coordinates $u_i$, and which has the open classification, injectivity and rigidity properties of a chart. The lower base of Section 10 gives the abelian part and its parameters. A *canonical family* is then the family of Mumford's construction over a power series ring over the lower base, with the parameters $s_i$ as new variables. The family that we start with is a specialization of the canonical family. We use the notation of Sections 1, 2 and 10. $V$ is a local domain that is a Mumford base, and $(t, P, y, s, \delta)$ is a monomial family over $V$ with $s = (s_1, \dots, s_m)$ and character lattice $X_P$. We write $l'$ for the lower level.

**Definition 7.11.1 (Data from a lower base).** Let $L$ be a lower base for $D'$ with ring $W$, map $b$ and degeneration data $Q$ with lattice $X_Q$. Let $Q_V$ be degeneration data over $V$ with lattice $X_V$, $\iota : W \to V$ a ring map, $s : I \to V$ a finite family, $\varepsilon : I \to$ forms on $X_Q$, and $e : X_V \to X_Q$ an $\mathcal{O}_E$-isomorphism. Then $Q_V$ *comes from $L$ through $\iota$, $s$, $\varepsilon$ and $e$* if there is $g : X_V \to (\operatorname{Frac} V)^\times$ such that:

1. the rescaling of $Q_V$ by $g$ is the pullback along $\iota$ of the data $Q$ with points $c(M' y)$ in place of $c(y)$;
2. $g(y)^{-1} = \prod_{k \in I} s_k^{M' \varepsilon_k(e y, w_0 e y)}$ for each $y \in X_V$;
3. the isomorphism of item 1 induces $e$ on the lattices and respects the action of $\mathcal{O}_E$ on the abelian parts.

Lean: `GlobalTheory.UCanon.DivFrom`.

**Theorem 7.11.2 (Data of a family from a lower base).** Suppose that the residue field of $V$ is algebraically closed and $X_P \ne 0$. Then there are a Hermitian datum $D'$ with $p' + r = p$ and $q' + r = q$ for $r = \operatorname{rank}_{\mathcal{O}_E} X_P$, a lower base $L$ for $D'$, a local map $\theta_0 : W \to V$ with $\theta_0 \circ b = (F \to V)$, an integer $N$, a $\mathbb{Z}$-basis $(\varepsilon_k)_{k \in \{1..m\} \sqcup \{1..N\}}$ of the balanced forms on $X_Q$, an isomorphism $e : X_P \to X_Q$ and a family $s'$ on $\{1..m\} \sqcup \{1..N\}$ in $V$, such that:

1. $\delta_i(a, b) = \varepsilon_i(ea, eb)$ for $i \le m$;
2. $s'_i$ is associated to $s_i$ for $i \le m$, and $s'_k$ is a unit for the other indices;
3. the degeneration data of $P$ come from $L$ through $\theta_0$, $s'$, $\varepsilon$ and $e$.

Lean: `GlobalTheory.VData.exists_divFrom` (also `GlobalTheory.T.degeneratingFamily_data_from_base_algClosed_residue`, a second name).

*Proof.* As $X_P \ne 0$, its rank is at least $1$.

1. The theorem on the lower datum of a family in Section 10 gives $Z$, $D'$, $f$, an object $o'$ over $V$ and $\varphi_B$, with $p' = p - r$ and $q' = q - r$. Since $r \le \min(p, q)$, this gives $p' + r = p$ and $q' + r = q$. Since $\varphi_B$ is a pullback of groups over the identity, it is an isomorphism $i$ from the abelian part of $P$ onto the group of $o'$, and $i$ respects the action of $\mathcal{O}_E$.
2. The integer $M'$ is a unit in $F$, so it is a unit in $V$. Since $V$ is henselian with algebraically closed residue field, a lemma on abelian schemes with a module action gives additive $\mathcal{O}_E$-linear points $x'$ of $o'$ with $x'(y)$ related to the points $c(y)$ of $P$ through $i$ and the integer $M'$.
3. [The theorem on lower bases of linear points](/entry/lower-datum-object-comes-from-base-of-linear-points/) of Section 10, for $o'$ and $x'$, gives $L$, $\theta_0$, $e$ and a map of objects $m$.
4. The cone $\delta$ is part of a basis $b$ of the balanced forms on $X_P$. Its image under $e$ is the basis $\varepsilon$, and so $\delta_i = e^* \varepsilon_i$.
5. A lemma on the periods of monomial families over a base, applied with the isomorphism $\varphi_B \circ m \circ i$ of abelian parts, gives $s'$ with properties 2 and 3. $\square$

**Definition 7.11.3 (Canonical family, passing through).** Let $R$ be a local domain and $C_1 = (t_1, P_1, y_1, s^1, \delta^1)$ a monomial family over $R$ with $m$ parameters.

1. A *canonical structure* on $C_1$ consists of $D'$ with $p' + r = p$ and $q' + r = q$, a lower base $L$ for $D'$, $N$, a basis $\varepsilon$ of balanced forms on $X_Q$ indexed by $\{1..m\} \sqcup \{1..N\}$, an isomorphism $e : X_{P_1} \to X_Q$ with $\delta^1_i = e^* \varepsilon_i$, and a ring map $\psi : W[x_1, \dots, x_m, z_1, \dots, z_N] \to R$ that is complete at the variables. The map $\psi$ is local on $W$, $\psi \circ b$ is the map $F \to R$ of $C_1$, $\psi(x_i) = s^1_i$, each $\psi(z_k)$ is a unit, and the data of $P_1$ come from $L$ through $\psi|_W$, $\psi(x, z)$, $\varepsilon$ and $e$.
2. Let $C$ be a monomial family over $V$ and $\theta : R \to V$ a ring map. Let $R_s = R[1/\prod_i s^1_i]$. Then $C$ *passes through* $C_1$ along $\theta$ if there are $y_o : \operatorname{Spec} R_s \to X_F$ and $\kappa : \operatorname{Spec} \operatorname{Frac} V \to \operatorname{Spec} R_s$ such that $y_o$ restricts to $y_1$ at each generic point over $R$, $\kappa$ lies over $\operatorname{Spec} \theta$, and $y_o \circ \kappa$ is the point $y$ of $C$.

Lean: `GlobalTheory.UCanon.Canon` (also `GlobalTheory.UCanon.Through`).

**Theorem 7.11.4 (Canonical family through a family).** Suppose that the residue field of $V$ is algebraically closed and $X_P \ne 0$. Then there are a field $k$, integers $m, e$, a monomial family $C_1$ over the chart ring $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ with a canonical structure, and a local map $\theta : R \to V$, such that $C_1$ has $m$ parameters with $s^1_i = u_i$, and $C$ passes through $C_1$ along $\theta$.

Lean: `GlobalTheory.UCanon.exists_canon_through` (also `GlobalTheory.T.exists_canonical_family_through_degenerating_family`, a second name).

*Proof.* There are eight steps.

1. The theorem on data from a lower base gives $D'$, $L$, $\theta_0$, $N$, $\varepsilon$, $e$ and $s'$. For $i \le m$, $s'_i$ is a nonzero element of the maximal ideal, since it is associated to $s_i$.
2. A factorization lemma for toric chart rings factors $\operatorname{ev}_{s'} : W[x, z] \to V$, the map $\theta_0$ on $W$ and $s'$ on the variables, as $\theta \circ \psi$. Here $\psi : W[x, z] \to R$ is complete at the variables, $R$ is a chart ring with $\psi(x_i) = u_i$, and $\theta$ is local.
3. The map $W \to R$ is flat between domains, so it is injective. The chart ring is a Mumford base, and it has characteristic $0$ because $F$ maps to it.
4. The elements $\psi(z_k)$ are units, because their images $s'_k$ in $V$ are units and $\theta$ is local.
5. For each $y \ne 0$ in $X_Q$, each $\varepsilon_i(y, y)$ with $i \le m$ is at least $0$, since the $\delta_i$ form a cone, and their sum is positive, since the periods of $P$ are monomial and not units.
6. A lemma on Mumford families over regular bases builds degeneration data $P_1$ over $R$ from $L$ with periods monomial in $\psi(x, z)$ with exponents $M' \varepsilon$, a datum $t_1$, and the data of item 1 of the definition.
7. A lemma on classification over the open set $R_s$ gives $y_1$, $y_o$ and $\kappa$, since $C$ specializes from the family over $R$ along $\theta$.
8. The cone condition on $\delta^1 = e^* \varepsilon$ moves from $\delta$ along the equivalence of balanced forms. This assembles $C_1$ and its canonical structure. $\square$

**Definition 7.11.5 (Tautological chart).** Let $C_1$ be a monomial family over a chart ring $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$. Then $C_1$ is a *tautological chart* if:

1. it has $m$ parameters with $s^1_i = u_i$;
2. (*open classification*) the datum $t_1$ on $R_s = R[1/\prod u_i]$ is classified by a point $y_o : \operatorname{Spec} R_s \to X_F$ that restricts to $y_1$;
3. (*injectivity*) two injective local maps $R \to R'$ to a Mumford base that give the same point of $X_F$ over $\operatorname{Frac} R'$ are equal;
4. (*rigidity*) the data are rigid in the sense of Section 1, and *point rigid*: for each ring map $\mathrm{ev} : R \to K$ to an algebraically closed field and each algebraically closed $k_0 \subseteq K$ that embeds in the algebraic closure of the residue field, if the data are separated at $\mathrm{ev}$ over $k_0$ as in Section 2, then $\mathrm{ev}$ kills the maximal ideal and takes values in $k_0$;
5. the residue field of $R$ is essentially of finite type over $F$, and $m + e + \operatorname{trdeg}_F \kappa(R) = n_D$;
6. the periods of $P_1$ are monomial in an extension of $s^1$ by units, with exponents $M'$ times a basis of balanced forms that extends $\delta^1$.

It is a *tautological chart with rigid coordinates* if, in addition, the extension of item 6 can be chosen with point rigidity for the extended family.

Lean: `GlobalTheory.UChart.IsTaut` (also `GlobalTheory.UCanon.IsTautB`, `GlobalTheory.UCanon.HasRigidCoords`, `GlobalTheory.UChart.OpenCls`, `GlobalTheory.UChart.Inj`, `GlobalTheory.UChart.PointRigid`, `GlobalTheory.UCanon.PointRigidB`).

[The theorem on canonical families that are tautological charts](/entry/canonical-family-is-point-rigid-tautological-chart/) says that, for $p + q \ge 1$ and $\varphi$ a polarized fan with no self-intersections in rank at most $\min(p, q)$, each canonical family over a chart ring with $s^1_i = u_i$ is a tautological chart with rigid coordinates.

**Theorem 7.11.6 (Tautological chart through a family).** Let $p + q \ge 1$ and $\varphi$ a polarized fan with no self-intersections in rank at most $\min(p, q)$. Let $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ be separating blowup data with $j$ separating for $\varphi$. Suppose that the residue field of $V$ is algebraically closed, $X_P \ne 0$, and $\xi_V : \operatorname{Spec} V \to S$ satisfies $j \circ y = \xi_V$ on $\operatorname{Spec} \operatorname{Frac} V$. Then there are $k$, $m$, $e$, a tautological chart $C_1$ with rigid coordinates over $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$, a map $\xi : \operatorname{Spec} R \to S$ with $j \circ y_1 = \xi$ on $\operatorname{Spec} \operatorname{Frac} R$, and a local map $\theta : R \to V$ with $\xi \circ \operatorname{Spec} \theta = \xi_V$.

Lean: `GlobalTheory.UCanon.exists_taut_through` (also `GlobalTheory.T.exists_tautological_chart_versality`, a second name).

*Proof.* The theorem on canonical families through a family gives $C_1$, its canonical structure, and $\theta$ with $s^1_i = u_i$, $\theta$ local, and $C$ passing through $C_1$ along $\theta$. The theorem on canonical families that are tautological charts makes $C_1$ a tautological chart with rigid coordinates. A lemma on tautological charts and separating blowup data gives $\xi : \operatorname{Spec} R \to S$ with $j \circ y_1 = \xi$ on the generic point. It remains to prove $\xi \circ \operatorname{Spec} \theta = \xi_V$.

The scheme $S$ is projective over $F$, so it is separated. Two maps from the spectrum of a domain to a separated scheme are equal if they agree on a dominant map to it, for example the map from the spectrum of the field of fractions. So it is enough to compare $\xi \circ \operatorname{Spec} \theta$ and $\xi_V$ on $\operatorname{Spec} \operatorname{Frac} V$. Since $\prod u_i \ne 0$, the ring $R_s$ is a domain with the same field of fractions as $R$. On $\operatorname{Spec} R_s$ the map $\xi$ is $j \circ y_o$, because both agree at the generic point. Since $C$ passes through $C_1$ along $\theta$, the map $\operatorname{Spec} \operatorname{Frac} V \to \operatorname{Spec} R$ factors through $\kappa$ into $\operatorname{Spec} R_s$. So $\xi \circ \operatorname{Spec} \theta$ at the generic point of $V$ is $j \circ y_o \circ \kappa = j \circ y$, which is $\xi_V$ there. $\square$

**Remark 7.11.7 (Formalization).** The proofs are in [DegeneratingFamilyDataFromBaseAlgClosedResidue.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegeneratingFamilyDataFromBaseAlgClosedResidue.lean#L16), [ExistsCanonicalFamilyThroughDegeneratingFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCanonicalFamilyThroughDegeneratingFamily.lean#L28) and [ExistsTautologicalChartVersality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartVersality.lean#L38). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. `DivFrom`, `Canon`, `PointRigidB`, `HasRigidCoords`, `IsTautB` and `Through` are in [HasRigidCoords.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidCoords.lean#L76), at lines 76, 89, 113, 118, 126 and 129. `OpenCls`, `Inj`, `PointRigid` and `IsTaut` are in [ExistsMonoFamNontrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMonoFamNontrivial.lean#L119), at lines 119, 133, 139 and 144. Item 5 of the tautological chart compares a cardinal sum with `Dw.dim`. `PointRigid` and `PointRigidB` have the hypothesis that $k_0$ embeds in the algebraic closure of the residue field (line 139). In `exists_taut_through` the hypotheses $p + q \ge 1$, `IsPolFan` and `NoSelfInt` are only passed to `T.canonicalFamily_isPointRigid_tautologicalChart` and `UChart.taut_exists_map`, and the separatedness of $S$ is read from the projectivity in the hypothesis `UPoinOnX` as `hU.2.2.2.2.1.2.1` (line 44). The helper lemmas for the last step are at lines 14 to 32. In `exists_canon_through` injectivity of $W \to R$ comes from `injective_of_flat_of_isDomain` (line 17). The proofs apply `T.abelian_scheme_module_action_homomorphism`, `T.exists_periods_monomialFamily_coords_over_base`, `T.exists_toricChartRing_factorisation_localHom`, `T.mumford_family_from_regular_base_coordinates`, `T.classified_on_open_of_specialises_to_classified` and `UChart.taut_exists_map`. They have no entries in this chapter, and we use only their statements. The forms of item 6 and of `HasRigidCoords` are the same, so `IsTautB` adds only `PointRigidB` for the extended parameters. We have not unfolded `IsComplAt`, `IsPullDeg`, `mulDeg`, `IsMonomial`, `TauIn`, `SepAt`, `SepAtB` or `IsRigid` beyond Sections 1 and 2.
