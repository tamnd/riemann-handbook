---
title: The fan order ideal and the normalized blowup
decls:
  - GlobalTheory.T.exists_thetaSetup_ideal_over_clopen_component
  - GlobalTheory.Poinc.exists_setup_ideal_over_component
  - GlobalTheory.T.exists_fanOrder_ideal_thetaCompactification
  - GlobalTheory.Poinc.idealSt_holds
  - GlobalTheory.T.normalisedBlowup_ampleDivisor_compactification
  - GlobalTheory.PoincTop.poinSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The fan order ideal and the normalized blowup

The previous section gave, on the rational model $Z_1$ of a theta setup, an ideal sheaf with orders $\iota'\varphi(\beta)$ along traits after pullback to a proper model $Y$. This section first removes $Y$, then moves the ideal sheaf from $Z_1$ to the theta compactification $Z$, one clopen irreducible piece at a time, and glues the pieces. The result is an ideal sheaf $J$ on $Z$, supported on the boundary, with valuation $d\varphi$ along traits. Its normalized blowup $\pi : S \to Z$ is the toroidal compactification: the last theorem of the section shows that $S$ with the divisor $B = \pi^{-1}J$ has all the properties used in the [theorem with polarized charts](/entry/siegel-toroidal-pol-charts/), including ampleness of $\pi^*\mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ for large $k$.

We keep the notation of the previous sections. Fix $g \ge 1$, an odd $n \ge 3$, a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$ with base $s : X \to \operatorname{Spec}\Lambda_n$, a theta compactification $(Z, z, i)$ of $F$, and a polarization function $\varphi$ of rank $g$. The valuation condition along traits is the one of the section on [charts on the normalized blowup](/entry/chart-st5-holds/). For a trait $\mathcal{T}$ we write $V$, $\varpi$, $y$ and $\beta$ for its ring, uniformizer, generic point and form.

**Theorem 9.18.1 (An ideal over a component).** Let $C \subseteq Z$ be clopen and irreducible. Then there are an $8 \times 8$ integer matrix $W$, a theta setup $X_1$ for $(F, W, i)$, an integer $\iota \ge 1$ and an ideal sheaf $J_1$ on $Z_1$ such that:

1. the image of $\pi_1 : Z_1 \to Z$ is $C$;
2. for each $x$ in the support of $J_1$, $\pi_1(x) \notin i(X)$;
3. for each trait $\mathcal{T}$ for $F$ and each $\xi_1 : \operatorname{Spec} V \to Z_1$ with $\pi_1 \circ \xi_1 \circ \iota_V = i \circ y$, there is an integer $a \ge 0$ with $a = \iota\,\varphi(\beta)$ such that $J_1$ generates the ideal $(\varpi^a)$ of $V$ along $\xi_1$.

Lean: `GlobalTheory.Poinc.exists_setup_ideal_over_component` (also `GlobalTheory.T.exists_thetaSetup_ideal_over_clopen_component`, a wrapper).

*Proof.* Since $(Z, z, i)$ is a theta compactification, $z$ is projective, $Z$ is normal, $i$ is an open immersion with dense image, $z \circ i = s$, and there is an $E_8$ matrix $W$ with theta integrality. Since $C$ is clopen and irreducible and $i(X)$ is dense, a lemma on generic points gives a generic point $\eta$ of $X$ whose image $i(\eta)$ has closure $C$. A theorem on the existence of theta setups at generic points gives a theta setup $X_1$ for $(F, W, i)$ whose map $u : \operatorname{Spec} S_R \to X$ sends every point to $\eta$. A lemma on the range of $\pi_1$ then shows that $\pi_1(Z_1) = C$; it uses that $\pi_1$ is finite and that the generic point of $Z_1$ goes to $i(\eta)$. We use only the statements of these three results.

By the theorem on [a normal model with a Cartier divisor](/entry/exists-model-divisor-of-orders/) there are $\iota$, $Y$, $\pi_Y : Y \to Z_1$ and $D$ with properties (1) to (4) of that theorem. A lemma on theta setups shows that $Z_1$ is projective over $o_1$. So the theorem on [descent of a divisor power](/entry/exists-ideal-sheaf-comap-orders/) applies and gives $\iota' \ge 1$ and $J_1$ on $Z_1$ whose pullback $\pi_Y^{-1}J_1 \cdot \mathcal{O}_Y$ has support over the complement of $i(X)$ and orders $\iota'\varphi(\beta)$ along traits into $Y$.

It remains to pass from traits into $Y$ to traits into $Z_1$. We first check homogeneity: for each trait $\mathcal{T}$ and each $k \ge 1$, $\varphi(k\beta) = k\,\varphi(\beta)$. The lattice of $\mathcal{T}$ has rank at most $g$, since the dimension of the abelian part plus the rank of the lattice is $g$. The form $\beta$ is symmetric and positive semidefinite. A polarization function of rank $g$ is homogeneous of degree $1$ on positive semidefinite real forms on such lattices, which gives the claim.

A theorem on orders of ideals on proper models now applies: for a map of rational models $\pi_Y : Y \to Z_1$ with $\pi_Y \circ \mathrm{pt}_Y = \mathrm{pt}_{Z_1}$ that is proper, an ideal sheaf $J_1$ on $Z_1$ whose pullback to $Y$ has the support condition and orders $\iota'\varphi(\beta)$ along traits into $Y$, and homogeneity of $\varphi$ along traits, it gives the support condition (2) for $J_1$ and the orders (3) with $\iota'$ in place of $\iota$. We use only its statement. With $\iota'$ for $\iota$, this proves the theorem. $\square$

The two hypotheses of the orders theorem that go beyond the data are properness of $\pi_Y$ and homogeneity of $\varphi$. Homogeneity is needed because the orders theorem compares a trait into $Z_1$ with traits into $Y$ over extensions of discrete valuation rings, where the form $\beta$ is multiplied by a ramification index, as in the theorem on [proportional forms of traits](/entry/trait-uniq/).

**Theorem 9.18.2 (The fan order ideal).** There are $d \ge 1$ and an ideal sheaf $J$ on $Z$ such that the support of $J$ does not meet $i(X)$ and $J$ has valuation $d\varphi$ along traits through $i$.

Lean: `GlobalTheory.Poinc.idealSt_holds` (also `GlobalTheory.T.exists_fanOrder_ideal_thetaCompactification`, a wrapper, and `GlobalTheory.Poinc.IdealSt`, the statement).

*Proof.* Since $z$ is projective and $Z$ is normal, a lemma on normal projective schemes writes $Z$ as a disjoint union of finitely many clopen irreducible subsets $C_c$. For each $c$, the previous theorem gives $W$, $X_1$, $\iota$ and $J_1$ for $C_c$. A theorem on descent from the theta model to the component then gives $d_c \ge 1$ and an ideal sheaf $J_c$ on $Z$ such that each point of the support of $J_c$ lies in $C_c$ and not in $i(X)$, and such that for each trait $\mathcal{T}$ and $\xi : \operatorname{Spec} V \to Z$ with $\xi \circ \iota_V = i \circ y$ and closed point in $C_c$, there is $a \ge 0$ with $a = d_c\,\varphi(\beta)$ and $J_c$ generates $(\varpi^a)$ along $\xi$. A theorem on gluing ideals over clopen pieces combines the $J_c$ and $d_c$ into one $d \ge 1$ and one ideal sheaf $J$ with the stated properties. We use only the statements of the lemma and the two theorems. $\square$

The ideal $J$ is the ideal used in step 3 of the proof of the [theorem with polarized charts](/entry/siegel-toroidal-pol-charts/), through the next theorem. Its orders along traits are determined by $\varphi$ up to the factor $d$.

**Theorem 9.18.3 (Normalized blowup with an ample twist).** Let $\mathcal{O}_Z(1)$ be an ample line bundle on $Z$. Then there are $d \ge 1$, an ideal sheaf $J$ on $Z$, a scheme $S$ with maps $\pi : S \to Z$ and $j : X \to S$, and an effective Cartier divisor $B$ on $S$ such that:

1. the support of $J$ does not meet $i(X)$, and $J$ has valuation $d\varphi$ along traits through $i$;
2. $\pi$ is a normalized blowup of $J$, and $z \circ \pi$ is projective;
3. $j$ is an open immersion with dense image, $\pi \circ j = i$ and $\pi^{-1}(i(X)) = j(X)$;
4. the ideal sheaf of $B$ is $\pi^{-1}J \cdot \mathcal{O}_S$, and it has valuation $d\varphi$ along traits through $j$;
5. there is $k_0$ such that $\pi^*\mathcal{O}_Z(1)^{\otimes k} \otimes \mathcal{O}(B)^{\vee}$ is ample for each $k \ge k_0$.

Lean: `GlobalTheory.PoincTop.poinSt` (also `GlobalTheory.T.normalisedBlowup_ampleDivisor_compactification`, a wrapper, and `GlobalTheory.Poinc.PoinSt`, the statement).

So $(\pi, j, B)$ are blowup data of order $d$ for $\varphi$, in the sense of the section on charts, with the extra ampleness (5).

*Proof.* The previous theorem gives $d$ and $J$ with (1). Let $U = i(X)$, an open subset of $Z$ since $i$ is an open immersion, and dense. The support of $J$ does not meet $U$. A theorem on normalized blowups over $\Lambda_n$, applied to the projective map $z$, the normal scheme $Z$, the ideal $J$ and the dense open $U$, gives a normalized blowup $\pi : S \to Z$ of $J$ with $z \circ \pi$ projective, an effective Cartier divisor $B$ with ideal sheaf $\pi^{-1}J \cdot \mathcal{O}_S$, such that $\pi$ restricts to an isomorphism $\pi^{-1}(U) \to U$ and $\pi^{-1}(U)$ is dense in $S$. We use only its statement. This gives (2) and the first half of (4).

Let $j$ be the composite of the isomorphism $X \cong U$ given by $i$, the inverse of $\pi^{-1}(U) \cong U$, and the inclusion of the open set $\pi^{-1}(U)$ in $S$. Then $j$ is an open immersion and $\pi \circ j = i$. The first two maps are surjective, so the image of $j$ is $\pi^{-1}(U) = \pi^{-1}(i(X))$, which is dense. This is (3).

For the second half of (4), let $\mathcal{T}$ be a trait and $\xi : \operatorname{Spec} V \to S$ with $\xi \circ \iota_V = j \circ y$. Then $\pi \circ \xi \circ \iota_V = \pi \circ j \circ y = i \circ y$, so by (1) there is $a = d\varphi(\beta)$ with $J$ generating $(\varpi^a)$ along $\pi \circ \xi$. The ideal generated along $\xi$ by $\pi^{-1}J \cdot \mathcal{O}_S$ is the ideal generated along $\pi \circ \xi$ by $J$, so it is also $(\varpi^a)$.

For (5), write $\pi = \pi_0 \circ \nu$ with $\pi_0 : S_0 \to Z$ a blowup of $J$ and $\nu$ finite. The ring $\Lambda_n$ is of finite type over $\mathbb{Z}$, hence noetherian, and it is a domain. A theorem on ample twists of normalized blowups over a noetherian domain then gives $k_0$ such that $\pi^*\mathcal{O}_Z(1)^{\otimes k} \otimes \mathcal{O}(B)^{\vee}$ is ample for $k \ge k_0$; we use only its statement. $\square$

The ampleness in (5) is the usual one for blowups. On the blowup $S_0$ the inverse image of $J$ is $\mathcal{O}_{S_0}(1)$, which is ample relative to $Z$, so $\pi_0^*\mathcal{O}_Z(k) \otimes \mathcal{O}_{S_0}(1)$ is ample for large $k$ (R. Hartshorne, *Algebraic Geometry*, Chapter II, Section 7). The pullback of an ample line bundle along the finite map $\nu$ is ample. In the notation of the theorem, $\mathcal{O}(B)^{\vee} = \mathcal{O}(-B)$ is the ideal sheaf of $B$, the pullback of $\mathcal{O}_{S_0}(1)$.

**Remark 9.18.4 (Formalization).** In `poinSt` the hypothesis that $\mathcal{O}_Z(1)$ is a line bundle is introduced and not used; only its ampleness enters ([NormalisedBlowupAmpleDivisorCompactification.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedBlowupAmpleDivisorCompactification.lean#L18)). The comparison of ideals along $\xi$ and along $\pi \circ \xi$ is `PullAlong.idlAlong_comap_eq`. In `exists_setup_ideal_over_component` the theorem on theta setups at generic points is called with level bound $0$, and its conclusion $0 \le N_S$ is discarded ([ExistsThetaSetupIdealOverClopenComponent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsThetaSetupIdealOverClopenComponent.lean#L22)); the homogeneity of $\varphi$ along traits is proved in the same proof from `Trait.dim_add_rank` and the homogeneity clause of `IsPolFan` (line 28). The orders theorem for proper models is in [IdealOrdersOfProperModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdealOrdersOfProperModel.lean#L19). The statements `IdealSt` and `PoinSt` are definitions of propositions in [IsThetaCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsThetaCompact.lean#L80), and the theorems prove them. The lemmas on partitions, generic points and theta setups, and the theorems on descent to components, gluing, normalized blowups and ample twists, have no entries in this part; we use only their statements.
